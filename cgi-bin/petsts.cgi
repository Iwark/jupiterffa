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
<form action="petsts.cgi" >
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

&petsts;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub petsts {

	&chara_load;

	&chara_check;

	&header;
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	print <<"EOM";
<h1>$penameのステータス</h1>
現在の所持金：$chara[19] Ｇ<br><br>
お金を使ってペットに変化をもたらすことができる可\能\性があります。<br>
最低ボーダーを越えていないと\能\力\値が下がってしまうこともあります。<br>
ボーダーを越えていても\能\力\値が上がる保障はありません。<br>
<font SIZE=2 color="red">卵最強のペットを変化させると何か起こるかもしれません</font><br>
EOM
if($chara[45]){
	print <<"EOM";
	<IMG SRC="$img_path_pet/$egg_img[$chara[45]]">
	<br>最大ＨＰ：$chara[43]
	<br>攻撃力：$chara[44]
	<br>レベル：$chara[46]
	<br><br>
EOM
}
if($chara[46]==20 and $chara[38]==3000 and $chara[37]>3){
	print <<"EOM";
<form action="petsts.cgi" >
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="変化！"></form><p>
EOM
}
if($chara[70]<1){
	print <<"EOM";
最低ボーダー<br><br>
ＨＰ１ＵＰ：10000Ｇ<br>
攻撃力１ＵＰ：50000Ｇ<br>
レベル１ＵＰ：100000Ｇ<br><br>
<table width='25%' border=0>
<form action="petsts.cgi" >
<tr><td id="td2">ＨＰ</td>
<td align="right" class="b2"><input type="text" name="up1" size="24">　Ｇ</td></tr>
<tr><td id="td2">攻撃力</td>
<td align="right" class="b2"><input type="text" name="up2" size="24">　Ｇ</td></tr>
<tr><td id="td2">レベル</td>
<td align="right" class="b2"><input type="text" name="up3" size="24">　Ｇ</td></tr>
</tr>
</table>
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="変化！"></form><p>
EOM
}else{
	print <<"EOM";
入手した魂：<br><table><tr><th></th><th></th></tr>
EOM
	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);
	for($k=201;$k<300;$k++){
		if($chara[$k]){
			$hit=0;
			foreach(@item_array){
		($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
			if($phi_no == $k+3200) { last; }
			}
			print <<"EOM";
			<tr><th>
			$phi_nameの魂
			</th><th>
			<form action="petsts.cgi" >
			<input type="hidden" name="mode" value="tukau">
			<input type="hidden" name="aite" value="$phi_name">
			<input type="hidden" name="kno" value="$k">
			<input type="hidden" name="id" value="$chara[0]">
			<input type="hidden" name="mydata" value="$chara_log">
			<input type="submit" class="btn" value="使う">
			</form>
			</th></tr>
EOM
		}
	}
	print <<"EOM";
</table>
<table width='25%' border=0>
<form action="petsts.cgi" >
<tr><td id="td2">名前変更</td>
<td align="right" class="b2"><input type="text" name="namae" size="48"></td></tr>
</table>
<input type="hidden" name="mode" value="henkou">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="変化！"></form><p>
EOM
}
if($chara[70]==1 and $chara[38]==3000 and $chara[19]>=1000000){
	print <<"EOM";
	<form action="petsts.cgi" >
	<input type="hidden" name="mode" value="koware">
	<input type="hidden" name="id" value="$chara[0]">
	<input type="hidden" name="mydata" value="$chara_log">
	<input type="submit" class="btn" value="壊れた卵を闇卵に戻す（100万Ｇ）">
	</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub kounyu {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[19]<$in{'up1'}+$in{'up2'}+$in{'up3'}){ &error("お金が足りません$back_form"); }
	elsif($in{'up1'} < 0 or $in{'up2'} < 0 or $in{'up3'} < 0){ &error("マイナスの数値はダメです$back_form"); }
	elsif($in{'up1'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}
	elsif($in{'up2'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}
	elsif($in{'up3'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}
	else{ $chara[19] = $chara[19] - $in{'up1'} - $in{'up2'} - $in{'up3'}; }

	if ($in{'up1'}){
		if ($in{'up1'} > 10000){
			$hpup = int(rand($in{'up1'} / 1000 + 1)) + int($in{'up1'}/10000);
		}elsif(int(rand(4))==0){
			$hpup = -int(rand($in{'up1'}/1000 + 1)) - int($in{'up1'}/10000);
		}else{
			$hpup = int(rand($in{'up1'} / 1000 + 1)) + int($in{'up1'}/10000);
		}
		if($chara[43] + $hpup>10000){$hpup=0;}
	}
	if ($in{'up2'}){
		if ($in{'up2'} > 50000){
			$dmgup = int(rand($in{'up2'} / 10000 + 1)) + int($in{'up2'}/50000);
		}elsif(int(rand(4))==0){
			$dmgup = -int(rand($in{'up2'}/10000 + 1)) - int($in{'up2'}/50000);
		}else{
			$dmgup = int(rand($in{'up2'} / 10000)) + int($in{'up2'}/50000);
		}
	}
	if ($in{'up3'}){
		if ($in{'up3'} > 100000){
			$lvup = int(rand($in{'up3'} / 100000 + 1));
		}elsif(int(rand(4))==0){
			$lvup = -int(rand($in{'up3'}/ 75000 + 1));
		}else{
			$lvup = int(rand($in{'up3'} / 75000 + 1));
		}
	}
	$chara[43] += $hpup;
	$chara[42] = $chara[43];
	$chara[44] += $dmgup;
	$chara[46] += $lvup;
	if($chara[42]<1){$chara[42]=1;}
	if($chara[44]<1){$chara[44]=1;}
	if($chara[46]>20){$chara[46]=20;}
	if($chara[46]==20){
		if($chara[38]==3000 and $chara[37]>3){
			$k=100;
			#壊れた卵→ゴーチル
			$chara[38] = 3151;$chara[39] = "ゴーチル";$chara[40] = 0;
			$chara[41] = 2000;$chara[42] = 2400;$chara[43] = 2400;
			$chara[44] = 240;$chara[45] = 137;$chara[46] = 1;
			$chara[47] = 11;
		}
		if($chara[38]==3126){
			if(!$chara[131]){
				$k=1;
				#パンダマン→イエローマスター
				$chara[131]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
		if($chara[38]==3136 or $chara[38]==3135){
			if(!$chara[132]){
				$k=2;
				#ゴッドバード→レッドマスター
				$chara[132]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
		if($chara[38]==3122){
			if(!$chara[133]){
				$k=3;
				#ドラゴンロード→ドラゴンマスター
				$chara[133]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

if($k==1){
	print <<"EOM";
<FONT SIZE=4 color="red">変化時にパンダマンは自分が役目を果たした事を悟った。<br>
役目を果たしたパンダマンはイエローワールドの鍵を$chara[4]に与えて去っていった…</font>
EOM
}elsif($k==2){
	print <<"EOM";
<FONT SIZE=4 color="red">変化時にゴッドバードは自分が役目を果たした事を悟った。<br>
役目を果たしたゴッドバードはレッドワールドの鍵を$chara[4]に与えて去っていった…</font>
EOM
}elsif($k==3){
	print <<"EOM";
<FONT SIZE=4 color="red">変化時にドラゴンロードは自分の役目を果たした事を悟った。<br>
役目を果たしたドラゴンロードはドラゴンワールドの鍵を$chara[4]に与えて去っていった…</font>
EOM
}elsif($k==100){
	print <<"EOM";
<FONT SIZE=4 color="red">壊れた卵がなんと動き出した！！<br>
中から、なんと人の姿に酷似しているゴーチルが生まれた！！！！！！</font>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>変化が完了しました。<br>
＜変化＞<br>
ＨＰ：$hpup<br>
攻撃力：$dmgup<br>
レベル：$lvup</B></font><br>
EOM
}
	print <<"EOM";
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  情報買う　　  #
#----------------#
sub koware {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]!=1 or $chara[38]!=3000 or $chara[19]<1000000){ &error("条件満たしてません$back_form"); }
	else{ $chara[19] = $chara[19] - 1000000;}

	$chara[38]=3006;
	$chara[39]="闇の卵";
	$chara[40]=0;
	$chara[41]=3000000;
	$chara[42]=6500;
	$chara[43]=6500;
	$chara[44]=0;
	$chara[45]=5;
	$chara[46]=1;
	$chara[47]=0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>闇の卵に無事戻りました。<br>
＜変化＞<br>
ＨＰ：$hpup<br>
攻撃力：$dmgup<br>
レベル：$lvup</B></font><br>

<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub henkou {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if (!$in{'namae'}){ &error("入力してください$back_form"); }

	$chara[138] = $in{'namae'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>変化が完了しました。<br>
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub tukau {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($chara[38]!=3159 and $chara[46]<1000){ $comment = "対象ペットが弱すぎます。<br>"; }
	else{

	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	if ($in{'aite'} eq "警官"){
		if($chara[39] eq "警官"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "警官2") { $hit=1;$chara[235]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "ガオーン"){
		if($chara[39] eq "ヴァンプ"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "キング") { $hit=1;$chara[225]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "新型ウイルス"){
		if($chara[39] eq "新型ウイルス"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "新型ウイルス2") { $hit=1;$chara[231]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "新型ウイルス2"){
		if($chara[39] eq "新型ウイルス2"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "新型ウイルス3") { $hit=1;$chara[232]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "緑細菌"){
		if($chara[39] eq "新型ウイルス3"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "赤の玉") { $hit=1;$chara[275]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "タヌキマン"){
		if($chara[39] eq "オーガ"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "ギガントオーク") { $hit=1;$chara[234]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "警官2"){
		if($chara[39] eq "新型ウイルス3"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "グーガル") { $hit=1;$chara[236]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "マーシュ"){
		if($chara[39] eq "ギガントオーク"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "マーシュ・シャーク") { $hit=1;$chara[290]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "スノーマン"){
		if($chara[39] eq "グーガル"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "マーシュ") { $hit=1;$chara[220]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($in{'aite'} eq "エッグエンジェル"){
		if($chara[39] eq "ゴッドエンジェル"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "エッグエンジェル") { $hit=1;$chara[294]=0;last; }
			}
		}
			$comment = "そのペットには合わない魂のようです。<br>";
	}
	elsif ($chara[39] eq "ゴッドエンジェル" and $chara[24]==1400){
		if(int(rand(2))==0){
			$kougeki=int(rand(($in{'kno'}-200)*5));
			if($chara[128]>=5 and $item[1]>9998){$kougeki=int($kougeki/int($item[1]/10000+1));}
			if($item[1]+$kougeki>9999 and $chara[128]<5){$kougeki=9999-$item[1];}
			$item[1]+=$kougeki;
			$comment = "ゴッドエンジェルの\特\殊\能\力\によって武器の攻撃力が$kougekiポイント上がった！<br>";
		}else{
			$hitp=int(rand(($in{'kno'}-200)*5));
			if($chara[128]>=5 and $item[2]>9998){$hitp=int($hitp/int($item[2]/10000+1));}
			if($item[2]+$hitp>9999 and $chara[128]<5){$hitp=9999-$item[2];}
			$item[2]+=$hitp;
			$comment = "ゴッドエンジェルの\特\殊\能\力\によって武器の命中率が$hitpポイント上がった！<br>";
		}
		$chara[$in{'kno'}]=0;
	}
	else{ 
		$comment = "その魂は使えません。<br>";
	}
	if($hit) {
		$comment = "<b><font size=4 color=red>ペットが$phi_nameに変化した！！</font></b><br>";
		$chara[38] = $phi_no;
		$chara[39] = $phi_name;
		$chara[40] = 0;
		$chara[41] = $phi_exp;
		$chara[42] = $phi_hp;
		$chara[43] = $phi_hp;
		$chara[44] = $phi_damage;
		$chara[45] = $phi_image;
		$chara[46] = 1;
		$chara[47] = $ps;
	}

	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$comment<br>
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}