#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��3�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#�@FF ADVENTURE ��i v2.1
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE v0.21
#�@programed by CUMRO
#�@http://cgi.members.interq.or.jp/sun/cumro/mm/
#�@cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(��) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B     	#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B   	#
#---------------------------------------------------------------#
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
<form action="ippatu.cgi" method="post">
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
<h1>�ꔭ�t�]�V���b�v</h1>
<hr size=0>
<FONT SIZE=3>
<B>�V���b�v�̓X���̑��̗F�B</B><BR>
�u��H�A�N�A�������������̂��B��邶��Ȃ��B<br>
�ꔭ�t�]�V���b�v�ւ悤�����B�����ł́A�N�������𔃂��̂łȂ��A�l���N�̗E�C�𔃂���B<br>
�����A<br>
�N���l�̌������Ƃ𐬌������邱�Ƃ��ł�����A<br>
�N�̖]�ޕ��������悤�Ǝv����B<br>
�������A�������ł��Ȃ��������̎��́A<br>
�^�C�w���Ȃ��ƂɂȂ邩��Ȃ��I�I�I�I�I�I�I�I�I�I�I�I�I<br>
���킵�������x����I�����ȁB������΍����قǓ�����A��V���傫����B�v
</FONT>
<hr size=0>
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
EOM
if($chara[191]!=1 and $chara[191]!=2){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="1">�X�[�p�[�C�[�W�[<br>
EOM
}
if($chara[192]!=1 and $chara[192]!=2){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="2">�C�[�W�[<br>
EOM
}
if($chara[193]!=1 and $chara[193]!=2 and $chara[64] > 90){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="3">�P�l���[�h<br>
EOM
}
	print <<"EOM";
<br>�@�@
<input type=submit class=btn value="���킷��">
</form>
EOM
if($chara[191]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=191>
<br>�@�@
<input type=submit class=btn value="�X�[�p�[�C�[�W�[�N���A��V���󂯎��">
</form>
EOM
}
if($chara[192]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=192>
<br>�@�@
<input type=submit class=btn value="�C�[�W�[�N���A��V���󂯎��">
</form>
EOM
}
if($chara[193]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=193>
<br>�@�@
<input type=submit class=btn value="�P�l���[�h�N���A��V���󂯎��">
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
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$cylv=$in{'cylv'};

	if($cylv == 1){
		$chara[191]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�悵�A�N�ɂ���Ă��炤���Ƃ������悤�B<br>
		����́A�A�A���������퉮�̓X���|�����ƁI<br>
		�������A�|�����Ƃɐ���������A�܂������֖߂��Ă���Ƃ����B
		�v</font>
		<hr size=0>
EOM
	}elsif($cylv == 2){
		$chara[192]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�悵�A�N�ɂ���Ă��炤���Ƃ������悤�B<br>
		����́A�A�A���������퉮�̓X�傩�畐��𓐂ނ��ƁI<br>
		�����ɂ͍��݂����邩��ȁE�E�E��<br>
		�������A�|�����Ƃɐ���������A�܂������֖߂��Ă���Ƃ����B
		�v</font>
		<hr size=0>
EOM
	}elsif($cylv == 3){
		$chara[193]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�����āA�N�̂��ׂ����Ƃ͋����Ȃ���B<br>
		����̐l�Ƒ��k���Ă���Ă݂Ȃ��I<br>
		�q���g�́A�A�����������B<br>
		��[���s���Ă����I���s�����珈�Y�������I�v</font>
		<hr size=0>
EOM
	}elsif($cylv == 4){
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u��[���s���Ă����I���s�����珈�Y�������I�v</font>
		<hr size=0>
EOM
	}elsif($cylv == 5){
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u��[���s���Ă����I���s�����珈�Y�������I�v</font>
		<hr size=0>
EOM
	}else{
		&error("���x����ݒ肵�Ă��܂���B$back_form");
	}

	&shopfooter;

	&footer;

	exit;
}
sub hosh {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$cqu=$in{'cqu'};

	if($cqu == 191){
		$chara[191]=0;
		if(int(rand(100))<80){
			$hoos=10000000;
		}elsif(int(rand(100))<99){
			$hoos=30000000;
		}else{
			$hoos=50000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�悭������ȁI����A��V�Ƃ��āA$hoos�f��낤�B
		�v</font>
		<hr size=0>
EOM
	}elsif($cqu == 192){
		$chara[192]=0;
		if(int(rand(100))<80){
			$hoos=30000000;
		}elsif(int(rand(100))<99){
			$hoos=50000000;
		}else{
			$hoos=80000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�悭������ȁI����A��V�Ƃ��āA$hoos�f��낤�B
		�v</font>
		<hr size=0>
EOM
	}elsif($cqu == 193){
		$chara[193]=0;
		if(int(rand(100))<80){
			$hoos=70000000;
		}elsif(int(rand(100))<99){
			$hoos=100000000;
		}else{
			$hoos=130000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u�悭������ȁI����A��V�Ƃ��āA$hoos�f��낤�B
		�v</font>
		<hr size=0>
EOM
	}elsif($cqu == 194){
		$chara[194]=0;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u��[���s���Ă����I���s�����珈�Y�������I�v</font>
		<hr size=0>
EOM
	}elsif($cqu == 195){
		$chara[195]=0;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>�V���b�v�̓X���̑��̗F�B</B><BR>
		�u��[���s���Ă����I���s�����珈�Y�������I�v</font>
		<hr size=0>
EOM
	}else{
		&error("���x����ݒ肵�Ă��܂���B$back_form");
	}

	&shopfooter;

	&footer;

	exit;
}