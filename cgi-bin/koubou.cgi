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
<form action="koubou.cgi" >
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

&haigo;

&error;

exit;

#----------#
#  �z����  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	&item_load;

	if($chara[70]<1){&error("�G���[");}

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
	if(!$chara[98]){$chara[98]=0;}
	if(!$chara[99]){$chara[99]=0;}
	&header;

	print <<"EOM";
<h1>�H�[</h1>
<hr size=0>
<FONT SIZE=3>
<B>�H�[�̂�������</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
���������̏ꏊ���m���Ă��邩�E�E�E<br>
�m�炸�ɗ��p����͓̂��Ƃ͌�����ȁB<br>
�����ł́A����ȑ�������邱�Ƃ���\�\\���B�v
</FONT>
<br>���݂̏������F$chara[19] �f
<br>�����΂̏����F$chara[99] ��
<br><hr>���݂̑���<br>
<table>
<tr>
<td id="td2" class="b2">����</td><td align="right" class="b2">$item[0] $bukilv</td>
<td id="td2" class="b2">�U����</td><td align="right" class="b2">$item[1]</td>
</tr>
<tr>
<td id="td2" class="b2">�h��</td><td align="right" class="b2">$item[3] $bogulv</td>
<td id="td2" class="b2">�h���</td><td align="right" class="b2">$item[4]</td>
</tr>
</table>
<table width = "100%">
<tr>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_soubi">
<td width = "25%" align = "center" valign = "top">
�{�́i����j
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���i</th></tr>
EOM
	$i = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
EOM
if($ino==1400){
		print << "EOM";
�~
EOM
}else{
		print << "EOM";
<input type=radio name=item_no1 value="$i">
EOM
}
		print << "EOM";
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
�Ώہi����j
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���i</th></tr>
EOM
	$g = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
EOM
if($ino==1400){
		print << "EOM";
�~
EOM
}else{
		print << "EOM";
<input type=radio name=item_no2 value="$g">
EOM
}
		print << "EOM";
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$g++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
�{�́i�h��j
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���i</th></tr>
EOM
	$d = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defd=$d+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$defd">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$d++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
�Ώہi�h��j
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���i</th></tr>
EOM
	$e = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defe = $e+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$defe">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$e++;
	}
		print << "EOM";
</table>
</td>
<table>
<br><br>
<input type=submit class=btn value="��������">
</table>
</form>
</table>
<table>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=submit class=btn value="�����΂𔃂�����(1���f)">
</form>
</table>
<table>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=1>
<input type=submit class=btn value="�U�Z�b�g�̂��������p�b�N�𔃂�(5���f)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=2>
<input type=submit class=btn value="30�Z�b�g�̂��������p�b�N�𔃂�(24���f)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=3>
<input type=submit class=btn value="100�Z�b�g�̂��������p�b�N�𔃂�(75���f)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=4>
<input type=submit class=btn value="300�Z�b�g�̂��������p�b�N�𔃂�(200���f)">
</form>
</table>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	if($in{'item_no1'} > 99){
		$item_no1 = $in{'item_no1'} - 100;
		$souko_def[$item_no1] =~ s/\n//g;
		$souko_def[$item_no1] =~ s/\r//g;
		($ino1,$iname1,$idmg1,$igold1,$ihit1,$ilv1,$iexp1) = split(/<>/,$souko_def[$item_no1]);
	}else{
		$item_no1 = $in{'item_no1'};
		$souko_item[$item_no1] =~ s/\n//g;
		$souko_item[$item_no1] =~ s/\r//g;
		($ino1,$iname1,$idmg1,$igold1,$ihit1,$ilv1,$iexp1) = split(/<>/,$souko_item[$item_no1]);
	}
	if($in{'item_no2'} > 99){
		$item_no2 = $in{'item_no2'} - 100;
		$souko_def[$item_no2] =~ s/\n//g;
		$souko_def[$item_no2] =~ s/\r//g;
		($ino2,$iname2,$idmg2,$igold2,$ihit2,$ilv2,$iexp2) = split(/<>/,$souko_def[$item_no2]);
	}else{
		$item_no2 = $in{'item_no2'};
		$souko_item[$item_no2] =~ s/\n//g;
		$souko_item[$item_no2] =~ s/\r//g;
		($ino2,$iname2,$idmg2,$igold2,$ihit2,$ilv2,$iexp2) = split(/<>/,$souko_item[$item_no2]);
	}
	if($item_no1 == $item_no2){&error("�����A�C�e���ł��B");}
	if($iname1 eq "�G\�b\�O\�\\�[\�h" and $iname2 eq "�X\�s\�X\�\\�[\�h"){
		$mes = "�����A�f���炵���g�ݍ��킹�����B����͗ǂ������ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂͂R���B���킷�邩�����H";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1173;
		}else{
			$it_no = 1174;
		}
	}elsif($iname1 eq "�}�V���K��" and $iname2 eq "�L���[�{�E"){
		$mes = "���[�B����͂���́B�ǂ��g�݂��킹���ˁB<br>";
		$mes.= "�K�v�ȍ����΂�4���B���킷�邩�����H";
		$gouseiseki=4;
		if(int(rand(3))==0){
			$it_no = 1176;
		}else{
			$it_no = 1177;
		}
	}elsif($iname1 eq "�^�~�t��" and $iname2 eq "�L���O�i�C�t"){
		$mes = "�܂��܂��̑g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�3���B���킷�邩�����H";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1179;
		}else{
			$it_no = 1180;
		}
	}elsif($iname1 eq "�X�s�A" and $iname2 eq "����"){
		$mes = "�܂��܂��̑g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�3���B���킷�邩�����H";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1182;
		}else{
			$it_no = 1183;
		}
	}elsif($iname1 eq "������" and $iname2 eq "������"){
		$mes = "�Ȃ�Ƃ������A���x�����オ�肻���ȑg�ݍ��킹���ȁB<br>";
		$mes.= "�K�v�ȍ����΂�4���B���킷�邩�����H";
		$gouseiseki=4;
		if(int(rand(3))==0){
			$it_no = 1185;
		}else{
			$it_no = 1186;
		}
	}elsif($iname1 eq "���[�[�̏�" and $iname2 eq "�G���t�B���{�E"){
		$mes = "�܂��܂��̑g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�5���B���킷�邩�����H";
		$gouseiseki=5;
		if(int(rand(3))==0){
			$it_no = 1188;
		}else{
			$it_no = 1189;
		}
	}elsif($iname1 eq "���쌕" and $iname2 eq "������"){
		$mes = "�Ђ��[�B�����낵�����킪�ł��������B<br>";
		$mes.= "�K�v�ȍ����΂�15���B���킷�邩�����H";
		$gouseiseki=15;
		if(int(rand(3))==0){
			$it_no = 1191;
		}else{
			$it_no = 1192;
		}
	}elsif($iname1 eq "���J��" and $iname2 eq "�ŋ���"){
		$mes = "���������A���������˂��ȁB����ȋ��������I�H<br>";
		$mes.= "�K�v�ȍ����΂�20���B���킷�邩�����H";
		$gouseiseki=20;
		if(int(rand(3))==0){
			$it_no = 1194;
		}else{
			$it_no = 1195;
		}
	}elsif($iname1 eq "�_��" and $iname2 eq "���̌�"){
		$mes = "�\���̂��Ȃ��g�ݍ��킹���ȁB�ǂ������ł���Ƃ����Ȃ�<br>";
		$mes.= "�K�v�ȍ����΂�10���B���킷�邩�����H";
		$gouseiseki=10;
		if(int(rand(3))==0){
			$it_no = 1170;
		}else{
			$it_no = 1170;
		}
	}elsif($iname1 eq "�鉤�o��" and $iname2 eq "������"){
		$mes = "����ȏ�̑g�ݍ��킹�Ȃǂ��̐��ɑ��݂��Ȃ��B<br>";
		$mes.= "�K�v�ȍ����΂�50���B���킷�邩�����H";
		$gouseiseki=50;
		if(int(rand(3))==0){
			$it_no = 1197;
		}else{
			$it_no = 1198;
		}
	}elsif($iname1 eq "���ʂ̏�" and $iname2 eq "�~�l���o�r�X�`�F"){
		$mes = "�܂��܂��̑g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�3���B���킷�邩�����H";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 2152;
		}else{
			$it_no = 2153;
		}
	}elsif($iname1 eq "�ŕ����̌�" and $iname2 eq "�ł̉H��"){
		$mes = "�ǂ��Z���X���Ă�ȁB<br>";
		$mes.= "�K�v�ȍ����΂�5���B���킷�邩�����H";
		$gouseiseki=5;
		if(int(rand(3))==0){
			$it_no = 2155;
		}else{
			$it_no = 2156;
		}
	}elsif($iname1 eq "������" and $iname2 eq "������"){
		$mes = "�ǂ��Z���X���Ă�ȁB<br>";
		$mes.= "�K�v�ȍ����΂�6���B���킷�邩�����H";
		$gouseiseki=6;
		if(int(rand(3))==0){
			$it_no = 2158;
		}else{
			$it_no = 2159;
		}
	}elsif($iname1 eq "���l�̊Z" and $iname2 eq "������"){
		$mes = "�܂��܂��̑g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�3���B���킷�邩�����H";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 2161;
		}else{
			$it_no = 2162;
		}
	}elsif($iname1 eq "�����̊Z" and $iname2 eq "��̋�����"){
		$mes = "�ǁ[�����B����܂悳��������Ȃ���<br>";
		$mes.= "�K�v�ȍ����΂�2���B���킷�邩�����H";
		$gouseiseki=2;
		if(int(rand(3))==0){
			$it_no = 2164;
		}else{
			$it_no = 2165;
		}
	}elsif($iname1 eq "�p�Y�{��" and $iname2 eq "����3000"){
		$mes = "�ǂ��g�ݍ��킹���ȁB�Ǖ����ł���Ƃ݂邺��<br>";
		$mes.= "�K�v�ȍ����΂�7���B���킷�邩�����H";
		$gouseiseki=7;
		if(int(rand(3))==0){
			$it_no = 2167;
		}else{
			$it_no = 2168;
		}
	}elsif($iname1 eq "�q�[���[�X�[�c" and $iname2 eq "���C�_�[�X�[�c"){
		$mes = "�Ȃ�ėǂ��g�ݍ��킹���I���҂��Ȃ�<br>";
		$mes.= "�K�v�ȍ����΂�10���B���킷�邩�����H";
		$gouseiseki=10;
		if(int(rand(3))==0){
			$it_no = 2170;
		}else{
			$it_no = 2171;
		}
	}elsif($iname1 eq "���~��" and $iname2 eq "���~�Z"){
		$mes = "�ӂށB�g�Əo�邩���Əo�邩�c<br>";
		$mes.= "�K�v�ȍ����΂�8���B���킷�邩�����H";
		$gouseiseki=8;
		if(int(rand(3))==0){
			$it_no = 2173;
		}else{
			$it_no = 2174;
		}
	}elsif($iname1 eq "�X�[�p�[�X�[�c" and $iname2 eq "�剮�~�Z"){
		$mes = "���������B�x������ȁB��������ΓV�������B<br>";
		$mes.= "�K�v�ȍ����΂�25���B���킷�邩�����H";
		$gouseiseki=25;
		if(int(rand(3))==0){
			$it_no = 2176;
		}else{
			$it_no = 2177;
		}
	}elsif($iname1 eq "�L���E��" and $iname2 eq "�����̊Z"){
		$mes = "����ȏ�̑g�ݍ��킹�͖��������B�_�ɂł��Ȃ���肩�H<br>";
		$mes.= "�K�v�ȍ����΂�50���B���킷�邩�����H";
		$gouseiseki=50;
		if(int(rand(3))==0){
			$it_no = 2179;
		}else{
			$it_no = 2180;
		}
	}elsif($iname1 eq "�A���e�}�X�[�c" and $iname2 eq "������"){
		$mes = "�����E�E�E�����̃x�[�X�͎ア���E�E�E�ʔ����ȁB�Ƃ������������Ɩ����g�ݍ��킹���ȁB<br>";
		$mes.= "���ʂ��m�肽���B���ʂɍ�����1�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2228;
		}else{
			$it_no = 2229;
		}
	}elsif($iname1 eq "�~����" and $iname2 eq "������"){
		$mes = "�����E�E�E�����̃x�[�X�͎ア���E�E�E�ʔ����ȁB�Ƃ������������Ɩ����g�ݍ��킹���ȁB<br>";
		$mes.= "���ʂ��m�肽���B���ʂɍ�����1�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2231;
		}else{
			$it_no = 2232;
		}
	}elsif($iname1 eq "��񂻂̂P�O" and $iname2 eq "10����"){
		$mes = "�����E�E�E�����̃x�[�X�͎ア���E�E�E�ʔ����ȁB�Ƃ������������Ɩ����g�ݍ��킹���ȁB<br>";
		$mes.= "���ʂ��m�肽���B���ʂɍ�����1�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2234;
		}else{
			$it_no = 2235;
		}
	}elsif($iname1 eq "�f�X�y�i���e�B" and $iname2 eq "�V���̏�"){
		$mes = "�����E�E�E�����̃x�[�X�͎ア���E�E�E�ʔ����ȁB�Ƃ������������Ɩ����g�ݍ��킹���ȁB<br>";
		$mes.= "���ʂ��m�肽���B���ʂɍ�����1�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 1228;
		}else{
			$it_no = 1229;
		}
	}elsif($iname1 eq "���[���C" and $iname2 eq "���~�b�^�["){
		$mes = "�����E�E�E�����̃x�[�X�͎ア���E�E�E�ʔ����ȁB�Ƃ������������Ɩ����g�ݍ��킹���ȁB<br>";
		$mes.= "���ʂ��m�肽���B���ʂɍ�����1�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 1231;
		}else{
			$it_no = 1232;
		}
	}elsif($iname1 eq "���[�[���t�B��" and $iname2 eq "���|"){
		$mes = "���ށB�ǂ������̑g�ݍ��킹���ȁB<br>";
		$mes.= "������20�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=20;
		if(int(rand(3))==0){
			$it_no = 1234;
		}else{
			$it_no = 1235;
		}
	}elsif($iname1 eq "����_��" and $iname2 eq "����^��"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1237;
		}else{
			$it_no = 1238;
		}
	}elsif($iname1 eq "���`�̞��_"){
		$mes = "�����͂��́B���s�����܂����悤���ȁI<br>";
		$mes.= "������100�ł�����x���킵�Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1237;
		}else{
			$it_no = 1238;
		}
	}elsif($iname1 eq "�������イ" and $iname2 eq "�y�b�g�j�E��"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1242;
		}else{
			$it_no = 1243;
		}
	}elsif($iname1 eq "����_�Z" and $iname2 eq "����^��"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 2237;
		}else{
			$it_no = 2238;
		}
	}elsif($iname1 eq "���`�̋���" and $iname2 eq "���`�̓S��"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1240;
		}else{
			$it_no = 1240;
		}
	}elsif($iname1 eq "���`�̏�" and $iname2 eq "���`�̊�"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 2240;
		}else{
			$it_no = 2240;
		}
	}elsif($iname1 eq "�E�f�t����" and $iname2 eq "�W���o�[�i��"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1170;
		}else{
			$it_no = 1170;
		}
	}elsif($iname1 eq "�c�f�A�b�N�X" and $iname2 eq "�V���h�[�i�C�t"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������150�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=150;
		if(int(rand(3))==0){
			$it_no = 1194;
		}else{
			$it_no = 1194;
		}
	}elsif($iname1 eq "�G�O�W�F�\\�[�h" and $iname2 eq "�I���W���X�^�b�t"){
		$mes = "��͂����ł���������<br>";
		$mes.= "������200�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=200;
		if(int(rand(3))==0){
			$it_no = 1341;
		}else{
			$it_no = 1341;
		}
	}elsif($iname1 eq "����J�u�g" and $iname2 eq "���`�̃}���g"){
		$mes = "�ʎ����̑��������܂ꂻ������<br>";
		$mes.= "������100�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=100;
		$it_no = 2246;
	}elsif($iname1 eq "�X�J�C�X�s�A" and $iname2 eq "�X�J�C�A�N�X"){
		$mes = "���̋C�z�c�G�A���K���c�B���������ȁc�B<br>";
		$mes.= "������1500�ł���Ă�邼�B���킷�邩�����H";
		$gouseiseki=1500;
		$it_no = 1356;
	}elsif($iname1 eq $iname2){
		$gouseiseki=1;
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
			if($iname1 eq $si_name){$hit=1;last;}
		}
		if($hit!=1){
			foreach(@log_def){
				($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
				if($iname1 eq $si_name){$hit=2;last;}
			}	
		}
		if($hit==1 and $si_no > 1172){
			$mes = "���ꓯ���������E�E�E�B���ꓯ�������͎��s�ł��Ȃ��\���������B<br>";
			$mes.= "�����Ă���Ă��������c�B���������獇����1��Ⴈ���B���킷�邩�����H";
			$it_no = $si_no - 1;
		}elsif($hit==2 and $si_no > 2151){
			$mes = "���ꓯ���������E�E�E�B���ꓯ�������͎��s�ł��Ȃ���\�\\���������B<br>";
			$mes.= "�����Ă���Ă��������c�B���������獇����1��Ⴈ���B���킷�邩�����H";
			$it_no = $si_no - 1;
		}else{
			$mes = "<font color=\"red\" size=5>$iname1��$iname2�̑g�ݍ��킹�̓_�����B";
			$mes.= "��������߂Ȃ����B<br></font>�K�v�ȍ����΂͂P���B���킷�邩�����H";
			if($in{'item_no1'} > 99){
				if(int(rand(2))==0){
					$it_no = 2001 + int(rand(75));
				}else{
					$it_no = 2091 + int(rand(10));
				}
			}else{
				if(int(rand(2))==0){
					$it_no = 1001 + int(rand(75));
				}else{
					$it_no = 1091 + int(rand(10));
				}
			}
		}
	}else{
		$mes = "<font color=\"red\" size=5>$iname1��$iname2�̑g�ݍ��킹�̓_�����B��������߂Ȃ���<br>";
		$mes.= "</font>�K�v�ȍ����΂͂P���B���킷�邩�����H";
		$gouseiseki=1;
		if($in{'item_no1'} > 99){
			if(int(rand(2))==0){
				$it_no = 2001 + int(rand(75));
			}else{
				$it_no = 2091 + int(rand(10));
			}
		}else{
			if(int(rand(2))==0){
				$it_no = 1001 + int(rand(75));
			}else{
				$it_no = 1091 + int(rand(10));
			}
		}
	}

if (!$in{'kakunin'}){
	&unlock($lock_file,'SI');
	&header;
	print << "EOM";
<center>
<h3>�H�[�̂�������u$mes�v</h3>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no1 value="$in{'item_no1'}">
<input type=hidden name=item_no2 value="$in{'item_no2'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="���킷��">
</form>
</center>
EOM
	$new_chara = $chara_log;
	&shopfooter;
	&footer;
	exit;
}
	open(IN,"$def_file");
	@log_def = <IN>;
	close(IN);

	open(IN,"$item_file");
	@log_item = <IN>;
	close(IN);

	if($chara[99]<$gouseiseki){&error("�����΂�$gouseiseki�K�v�ł�$back_form");}
	else{$chara[99]-=$gouseiseki;}

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
		if($it_no == $si_no){$hit=1;last;}
	}
	if($hit!=1){
	foreach(@log_def){
		($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
		if($it_no == $si_no){$hit=2;last;}
	}
	}
	if($hit!=1 and $hit!=2){&error("���̑g�ݍ��킹�͓���ȈׁA�����ł��܂���B");}

	if($in{'item_no1'} > 99){
		if($hit==1){
			$souko_def[$item_no1] = ();
			$souko_item[$item_no2] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}elsif($in{'item_no2'} > 99){
			$souko_def[$item_no2] = ();
			$souko_def[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}else{
			$souko_item[$item_no2] = ();
			$souko_def[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}
	}elsif($in{'item_no2'} > 99){
		if($hit==1){
			$souko_def[$item_no2] = ();
			$souko_item[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}else{
			$souko_item[$item_no1] = ();
			$souko_def[$item_no2] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}
	}else{
		$souko_item[$item_no2] = ();
		$souko_item[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
	}

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	&item_regist;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$si_name���ł��܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub gouseiseki {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'tokutoku'}==1){
		if($chara[19]<500000000){&error("����������܂���$back_form");}
		else{$chara[19]-=500000000;}
		$chara[99]+=6;	
	}elsif($in{'tokutoku'}==2){
		if($chara[19]<2400000000){&error("����������܂���$back_form");}
		else{$chara[19]-=2400000000;}
		$chara[99]+=30;	
	}elsif($in{'tokutoku'}==3){
		if($chara[19]<7500000000){&error("����������܂���$back_form");}
		else{$chara[19]-=7500000000;}
		$chara[99]+=100;	
	}elsif($in{'tokutoku'}==4){
		if($chara[19]<20000000000){&error("����������܂���$back_form");}
		else{$chara[19]-=20000000000;}
		$chara[99]+=300;	
	}else{
		if($chara[19]<100000000){&error("����������܂���$back_form");}
		else{$chara[19]-=100000000;}
		$chara[99]+=1;
	}

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�����΂𔃂��܂���</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}