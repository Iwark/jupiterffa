#!/usr/local/bin/perl

#------------------------------------------------------#
#  �\�͉�ver1.00
#  by ���J
#  drop@cgi-games.com
#  http://cgi-games.com/drop/
#------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# �\�͂��P�グ��̂ɕK�v�ȃ|�C���g
$nouryoku_gold = 1;

#--------------#
#�@���C�������@#
#--------------#

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}

	$back_form = << "EOM";
<br>
<form action="shop_ability.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

if ($mode) { &$mode; }

&ability;

exit;

#--------------------#
#   ���C�����       #
#--------------------#
sub ability{

	&chara_load;

	&chara_check;

	&header;
if(!$chara[35]){$chara[35]=0;}
if($chara[70]<1){$maxpoint= 200 + $chara[37] * 5;}else{$maxpoint=$chara[18]*2;}
if($chara[55]==70){$maxpoint+=2500;$coma="���ÃA�r���e�B���邢�������ɂ���āA�ő�|�C���g���������Ă��܂��B";}
if($chara[56]==70){$maxpoint+=2500;$coma="���ÃA�r���e�B���邢�������ɂ���āA�ő�|�C���g���������Ă��܂��B";}
if($chara[57]==70){$maxpoint+=2500;$coma="���ÃA�r���e�B���邢�������ɂ���āA�ő�|�C���g���������Ă��܂��B";}
if($chara[58]==70){$maxpoint+=2500;$coma="���ÃA�r���e�B���邢�������ɂ���āA�ő�|�C���g���������Ă��܂��B";}
	print << "EOM";
<h1>�\\�͉�</h1><hr>
<br>���݂̃|�C���g�F$chara[35]<br></font>
�\\�͂�1�グ��̂�$nouryoku_gold\�|�C���g�K�v�ł��B<br>
EOM
if($chara[70]!=1){print "1�̃X�e�[�^�X�ɏグ����ő�|�C���g��200�{�]���񐔁~5�Ȃ̂ŁA$maxpoint�ł��B";}
else{print "1�̃X�e�[�^�X�ɏグ����ő�|�C���g�̓��x���~�Q�Ȃ̂ŁA$maxpoint�ł��B";}
print "<br>$coma";
	print << "EOM";
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<tr><td id="td2">STR(��)</td> 
<td align="right" class="b2">$chara[7] +<input type="text" name="up1" size="4"></td></tr>
<tr><td id="td2">INT(����)</td>
<td align="right" class="b2">$chara[8] +<input type="text" name="up2" size="4"></td></tr>
<tr><td id="td2">DEX(����)</td>
<td align="right" class="b2">$chara[9] + <input type="text" name="up3" size="4"></td></tr>
<tr><td id="td2">VIT(HP)</td>
<td align="right" class="b2">$chara[10] + <input type="text" name="up4" size="4"></td></tr>
<tr><td id="td2">LUK(�^)</td>
<td align="right" class="b2">$chara[11] + <input type="text" name="up5" size="4"></td></tr>
<tr><td id="td2">EGO(�K�E)</td>
<td align="right" class="b2">$chara[12] + <input type="text" name="up6" size="4"></td></tr>
</tr>
</table>
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�\\�͂�U��"></form>

EOM
if(!$chara[35]){$chara[35]=0;}
$goldneed = $chara[18] * 500;
	print << "EOM";
<h3>�\\��\��\��\��</h3>
<br>
�\\�͂̏������ɂ̓��x���~500G�K�v�ł��B<br><br>
���݂̏������F$chara[19]G<br><br>
�K�v�Ȃ����ˁF$goldneed G<br>�@<br>�@
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<input type="hidden" name="mode" value="kounyuu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�\\�͂���\��\������"></form>
EOM
if($chara[177]==2){
	print << "EOM";
<h3>���x���_�E��</h3>
<br>
���x�����P�O���_�E�������邱�ƂŁA�N�G�X�g���󂯂Ȃ������Ƃ��ł��܂��B<br><br>
<table width='20%' border=0>
<form action="shop_ability.cgi" >
<input type="hidden" name="mode" value="lvdown">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="���x���_�E������"></form>
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#--------------------#
#   �w������         #
#--------------------#
sub kounyu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'IM');
	&chara_load;
	&chara_check;

if(!$chara[35]){$chara[35]=0;}
if($chara[70]<1){$maxpoint= 200 + $chara[37] * 5;}else{$maxpoint=$chara[18]*2;}
if($chara[55]==70){$maxpoint+=2500;}
if($chara[56]==70){$maxpoint+=2500;}
if($chara[57]==70){$maxpoint+=2500;}
if($chara[58]==70){$maxpoint+=2500;}

	if($in{'up1'} eq "" and $in{'up2'} eq "" and $in{'up3'} eq "" and $in{'up4'} eq "" 
		and $in{'up5'} eq "" and $in{'up6'} eq "") { &error("�L������Ă܂���B"); }

	if ($in{'up1'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'up2'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'up3'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'up4'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'up5'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'up6'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	
	if($chara[35] < $in{'up1'} * $nouryoku_gold + $in{'up2'} * $nouryoku_gold +
			$in{'up3'} * $nouryoku_gold + $in{'up4'} * $nouryoku_gold +
			$in{'up5'} * $nouryoku_gold + $in{'up6'} * $nouryoku_gold)
		{ &error("�|�C���g������܂���$back_form"); }

	if($chara[7] + $in{'up1'} > $maxpoint){&error("STR�����E��˔j���Ă��܂��B$back_form");}
	if($chara[8] + $in{'up2'} > $maxpoint){&error("INT�����E��˔j���Ă��܂��B$back_form");}
	if($chara[9] + $in{'up3'} > $maxpoint){&error("DEX�����E��˔j���Ă��܂��B$back_form");}
	if($chara[10] + $in{'up4'} > $maxpoint){&error("VIT�����E��˔j���Ă��܂��B$back_form");}
	if($chara[11] + $in{'up5'} > $maxpoint){&error("LUK�����E��˔j���Ă��܂��B$back_form");}
	if($chara[12] + $in{'up6'} > $maxpoint){&error("EGO�����E��˔j���Ă��܂��B$back_form");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'IM');

	$chara[7] = $chara[7] + $in{'up1'};
	$chara[8] = $chara[8] + $in{'up2'};
	$chara[9] = $chara[9] + $in{'up3'};
	$chara[10] = $chara[10] + $in{'up4'};
	if($in{'up4'}){
		if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
			$chara[16] += int((rand($in{'up4'}*2)+$in{'up4'})*100000);
		}else{
			$chara[16] = $chara[16] + int((rand($in{'up4'}*2)+$in{'up4'})*1000);
		}
	}
	$chara[15] = $chara[16];
	$chara[11] = $chara[11] + $in{'up5'};
	$chara[12] = $chara[12] + $in{'up6'};

	$chara[35] = $chara[35] - $in{'up1'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up2'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up3'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up4'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up5'} * $nouryoku_gold;
	$chara[35] = $chara[35] - $in{'up6'} * $nouryoku_gold;

	&chara_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
�\\�͂�U��܂����B

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�߂�"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}

#--------------------#
#   �w������         #
#--------------------#
sub kounyuu {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[19] < $chara[18] * 500) { &error("����������܂���"); }
if($chara[70]<1){
	$chara[16] = $kiso_hp + ($chara[18]-1) * 400;
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + $chara[37] * 20 - 4;
}else{
	if($chara[18]<=100){$hpup=($chara[18]-1) * 300;}
	elsif($chara[18]<=200){$hpup =30000 + ($chara[18]-101) * 500;}
	elsif($chara[18]<=500){$hpup =80000 + ($chara[18]-201) * 800;}
	elsif($chara[18]<=1000){$hpup = 320000 + ($chara[18]-501) * 1000;}
	elsif($chara[18]<=2000){$hpup = 820000 + ($chara[18]-1001) * 1200;}
	else{$hpup =2020000 + ($chara[18]-2001) * 1500;}
	$chara[16] = $kiso_hp + $hpup;
	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		$chara[16]= $chara[16]*100;
	}
	$chara[15] = $chara[16];
	$point=0;
	if($chara[55]==70){$point+=2500;}
	if($chara[56]==70){$point+=2500;}
	if($chara[57]==70){$point+=2500;}
	if($chara[58]==70){$point+=2500;}
	$chara[7] = 1+$point;
	$chara[8] = 1+$point;
	$chara[9] = 1+$point;
	$chara[10] = 1+$point;
	$chara[11] = 1+$point;
	$chara[12] = 1+$point;
	$chara[19] = $chara[19] - $chara[18] * 500;
	$chara[35] = $chara[18] * 4 + 20 - 4;
}
	&chara_regist;

	&header;

	print <<"EOM";
�\\�͂���\��\�����܂����B

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�߂�"></form>

EOM

	&shopfooter;

	&footer;

	exit;
}
sub lvdown {

	&get_host;

	&chara_load;
	&chara_check;

	if($chara[177] != 2) { &error("�G���[�B"); }
if($in{'kakunin'}==1){
	$ccccc=151;
	for($ccccc=151;$ccccc<180;$ccccc++){
		$chara[$ccccc]=0;
	}
	$chara[18]-=int($chara[18]/10);
	if($chara[18]<=100){$hpup=($chara[18]-1) * 300;}
	elsif($chara[18]<=200){$hpup =30000 + ($chara[18]-101) * 500;}
	elsif($chara[18]<=500){$hpup =80000 + ($chara[18]-201) * 800;}
	elsif($chara[18]<=1000){$hpup = 320000 + ($chara[18]-501) * 1000;}
	elsif($chara[18]<=2000){$hpup = 820000 + ($chara[18]-1001) * 1200;}
	else{$hpup =2020000 + ($chara[18]-2001) * 1500;}
	$chara[16] = $kiso_hp + $hpup;
	$chara[15] = $chara[16];
	$chara[7] = 1;
	$chara[8] = 1;
	$chara[9] = 1;
	$chara[10] = 1;
	$chara[11] = 1;
	$chara[12] = 1;
	$chara[35] = $chara[18] * 4 + 20 - 4;
	$chara[188]++;

	&chara_regist;

	&header;
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]�l�����x���_�E�������܂����B";

	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');
	print <<"EOM";
���x���_�E�����I�����܂����B�X�e�[�^�X�����Z�b�g����Ă���̂Œ��ӁB

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�߂�"></form>

EOM
}else{
	&chara_regist;
	&header;
	print <<"EOM";
�{���Ƀ��x���_�E�������Ă������ł����H
<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvdown">
<input type="hidden" name="kakunin" value=1>
<input type="submit" class="btn" value="����"></form>

<form action="shop_ability.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�߂�"></form>
EOM
}
	&shopfooter;

	&footer;

	exit;
}