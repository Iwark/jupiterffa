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
<form action="haigo.cgi" method="post">
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

&haigo;

&error;

exit;

#----------#
#  �z����  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�z����</h1>
<hr size=0>
<FONT SIZE=3>
<B>�z�����̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�����ł̓y�b�g�ƃy�b�g�̔z�����ł��邺�E�E�E<br>
�܂��A�{�̂������Ă��ȁA��x�{�̂�a���Ă���A����������Ă��ȁB<br>
��������z�����Ă���E�E�E�v
</FONT>
<br>���݂̏������F$chara[19] �f
<hr size=0>
<br><br>
���ł���z��
<form action="./haigo.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=haigo_buy>
<table>
<tr>
<th>No.</th><th>�{��</th><th>����</th><th>���i</th></tr>

<th>001</th><th>�h���S��</th><th>�_�C�i�\\�[mini</th><th>500000G</th></tr>
EOM
if($chara[38]==3113 or $chara[38]==3103){
	$selection.="<option value=\"1\">001</option>\n";
}
	print <<"EOM";
<br><br>
</table><br>
<select name=questno>
<option value="no">�I�����Ă�������
$selection
</select>
<input type=submit class=btn value="�z��">
<br>
</table>
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
sub haigo_buy {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno'} eq 'no'){&error("�z����I�����Ă�������$back_form");}

	$quest_no = $in{'questno'};

	if($quest_no == 1){
		if($chara[48]==3113){
			$chara[38] = 3004;
			$chara[39] = "�h���S���G�b�O";
			$chara[40] = 0;
			$chara[41] = 100000;
			$chara[42] = 20000;
			$chara[43] = 20000;
			$chara[44] = 0;
			$chara[45] = 3;
			$chara[46] = 1;
			$chara[47] = 0;
			$chara[48] = 0;
		}
		elsif($chara[38]==3113){
			$chara[38] = 0;
			$chara[39] = "";
			$chara[40] = 0;
			$chara[41] = 0;
			$chara[42] = 0;
			$chara[43] = 0;
			$chara[44] = 0;
			$chara[45] = 0;
			$chara[46] = 0;
			$chara[47] = 0;
			$chara[48] =3113;
		}
		else{&error("�{�̂�n���Ă܂���$back_form");}
	}

	&chara_regist;

	&header;

	print <<"EOM";
<FONT SIZE=5><B>�������܂���</B></font><BR>
<FONT SIZE=3>
<B>�z�����̃}�X�^�[</B><BR>
�u�ӂӂӁB�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
