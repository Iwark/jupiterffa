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
<form action="bokujyo.cgi" >
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

&item_view;

exit;

#----------------#
#  �y�b�g�\���@  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	foreach(@log_item){
		($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/);
		if(!$i_no or !$i_name){splice(@acs_array,$g,1);$hit=1;}
		else{$g++;}
	}
	if($hit==1){
		open(OUT,">pets/$chara[0].cgi");
		print OUT @log_item;
		close(OUT);
	}

	&header;

	print <<"EOM";
<h1>�q��</h1>
<hr size=0>

<FONT SIZE=3>
<B>�q��Ǘ��l</B><BR>
�u
$chara[4]�l�ɗa�����Ă���y�b�g�͉��̂悤�ɂȂ��Ă���܂�
�v
</FONT>
<br><hr>���݂̃y�b�g<br>
EOM
if($chara[138] eq ""){$peename=$chara[39];}else{$peename=$chara[138];}
if($chara[38]>3000){
	print <<"EOM";
<form action="bokujyo.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
<input type=submit class=btn value="�n��">$peename
</form>
EOM
}
	print <<"EOM";
�a���Ă���y�b�g
<table>
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>���x��</th><th nowrap>�g�o</th><th nowrap>�U����</th></tr>
EOM
	$i = 0;
	foreach (@log_item) {
		($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/);
		if($i_namae eq ""){$pename=$i_name;}else{$pename=$i_namae;}
		print << "EOM";
<tr>
<form action="bokujyo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="�������">
</td>
</form>
<td class=b1 nowrap>$pename</td>
<td align=right class=b1>$i_lv</td>
<td align=right class=b1>$i_hp</td>
<td align=right class=b1>$i_damage</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[38]==3000){ &error("��ꂽ���͗a����܂���I"); }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	$log_item[$in{'item_no'}] =~ s/\n//g;
	$log_item[$in{'item_no'}] =~ s/\r//g;

	($i_no,$i_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/,$log_item[$in{'item_no'}]);

	if($chara[38]){
		$log_item[$in{'item_no'}] = "$chara[38]<>$chara[39]<>$chara[40]<>$chara[41]<>$chara[43]<>$chara[44]<>$chara[45]<>$chara[46]<>$chara[47]<>$chara[138]<>\n";
	}
	else{
		$log_item[$in{'item_no'}] = ();
	}

	open(OUT,">pets/$chara[0].cgi");
	print OUT @log_item;
	close(OUT);
	$chara[38]=$i_no;
	$chara[39]=$i_name;
	$chara[40]=$i_exp;
	$chara[41]=$i_maxexp;
	$chara[43]=$i_hp;
	$chara[44]=$i_damage;
	$chara[45]=$i_image;
	$chara[46]=$i_lv;
	$chara[47]=$i_ps;
	$chara[138]=$i_namae;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	print <<"EOM";
<FONT SIZE=3>
<B>$pename���������܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_sell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($chara[38]==3000){ &error("��ꂽ���͗a����܂���I"); }

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"pets/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= 20) {
		&error("�q�ꂪ�y�b�g�ł����ς��ł��I$back_form");
	}

	push(@souko_item,"$chara[38]<>$chara[39]<>$chara[40]<>$chara[41]<>$chara[43]<>$chara[44]<>$chara[45]<>$chara[46]<>$chara[47]<>$chara[138]<>\n");

	open(OUT,">pets/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	$chara[38]=0;
	$chara[39]="";
	$chara[40]=0;
	$chara[41]=0;
	$chara[43]=0;
	$chara[44]=0;
	$chara[45]=0;
	$chara[46]=0;
	$chara[47]=0;
	$chara[138]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�y�b�g����������Ă��炢�܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
