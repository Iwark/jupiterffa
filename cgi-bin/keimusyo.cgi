#!/usr/local/bin/perl

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
<form action="keimusyo.cgi" method="post">
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

	&header;

	print <<"EOM";
<h1>�Y����</h1>
�ǂ������񂾂��H
<hr size=0>
EOM
if($chara[63]>=1){
	print <<"EOM";
<form action="keimusyo.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="syussyo">
<input type=submit class=btn value="�o������">($chara[63] G)
</form>
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub syussyo {

	&chara_load;

	&chara_check;

	if($chara[19]<$chara[63]){&error("����������܂���");}
	else{$chara[19] -= $chara[63];}

	$chara[63]=0;

	if($chara[65]>50){
		$chara[64]+=1;
		$chara[65]-=1;
	}elsif($chara[64]>50){
		$chara[65]+=1;
		$chara[64]-=1;
	}
	&chara_regist;

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		if($chara[0] eq "jupiter"){
			if(int(rand(4)) == 0){
				$eg="$chara[4]�l���Y�������Ԃ��󂵂ĒE�����܂����B";
			}elsif(int(rand(4)) == 0){
				$eg="$chara[4]�l���Y�����̔Ԑl���ÎE���ĒE�����܂����B";
			}elsif(int(rand(4)) == 0){
				$eg="$chara[4]�l���Y�����̔Ԑl�Ƃ̎����̖��E�����܂����B";
			}else{
				$eg="$chara[4]�l���Y������j�󂵂ĒE�����܂����B";
			}
		}else{
			$eg="$chara[4]�l���Y��������o�����܂����B";
		}
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');


	&header;

	print <<"EOM";
<h1>�o�����܂���</h1>
<hr size=0>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}