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
<form action="ivent.cgi" method="post">
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

&jyoho;

&error;

exit;

#----------#
#  ���  #
#----------#
sub jyoho {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�C�x���g���</h1>
<hr size=0>
<FONT SIZE=3>
<B>��t�̐l</B><BR>
�u<B>$chara[4]</B>�l�ł��ˁA�ǂ���������ցB<br>�v
</FONT>
<br>���݂̏������F$chara[19] �f
<hr size=0>
	<form action="./ivent.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=jyoho_buy>
	<table>
	<tr>
	<th></th><th>�C�x���g��</th><th>�i�i</th><th>�Q����p</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000 and !$chara[91]) {print "<input type=radio name=ps_no value=1>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>�G�b�O�G���W�F������</th><th>�G�b�O�\\�[�h</th>
	<th>200000�f</th><th>�G�b�O�G���W�F����|���ƕK���G�b�O�\\�[�h����I(1�x�̂�)</th></tr>
	<th>

	</table>
	<br><br>
	<input type=submit class=btn value="�C�x���g���󂯂�">
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
sub jyoho_buy {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("�C�x���g��I��ł�������$back_form"); }
	if ($in{'ps_no'}==1){$ps_gold = 200000;}

	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	if($in{'ps_no'}==1){
		$chara[91]=1;
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>��t�̐l</B><BR>
�u�撣���Ă��������ˁI�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
