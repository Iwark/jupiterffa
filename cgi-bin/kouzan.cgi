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
<form action="./kouzan.cgi" method="post">
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

	if(!$chara[100]){$chara[100]=0;}
	if(!$chara[97]){$chara[97]=0;}
	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	&header;

	print <<"EOM";
	<h1>鉱山</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>おっさん</B><BR>
	「若者は働けー。バイトすんじゃろ～？ハッハ。<br>
	当然、つるはしが必要だぞ笑」
	</FONT>
	<br>
	現在のＨＰ：$chara[15]\/$chara[16]<br>
	つるはしの数：$chara[100]本<br>
	黄金のつるはしの数：$chara[97]本<br>
	プラチナのつるはしの数：$chara[310]本
	<br>
EOM
	if($chara[100]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=goto_world>
		<input type=submit class=btn value="働く">
		</form>
EOM
	}
	if($chara[97]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=ougon_world>
		<input type=submit class=btn value="黄金のつるはしで働く">
		</form>
EOM
	}
	if($chara[310]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=pra_world>
		<input type=submit class=btn value="プラチナのつるはしで働く">
		</form>
EOM
	}
	if($chara[24] == 1341){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=turu_world>
		<input type=submit class=btn value="鶴嘴で働く">※なくなります
		</form>
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
sub goto_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	if(!$chara[100]){&error("つるはしがありません");}
	else{$chara[100]-=1;}
	if(!$chara[37]){$chara[37]=1;$ten=1;}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=30;$i++){
		if($chara[70]!=1){$rdd=int(rand(3000));}
		else{$rdd=int(rand(5000));}
		$com.="<hr size=0>$iターン<br>ＨＰ：$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>特殊合成石だ！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd==1){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>黄金のつるはしだ！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<5){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>つるはしだ！ひゃほーい！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<10){
			$com.="あ！？珍しい！ミニデビルだ！！<br><br>";
			$com.="倒せば大変珍しい物が手に入るとか…。<br><br>";
			$com.="<b><font size=6 color=red>ちっぽけなつるはしじゃ無理！</font></b><br>";
			$dmg = $chara[16] + int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<20){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>合成石だ！ひゃほーい!!</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<50){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("武具倉庫がいっぱいです！$back_form");
			}
			if(int(rand(4))<3){$i_no=1001+int(rand(15));}
			else{$i_no=1001+int(rand(30+$chara[37]));}
			if($i_no > 1060){$i_no=1001+int(rand(60));}
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$com.="こ・・・これは！！！<br><br>";
			$com.="なんだこりゃ・・・！？<br><br>";
			$com.="<b><font size=4 color=yellow>$i_nameだ！ひゃほーい!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<80){
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
			$souko_def_num = @souko_def;
			if ($souko_def_num >= $def_max) {
				&error("防具倉庫がいっぱいです！$back_form");
			}
			if(int(rand(4))<3){$i_no=2001+int(rand(15));}
			else{$i_no=2001+int(30+$chara[37]);}
			if($i_no > 2060){$i_no=2001+int(rand(60));}
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$com.="こ・・・これは！！！<br><br>";
			$com.="なんだこりゃ・・・！？<br><br>";
			$com.="<b><font size=4 color=yellow>$i_nameだ！ひゃほーい!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<85){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=5 color=red>玉手箱だっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] * 3 / 2));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[70]>=1){
				if($chara[18]<50000){
					$lv = int(rand($chara[18]/100));
				}else{
					$lv = int(rand($chara[18]/500));
				}
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=red>$lvレベル上がった！</font></b><br>";
				}else{
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$kexp = int($chara[15]/3) * int(rand($chara[18] / 50) + 1);
				$com.="<b><font size=4 color=yellow>$kexpの経験値！</font></b><br>";
				$exp += $kexp;
				}
			}else{
				$lvdown = int(rand($chara[18]/1000));
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdownレベル下がった！</font></b><br>";
			}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<150){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=4 color=yellow>モンスターだっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>何とか倒せた!!</font></b><br>";
				$kexp = int($chara[15]/3) * int(rand($chara[18] / 50) + 1);
				$com.="<b><font size=4 color=yellow>$kexpの経験値！</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>ダメだ強い…。</font></b><br>";}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<250){
			$com.="こ・・・これは！！！<br><br>";
			$com.="金・・・！？<br><br>";
			$kgold = int(rand($chara[37] * 10000 + $chara[18] * 100));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>金だ！ひゃほーい!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgoldＧ入手した！！</font></b><br>";
			$dmg = int(rand($chara[16] / 5) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<500){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<font color=white><b>うおおおお、休憩所だ！！！</b></font><br><br>";
			if(int(rand(3))<2){$com.="と、思ったらそんなのあるわけなかった！<br><br>";}
			else{
				$com.="<b><font size=4 color=white>ちょっと回復!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>ＨＰが$dmg回復。</font></b><br>";
			}
		}
		elsif($rdd<800){
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="<b><font size=4 color=red>ゴン！頭に岩が!!</font></b><br><br>";
			$com.="いってぇなボケコラァ・・・・！！！！<br><br>";
			$dmg = int(rand($chara[16] / 3) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		else{
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ふぃ～疲れた～。何もねー。<br><br>";
			$dmg = int(rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]は限界だ！！";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}
	if($ten==1){$chara[37]=0;}

	$chara[15]=$chara[16];
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	結果：<br>
	レベル$lv<br>
	経験値$exp<br>
	金$goldＧ<br>
	合成石$goseiseki個<br>
	特殊合成石$tokusyugoseiseki個<br>
	つるはし$turu個<br>
	黄金のつるはし$turu_gold個<br>
	その他$k個<br></font>
EOM
	if($chara[100]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$new_chara">
		<input type=hidden name=mode value=goto_world>
		<input type=submit class=btn value="もう一発！！">
		</form>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub ougon_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if(!$chara[97]){&error("黄金のつるはしがありません");}
	if(!$chara[37]){$chara[37]=1;$ten=1;}
	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=30;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$iターン<br>ＨＰ：$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>特殊合成石だ！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd==1){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>黄金のつるはしだ！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<3){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>つるはしだ！ひゃほーい！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<10){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>合成石だ！ひゃほーい!!</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<20){
			$com.="あ！？珍しい！ミニデビルだ！！<br><br>";
			$com.="倒せば大変珍しい物が手に入るとか…。<br><br>";
			$com.="ふっ、余裕！黄金のつるはしなめるなぁ！さぁ何かあるか…？<br><br>";
			$ran=int(rand(5));
			for($i=0;$i<$ran;$i++){
			$rann=int(rand(4));
			if($rann==0){
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>合成石だ！ひゃほーい!!</font></b><br>";
			}
			elsif($rann==1){
			$turu+=1;
			$com.="<b><font size=5 color=yellow>つるはしだ！ひゃほーい！</font></b><br>";
			}
			elsif($rann==2){
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>黄金のつるはしだ！！</font></b><br>";
			}
			elsif($rann==3){
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>特殊合成石だ！！</font></b><br>";
			}
			}
			$dmg = $chara[16] + int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<35){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("武具倉庫がいっぱいです！$back_form");
			}
			if(int(rand(4))<2){$i_no=1001+int(rand(30));}
			else{$i_no=1001+int(rand(45));}
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$com.="こ・・・これは！！！<br><br>";
			$com.="なんだこりゃ・・・！？<br><br>";
			$com.="<b><font size=4 color=yellow>$i_nameだ！ひゃほーい!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<50){
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
			$souko_def_num = @souko_def;
			if ($souko_def_num >= $def_max) {
				&error("防具倉庫がいっぱいです！$back_form");
			}
			if(int(rand(4))<2){$i_no=2001+int(rand(30));}
			else{$i_no=2001+int(rand(45));}
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$com.="こ・・・これは！！！<br><br>";
			$com.="なんだこりゃ・・・！？<br><br>";
			$com.="<b><font size=4 color=yellow>$i_nameだ！ひゃほーい!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<60){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=5 color=red>玉手箱だっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] * 4 / 3));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[18]<50000){
					$lv = int(rand($chara[18]/99));
				}else{
					$lv = int(rand($chara[18]/495));
				}
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=red>$lvレベル上がった！</font></b><br>";
			}else{
				$lvdown = int(rand($chara[18]/5000));
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdownレベル下がった！</font></b><br>";
			}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<85){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=4 color=yellow>モンスターだっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>何とか倒せた!!</font></b><br>";
				$kexp = $chara[15] * int(rand($chara[18] / 25) + 1);
				$com.="<b><font size=4 color=yellow>$kexpの経験値！</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>ダメだ強い…。</font></b><br>";}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<125){
			$com.="こ・・・これは！！！<br><br>";
			$com.="金・・・！？<br><br>";
			$kgold = int(rand($chara[37] * 10000 + $chara[18] * 100));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>金だ！ひゃほーい!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgoldＧ入手した！！</font></b><br>";
			$dmg = int(rand($chara[16] / 5) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<200){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<font color=white><b>うおおおお、休憩所だ！！！</b></font><br><br>";
			if(int(rand(3))<2){$com.="と、思ったらそんなのあるわけなかった！<br><br>";}
			else{
				$com.="<b><font size=4 color=white>ちょっと回復!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>ＨＰが$dmg回復。</font></b><br>";
			}
		}
		elsif($rdd<350){
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="<b><font size=4 color=red>ゴン！頭に岩が!!</font></b><br><br>";
			$com.="いってぇなボケコラァ・・・・！！！！<br><br>";
			$dmg = int(rand($chara[16] / 3) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		else{
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ふぃ～疲れた～。何もねー。<br><br>";
			$dmg = int(rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]は限界だ！！";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}

	if(int(rand(3))<2){$chara[97]-=1;$mes="黄金のつるはしが壊れてしまった。";}
	
	if($ten==1){$chara[37]=0;}

	$chara[15]=$chara[16];

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	結果：<br>
	レベル$lv<br>
	$mes<br>
	経験値$exp<br>
	金$goldＧ<br>
	合成石$goseiseki個<br>
	特殊合成石$tokusyugoseiseki個<br>
	つるはし$turu個<br>
	黄金のつるはし$turu_gold個<br>
	その他$k個<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub pra_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if(!$chara[310]){&error("プラチナのつるはしがありません");}
	$k=0;
	$com="<font size=3><center>";
	$hi=0;$mizu=0;$yami=0;$hikari=0;
	$rdd=0;
	for($i=0;$i<=10;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$iターン<br>ＨＰ：$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=6 color=yellow>元素がザクザク！！</font></b><br>";
			$hi += int(rand(10));
			$mizu += int(rand(10));
			$yami += int(rand(10));
			$hikari += int(rand(10));
			$dmg = int(rand($chara[16] * 4));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<10){
			$com.="ん・・・？何かが光り輝いている・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=5 color=yellow>色んな元素がいくつか見える気がする！！</font></b><br>";
			$hi += int(rand(3));
			$mizu += int(rand(3));
			$yami += int(rand(3));
			$hikari += int(rand(3));
			$dmg = int(rand($chara[16] * 3));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<100){
			$com.="ん・・・？何かが見えるぞ・・・。<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			if(int(rand(4))==0){$hi += int(rand(3));}
			elsif(int(rand(4))==0){$mizu += int(rand(3));}
			elsif(int(rand(4))==0){$yami += int(rand(3));}
			else{$hikari += int(rand(3));}
			$com.="<b><font size=4 color=yellow>気のせいか、元素が見える気がする！！</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<500){
			$com.="ん・・・？何かが見えるぞ・・・。<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			if(int(rand(4))==0){$hi += int(rand(2));}
			elsif(int(rand(4))==0){$mizu += int(rand(2));}
			elsif(int(rand(4))==0){$yami += int(rand(2));}
			else{$hikari += int(rand(2));}
			$com.="<b><font size=3 color=yellow>気のせいか、元素が見える気がする！！</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		else{
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ふぃ～疲れた～。何もねー。<br><br>";
			$dmg = int(rand($chara[16] / 3));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]は限界だ！！";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";

	$chara[310]-=1;

	$chara[15]=$chara[16];

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$isi[29]+=$hi;
		$isi[30]+=$mizu;
		$isi[31]+=$yami;
		$isi[32]+=$hikari;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	結果：<br>
	火の元素$hi個<br>
	水の元素$mizu個<br>
	闇の元素$yami個<br>
	光の元素$hikari個<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub turu_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if($chara[24] != 1341){&error("鶴嘴がありません");}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=50;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$iターン<br>ＨＰ：$chara[15]\/$chara[16]<br>";

		if($rdd<100){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>特殊合成石だ！！</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<200){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>黄金のつるはしだ！！</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<350){
			$com.="ん・・・？こんなところにつるはし・・・？<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>つるはしだ！ひゃほーい！</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<500){
			$com.="ん・・・？何か硬いものにぶつかったぞ・・・<br><br>";
			$com.="こ・・・これは！！！<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>合成石だ！ひゃほーい!!</font></b><br>";
			$dmg = int(rand($chara[16] / 10));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<550){
			$com.="あ！？珍しい！デビルだ！！<br><br>";
			$com.="倒せば大変珍しい物が手に入るとか…。<br><br>";
			$com.="ふっ、余裕！鶴嘴なめるなぁ！さぁ何かあるか…？<br><br>";
			$ran=int(rand(20));
			for($i=0;$i<$ran;$i++){
			$rann=int(rand(4));
			if($rann==0){
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>合成石だ！ひゃほーい!!</font></b><br>";
			}
			elsif($rann==1){
			$turu+=1;
			$com.="<b><font size=5 color=yellow>つるはしだ！ひゃほーい！</font></b><br>";
			}
			elsif($rann==2){
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>黄金のつるはしだ！！</font></b><br>";
			}
			elsif($rann==3){
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>特殊合成石だ！！</font></b><br>";
			}
			}
			$dmg = $chara[16] + int(rand($chara[16]/10));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<600){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("武具倉庫がいっぱいです！$back_form");
			}
			if(int(rand(4))<2){$i_no=1170;}
			else{$i_no=1193+int(rand(8));}
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$com.="こ・・・これは！！！<br><br>";
			$com.="なんだこりゃ・・・！？<br><br>";
			$com.="<b><font size=4 color=yellow>$i_nameだ！ひゃほーい!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 40));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<650){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=5 color=red>玉手箱だっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] * 4 / 30));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[18]<50000){
					$lvc = int(rand($chara[18]/100));
				}else{
					$lvc = int(rand($chara[18]/500));
				}
				$lv += $lvc;
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=red>$lvレベル上がった！</font></b><br>";
			}else{
				$lvc =  int(rand($chara[18]/5000));
				$lvdown += $lvc;
				$com.="<b><font size=4 color=yellow>中を開けると…</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdownレベル下がった！</font></b><br>";
			}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<700){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<b><font size=4 color=yellow>モンスターだっ！！！！</font></b><br>";
			$dmg = int(rand($chara[16] / 5 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>何とか倒せた!!</font></b><br>";
				$kexp = $chara[15] * int(rand($chara[18] / 25) + 1);
				$com.="<b><font size=4 color=yellow>$kexpの経験値！</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>ダメだ強い…。</font></b><br>";}
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<800){
			$com.="こ・・・これは！！！<br><br>";
			$com.="金・・・！？<br><br>";
			$kgold = int(rand($chara[37] * 100000 + $chara[18] * 10000));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>金だ！ひゃほーい!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgoldＧ入手した！！</font></b><br>";
			$dmg = int(rand($chara[16] / 50) + rand($chara[16] / 10 / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}
		elsif($rdd<900){
			$com.="こ・・・これは！！！<br><br>";
			$com.="<font color=white><b>うおおおお、休憩所だ！！！</b></font><br><br>";
			if(int(rand(3))<2){$com.="と、思ったらそんなのあるわけなかった！<br><br>";}
			else{
				$com.="<b><font size=4 color=white>ちょっと回復!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>ＨＰが$dmg回復。</font></b><br>";
			}
		}
		else{
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ザクザクザクザクザクザク。ザクザクザクザクザクザク。<br><br>";
			$com.="ふぃ～疲れた～。何もねー。<br><br>";
			$dmg = int(rand($chara[16] / 10 / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>ＨＰが$dmg減った。</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]は限界だ！！";
			$chara[15]=1;
			$i=51;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}

	if(int(rand(4))<3){&item_lose;$chara[24]="";$mes="鶴嘴が壊れてしまった。";}

	$chara[15]=$chara[16];

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	結果：<br>
	レベル$lv<br>
	$mes<br>
	経験値$exp<br>
	金$goldＧ<br>
	合成石$goseiseki個<br>
	特殊合成石$tokusyugoseiseki個<br>
	つるはし$turu個<br>
	黄金のつるはし$turu_gold個<br>
	その他$k個<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}