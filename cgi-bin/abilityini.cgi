#!/usr/local/bin/perl



# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

#--------------#
#�@���C�������@#
#--------------#

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

	$back_form = << "EOM";
<br>
<form action="abilityini.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

if ($mode) { &$mode; }

&ability;

exit;

#--------------------#
#   ���C�����       #
#--------------------#
sub ability{

	&chara_load;

	&chara_check;

	&header;
if(!$chara[35]){$chara[35]=0;}
$goldneed = $chara[18] * 500;
	print << "EOM";
<h1>�\\��\��\��\��\��</h1><hr>
<br>
�\\�͂̏������ɂ̓��x���~500G�K�v�ł��B<br><br>
���݂̏������F$chara[19]G<br><br>
�K�v�Ȃ����ˁF$goldneed G<br>�@<br>�@
<table width='20%' border=0>
<form action="abilityini.cgi" method="POST">
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�\\�͂���\��\������"></form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#--------------------#
#   �w������         #
#--------------------#
sub kounyu {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[19] < $chara[18] * 500) { &error("����������܂���$back_form"); }

	$chara[16] = $chara[16] - int((rand($chara[10]*2)+$chara[10])*10);
	if($chara[16] < $kiso_hp){$chara[16] = $kiso_hp;}
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + $chara[37] * 20 - 4;

	&chara_regist;

	&header;

	print <<"EOM";
�\\�͂���\��\�����܂����B

<form action="$script" method="POST">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}

