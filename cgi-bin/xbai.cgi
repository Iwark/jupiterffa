#!/usr/bin/perl

#-----------------------------------------------------#
#---�q������------------------------------------------#
#---Edit by Right-Blue--------------------------------#
#---http://wsr.a-auc.jp/------------------------------#
#-----------------------------------------------------#

# ���{�ꃉ�C�u����
require 'jcode.pl';

# ���W�X�g���C�u����
require 'regist.pl';

# �����ݒ�̓ǂݍ���
require 'data/ffadventure.ini';

# �{���ݒ�
$bai1 = 50;
$bai2 = 999;
$bai3 = 9999;

# ��������m��(�f�t�H���g10�ł͓�����m����10����1)
$bai_atta1 = 10;
$bai_atta2 = 90;
$bai_atta3 = 200;

# �{���ݒ�Q
$bai_a = int(rand($bai1)) + 2;
$bai_b = int(rand($bai2)) + $bai1;
$bai_c = int(rand($bai3)) + $bai2;

$backgif = $shop_back;
$midi = $shop_midi;

#-------------------------[�ݒ�͂����܂�]-------------------------#
#-----------��������b�f�h��������l�̂ݕύX���Ă�������-----------#
#------------------------------------------------------------------#
&decode;

$back_form = << "EOM";
<br>
<form action="./xbai.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

if ($mode) { &$mode; }

&kake;

exit;
#------------#
#--��t���--#
#------------#
sub kake{

	&chara_load;

	&chara_check;

	&header;

	print << "EOM";
<h1>�J�W�m</h1>
<hr size=0>
<FONT SIZE=3>
<B>��t</B><BR>
�u��������Ⴂ�܂��A$chara[4]�l�B<br>
�@�����͂�����q���đ������ɓ����ꏊ�ł��B<br>
�@�{���������A�q���邨���������قǏ܋��������Ȃ�܂�<br>
�@�������A�O���Ƃ������K�N���ƌ���܂��̂ł����ӂ��Ă��������B�v</font>
<hr>
�莝����:$chara[19]�M��<br>
���݃J�W�m���x���͂P�`�R�܂ł���܂��B<br>
�P�`�R�ɂȂ�ɂ�A���s���̌������z���ς��܂��B<br>
�J�W�m���x���P�̔{��:$bai_a\%<br>
�J�W�m���x���Q�̔{��:$bai_b\%<br>
�J�W�m���x���R�̔{��:$bai_c\%<br>
<table width=50%>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">�J�W�m���x���P</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">�q���邨�����w�肵�Ă�������
<input type="text" name="c_bai1" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_1>
<input type=submit class=btn value="�q����">
</td></form>
</tr>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">�J�W�m���x���Q</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">�q���邨�����w�肵�Ă�������
<input type="text" name="c_bai2" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_2>
<input type=submit class=btn value="�q����">
</td></form>
</tr>
<tr>
<form action="xbai.cgi" method="post">
<td class="b1" align="center" colspan=2 id="td1">�J�W�m���x���R</td>
</tr>
<tr>
<td align="center" class="b1" id="td2">�q���邨�����w�肵�Ă�������
<input type="text" name="c_bai3" size=30>G</td>
<td align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=bai_3>
<input type=submit class=btn value="�q����">
</td></form>
</tr>
</table>
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>

EOM
	&footer;
	exit;
}

#----------------#
#--���q������--#
#----------------#
sub bai_1{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai1'} eq "") { &error("�q�������󔒂ł��I$back_form"); }

	if($in{'c_bai1'} <= 0) {&error("�}�C�i�X�͓��͏o���܂���B$back_form");
	}elsif($in{'c_bai1'} > $chara[19]) {&error("����Ȃɂ������������Ă��܂���B$back_form");
	}else {
		$baibai = int(rand($bai_atta1));
			if($baibai==0){
				$seikou = $bai_a * $in{'c_bai1'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>���߂łƂ��������܂��I�I</b></font><br><br>�q���ɐ������A$seikou�f��ɓ���܂����I�I</center>";
				&all_message("$chara[4]���񂪃J�W�m���x���P�ɂēq���ɐ�����<font color=gold>$seikou</font>�f��ɓ���܂����B");
				if($chara[106]==1){
$al_mes .= "<b><font size=4 color=red>�N�G�X�g�u�X�[�p�[�M�����u���[�v���N���A�I</font></b><br>";
$al_mes .= "<b><font size=3 color=red>��V250000G����ɓ��ꂽ�I</font></b><br>";
				$chara[19] += 250000;
				$chara[106] = 2;

			}
			}else{
				$sippai = $in{'c_bai1'} * (int(rand(5)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>�c�O�ł���</b></font><br><br>�q���Ɏ��s��������$sippai�f����܂����E�E�E</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>�J�W�m���x���P</h1>
<br><center>�q�����ʂł��B
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�܂����킷��">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
	&footer;

	exit;
}

#----------------#
#--���q������--#
#----------------#
sub bai_2{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai2'} eq "") { &error("�q�������󔒂ł��I$back_form"); }

	if($in{'c_bai2'} <= 0) {&error("�}�C�i�X�͓��͏o���܂���B$back_form");
	}elsif($in{'c_bai2'} > $chara[19]) {&error("����Ȃɂ������������Ă��܂���B$back_form");
	}else {
		$baibai = int(rand($bai_atta2));
			if($baibai==0){
				$seikou = $bai_b * $in{'c_bai2'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>���߂łƂ��������܂��I�I</b></font><br><br>�q���ɐ������A$seikou�f��ɓ���܂����I�I</center>";
				&all_message("$chara[4]���񂪃J�W�m���x���Q�ɂēq���ɐ�����<font color=gold>$seikou</font>�f��ɓ���܂����B");
			}else{
				$sippai = $in{'c_bai2'} * (int(rand(10)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>�c�O�ł���</b></font><br><br>�q���Ɏ��s��������$sippai�f����܂����E�E�E</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>�J�W�m���x���Q</h1>
<br><center>�q�����ʂł��B
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�܂����킷��">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
	&footer;

	exit;
}
#----------------#
#--��O�q������--#
#----------------#
sub bai_3{

	&chara_load;

	&chara_check;

	&get_host;

	$chara[26] = $host;

	if ($in{'c_bai3'} eq "") { &error("�q�������󔒂ł��I$back_form"); }

	if($in{'c_bai3'} <= 0) {&error("�}�C�i�X�͓��͏o���܂���B$back_form");
	}elsif($in{'c_bai3'} > $chara[19]) {&error("����Ȃɂ������������Ă��܂���B$back_form");
	}else {
		$baibai = int(rand($bai_atta3));
			if($baibai==0){
				$seikou = $bai_a * $in{'c_bai3'};
				$chara[19] += $seikou;
				$al_mes = "<font size=5 color=yellow><b>���߂łƂ��������܂��I�I</b></font><br><br>�q���ɐ������A$seikou�f��ɓ���܂����I�I</center>";
				&all_message("$chara[4]���񂪃J�W�m���x���R�ɂēq���ɐ�����<font color=gold>$seikou</font>�f��ɓ���܂����B");
			}else{
				$sippai = $in{'c_bai3'} * (int(rand(5)) + 1);
				$chara[19] -= $sippai;
				if($chara[19] < 0){
					$chara[19] = 0;
				}
					$al_mes = "<font size=3><b>�c�O�ł���</b></font><br><br>�q���Ɏ��s��������$sippai�f����܂����E�E�E</center>";
			}
		}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'RI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'RI');

	&header;

	print <<"EOM";
<h1>�J�W�m���x���R</h1>
<br><center>�q�����ʂł��B
<br><br>$al_mes<br>
<br><div align="center">
<form action="./xbai.cgi" method="post">
<input type="hidden" name="mode" value="kake">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�܂����킷��">
</form>
</div>
EOM

	print << "EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
	&footer;

	exit;
}