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
<form action="itemya2.cgi" >
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
	if($chara[70]<1){&error("突破前です");}	
	if($chara[18]<100){&error("レベルが足りません");}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	open(IN,"freekako2.cgi");
	@kako_array2 = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>加工品素材フリーマーケット</h1>
<hr size=0>
<FONT SIZE=3><B>ふりーまーけっとの人</B><BR>
「<B>$chara[4]</B>だな。<br>
ここでは、加工品素材の売買が出来るぞ。基本的なルールはフリーマーケットとほぼ同じだ。<br>
<font color="red" size=4><b>ただし、金額は１億Ｇ単位、１０００億Ｇまでの設定となる。</b></font>」<br></FONT>
現在の持ち金：$chara[19]　Ｇ
<hr>

<table width = "100%">
	<tr>
	<td width = "49%" align = "center" valign = "top">
	<form action="./itemya2.cgi" >
	<table border=1>
		<tr><th></th><th>加工品素材名</th><th>数</th><th>価格</th></tr>
		<tr>
EOM
		$i=1;
		#出品者のＩＤ、値段、Ｎｏ、名前、数
		foreach(@kako_array){
			($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
			$i_gold=$i_gold/100000000;
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name</td><td>$i_kazu</td><td>$i_gold億Ｇ</td></tr>
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

	<td width = "49%" align = "center" valign = "top">
	<form action="./itemya2.cgi" >
	<table border=1>
		<tr><th></th><th>加工品素材名</th><th>数</th><th>制限</th></tr>
		<tr>
EOM
		$g=1;
		#出品者のＩＤ、値段、Ｎｏ、名前、数
		foreach(@kako_array2){
			($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
			if($i_name){
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$g></td>
			<td>$i_name</td><td>$i_kazu</td><td>$i_gold</td></tr>
EOM
			}
		$g++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=bogu>
	<input type=submit class=btn value="１日制限アイテムをゲットする">
	</form>
	</td>
	</tr></table>

<form action="./itemya2.cgi" >
<hr>
<table width = "100%">
<tr>
<td width = "49%" align = "center" valign = "top">
加工品素材
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>かず</th></tr>
EOM
	$i = 0;
	foreach (@isi) {
		if($_>0){
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			($sozai) = split(/<>/,$sozai_data[$i]);
			$g=$i+1;
			print << "EOM";
			<tr><td class=b1 align="center"><input type=radio name=soubi value=$g></td>
			<td class=b1 nowrap>$sozai</td>
			<td align=right class=b1>$_</td>
			</tr>
EOM
		}
		$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "49%" align = "center" valign = "top">

<table width = "98%">
<tr><th></th><th nowrap></th><th nowrap></th><th nowrap></th></tr>
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
</table>
<p>
売値：<input type="text" name="sgold" size=30>億Ｇ</td>
数：<input type="text" name="skazu" size=10></td>
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

	if(!$in{'item_no'}){&error("選択してください");}

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	$hit=0;$ii=1;
	foreach(@kako_array){
		($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($i_id eq $chara[0]){
		&header;
	print <<"EOM";
<FONT SIZE=3>
<B>ふりーまーけっとの人</B><BR>
「それはあんたの出品したやつだぜ！<br>
返すことはできないがな、売れないなら俺がもらってやろうか？」</font>
<form action="./itemya2.cgi" >
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemsyobun>
<input type=submit class=btn value="はい">
</form>
<hr size=0>
EOM
	}else{
	if($chara[19] < $i_gold) { &error("お金が足りません"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$isi[$i_no]+=$i_kazu;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	$ii-=1;

	splice(@kako_array,$ii,1);

	open(OUT,">freekako.cgi");
	print OUT @kako_array;
	close(OUT);

	open(IN,"./charalog/$i_id.cgi") || &error("キャラクターが見つかりません$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[137] -= 1;
	if($charan[137]<0){$charan[137]=0;}
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
	$eg="$charan[4]様が出品していた$i_name($i_kazu個)を、$chara[4]様が$i_gold Gで購入しました。";
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ふりーまーけっとの人</B><BR>
「ほい、取引終了だなっ。」</font>
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
sub bogu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if(!$in{'item_no'}){&error("選択してください");}

	open(IN,"freekako2.cgi");
	@kako_array2 = <IN>;
	close(IN);

	$hit=0;$ii=1;
	foreach(@kako_array2){
		($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
		@array2 = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($chara[129] == $mday) { &error("制限。"); }
	else { $chara[129] = $mday; }

	$chara[26] = $host;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$isi[$i_no]+=1;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	$ii-=1;
	if($i_kazu>1){
		$array2[4]-=1;
		$new_isi2 = '';
		$new_isi2 = join('<>',@array2);
		$new_isi2 .= '<>';
		$kako_array2[$ii]=$new_isi2;
	}else{splice(@kako_array2,$ii,1);}

	open(OUT,">freekako2.cgi");
	print OUT @kako_array2;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ふりーまーけっとの人</B><BR>
「ほい、取引終了だなっ。」</font>
<hr size=0>
EOM

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

	if(!$in{'soubi'}) {&error("出品するものを選択してください");}
	if($chara[137]>=4){&error("同時に出品できる数は４つまでです。");}
	$soubi = $in{'soubi'}-1;
	$sgold = $in{'sgold'}*100000000;
	$skazu = $in{'skazu'};

	if(!$sgold) {&error("金額を設定してください");}
	if(!$skazu) {&error("数を設定してください");}

	if($in{'sgold'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}
	if($sgold > 100000000000){&error("高すぎます。最大価格は１０００億Ｇです。");}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if($isi[$soubi]<$skazu){&error("足りません");}
	else{$isi[$soubi]-=$skazu;}

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	$ckazu=0;
	foreach(@kako_array){
		@array = split(/<>/);
		if($array[0] eq $chara[0]){$ckazu+=1;}
	}
	$chara[137]=$ckazu;
	if($chara[137]>=4){&error("同時に出品できる数は４つまでです。");}
	else{
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		($sozai) = split(/<>/,$sozai_data[$soubi]);
		push(@kako_array,"$chara[0]<>$sgold<>$soubi<>$sozai<>$skazu<>\n");
		open(OUT,">freekako.cgi");
		print OUT @kako_array;
		close(OUT);
	}

	$chara[137]++;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>ふりーまーけっとに出品しました</h1>
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

	open(IN,"freekako.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=1;
	foreach(@item_chara){
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;
	$ii-=1;
	splice(@item_chara,$ii,1);

	open(OUT,">freekako.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[137] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ふりーまーけっとの人</B><BR>
「ほいっ、あんがとよ！」</font>
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

	open(IN,"freedef.cgi");
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

	open(OUT,">freedef.cgi");
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

	open(IN,"freeacs.cgi");
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

	open(OUT,">freeacs.cgi");
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