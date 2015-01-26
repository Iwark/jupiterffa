#!/usr/local/bin/perl



# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# アイテムライブラリの読み込み
require 'item.pl';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

#--------------#
#　メイン処理　#
#--------------#

&decode;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}

	$back_form = << "EOM";
<br>
<form action="abilityini.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

if ($mode) { &$mode; }

&ability;

exit;

#--------------------#
#   メイン画面       #
#--------------------#
sub ability{

	&chara_load;

	&chara_check;

	&header;
if(!$chara[35]){$chara[35]=0;}
$goldneed = $chara[18] * 500;
	print << "EOM";
<h1>能\力\初\期\化\屋</h1><hr>
<br>
能\力の初期化にはレベル×500G必要です。<br><br>
現在の所持金：$chara[19]G<br><br>
必要なおかね：$goldneed G<br>　<br>　
<table width='20%' border=0>
<form action="abilityini.cgi" method="POST">
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="能\力を初\期\化する"></form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#--------------------#
#   購入部分         #
#--------------------#
sub kounyu {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[19] < $chara[18] * 500) { &error("お金が足りません$back_form"); }

	$chara[16] = $chara[16] - int((rand($chara[10]*2)+$chara[10])*10);
	if($chara[16] < $kiso_hp){$chara[16] = $kiso_hp;}
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + $chara[37] * 20 - 4;

	&chara_regist;

	&header;

	print <<"EOM";
能\力を初\期\化しました。

<form action="$script" method="POST">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}

