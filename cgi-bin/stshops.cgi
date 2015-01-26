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
<form action="stshops.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
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

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

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

	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($si_gold / 4) * 3;
		$udi_gold = int($di_gold / 4) * 3;
		$uai_gold = int($a_gold / 4) * 3;
	}else{
		$ui_gold = int($si_gold / 3) * 2;
		$udi_gold = int($di_gold / 3) * 2;
		$uai_gold = int($a_gold / 3) * 2;
	}

	open(IN,"data/item/stitem.ini");
	@item_array = <IN>;
	close(IN);

	open(IN,"data/def/stdef.ini");
	@def_array = <IN>;
	close(IN);

	open(IN,"data/def/stacs.ini");
	@acs_array = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";$si_dmg += $item[20];}
	if($item[22]){$bogulv="+ $item[22]";$di_dmg += $item[22];}

	&header;

	print <<"EOM";
<h1>闇の商店街</h1>
<hr size=0>

<FONT SIZE=3>
<B>闇の商店街のマスター</B><BR>
「いらっしゃい！新しくなった闇の武器、防具、そして魔法と、いろいろと揃ってるよ～。<BR>
　あ、なんだい、<B>$chara[4]</B>じゃないか。まだ生きてたのかい？
<BR>
　まあ、ゆっくり見ていってくれ。
<BR><BR>そうそう！最近装備品の下取りもはじめたんだ。」
</FONT>
<br><hr>現在の所持金：$chara[19] Ｇ<br>
現在の魔法 NO：$chara[59]<br>
<table>
<tr>
<th></th><th></th><th>なまえ</th><th>威力,説明</th><th>売値</th></tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の武器</th><th>$si_name $bukilv</th><th>$si_dmg</th><th>$ui_gold</th>
</tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_sell>
EOM
if ($hitd) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の防具</th><th>$di_name $bogulv</th><th>$di_dmg</th><th>$udi_gold</th>
</tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_sell>
EOM
if ($hita) { print "<input type=submit class=btn value=\"売る\">"; }
	print <<"EOM";
</th></form><th>現在の装飾品</th><th>$a_name</th><th>$a_ex</th><th>$uai_gold</th>
</tr>
</table>
<table>
<tr>
<td>
<form action="stshops.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		if($ino != 1140 or $chara[69]==1){
			print "<tr><td class=b1 align=\"center\">\n";
			print "<input type=radio name=item_no value=\"$ino\">";
			print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="武器を手に取る">
</form>
</td>
<td>
<form action="stshops.cgi" method="post">
<table>
EOM

	foreach (@def_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		print "<input type=radio name=item_no value=\"$ino\">";
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="防具を手に取る">
</form>
</td>
<td>
<form action="stshops.cgi" method="post">
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
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="装飾品を買う">
</form>
</td>
</tr>
</table>
EOM
if ($chara[55]==27 or $chara[56]==27 or $chara[57]==27 or $chara[58]==27){
	print <<"EOM";
	<form action="stshops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>忍術</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000000) {print "<input type=radio name=ps_no value=22>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>022</th><th>空蝉</th><th>5000000G</th>
	<th>忍術空蝉を放ちます。</th></tr>

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
	<form action="./stshops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>赤魔法</th><th>値段</th><th>説明</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000000) {print "<input type=radio name=ps_no value=32>";}
	else{print "×";}
	print <<"EOM";
	</th>
	<th>032</th><th>ギガドレイン</th><th>5000000G</th>
	<th>赤魔法ギガドレインを放ちます。</th></tr>

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

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("$in{'item_no'}そんなアイテムは存在しません@item_array"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	if($in{'kane'}>0){$chara[19]-=$in{'kane'};}
	elsif($chara[19] < $i_gold) { $bgg=1; }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;
if($bgg!=1){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("武器倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("防具倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("装飾品倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>怪しい武器屋のマスター</B><BR>
「毎度あり～！<br>
買った武器はあんたの武器倉庫に送っておいたよ！
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;
}else{

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい武器屋のマスター</B><BR>
「貴様・・・金もないのに武器を手に取るとは良い度胸だな<br>
そこを一歩でも動いたら、地獄よりも恐ろしい恐怖を体験することになるぞ。
」</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="武器を元に戻す">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=nigeru>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="武器を持って逃亡する。">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tatakau>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="店主と戦う">
</form>
EOM
if($chara[64]==100){
	print <<"EOM";
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=negiri>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="値切り交渉する">
</form>
EOM
}
print "<hr size=0>";
}

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

	if ($in{'ps_no'}==22){$ps_gold = 5000000;}
	if ($in{'ps_no'}==32){$ps_gold = 5000000;}

	if($chara[19] < $ps_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[59] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>怪しいスペルショップの店員</B><BR>
「毎度あり～！<br>
仮に魔法を元々持ってたなら、もうないよ！ハハ」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム盗む  #
#----------------#
sub nigeru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$chara[26] = $host;

if(int(rand(4))==1){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("武器倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("防具倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("装飾品倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	if($chara[192]==1){
		$chara[192]=2;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい商店街のマスター</B><BR>
「待てゴラァァァァ<br>
・・・・・・っち、逃がしたか。<br>
覚えてろよ・・・。
」</font>
<hr size=0>
EOM
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	$chmes="$chara[4]様が怪しい者に追われているようです。";
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	unshift(@chat_mes,"<><font color=\"yellow\">告知</font><>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$chmes</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]様は悪に染まりすぎ、賞金首(賞金：$syoukingaku G)となりました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);
		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");
		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);
	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	$chara[13]-=1;
	if($chara[192]==1){
		$chara[192]=0;
		$chara[19]=int($chara[19]/3);
		$chara[34]=int($chara[34]/3);
		$bb=1;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($bb==1){
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい商店街のマスター</B><BR>
「逃げられると思ってたのか？貴様・・・言ったよな。<br>
そこを一歩でも動いたら、地獄よりも恐ろしい恐怖を体験することになる、と。<br>
後悔しても遅いぜ・・・。お前には恐ろしい呪いがかかったのだ。
」</font>
<B>一発逆転のミッションに失敗してしまった！</B><BR></font>
<FONT SIZE=6 color="red">見覚えのある顔に所持金を盗まれた！<br></font>
<FONT SIZE=6 color="red">銀行が強盗に入られた！！<br></font>
$back_form
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい商店街のマスター</B><BR>
「逃げられると思ってたのか？貴様・・・言ったよな。<br>
そこを一歩でも動いたら、地獄よりも恐ろしい恐怖を体験することになる、と。<br>
後悔しても遅いぜ・・・。お前には恐ろしい呪いがかかったのだ。
」</font>
$back_form
<hr size=0>
EOM
}
}

	exit;
}
#----------------#
#  アイテム盗む  #
#----------------#
sub tatakau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$chara[26] = $host;
	if($chara[18]>5000){$byouyy=int(19701+rand(400));}
	else{$byouyy=int(10000+rand($chara[18]+12500));}
if($byouyy>20000){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("武器倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("防具倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("装飾品倉庫がいっぱいです！$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	if($chara[191]==1){
		$chara[191]=2;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい商店街のマスター</B><BR>
「ぐ・・・今日は調子が悪いぜ。<br><br>
覚えてろよ・・・。
」</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様が怪しい商店街の店主をやっつけたようです。";

	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]様は悪に染まりすぎ、賞金首(賞金：$syoukingaku G)となりました。";

		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);

		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");

		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[13]-=2;
	if($chara[191]==1){
		$chara[191]=0;
		$chara[19]=int($chara[19]/2);
		$chara[34]=int($chara[34]/2);
		$bb=1;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	$byouyy-=10000;
if($bb==1){
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy秒で瞬殺された。</B><BR><BR>
<B>怪しい商店街のマスター</B><BR>
「ザコが。その程度の腕でうちへくるんじゃねぇ。帰りな。AP下げといてやったよｗ
」
<B>一発逆転のミッションに失敗してしまった！</B><BR></font>
<FONT SIZE=6 color="red">見覚えのある顔に所持金を盗まれた！<br></font>
<FONT SIZE=6 color="red">銀行が強盗に入られた！！<br></font>
$back_form
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy秒で瞬殺された。</B><BR><BR>
<B>怪しい商店街のマスター</B><BR>
「ザコが。その程度の腕でうちへくるんじゃねぇ。帰りな。AP下げといてやったよｗ
」</font>
<br>
<form action="stshops.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM
}
}

	exit;
}

sub negiri {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$ok=1;
	if($i_gold > 100000000){$kane=int($i_gold / 100);}else{$kane=int($i_gold/2);}
	if($kane > $chara[19]){$ok=0;}

	$chara[26] = $host;

	&header;
if($ok==1){
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい武器屋のマスター</B><BR>
「ｆｍ・・・確かに君は、人の良さそうな人間だ・・・。<br>
気にいったぜ！それ、あんたの買える値段に値下げしてやる。<br>
どうだ、$kaneＧで買わないか？」</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=kane value=$kane>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="買う">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="買わない">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい武器屋のマスター</B><BR>
「ｆｍ・・・確かに君は、人の良さそうな人間だ・・・。<br>
だが、いくらなんでも君の所持金は低すぎるな。その値段では売れないよ。<br>
$kaneＧぐらいは用意してくれ。」</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="武器を元に戻す">
</form>
<hr size=0>
EOM
}
	exit;
}