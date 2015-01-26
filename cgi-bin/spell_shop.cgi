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
<form action="./spell_shop.cgi" method="post">
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

	&item_load;

	&header;

	print <<"EOM";
<h1>スペルショップ</h1>
<hr size=0>

<FONT SIZE=3>
<B>スペルショップの店員</B><BR>
「<B>$chara[4]</B>か。元気にしてたかい？<BR>
ここの品物、あなたに使えこなせるかどうか・・・。」
</FONT>
<br><hr>現在の所持金：$chara[19] Ｇ<br>
現在の魔法 NO：$chara[59]<br>
EOM
if ($chara[55]==3 or $chara[56]==3 or $chara[57]==3 or $chara[58]==3){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>黒魔法</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=1>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>001</th><th>ファイア</th><th>50000G</th>
	<th>黒魔法ファイアを放ちます。ダメージ小ＵＰ。</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=2>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>002</th><th>ファイラ</th><th>75000G</th>
	<th>黒魔法ファイラを放ちます。ダメージ中ＵＰ。</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=3>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>003</th><th>ファイガ</th><th>200000G</th>
	<th>黒魔法ファイガを放ちます。ダメージ大ＵＰ。</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=4>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>004</th><th>ブリザド</th><th>50000G</th>
	<th>黒魔法ブリザドを放ちます。相手ダメージ小ダウン。</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=5>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>005</th><th>ブリザラ</th><th>75000G</th>
	<th>黒魔法ブリザラを放ちます。相手ダメージ中ダウン。</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=6>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>006</th><th>ブリザガ</th><th>200000G</th>
	<th>黒魔法ブリザガを放ちます。相手ダメージ大ダウン。</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=7>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>007</th><th>サンダー</th><th>50000G</th>
	<th>黒魔法サンダーを放ちます。相手回避小ダウン。</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=8>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>008</th><th>サンダラ</th><th>75000G</th>
	<th>黒魔法サンダラを放ちます。相手回避中ダウン。</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=9>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>009</th><th>サンダガ</th><th>200000G</th>
	<th>黒魔法サンダガを放ちます。相手回避大ダウン。</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="黒魔法を買う">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>あなたは「黒魔法装備」がないので黒魔法は買えません。
EOM
}
if ($chara[55]==13 or $chara[56]==13 or $chara[57]==13 or $chara[58]==13){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>白魔法</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=11>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>011</th><th>ヒール</th><th>50000G</th>
	<th>白魔法ヒールを放ちます。</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=12>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>012</th><th>ヒールラ</th><th>100000G</th>
	<th>白魔法ヒールラを放ちます。</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=13>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>013</th><th>ヒールガ</th><th>200000G</th>
	<th>白魔法ヒールガを放ちます。</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="白魔法を買う">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>あなたは「白魔法装備」がないので白魔法は買えません。
EOM
}
if ($chara[55]==27 or $chara[56]==27 or $chara[57]==27 or $chara[58]==27){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>忍術</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=21>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>021</th><th>分身</th><th>50000G</th>
	<th>忍術分身を放ちます。</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="忍術を買う">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>あなたは「忍術装備」がないので忍術は買えません。
EOM
}
if ($chara[55]==31 or $chara[56]==31 or $chara[57]==31 or $chara[58]==31){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>赤魔法</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=31>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>031</th><th>ドレイン</th><th>50000G</th>
	<th>赤魔法ドレインを放ちます。</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="赤魔法を買う">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>あなたは「赤魔法装備」がないので赤魔法は買えません。
EOM
}
if ($chara[55]==35 or $chara[56]==35 or $chara[57]==35 or $chara[58]==35){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>時魔法</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=41>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>041</th><th>スロウ</th><th>50000G</th>
	<th>時魔法スロウを放ちます。</th></tr>
	<tr><th>
EOM
	if ($item[0] eq "闇封じの剣" and $item[3] eq "闇の羽衣" and $item[6] eq "闇の衣"){
		if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=43>";}
		else{print "×";}
		print <<"EOM";
		</th>
		<th>043</th><th>ダークメテオ</th><th>100000000G</th>
		<th>時魔法奥義メテオを放ちます。</th></tr>
EOM
	}
		print <<"EOM";
	</table>
	<br><br>
	<input type=submit class=btn value="時魔法を買う">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>あなたは「時魔法装備」がないので時魔法は買えません。
EOM
}
	$new_chara = $chara_log;
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
	if ($in{'ps_no'}==2){$ps_gold = 75000;}
	if ($in{'ps_no'}==3){$ps_gold = 200000;}
	if ($in{'ps_no'}==4){$ps_gold = 50000;}
	if ($in{'ps_no'}==5){$ps_gold = 75000;}
	if ($in{'ps_no'}==6){$ps_gold = 200000;}
	if ($in{'ps_no'}==7){$ps_gold = 50000;}
	if ($in{'ps_no'}==8){$ps_gold = 75000;}
	if ($in{'ps_no'}==9){$ps_gold = 200000;}
	if ($in{'ps_no'}==11){$ps_gold = 50000;}
	if ($in{'ps_no'}==12){$ps_gold = 100000;}
	if ($in{'ps_no'}==13){$ps_gold = 200000;}
	if ($in{'ps_no'}==21){$ps_gold = 50000;}
	if ($in{'ps_no'}==31){$ps_gold = 50000;}
	if ($in{'ps_no'}==41){$ps_gold = 50000;}
	if ($in{'ps_no'}==43){$ps_gold = 100000000;}
	if($chara[19] < $ps_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[59] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>スペルショップの店員</B><BR>
「毎度あり～！<br>
仮に魔法を元々持ってたなら、もうないよ！ハハ」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
