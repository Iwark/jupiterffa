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
#�@http://www3.big.or.jp/~icu/
#�@icus2@hotmail.com
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#     http://www3.big.or.jp/~icu/cgi-bin/cbbs/cbbs.cgi�@		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

require './chat_conf.cgi';

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if ($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m");
}
&decode;

	$back_form = << "EOM";
<br>
<form action="$scriptst" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

if ($mode) { &$mode; }
&chara_st;
exit;

#----------------#
#  ���O�C�����  #
#----------------#
sub chara_st {

	&chara_load;

	&chara_check;

	&item_load;

	# �\�͒l�o�[�̏ڂ������ݒ�
$hit_ritu = int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16];
$sake = int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17];
$waza_ritu = int(($chara[11] / 10)) + 10 + $a_wazaup;
if($waza_ritu > 90){$waza_ritu = 90;}
$hissatu_ritu = $waza_ritu + int($chara[12]/4);
$ci_plus = $item[2] + $item[16];
$cd_plus = $item[5] + $item[18];

	open(IN,"$tac_file");
	@gettac = <IN>;
	close(IN);

	$thit = 0;
	foreach (@gettac) {
		($tacno,$tacname) = split(/<>/);
		if ($chara[30] == $tacno) {
			$ktac_name = $tacname;
			$thit = 1;
			last;
		}
	}

	if (!$thit) { $ktac_name = "���ʂɐ키"; }

	if($chara[5]) { $esex = "�j"; } else { $esex = "��"; }
	$next_ex = $chara[18] * $lv_up;

        if(!$chara[32]){$chara[32] = 0;}
	$syou = @shogo[$chara[32]];

	&syoku_load;

	&header;

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}

       print <<"EOM";
<table align="center">
<TR>
<TD><font size=5>$chara[4]����p�X�e�[�^�X�ύX���</font></TD>
</TR>
</table>
<hr size=0>
<form action="$scripts" >
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td></tr>
<td rowspan="4" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$chara[6]]">
<tr><td id="td2" class="b2">����</td><td align="right" class="b2">$item[0] $bukilv</td>
<td id="td2" class="b1">�U����</td><td align="right" class="b2">$item[1]</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="right" class="b2">$item[3] $bogulv</td>
<td id="td2" class="b1">�h���</td><td align="right" class="b2">$item[4]</td></tr>
<tr><td id="td2" class="b2">�A�N�Z�T���[</td><td align="right" class="b2">$item[6]</td>
	
<td id="td2" class="b2">�̍�</td><td align="center" class="b2"><font color=yellow>$syou</font></td></tr>
</table>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr><td class="b1" id="td2">�W���u</td>
<td class="b2">
$chara_syoku[$chara[14]]
</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
</table>
<table width="100%"><tr><td id="td2" align="center" class="b1">���܂ł̃W���u</td></tr>
<tr><td colspan=3 align="center" class="b1">
<table width="100%">
<tr>
EOM
	$s = 0;
	foreach (@syoku_master){
		if ($_) {
			$class_flg = int($syoku_master[$s]/10);
			$class[$s] = $class_mark[$class_flg];
			print "<td class=\"b2\" width=\"20%\" align=\"center\">$chara_syoku[$s]</td>";
		}
		$s++;
		if ($s % 5 == 0) {
			print '</tr><tr>';
		}
	}

	if (!$s) {
		print "<td class=\"b2\" width=\"100%\" align = \"center\">�Ȃ�</td>";
	}

       print <<"EOM";
</tr></table></td></tr></table>
<table width="100%"></form>
<tr><td id="td1" colspan="5" class="b2" align="center">���̑��̃R�}���h</td></tr>
<tr><td id="td2"align="center" class="b2">�y�X�e�[�^�X��ʂցz</td>
<form action="$script" >
<td align="center"colspan="4" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�"></td>
</form>
</tr>
<tr><td id="td2"align="center" class="b2">�y�p�X���[�h�ύX�z</td>
<form action="$script_pass" >
<td align="center"colspan="4" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�p�X���[�h�ύX"></td>
</form>
</tr></table>
<td valign="top">
<table width='100%'>
<form action="$scriptst" >
<tr><td id="td1" colspan="5" class="b2" align="center">�z�[���y�[�W�f�[�^</td></tr>
<tr><td id="td2" class="b1">�z�[���y�[�W��</td></tr><tr><td colspan="4"><input type="text" name=site value="$chara[2]" size=50></td></tr>
<tr><td id="td2" class="b1">�z�[���y�[�W��URL</td></tr><tr><td colspan="4"><input type="text" name=url value="$chara[3]" size=60></td></tr>
</table>
<table width='100%'>
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr>
<td class="b1" id="td2">�摜�ݒ�</td>
<td class="b2"colspan="4">
<input type="text" name="chara" value="$chara[6]" size=5>
<a href="$img_all_list" target="_blank">
$vote_gazou</a>
</td>
</tr>
<tr>
<td class="b1" id="td2">��A�`�����l��</td>
<td class="b2"colspan="4">
<input type="text" name="chan" value="$chara[96]" size=5>
</td>
</tr>
<tr>
<td class="b1" id="td2">��A�`�����l��2</td>
<td class="b2"colspan="4">
<input type="text" name="chan2" value="$chara[180]" size=5>
</td>
</tr>
<tr>
<td class="b1" id="td2">�퓬�㎩���h��</td>
<td class="b2"colspan="4">
EOM
if($chara[36]==1){
	print <<"EOM";
<INPUT TYPE="radio" NAME="autoyado" VALUE="1" checked>ON
<INPUT TYPE="radio" NAME="autoyado" VALUE="2">OFF
EOM
}else{
	print <<"EOM";
<INPUT TYPE="radio" NAME="autoyado" VALUE="1">ON
<INPUT TYPE="radio" NAME="autoyado" VALUE="2" checked>OFF
EOM
}
	print <<"EOM";
(���W�F���h�퓬��͎����ŏh���ɍs���܂���B)
</td>
</tr>
<tr>
<td class="b1" id="td2">���C���`���b�g��\\��</td>
<td class="b2"colspan="4">
EOM
if($chara[60]==1){
	print <<"EOM";
<INPUT TYPE="radio" NAME="mainchat" VALUE="1" checked>ON
<INPUT TYPE="radio" NAME="mainchat" VALUE="2">OFF
EOM
}else{
	print <<"EOM";
<INPUT TYPE="radio" NAME="mainchat" VALUE="1">ON
<INPUT TYPE="radio" NAME="mainchat" VALUE="2" checked>OFF
EOM
}
	print <<"EOM";
(�퓬�Ԋu�̃`���b�g�͕\\������܂��B)
</td>
</tr>
<tr>
<td class="b1" id="td2">(�ꕔ��)�摜��\\��</td>
<td class="b2"colspan="4">
EOM
if($chara[50]==1){
	print <<"EOM";
<INPUT TYPE="radio" NAME="sgazo" VALUE="1" checked>ON
<INPUT TYPE="radio" NAME="sgazo" VALUE="2">OFF
EOM
}else{
	print <<"EOM";
<INPUT TYPE="radio" NAME="sgazo" VALUE="1">ON
<INPUT TYPE="radio" NAME="sgazo" VALUE="2" checked>OFF
EOM
}
	print <<"EOM";
(�d���Ƃ��Ɏg�p���Ă��������B)
</td>
</tr>
<tr>
<td class="b1" id="td2">�w�i�摜</td>
<td class="b2"colspan="4">
EOM
if($chara[145]==2){
	print <<"EOM";
<INPUT TYPE="radio" NAME="shai" VALUE="1">�ʏ�(��)
<INPUT TYPE="radio" NAME="shai" VALUE="2" checked>��
<INPUT TYPE="radio" NAME="shai" VALUE="3">�F��
<INPUT TYPE="radio" NAME="shai" VALUE="4">������
<INPUT TYPE="radio" NAME="shai" VALUE="5">���V
EOM
}elsif($chara[145]==3){
	print <<"EOM";
<INPUT TYPE="radio" NAME="shai" VALUE="1">�ʏ�(��)
<INPUT TYPE="radio" NAME="shai" VALUE="2">��
<INPUT TYPE="radio" NAME="shai" VALUE="3" checked>�F��
<INPUT TYPE="radio" NAME="shai" VALUE="4">������
<INPUT TYPE="radio" NAME="shai" VALUE="5">���V
EOM
}elsif($chara[145]==4){
	print <<"EOM";
<INPUT TYPE="radio" NAME="shai" VALUE="1">�ʏ�(��)
<INPUT TYPE="radio" NAME="shai" VALUE="2">��
<INPUT TYPE="radio" NAME="shai" VALUE="3">�F��
<INPUT TYPE="radio" NAME="shai" VALUE="4" checked>������
<INPUT TYPE="radio" NAME="shai" VALUE="5">���V
EOM
}elsif($chara[145]==5){
	print <<"EOM";
<INPUT TYPE="radio" NAME="shai" VALUE="1">�ʏ�(��)
<INPUT TYPE="radio" NAME="shai" VALUE="2">��
<INPUT TYPE="radio" NAME="shai" VALUE="3">�F��
<INPUT TYPE="radio" NAME="shai" VALUE="4">������
<INPUT TYPE="radio" NAME="shai" VALUE="5" checked>���V
EOM
}else{
	print <<"EOM";
<INPUT TYPE="radio" NAME="shai" VALUE="1" checked>�ʏ�(��)
<INPUT TYPE="radio" NAME="shai" VALUE="2">��
<INPUT TYPE="radio" NAME="shai" VALUE="3">�F��
<INPUT TYPE="radio" NAME="shai" VALUE="4">������
<INPUT TYPE="radio" NAME="shai" VALUE="5">���V
EOM
}
	print <<"EOM";
</td>
</tr>
<tr>
<td class="b1" id="td2">�Ȃ܂�</td><td class="b2">$chara[4]</td>
<td class="b1" id="td2">����</td><td class="b2">$esex</td></tr>
<tr><td class="b1" id="td2">�W���u</td><td class="b2">$chara_syoku[$chara[14]]</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
<tr><td class="b1" id="td2">STR</td><td align="left" class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$chara[7] + $item[8]</b></td>
<td class="b1" id="td2">INT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$chara[8] + $item[9]</b></td></tr>
<tr><td class="b1" id="td2">DEX</td><td align="left" class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$chara[9] + $item[10]</b></td>
<td class="b1" id="td2">VIT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$chara[10] + $item[11]</b></td></tr>
<tr><td class="b1" id="td2">LUK</td><td align="left" class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$chara[11] + $item[12]</b></td>
<td class="b1" id="td2">EGO</td><td align="left" class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$chara[12] + $item[13]</b></td></tr>
<tr><td id="td2" class="b2">������</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu</b></td>
<td id="td2" class="b2">���</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$sake</b></td></tr>
<tr><td id="td2" class="b2">��S��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu</b></td>
<td id="td2" class="b2">�K�E��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$hissatu_ritu</b></td></tr>
<tr><td class="b1" id="td2">�Z�������R�����g</td><td colspan="3" align="center" class="b2"><input type="text" name=waza value="$chara[23]" size=50></td></tr>
<tr><td id="td2" class="b1">

�ύX�����X�e�[�^�X��o�^><td align="center" colspan=3 class="b2">
<input type=hidden name=mode value=st_buy>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��o�^����">
</td></tr>
</form>
</table>
</table></td></tr></table>
EOM

	&footer;

	exit;
}

#----------------#
#  �ύX�o�^���  #
#----------------#
sub st_buy {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if($in{'id'} eq test){
		&error("�e�X�g�L�����̓X�e�[�^�X�ύX�͂ł��܂���$back_form");
	}

	if($in{'site'} eq "") {
		$in{'site'} = '�����̂b�f�h�̂g�o';
	}
	if($in{'url'} eq "") {
		$in{'url'} = 'http://www.eriicu.com';
	}

	if (length($in{'waza'}) > 40) {
		&error("�N���e�B�J���R�����g���������܂��I$back_form");
	}

	foreach (@ban_word) {
		if(index($in{'waza'},$_) >= 0) {
			$in{'mesname'} = $aite_data[4];
			&error("�֎~��u$_�v���܂܂�Ă��܂�$back_form");
		}
	}

	$chara[2] = $in{'site'};
	$chara[3] = $in{'url'};
	$chara[50] = $in{'sgazo'};
	$chara[145] = $in{'shai'};
	if($in{'chan'} > 90000 and $chara[0] ne "fufufu" and $chara[0] ne "jupiter" and $chara[0] ne "togetoge" and $chara[0] ne "aisai" and $chara[0] ne "kazuma" and $chara[0] ne "1357"){
		&error("���̃`�����l���𗘗p���錠��������܂���B$back_form");
	}else{
		$chara[96] = $in{'chan'};
	}
	if($in{'chan2'} > 90000 and $chara[0] ne "jupiter" and $chara[0] ne "togetoge" and $chara[0] ne "aisai" and $chara[0] ne "kazuma" and $chara[0] ne "1357"){
		&error("���̃`�����l���𗘗p���錠��������܂���B$back_form");
	}else{
		$chara[180] = $in{'chan2'};
	}
	if($chara[30]%1000!=0){$chara[30]=0;}
	if($in{'chara'}==4649 and $chara[30]!=1000 and $chara[30]!=3000){$chara[30]+=1000;}
	else{
		open(IN,"data/img.cgi");
		@img_data = <IN>;
		close(IN);
		$no_img_data=@img_data;
		if (200<$in{'chara'} or 201+$no_img_data>=$in{'chara'}) {
			open(IN,"senyou.cgi");
			@member_data = <IN>;
			close(IN);
			foreach (@member_data) {
				($cid,$cno) = split(/<>/);
				if ($cno == $in{'chara'} and $cid ne $chara[0]) {
					&error("���̃A�C�R���͕ʂ̐l�̐�p�A�C�R���ł��B$back_form");
				}
			}
		}
		$chara[6] = $in{'chara'};
	}
	if($in{'waza'} eq "���J�e����!!" and $chara[30]!=2000 and $chara[30]!=3000){$chara[30]+=2000;}
	else{$chara[23] = $in{'waza'};}

	if($in{'autoyado'}){$chara[36] = $in{'autoyado'};}

	if($in{'mainchat'}){$chara[60] = $in{'mainchat'};}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

 print <<"EOM";
<h1>$chara[4]����̃X�e�[�^�X��ύX���܂���</h1><br>
<form action="$scriptst" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�X�e�[�^�X�ύX��ʂ�">
</form>
EOM

	&footer;

	exit;
}
