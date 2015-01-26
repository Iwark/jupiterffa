#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
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
<form action="sihai.cgi" method="post">
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

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	$g=0;
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
		$g++;
	}

	$sihai_data[$g]="$sihaisya[0]<>$sihaisya[1]<>$sihaisya[2]<>$sihaisya[3]<>$sihaisya[4]<>$sihaisya[5]<>$sihaisya[6]<>$sihaisya[7]<>$sihaisya[8]<>$sihaisya[9]<>$sihaisya[10]<>$sihaisya[11]<>$sihaisya[12]<>$sihaisya[13]<>$sihaisya[14]<>$sihaisya[15]<>$sihaisya[16]<>$sihaisya[17]<>$sihaisya[18]<>$sihaisya[19]<>$sihaisya[20]<>\n";

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);

	$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);
if(!$sihaisya[15]){$sihaisya[15]=0;}
	print <<"EOM";
<h1>支配者施設</h1>
<hr size=0>
<FONT SIZE=3>
<B>マスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
支配者との戦闘ができるのは限られた時のみだ。(詳しくは掲示板)<br>
支配者との戦いに勝利すると、支配者ダンジョンの設定ができるぞ。<br>
支配者との戦いでは、アビリティが(お互い)発動しないぞ。<br>
ただし、ペットの持ち込みが可\能\だ。」<p>
現在の支配者：$sihaisya[1]
</FONT>
<hr size=0>
EOM
if($mday != 3 and $mday != 6 and $mday != 9 and $mday != 12 and $mday != 15 and $mday != 18 and $mday != 21 and $mday != 24 and $mday != 27 and $mday != 30){print "今日は支配者との戦闘はできません。";}
elsif($sihaisya[1] ne $chara[4]){
	print <<"EOM";
現在の支配者：$sihaisya[1]
<form action="./sihaibattle.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sihai>
<input type=submit class=btn value="戦う">
</form>
EOM
}
if($sihaisya[1] eq $chara[4]){
	print <<"EOM";
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="支配者ダンジョンの設定">
</form>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<input type=submit class=btn value="入場料による収入を受け取る($sihaisya[15] G)">
</form>
<p>
EOM
}
	print <<"EOM";
<p>
<FONT SIZE=3.3><br>
<font size=4>現在の設定：</font><br>
ポイント：$point ポイント<br>
入場料：$sihaisya[2] Ｇ<br>
出現モンスター名：<br>
・$sihaisya[3]<br>
・$sihaisya[4]<br>
・$sihaisya[5]<br>
・$sihaisya[6]<br>
・$sihaisya[7]<br>
・$sihaisya[8]<br>
・$sihaisya[9]<br>
・$sihaisya[10]<br>
モンスター出現数：$sihaisya[11] 体<br>
経験値倍率：$sihaisya[12] 倍<br>
取得金倍率：$sihaisya[13] 倍<br>
<p>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub settei {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);

	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}

	&header;

	$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);

	print <<"EOM";
<FONT SIZE=3.3><br>
<font size=4>現在の設定：</font><br>
注意：ポイントが１００００ポイントをオーバーしていると支配者ダンジョンに行けなくなります。<br><br>
ポイント：$point ポイント<br>
入場料：$sihaisya[2] Ｇ<br>
出現モンスター名：<br>
・$sihaisya[3]<br>
・$sihaisya[4]<br>
・$sihaisya[5]<br>
・$sihaisya[6]<br>
・$sihaisya[7]<br>
・$sihaisya[8]<br>
・$sihaisya[9]<br>
・$sihaisya[10]<br>
モンスター出現数：$sihaisya[11] 体<br>
経験値倍率：$sihaisya[12] 倍<br>
取得金倍率：$sihaisya[13] 倍<br>
<p>
<font size=4>設定の変更：</font>
<p>
モンスターの設定：Ｎｏ．に1～8までの数字を入力し、設定ボタンを押す。<br>
<table><tr><td class=b1>No.</td><td class=b1></td><td class=b1>モンスター名</td><td class=b1>ポイント</td></tr>
EOM

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);
	$i=0;
	foreach (@mons_data) {
		@mons = split(/<>/);
		if($sihaisya[3] ne $mons[0] and $sihaisya[4] ne $mons[0] and $sihaisya[5] ne $mons[0] and 		$sihaisya[6] ne $mons[0] and $sihaisya[7] ne $mons[0] and $sihaisya[8] ne $mons[0] and $sihaisya[9] ne $mons[0] and $sihaisya[10] ne $mons[0]){
		if($i %4 ==0){print "<tr>";}
		print <<"EOM";
		<form action="./sihai.cgi" method="post">
		<td class=b1>
		<input type="text" name="taisyo" size=5><br>
		</td>
		<td class=b1>
		<input type=hidden name=id value="$chara[0]">
		<input type=hidden name=mydata value="$chara_log">
		<input type=hidden name=mode value=okuru>
		<input type=hidden name=aite value=$mons[0]>
		<input type=hidden name=point value=$mons[2]>
		<input type=submit class=btn value="設定">
		</form>
		</td>
		<td class=b1>$mons[0]</td>
		<td class=b1>$mons[2]</td>
EOM
		if($i %4 ==3){print "<tr>";}
		$i++;
		}
	}

	print <<"EOM";
</table>
<p>
モンスター出現数、経験値とお金の倍率設定：Ｎｏ．に1～8までの数字を入力し、設定ボタンを押す。<br>
<form action="./sihai.cgi" method="post">
<table>
<tr><td class=b1>モンスター出現数</td>
<td class=b1>１体</td><td class=b1>２体</td><td class=b1>３体</td>
<td class=b1>４体</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=kazu value=1></td>
<td class=b1><input type=radio name=kazu value=2></td>
<td class=b1><input type=radio name=kazu value=3></td>
<td class=b1><input type=radio name=kazu value=4></td>
</tr>
<tr><td class=b1>お金</td>
<td class=b1>0.2倍</td><td class=b1>0.6倍</td><td class=b1>1.0倍</td>
<td class=b1>1.4倍</td><td class=b1>1.8倍</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=kane value=0.2></td>
<td class=b1><input type=radio name=kane value=0.6></td>
<td class=b1><input type=radio name=kane value=1.0></td>
<td class=b1><input type=radio name=kane value=1.4></td>
<td class=b1><input type=radio name=kane value=1.8></td>
</tr>
<tr><td class=b1>経験値</td>
<td class=b1>0.2倍</td><td class=b1>0.6倍</td><td class=b1>1.0倍</td>
<td class=b1>1.4倍</td><td class=b1>1.8倍</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=exp value=0.2></td>
<td class=b1><input type=radio name=exp value=0.6></td>
<td class=b1><input type=radio name=exp value=1.0></td>
<td class=b1><input type=radio name=exp value=1.4></td>
<td class=b1><input type=radio name=exp value=1.8></td>
</tr>
</table>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value="kk">
<input type=submit class=btn value="設定">
</form>
<p>
入場料の設定(10Ｇにつき1ポイント)：<br>
<form action="./sihai.cgi" method="post">
<input type="text" name="ryoukin" size=5><br>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=kane>
<input type=submit class=btn value="設定">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  情報買う　　  #
#----------------#
sub okuru {

	&chara_load;

	&chara_check;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if ($in{'taisyo'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。"); 
	}elsif($in{'taisyo'}>8 or $in{'taisyo'} <1){
		&error("数字は１～８までを入力してください。"); 
	}elsif(!$in{'aite'}){
		&error("モンスターが存在しません。"); 
	}else{
		$t=$in{'taisyo'}+2;
		$hit=0;
		foreach (@mons_data) {
			@mons = split(/<>/);
			if($mons[0] eq $sihaisya[$t]){$hit=1;last;}
		}
		$sihaisya[14] += $in{'point'};
		if($hit){$sihaisya[14] -= $mons[2];}
		$sihaisya[$t] = $in{'aite'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>モンスターを設定しました。</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="設定を続ける">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub kk {

	&chara_load;

	&chara_check;

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if(!$in{'kane'} or !$in{'exp'} or !$in{'kazu'}){
		&error("正しくモンスター出現数、お金と経験値を設定してください。");
	}else{
		$sihaisya[12] = $in{'exp'};
		$sihaisya[13] = $in{'kane'};
		$sihaisya[11] = $in{'kazu'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>モンスター出現数、お金と経験値を設定しました。</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="設定を続ける">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  情報買う　　  #
#----------------#
sub uketoru {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	$chara[19]+=$sihaisya[15];
	$sihaisya[15]=0;

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>収入を受け取りました。</B><BR>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub kane {

	&chara_load;

	&chara_check;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if ($in{'ryoukin'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。"); 
	}else{
		$sihaisya[2] = $in{'ryoukin'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>入場料を設定しました。</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="設定を続ける">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}