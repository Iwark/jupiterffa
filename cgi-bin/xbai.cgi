#!/usr/bin/perl

#-----------------------------------------------------#
#---賭金部屋------------------------------------------#
#---Edit by Right-Blue--------------------------------#
#---http://wsr.a-auc.jp/------------------------------#
#-----------------------------------------------------#

# 日本語ライブラリ
require 'jcode.pl';

# レジストライブラリ
require 'regist.pl';

# 初期設定の読み込み
require 'data/ffadventure.ini';

# 倍率設定
$bai1 = 50;
$bai2 = 999;
$bai3 = 9999;

# 成功する確率(デフォルト10では当たる確立が10分の1)
$bai_atta1 = 10;
$bai_atta2 = 90;
$bai_atta3 = 200;

# 倍率設定２
$bai_a = int(rand($bai1)) + 2;
$bai_b = int(rand($bai2)) + $bai1;
$bai_c = int(rand($bai3)) + $bai2;

$backgif = $shop_back;
$midi = $shop_midi;

#-------------------------[設定はここまで]-------------------------#
#-----------ここからＣＧＩが分かる人のみ変更してください-----------#
#------------------------------------------------------------------#
&decode;

$back_form = << "EOM";
<br>
<form action="./xbai.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}

if ($mode) { &$mode; }

&kake;

exit;
#------------#
#--受付画面--#
#------------#
sub kake{

	&chara_load;

	&chara_check;

	&header;

	print << "EOM";
<h1>カジノ</h1>
<hr size=0>
<FONT SIZE=3>
<B>受付</B><BR>
「いらっしゃいませ、$chara[4]様。<br>
　ここはお金を賭けて大金を手に入れる場所です。<br>
　倍率が高く、賭けるお金が高いほど賞金が高くなります<br>
　しかし、外れるとお金がガクっと減りますのでご注意してください。」</font>
<hr>
手持ち金:$chara[19]ギル<br>
現在カジノレベルは１～３まであります。<br>
１～３になるにつれ、失敗時の減少金額が変わります。<br>
カジノレベル１の倍率:$bai_a\%<br>
カジノレベル２の倍率:$bai_b\%<br>
カジノレベル３の倍率:$bai_c\%<br>
<table width=50%>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">カジノレベル１</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">賭けるお金を指定してください
<input type="text" name="c_bai1" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_1>
<input type=submit class=btn value="賭ける">
</td></form>
</tr>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">カジノレベル２</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">賭けるお金を指定してください
<input type="text" name="c_bai2" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_2>
<input type=submit class=btn value="賭ける">
</td></form>
</tr>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">カジノレベル３</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">賭けるお金を指定してください
<input type="text" name="c_bai3" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_3>
<input type=submit class=btn value="賭ける">
</td></form>
</tr>
</table>
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="ステータス画面へ">
</form>

EOM
	&footer;
	exit;
}

#----------------#
#--第一賭金部屋--#
#----------------#
sub bai_1{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai1'} eq "") { &error("賭け金が空白です！$back_form"); }

	if($in{'c_bai1'} <= 0) {&error("マイナスは入力出来ません。$back_form");
	}elsif($in{'c_bai1'} > $chara[19]) {&error("そんなにお金を所持していません。$back_form");
	}else {
		$baibai = int(rand($bai_atta1));
			if($baibai==0){
				$seikou = $bai_a * $in{'c_bai1'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>おめでとうございます！！</b></font><br><br>賭けに成功し、$seikouＧ手に入れました！！</center>";
				&all_message("$chara[4]さんがカジノレベル１にて賭けに成功し<font color=gold>$seikou</font>Ｇ手に入れました。");
				if($chara[106]==1){
$al_mes .= "<b><font size=4 color=red>クエスト「スーパーギャンブラー」をクリア！</font></b><br>";
$al_mes .= "<b><font size=3 color=red>報酬250000Gを手に入れた！</font></b><br>";
				$chara[19] += 250000;
				$chara[106] = 2;

			}
			}else{
				$sippai = $in{'c_bai1'} * (int(rand(5)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>残念でした</b></font><br><br>賭けに失敗し所持金$sippaiＧ減りました・・・</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>カジノレベル１</h1>
<br><center>賭け結果です。
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="まだ挑戦する">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
	&footer;

	exit;
}

#----------------#
#--第二賭金部屋--#
#----------------#
sub bai_2{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai2'} eq "") { &error("賭け金が空白です！$back_form"); }

	if($in{'c_bai2'} <= 0) {&error("マイナスは入力出来ません。$back_form");
	}elsif($in{'c_bai2'} > $chara[19]) {&error("そんなにお金を所持していません。$back_form");
	}else {
		$baibai = int(rand($bai_atta2));
			if($baibai==0){
				$seikou = $bai_b * $in{'c_bai2'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>おめでとうございます！！</b></font><br><br>賭けに成功し、$seikouＧ手に入れました！！</center>";
				&all_message("$chara[4]さんがカジノレベル２にて賭けに成功し<font color=gold>$seikou</font>Ｇ手に入れました。");
			}else{
				$sippai = $in{'c_bai2'} * (int(rand(10)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>残念でした</b></font><br><br>賭けに失敗し所持金$sippaiＧ減りました・・・</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>カジノレベル２</h1>
<br><center>賭け結果です。
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="まだ挑戦する">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
	&footer;

	exit;
}
#----------------#
#--第三賭金部屋--#
#----------------#
sub bai_3{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai3'} eq "") { &error("賭け金が空白です！$back_form"); }

	if($in{'c_bai3'} <= 0) {&error("マイナスは入力出来ません。$back_form");
	}elsif($in{'c_bai3'} > $chara[19]) {&error("そんなにお金を所持していません。$back_form");
	}else {
		$baibai = int(rand($bai_atta3));
			if($baibai==0){
				$seikou = $bai_a * $in{'c_bai3'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>おめでとうございます！！</b></font><br><br>賭けに成功し、$seikouＧ手に入れました！！</center>";
				&all_message("$chara[4]さんがカジノレベル３にて賭けに成功し<font color=gold>$seikou</font>Ｇ手に入れました。");
			}else{
				$sippai = $in{'c_bai3'} * (int(rand(5)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>残念でした</b></font><br><br>賭けに失敗し所持金$sippaiＧ減りました・・・</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>カジノレベル３</h1>
<br><center>賭け結果です。
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="まだ挑戦する">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
	&footer;

	exit;
}