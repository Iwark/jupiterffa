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
<h1>�`���b�g���U��</h1>
<font size=4>
�`���b�g�����[��ԏ����āA�C���p�N�g��^���܂��B�{���ɂ�낵���ł����H�H<br>
�r�炵���ȊO�A���ցB���O�����Ɏg���̂͐�΂ɂ�߂Ă��������B<br>
�����ƁA�Ȍ�P���ԁA�N�������ł��Ȃ��Ȃ�܂��B
</font>
<hr size=0>
EOM
if($chara[18]>10000 or $chara[0] eq "jupiter"){
	print <<"EOM";
<form action="kougeki.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kougeki">
<input type=submit class=btn value="�U������">
</form>
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub kougeki {

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($wday==0){$ww="��";}if($wday==1){$ww="��";}if($wday==2){$ww="��";}if($wday==3){$ww="��";}if($wday==4){$ww="��";}
	if($wday==5){$ww="��";}if($wday==6){$ww="�y";}
	$eg="$chara[4]�l���`���b�g�����U�����܂����B$chara[18]�̃_���[�W�I�I";
	$chatmes[0]="<>���m<>$year�N$mon��$mday��($ww)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>$koktime<>\n";
	unshift(@chatmes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");
	open(OUT,">$chat_file");
	print OUT @chatmes;
	close(OUT);

	&unlock($lock_file,'MS');


	&header;

	print <<"EOM";
<h1>�U�����܂���</h1>
<hr size=0>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}