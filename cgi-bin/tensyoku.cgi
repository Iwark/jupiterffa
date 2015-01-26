#!/usr/bin/perl --

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

#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した	#
#    いかなる損害に対して作者は一切の責任を負いません。		#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。	#
#    直接メールによる質問は一切お受けいたしておりません。	#
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
$tenseibairitu = 50;

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
<form action="$script_tensyoku" method="post">
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

$mitensyoku.="現在転職できるまだマスターしていない職業は<br><table><tr>";
$tensyokuok.= "現在転職できる職業は<br><table><tr>";

	$i=0;$hit=0;$mhit=0;
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		($ten) = split(/<>/);
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		if($chara[37] >= $ten){
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
		}
		$i++;
	}
	if(!$hit) { $tensyokuok.= "<td>ありません</td>"; }
	if(!$mhit) { $mitensyoku.="<td>ありません</td>"; }

	&header;

	$tensyokuryoukin = $chara[37] * 500000;

	print <<"EOM";
<h1>転職の神殿</h1><hr>
ここでは転職ができます。転職するには$tensyokuryoukin Gとレベル$tenseilevelが必要です。<br>
※ 転職するとレベルが1になり、経験値・能\力値がリセットされます。<br>
料金は転職と転生の回数×50万Gです。ステータスポイントが転職と転生の回数×20ポイント増えます。<br>
$tensyokuok</tr></table><br>
$mitensyoku</tr></table><br>
<form action="$script_tensyoku" method="post">
<select name=syoku>
<option value="no">選択してください
$selection
</select>
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[21]) {
		print "準備中です。\n";
	}elsif ($chara[19]<$tensyokuryoukin) {
		print "お金が足りません。\n";
	}elsif($chara[18]>=$tenseilevel) {
		print "<input type=\"submit\" class=btn value=\"転職する\">\n";
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

#--------#
#  転職  #
#--------#
sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'syoku'} eq 'no') {
		&error("職業を選択してください。$back_form");
	}

	$tensyokuryoukin = $chara[37] * 500000;

	if($chara[19] < $tensyokuryoukin){&error("お金が足りません$back_form");}
	else{$chara[19] -= $tensyokuryoukin;}
	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$syoku_master[$chara[14]] = $chara[33];

	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;

	$chara[14] = $in{'syoku'};
	if ($master_tac) { $chara[30] = 0; }	# 転職後の戦術クリア
	$chara[33] = $syoku_master[$chara[14]];

	if (!$chara[33]) { $chara[33] = 1; }

		$chara[16] = $kiso_hp + int(rand($chara[37]*100));
		$chara[15] = $chara[16];
		$chara[17] = 0;
		$chara[18] = 1;
		$chara[37] += 1;
		$chara[35] = 20 * $chara[37];
		$chara[7] = 1;
		$chara[8] = 1;
		$chara[9] = 1;
		$chara[10] = 1;
		$chara[11] = 1;
		$chara[12] = 1;
		$chara[13] += 1;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

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

	$boss="$chara[4]様が$chara_syoku[$chara[14]]に転職しました";
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

	print <<"EOM";
<h1>$chara_syoku[$chara[14]]に転職しました</h1><hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
