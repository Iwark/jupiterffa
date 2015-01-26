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
<form action="jyoho.cgi" method="post">
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

&jyoho;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub jyoho {

	&chara_load;

	&chara_check;

	&header;

	$x[0]=1;$y[0]=1;
	$x[1]=2;$y[1]=1;
	$x[2]=4;$y[2]=1;
	$x[3]=5;$y[3]=4;
	$x[4]=6;$y[4]=6;

	print <<"EOM";
<h1>計算</h1>
<hr size=0>
<FONT SIZE=3>
<B>計算</B><BR>
($x[0],$y[0]),($x[1],$y[1]),($x[2],$y[2]),($x[3],$y[3]),($x[4],$y[4])
</FONT>
<hr size=0>
EOM

	for($i=0;$i<5;$i++){
		for($t=$i;$t<5;$t++){
			if($i != $t){
				$c = $x[$i] - $x[$t];
				$d = $y[$i] - $y[$t];
				$e = $c ** 2 + $d ** 2;
				$k = ($c ** 2 + $d ** 2) ** (1/2);
				print "($x[$i],$y[$i])と($x[$t],$y[$t])の距離は $k ( $e )<br>";
			}
		}
	}

	$new_chara = $chara_log;

	exit;
}