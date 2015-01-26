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
<h1>刑務所</h1>
どうしたんだい？
<hr size=0>
EOM
if($chara[63]>=1){
	print <<"EOM";
<form action="keimusyo.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="syussyo">
<input type=submit class=btn value="出所する">($chara[63] G)
</form>
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub syussyo {

	&chara_load;

	&chara_check;

	if($chara[19]<$chara[63]){&error("お金が足りません");}
	else{$chara[19] -= $chara[63];}

	$chara[63]=0;

	if($chara[65]>50){
		$chara[64]+=1;
		$chara[65]-=1;
	}elsif($chara[64]>50){
		$chara[65]+=1;
		$chara[64]-=1;
	}
	&chara_regist;

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		if($chara[0] eq "jupiter"){
			if(int(rand(4)) == 0){
				$eg="$chara[4]様が刑務所をぶち壊して脱獄しました。";
			}elsif(int(rand(4)) == 0){
				$eg="$chara[4]様が刑務所の番人を暗殺して脱獄しました。";
			}elsif(int(rand(4)) == 0){
				$eg="$chara[4]様が刑務所の番人との死闘の末脱獄しました。";
			}else{
				$eg="$chara[4]様が刑務所を破壊して脱獄しました。";
			}
		}else{
			$eg="$chara[4]様が刑務所から出所しました。";
		}
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');


	&header;

	print <<"EOM";
<h1>出所しました</h1>
<hr size=0>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}