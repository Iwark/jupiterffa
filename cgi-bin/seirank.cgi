#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# アイテムライブラリの読み込み
require 'item.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# このファイル用設定
$backgif = "images/hosi01.gif";
$midi = $shop_midi;

	$back_form = << "EOM";
<br>
<form action="seirank.cgi">
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

	open(IN,"./data/boss.ini");
	@boss_data = <IN>;
	close(IN);

	&all_data_read;

	$hit=0;$ahit=0;$i=0;$es=0;$sima = $ltime;$iphit=0;$tc=0;
	foreach (@RANKING) {
		@sorr = split(/<>/);
		$fhogehoge[$i]="$sorr[0]<>$sorr[18]";
		$bhogehoge[$i]="$sorr[4],$sorr[18]";
		$ehogehoge[$i]="$sorr[4],$sorr[37]";
		$i++;
		$srdate = $sorr[27] + (60*60*24*$limit);
		$sniti = $srdate - $sima;
		$sniti = int($sniti / (60*60*24));
		$es++;
	}

	open(IN,"./allhatake.cgi");
	@hatake = <IN>;
	close(IN);
	$hata=0;
	foreach (@hatake) {
		($g_name,$g_rank,$g_seisan) = split(/<>/);
		$chogehoge[$hata]="$g_name,$g_rank";
		$dhogehoge[$hata]="$g_name,$g_seisan";
		$hata++;
	}

	open(IN,"./tougimons.cgi");
	@tougi = <IN>;
	close(IN);
	$tou=0;
	foreach (@tougi) {
		($t_name,$t_hp,$t_at,$t_hit,$t_waza,$t_ritu) = split(/<>/);
		$ghogehoge[$tou]="$t_name,$t_ritu";
		$tou++;
	}

	@bsortdata = reverse sort { (split(/\,/,$a))[1] <=> (split(/\,/,$b))[1] } @bhogehoge;
	@csortdata = reverse sort { (split(/\,/,$a))[1] <=> (split(/\,/,$b))[1] } @chogehoge;
	@dsortdata = reverse sort { (split(/\,/,$a))[1] <=> (split(/\,/,$b))[1] } @dhogehoge;
	@esortdata = reverse sort { (split(/\,/,$a))[1] <=> (split(/\,/,$b))[1] } @ehogehoge;
	@fsortdata = reverse sort { (split(/<>/,$a))[1] <=> (split(/<>/,$b))[1] } @fhogehoge;
	@gsortdata = reverse sort { (split(/\,/,$a))[1] <=> (split(/\,/,$b))[1] } @ghogehoge;
	#@sort_array = sort {$b <=> $a} @files;
	#@asort_array = sort {$b <=> $a} @afiles;

	splice(@fsortdata, 10);

	$new_array = '';
	$new_array = join('<>',@fsortdata);

	open(OUT,">llrank.cgi");
	print OUT $new_array;
	close(OUT);

	&header;

	print <<"EOM";
<h1>ランキング</h1>
１日に一回くらい更新されます。
<form action="seirank.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=hidden name="mode" value="syoku">
<input type=submit class=btn value="職業人気投票">
</form>
<hr size=0>

<FONT SIZE=5>
<table><tr><td>
<B>レベルランキング</B><BR>
「	１位：$bsortdata[0]P<br>
	２位：$bsortdata[1]P<br>
	３位：$bsortdata[2]P<br>
	４位：$bsortdata[3]P<br>
	５位：$bsortdata[4]P<br>
	６位：$bsortdata[5]P<br>
	７位：$bsortdata[6]P<br>
	８位：$bsortdata[7]P<br>
	９位：$bsortdata[8]P<br>
	10位：$bsortdata[9]P」<br>
</td>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<td>
<B>闘技場勝率ランキング</B><BR>
「	１位：$gsortdata[0]P<br>
	２位：$gsortdata[1]P<br>
	３位：$gsortdata[2]P<br>
	４位：$gsortdata[3]P<br>
	５位：$gsortdata[4]P<br>
	６位：$gsortdata[5]P<br>
	７位：$gsortdata[6]P<br>
	８位：$gsortdata[7]P<br>
	９位：$gsortdata[8]P<br>
	10位：$gsortdata[9]P」<br>
</td>
EOM
}else{
	print <<"EOM";
<td>
</td>
EOM
}
	print <<"EOM";
<td>
</td></tr>
<tr><td>
<B>土地ランクランキング</B><BR>
「	１位：$csortdata[0]P<br>
	２位：$csortdata[1]P<br>
	３位：$csortdata[2]P<br>
	４位：$csortdata[3]P<br>
	５位：$csortdata[4]P<br>
	６位：$csortdata[5]P<br>
	７位：$csortdata[6]P<br>
	８位：$csortdata[7]P<br>
	９位：$csortdata[8]P<br>
	10位：$csortdata[9]P」<br>
</td><td>
<B>生産度ランキング</B><BR>
「	１位：$dsortdata[0]P<br>
	２位：$dsortdata[1]P<br>
	３位：$dsortdata[2]P<br>
	４位：$dsortdata[3]P<br>
	５位：$dsortdata[4]P<br>
	６位：$dsortdata[5]P<br>
	７位：$dsortdata[6]P<br>
	８位：$dsortdata[7]P<br>
	９位：$dsortdata[8]P<br>
	10位：$dsortdata[9]P」<br>
</td><td>
<B>転生回数ランキング</B><BR>
「	１位：$esortdata[0]P<br>
	２位：$esortdata[1]P<br>
	３位：$esortdata[2]P<br>
	４位：$esortdata[3]P<br>
	５位：$esortdata[4]P<br>
	６位：$esortdata[5]P<br>
	７位：$esortdata[6]P<br>
	８位：$esortdata[7]P<br>
	９位：$esortdata[8]P<br>
	10位：$esortdata[9]P」<br>
</td></tr>
</FONT>
</table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

sub syoku {

	&chara_load;

	&chara_check;

	open(IN,"./data/syokurank.cgi");
	@syoku_rank = <IN>;
	close(IN);
	@ninki=();
	foreach (@syoku_rank) {
		@r_syoku = split(/<>/);
		$ninki[$r_syoku[1]]+=1;
	}

	&header;

	print <<"EOM";
	<h1>ランキング</h1>
	<br>
	<h3>複数の職業に投票することが出来ます。
	<hr>
	<br>
	<table>
	<form action="./seirank.cgi">
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=touhyou>
EOM

	for($i=0;$i<61;$i++){
		print "<tr><td><input type=radio name=no value=$i></td><td>$i</td><td>$chara_syoku[$i]</td><td>";
		for($t=0;$t<$ninki[$i];$t++){print "l";}
		print "</td></tr>";
	}
	print "</table></h3><input type=submit class=btn value=\"投票\"></form>";

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub touhyou {

	&chara_load;

	&chara_check;

	open(IN,"./data/syokurank.cgi");
	@syoku_rank = <IN>;
	close(IN);

	foreach (@syoku_rank) {
		@r_syoku = split(/<>/);
		if($r_syoku[0] eq $chara[0] and $in{'no'} == $r_syoku[1]){&error("その職業にはもう投票しました");}
	}
	push(@syoku_rank,"$chara[0]<>$in{'no'}<>\n");

	open(OUT,">./data/syokurank.cgi");
	print OUT @syoku_rank;
	close(OUT);

	&header;

	print <<"EOM";
	<h1>ランキング</h1>
	<br>
	<h3>投票しました。<br>
<form action="seirank.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=hidden name="mode" value="syoku">
<input type=submit class=btn value="戻る">
</form>
	<hr>
	<br>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}