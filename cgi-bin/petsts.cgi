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

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="petsts.cgi" >
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

&petsts;

&error;

exit;

#----------#
#  ���  #
#----------#
sub petsts {

	&chara_load;

	&chara_check;

	&header;
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	print <<"EOM";
<h1>$pename�̃X�e�[�^�X</h1>
���݂̏������F$chara[19] �f<br><br>
�������g���ăy�b�g�ɕω��������炷���Ƃ��ł����\�\\��������܂��B<br>
�Œ�{�[�_�[���z���Ă��Ȃ���\�\\��\�l���������Ă��܂����Ƃ�����܂��B<br>
�{�[�_�[���z���Ă��Ă�\�\\��\�l���オ��ۏ�͂���܂���B<br>
<font SIZE=2 color="red">���ŋ��̃y�b�g��ω�������Ɖ����N���邩������܂���</font><br>
EOM
if($chara[45]){
	print <<"EOM";
	<IMG SRC="$img_path_pet/$egg_img[$chara[45]]">
	<br>�ő�g�o�F$chara[43]
	<br>�U���́F$chara[44]
	<br>���x���F$chara[46]
	<br><br>
EOM
}
if($chara[46]==20 and $chara[38]==3000 and $chara[37]>3){
	print <<"EOM";
<form action="petsts.cgi" >
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�ω��I"></form><p>
EOM
}
if($chara[70]<1){
	print <<"EOM";
�Œ�{�[�_�[<br><br>
�g�o�P�t�o�F10000�f<br>
�U���͂P�t�o�F50000�f<br>
���x���P�t�o�F100000�f<br><br>
<table width='25%' border=0>
<form action="petsts.cgi" >
<tr><td id="td2">�g�o</td>
<td align="right" class="b2"><input type="text" name="up1" size="24">�@�f</td></tr>
<tr><td id="td2">�U����</td>
<td align="right" class="b2"><input type="text" name="up2" size="24">�@�f</td></tr>
<tr><td id="td2">���x��</td>
<td align="right" class="b2"><input type="text" name="up3" size="24">�@�f</td></tr>
</tr>
</table>
<input type="hidden" name="mode" value="kounyu">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�ω��I"></form><p>
EOM
}else{
	print <<"EOM";
���肵�����F<br><table><tr><th></th><th></th></tr>
EOM
	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);
	for($k=201;$k<300;$k++){
		if($chara[$k]){
			$hit=0;
			foreach(@item_array){
		($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
			if($phi_no == $k+3200) { last; }
			}
			print <<"EOM";
			<tr><th>
			$phi_name�̍�
			</th><th>
			<form action="petsts.cgi" >
			<input type="hidden" name="mode" value="tukau">
			<input type="hidden" name="aite" value="$phi_name">
			<input type="hidden" name="kno" value="$k">
			<input type="hidden" name="id" value="$chara[0]">
			<input type="hidden" name="mydata" value="$chara_log">
			<input type="submit" class="btn" value="�g��">
			</form>
			</th></tr>
EOM
		}
	}
	print <<"EOM";
</table>
<table width='25%' border=0>
<form action="petsts.cgi" >
<tr><td id="td2">���O�ύX</td>
<td align="right" class="b2"><input type="text" name="namae" size="48"></td></tr>
</table>
<input type="hidden" name="mode" value="henkou">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�ω��I"></form><p>
EOM
}
if($chara[70]==1 and $chara[38]==3000 and $chara[19]>=1000000){
	print <<"EOM";
	<form action="petsts.cgi" >
	<input type="hidden" name="mode" value="koware">
	<input type="hidden" name="id" value="$chara[0]">
	<input type="hidden" name="mydata" value="$chara_log">
	<input type="submit" class="btn" value="��ꂽ�����ŗ��ɖ߂��i100���f�j">
	</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub kounyu {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[19]<$in{'up1'}+$in{'up2'}+$in{'up3'}){ &error("����������܂���$back_form"); }
	elsif($in{'up1'} < 0 or $in{'up2'} < 0 or $in{'up3'} < 0){ &error("�}�C�i�X�̐��l�̓_���ł�$back_form"); }
	elsif($in{'up1'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}
	elsif($in{'up2'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}
	elsif($in{'up3'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}
	else{ $chara[19] = $chara[19] - $in{'up1'} - $in{'up2'} - $in{'up3'}; }

	if ($in{'up1'}){
		if ($in{'up1'} > 10000){
			$hpup = int(rand($in{'up1'} / 1000 + 1)) + int($in{'up1'}/10000);
		}elsif(int(rand(4))==0){
			$hpup = -int(rand($in{'up1'}/1000 + 1)) - int($in{'up1'}/10000);
		}else{
			$hpup = int(rand($in{'up1'} / 1000 + 1)) + int($in{'up1'}/10000);
		}
		if($chara[43] + $hpup>10000){$hpup=0;}
	}
	if ($in{'up2'}){
		if ($in{'up2'} > 50000){
			$dmgup = int(rand($in{'up2'} / 10000 + 1)) + int($in{'up2'}/50000);
		}elsif(int(rand(4))==0){
			$dmgup = -int(rand($in{'up2'}/10000 + 1)) - int($in{'up2'}/50000);
		}else{
			$dmgup = int(rand($in{'up2'} / 10000)) + int($in{'up2'}/50000);
		}
	}
	if ($in{'up3'}){
		if ($in{'up3'} > 100000){
			$lvup = int(rand($in{'up3'} / 100000 + 1));
		}elsif(int(rand(4))==0){
			$lvup = -int(rand($in{'up3'}/ 75000 + 1));
		}else{
			$lvup = int(rand($in{'up3'} / 75000 + 1));
		}
	}
	$chara[43] += $hpup;
	$chara[42] = $chara[43];
	$chara[44] += $dmgup;
	$chara[46] += $lvup;
	if($chara[42]<1){$chara[42]=1;}
	if($chara[44]<1){$chara[44]=1;}
	if($chara[46]>20){$chara[46]=20;}
	if($chara[46]==20){
		if($chara[38]==3000 and $chara[37]>3){
			$k=100;
			#��ꂽ�����S�[�`��
			$chara[38] = 3151;$chara[39] = "�S�[�`��";$chara[40] = 0;
			$chara[41] = 2000;$chara[42] = 2400;$chara[43] = 2400;
			$chara[44] = 240;$chara[45] = 137;$chara[46] = 1;
			$chara[47] = 11;
		}
		if($chara[38]==3126){
			if(!$chara[131]){
				$k=1;
				#�p���_�}�����C�G���[�}�X�^�[
				$chara[131]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
		if($chara[38]==3136 or $chara[38]==3135){
			if(!$chara[132]){
				$k=2;
				#�S�b�h�o�[�h�����b�h�}�X�^�[
				$chara[132]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
		if($chara[38]==3122){
			if(!$chara[133]){
				$k=3;
				#�h���S�����[�h���h���S���}�X�^�[
				$chara[133]=1;
				$chara[38] = 0;$chara[39] = "";$chara[40] = 0;
				$chara[41] = 0;$chara[42] = 0;$chara[43] = 0;
				$chara[44] = 0;$chara[45] = 0;$chara[46] = 0;
				$chara[47] = 0;
			}
		}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

if($k==1){
	print <<"EOM";
<FONT SIZE=4 color="red">�ω����Ƀp���_�}���͎�������ڂ��ʂ���������������B<br>
��ڂ��ʂ������p���_�}���̓C�G���[���[���h�̌���$chara[4]�ɗ^���ċ����Ă������c</font>
EOM
}elsif($k==2){
	print <<"EOM";
<FONT SIZE=4 color="red">�ω����ɃS�b�h�o�[�h�͎�������ڂ��ʂ���������������B<br>
��ڂ��ʂ������S�b�h�o�[�h�̓��b�h���[���h�̌���$chara[4]�ɗ^���ċ����Ă������c</font>
EOM
}elsif($k==3){
	print <<"EOM";
<FONT SIZE=4 color="red">�ω����Ƀh���S�����[�h�͎����̖�ڂ��ʂ���������������B<br>
��ڂ��ʂ������h���S�����[�h�̓h���S�����[���h�̌���$chara[4]�ɗ^���ċ����Ă������c</font>
EOM
}elsif($k==100){
	print <<"EOM";
<FONT SIZE=4 color="red">��ꂽ�����Ȃ�Ɠ����o�����I�I<br>
������A�Ȃ�Ɛl�̎p�ɍ������Ă���S�[�`�������܂ꂽ�I�I�I�I�I�I</font>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>�ω����������܂����B<br>
���ω���<br>
�g�o�F$hpup<br>
�U���́F$dmgup<br>
���x���F$lvup</B></font><br>
EOM
}
	print <<"EOM";
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  ��񔃂��@�@  #
#----------------#
sub koware {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]!=1 or $chara[38]!=3000 or $chara[19]<1000000){ &error("�����������Ă܂���$back_form"); }
	else{ $chara[19] = $chara[19] - 1000000;}

	$chara[38]=3006;
	$chara[39]="�ł̗�";
	$chara[40]=0;
	$chara[41]=3000000;
	$chara[42]=6500;
	$chara[43]=6500;
	$chara[44]=0;
	$chara[45]=5;
	$chara[46]=1;
	$chara[47]=0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�ł̗��ɖ����߂�܂����B<br>
���ω���<br>
�g�o�F$hpup<br>
�U���́F$dmgup<br>
���x���F$lvup</B></font><br>

<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub henkou {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if (!$in{'namae'}){ &error("���͂��Ă�������$back_form"); }

	$chara[138] = $in{'namae'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�ω����������܂����B<br>
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub tukau {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($chara[38]!=3159 and $chara[46]<1000){ $comment = "�Ώۃy�b�g���シ���܂��B<br>"; }
	else{

	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	if ($in{'aite'} eq "�x��"){
		if($chara[39] eq "�x��"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�x��2") { $hit=1;$chara[235]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�K�I�[��"){
		if($chara[39] eq "���@���v"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�L���O") { $hit=1;$chara[225]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�V�^�E�C���X"){
		if($chara[39] eq "�V�^�E�C���X"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�V�^�E�C���X2") { $hit=1;$chara[231]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�V�^�E�C���X2"){
		if($chara[39] eq "�V�^�E�C���X2"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�V�^�E�C���X3") { $hit=1;$chara[232]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�΍׋�"){
		if($chara[39] eq "�V�^�E�C���X3"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�Ԃ̋�") { $hit=1;$chara[275]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�^�k�L�}��"){
		if($chara[39] eq "�I�[�K"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�M�K���g�I�[�N") { $hit=1;$chara[234]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�x��2"){
		if($chara[39] eq "�V�^�E�C���X3"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�O�[�K��") { $hit=1;$chara[236]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�}�[�V��"){
		if($chara[39] eq "�M�K���g�I�[�N"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�}�[�V���E�V���[�N") { $hit=1;$chara[290]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�X�m�[�}��"){
		if($chara[39] eq "�O�[�K��"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�}�[�V��") { $hit=1;$chara[220]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($in{'aite'} eq "�G�b�O�G���W�F��"){
		if($chara[39] eq "�S�b�h�G���W�F��"){
			foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
				if($phi_name eq "�G�b�O�G���W�F��") { $hit=1;$chara[294]=0;last; }
			}
		}
			$comment = "���̃y�b�g�ɂ͍���Ȃ����̂悤�ł��B<br>";
	}
	elsif ($chara[39] eq "�S�b�h�G���W�F��" and $chara[24]==1400){
		if(int(rand(2))==0){
			$kougeki=int(rand(($in{'kno'}-200)*5));
			if($chara[128]>=5 and $item[1]>9998){$kougeki=int($kougeki/int($item[1]/10000+1));}
			if($item[1]+$kougeki>9999 and $chara[128]<5){$kougeki=9999-$item[1];}
			$item[1]+=$kougeki;
			$comment = "�S�b�h�G���W�F����\��\��\�\\��\�ɂ���ĕ���̍U���͂�$kougeki�|�C���g�オ�����I<br>";
		}else{
			$hitp=int(rand(($in{'kno'}-200)*5));
			if($chara[128]>=5 and $item[2]>9998){$hitp=int($hitp/int($item[2]/10000+1));}
			if($item[2]+$hitp>9999 and $chara[128]<5){$hitp=9999-$item[2];}
			$item[2]+=$hitp;
			$comment = "�S�b�h�G���W�F����\��\��\�\\��\�ɂ���ĕ���̖�������$hitp�|�C���g�オ�����I<br>";
		}
		$chara[$in{'kno'}]=0;
	}
	else{ 
		$comment = "���̍��͎g���܂���B<br>";
	}
	if($hit) {
		$comment = "<b><font size=4 color=red>�y�b�g��$phi_name�ɕω������I�I</font></b><br>";
		$chara[38] = $phi_no;
		$chara[39] = $phi_name;
		$chara[40] = 0;
		$chara[41] = $phi_exp;
		$chara[42] = $phi_hp;
		$chara[43] = $phi_hp;
		$chara[44] = $phi_damage;
		$chara[45] = $phi_image;
		$chara[46] = 1;
		$chara[47] = $ps;
	}

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
<B>$comment<br>
<br>
<form action="petsts.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}