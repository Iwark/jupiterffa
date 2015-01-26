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
<form action="kaji.cgi" method="post">
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

	&item_load;

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
if($item[20]==10 and $chara[24]==1400){$g="yellow";}elsif($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="pink";}else{$g="";}
	if($item[22]==10){$w="red";}else{$w="";}

	$bukikoka = "攻撃力 $item[1]<br>命中率 $item[2]<br>効果 $item[24]";
	$bogukoka = "防御力 $item[4]<br>回避率 $item[5]<br>効果 $item[25]";
	$acskoka = "効果 $item[19]";

	&header;

	print <<"EOM";
<h1>鍛冶屋</h1>
<hr size=0>

<FONT SIZE=3>
<B>鍛冶屋の人</B><BR>
「＋４を越える強化は、失敗する確率があるぞ。値段は、1回30000Ｇだぞ。」
</FONT><br>
所持金：$chara[19]G
<br><hr>現在の装備<br>
<table>
<tr>
<td id="td2" class="b2">武器</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
EOM
	if ($chara[24] and $chara[24]>0 and $chara[24]<4000 and $chara[19]>30000 and $item[20]<10) {
	print <<"EOM";
<form action="kaji.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=submit class=btn value="鍛える">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
<tr>
<td id="td2" class="b2">防具</td><td align="right" class="b2">
<A onmouseover="up('$bogukoka')"; onMouseout="kes()"><font color="$w">$item[3] $bogulv</font></A></td>
EOM
	if ($chara[29] and $chara[29]>0 and $chara[29]<4000 and $chara[19] > 30000 and $item[22]<10) {
	print <<"EOM";
<form action="kaji.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=submit class=btn value="鍛える">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
</table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#------------#
#  武器装備  #
#------------#
sub item_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19] < 30000){&error("お金が足りませんよー。");}
	else{$chara[19] -= 30000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[20]<4){$ss=100;}
	elsif($item[20]<6){$ss=80;}
	elsif($item[20]<8){$ss=50;}
	elsif($item[20]==8){$ss=20;}
	elsif($item[20]==9){$ss=10;}
	if($rr<$ss+2){$item[20]+=1;$item[21]=0;$item[1]+=1;$item[2]+=2;$mes="強化に成功しました";}
	else{
		if($chara[24]==1400){$mes="強化に失敗しました";}else{&item_lose;$chara[24]=0;$mes="強化に失敗しました";}
	}
	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  防具装備  #
#------------#
sub def_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19] < 30000){&error("お金が足りませんよー。");}
	else{$chara[19] -= 30000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[22]<4){$ss=100;}
	elsif($item[22]<6){$ss=80;}
	elsif($item[22]<8){$ss=50;}
	elsif($item[22]==8){$ss=20;}
	elsif($item[22]==9){$ss=10;}
	if($rr<$ss+2){$item[22]+=1;$item[23]=0;$item[4]+=1;$item[5]+=2;$mes="強化に成功しました";}
	else{&def_lose;$chara[29]=0;$mes="強化に失敗しました";}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}