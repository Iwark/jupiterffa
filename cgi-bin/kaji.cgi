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
<form action="kaji.cgi" method="post">
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

	&item_load;

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
if($item[20]==10 and $chara[24]==1400){$g="yellow";}elsif($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="pink";}else{$g="";}
	if($item[22]==10){$w="red";}else{$w="";}

	$bukikoka = "�U���� $item[1]<br>������ $item[2]<br>���� $item[24]";
	$bogukoka = "�h��� $item[4]<br>��� $item[5]<br>���� $item[25]";
	$acskoka = "���� $item[19]";

	&header;

	print <<"EOM";
<h1>�b�艮</h1>
<hr size=0>

<FONT SIZE=3>
<B>�b�艮�̐l</B><BR>
�u�{�S���z���鋭���́A���s����m�������邼�B�l�i�́A1��30000�f�����B�v
</FONT><br>
�������F$chara[19]G
<br><hr>���݂̑���<br>
<table>
<tr>
<td id="td2" class="b2">����</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
EOM
	if ($chara[24] and $chara[24]>0 and $chara[24]<4000 and $chara[19]>30000 and $item[20]<10) {
	print <<"EOM";
<form action="kaji.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=submit class=btn value="�b����">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
<tr>
<td id="td2" class="b2">�h��</td><td align="right" class="b2">
<A onmouseover="up('$bogukoka')"; onMouseout="kes()"><font color="$w">$item[3] $bogulv</font></A></td>
EOM
	if ($chara[29] and $chara[29]>0 and $chara[29]<4000 and $chara[19] > 30000 and $item[22]<10) {
	print <<"EOM";
<form action="kaji.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=submit class=btn value="�b����">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
</table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#------------#
#  ���푕��  #
#------------#
sub item_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19] < 30000){&error("����������܂����[�B");}
	else{$chara[19] -= 30000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[20]<4){$ss=100;}
	elsif($item[20]<6){$ss=80;}
	elsif($item[20]<8){$ss=50;}
	elsif($item[20]==8){$ss=20;}
	elsif($item[20]==9){$ss=10;}
	if($rr<$ss+2){$item[20]+=1;$item[21]=0;$item[1]+=1;$item[2]+=2;$mes="�����ɐ������܂���";}
	else{
		if($chara[24]==1400){$mes="�����Ɏ��s���܂���";}else{&item_lose;$chara[24]=0;$mes="�����Ɏ��s���܂���";}
	}
	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  �h���  #
#------------#
sub def_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19] < 30000){&error("����������܂����[�B");}
	else{$chara[19] -= 30000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[22]<4){$ss=100;}
	elsif($item[22]<6){$ss=80;}
	elsif($item[22]<8){$ss=50;}
	elsif($item[22]==8){$ss=20;}
	elsif($item[22]==9){$ss=10;}
	if($rr<$ss+2){$item[22]+=1;$item[23]=0;$item[4]+=1;$item[5]+=2;$mes="�����ɐ������܂���";}
	else{&def_lose;$chara[29]=0;$mes="�����Ɏ��s���܂���";}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}