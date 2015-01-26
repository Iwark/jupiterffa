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
<form action="haigo.cgi" method="post">
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

	&header;

	print <<"EOM";
<h1>配合所</h1>
<hr size=0>
<FONT SIZE=3>
<B>配合所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここではペットとペットの配合ができるぜ・・・<br>
まず、本体を持ってきな、一度本体を預けてから、相手を持ってきな。<br>
そしたら配合してやるよ・・・」
</FONT>
<br>現在の所持金：$chara[19] Ｇ
<hr size=0>
<br><br>
今できる配合
<form action="./haigo.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=haigo_buy>
<table>
<tr>
<th>No.</th><th>本体</th><th>相手</th><th>価格</th></tr>

<th>001</th><th>ドラゴン</th><th>ダイナソ\ーmini</th><th>500000G</th></tr>
EOM
if($chara[38]==3113 or $chara[38]==3103){
	$selection.="<option value=\"1\">001</option>\n";
}
	print <<"EOM";
<br><br>
</table><br>
<select name=questno>
<option value="no">選択してください
$selection
</select>
<input type=submit class=btn value="配合">
<br>
</table>
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub haigo_buy {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno'} eq 'no'){&error("配合を選択してください$back_form");}

	$quest_no = $in{'questno'};

	if($quest_no == 1){
		if($chara[48]==3113){
			$chara[38] = 3004;
			$chara[39] = "ドラゴンエッグ";
			$chara[40] = 0;
			$chara[41] = 100000;
			$chara[42] = 20000;
			$chara[43] = 20000;
			$chara[44] = 0;
			$chara[45] = 3;
			$chara[46] = 1;
			$chara[47] = 0;
			$chara[48] = 0;
		}
		elsif($chara[38]==3113){
			$chara[38] = 0;
			$chara[39] = "";
			$chara[40] = 0;
			$chara[41] = 0;
			$chara[42] = 0;
			$chara[43] = 0;
			$chara[44] = 0;
			$chara[45] = 0;
			$chara[46] = 0;
			$chara[47] = 0;
			$chara[48] =3113;
		}
		else{&error("本体を渡してません$back_form");}
	}

	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=5><B>完了しました</B></font><BR>
<FONT SIZE=3>
<B>配合所のマスター</B><BR>
「ふふふ。」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
