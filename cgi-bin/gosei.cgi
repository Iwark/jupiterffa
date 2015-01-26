#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
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
<form action="gosei.cgi" >
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

&haigo;

&error;

exit;

#----------#
#  配合所  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
	if(!$chara[98]){$chara[98]=0;}
	if(!$chara[99]){$chara[99]=0;}
	&header;

	print <<"EOM";
<h1>合成所</h1>
<hr size=0>
<FONT SIZE=3>
<B>合成所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここでは合成ができるぜ・・・<br>
言っておくが、情報を持たずに合成をするのはお勧めしないぜ・・・<br>
ちなみに、うちは高い技術を使ってるから少々高くつくぜ・・・？<br>
まぁ、作るものによるんだがよ。」
</FONT>
<br>現在の所持金：$chara[19] Ｇ
<br>合成石の所持：$chara[99] 個
<br>特殊合成石の所持：$chara[98] 個
<br><hr>現在の装備<br>
<table>
<tr>
<td id="td2" class="b2">武器</td><td align="right" class="b2">$item[0] $bukilv</td>
<td id="td2" class="b2">攻撃力</td><td align="right" class="b2">$item[1]</td>
</tr>
<tr>
<td id="td2" class="b2">防具</td><td align="right" class="b2">$item[3] $bogulv</td>
<td id="td2" class="b2">防御力</td><td align="right" class="b2">$item[4]</td>
</tr>
</table>
<table width = "100%">
<tr>
<form action="gosei.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_soubi">
<td width = "25%" align = "center" valign = "top">
合成本体（武器）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>価格</th></tr>
EOM
	$i = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$i">
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
合成対象（武器）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>価格</th></tr>
EOM
	$g = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$g">
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$g++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
合成本体（防具）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>価格</th></tr>
EOM
	$d = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defd=$d+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$defd">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$d++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
合成対象（防具）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>価格</th></tr>
EOM
	$e = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defe = $e+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$defe">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$e++;
	}
		print << "EOM";
</table>
</td>
<table>
<br><br>
<input type=submit class=btn value="合成する">
</table>
</form>
</table>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'item_no1'} > 99 and $in{'item_no2'} < 100){
		&error("武器と防具の合成はできません。$back_form");}
	if($in{'item_no1'} < 100 and $in{'item_no2'} > 99){
		&error("武器と防具の合成はできません。$back_form");}
	if($in{'item_no1'} eq $in{'item_no2'}){
		&error("同じアイテムを選択しています。$back_form");}

	$cha=0;
	if($in{'item_no1'} > 99){
		$cha=1;
		$item_no1 = $in{'item_no1'}-100;
		$item_no2 = $in{'item_no2'}-100;
	}
	else{
		$item_no1 = $in{'item_no1'};
		$item_no2 = $in{'item_no2'};
	}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	if($cha==1){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
	}else{
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
	}

	$souko_item[$item_no1] =~ s/\n//g;
	$souko_item[$item_no1] =~ s/\r//g;
	$souko_item[$item_no2] =~ s/\n//g;
	$souko_item[$item_no2] =~ s/\r//g;

	($ino1,$iname1,$idmg1,$igold1,$ihit1,$ilv1,$iexp1) = split(/<>/,$souko_item[$item_no1]);
	($ino2,$iname2,$idmg2,$igold2,$ihit2,$ilv2,$iexp2) = split(/<>/,$souko_item[$item_no2]);

	$itm1=$ino1%1000;$itm2=$ino2%1000;

	if($itm1<16){$rare1=2;}
	elsif($itm1<31){$rare1=4;}
	elsif($itm1<46){$rare1=6;}
	elsif($itm1<61){$rare1=8;}
	elsif($itm1<76){$rare1=10;}
	elsif($itm1 == 79){$rare1=10;}
	else{$rare1=8;}

	if($itm2<16){$rare2=2;}
	elsif($itm2<31){$rare2=4;}
	elsif($itm2<46){$rare2=6;}
	elsif($itm2<61){$rare2=8;}
	elsif($itm2<76){$rare2=10;}
	elsif($itm2 == 79){$rare2=10;}
	else{$rare2=8;}

	if(($rare1+$rare2)/2 > 8){
		if($chara[99]<10){&error("レア度５以上の装備を作るには合成石が10個必要です$back_form");}
		else{$chara[99]-=10;$goseiseki=10;}
	}
	elsif(($rare1+$rare2)/2 > 6){
		if($chara[99]<2){&error("レア度４以上の装備を作るには合成石が2個必要です$back_form");}
		else{$chara[99]-=2;$goseiseki=2;}
	}
	elsif(($rare1+$rare2)/2 > 4){
		if(!$chara[99]){&error("レア度３以上の装備を作るには合成石が必要です$back_form");}
		else{$chara[99]-=1;$goseiseki=1;}
	}
	else{$goseiseki=0;}
	$rare3=($rare1+$rare2)/2;
	if($ilv1+$ilv2 > 2){$lvb=int(($ilv1+$ilv2)/2);}
	if($cha==1){
		if($rare3==2){$it_no=2000+int(rand(16)+1+$lvb);$ggold=120000;}
		if($rare3==3){$it_no=2000+int(rand(31)+1+$lvb);$ggold=200000;}
		if($rare3==4){$it_no=2000+int(rand(16)+16+$lvb);$ggold=280000;}
		if($rare3==5){$it_no=2000+int(rand(31)+16+$lvb);$ggold=400000;}
		if($rare3==6){$it_no=2000+int(rand(16)+31+$lvb);$ggold=520000;}
		if($rare3==7){$it_no=2000+int(rand(38)+16+$lvb);$ggold=750000;}
		if($rare3==8){$it_no=2000+int(rand(16)+38+$lvb);$ggold=1000000;}
		if($rare3==9){$it_no=2000+int(rand(50)+16+$lvb);$ggold=1500000;}
		if($rare3==10){$it_no=2000+int(rand(16)+50+$lvb);$ggold=2000000;}
		open(IN,"$def_file");
		@log_item = <IN>;
		close(IN);
	}else{
		if($rare3==2){$it_no=1000+int(rand(16)+1+$lvb);$ggold=120000;}
		if($rare3==3){$it_no=1000+int(rand(31)+1+$lvb);$ggold=200000;}
		if($rare3==4){$it_no=1000+int(rand(16)+16+$lvb);$ggold=280000;}
		if($rare3==5){$it_no=1000+int(rand(31)+16+$lvb);$ggold=400000;}
		if($rare3==6){$it_no=1000+int(rand(16)+31+$lvb);$ggold=520000;}
		if($rare3==7){$it_no=1000+int(rand(38)+16+$lvb);$ggold=750000;}
		if($rare3==8){$it_no=1000+int(rand(16)+38+$lvb);$ggold=1000000;}
		if($rare3==9){$it_no=1000+int(rand(50)+16+$lvb);$ggold=1500000;}
		if($rare3==10){$it_no=1000+int(rand(16)+50+$lvb);$ggold=2000000;}
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
	}


	if (!$in{'kakunin'}){

		&unlock($lock_file,'SI');

		&header;

		print << "EOM";
<center>
<h2>この合成にかかる費用は$ggold G、合成石は$goseiseki個です。よろしいですか？</h2>
<form action="gosei.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no1 value="$in{'item_no1'}">
<input type=hidden name=item_no2 value="$in{'item_no2'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="確認">
</form>
EOM
if($chara[98]){
		print << "EOM";
<form action="gosei.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no1 value="$in{'item_no1'}">
<input type=hidden name=item_no2 value="$in{'item_no2'}">
<input type=hidden name=kakunin value="2">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="特殊合成石を使う">
</form>
EOM
}
print "</center>";

		$new_chara = $chara_log;

		&shopfooter;

		&footer;

		exit;

	}
	if ($in{'kakunin'}==2){
		$chara[98]-=1;
		while(int( ($ino1 + $ino2) /2 ) > $it_no){
			if($it_no>70){break;}
			$it_no+=int(rand(3));
		}
	}
	if($chara[19]<$ggold){&error("お金が足りません$back_form");}
	$chara[19] -= $ggold;
	if(int( ($ino1 + $ino2) /2 ) > $it_no){$hgold = int($ggold / 2);}
	if($hgold){$chara[19] += $hgold;}

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
		if($it_no eq "$si_no"){ $hit=1;last; }
	}

	$souko_item[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
	$souko_item[$item_no2] = ();

	if($cha==1){
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}else{
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	&item_regist;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

if($hgold){
	print <<"EOM";
<FONT SIZE=3>
<B>$si_nameを作りました。あんまり良くない装備ができた為半額の$hgold Gキャシュバックした。</B><BR>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>$si_nameを作りました。</B><BR>
<hr size=0>
EOM
}

	&shopfooter;

	&footer;

	exit;
}