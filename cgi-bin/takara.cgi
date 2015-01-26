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
<form action="takara.cgi" method="post">
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

&sakaba;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub sakaba {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>宝くじ所</h1>
<hr size=0>
<FONT SIZE=3>
<B>人間</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
宝くじを買いにきたようだな。5万Ｇだぞ。ただし何度買っても意味はない。最後の番号で投票されるのだ。<br>
４桁の数字を入力するんだ。変な入力をすると無効票になってしまうから注意するんだぞ。」
</FONT>
<hr size=0>
<form action="takara.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
番号：<input type="text" name="p_id" value="" size=40><br>
<br>　　
<input type=submit class=btn value="投票する">
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
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($in{'p_id'} eq "") {
		&error("宝くじの数値が入力されていません。$back_form");
	}
	if (length($in{'p_id'}) > 4) {
		&error("宝くじの数値が長すぎます。$back_form");
	}
	if ($in{'p_id'} =~ m/[^0-9]/){
		&error("宝くじの数値に数字以外の文字が含まれています。$back_form"); 
	}
	if($chara[19] < 50000) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - 50000; }

	open(IN,"bango.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;

	$ppt=0;$iz=0;
	foreach(@member_data){
		($id,$suuti) = split(/<>/);
		if($id eq $chara[0]){$member_data[$iz]="$chara[0]<>$chara[4]<>$in{'p_id'}<>\n";$ppt=1;}
		$iz++;
	}
	if($ppt==0){push(@member_data,"$chara[0]<>$chara[4]<>$in{'p_id'}<>\n");}

	open(OUT,">bango.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>人間</B><BR>
「50000G使って投票しました」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}