#!/usr/local/bin/perl
BEGIN{ $| = 1;open(STDERR,">&STDOUT"); }
# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
#require 'data/ffadventure.ini';

# チャットログファイル
$chat_file = "datalog/chatloog.cgi";
# チャット表示数
$max_chat = 18;
# メッセージ保存数
$mes_max = 100;
# 最大メッセージサイズ(半角文字数)
$mes_size = 120;
# IDでのチャット制限(荒らし対策)
$shut_id[0] = "test";
$shut_id[1] = "unnko";
$shut_host[0] = "118.22.98";
$shut_host[1] = "110.67.181";
$shut_host[2] = "111.217.192";
# チャットにレベル表示させるか(Yes:1 NO:0)
$clvh = 0;
# フォントサイズ(推奨2)
$fsize = 2.5;
# 背景色を指定
$bgcolor = "#000011";
# 文字色を指定
$text = "#aaaaff";

# このファイル用設定
$backgif = $sts_back;
$midi = $sts_midi;
#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

#--------------#
#　メイン処理　#
#--------------#
if ($mente) {
	&error("バージョンアップ中です"); 
}
&decode;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("アクセスできません！！");
	}
}

&chat;

#----------------#
#--チャット画面--#
#----------------#
sub chat {

	&all_data_read;

	&get_time(time());

	if ($in{'tch'} =~ m/[^0-9]/){
		&chat_error("チャンネルに数字以外の文字が含まれています。"); 
	}

	if($in{'chattime'} and $in{'mes'}) {

		$now_mes = length($in{'mes'});

		foreach (@ban_word) {
			if(index($in{'mes'},$_) >= 0) {
				&chat_error("暴\言は禁止されています");
			}
		}

		if ($now_mes > $mes_size) {
			&chat_error("メッセージが長すぎます！半角で$mes_size文字までです！(現在文字数：$now_mes)<br>");
		}

		foreach (@shut_id) {
			$_ =~ s/\*/\.\*/g;
			if ($in{'id'} =~ /$_/) {
				&chat_error("発言を禁止されています");
			}
		}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);

		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;
		$year = $year +1900;
		$kyo="$year$mon$mday";

		open(IN,"datalog/meslog/$kyo.cgi");
		@chat_mes2 = <IN>;
		close(IN);

		@zenkai = split(/<>/,$chat_mes[0]);
		#@zenkai2 = split(/<>/,$chat_mes[1]);
		#$koktime=time();
		#if(($koktime-$zenkai2[6])<60 and $in{'mes'}){&chat_error("クールタイムです。");}
		if($zenkai[0] ne $in{'id'} or $zenkai[3] ne $in{'mes'}){

		$mes_sum = @chat_mes;
		
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		if($in{'tch'}){$tch=$in{'tch'};}
		elsif($in{'tch2'}){$tch=$in{'tch2'};}
		elsif($in{'tch3'}){$tch=$in{'tch3'};}
		#if(!$tch){&chat_error("メインチャットは現在使用できません。");}
		unshift(@chat_mes,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");
		unshift(@chat_mes2,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");
		open(OUT,">datalog/meslog/$kyo.cgi");
		print OUT @chat_mes2;
		close(OUT);

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);
		
		}

		&unlock($lock_file,'MS');

	}

	&header;

	open(IN,"$chat_file");
	@CHAT_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@CHAT_LOG){
		($hid,$hname,$htime,$hmessage,$hhost,$clv,$tch,$sasa,$bakuhatu) = split(/<>/);
		if ($max_chat < $i) {
			last;
		}
	$foncolor=$text;$foncolort=$text;$foncolors=$text;$foncoloru=$text;

	if($in{'chan'} and $in{'chan'}==$tch){
		$kchn=1;
		$foncoloru="red";
	}elsif($sasa and $sasa eq $in{'name'}){
		$kchn=2;
		$foncoloru="yellow";$fonmes="(From $hname)";
	}elsif($in{'chan2'} and $in{'chan2'}==$tch){
		$kchn=3;
		$foncoloru="pink";
	}else{
		$kchn=0;
		$foncolors=$text;$fonmes="";
	}
	if($hname and $hname eq $in{'name'} and $sasa){
		$foncolort="yellow";
		$fonmest="(To $sasa)";
	}else{
		$foncolort=$text;
		$fonmest="";
	}
if($foncoloru ne $text){$foncolor=$foncoloru;}
elsif($foncolors ne $text){$foncolor=$foncolors;}
elsif($foncolort ne $text){$foncolor=$foncolort;}
		print <<"EOM";
<font color="$foncolor">
EOM
if($in{'tch'}==$tch or $kchn==1 or $kchn==3){
if(!$sasa or $kchn==2 or $hid eq $in{'id'}){
if(!$clvh) { print "<font size=\"$fsize\"><b>$hname</b>>>「$fonmes$fonmest$hmessage」$htime\</font>\n";
}else { print "<font size=\"$fsize\"><b>$hname(Lv.$clv)</b>>>「$hmessage」$htime\</font>\n"; }
	print <<"EOM";
<br></font>
EOM
}}
		$hit=1;$i++;
	}
	if(!$hit) { print "<hr size=0><font color=$text>メッセージはありません</font>\n"; }
	print <<"EOM";
<hr size=0>
<!--削除禁止-->
<center>FFA CHAT by <a href="http://wsr.a-auc.jp/" target="_blank">Right-Blue</a></center>
</body></html>
EOM
	exit;
}

#--------------#
#--エラー処理--#
#--------------#
sub chat_error {

	&header;
	print "<center><h3><b>Ｗａｒｎｉｎｇ！！</b></h3>\n";
	print "<font color=red><B>$_[0]</B></font><br><br>\n";
	print "<font size=2><b>発言/更新ボタンを押してください</b></font></center>\n";
	print "</body></html>\n";
	exit;
}