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
<form action="seityo.cgi" >
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
	if($item[20]==10){$g="red";}else{$g="";}
	if($item[22]==10){$w="red";}else{$w="";}
	if($chara[24]<1016){$rare1=1;}
	elsif($chara[24]<1031){$rare1=2;}
	elsif($chara[24]<1046){$rare1=3;}
	elsif($chara[24]<1061){$rare1=4;}
	elsif($chara[24]<1076){$rare1=5;}
	else{$rare1=10;}
	if($chara[29]<2016){$rare2=1;}
	elsif($chara[29]<2031){$rare2=2;}
	elsif($chara[29]<2046){$rare2=3;}
	elsif($chara[29]<2061){$rare2=4;}
	elsif($chara[29]<2076){$rare2=5;}
	else{$rare2=10;}
	$bukikoka = "攻撃力 $item[1]<br>命中率 $item[2]<br>効果 $item[24]";
	$bogukoka = "防御力 $item[4]<br>回避率 $item[5]<br>効果 $item[25]";
	$acskoka = "効果 $item[19]";

	&header;

	print <<"EOM";
<h1>成長所</h1>
<hr size=0>

<FONT SIZE=3>
<B>成長所の人</B><BR>
「装備を成長させることができるぞ。値段は、ランク×100000Ｇだが、特殊な装備は1000000Gだぞ。<br>
成長するかどうかは、装備の強さ、そして運次第だっ。稀に壊れるから注意するんだなっ<br>
高成長ボタンだと、成長する確率が上がる。代わりに壊れる確率も上がるぞ。」
</FONT><br>
所持金：$chara[19]G
<br><hr>現在の装備<br>
<table>
<tr>
<td id="td2" class="b2">武器</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
EOM
	if ($chara[24] > 1090 and $chara[24] < 1101){
	}elsif($chara[24] > 1200 and $chara[24] < 1228){
	}elsif ($chara[24] and $chara[24]>0 and $chara[24]<4000 and $chara[19]>$rare1*100000 and $chara[24]!=1400) {
	print <<"EOM";
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=submit class=btn value="成長">
</td>
</form>
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=hidden name=kou value=1>
<input type=submit class=btn value="高成長">
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
	if ($chara[29] > 2090 and $chara[29] < 2101){
	}elsif($chara[29] > 2200 and $chara[29] < 2228){
	}elsif ($chara[29] and $chara[29]>0 and $chara[29]<4000 and $chara[19] > $rare2*100000) {
	print <<"EOM";
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=submit class=btn value="成長">
</td>
</form>
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=hidden name=kou value=1>
<input type=submit class=btn value="高成長">
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

	if($chara[24]==1240 and $chara[135]>2){$rare1=1000000;}
	elsif($chara[24]<1016){$rare1=1;}
	elsif($chara[24]<1031){$rare1=2;}
	elsif($chara[24]<1046){$rare1=3;}
	elsif($chara[24]<1061){$rare1=4;}
	elsif($chara[24]<1076){$rare1=5;}
	else{$rare1=10;}

	if($chara[19] < $rare1*100000){&error("お金が足りませんよー。");}
	else{$chara[19] -= $rare1*100000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[20]<5){$ss=20;}
	elsif($item[20]<7){$ss=30;}
	elsif($item[20]<9){$ss=40;}
	elsif($item[20]<11){$ss=50;}
	$kowa=0;
	if($in{'kou'}==1){$ss+=10;$kowa=5;}
	if($rr<$ss+2 or $chara[93]){
		$chara[24]+=1;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit,$si_koka) = split(/<>/);
			if($chara[24]==1241 and $chara[135]>2){
				$chara[24]=1339;
				$item[0]="時空剣";
				$item[1]=0;
				$item[2]=0;
				$item[20]=0;
				$item[21]=0;
				$si_koka="裸で時空を飛ぶ(？)";
				$item[24]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[24] == 1005 and $in{'kou'}==1){
				$chara[24]=1131;
				$item[0]="げっちゅう";
				$item[1]=1;
				$item[2]=-100;
				$item[20]=0;
				$item[21]=0;
				$si_koka="モンスターを捕らえられるぞっ！";
				$item[24]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[24] eq "$si_no"){
				$item[0]=$si_name;
				$item[1]=$si_dmg;
				$item[2]=$si_hit;
				$item[20]=0;
				$item[21]=0;
				if(!$si_koka){$si_koka="特になし";}
				$item[24]=$si_koka;
				$hit=1;
				last;
			}
		}
		if(!$hit) {$chara[24]-=1;}
		$mes="成長に成功しました";
	}else{
		if(int(rand(10))>$kowa){$mes="成長に失敗しました";
		}else{
		if($item[1]>504){$chara[85]+=50000;}
		elsif($item[1]>203){$chara[85]+=10000;}
		elsif($item[1]>152){$chara[85]+=1000;}
		elsif($item[1]>93){$chara[85]+=300;}
		elsif($item[1]>43){$chara[85]+=75;}
		else{$chara[85]+=1;}
		&item_lose;
		$chara[24]=0;
		$mes="成長に失敗し、さらに壊れてしまった！！";
		}
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
	if($chara[29]<2016){$rare2=1;}
	elsif($chara[29]<2031){$rare2=2;}
	elsif($chara[29]<2046){$rare2=3;}
	elsif($chara[29]<2061){$rare2=4;}
	elsif($chara[29]<2076){$rare2=5;}
	else{$rare2=10;}

	if($chara[19] < $rare2*100000){&error("お金が足りませんよー。");}
	else{$chara[19] -= $rare2*100000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[22]<5){$ss=20;}
	elsif($item[22]<7){$ss=30;}
	elsif($item[22]<9){$ss=40;}
	elsif($item[22]<11){$ss=50;}
	$kowa=0;
	if($in{'kou'}==1){$ss+=10;$kowa=5;}
	if($rr<$ss+2 or $chara[93]){
		$chara[29]+=1;
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit,$si_koka) = split(/<>/);
			if($chara[29] == 2132 and $in{'kou'}==1){
				$chara[29]=2134;
				$item[3]="七角帽子";
				$item[4]=208;
				$item[5]=70;
				$item[22]=0;
				$item[23]=0;
				$si_koka="高成長した帽子";
				$item[25]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[29] == 2133 and $in{'kou'}==1){
				$chara[29]=2143;
				$item[3]="リミッター";
				$item[4]=500;
				$item[5]=50;
				$item[22]=0;
				$item[23]=0;
				$si_koka="封印の印がある。";
				$item[25]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[29] eq "$si_no"){
				$item[3]=$si_name;
				$item[4]=$si_dmg;
				$item[5]=$si_hit;
				$item[22]=0;
				$item[23]=0;
				if(!$si_koka){$si_koka="特になし";}
				$item[25]=$si_koka;
				$hit=1;
				last;
			}
		}
		if(!$hit) {$chara[29]-=1;}
		$mes="成長に成功しました";
	}else{
		if(int(rand(10))>$kowa){
			$mes="成長に失敗しました";
		}else{
		if($item[4]>704){$chara[85]+=50000;}
		elsif($item[4]>404){$chara[85]+=10000;}
		elsif($item[4]>199){$chara[85]+=1000;}
		elsif($item[4]>103){$chara[85]+=100;}
		elsif($item[4]>52){$chara[85]+=10;}
		else{$chara[85]+=1;}
		&def_lose;
		$chara[29]=0;
		$mes="成長に失敗し、さらに壊れてしまった！！";
		}
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