#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = "images/hosi01.gif";
$midi = $shop_midi;

	$back_form = << "EOM";
<br>
<form action="seirank.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  �A�C�e���\��  #
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
<h1>�����L���O</h1>
�P���Ɉ�񂭂炢�X�V����܂��B
<form action="seirank.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=hidden name="mode" value="syoku">
<input type=submit class=btn value="�E�Ɛl�C���[">
</form>
<hr size=0>

<FONT SIZE=5>
<table><tr><td>
<B>���x�������L���O</B><BR>
�u	�P�ʁF$bsortdata[0]P<br>
	�Q�ʁF$bsortdata[1]P<br>
	�R�ʁF$bsortdata[2]P<br>
	�S�ʁF$bsortdata[3]P<br>
	�T�ʁF$bsortdata[4]P<br>
	�U�ʁF$bsortdata[5]P<br>
	�V�ʁF$bsortdata[6]P<br>
	�W�ʁF$bsortdata[7]P<br>
	�X�ʁF$bsortdata[8]P<br>
	10�ʁF$bsortdata[9]P�v<br>
</td>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<td>
<B>���Z�ꏟ�������L���O</B><BR>
�u	�P�ʁF$gsortdata[0]P<br>
	�Q�ʁF$gsortdata[1]P<br>
	�R�ʁF$gsortdata[2]P<br>
	�S�ʁF$gsortdata[3]P<br>
	�T�ʁF$gsortdata[4]P<br>
	�U�ʁF$gsortdata[5]P<br>
	�V�ʁF$gsortdata[6]P<br>
	�W�ʁF$gsortdata[7]P<br>
	�X�ʁF$gsortdata[8]P<br>
	10�ʁF$gsortdata[9]P�v<br>
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
<B>�y�n�����N�����L���O</B><BR>
�u	�P�ʁF$csortdata[0]P<br>
	�Q�ʁF$csortdata[1]P<br>
	�R�ʁF$csortdata[2]P<br>
	�S�ʁF$csortdata[3]P<br>
	�T�ʁF$csortdata[4]P<br>
	�U�ʁF$csortdata[5]P<br>
	�V�ʁF$csortdata[6]P<br>
	�W�ʁF$csortdata[7]P<br>
	�X�ʁF$csortdata[8]P<br>
	10�ʁF$csortdata[9]P�v<br>
</td><td>
<B>���Y�x�����L���O</B><BR>
�u	�P�ʁF$dsortdata[0]P<br>
	�Q�ʁF$dsortdata[1]P<br>
	�R�ʁF$dsortdata[2]P<br>
	�S�ʁF$dsortdata[3]P<br>
	�T�ʁF$dsortdata[4]P<br>
	�U�ʁF$dsortdata[5]P<br>
	�V�ʁF$dsortdata[6]P<br>
	�W�ʁF$dsortdata[7]P<br>
	�X�ʁF$dsortdata[8]P<br>
	10�ʁF$dsortdata[9]P�v<br>
</td><td>
<B>�]���񐔃����L���O</B><BR>
�u	�P�ʁF$esortdata[0]P<br>
	�Q�ʁF$esortdata[1]P<br>
	�R�ʁF$esortdata[2]P<br>
	�S�ʁF$esortdata[3]P<br>
	�T�ʁF$esortdata[4]P<br>
	�U�ʁF$esortdata[5]P<br>
	�V�ʁF$esortdata[6]P<br>
	�W�ʁF$esortdata[7]P<br>
	�X�ʁF$esortdata[8]P<br>
	10�ʁF$esortdata[9]P�v<br>
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
	<h1>�����L���O</h1>
	<br>
	<h3>�����̐E�Ƃɓ��[���邱�Ƃ��o���܂��B
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
	print "</table></h3><input type=submit class=btn value=\"���[\"></form>";

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
		if($r_syoku[0] eq $chara[0] and $in{'no'} == $r_syoku[1]){&error("���̐E�Ƃɂ͂������[���܂���");}
	}
	push(@syoku_rank,"$chara[0]<>$in{'no'}<>\n");

	open(OUT,">./data/syokurank.cgi");
	print OUT @syoku_rank;
	close(OUT);

	&header;

	print <<"EOM";
	<h1>�����L���O</h1>
	<br>
	<h3>���[���܂����B<br>
<form action="seirank.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=hidden name="mode" value="syoku">
<input type=submit class=btn value="�߂�">
</form>
	<hr>
	<br>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}