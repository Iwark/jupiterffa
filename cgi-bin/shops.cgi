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
<form action="shops.cgi" method="post">
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
#  アイテム表示  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"$item_file");
	@log_item = <IN>;
	close(IN);

	open(IN,"$def_file");
	@log_def = <IN>;
	close(IN);

	open(IN,"$acs_file");
	@log_acs = <IN>;
	close(IN);

	open(IN,"$pet_file");
	@log_pet = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold) = split(/<>/);
		if($chara[24] eq "$si_no"){ $hit=1;last; }
	}
	if(!$hit) {$si_name="素手";$si_dmg="0";$si_gold="0";}
	if($chara[24]==1400){
		$hit=0;
		$si_name=$item[0];
		$si_dmg=$item[1];
	}
	$hitd=0;
	foreach(@log_def){
		($di_no,$di_name,$di_dmg,$di_gold) = split(/<>/);
		if($chara[29] eq "$di_no"){ $hitd=1;last; }
	}
	if(!$hitd) {$di_name="普段着";$di_dmg="0";$di_gold="0";}

	$hita=0;
	foreach(@log_acs){
		($a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($chara[31] eq "$a_no"){ $hita=1;last; }
	}

	if(!$hita) {$a_name="なし";$a_gold="0";$a_ex = "-";}

	$hitp=0;
	foreach(@log_pet){
		($pi_no,$pi_name,$pi_gold,$pi_exp,$pi_hp,$pi_damage,$pi_image,$ps) = split(/<>/);
		if($chara[38] eq "$pi_no"){ $hitp=1;last; }
	}
	if(!$hitp) {$pi_name="なし";$pi_exp="0";$pi_gold="0";$pi_hp="0";$pi_damage="0";}

	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($si_gold / 4) * 3;
		$udi_gold = int($di_gold / 4) * 3;
		$uai_gold = int($a_gold / 4) * 3;
	}else{
		$ui_gold = int($si_gold / 3) * 2;
		$udi_gold = int($di_gold / 3) * 2;
		$uai_gold = int($a_gold / 3) * 2;
	}
	$upi_gold = int($pi_gold / 3) * 2;
	if ($pi_no==3000){$upi_gold = $pi_gold;}

	open(IN,"$item_folder");
	@item_array = <IN>;
	close(IN);

	open(IN,"$def_folder");
	@def_array = <IN>;
	close(IN);

	open(IN,"$acs_folder");
	@acs_array = <IN>;
	close(IN);

	open(IN,"$pet_folder");
	@pet_array = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";$si_dmg += $item[20];}
	if($item[22]){$bogulv="+ $item[22]";$di_dmg += $item[22];}

	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}

	&header;

	print <<"EOM";
<h1>商店街</h1>
<hr size=0>

<FONT SIZE=3>
<B>商店街のマスター</B><BR>
「いらっしゃい！武器、防具、装飾品、そして魔法、さらにペットの卵、スキルと、いろいろと揃ってるよ～。<BR>
　あ、なんだい、<B>$chara[4]</B>じゃないか。元気にしてたかい？
<BR>
　まあ、ゆっくり見ていってくれ。
<BR><BR>そうそう！最近装備品の下取りもはじめたんだ。」<br>
</FONT>
EOM
if($chara[18]>200){
	print <<"EOM";
<br>
<form action="stshops.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="裏商店街へ"></td>
</form>
EOM
}
	print <<"EOM";
<br><hr>現在の所持金：$chara[19] Ｇ<br>
現在の魔法 NO：$chara[59]<br>
現在のペットスキルNO：$chara[47]
<table>
<tr>
<th></th><th></th><th>なまえ</th><th>HP,威力,説明</th><th>売値</th></tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の武器</th><th>$si_name $bukilv</th><th>$si_dmg</th><th>$ui_gold</th>
</tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_sell>
EOM
if ($hitd) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の防具</th><th>$di_name $bogulv</th><th>$di_dmg</th><th>$udi_gold</th>
</tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_sell>
EOM
if ($hita) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の装飾品</th><th>$a_name</th><th>$a_ex</th><th>$uai_gold</th>
</tr>
<tr>
<form action="./shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=pet_sell>
<input type=submit class=btn value="売る">
</th></form><th>現在のペット</th><th>$pename</th><th>HP $pi_hp,攻撃力 $pi_damage</th><th>$upi_gold</th>
</tr>
</table>
<table>
<tr>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $igold) {
			print "<input type=radio name=item_no value=\"$ino\">";
		} else {
			print "×";
		}
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="武器を買う">
</form>
</td>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@def_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $igold) {
			print "<input type=radio name=item_no value=\"$ino\">";
		} else {
			print "×";
		}
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_buy>
<input type=submit class=btn value="防具を買う">
</form>
</td>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@acs_array) {
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($ai_no eq "0015"){
			if($chara[70]==1){
				print "<tr><td class=b1 align=\"center\">\n";
				if ($chara[19] >= $ai_gold) {
					print "<input type=radio name=item_no value=\"$ai_no\">";
				} else {
					print "×";
				}
				print "</td><td align=right class=b1>$ai_no</td><td class=b1>$ai_name</td><td align=right class=b1>$ai_msg</td><td align=right class=b1>$ai_gold</td>\n";
				print "</tr>\n";
			}
		}elsif($ai_no eq "0016"){
		}else{
			print "<tr><td class=b1 align=\"center\">\n";
			if ($chara[19] >= $ai_gold) {
				print "<input type=radio name=item_no value=\"$ai_no\">";
			} else {
				print "×";
			}
			print "</td><td align=right class=b1>$ai_no</td><td class=b1>$ai_name</td><td align=right class=b1>$ai_msg</td><td align=right class=b1>$ai_gold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_buy>
<input type=submit class=btn value="装飾品を買う">
</form>
</td>
<td>
<form action="./shops.cgi" method="post">
<table>
EOM

	foreach (@pet_array) {
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
<input type=hidden name=mode value=pet_buy>
<input type=submit class=btn value="卵を買う">
</form>
</td>
</tr>
</table>
EOM
if ($chara[55]==3 or $chara[56]==3 or $chara[57]==3 or $chara[58]==3){
	print <<"EOM";
	<form action="./shops.cgi" method="post">
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
	<th>黒魔法サンダーを放ちます。命中力小アップ。</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=8>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>008</th><th>サンダラ</th><th>75000G</th>
	<th>黒魔法サンダラを放ちます。命中力中アップ。</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=9>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>009</th><th>サンダガ</th><th>200000G</th>
	<th>黒魔法サンダガを放ちます。命中力大アップ。</th></tr>

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
	<form action="./shops.cgi" method="post">
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
	<form action="shops.cgi" method="post">
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
	<form action="./shops.cgi" method="post">
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
	<form action="./shops.cgi" method="post">
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
if ($chara[38]>3100) {
	print <<"EOM";
<form action="./shops.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=pps_buy>
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
<br><br>ペットを持ってないのでペットスキルは買えません。
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

	open(IN,"$item_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($chara[19] < $i_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("武器倉庫がいっぱいです！$back_form");
	}

	push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>武器屋のマスター</B><BR>
「毎度あり～！<br>
買った武器はあんたの武器倉庫に送っておいたよ！
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

	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($chara[24] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if(!$chara[24]) { &error("そんなアイテムは存在しません"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[24] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&item_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name $bukilvを売りました</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub def_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$def_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($d_no,$d_name,$d_dmg,$d_gold,$d_hit) = split(/<>/);
		if($in{'item_no'} eq "$d_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($chara[19] < $d_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $d_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $def_max) {
		&error("防具倉庫がいっぱいです！$back_form");
	}

	push(@souko_item,"$d_no<>$d_name<>$d_dmg<>$d_gold<>$d_hit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SD');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>防具屋のマスター</B><BR>
「毎度あり～！<br>
買った防具はあんたの防具倉庫に送っておいたよ！
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
sub def_sell {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$def_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($chara[29] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if(!$chara[29]) { &error("そんなアイテムは存在しません"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[29] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&def_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name $bogulvを売りました</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub acs_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$acs_folder");
	@acs_array = <IN>;
	close(IN);
	if($in{'item_no'} eq "0015" and $chara[83]==1){$item2_no="0016";$chara[83]=0;}
	else{$item2_no=$in{'item_no'};}
	$hit=0;
	foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($item2_no eq "$ai_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($chara[19] < $ai_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ai_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("装飾品倉庫がいっぱいです！$back_form");
	}

	push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);
	&unlock($lock_file,'SA');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>装飾品屋のマスター</B><BR>
「毎度あり～！<br>
買った装飾品はあんたの装飾品倉庫に送っておいたよ！
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
sub acs_sell {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$acs_file");
	@acs_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@acs_array){
		($i_no,$i_name,$i_gold) = split(/<>/);
		if($chara[31] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if(!$chara[31]) { &error("そんなアイテムは存在しません"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[31] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&acs_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_nameを売りました</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

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

sub pet_buy {

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
sub pet_sell {
	

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
sub pps_buy {

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
