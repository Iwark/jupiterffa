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
<form action="kinkyuu.cgi" >
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

	&header;

	print <<"EOM";
<h1>�ً}��</h1>
<hr size=0>
<FONT SIZE=3>
<B>�ً}��</B><BR>
�u�ŋߔ������Ă���L�����o�O�΍�B<br>
�����Ńf�[�^��ۑ����Ă����ƁA�L�����������ɕ�������A�Ǝv���܂��B<br>
����ɂP�񂮂炢���Ă����Ɨǂ������ł��B<br>
���ɏ������Ă��܂����f�[�^�̕��A�Ή����A�����ŏo����悤�ɂ������Ƃ������Ă��܂����c�B<br>
�L�������������āAID��������܂���ƂȂ������́A<font color="red" size=5><b>����ID</b></font>�ŃL��������蒼���A�����֗��Ă��������B�v
<font color="red" size=5><b>���݁A�f�[�^�͎����ŕۑ������悤�ɂȂ��Ă��܂��B�蓮�ۑ��͒�~���B</b></font>
</FONT>
<hr size=0>
<br>
<form action="./kinkyuu.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=data>
<input type=submit class=btn value="�Ƃ肠�����f�[�^��ۑ�" disabled>
</form>
<form action="./kinkyuu.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=submit class=btn value="�f�[�^�𕜌�" disabled>(�������ȊO�̏ꍇ�ɉ����ƃo�O�̌����ɂȂ�܂��B)
</form>
<font size =5 color="red">���łɏ������Ă��܂����f�[�^���A(�ŏ���)(����ID�ŃL����������ē��͂��Ă�������)</font><br>
�ȉ��̕��A�ɕK�v�ȏ���S�Ĕ��p�p�����œ��͂��Ă��������B�i�����悻��\�\\���܂���j<br>
<font size =5 color="red">����ID�ŃL����������Ă���Αq�ɓ��A�q����A�E�Ɨ����Ȃǂ͎����ŕ������Ă���͂��ł�</font><br>
<form action="./kinkyuu.cgi" >
�A�r���e�B�|�C���g:<input type="text" name="13" value="" size=10><br>
���x��:<input type="text" name="18" value="" size=10><br>
������:<input type="text" name="19" value="" size=10><br>
�]����:<input type="text" name="37" value="" size=10><br>
�P�l�x:<input type="text" name="64" value="" size=10><br>
���l�x:<input type="text" name="65" value="" size=10><br>
�N���E��:<input type="text" name="69" value="" size=10>(�f�r���N���E���Ȃ�1�A�G���W�F���N���E���Ȃ�2�Ɠ���)<br>
�˔j�̗L��:<input type="text" name="70" value="" size=10>(�˔j��Ȃ�1�A�˔j�O�Ȃ�0�Ɠ���)<br>
�ł̐Ώ�����:<input type="text" name="71" value="" size=10><br>
������������:<input type="text" name="72" value="" size=10><br>
���Ώ�����:<input type="text" name="73" value="" size=10><br>
�󓤏�����:<input type="text" name="74" value="" size=10><br>
�_�[�N�}�^�[������:<input type="text" name="75" value="" size=10><br>
�Z�u���X�^�[������:<input type="text" name="76" value="" size=10><br>
�M���Ώ�����:<input type="text" name="77" value="" size=10><br>
�����̐Ώ�����:<input type="text" name="78" value="" size=10><br>
�_��Ώ�����:<input type="text" name="79" value="" size=10><br>
���҂̏؏�����:<input type="text" name="80" value="" size=10><br>
�鉤�̏؏�����:<input type="text" name="81" value="" size=10><br>
���G������:<input type="text" name="82" value="" size=10><br>
�����̂�͂�������:<input type="text" name="97" value="" size=10><br>
���ꍇ���Ώ�����:<input type="text" name="98" value="" size=10><br>
�����Ώ�����:<input type="text" name="99" value="" size=10><br>
��͂�������:<input type="text" name="100" value="" size=10><br>
�C�G���[���[���h�̌������̗L��:<input type="text" name="131" value="" size=10>(�L���1�A�������0)<br>
���b�h���[���h�̌������̗L��:<input type="text" name="132" value="" size=10>(�L���1�A�������0)<br>
�h���S�����[���h�̌������̗L��:<input type="text" name="133" value="" size=10>(�L���1�A�������0)<br>
���~�Ŏg��������:<input type="text" name="187" value="" size=10><br>
���x���_�E����(�˔j��):<input type="text" name="188" value="" size=10><br>
�ŋ�ԃ`�P�b�g������:<input type="text" name="189" value="" size=10><br>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen2>
<input type=submit class=btn value="�m�F">
</form>
EOM

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

	$chara[303]=$mday + $mon + $year;

	$dnew_chara = '';

	$dnew_chara = join('<>',@chara);

	$dnew_chara .= '<>';

	open(OUT,">./dcharalog/$in{'id'}.cgi");
	print OUT $dnew_chara;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
�L�����f�[�^��ۑ����܂����B<br>
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

sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

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