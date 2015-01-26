#!/usr/local/bin/perl

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

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

		if ($now_mes > $chat_size) {
			&res("メッセージが長すぎます！半角で$mes_size文字までです！(現在文字数：$now_mes)<br>");
		}

		foreach (@shut_id) {
			$_ =~ s/\*/\.\*/g;
			if ($in{'id'} =~ /$_/) {
				&chat_error("発言を禁止されています");
			}
			if ($in{'id'} == "3333") {
				&chat_error("発言を禁止されています");
			}
		}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);

		$mes_sum = @chat_mes;

		if($mes_sum > $mes_max) { pop(@chat_mes); }
		if($in{'tch'}){$tch=$in{'tch'};}
		elsif($in{'tch2'}){$tch=$in{'tch2'};}
		unshift(@chat_mes,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	}

	&header;

	open(IN,"$chat_file");
	@CHAT_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@CHAT_LOG){
		($hid,$hname,$htime,$hmessage,$hhost,$clv,$tch,$sasa) = split(/<>/);
		if ($max_chat < $i) {
			last;
		}
$foncolor=$text;$foncolort=$text;$foncolors=$text;$foncoloru=$text;
if($in{'chan'} and $in{'chan'}==$tch){$kchn=1;}elsif($sasa and $sasa eq $in{'name'}){$kchn=2;}else{$kchn=0;}
if($kchn==1){$foncoloru="red";}elsif($kchn==2){$foncoloru="yellow";$fonmes="(From $hname)";}else{$foncolors=$text;$fonmes="";}
#if($in{'chan'} and $in{'chan'}==$tch){$fonmest="(ch$tch)";}else{$fonmest="";}
if($hname and $hname eq $in{'name'} and $sasa){$foncolort="yellow";$fonmest="(To $sasa)";}else{$foncolort=$text;$fonmest="";}
if($foncoloru ne $text){$foncolor=$foncoloru;}
elsif($foncolors ne $text){$foncolor=$foncolors;}
elsif($foncolort ne $text){$foncolor=$foncolort;}
		print <<"EOM";
<font color="$foncolor">
EOM
if($in{'tch'}==$tch or $kchn==1){
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