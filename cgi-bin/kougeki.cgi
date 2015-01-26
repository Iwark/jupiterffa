#!/usr/local/bin/perl

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

	$back_form = << "EOM";
<br>
<form action="keimusyo.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  アイテム表示  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>チャットを攻撃</h1>
<font size=4>
チャットをぜーんぶ消して、インパクトを与えます。本当によろしいですか？？<br>
荒らし時以外、厳禁。ログ流しに使うのは絶対にやめてください。<br>
押すと、以後１分間、誰も発言できなくなります。
</font>
<hr size=0>
EOM
if($chara[18]>10000 or $chara[0] eq "jupiter"){
	print <<"EOM";
<form action="kougeki.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kougeki">
<input type=submit class=btn value="攻撃する">
</form>
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub kougeki {

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($wday==0){$ww="日";}if($wday==1){$ww="月";}if($wday==2){$ww="火";}if($wday==3){$ww="水";}if($wday==4){$ww="木";}
	if($wday==5){$ww="金";}if($wday==6){$ww="土";}
	$eg="$chara[4]様がチャット欄を攻撃しました。$chara[18]のダメージ！！";
	$chatmes[0]="<>告知<>$year年$mon月$mday日($ww)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>$koktime<>\n";
	unshift(@chatmes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");
	open(OUT,">$chat_file");
	print OUT @chatmes;
	close(OUT);

	&unlock($lock_file,'MS');


	&header;

	print <<"EOM";
<h1>攻撃しました</h1>
<hr size=0>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}