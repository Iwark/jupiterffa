#!/usr/bin/perl

#------------------------------------------------------#
#　本スクリプトの著作権はいくにあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
#  FF ADVENTURE(いく改)
#　edit by いく
#　http://www.eriicu.com
#　icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#------------------------------------------------------#
# 転生の神殿 edit by 霧雨
# http://cgi-games.com/drop/
#------------------------------------------------------#
#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。         #
# 2. 設置に関する質問はサポート掲示板にお願いいたします。       #
#    直接メールによる質問は一切お受けいたしておりません。       #
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#---------------------------------------------------------------#

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# syoku_regist呼び出し
require 'battle.pl';

# shopfooter呼び出し
require 'item.pl';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

# 転生に必要な料金の倍率(転生回数×？万倍)
$tenseibairitu = 100;

# 転生に必要なレベルの設定
$tenseilevel = 100;

#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

#--------------#
#　メイン処理　#
#--------------#
if ($mente) {
	&error("バージョンアップ中です。２、３０秒ほどお待ち下さい。m(_ _)m");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="tensei.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}

if ($mode) { &$mode; }
&tensyoku;

exit;

#------------#
# 転職の神殿 #
#------------#
sub tensyoku {

	&chara_load;

	&chara_check;

	&syoku_load;

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

$mitensyoku.="現在転生できるまだマスターしていない職業は<br><table><tr>";
$tensyokuok.= "現在転生できる職業は<br><table><tr>";

	$i=0;$hit=0;$mhit=0;
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {
		$tensyokuok.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
		$selection.="<option value=\"$i\">$chara_syoku[$i]</option>\n";
		$hit+=1;
			if($hit % 5 == 0){$tensyokuok.="</tr><tr>";}
			if ($syoku_master[$i] < 100) {
				$mitensyoku.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
				$mhit+=1;
				if($mhit % 5 == 0){$mitensyoku.="</tr><tr>";}

			}
		}
		$i++;
	}
	if(!$hit) { $tensyokuok.= "<td>ありません</td>"; }
	if(!$mhit) { $mitensyoku.="<td>ありません</td>"; }

	&header;

	if (!$chara[37]) { $chara[37] = 0; }
	$tenseiryoukin = 1000000 * $chara[37];

	print <<"EOM";
<h1>転生の神殿</h1><hr>
ここでは転生ができます。転生するには$tenseiryoukin\Gとレベルが$tenseilevel必要です。<br>
※ 転生するとレベルが1になり、経験値・能\力値がリセット、職業がランダムに変わります。<br>
料金は転職と転生の回数×100万Gです。ステータスポイントが転職と転生の回数×20ポイント増えます。<br>
EOM
if($chara[70]<1){
	print <<"EOM";
$tensyokuok</tr></table><br>
$mitensyoku</tr></table><br>
EOM
}
	print <<"EOM";
<form action="tensei.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[21]) {
		print "準備中です。\n";
	}elsif ($chara[19]<$tenseiryoukin) {
		print "お金が足りません。\n";
	}elsif ($chara[70]>=2) {
		print "転生できません。\n";
	}elsif($chara[18]>=100 and $chara[33]>=100) {
		print "<input type=\"submit\" class=btn value=\"転生する\">\n";
	}else{
		print "レベルが足りません。\n";
	}
	
	print <<"EOM";
</form>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステータス画面へ">
</form>
EOM

	&footer;

	exit;
}

sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$tenseiryoukin = 1000000 * $chara[37];

	if($chara[33]<$tenseilevel) {&error("レベルが足りません");}

	if($tenseiryoukin>$chara[19]){&error("お金が足りません");}
	else{$chara[19] -= $tenseiryoukin;}

	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$syoku_master[$chara[14]] = $chara[33];

	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;

if($chara[70]!=1){
	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$i=0;$hit=0;@ten_sei=();
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {$hit++;}
		$i++;
	}
}else{
	open(IN,"$syoku2_file");
	@syoku = <IN>;
	close(IN);

	$hit=0;
	foreach (@syoku) {
		if($chara[37] >= $_){$hit++;}
	}
}
	$ksyoku = int(rand($hit + 1));
if($chara[70]!=1){
	$hit=0;$i=0;@ten_sei=();
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {$hit++;}
		if($ksyoku == $hit){$chara[14]=$i;last;}
		$i++;
	}
}else{
	$hit=0;$i=0;
	foreach (@syoku) {
		$shit=0;
		if($chara[37] >= $_){
			if($chara[37] >= $_){$hit++;}
		}
		if($ksyoku == $hit){$chara[14]=$i;last;}
		$i++;
	}
}
	if ($master_tac) { $chara[30] = 0; }
	$chara[33] = $syoku_master[$chara[14]];

	if (!$chara[33]) { $chara[33] = 1; }

	if ($chara[33]) {
		if($chara[70]!=1){
			$chara[16] = $kiso_hp + int(rand($chara[37]*100));
			$chara[15] = $chara[16];
			$chara[17] = 0;
			$chara[18] = 1;
			$chara[35] = 20 * $chara[37];
			$chara[7] = 1;
			$chara[8] = 1;
			$chara[9] = 1;
			$chara[10] = 1;
			$chara[11] = 1;
			$chara[12] = 1;
		}
		$chara[37] += 1;
		$chara[13] += 1;
	}

	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;
	$year = $year +1900;

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$boss="$chara[4]様が$chara_syoku[$chara[14]]に転生しました";
	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$boss</span>";

	unshift(@CLOG,"kokuti<>告知<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<>$boss<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	
	$next_ex = $chara[18] * $lv_up;

	print <<"EOM";
<h1> 転生が終了しました</h1><hr size=0><br>
レベル : $chara[18]<br>
職業 : $chara_syoku[$chara[14]]<br>
経験地 : $chara[17] / $next_ex<br>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM

	&shopfooter;

	&footer;

	exit;
}
