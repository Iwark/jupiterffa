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
$backgif = $shop_back;
$midi = $shop_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="yohou.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if($mode) { &$mode; }

&sakaba;

&error;

exit;

#----------#
#  ���  #
#----------#
sub sakaba {

	&chara_load;

	&chara_check;

	if(int(($mon+$mday*$hour)%20)==0){$yoho="�����A�h�����G�h����";}
	elsif(int(($mon*$mday)%7)<4){$yoho="�܂���͂����b�V��";}
	else{$yoho="�J��f�X�g�[�����b�V��";}

	&header;

	if ($mday % $mon ==5 or ($mon<6 and ($mday % $mon + 1) == 1 and $mday > 17)){
		if($hour < $wday*4 and $wday*4 < 24){
			$yoho1="�����͑�n�k�������������ł��I�I<br>";
		}elsif($hour == $wday*4){
			$yoho1="�n�k�����ԋ߁I�I�@���S�ȏꏊ�ɓ����Ă�������<br>";
		}elsif($hour > $wday*4){
			$yoho1="�C�G���[���[���h�ő�n�k���������܂������A���҂͋��Ȃ��悤�ł��B<br>";
		}
	}
	print <<"EOM";
<h1>�\\��\��</h1>
<hr size=0>
<FONT SIZE=3>
<B>�\\��\��</B><BR>
�u�����ł́A�V�C\�\\��Ȃǂ����邱�Ƃ��ł��܂��B<br>
�V�C�ɂ���ăh���b�v���Ȃǂ����E����Ȃ�Ă������M�����݂��܂��B<br>
���݂̓V�C�́c<font color="red" size=5>$yoho</font>�ł��B<br>
<font color="red" size=5>$yoho1 $yoho2</font>�v
</FONT>
<hr size=0>
<br>
EOM
if($chara[70]==1 and $chara[18] > 2000){
	print <<"EOM";
<form action="./yohou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=data>
<input type=submit class=btn value="���Z����">(1��G������܂�)
</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub data {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[19] < 100000000) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - 100000000; }

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');

	$jik=0;
	if($hour>=12){$jik=1;}
	open(IN,"./tougigold.cgi");
	@tougigold = <IN>;
	close(IN);
	foreach(@tougigold){
		@tgold = split(/<>/);
		if($tgold[0] eq $chara[0] and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){$kakekin=$tgold[4];$kakeno=$tgold[5];}
		if($tgold[1] == $year and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){
			${'tkazu'.$tgold[5]}++;
			${'tkane'.$tgold[5]}+=$tgold[4];
		}
	}
	$ykane=int(rand(4)+1);
	if(${'tkane'.$ykane}==0){${'tkane'.$ykane}=0;$ycomment="�N���q���Ă��Ȃ����炱���A�q���Ă݂�̂��ʔ����񂶂�Ȃ��H";}
	elsif(${'tkane'.$ykane}<1000){$ycomment="������_���Ă����̂��ǂ���������Ȃ���B";}
	elsif(${'tkane'.$ykane}<5000){$ycomment="�����Ɣ{�������Ƃ���A�Ȃ�������ˁB";}
	else{$ycomment="������R�������Ă�̂ˁB";}
	open(IN,"./tougi.cgi");
	@monster = <IN>;
	close(IN);
	$hit=0;
	foreach(@monster){
		@tmon = split(/<>/);
		if($tmon[0] == $mday){
			$hit=1;
			if($tmon[9]>=40){$mes="�����͏��R�������̌��ߎ�����肻���ˁB�{�������Ƃ����_���čs���Ƃ�����B";}
			elsif($tmon[9]>=25){$mes="�����͓���킢��B�q���Ȃ��̂��P�̎肩������Ȃ���B���R������r�炵�����B";}
			elsif($tmon[9]>=10){$mes="�����͌����ɍs�����Ƃ������߂����B�t�]�����N����Ȃ��Ƃ�����Ȃ����ǁB";}
			else{$mes="�����͂܂��Ɏ��͏����I�t�]���͊��҂��Ȃ������ǂ��Ǝv����B";}
			$mes.="<br>�Ƃ����$ykane�Ԗڂ̃����X�^�[�ɂ�${'tkane'.$ykane}���̃R�C�����������Ă���悤�ˁB<br>";
			$mes.=$ycomment;
			last;
		}
	}
	if($hit!=1){$mes="�����͂܂����Z�ꂪ�J�n���Ă��܂���B";}

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$mes<br>
</font>
<br>
<form action="yohou.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	$chara[303]=$mday + $mon + $year;

	open(IN,"./dcharalog/$in{'id'}.cgi") || &error("$in{'id'}�L�����N�^�[��($!)������܂���$ENV{'CONTENT_LENGTH'}");
	$chara_log2 = <IN>;
	close(IN);

	@chara2 = split(/<>/,$chara_log2);

	if($chara2[303] == $mday + $mon + $year){
		&error("���݂܂���A�����͕����ł��܂���B�����A�����Ă��������B(�o�O���p�΍�)");
	}
	elsif($chara[70] == 1 or $chara[37] > 40){
		&error("���Ȃ��̃L�����͏�����Ƃ͎v���Ȃ������ł��B");
	}
	else{
		open(OUT,">./charalog/$in{'id'}.cgi");
		print OUT $chara_log2;
		close(OUT);
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
�����ɕ������������܂����I�I<br>
</font>
<br>
<form action="kinkyuu.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub hukugen2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	for($noo=0;$noo<200;$noo++){
		if($in{$noo}){$chara[$noo]=$in{$noo};}
	}
	if($in{'70'}==1){
		for($nooo=101;$nooo<128;$nooo++){
			$chara[$nooo]=2;
		}
	}
	$enew_chara = '';

	$enew_chara = join('<>',@chara);

	$enew_chara .= '<>';

	open(OUT,">./echaralog/$in{'id'}.cgi");
	print OUT $enew_chara;
	close(OUT);

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
����\�\\��\���܂����B���̕�����<font color="red">�蓮</font>�ōs���܂��B<br>
�f���Ȃǂ�ʂ��āA����\�\\��\�����������Ƃ��Ǘ��l�Ɉꌾ�`���Ă��������B<br>
���͂����l�ł����B<br>
</font>
<br>
<form action="kinkyuu.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}