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
<form action="takara.cgi" method="post">
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
<h1>�󂭂���</h1>
<hr size=0>
<FONT SIZE=3>
<B>�l��</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�󂭂��𔃂��ɂ����悤���ȁB5���f�����B���������x�����Ă��Ӗ��͂Ȃ��B�Ō�̔ԍ��œ��[�����̂��B<br>
�S���̐�������͂���񂾁B�ςȓ��͂�����Ɩ����[�ɂȂ��Ă��܂����璍�ӂ���񂾂��B�v
</FONT>
<hr size=0>
<form action="takara.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
�ԍ��F<input type="text" name="p_id" value="" size=40><br>
<br>�@�@
<input type=submit class=btn value="���[����">
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
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($in{'p_id'} eq "") {
		&error("�󂭂��̐��l�����͂���Ă��܂���B$back_form");
	}
	if (length($in{'p_id'}) > 4) {
		&error("�󂭂��̐��l���������܂��B$back_form");
	}
	if ($in{'p_id'} =~ m/[^0-9]/){
		&error("�󂭂��̐��l�ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
	}
	if($chara[19] < 50000) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - 50000; }

	open(IN,"bango.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;

	$ppt=0;$iz=0;
	foreach(@member_data){
		($id,$suuti) = split(/<>/);
		if($id eq $chara[0]){$member_data[$iz]="$chara[0]<>$chara[4]<>$in{'p_id'}<>\n";$ppt=1;}
		$iz++;
	}
	if($ppt==0){push(@member_data,"$chara[0]<>$chara[4]<>$in{'p_id'}<>\n");}

	open(OUT,">bango.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�l��</B><BR>
�u50000G�g���ē��[���܂����v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}