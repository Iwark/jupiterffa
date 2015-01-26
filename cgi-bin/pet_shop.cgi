#!/usr/local/bin/perl

#------------------------------------------------------#
#　本スクリプトの著作権は下記の3人にあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
#　FF ADVENTURE 改i v2.1
#　programed by jun-k
#　http://www5b.biglobe.ne.jp/~jun-kei/
#　jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#　FF ADVENTURE v0.21
#　programed by CUMRO
#　http://cgi.members.interq.or.jp/sun/cumro/mm/
#　cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(改) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(いく改)
#　remodeling by いく
#　http://www.eriicu.com
#　icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。     	#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    直接メールによる質問は一切お受けいたしておりません。   	#
#---------------------------------------------------------------#
# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# アイテムライブラリの読み込み
require 'item.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="./pet_shop.cgi" method="post">
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
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  ペット表示　  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"$pet_file");
	@log_item = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_gold,$si_exp,$si_hp,$si_damage,$si_image,$ps) = split(/<>/);
		if($chara[38] eq "$si_no"){ $hit=1;last; }
	}

	if(!$hit) {
		$si_name="なし";
		$si_exp="0";
		$si_gold="0";
		$si_hp="0";
		$si_damage="0";
	}
	$ui_gold = int($si_gold / 3) * 2;
	if ($si_no==3000){$ui_gold = $si_gold;}


	open(IN,"$pet_folder");
	@item_array = <IN>;
	close(IN);

	open(IN,"$pet_folder");
	@ps_array = <IN>;
	close(IN);
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	&header;

	print <<"EOM";
<h1>ペットショップ</h1>
<hr size=0>

<FONT SIZE=3>
<B>ペットショップの店員</B><BR>
「いらっしゃい！ここではね、ペットの卵が買えるんですよ！<BR>
　あ、なんだい、<B>$chara[4]</B>じゃないか。元気にしてたかい？
<BR>
　ふふ、最近<B>ペットスキル</B>も入荷したんだよ、買っていくかい？スキルは１つまでだぞ！
<BR><BR>そうそう！卵は１つしか持てないが卵の引き取りはできるよ。
<br>戦闘中は卵を壊さないように注意するんだぞ！万が一壊れたらこっちで引き取るのにお金がかかるぞ。」
</FONT>
<br><hr>現在の所持金：$chara[19] Ｇ<br>
<table>
<tr>
<th></th><th></th><th>No.</th><th>なまえ</th><th>HP</th><th>攻撃力</th><th>価格</th></tr>
<th>
<form action="./pet_shop.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) {
	if ($si_no==3000){print "<input type=submit class=btn value=\"渡す\">";}
	else{print "<input type=submit class=btn value=\"売る\">";}
}
	print <<"EOM";
</th></form><th>現在のペット</th><th>$pename</th><th>$si_hp</th><th>$si_damage</th><th>$ui_gold</th></tr></table>
<form action="./pet_shop.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$igold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
		if($ino == 3007){
			if($chara[31] eq "0032"){
				print "<tr><td class=b1 align=\"center\">\n";
				print "<input type=radio name=item_no value=\"$ino\">";
				print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td class=b1>$i_hp</td><td class=b1>$i_damage</td><td align=right class=b1>$igold</td>\n";
				print "</tr>\n";
			}
		}else{
			print "<tr><td class=b1 align=\"center\">\n";
			if ($chara[19] >= $igold and $chara[70]!=1) {
				print "<input type=radio name=item_no value=\"$ino\">";
			} else {
				print "×";
			}
			print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td class=b1>$i_hp</td><td class=b1>$i_damage</td><td align=right class=b1>$igold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="卵を買う">
</form>
EOM

if ($chara[38]>3100) {
	print <<"EOM";
現在のペットスキルNO：$chara[47]
<form action="./pet_shop.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<table>
<tr>
<th></th><th>No.</th><th>スキル</th><th>値段</th><th>発動率</th><th>効果</th></tr>
<th>
EOM
if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=1>";}
else{print "×";}
	print <<"EOM";
</th>
<th>001</th><th>ヒーリング</th><th>50000G</th><th>２５％</th>
<th>キャラを回復してくれます。</th></tr>

<th>
EOM
if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=2>";}
else{print "×";}
	print <<"EOM";
</th>
<th>002</th><th>\大\暴\れ</th><th>50000G</th><th>１０％</th>
<th>\大\暴\れして大ダメージ。</th></tr>

<th>
EOM
if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=3>";}
else{print "×";}
	print <<"EOM";
</th>
<th>003</th><th>\幻\影\</th><th>100000G</th><th>５０％</th>
<th>\幻\影\を発動し、回避力ＵＰ。</th></tr>

<th>
EOM
if ($chara[19] >= 500000) {print "<input type=radio name=ps_no value=19>";}
else{print "×";}
	print <<"EOM";
</th>
<th>004</th><th>クロスカウンター</th><th>500000G</th><th>３０％</th>
<th>相手の攻撃を避けて、倍の威力で攻撃！！</th></tr>

</table>
<br><br>
<input type=submit class=btn value="スキルを買う">
</form>
EOM
}else{
	print <<"EOM";
<br><br>ペットを持ってないのでスキルは買えません。
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub item_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$pet_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	if($chara[38]>3000){ &error("既に現在持っています！$back_form"); }
	foreach(@item_array){
		($i_no,$i_name,$i_gold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません$back_form"); }
	if($chara[19] < $i_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;

	$chara[38] = $i_no;
	$chara[39] = $i_name;
	$chara[40] = 0;
	$chara[41] = $i_exp;
	$chara[42] = $i_hp;
	$chara[43] = $i_hp;
	$chara[44] = $i_damage;
	$chara[45] = $i_image;
	$chara[46] = 1;
	$chara[47] = $ps;
	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ペットショップの店員</B><BR>
「毎度あり～！<br>
愛着を持って育てることが重要だぞ！戦闘で死んだら壊れるかもしれないから注意だぞ！
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム売る  #
#----------------#
sub item_sell {
	

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_gold,$i_exp,$i_hp,$i_image,$ps) = split(/<>/);
		if($chara[38] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません$back_form"); }
	if(!$chara[38]) { &error("そんなアイテムは存在しません$back_form"); }
	if($i_no==3000){
		if($chara[19] < 30000) { &error("お金が足りません$back_form"); }
	}
	$ui_gold = int($i_gold / 3) * 2;
	if ($i_no==3000){$ui_gold = $i_gold;}
	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[38] = 0;
	$chara[39] = "なし";
	$chara[40] = 0;
	$chara[41] = 0;
	$chara[42] = 0;
	$chara[43] = 0;
	$chara[44] = 0;
	$chara[45] = 0;
	$chara[46] = 0;
	$chara[47] = 0;
	$chara[138] ="";
	&chara_regist;
	&header;
if ($si_no=3000){
	print <<"EOM";
<h1>$i_nameを引き取ってもらいました</h1>
<hr size=0>
EOM
}else{
	print <<"EOM";
<h1>$i_nameを売りました</h1>
<hr size=0>
EOM
}
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  　スキル買う  #
#----------------#
sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("買いたいスキルを選んでください$back_form"); }

	if ($in{'ps_no'}==1){$ps_gold = 50000;}
	if ($in{'ps_no'}==2){$ps_gold = 50000;}
	if ($in{'ps_no'}==3){$ps_gold = 100000;}
	if ($in{'ps_no'}==19){$ps_gold = 500000;}

	if($chara[19] < $ps_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[47] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ペットショップの店員</B><BR>
「毎度あり～！<br>
仮にスキルを元々持ってたなら、そいつは忘れちまったがな！ワハハ」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
