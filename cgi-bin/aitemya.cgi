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
<form action="aitemya.cgi" method="post">
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
	if($chara[70]){&error("突破後です");}
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

	open(IN,"afreeitem.cgi");
	@item_array = <IN>;
	close(IN);

	open(IN,"afreedef.cgi");
	@def_array = <IN>;
	close(IN);

	open(IN,"afreeacs.cgi");
	@acs_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>パワーアップして帰ってきたフリーマーケット</h1>
<hr size=0>
<FONT SIZE=3><B>帰ってきたフリーマーケットの人</B><BR>
「<B>$chara[4]</B>か。丁度いい所に来たな。<br>
たった今この私のパワーアップが完了したところだ。以前のバグは完全に修正されたんだぜ？。<br>
突破後だけにする予定だったが、丁度いい土地があったから第２店舗としてやってきたんだ。<br>
新たなバグ(特に、突破前でしか起こりえないことがあるかもしれない)があったら管理人に一報してくれ。<br>
一度に売ることができるのは、<font color="red">武器、防具、アクセサリーそれぞれ４つずつまで</font>だ。<br>
そして、<font color="red">出品された数がそれぞれ30個を超えると出品された順番に消えていく</font>ぞ。<br>
<font color="red">自分で出品した物は買えない</font>ようになったから注意が必要だ。<br>
また、<font color="red">最大で８億Ｇ</font>の価格設定となる。<br>
どうしてももっと高く売りたかったら、頭を使って工夫するんだな。<br>
この剣を２億で買ってくれたら向こうの剣を８億で売ります…という風に取引するとかな。」<br></FONT>
現在の持ち金：$chara[19]　Ｇ
<hr>

<table width = "100%">
	<tr>
	<td width = "30%" align = "center" valign = "top">
	<form action="./aitemya.cgi" method="post">
	<table border=1>
		<tr><th></th><th>武器名</th><th>攻撃力</th><th>命中力</th><th>価格</th></tr>
		<tr>
EOM
		$i=0;
		#出品者のＩＤ、値段、武器Ｎｏ、名前、ダメージ、金、命中、説明、レベル、経験値
		foreach(@item_array){
			($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
			if($ilv>0){$lvv="+ $ilv";}else{$lvv="";}
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name $lvv</td><td>$i_dmg</td><td>$ihit</td><td>$i_gold</td></tr>
EOM
		$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=buki>
	<input type=submit class=btn value="アイテムを買う">
	</form>
	</td>

	<td width = "30%" align = "center" valign = "top">
	<form action="./aitemya.cgi" method="post">
	<table border=1>
		<tr><th></th><th>防具名</th><th>防御力</th><th>回避力</th><th>価格</th></tr>
		<tr>
EOM
		$i=0;
		#出品者のＩＤ、値段、防具Ｎｏ、名前、防御力、金、回避、説明、レベル、経験値
		foreach(@def_array){
			($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
			if($ilv>0){$lvv="+ $ilv";}else{$lvv="";}
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name $lvv</td><td>$i_dmg</td><td>$ihit</td><td>$i_gold</td></tr>
EOM
			$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=bougu>
	<input type=submit class=btn value="アイテムを買う">
	</form>
	</td>

	<td width = "35%" align = "center" valign = "top">
	<form action="./aitemya.cgi" method="post">
	<table border=1>
		<tr><th></th><th>アクセ名</th><th>説明</th><th>価格</th></tr>
		<tr>
EOM
		$i=0;
		#出品者のＩＤ、値段、アクセＮｏ、名前、金、効果、…、説明
		foreach(@acs_array){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$a_name</td><td>$a_ex</td><td>$i_gold</td></tr>
EOM
			$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=acs>
	<input type=submit class=btn value="アイテムを買う">
	</form>
	</td></tr></table>

<form action="./aitemya.cgi" method="post">
<hr>
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
武器
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>売値</th></tr>
EOM
	$i = 0;
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
	$i = 100;
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

	$i = 200;
	foreach (@souko_acs) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
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
売値：<input type="text" name="sgold" size=30>G</td>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemu>
<input type=submit class=btn value="売る">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub buki {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreeitem.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「それはあんたの出品した物だぜ！<br>
返すことはできないがな、売れないなら処分してやろうか？」</font>
<form action="./aitemya.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemsyobun>
<input type=submit class=btn value="処分する">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("お金が足りません"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("武器倉庫がいっぱいです！$back_form");
	}

	push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$igold<>$ihit<>$ilv<>$iexp<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	splice(@item_chara,$ii,1);

	open(OUT,">afreeitem.cgi");
	print OUT @item_chara;
	close(OUT);

	open(IN,"./charalog/$i_id.cgi") || &error("キャラクターが見つかりません$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	$eg="$charan[4]様が出品していた$i_name $ibukiを、$chara[4]様が$i_gold Gで購入しました。";
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「毎度あり～！<br>
買ったモンはあんたの倉庫に送っておいたよ！」</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム買う  #
#----------------#
sub bougu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreedef.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「それはあんたの出品した物だぜ！<br>
返すことはできないがな、売れないなら処分してやろうか？」</font>
<form action="./aitemya.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=defsyobun>
<input type=submit class=btn value="処分する">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("お金が足りません"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $def_max) {
		&error("防具倉庫がいっぱいです！$back_form");
	}

	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>$igold<>$ihit<>$ilv<>$iexp<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	splice(@item_chara,$ii,1);

	open(OUT,">afreedef.cgi");
	print OUT @item_chara;
	close(OUT);

	open(IN,"./charalog/$i_id.cgi") || &error("キャラクターが見つかりません$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	$eg="$charan[4]様が出品していた$i_name $ibukiを、$chara[4]様が$i_gold Gで購入しました。";
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「毎度あり～！<br>
買ったモンはあんたの倉庫に送っておいたよ！」</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム買う  #
#----------------#
sub acs {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreeacs.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「それはあんたの出品した物だぜ！<br>
返すことはできないがな、売れないなら処分してやろうか？」</font>
<form action="./aitemya.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=acssyobun>
<input type=submit class=btn value="処分する">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("お金が足りません"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("アクセサリー倉庫がいっぱいです！$back_form");
	}

	push(@souko_acs,"$a_no<>$a_name<>$a_gold<>$a_kouka<>$a_0up<>$a_1up<>$a_2up<>$a_3up<>$a_4up<>$a_5up<>$a_hitup<>$a_kaihiup<>$a_wazaup<>$a_ex<>\n");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);

	splice(@item_chara,$ii,1);

	open(OUT,">afreeacs.cgi");
	print OUT @item_chara;
	close(OUT);

	open(IN,"./charalog/$i_id.cgi") || &error("キャラクターが見つかりません$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	$eg="$charan[4]様がフリーマーケットに出品していた$a_nameを、$chara[4]様が$i_gold Gで購入なさいました。";
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「毎度あり～！<br>
買ったモンはあんたの倉庫に送っておいたよ！」</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム売る  #
#----------------#
sub itemu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	$sgold = $in{'sgold'};

	if(!$soubi) {&error("アイテムがありません");}
	if(!$sgold) {&error("金額を設定してください");}

	if($in{'sgold'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}
	if($sgold > 800000000){&error("高すぎます。最大価格は１億です。");}

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
		open(IN,"afreeitem.cgi");
		@item_chara = <IN>;
		close(IN);
		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("同時に出品できる武具の数は４つまでです。");}
		else{
		if($ilv<1){$ilv=0;$iexp=1;}
	push(@item_chara,"$chara[0]<>$sgold<>$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><>$ilv<>$iexp<>\n");
		open(OUT,">afreeitem.cgi");
		print OUT @item_chara;
		close(OUT);
		splice(@souko_item,$soubi,1);
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		}
	}elsif($hit==2){
		open(IN,"afreedef.cgi");
		@item_chara = <IN>;
		close(IN);
		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("同時に出品できる防具の数は４つまでです。");}
		else{
		if($ilv<1){$ilv=0;$iexp=1;}
	push(@item_chara,"$chara[0]<>$sgold<>$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><>$ilv<>$iexp<>\n");
		open(OUT,">afreedef.cgi");
		print OUT @item_chara;
		close(OUT);
		splice(@souko_def,$soubi,1);
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		}
	}elsif($hit==3){
		open(IN,"afreeacs.cgi");
		@item_chara = <IN>;
		close(IN);
		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("同時に出品できるアクセサリーの数は４つまでです。");}
		else{
		push(@item_chara,"$chara[0]<>$sgold<>$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">afreeacs.cgi");
		print OUT @item_chara;
		close(OUT);
		splice(@souko_acs,$soubi,1);
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		}
	}else{
		&error("そんなアイテムは存在しません");
	}
	$chara[88]++;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>フリーマーケットに出品しました</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub itemsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreeitem.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	open(OUT,">afreeitem.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「処分してやったよ！」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub defsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreedef.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	open(OUT,">afreedef.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「処分してやったよ！」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub acssyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"afreeacs.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	open(OUT,">afreeacs.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>フリーマーケットの人</B><BR>
「処分してやったよ！」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}