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
<form action="sihai.cgi" method="post">
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

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	$g=0;
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
		$g++;
	}

	$sihai_data[$g]="$sihaisya[0]<>$sihaisya[1]<>$sihaisya[2]<>$sihaisya[3]<>$sihaisya[4]<>$sihaisya[5]<>$sihaisya[6]<>$sihaisya[7]<>$sihaisya[8]<>$sihaisya[9]<>$sihaisya[10]<>$sihaisya[11]<>$sihaisya[12]<>$sihaisya[13]<>$sihaisya[14]<>$sihaisya[15]<>$sihaisya[16]<>$sihaisya[17]<>$sihaisya[18]<>$sihaisya[19]<>$sihaisya[20]<>\n";

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);

	$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);
if(!$sihaisya[15]){$sihaisya[15]=0;}
	print <<"EOM";
<h1>�x�z�Ҏ{��</h1>
<hr size=0>
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�x�z�҂Ƃ̐퓬���ł���̂͌���ꂽ���݂̂��B(�ڂ����͌f����)<br>
�x�z�҂Ƃ̐킢�ɏ�������ƁA�x�z�҃_���W�����̐ݒ肪�ł��邼�B<br>
�x�z�҂Ƃ̐킢�ł́A�A�r���e�B��(���݂�)�������Ȃ����B<br>
�������A�y�b�g�̎������݂���\�\\���B�v<p>
���݂̎x�z�ҁF$sihaisya[1]
</FONT>
<hr size=0>
EOM
if($mday != 3 and $mday != 6 and $mday != 9 and $mday != 12 and $mday != 15 and $mday != 18 and $mday != 21 and $mday != 24 and $mday != 27 and $mday != 30){print "�����͎x�z�҂Ƃ̐퓬�͂ł��܂���B";}
elsif($sihaisya[1] ne $chara[4]){
	print <<"EOM";
���݂̎x�z�ҁF$sihaisya[1]
<form action="./sihaibattle.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sihai>
<input type=submit class=btn value="�키">
</form>
EOM
}
if($sihaisya[1] eq $chara[4]){
	print <<"EOM";
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="�x�z�҃_���W�����̐ݒ�">
</form>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<input type=submit class=btn value="���ꗿ�ɂ��������󂯎��($sihaisya[15] G)">
</form>
<p>
EOM
}
	print <<"EOM";
<p>
<FONT SIZE=3.3><br>
<font size=4>���݂̐ݒ�F</font><br>
�|�C���g�F$point �|�C���g<br>
���ꗿ�F$sihaisya[2] �f<br>
�o�������X�^�[���F<br>
�E$sihaisya[3]<br>
�E$sihaisya[4]<br>
�E$sihaisya[5]<br>
�E$sihaisya[6]<br>
�E$sihaisya[7]<br>
�E$sihaisya[8]<br>
�E$sihaisya[9]<br>
�E$sihaisya[10]<br>
�����X�^�[�o�����F$sihaisya[11] ��<br>
�o���l�{���F$sihaisya[12] �{<br>
�擾���{���F$sihaisya[13] �{<br>
<p>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub settei {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);

	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}

	&header;

	$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);

	print <<"EOM";
<FONT SIZE=3.3><br>
<font size=4>���݂̐ݒ�F</font><br>
���ӁF�|�C���g���P�O�O�O�O�|�C���g���I�[�o�[���Ă���Ǝx�z�҃_���W�����ɍs���Ȃ��Ȃ�܂��B<br><br>
�|�C���g�F$point �|�C���g<br>
���ꗿ�F$sihaisya[2] �f<br>
�o�������X�^�[���F<br>
�E$sihaisya[3]<br>
�E$sihaisya[4]<br>
�E$sihaisya[5]<br>
�E$sihaisya[6]<br>
�E$sihaisya[7]<br>
�E$sihaisya[8]<br>
�E$sihaisya[9]<br>
�E$sihaisya[10]<br>
�����X�^�[�o�����F$sihaisya[11] ��<br>
�o���l�{���F$sihaisya[12] �{<br>
�擾���{���F$sihaisya[13] �{<br>
<p>
<font size=4>�ݒ�̕ύX�F</font>
<p>
�����X�^�[�̐ݒ�F�m���D��1�`8�܂ł̐�������͂��A�ݒ�{�^���������B<br>
<table><tr><td class=b1>No.</td><td class=b1></td><td class=b1>�����X�^�[��</td><td class=b1>�|�C���g</td></tr>
EOM

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);
	$i=0;
	foreach (@mons_data) {
		@mons = split(/<>/);
		if($sihaisya[3] ne $mons[0] and $sihaisya[4] ne $mons[0] and $sihaisya[5] ne $mons[0] and 		$sihaisya[6] ne $mons[0] and $sihaisya[7] ne $mons[0] and $sihaisya[8] ne $mons[0] and $sihaisya[9] ne $mons[0] and $sihaisya[10] ne $mons[0]){
		if($i %4 ==0){print "<tr>";}
		print <<"EOM";
		<form action="./sihai.cgi" method="post">
		<td class=b1>
		<input type="text" name="taisyo" size=5><br>
		</td>
		<td class=b1>
		<input type=hidden name=id value="$chara[0]">
		<input type=hidden name=mydata value="$chara_log">
		<input type=hidden name=mode value=okuru>
		<input type=hidden name=aite value=$mons[0]>
		<input type=hidden name=point value=$mons[2]>
		<input type=submit class=btn value="�ݒ�">
		</form>
		</td>
		<td class=b1>$mons[0]</td>
		<td class=b1>$mons[2]</td>
EOM
		if($i %4 ==3){print "<tr>";}
		$i++;
		}
	}

	print <<"EOM";
</table>
<p>
�����X�^�[�o�����A�o���l�Ƃ����̔{���ݒ�F�m���D��1�`8�܂ł̐�������͂��A�ݒ�{�^���������B<br>
<form action="./sihai.cgi" method="post">
<table>
<tr><td class=b1>�����X�^�[�o����</td>
<td class=b1>�P��</td><td class=b1>�Q��</td><td class=b1>�R��</td>
<td class=b1>�S��</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=kazu value=1></td>
<td class=b1><input type=radio name=kazu value=2></td>
<td class=b1><input type=radio name=kazu value=3></td>
<td class=b1><input type=radio name=kazu value=4></td>
</tr>
<tr><td class=b1>����</td>
<td class=b1>0.2�{</td><td class=b1>0.6�{</td><td class=b1>1.0�{</td>
<td class=b1>1.4�{</td><td class=b1>1.8�{</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=kane value=0.2></td>
<td class=b1><input type=radio name=kane value=0.6></td>
<td class=b1><input type=radio name=kane value=1.0></td>
<td class=b1><input type=radio name=kane value=1.4></td>
<td class=b1><input type=radio name=kane value=1.8></td>
</tr>
<tr><td class=b1>�o���l</td>
<td class=b1>0.2�{</td><td class=b1>0.6�{</td><td class=b1>1.0�{</td>
<td class=b1>1.4�{</td><td class=b1>1.8�{</td>
</tr>
<tr><td class=b1></td>
<td class=b1><input type=radio name=exp value=0.2></td>
<td class=b1><input type=radio name=exp value=0.6></td>
<td class=b1><input type=radio name=exp value=1.0></td>
<td class=b1><input type=radio name=exp value=1.4></td>
<td class=b1><input type=radio name=exp value=1.8></td>
</tr>
</table>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value="kk">
<input type=submit class=btn value="�ݒ�">
</form>
<p>
���ꗿ�̐ݒ�(10�f�ɂ�1�|�C���g)�F<br>
<form action="./sihai.cgi" method="post">
<input type="text" name="ryoukin" size=5><br>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=kane>
<input type=submit class=btn value="�ݒ�">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  ��񔃂��@�@  #
#----------------#
sub okuru {

	&chara_load;

	&chara_check;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if ($in{'taisyo'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B"); 
	}elsif($in{'taisyo'}>8 or $in{'taisyo'} <1){
		&error("�����͂P�`�W�܂ł���͂��Ă��������B"); 
	}elsif(!$in{'aite'}){
		&error("�����X�^�[�����݂��܂���B"); 
	}else{
		$t=$in{'taisyo'}+2;
		$hit=0;
		foreach (@mons_data) {
			@mons = split(/<>/);
			if($mons[0] eq $sihaisya[$t]){$hit=1;last;}
		}
		$sihaisya[14] += $in{'point'};
		if($hit){$sihaisya[14] -= $mons[2];}
		$sihaisya[$t] = $in{'aite'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�����X�^�[��ݒ肵�܂����B</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="�ݒ�𑱂���">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub kk {

	&chara_load;

	&chara_check;

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if(!$in{'kane'} or !$in{'exp'} or !$in{'kazu'}){
		&error("�����������X�^�[�o�����A�����ƌo���l��ݒ肵�Ă��������B");
	}else{
		$sihaisya[12] = $in{'exp'};
		$sihaisya[13] = $in{'kane'};
		$sihaisya[11] = $in{'kazu'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�����X�^�[�o�����A�����ƌo���l��ݒ肵�܂����B</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="�ݒ�𑱂���">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  ��񔃂��@�@  #
#----------------#
sub uketoru {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	$chara[19]+=$sihaisya[15];
	$sihaisya[15]=0;

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�������󂯎��܂����B</B><BR>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub kane {

	&chara_load;

	&chara_check;

	open(IN,"data/sihai.ini");
	@mons_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	if ($in{'ryoukin'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B"); 
	}else{
		$sihaisya[2] = $in{'ryoukin'};
	}

	$new_array = '';
	$new_array = join('<>',@sihaisya);
	$new_array =~ s/\n//;
	$new_array .= "<>\n";
	$sihai_data[0] =$new_array;

	open(OUT,">sihaisya.cgi");
	print OUT @sihai_data;
	close(OUT);
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���ꗿ��ݒ肵�܂����B</B><BR>
<form action="./sihai.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=settei>
<input type=submit class=btn value="�ݒ�𑱂���">
</form>
</font>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}