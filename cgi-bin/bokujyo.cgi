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
<form action="bokujyo.cgi" >
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

&item_view;

exit;

#----------------#
#  ペット表示　  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	foreach(@log_item){
		($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/);
		if(!$i_no or !$i_name){splice(@acs_array,$g,1);$hit=1;}
		else{$g++;}
	}
	if($hit==1){
		open(OUT,">pets/$chara[0].cgi");
		print OUT @log_item;
		close(OUT);
	}

	&header;

	print <<"EOM";
<h1>牧場</h1>
<hr size=0>

<FONT SIZE=3>
<B>牧場管理人</B><BR>
「
$chara[4]様に預かっているペットは下のようになっております
」
</FONT>
<br><hr>現在のペット<br>
EOM
if($chara[138] eq ""){$peename=$chara[39];}else{$peename=$chara[138];}
if($chara[38]>3000){
	print <<"EOM";
<form action="bokujyo.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
<input type=submit class=btn value="渡す">$peename
</form>
EOM
}
	print <<"EOM";
預けているペット
<table>
<tr><th></th><th nowrap>なまえ</th><th nowrap>レベル</th><th nowrap>ＨＰ</th><th nowrap>攻撃力</th></tr>
EOM
	$i = 0;
	foreach (@log_item) {
		($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/);
		if($i_namae eq ""){$pename=$i_name;}else{$pename=$i_namae;}
		print << "EOM";
<tr>
<form action="bokujyo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="引き取る">
</td>
</form>
<td class=b1 nowrap>$pename</td>
<td align=right class=b1>$i_lv</td>
<td align=right class=b1>$i_hp</td>
<td align=right class=b1>$i_damage</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[38]==3000){ &error("壊れた卵は預かれません！"); }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	$log_item[$in{'item_no'}] =~ s/\n//g;
	$log_item[$in{'item_no'}] =~ s/\r//g;

	($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/,$log_item[$in{'item_no'}]);

	if($chara[38]){
		$log_item[$in{'item_no'}] = "$chara[38]<>$chara[39]<>$chara[40]<>$chara[41]<>$chara[43]<>$chara[44]<>$chara[45]<>$chara[46]<>$chara[47]<>$chara[138]<>\n";
	}
	else{
		$log_item[$in{'item_no'}] = ();
	}

	open(OUT,">pets/$chara[0].cgi");
	print OUT @log_item;
	close(OUT);
	$chara[38]=$i_no;
	$chara[39]=$i_name;
	$chara[40]=$i_exp;
	$chara[41]=$i_maxexp;
	$chara[43]=$i_hp;
	$chara[44]=$i_damage;
	$chara[45]=$i_image;
	$chara[46]=$i_lv;
	$chara[47]=$i_ps;
	$chara[138]=$i_namae;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	print <<"EOM";
<FONT SIZE=3>
<B>$penameを引き取りました</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム売る  #
#----------------#
sub item_sell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($chara[38]==3000){ &error("壊れた卵は預かれません！"); }

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"pets/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= 20) {
		&error("牧場がペットでいっぱいです！$back_form");
	}

	push(@souko_item,"$chara[38]<>$chara[39]<>$chara[40]<>$chara[41]<>$chara[43]<>$chara[44]<>$chara[45]<>$chara[46]<>$chara[47]<>$chara[138]<>\n");

	open(OUT,">pets/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	$chara[38]=0;
	$chara[39]="";
	$chara[40]=0;
	$chara[41]=0;
	$chara[43]=0;
	$chara[44]=0;
	$chara[45]=0;
	$chara[46]=0;
	$chara[47]=0;
	$chara[138]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ペットを引き取ってもらいました</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
