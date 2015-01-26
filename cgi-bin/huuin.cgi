#!/usr/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
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
<form action="huuin.cgi" method="post">
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

	$hit=0;
	foreach (@syoku_master) {if($_ >= 100){$hit++;}}

	&header;

	print <<"EOM";
<h1>封印の間</h1><hr>
封印の条件：<br>
①？？？？<br>
②？？？？<br>
③？？？？<br>
<font color="red" size=5>
封印は現在、(副)管理人のシナちゃんがテスト中です。<br>
今後、消えてなくなる可\能\性も高いです。<br>
管理人多忙の中ですが、できればやってみたい程度の感じの試み…。
</font><br>
<form action="huuin.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[131] or !$chara[132] or !$chara[133]) {
		print "封印の条件を満たしていません\n";
	}elsif ($chara[127]!=2) {
		print "封印の条件を満たしていません。\n";
	}elsif($chara[4] ne "双風シナ") {
		print "封印の条件を満たしていません。$hit\n";
	}else{
		print "<input type=\"submit\" class=btn value=\"封印\">\n";
	}
	
	print <<"EOM";
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
#------------#
# 　封　印　 #
#------------#
sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;
#-----------------------------------------------------条件を満たしているかチェック
#	if($tenseiryoukin>$chara[19]){&error("条件を満たしていません。");}
#-----------------------------------------------------職業データの消去
#	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
#	&lock($lock_file,'SK');
#	&syoku_load;

#	$num = @syoku_master;

#	for($i=0;$i<=$num;$i++){
#		$syoku_master[$i] = 0;
#	}
#	&syoku_regist;
#	&unlock($lock_file,'SK');

	&get_host;
#-----------------------------------------------------アイテム・ペットの消去
#	$lock_file = "$lockfolder/item$in{'id'}.lock";
#	&lock($lock_file,'IM');
#	&item_load;

#	&item_lose;

#	&def_lose;

#	&acs_lose;

#	&pet_lose;

#	&souko_lose;

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[61]){
			if($array[5] eq $chara[0] and $array[6]){
				$lock_file = "$lockfolder/$array[6].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[6].cgi");
				$member2_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[6].lock";
				&unlock($lock_file,'DR');
				@mem2 = split(/<>/,$member2_data);
				$array[1]=$mem2[4];
				$solv=$mem2[18]+$mem2[37]*100;
				$array[2]=$solv;
				$array[3]-=1;
				splice(@array,5,1);
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}elsif($array[5] eq $chara[0]){
				splice(@member_data,$i,1);
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
			elsif($array[6] eq $chara[0]){splice(@array,6,1);$hit=1;}
			elsif($array[7] eq $chara[0]){splice(@array,7,1);$hit=1;}
			if($hit){
				$array[3]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array =~ s/\n//;
				$new_array .= "\n";
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}

#	&item_regist;
#	&unlock($lock_file,'IM');

#-----------------------------------------------------ステータスリセット
	if ($chara[33]) {
		$chara[16] = $kiso_hp;
		$chara[15] = $chara[16];
		$chara[17] = 0;
		$chara[18] = 1;
#		$chara[19] = 1;
#		$chara[24] = 0;
#		$chara[29] = 0;
#		$chara[31] = 0;
#		$chara[34] = 0;
		$chara[37] = 0;
		$chara[35] = 20;
#		$chara[51] = 0;
#		$chara[52] = 0;
#		$chara[53] = 0;
#		$chara[54] = 0;
#		$chara[55] = 0;
#		$chara[56] = 0;
#		$chara[57] = 0;
#		$chara[58] = 0;
#		$chara[59] = 0;
		$chara[61] = "";
#		$chara[97] = "";
#		$chara[98] = "";
#		$chara[99] = "";
#		$chara[100] = "";
		$chara[7] = 1;
		$chara[8] = 1;
		$chara[9] = 1;
		$chara[10] = 1;
		$chara[11] = 1;
		$chara[12] = 1;
#		$chara[13] = 4;
		$chara[70] = 2;
		$chara[14]= 41;
		$chara[33] = 1;
		$chara[140] = 0;
#		$chara[71] = 0;
#		$chara[72] = 0;
#		$chara[73] = 0;
#		$chara[74] = 0;
#		$chara[75] = 0;
#		$chara[76] = 0;
#		$chara[77] = 0;
#		$chara[78] = 0;
#		$chara[79] = 0;
#		$chara[80] = 0;
#		$chara[81] = 0;
#		$chara[82] = 0;
	}
#-----------------------------------------------------告知
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

	$boss="<font color=\"yellow\">$chara[4]様が封印され、$chara_syoku[$chara[14]]となりました。</font>";
	
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<>$boss<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');
#-----------------------------------------------------レジスト・ヘッダー
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	
#-----------------------------------------------------表示
	print <<"EOM";
<h1> 封印しました。</h1><hr size=0><br>
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
