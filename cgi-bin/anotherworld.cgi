#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
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
<form action="./anotherworld.cgi" >
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

&item_view;

exit;

#----------------#
#  �y�b�g�\���@  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�V���E�ւ̓����</h1>
<hr size=0>

<FONT SIZE=3>
<B>�������l</B><BR>
�u�L�~�́A�A�A���������Ă���̂����E�E�E�H�v
</FONT>
<br>
EOM
if($chara[18] > 3000){
	print <<"EOM";
<form action="./anotherworld.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=music>
<input type=submit class=btn value="�������l�̎����">
</form>
EOM
}
	print <<"EOM";
<form action="./anotherworld.cgi" >
<table>
EOM
if($chara[130]){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="1"></td>
	<td>�W���s�^���[���h��(0G)</td></tr>
EOM
}
if($chara[131] and $chara[140]!=2){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="2"></td>
	<td>�C�G���[���[���h��(10���f)</td></tr>
EOM
}
if($chara[132] and $chara[140]!=3){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="3"></td>
	<td>���b�h���[���h��(20���f)</td></tr>
EOM
}
if($chara[133] and $chara[140]!=4){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="4"></td>
	<td>�h���S�����[���h��(30���f)</td></tr>
EOM
}
if($chara[315] and $chara[140]!=5){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="5"></td>
	<td>�V�E��(�P���f)</td></tr>
EOM
}
if($chara[40]>1000000000000 and $chara[37]>=1000){
	print <<"EOM";
	<tr><td class=b1 align="center">
	<input type=radio name=world_no value="6"></td>
	<td>�`���C�i�ցH</td></tr>
EOM
}
if(!$chara[130] and !$chara[131] and !$chara[132] and !$chara[133]){
	print <<"EOM";
	���������Ă܂���B
EOM
}
else{
	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=goto_world>
<input type=submit class=btn value="�V���E��">
</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub goto_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'world_no'}==6){
		$com = "��������";
		$com2 = <<"EOM";
		���́A�`���C�i�̃����E�����Ƃ����҂���ˁB���Ȃ����X��������ˁB�����Ȃ�ˁH
	<form action="./anotherworld.cgi" >
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=oneone>
	<input type=submit class=btn value="�Ȃ�">
	</form>
EOM
	}else{
		if($in{'world_no'}==2){$ps_gold=100000;}
		if($in{'world_no'}==3){$ps_gold=200000;}
		if($in{'world_no'}==4){$ps_gold=300000;}
		if($in{'world_no'}==5){$ps_gold=100000000;}
		if($chara[19]<$ps_gold){&error("����������܂���$back_form");}
		else{$chara[19] = $chara[19] - $ps_gold;}
	
		if($chara[130]!=1){$chara[130]=1;}
		else{$chara[130]=0;}

		$chara[140] = $in{'world_no'};
		$com = "�ړ��������܂����B";
		$com2 = "�C�����āE�E�E�B";
	}

	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$com</B><BR>
�u$com2�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub music {

	&chara_load;

	&chara_check;

	&header;
	$musicno=int(rand(10));
	if($musicno==0){ $musicname="�X�N�����[�r���́u�s�A�m�\\�i�^�S�ԁv"; }
	elsif($musicno==1){ $musicname="�J�v�[�X�`���́u�R���T�[�g�G�`���[�hop40-2�v"; }
	elsif($musicno==2){ $musicname="�V���[�}���́uPresto Passionato�v"; }
	elsif($musicno==3){
		$musicname="�t�@�����̑g�ȁu���͖��p�t�v���u�΍Ղ�̗x��v";
		if($chara[259]==1){
			$musiccom = << "EOM";
<font color="red" size=4>
���A����͖��p�t�̍��I�I�I���ꂪ����΂���ɏ�B���邼�I<br>
��������Ă͂���Ȃ����H
</font>
<form action="./anotherworld.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tama>
<input type=hidden name=tama value=259>
<input type=submit class=btn value="����">
</form>
EOM
		}
	}
	elsif($musicno==4){ $musicname="�V���p���́u�s�A�m�\\�i�^�R��op58 ��P�y�́v"; }
	elsif($musicno==5){ $musicname="���X�g�́u����Z�I���K�ȁ@��P�O�ԁv"; }
	elsif($musicno==6){ $musicname="�x�[�g�[���F���́u�s�A�m�\\�i�^��P�S��op27-2�w�����x��R�y�́v"; }
	elsif($musicno==7){ $musicname="�A���x�j�X�́u�C�x���A��3�� ��7�� �G���E�A���o�C�V���v"; }
	elsif($musicno==8){ $musicname="���t�}�j�m�t�́u�O�t��op3 ��Q�ԁw���x�v"; }
	elsif($musicno==9){ $musicname="�h�r���b�V�[�́u�f�� ��1�W �w���̔��f(���ɉf��e)�x�v"; }

	print <<"EOM";
<FONT SIZE=3>
<B>�������l�͎��̓s�A�j�X�g�������̂��I</B><BR>
�������l��$musicname��e���͂��߂��B</font><br>
$musiccom
<hr size=0>
	$back_form
EOM

	$new_chara=$chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub tama {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[259]<1){&error("��������܂���$back_form");}
	else{$chara[259] -= 1;}

	$chara[305]+=365;
	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�s�A�j�X�g</B><BR>
�u���肪�Ƃ����������I<br>
����ɏh���݂�365�����悤�I<br>
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub oneone {

	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
	$chara[14]=61;
	$chara[33]=1;
	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>��������</B><BR>
�����������������������I</font><br>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}