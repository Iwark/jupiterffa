#!/usr/local/bin/perl

#------------------------------------------------------#
#  能力屋ver1.00
#  by 霧雨
#  drop@cgi-games.com
#  http://cgi-games.com/drop/
#------------------------------------------------------#

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

# 能力を１上げるのに必要なポイント
$nouryoku_gold = 1;

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
<form action="shop_ability.cgi" >
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
if($chara[70]<1){$maxpoint= 200 + $chara[37] * 5;}else{$maxpoint=$chara[18]*2;}
if($chara[55]==70){$maxpoint+=2500;$coma="※静アビリティ明るい未来作りによって、最大ポイントが増加しています。";}
if($chara[56]==70){$maxpoint+=2500;$coma="※静アビリティ明るい未来作りによって、最大ポイントが増加しています。";}
if($chara[57]==70){$maxpoint+=2500;$coma="※静アビリティ明るい未来作りによって、最大ポイントが増加しています。";}
if($chara[58]==70){$maxpoint+=2500;$coma="※静アビリティ明るい未来作りによって、最大ポイントが増加しています。";}
	print << "EOM";
<h1>能\力屋</h1><hr>
<br>現在のポイント：$chara[35]<br></font>
能\力を1上げるのに$nouryoku_gold\ポイント必要です。<br>
EOM
if($chara[70]!=1){print "1つのステータスに上げられる最大ポイントは200＋転生回数×5なので、$maxpointです。";}
else{print "1つのステータスに上げられる最大ポイントはレベル×２なので、$maxpointです。";}
print "<br>$coma";
	print << "EOM";
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<tr><td id="td2">STR(力)</td> 
<td align="right" class="b2">$chara[7] +<input type="text" name="up1" size="4"></td></tr>
<tr><td id="td2">INT(魔力)</td>
<td align="right" class="b2">$chara[8] +<input type="text" name="up2" size="4"></td></tr>
<tr><td id="td2">DEX(命中)</td>
<td align="right" class="b2">$chara[9] + <input type="text" name="up3" size="4"></td></tr>
<tr><td id="td2">VIT(HP)</td>
<td align="right" class="b2">$chara[10] + <input type="text" name="up4" size="4"></td></tr>
<tr><td id="td2">LUK(運)</td>
<td align="right" class="b2">$chara[11] + <input type="text" name="up5" size="4"></td></tr>
<tr><td id="td2">EGO(必殺)</td>
<td align="right" class="b2">$chara[12] + <input type="text" name="up6" size="4"></td></tr>
</tr>
</table>
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="能\力を振る"></form>

EOM
if(!$chara[35]){$chara[35]=0;}
$goldneed = $chara[18] * 500;
	print << "EOM";
<h3>能\力\初\期\化</h3>
<br>
能\力の初期化にはレベル×500G必要です。<br><br>
現在の所持金：$chara[19]G<br><br>
必要なおかね：$goldneed G<br>　<br>　
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<input type="hidden" name="mode" value="kounyuu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="能\力を初\期\化する"></form>
EOM
if($chara[177]==2){
	print << "EOM";
<h3>レベルダウン</h3>
<br>
レベルを１０％ダウンさせることで、クエストを受けなおすことができます。<br><br>
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<input type="hidden" name="mode" value="lvdown">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="レベルダウンする"></form>
EOM
}
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

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'IM');
	&chara_load;
	&chara_check;

if(!$chara[35]){$chara[35]=0;}
if($chara[70]<1){$maxpoint= 200 + $chara[37] * 5;}else{$maxpoint=$chara[18]*2;}
if($chara[55]==70){$maxpoint+=2500;}
if($chara[56]==70){$maxpoint+=2500;}
if($chara[57]==70){$maxpoint+=2500;}
if($chara[58]==70){$maxpoint+=2500;}

	if($in{'up1'} eq "" and $in{'up2'} eq "" and $in{'up3'} eq "" and $in{'up4'} eq "" 
		and $in{'up5'} eq "" and $in{'up6'} eq "") { &error("記入されてません。"); }

	if ($in{'up1'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'up2'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'up3'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'up4'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'up5'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'up6'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	
	if($chara[35] < $in{'up1'} * $nouryoku_gold + $in{'up2'} * $nouryoku_gold +
			$in{'up3'} * $nouryoku_gold + $in{'up4'} * $nouryoku_gold +
			$in{'up5'} * $nouryoku_gold + $in{'up6'} * $nouryoku_gold)
		{ &error("ポイントが足りません$back_form"); }

	if($chara[7] + $in{'up1'} > $maxpoint){&error("STRが限界を突破しています。$back_form");}
	if($chara[8] + $in{'up2'} > $maxpoint){&error("INTが限界を突破しています。$back_form");}
	if($chara[9] + $in{'up3'} > $maxpoint){&error("DEXが限界を突破しています。$back_form");}
	if($chara[10] + $in{'up4'} > $maxpoint){&error("VITが限界を突破しています。$back_form");}
	if($chara[11] + $in{'up5'} > $maxpoint){&error("LUKが限界を突破しています。$back_form");}
	if($chara[12] + $in{'up6'} > $maxpoint){&error("EGOが限界を突破しています。$back_form");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'IM');

	$chara[7] = $chara[7] + $in{'up1'};
	$chara[8] = $chara[8] + $in{'up2'};
	$chara[9] = $chara[9] + $in{'up3'};
	$chara[10] = $chara[10] + $in{'up4'};
	if($in{'up4'}){
		if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
			$chara[16] += int((rand($in{'up4'}*2)+$in{'up4'})*100000);
		}else{
			$chara[16] = $chara[16] + int((rand($in{'up4'}*2)+$in{'up4'})*1000);
		}
	}
	$chara[15] = $chara[16];
	$chara[11] = $chara[11] + $in{'up5'};
	$chara[12] = $chara[12] + $in{'up6'};

	$chara[35] = $chara[35] - $in{'up1'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up2'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up3'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up4'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up5'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up6'} * $nouryoku_gold;

	&chara_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
能\力を振りました。

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="戻る"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}

#--------------------#
#   購入部分         #
#--------------------#
sub kounyuu {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[19] < $chara[18] * 500) { &error("お金が足りません"); }
if($chara[70]<1){
	$chara[16] = $kiso_hp + ($chara[18]-1) * 400;
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + $chara[37] * 20 - 4;
}else{
	if($chara[18]<=100){$hpup=($chara[18]-1) * 300;}
	elsif($chara[18]<=200){$hpup =30000 + ($chara[18]-101) * 500;}
	elsif($chara[18]<=500){$hpup =80000 + ($chara[18]-201) * 800;}
	elsif($chara[18]<=1000){$hpup = 320000 + ($chara[18]-501) * 1000;}
	elsif($chara[18]<=2000){$hpup = 820000 + ($chara[18]-1001) * 1200;}
	else{$hpup =2020000 + ($chara[18]-2001) * 1500;}
	$chara[16] = $kiso_hp + $hpup;
	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		$chara[16]= $chara[16]*100;
	}
	$chara[15] = $chara[16];
	$point=0;
	if($chara[55]==70){$point+=2500;}
	if($chara[56]==70){$point+=2500;}
	if($chara[57]==70){$point+=2500;}
	if($chara[58]==70){$point+=2500;}
	$chara[7] = 1+$point;
	$chara[8] = 1+$point;
	$chara[9] = 1+$point;
	$chara[10] = 1+$point;
	$chara[11] = 1+$point;
	$chara[12] = 1+$point;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + 20 - 4;
}
	&chara_regist;

	&header;

	print <<"EOM";
能\力を初\期\化しました。

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="戻る"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}
sub lvdown {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[177] != 2) { &error("エラー。"); }
if($in{'kakunin'}==1){
	$ccccc=151;
	for($ccccc=151;$ccccc<180;$ccccc++){
		$chara[$ccccc]=0;
	}
	$chara[18]-=int($chara[18]/10);
	if($chara[18]<=100){$hpup=($chara[18]-1) * 300;}
	elsif($chara[18]<=200){$hpup =30000 + ($chara[18]-101) * 500;}
	elsif($chara[18]<=500){$hpup =80000 + ($chara[18]-201) * 800;}
	elsif($chara[18]<=1000){$hpup = 320000 + ($chara[18]-501) * 1000;}
	elsif($chara[18]<=2000){$hpup = 820000 + ($chara[18]-1001) * 1200;}
	else{$hpup =2020000 + ($chara[18]-2001) * 1500;}
	$chara[16] = $kiso_hp + $hpup;
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[35] = $chara[18] * 4 + 20 - 4;
	$chara[188]++;

	&chara_regist;

	&header;
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様がレベルダウンをしました。";

	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');
	print <<"EOM";
レベルダウンを終了しました。ステータスがリセットされているので注意。

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="戻る"></form>

EOM
}else{
	&chara_regist;
	&header;
	print <<"EOM";
本当にレベルダウンをしてもいいですか？
<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvdown">
<input type="hidden" name="kakunin" value=1>
<input type="submit" class="btn" value="する"></form>

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="戻る"></form>
EOM
}
	&shopfooter;

	&footer;

	exit;
}