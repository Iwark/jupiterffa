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

	$back_form = << "EOM";
<br>
<form action="isisouko.cgi" method="post">
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

	open(IN,"./kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	&header;

	print <<"EOM";
<h1>�f�ޑq��</h1>
<hr size=0>

<FONT SIZE=3>
<B>�f�ޑq�ɊǗ��l</B><BR>
�u
$chara[4]�l����a�����Ă���f�ށE�A�C�e���͉��̂悤�ɂȂ��Ă���܂�
�v
</FONT>
<br><hr><br>
<table width = "100%">
<tr>
<td width = "45%" align = "center" valign = "top">
�f��
<table width = "98%">
<tr><th></th><th></th><th nowrap>�Ȃ܂�</th><th nowrap>����</th></tr>
EOM
	$i = 0;
	foreach (@isi) {
		if($_ > 0){
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			$g=0;
			foreach(@sozai_data){
				($sozainame) = split(/<>/);
				if($g == $i) {last;}
				$g++;
			}

			print << "EOM";
<tr>
<form action="isisouko.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="�g��" disabled>
</td>
</form>
<form action="isisouko.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_delete">
<input type=submit class=btn value="����" disabled>
</td>
</form>
<td class=b1 nowrap>$sozainame</td>
<td class=b1 nowrap>$_</td>
</tr>
EOM
		}
		$i++;
	}
	print << "EOM";
</table>
</td>
<td width = "45%" align = "center" valign = "top">
�A�C�e��
<table width = "98%">
<tr><th></th><th></th><th nowrap>�Ȃ܂�</th></tr>
</table>
</td></table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}