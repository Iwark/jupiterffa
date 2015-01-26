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
<form action="azukari.cgi" method="post">
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

&itemh;

exit;

#----------------#
#  アイテム表示  #
#----------------#
sub itemh {

	&chara_load;

	&chara_check;

	if($chara[0] eq "test" or $chara[0] eq "test2"){&error("テストキャラです。");}
	elsif($chara[18]<30000){&error("レベルが足りません。");}

	&item_load;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	
	open(IN,"azukari/item/$chara[0].cgi");
	@item_array = <IN>;
	close(IN);

	open(IN,"azukari/def/$chara[0].cgi");
	@def_array = <IN>;
	close(IN);

	open(IN,"azukari/acs/$chara[0].cgi");
	@acs_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>預かり所</h1>
<hr size=0>
<FONT SIZE=3><B>預かり人</B><BR>
「<B>君は$chara[4]</B>だろう。<br>
もはやこの世界で君の事を知らない人は少ないだろう。<br>
さぞかし高価なアイテムも沢山持っていることだろう。<br>
だが、この世界に信用できる倉庫は数少なく、困っていることだろう。<br>
そこで、この"預かり人"の出番だろう。<br>
君から預かったアイテムは全力で守るだろう。<br>
ただし、１つのアイテムにつき１億Ｇの手数料を貰うだろう。」<br></FONT>
現在の持ち金：$chara[19]　Ｇ
<hr>
<form action="./azukari.cgi" method="post">
<hr>
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
預けている武器
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>売値</th></tr>
EOM
	$i = 1;
	foreach (@item_array) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	open(IN,"$item_file");
	@item_item = <IN>;
	close(IN);
	foreach(@item_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="特になし";}
	$bukikoka = "攻撃力 $idmg<br>命中率 $ihit<br>効果 $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
防具
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>売値</th></tr>
EOM
	$i = 101;
	foreach (@def_array) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibogu="+ $ilv";}else{$ibogu="";}
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="特になし";}
	$bogukoka = "防御力 $idmg<br>回避率 $ihit<br>効果 $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
装飾品
<table width = "98%">
<tr><th></th><th>なまえ</th><th>説明</th><th>売値</th></tr>
EOM

	$i = 201;
	foreach (@acs_array) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_msg</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td></table>
<p>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemr>
<input type=submit class=btn value="返してもらう">
</form>

<form action="./azukari.cgi" method="post">
<hr>
<table width = "100%">
<td width = "30%" align = "center" valign = "top">
武器
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>売値</th></tr>
EOM
	$t = 1;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	open(IN,"$item_file");
	@item_item = <IN>;
	close(IN);
	foreach(@item_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="特になし";}
	$bukikoka = "攻撃力 $idmg<br>命中率 $ihit<br>効果 $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
防具
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>売値</th></tr>
EOM
	$t = 101;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibogu="+ $ilv";}else{$ibogu="";}
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="特になし";}
	$bogukoka = "防御力 $idmg<br>回避率 $ihit<br>効果 $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
装飾品
<table width = "98%">
<tr><th></th><th>なまえ</th><th>説明</th><th>売値</th></tr>
EOM

	$t = 201;
	foreach (@souko_acs) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_msg</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td></table>
<p>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemu>
<input type=submit class=btn value="預ける">
</form>
EOM


	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  返してもらう  #
#----------------#
sub itemr {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	if(!$soubi) {&error("アイテムがありません");}

	$soubi-=1;

	open(IN,"azukari/item/$chara[0].cgi");
	@item_chara = <IN>;
	close(IN);
		
	open(IN,"azukari/def/$chara[0].cgi");
	@def_chara = <IN>;
	close(IN);

	open(IN,"azukari/acs/$chara[0].cgi");
	@acs_chara = <IN>;
	close(IN);

	$hit=0;
	$iii=0;

	foreach(@item_chara){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
		if($soubi == $iii) { $hit=1;last; }
		$iii++;
	}
	if(!$hit){
		$ddd=0;
		$soubi-=100;
		foreach(@def_chara){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
			if($soubi == $ddd) { $hit=2;last; }
		$ddd++;
		}
	}
	if(!$hit){
		$aaa=0;
		$soubi-=100;
		foreach(@acs_chara){
($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($soubi == $aaa) { $hit=3;last; }
		$aaa++;
		}
	}

	if($hit==1){
		if($chara[18]<10000){
			&error("レベルが足りません");
		}else{
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		
		splice(@item_chara,$soubi,1);
		open(OUT,">azukari/item/$chara[0].cgi");
		print OUT @item_chara;
		close(OUT);
		
	}elsif($hit==2){
		if($chara[18]<10000){
			&error("レベルが足りません");
		}else{
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@souko_def,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		
		splice(@def_chara,$soubi,1);
		open(OUT,">azukari/def/$chara[0].cgi");
		print OUT @def_chara;
		close(OUT);
	}elsif($hit==3){
		if($chara[18]<1000){
			&error("レベルが足りません");
		}else{
			open(IN,"$souko_folder/acs/$chara[0].cgi");
			@souko_acs = <IN>;
			close(IN);
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);

		splice(@acs_chara,$soubi,1);
		open(OUT,">azukari/acs/$chara[0].cgi");
		print OUT @acs_chara;
		close(OUT);
		
	}else{
		&error("そんなアイテムは存在しません");
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>返してもらいました。</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  預ける　　　  #
#----------------#
sub itemu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	if(!$soubi) {&error("アイテムがありません");}
	
	if($chara[19]<100000000){
		&error("お金が足りません");
	}else{
		$chara[19]-=100000000;
	}

	$soubi-=1;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$hit=0;
	$iii=0;

	foreach(@souko_item){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
		if($soubi == $iii) { $hit=1;last; }
		$iii++;
	}
	if(!$hit){
		$ddd=0;
		$soubi-=100;
		foreach(@souko_def){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
			if($soubi == $ddd) { $hit=2;last; }
		$ddd++;
		}
	}
	if(!$hit){
		$aaa=0;
		$soubi-=100;
		foreach(@souko_acs){
($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($soubi == $aaa) { $hit=3;last; }
		$aaa++;
		}
	}

	if($hit==1){
		if($chara[18]<10000){
			&error("レベルが足りません");
		}else{
			open(IN,"azukari/item/$chara[0].cgi");
			@item_chara = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@item_chara,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">azukari/item/$chara[0].cgi");
		print OUT @item_chara;
		close(OUT);
		
		splice(@souko_item,$soubi,1);
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		
	}elsif($hit==2){
		if($chara[18]<10000){
			&error("レベルが足りません");
		}else{
			open(IN,"azukari/def/$chara[0].cgi");
			@def_chara = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@def_chara,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">azukari/def/$chara[0].cgi");
		print OUT @def_chara;
		close(OUT);
		
		splice(@souko_def,$soubi,1);
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}elsif($hit==3){
		if($chara[18]<1000){
			&error("レベルが足りません");
		}else{
			open(IN,"azukari/acs/$chara[0].cgi");
			@acs_chara = <IN>;
			close(IN);
		}
		push(@acs_chara,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

		open(OUT,">azukari/acs/$chara[0].cgi");
		print OUT @acs_chara;
		close(OUT);

		splice(@souko_acs,$soubi,1);
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}else{
		&error("そんなアイテムは存在しません");
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>預かってもらいました。</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
