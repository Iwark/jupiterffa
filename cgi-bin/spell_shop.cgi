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
<form action="./spell_shop.cgi" method="post">
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

	&item_load;

	&header;

	print <<"EOM";
<h1>�X�y���V���b�v</h1>
<hr size=0>

<FONT SIZE=3>
<B>�X�y���V���b�v�̓X��</B><BR>
�u<B>$chara[4]</B>���B���C�ɂ��Ă������H<BR>
�����̕i���A���Ȃ��Ɏg�����Ȃ��邩�ǂ����E�E�E�B�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
���݂̖��@ NO�F$chara[59]<br>
EOM
if ($chara[55]==3 or $chara[56]==3 or $chara[57]==3 or $chara[58]==3){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=1>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>001</th><th>�t�@�C�A</th><th>50000G</th>
	<th>�����@�t�@�C�A������܂��B�_���[�W���t�o�B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=2>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>002</th><th>�t�@�C��</th><th>75000G</th>
	<th>�����@�t�@�C��������܂��B�_���[�W���t�o�B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=3>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>003</th><th>�t�@�C�K</th><th>200000G</th>
	<th>�����@�t�@�C�K������܂��B�_���[�W��t�o�B</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=4>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>004</th><th>�u���U�h</th><th>50000G</th>
	<th>�����@�u���U�h������܂��B����_���[�W���_�E���B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=5>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>005</th><th>�u���U��</th><th>75000G</th>
	<th>�����@�u���U��������܂��B����_���[�W���_�E���B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=6>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>006</th><th>�u���U�K</th><th>200000G</th>
	<th>�����@�u���U�K������܂��B����_���[�W��_�E���B</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=7>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>007</th><th>�T���_�[</th><th>50000G</th>
	<th>�����@�T���_�[������܂��B���������_�E���B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=8>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>008</th><th>�T���_��</th><th>75000G</th>
	<th>�����@�T���_��������܂��B�����𒆃_�E���B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=9>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>009</th><th>�T���_�K</th><th>200000G</th>
	<th>�����@�T���_�K������܂��B�������_�E���B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂ō����@�͔����܂���B
EOM
}
if ($chara[55]==13 or $chara[56]==13 or $chara[57]==13 or $chara[58]==13){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=11>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>011</th><th>�q�[��</th><th>50000G</th>
	<th>�����@�q�[��������܂��B</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=12>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>012</th><th>�q�[����</th><th>100000G</th>
	<th>�����@�q�[����������܂��B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=13>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>013</th><th>�q�[���K</th><th>200000G</th>
	<th>�����@�q�[���K������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂Ŕ����@�͔����܂���B
EOM
}
if ($chara[55]==27 or $chara[56]==27 or $chara[57]==27 or $chara[58]==27){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�E�p</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=21>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>021</th><th>���g</th><th>50000G</th>
	<th>�E�p���g������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�E�p�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�E�p�����v���Ȃ��̂ŔE�p�͔����܂���B
EOM
}
if ($chara[55]==31 or $chara[56]==31 or $chara[57]==31 or $chara[58]==31){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�Ԗ��@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=31>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>031</th><th>�h���C��</th><th>50000G</th>
	<th>�Ԗ��@�h���C��������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�Ԗ��@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�Ԗ��@�����v���Ȃ��̂ŐԖ��@�͔����܂���B
EOM
}
if ($chara[55]==35 or $chara[56]==35 or $chara[57]==35 or $chara[58]==35){
	print <<"EOM";
	<form action="./spell_shop.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=41>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>041</th><th>�X���E</th><th>50000G</th>
	<th>�����@�X���E������܂��B</th></tr>
	<tr><th>
EOM
	if ($item[0] eq "�ŕ����̌�" and $item[3] eq "�ł̉H��" and $item[6] eq "�ł̈�"){
		if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=43>";}
		else{print "�~";}
		print <<"EOM";
		</th>
		<th>043</th><th>�_�[�N���e�I</th><th>100000000G</th>
		<th>�����@���`���e�I������܂��B</th></tr>
EOM
	}
		print <<"EOM";
	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂Ŏ����@�͔����܂���B
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �@�X�L������  #
#----------------#
sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("���������X�L����I��ł�������$back_form"); }

	if ($in{'ps_no'}==1){$ps_gold = 50000;}
	if ($in{'ps_no'}==2){$ps_gold = 75000;}
	if ($in{'ps_no'}==3){$ps_gold = 200000;}
	if ($in{'ps_no'}==4){$ps_gold = 50000;}
	if ($in{'ps_no'}==5){$ps_gold = 75000;}
	if ($in{'ps_no'}==6){$ps_gold = 200000;}
	if ($in{'ps_no'}==7){$ps_gold = 50000;}
	if ($in{'ps_no'}==8){$ps_gold = 75000;}
	if ($in{'ps_no'}==9){$ps_gold = 200000;}
	if ($in{'ps_no'}==11){$ps_gold = 50000;}
	if ($in{'ps_no'}==12){$ps_gold = 100000;}
	if ($in{'ps_no'}==13){$ps_gold = 200000;}
	if ($in{'ps_no'}==21){$ps_gold = 50000;}
	if ($in{'ps_no'}==31){$ps_gold = 50000;}
	if ($in{'ps_no'}==41){$ps_gold = 50000;}
	if ($in{'ps_no'}==43){$ps_gold = 100000000;}
	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[59] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�X�y���V���b�v�̓X��</B><BR>
�u���x����`�I<br>
���ɖ��@�����X�����Ă��Ȃ�A�����Ȃ���I�n�n�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
