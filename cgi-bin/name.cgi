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
<form action="name.cgi" method="post">
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
<h1>���O�ύX��</h1>
<hr size=0>
<FONT SIZE=3>
<B>���O�ύX���̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
���O�ύX���������̂��E�E�E�H���ӓ_���B<br>
�@���O�ύX�͂Q�T�ԂɂP�x�̂݁B�ύX������100��G���B<br>
�A���L�����̖��O��A�Q�[�����L�����N�^�[�ɍ����������O�͐�΂ɂ��Ȃ��ł��������B<br>
�B���̑��A�s����A�����点�Ǝv����悤�Ȗ��O�ɂ����ꍇ�A���炩�̑Ώ�������܂��B�v
</FONT>
<br>���݂̏������F$chara[19] �f
<hr size=0>
	<form action="./name.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=jyoho_buy>
�V�������O�@�F<input type="text" name="new_name" value="" size=40><br>
	<input type=submit class=btn value="�ύX����">
	</form>
	�F�F�F�F�ύX�����F�F�F�F
	<table>
	<tr><th>�����O</th><th>�V���O</th><th>�ύX��</th></tr>
EOM
	open(IN,"allname.cgi");
	@member_data = <IN>;
	close(IN);

	foreach(@member_data){
		($old_name,$new_name,$henko_day) = split(/<>/);
		print <<"EOM";
		<tr><th>$old_name</th><th>$new_name</th><th>$henko_day</th></tr>
EOM
	}
	print "</table>";
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

$koutime=time();

	if ($in{'new_name'} eq ""){ &error("�ύX���������O����͂��Ă��������B$back_form"); }
	elsif ($name_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[4] eq $in{'new_name'}) {
				close(IN);
				&error("���ꖼ�̃L�����N�^�[�����܂��B$back_form");
			}
		}
	}
	elsif(int($koutime/1209600)>$chara[96]-1){&error("�O�񖼑O��ύX���Ă���2�T�Ԍo���Ă��܂���$back_form");}
	$ps_gold = 1000000;

	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[1] eq $chara[4]){
			$array[1]=$in{'new_name'};
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[1] eq $chara[4]){
			$array[1]=$in{'new_name'};
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	$old_name=$chara[4];
	$chara[4]=$in{'new_name'};
	$chara[94]=int($koutime/1209600);
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$boa="<font color=\"yellow\">$old_name�l���A$in{'new_name'}�l�ɁA���O�ύX���Ȃ����܂����I</font>";

	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<>$boa<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	open(IN,"allname.cgi");
	@member_data = <IN>;
	close(IN);

	push(@member_data,"$old_name<>$in{'new_name'}<>$year�N$mon��$mday��(��)$hour��$min��<>\n");

	open(OUT,">allname.cgi");
	print OUT @member_data;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���O�ύX���̃}�X�^�[</B><BR>
�u���O�̕ύX�������������B
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
