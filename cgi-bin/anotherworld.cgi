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
<form action="./anotherworld.cgi" >
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

	&header;

	print <<"EOM";
<h1>新世界への入り口</h1>
<hr size=0>

<FONT SIZE=3>
<B>怪しい人</B><BR>
「キミは、、、鍵を持っているのかい・・・？」
</FONT>
<br>
EOM
if($chara[18] > 3000){
	print <<"EOM";
<form action="./anotherworld.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=music>
<input type=submit class=btn value="怪しい人の自宅へ">
</form>
EOM
}
	print <<"EOM";
<form action="./anotherworld.cgi" >
<table>
EOM
if($chara[130]){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="1"></td>
	<td>ジュピタワールドへ(0G)</td></tr>
EOM
}
if($chara[131] and $chara[140]!=2){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="2"></td>
	<td>イエローワールドへ(10万Ｇ)</td></tr>
EOM
}
if($chara[132] and $chara[140]!=3){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="3"></td>
	<td>レッドワールドへ(20万Ｇ)</td></tr>
EOM
}
if($chara[133] and $chara[140]!=4){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="4"></td>
	<td>ドラゴンワールドへ(30万Ｇ)</td></tr>
EOM
}
if($chara[315] and $chara[140]!=5){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="5"></td>
	<td>天界へ(１億Ｇ)</td></tr>
EOM
}
if($chara[40]>1000000000000 and $chara[37]>=1000){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="6"></td>
	<td>チャイナへ？</td></tr>
EOM
}
if(!$chara[130] and !$chara[131] and !$chara[132] and !$chara[133]){
	print <<"EOM";
	鍵を持ってません。
EOM
}
else{
	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=goto_world>
<input type=submit class=btn value="新世界へ">
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

	if($in{'world_no'}==6){
		$com = "ワンさん";
		$com2 = <<"EOM";
		私は、チャイナのワン・ワンという者あるね。あなた中々見所あるね。わんわんなるね？
	<form action="./anotherworld.cgi" >
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=oneone>
	<input type=submit class=btn value="なる">
	</form>
EOM
	}else{
		if($in{'world_no'}==2){$ps_gold=100000;}
		if($in{'world_no'}==3){$ps_gold=200000;}
		if($in{'world_no'}==4){$ps_gold=300000;}
		if($in{'world_no'}==5){$ps_gold=100000000;}
		if($chara[19]<$ps_gold){&error("お金が足りません$back_form");}
		else{$chara[19] = $chara[19] - $ps_gold;}
	
		if($chara[130]!=1){$chara[130]=1;}
		else{$chara[130]=0;}

		$chara[140] = $in{'world_no'};
		$com = "移動完了しました。";
		$com2 = "気をつけて・・・。";
	}

	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$com</B><BR>
「$com2」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub music {

	&chara_load;

	&chara_check;

	&header;
	$musicno=int(rand(10));
	if($musicno==0){ $musicname="スクリャービンの「ピアノソ\ナタ４番」"; }
	elsif($musicno==1){ $musicname="カプースチンの「コンサートエチュードop40-2」"; }
	elsif($musicno==2){ $musicname="シューマンの「Presto Passionato」"; }
	elsif($musicno==3){
		$musicname="ファリャの組曲「恋は魔術師」より「火祭りの踊り」";
		if($chara[259]==1){
			$musiccom = << "EOM";
<font color="red" size=4>
そ、それは魔術師の魂！！！それがあればさらに上達するぞ！<br>
是非譲ってはくれないか？
</font>
<form action="./anotherworld.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tama>
<input type=hidden name=tama value=259>
<input type=submit class=btn value="譲る">
</form>
EOM
		}
	}
	elsif($musicno==4){ $musicname="ショパンの「ピアノソ\ナタ３番op58 第１楽章」"; }
	elsif($musicno==5){ $musicname="リストの「超絶技巧練習曲　第１０番」"; }
	elsif($musicno==6){ $musicname="ベートーヴェンの「ピアノソ\ナタ第１４番op27-2『月光』第３楽章」"; }
	elsif($musicno==7){ $musicname="アルベニスの「イベリア第3巻 第7曲 エル・アルバイシン」"; }
	elsif($musicno==8){ $musicname="ラフマニノフの「前奏曲op3 第２番『鐘』」"; }
	elsif($musicno==9){ $musicname="ドビュッシーの「映像 第1集 『水の反映(水に映る影)』」"; }

	print <<"EOM";
<FONT SIZE=3>
<B>怪しい人は実はピアニストだったのだ！</B><BR>
怪しい人は$musicnameを弾きはじめた。</font><br>
$musiccom
<hr size=0>
	$back_form
EOM

	$new_chara=$chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub tama {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[259]<1){&error("魂がありません$back_form");}
	else{$chara[259] -= 1;}

	$chara[305]+=365;
	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ピアニスト</B><BR>
「ありがとぅぅぅぅぅ！<br>
お礼に宿屋餅を365個あげよう！<br>
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub oneone {

	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("現在の職業をマスターしていません。");}
	$chara[14]=61;
	$chara[33]=1;
	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ワンさん</B><BR>
わんわんわんわんわんわんわんわんわんわんわん！</font><br>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}