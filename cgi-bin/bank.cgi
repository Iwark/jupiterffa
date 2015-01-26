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
<form action="$script_bank" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("アクセスできません！！");
	}
}

if($mode) { &$mode; }

&bank_shop;

exit;

#----------#
# 銀行表示 #
#----------#
sub bank_shop {

	&chara_load;

	&chara_check;

	&money_check;

	if($noroi==1){&error("のろいがかかっていて銀行の扉が開かないッ");}
	if($chara[141]>1){&error("のろいがかかっていて銀行の扉が開かないッ");}

	if (!$chara[34]) { $chara[34] = 0; }

	if ($bank_max < $chara[34] + $chara[19]) {
		$bank_max_in = int(($bank_max - $chara[34]) / 1000);
	} else {
		$bank_max_in = int($chara[19] / 1000);
	}

	if ($gold_max < $chara[34] + $chara[19]) {
		$bank_max_out = int(($gold_max - $chara[19]) / 1000);
	} else {
		$bank_max_out = int($chara[34] / 1000);
	}
	if($bank_max_in>1000){
		$banin1=int($bank_max_in/1000);
		$banin2=$bank_max_in%1000;
		if($banin2<10){$banin2="00$banin2";}
		elsif($banin2<100){$banin2="0$banin2";}
		$bank_max_inh="$banin1,$banin2";
	}else{$bank_max_inh=$bank_max_in;}
	if($bank_max_out>1000){
		$banout1=int($bank_max_out/1000);
		$banout2=$bank_max_out%1000;
		if($banout2<10){$banout2="00$banout2";}
		elsif($banout2<100){$banout2="0$banout2";}
		$bank_max_outh="$banout1,$banout2";
	}else{$bank_max_outh=$bank_max_out;}
	&header;

	print <<"EOM";
<h1>銀行</h1>
<hr size=0>
<font Size="3"> $chara[4]さんの現在の<br>
　　　所持金：<b>$chara[19]</b>ギル  ／<br>
　　　　　　　預金可能\額　：<b><font color=$yellow>$bank_max_inh\,000</font></b>ギル<br>
　　　預金　：<b>$chara[34]</b>ギル／<br>
　　　　　　　引出可能\額  ：<b><font color=$yellow>$bank_max_outh\,000</font></b>ギル<br>
　　　金貨　：<b>$chara[136]</b>枚
</font><br>
<font color=$yellow><b>最高預け入れ額 $bank_maxギル</b></font>を超えた分は動物愛護団体に寄付されます。<br>
<form action="$script_bank" >
<input type="text" name="azuke" value="" size=10>000 ギル
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_sell>
<input type=submit class=btn value="ギルを預ける">
</form>
<form action="$script_bank" >
<input type="hidden" name="azuke" value="$bank_max_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_sell>
<input type=submit class=btn value="預けれるだけ預ける">
</form>
<form action="$script_bank" >
<input type="text" name=dasu value="" size=10>000 ギル
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_buy>
<input type=submit class=btn value="ギルを出す">
</form>
<form action="$script_bank" >
<input type="hidden" name=dasu value="$bank_max_out">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=bank_buy>
<input type=submit class=btn value="出せるだけ出す">
</form>
EOM
if($chara[70]>0){
	print <<"EOM";
<form action="$script_bank" >
<input type="text" name=dasu value="" size=10> 枚
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kin_buy>
<input type=submit class=btn value="金貨を買う">(1枚10億Ｇ＋手数料１億Ｇ)
</form>
<form action="$script_bank" >
<input type="text" name=dasu value="" size=10> 枚
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kin_sell>
<input type=submit class=btn value="金貨を売る">(1枚10億Ｇ)
</form>
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
# お金を出す #
#----------------#
sub bank_buy {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'dasu'} eq ""){
		&error("金額が入力されていません。$back_form");
	}

	if($in{'dasu'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}

	if($in{'dasu'} <= 0) {
		&error("マイナスは入力出来ません。$back_form");
	} else {
		$dasuru = int($in{'dasu'}) * 1000;
	}

	if ($dasuru  > $chara[34]) {
		&error("預金額を超えています！！$back_form");
	}

	if(!($in{'dasu'} > 0 && $in{'dasu'} <= $gold_max)) {
		&error("不正な値です！");
	}
	if($dasuru==1000000 and $chara[140]==3){
		$chara[83]=1;
	}
	&get_host;

	$chara[26] = $host;

	$chara[34] -= $dasuru;

	$chara[19] += $dasuru;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>ご利用ありがとうございました</h1><br>
$dasuruＧ引き出しました。
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
# 金貨を買う　　 #
#----------------#
sub kin_buy {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'dasu'} eq ""){
		&error("枚数が入力されていません。$back_form");
	}

	if($in{'dasu'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}

	if($in{'dasu'} <= 0) {
		&error("マイナスは入力出来ません。$back_form");
	} else {
		$dasuru = int($in{'dasu'});
	}

	if ($dasuru*1000000000+100000000  > $chara[19]) {
		&error("お金が足りません！！$back_form");
	}else{
		$chara[19] -= $dasuru*1000000000+100000000;
		$chara[136] += $dasuru;
	}

	&get_host;

	$chara[26] = $host;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>ご利用ありがとうございました</h1><br>
$dasuru枚の金貨を購入しました。
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
# 金貨を売る　　 #
#----------------#
sub kin_sell {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'dasu'} eq ""){
		&error("枚数が入力されていません。$back_form");
	}

	if($in{'dasu'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}

	if($in{'dasu'} <= 0) {
		&error("マイナスは入力出来ません。$back_form");
	} else {
		$dasuru = int($in{'dasu'});
	}

	if ($dasuru  > $chara[136]) {
		&error("金貨の所持数を超えています！！$back_form");
	}

	if(!($in{'dasu'} > 0 && $in{'dasu'}*1000000000 <= $gold_max)) {
		&error("不正な値です！");
	}

	&get_host;

	$chara[26] = $host;

	$chara[136] -= $dasuru;

	$chara[19] += $dasuru*1000000000;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>ご利用ありがとうございました</h1><br>
$dasuru枚の金貨を売却しました。
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
# お金を預ける   #
#----------------#
sub bank_sell {
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'azuke'} eq ""){
		&error("金額が入力されていません。$back_form");
	}

	if($in{'azuke'} =~ /[^0-9]/){
		&error('エラー！数値不正のため受け付けません');
	}

	if($in{'azuke'} <= 0) {
		&error("マイナスは入力出来ません。$back_form");
	} else {
		$azukeru = int($in{'azuke'}) * 1000;
	}

	if ($azukeru  > $chara[19]) {
		&error("所持金を超えています！！$back_form");
	}

	if(!($in{'azuke'} > 0 && $in{'azuke'} <= $gold_max)) {
		&error("不正な値です！");
	}

	&get_host;

	$chara[26] = $host;

	$chara[34] += $azukeru;

	$chara[19] -= $azukeru;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>ご利用ありがとうございました</h1><br>
$azukeruＧ預けました。
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  送金チェック  #
#----------------#
sub money_check {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	open(IN,"money.cgi");
	@money = <IN>;
	close(IN);
	$hit=0;
	foreach(@money){
		($i_id,$i_gold) = split(/<>/);
		if($chara[0] eq "$i_id") { $hit=1;last; }
		
	}
	if($hit==1){
		&header;
		$chara[34] += $i_gold;
		$money[$i_id] = ();
		$new_chara = $chara_log;
		&chara_regist;
		open(OUT,">money.cgi");
		print OUT @money;
		close(OUT);
		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
		print <<"EOM";
		<body onload="document.FRM.submit();" >
		<form Name="FRM"  action="bank.cgi">
		<input type=hidden name=id value="$in{'id'}">
		<input type="hidden" name="mydata" value="$new_chara">
		</form>
		</body>
EOM
	}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

}
