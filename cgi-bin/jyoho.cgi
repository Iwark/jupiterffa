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
<form action="jyoho.cgi" method="post">
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

&jyoho;

&error;

exit;

#----------#
#  ���  #
#----------#
sub jyoho {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>���</h1>
<hr size=0>
<FONT SIZE=3>
<B>��񉮂̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
��������R�A���d����Ă邺�[���B<br>
���ɕ�������͂킸�������A����������Ă����ΈႤ�����������邱�Ƃ����邼�B<br>
����ɁA�ŋ߁A���̃��x�����オ���ĂȁB�L�������𒲂ׂ���悤�ɂȂ������B<br>
���O�������Ă����ΑΏۂ����O�C�����ĂȂ��Ă��X�e�[�^�X�������Ă�낤�B�v<br>
</FONT>
EOM
if($chara[70]>=1){
	print <<"EOM";
<form action="jyouhou2.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��񉮂Q��">
</form>
EOM
}
	print <<"EOM";
<br>���݂̏������F$chara[19] �f
<hr size=0>
	<form action="./jyoho.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=jyoho_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>���̎��</th><th>�l�i</th><th>���̐�</th></tr>
	<th>
EOM
	if ($chara[19] >= 20000) {print "<input type=radio name=ps_no value=1>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>001</th><th>�h���S���G�b�O�ɂ���</th><th>20000G</th><th>4�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 10000) {print "<input type=radio name=ps_no value=2>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>002</th><th>�G�b�O�\\�[�h�ɂ���</th><th>10000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 15000) {print "<input type=radio name=ps_no value=3>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>003</th><th>����y�b�g�ɂ���</th><th>15000G</th><th>3�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=4>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>004</th><th>�]�E��X�e�U��ɂ���</th><th>30000G</th><th>2�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=5>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>005</th><th>����ɂ���</th><th>30000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=6>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>006</th><th>�V���E�ɂ���</th><th>30000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000) {print "<input type=radio name=ps_no value=7>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>007</th><th>��͂�</th><th>5000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=8>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>008</th><th>�N���m��Ȃ�����</th><th>50000G</th><th>6�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 500000) {print "<input type=radio name=ps_no value=9>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>009</th><th>���b</th><th>500000G</th><th>3�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 1000000) {print "<input type=radio name=ps_no value=10>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>010</th><th>�U��포�Z</th><th>1000000G</th><th>3�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=11>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>011</th><th>���}�^�m�I���`</th><th>100000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=12>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>012</th><th>�������</th><th>100000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 150000) {print "<input type=radio name=ps_no value=13>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>013</th><th>���̖S��</th><th>150000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 8000000) {print "<input type=radio name=ps_no value=14>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>014</th><th>���~�b�^�[</th><th>8000000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=15>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>015</th><th>�h���[���R���{</th><th>100000000G</th><th>4�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 300000000) {print "<input type=radio name=ps_no value=16>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>016</th><th>�I���W�i������</th><th>300000000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 500000000) {print "<input type=radio name=ps_no value=17>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>017</th><th>����</th><th>500000000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=18>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>018</th><th>�����̃m�[�g�Ɩ����E</th><th>100000000G</th><th>8�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 800000000) {print "<input type=radio name=ps_no value=19>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>019</th><th>���q����</th><th>800000000G</th><th>1�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 1000000000) {print "<input type=radio name=ps_no value=20>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>020</th><th>���������@</th><th>1000000000G</th><th>2�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=21>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>021</th><th>�����@</th><th>100000000G</th><th>6�R</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=22>";}
	else{print "�~";}
	print <<"EOM";
	</th><th>022</th><th>�`���C�i�H</th><th>100000000G</th><th>1�R</th></tr>
	</table>
	<br><br>
	<input type=submit class=btn value="���𔃂�">
	</form>
EOM
	print <<"EOM";
	<form action="./jyoho.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type="text" name="taisyo" size=20><br>
	<input type=hidden name=mode value=mem_sts>
	<input type=submit class=btn value="�L�������𒲂ׂ�">
	</form>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub jyoho_buy {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("�~��������I��ł�������$back_form"); }
	if ($in{'ps_no'}==1){$ps_gold = 20000;}
	if ($in{'ps_no'}==2){$ps_gold = 10000;}
	if ($in{'ps_no'}==3){$ps_gold = 15000;}
	if ($in{'ps_no'}==4){$ps_gold = 30000;}
	if ($in{'ps_no'}==5){$ps_gold = 30000;}
	if ($in{'ps_no'}==6){$ps_gold = 30000;}
	if ($in{'ps_no'}==7){$ps_gold = 5000;}
	if ($in{'ps_no'}==8){$ps_gold = 50000;}
	if ($in{'ps_no'}==9){$ps_gold = 500000;}
	if ($in{'ps_no'}==10){$ps_gold = 1000000;}
	if ($in{'ps_no'}==11){$ps_gold = 100000;}
	if ($in{'ps_no'}==12){$ps_gold = 100000;}
	if ($in{'ps_no'}==13){$ps_gold = 150000;}
	if ($in{'ps_no'}==14){$ps_gold = 8000000;}
	if ($in{'ps_no'}==15){$ps_gold = 100000000;}
	if ($in{'ps_no'}==16){$ps_gold = 300000000;}
	if ($in{'ps_no'}==17){$ps_gold = 500000000;}
	if ($in{'ps_no'}==18){$ps_gold = 100000000;}
	if ($in{'ps_no'}==19){$ps_gold = 800000000;}
	if ($in{'ps_no'}==20){$ps_gold = 1000000000;}
	if ($in{'ps_no'}==21){$ps_gold = 100000000;}
	if ($in{'ps_no'}==22){$ps_gold = 100000000;}
	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	if($in{'ps_no'}==1){
	$ran=int(rand(4));
	if($ran==0){
$jyouhou="�u�h���S���G�b�O�v�Ƃ������ɋM�d�ȗ������̐��ɂ͂���炵���B<br>
�Ȃ�ł����̒�����͎푰�ŋ��̗��������܂��炵�����B<br>
������@�Ȃ񂾂��ȁA����y�b�g���������ɕ����������邱�Ƃ��|�C���g�炵���B";
}
	if($ran==1){
$jyouhou="�h���S���͂�A�G�b�O���琶�܂��炵���B<br>
�������Ƃ���B";
}
	if($ran==2){
$jyouhou="�h���S���G�b�O����ɓ������@�H<br>
�z������A�z��";
}
	if($ran==3){
$jyouhou="�G�b�O����ɓ���邽�߂ɂ́A���x��60�ȏ�ł���K�v������B<br>
�������Ƃ���B";
}
	}
	if($in{'ps_no'}==2){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="�`���̌��u�G�b�O�\\�[�h�v�A���̌��Ȃ痑�ɓ���o���l���ő�10�{�ɂȂ�Ƃ������B<br>
����������͓���B����{�X��|�����c���邢�͐������c���邢�́c�B<br>
�܂��A�����Ă�����������������̂͑f�l�ɂᖳ��������ȁB<br>
�������ĒT���Ȃ��Ă��A���Ԃ������ė�����Ă�Ƃ������낤�B";
}

	}
	if($in{'ps_no'}==3){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="��ꂽ���͂�A��������Ă��炤�Ƌ��������邾��H�������A<br>
�V�������𔃂����܂��΋���������Ȃ��񂾂�ȁB�m���Ă����H";
}
	if($ran==1){
$jyouhou="�ǂ�ȗ�����đ������牽���N���邼�B<br>
������A���E���ς��悤�ȁc����Ȃ��Ƃ���c";
}
	if($ran==2){
$jyouhou="�y�b�g�ɂ́A�ŏI�`�Ԃ�����B�Ⴆ�΃C�G���[�G�b�O�̓p���_�}�����ȁB<br>
�K�v�o���l��100���ɂȂ��Ă���ŏI�`�Ԃ��ȁB";
}
	}
	if($in{'ps_no'}==4){
	$ran=int(rand(2));
	if($ran==0){
$jyouhou="�ǂ�ȐE�Ƃ����������ĥ���H<br>
�܂��́A���@���m���d�v�ȐE�Ƃ��낤�ȁB�����떂�@���͋����I";
}
	if($ran==1){
$jyouhou="�X�e�[�^�X�|�C���g�A�����ƐU���Ă��邩�H<br>
�Z���������Ȃ��Ȃ�A�d�f�n������Ȃ��B<br>
�U����������Ȃ��Ȃ�A�c�d�w������Ȃ��B<br>
�U���͓����邵�A�Z����������Ȃ�΁A�U���͂��グ��ׂɂh�m�s��U��Ɨǂ����낤�B<br>
����ł��|�C���g�ɗ]�T������Ȃ�A�k�t�j�ŃN���e�B�J�������グ����A�r�s�q�ł���ɍU���͂��グ�悤�B<br>
�u�h�s�ł́A�g�o��h��͂��オ�邪�A�ǂ��炩�Ƃ����ƍU���͂̕����d�v���낤�ȁB";
}
	}
	if($in{'ps_no'}==5){
$jyouhou="����ɂ̓����N�Ƃ������̂�����c�����ł����������Ă����悤�B<br>
No.1�A�C�A���\\�[�h����No.10���[�j���O�X�^�[���X�Ŕ����Ă�A�C�e�����킾�ȁH�����ɉ����āA<br>
No.11���΂݂̏�A12�N���X�{�E�A13�v���Y�����b�h�A14���[���u���C�h�A15�t�����x���W��<br>
�����܂ł������N�P�̕��킾�cNo���オ��قǋ����ƍl���Ă����B�����āE�E�E<br>
No.16�d���̃��b�h�ANo.17�t���C���^���ANo.20�A�C�X�u�����h�ANo.25�ՓS�ȂǁANo.16�`No.30�̕���̓����N�Q���E�E�E<br>
�����N�R�͋e�ꕶ����t�F�A���[�e�[���A�T�C�R�_�K�[�ȂǁA�����N�S�̓O���O�j���A���J�A�j��̌����Ċ������B<br>
�����N�T�ɂȂ�ƃ��e�I�E�u���C�J�[�A�I���K�u���X�^�[�ȂǂƁA����ɋ��������ƂȂ�킯�����E�E�E<br>
���Ȃ݂ɃG�b�O�\\�[�h�Ȃǂ̓����N�U�����A�����N�U�͓���A�Ƃ������ƂŁA�����A�Ƃ͈Ⴄ�ȁB<br>
���łɈ��񂾁B������������鎞�́A�����N�̍��v�������Ȃ�悤�ɍ��������B�킩�������H<br>
�܂�������肷�邱�Ƃ����邾�낤����A���傭���傭����Ă���B";
	}
	if($in{'ps_no'}==6){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="�V���E���c�Y�o���A���������̂͌��̂��肩���낤�B<br>
�Ƃ���ŁA�y�b�g�͂��т��ёމ������Ď�������点���肷��ȁB<br>
����ȃy�b�g�������Ɛ����ł���ƁA���Ԃ������Ă����Ƃ����B���Ԃ��Ƃ́H<br>
�y�b�g�̃y�b�g�����m��Ȃ����E�ւ́u���v�ƕ\\�����Ă������̂��ȁB<br>
�����A���S�ɐ������~�܂������A���ꂪ�A�y�b�g�̉��Ԃ��̎������c�B<br>
������ɂ��܂���Ă�Ɨǂ����낤�B";
}
	}
	if($in{'ps_no'}==7){
$jyouhou="��͂��Ȃ�A����Ă�΃����X�^�[�����Ƃ���B";
	}
	if($in{'ps_no'}==8){
	$ran=int(rand(6));
	if($ran==0){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB<br>
�A���N�h�������񂪒񋟂��Ă��ꂽ��񂾁B<br>
���Ă��܂���������A�V���Ȑ�����������A�Ƃ������Ƃ��������B";
}
	if($ran==1){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB�����No�P���B<br>
�y�b�g�̂g�o�⃌�x���A�����čU���́A�����͋�����ŏ����͉��Ƃ��ł���̂͒m���Ă邩�H<br>
���̗͂��Ă����̂͋��낵�����񂾁B�����N���邩�킩���B";
}
	if($ran==2){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB�����No�Q���B<br>
�u����v�́A�u�S�[�`���v�Ɩ��Â���ꂽ�B�A���N�h��������̃Z���X�Ƀr�b�N�����B<br>
�A���N�h��������̌��ł��������炿�A�₪�āA���̖`���҂�y���ɉz����͂�g�ɂ����B<br>
�u�S�[�`���v���Ȃ��A�_�ɋ߂����݂Ƃ�����̂��A���̂Ƃ��͂܂��킩���Ă��Ȃ������B";
}
	if($ran==3){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB�����No�R���B<br>
�Ƃ���ŁA�i�����Ă��u�S�[�`���v�Ȃ̂́A�A���N�h�������񂪂��̖��O����������C�ɓ��������炾�B<br>
������A���܂��ɁA�i���O�ƁA��Ƃŋ�ʂ�����@���Ȃ��񂾁E�E�E<br>
�ʂ����āA�S�[�`���ɂ́u�S�b�h�o�[�h�v��u�h���S�����[�h�v�̂悤�ɁA�ŏI�`�Ԃ����݂���̂�<br>
���ɂ́A�A���N�h��������B������邱�Ƃ����ł��Ȃ������B�B�B";
}
	if($ran==4){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB�����No�S���B<br>
�₪�āA�S�[�`���ɕ�\�����o���B���͂�A���̑�\�݂́A����\�\\���Ȃ��B<br>
�ނ́A�키�S�̗l�ȑ�\�݂ł���Ȃ���A�D�����S������\�݂������B<br>
�ނ͐i\���̉�\���łǂ�ǂ�ƋZ���\���������B<br>
�����āE�E�E�A���ɁA�ނ́A�l�Ԃ�h\�����邱�Ƃ����A��\�\�ɂ����̂�����B";
}
	if($ran==5){
$jyouhou="�N���m��Ȃ����݂ɂ��Ă̏�񂾂ˁB�����No�T���B<br>
�_�̍��ƌĂ΂��A���o���_���ɁA����`��������B<br>
�_�́A����萶�܂�āA����^���鑶�݁B<br>
�_�́A���ߐ[���킯�ł͂Ȃ��A�C�܂���ŁA���������邱�Ƃ̕���������<br>
�_�́A�N�ɂ��E�����Ƃ��ł��Ȃ��B<br>
�����A���̓`����\�\\�����u�_�v�ɁA�S�[�`���́A���Ă���Ǝv��񂩁H";
}
	}
	if($in{'ps_no'}==9){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="��ꂽ���A���ʂɈ�������Ă��炨���Ƃ����3���f�����邾��H<br>
���́A���̗��𔃂��΁A�����ň�������ĖႦ�邺�B";
}
	if($ran==1){
$jyouhou="�ȂɁH�ŋ߃��x�����オ��ɂ����H�����A�㋉�҂̔Y�݂��ȁB<br>
����ȂƂ��́A���W�F���h�v���C�X�ŏ̍����グ�Ă݂ȁB�������Ƃ��邩����H";
}
	if($ran==2){
$jyouhou="�ȂɁH���b�h���[���h�̌����ǂ����Ă�����ł��Ȃ��H<br>
���͉ΓS���ŏI�`�Ԃ���Ȃ��̂Ɍ��������Ă���Ęb���B<br>
�����͂��Ȃ�̗��b�����A���܂�̌��̏o�Ȃ����ɋ��E�������炵���񂾁B";
}
	}
	if($in{'ps_no'}==10){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="�u���U�K�c����͒��X�̋Z���c���̌��ʂ͑��肪�������鎞�ɍł������ł���ȁB<br>
�Ȃɂ��S���̃_���[�W����C�ɗ��Ƃ��Ă���邩��ȁc�B";
}
	if($ran==1){
$jyouhou="�܂����U���ɍs�����Ď��ɋ��t�o���̓��ނ��̂��ĂȂ����낤�ȁH<br>
�ΐl�������A�C�e���𓐂ނ͔̂ƍ߂��B�ł��Ȃ����H��";
}
	if($ran==2){
$jyouhou="�ꌂ�K�E�B�m���̂Ƃ��ɔ����������ȁB�U���ł͔������₷�������ȁB<br>
����Ɩh��͂��d�v�ɂȂ肻�����ȁB";
}
	}
	if($in{'ps_no'}==11){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="���}�^�m�I���`���ǂ��ɂ��邩���āH<br>
�����̋��Ԃ��B���ꗬ�̖`���҂݂̂��s�����Ƃ��������̂��B<br>
�A���N�h��������H����������I�ɍs���Ă邺�B�����A�������̓G�̓G�O�C�̂��B<br>
�헪�I�ȃ����X�^�[�΂���łȁA�܂�PT�ōs�������M���h�ōs����������������Č��ǐ키���͈�l�ɂȂ�B<br>
����ɁA�����X�^�[�̋��͂Ȉꌂ�ő������Ԃ���ꂿ�܂����Ƃ�������Ă����񂾂���ȁc�B<br>
�f��ōs���Ζ��Ȃ�������������Ίi���Ƃɂ������ȁc�f��p�A�r���e�B�E�E�E�B";
}
	}
	if($in{'ps_no'}==12){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="���E�˔j��A���ԂŋH�ɁA��Ђ��o�邾��H<br>
�������͉�������Ђ���ȁ[�B�Ȃɂ��A�����x�`�N���X�́u�����i�v����ɓ���񂾂���ȁc�B<br>
�����A����������ȁB���܂���Ă����Ȃ����������B<br>
�֌W�Ȃ��񂾂��u�ŗ��v�m���Ă邩�H�ǂ����̎{�݂ŋ��͂Ȗ`���҂݂̂ɓn���Ă闑�炵�����B<br>
�ŗ��́A���������Ă��܂��Ă�100���f�Ō��ɖ߂���炵���B<br>
�����A���̏ꏊ�́A�������ɂ���������Ȃ��炵�����B�����R�����ĉ������ꏊ�𓖂����Ă݂ȁB";
}
	}
	if($in{'ps_no'}==13){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="���Ԃɋ��̖S�҂��Ă����{�X�����X�^�[���o�������ȁB<br>
������͖��B����������������Ă���΁A�P�^�[���Ƃ����炸�ɏu�E�ł��邻�������c�B<br>
���ʂɐ킨���Ƃ���Ɩ��B�܂��A�K�{�A�C�e�������A���v���ȁB<br>
���v�́A�b���ɒ��ӂ��Đ키�ƁA���c�̎�_���킩���Ă���B<br>
��x���c�ɍU�����N���[���q�b�g������A�����A�r���e�B��60�b��A�Đ킾�B<br>
�^���ǂ���΁A���Ƃ��キ�Ă��|����͂����B";
}
	}
	if($in{'ps_no'}==14){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="����̏�\��́u���~�b�^�[�v�B<br>
�u���~�b�^�[�v�Ƃ����̂͑�\���̖�\�O���ȁB�h\��B<br>
�u��\���v�́u��\�~�v�ɂ���B�u��\�~�v�ɂ��Ēm��Ȃ��z�ɂ͓�\��͂܂��������낤�B<br>
�������H�u��\�~�v�Łu�O\�p\�X\�q�v���u��\�ʂ̏��v�A�u��\�d�̊Z�v���E������A�E�����ꏊ���������Ă����񂾁B<br>
�����āA���̒��́u�O\�p\�X\�q�v�B��������\��̏�\��̌��ɂȂ�B<br>
������\�������āA�Ȃ�Ƃ��u��\�p\�X\�q�v�ɂ���B����ɐ�\������ƁA�u���~�b�^�[�v�ɂȂ�̂��B<br>
���̌�\�ʂ͐��܂����B���ł��A��\��ȃ����X�^�[�̕�\�l�ɂ͕K\�{���Ƃ��c�B<br>
���́A�u�O\�p\�X\�q�v���ǂ�����āu���~�b�^�[�v�ɐ�\�������邩�����c����͐F�X�����Ă݂鑼����܂��c�B";
}
	}
	if($in{'ps_no'}==15){
	$ran=int(rand(4));
	if($ran==0){
$jyouhou="�����Ƃ����W���u��m���Ă��邩�H<br>
�����ŋ߁A�A���N�h��������ɕ������񂾂��A�s�v�c�ȓ��A�r���e�B�������Ă���W���u���Ƃ����B<br>
���̓��A�r���e�B�̔��������͂������B�P�ڂ̓��A�r���e�B�Ɂu�h���[���R���{�v���Z�b�g���A<br>
�Q�ڂɁu�T�C�N�����v�A�R�ڂɁu�}�C�e�B�K�[�h�v���Z�b�g����B<br>
���ɂ���������������悤���B�u�}�C�e�B�T�C�N�����v�́A����̏󋵂ɂ����Đ��Ȍ��ʂ𔭊����邼�B";
}
	if($ran==1){
$jyouhou="�����Ƃ����W���u��m���Ă��邩�H<br>
�����ŋ߁A�A���N�h��������ɕ������񂾂��A�s�v�c�ȓ��A�r���e�B�������Ă���W���u���Ƃ����B<br>
���̓��A�r���e�B�̔��������͂������B�P�ڂ̓��A�r���e�B�Ɂu�h���[���R���{�v���Z�b�g���A<br>
�Q�ڂɁu������ԁv�A�R�ڂɁu�n���֔�΂��v���Z�b�g����B<br>
���ɂ���������������悤���B�u����n���֔�΂��v�́A���܂ł̏펯�𕢂��j��͂������A�g���Â炢�ꍇ������ȁB<br>
�����炭�A�u�ł̈߁v��u�S�ǂ̂����v�𑕔����Ďg���̂��������낤�B";
}
	if($ran==2){
$jyouhou="�����Ƃ����W���u��m���Ă��邩�H<br>
�����ŋ߁A�A���N�h��������ɕ������񂾂��A�s�v�c�ȓ��A�r���e�B�������Ă���W���u���Ƃ����B<br>
���̓��A�r���e�B�̔��������͂������B�P�ڂ̓��A�r���e�B�Ɂu�h���[���R���{�v���Z�b�g���A<br>
�Q�ڂɁu�K�E���@�v�A�R�ڂɁu�f�킷�v���Z�b�g����B<br>
���ɂ���������������悤���B�u�����v�́A���܂ł̏펯�𕢂��j��͂������A�g���Â炢�ꍇ������ȁB<br>
�����炭�A�u�d���A�W�A�v�𑕔����Ďg���̂��������낤�B";
}
	if($ran==3){
$jyouhou="�����Ƃ����W���u��m���Ă��邩�H<br>
�����ŋ߁A�A���N�h��������ɕ������񂾂��A�s�v�c�ȓ��A�r���e�B�������Ă���W���u���Ƃ����B<br>
���̓��A�r���e�B�̔��������͂������B�P�ڂ̓��A�r���e�B�Ɂu�h���[���R���{�v���Z�b�g���A<br>
�Q�ڂɁu���Ȃ�R���v�A�R�ڂɁu�h���S���u���X�v���Z�b�g����B<br>
���ɂ���������������悤���B�u���Ȃ�u���X�v�́A��񕜁E�S�̍U���̔��ɗL�p�ȃR���{���ȁB<br>
�Ƃ�������������𑕔����Ďg���̂��������낤�B";
}
	}
	if($in{'ps_no'}==16){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="�I���W�i������ɂ��Ă��B<br>
�����́w���̋�ԁx�œ���ł��鑕�����ȁB�S���������Ȃ��A�S���l�ׂ��������Ă��Ȃ����̂ɖ����̉�\�\\�������B<br>
���āA���������̕������肷�邱�Ƃ��ł����Ȃ�΁A���̎�舵���ɂ͏\\���C������ׂ����B<br>
������̈�ĕ��ɂ���āA�S��̕����֐i�������\�\\��������B�ȒP�ɐ������悤�c�B<br>
<br>
�@�܂��́A�����^�̕��킾�B�P���ɍU���͂������B<br>
�ł������₷�����A�S��̌^�̒��ł͈�Ă�̂��ȒP�ȕ����낤�B<br>
���̌^�Ɉ�Ă邽�߂ɂ́A�U���͂��グ��ނ̖�����g�p����΂悢�B<br>
<br>
�A���ɁA�K�E�^�̕��킾�B�P���ȍU���͂��������͂Ȃ����̂́A�K�E�Z�𔭓�����̂��������B<br>
�����ɂ������A�K�E�Z�𔭓��������̈З͂́A�z����₷�邾�낤�B<br>
���̌^�Ɉ�Ă邽�߂ɂ́A���������グ��ނ̖�����g�p����΂悢�B<br>
<br>
�B���́A�\\��\�^�̕��킾�B�U���͍͂����Ȃ����A�����̔\\�͂��������邱�Ƃ���\�\���B<br>
��������d���̔\\�͂��P�̕���Ŏ��Ă�Ƃ�����c�ƌ����΁A���̉��l�A�킩�邩�H<br>
���̌^�Ɉ�Ă邽�߂ɂ́A�U���͂ƁA���������グ��ނ̖�����A�ϓ��Ɏg�p���Ă����΂悢�B<br>
<br>
�C�Ō�ɁA����^�̕��킾�ȁB�����́A�ǂ����A�킩��Ȃ����Ƃ��炯���B<br>
���݂͊m�F����Ă��邪�c�B��������^�̕���ɂ��ď������ł���ΐ��񋳂��Ă���B<br>
<br>
�I���W�i�����킪�i��������A���̑����ł����Ĉ����E�̓G��|�����ƂŁA���ꂼ��̌^�ɂ������}�e���A������ł���悤�ɂȂ�B<br>
�u�����^�}�e���A�v�u�K�E�^�}�e���A�v�u�\\�͌^�}�e���A�v�u����^�}�e���A�v���ȁB<br>
���̃}�e���A�𑕔����邱�ƂŁA����͊i�i�ɋ����Ȃ邼�c�I<br>
�c�Ƃ܂��A���̒m���Ă�����́A����ȂƂ��낾�ȁB<br>
�܂����Ă�����B";
}
	}
	if($in{'ps_no'}==17){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="����ɂ��Ēm�肽���̂��c�H�@�ǂ��ł��̘b�𕷂����B<br>
����́A�����댯������A�C�e�����B���肷��̂��e�Ղ��႟�Ȃ��B<br>
�Ȃɂ���A�����E�̈����Ɛ��Ȃ���΂Ȃ�Ȃ��񂾂���ȁB<br>
�����E�ւ̓��͂��������݂��邪�c���Ƃ��΁A�����̊فc��������A�����E�̈����ɒ��킷�邱�Ƃ���\�\\���c�B<br>
�����E�̈����Ƃ̐킢�ɏ��Ă�΁A���A�ȑ�����A���򂪓���ł����\�\\��������Ƃ����킯���B<br>
���Ȃ݂ɁA����́A���̂܂܂ł͐l�ԊE�ɂ����Ďg�p���邱�Ƃ��ł��Ȃ��B<br>
�l�ԊE�p�ɒ�������K�v������񂾁B<br>
���̒��ɂ͂���ȋZ�p���������z�͋��Ȃ������񂾂��A�ŋ�<font color=\"red\" size=3>�h���[�����[���h</font>����֗����������ȁB<br>
�ӂ��������O�̓X�����A�h���[�����[���h�͍ł��Z�p�̐i��ł��郏�[���h�B��������Z�p�������Ă���c�炵�����B<br>
�ǂ�Ȗ��򂪂��邩�������悤�B<br>
�܂��́A�I���W�i������̐�\�\\���グ�閂��B<br>
�U���͂��グ��X�^�[�g�b�JA<br>
���������グ��X�^�[�g�b�JH<br>
�������グ��X�^�[�g�b�JS<br>
���ɁA�y�b�g�̔\\��\�l���グ�閂��B<br>
�U���͂��グ��V�F�h�����b�NA<br>
HP���グ��V�F�h�����b�NV<br>
���x�����グ��V�F�h�����b�NP<br>
����ɁA�y�b�g�̍������o���V�F�h�����b�NQ<br>
�Ȃǂ�����B<br>
�����E�ւ̑ϐ��������Ȃ�΁A��苭���A�C�e���������ł��邩������Ȃ��ȁB";
}
	}
	if($in{'ps_no'}==18){
	$ran=int(rand(8));
	if($ran==0){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
����ɁA���̂R���̃m�[�g�͌��E�˔j�����Ă����Ƃ����B<br>
�܂�A�}�e���A����������Ă����\���������Ƃ������ƁB�������������\�\\��\���߂Ă����������ȁB<br>
�܂��A�������ɕ���Ƃ���\��\��\����\�\\��\�͎����Ă��邾�낤���ȁB<br>
�N������������Ȃ̂��B�C�ɂȂ�Ȃ����ˁH";
}
	if($ran==1){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
���̂��ƂȂ̂��낤���c�B�܂��A���݊m�F����Ă���R�̐��E�����݂��Ȃ��������ɈႢ�Ȃ��c�B<br>
���s���Ȃ����E�c�������鐢�E�c�h���[�����[���h�ō��ꂽ�������낤�B<br>
�h���[�����[���h�̌��������Ă���̂̓X�e�B�[�u���Z��ŊԈႢ�Ȃ��B����A���̂ق��ɋ���͂����Ȃ��B<br>
����͒m���Ă���c�B�ނ炩�牽�Ƃ��h���[�����[���h�̌����؂�邱�Ƃ��ł��Ȃ����̂��c�B";
}
	if($ran==2){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
�X�e�B�[�u���Z�킪���������Ă���̂𕷂������Ƃ�����̂��B<br>
�ނ�́A�R���̃m�[�g�����߂Ă���B<br>
���̂R���̃m�[�g��������΁A�I���W�i���E�g�[�}�X���y���|�����Ƃ��o����A�Ƃ��Ӗ��s���Ȃ��Ƃ������Ă����B<br>
�����A���̂R��������΁c���͂ȁc�͂�g�ɂ��邱�Ƃ��ł���悤���ȁB";
}
	if($ran==3){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
�R���̃m�[�g����肷��̂́A�z����₷��قǍ���Ȃ��Ƃ��낤�B�܂��A�����E�ɓ˓����˂΂Ȃ�Ȃ��B<br>
�����͋����B�ǂ����Ă��I���W�i������̋������s�����B<br>
�������A�I���W�i������̋����ɂ́A�e�N�j�b�N������̂��c�B�A���N�h�������`�́c�B<br>
�֘A����͈̂ӊO�ɂ��y�b�g���Ƃ������Ƃ��ȁB���ɁA�������A��̃y�b�g�c�B�����b�����͂����B";
}
	if($ran==4){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
���̋�Ԃ��c�B<br>
�������œ��肵������A��������͕̂��̓w�͂���ς܂Ȃ����c�B<br>
������������A���낦��΁A�������y�ɂȂ�B<br>
<font color=\"red\">�}�e���A���A���ł��邩</font>�A���̍��{��m���Ă���΁A�C�Â����낤�B<br>";
}
	if($ran==5){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
���̋�Ԃœ��肵���������Ă����̂́A�����債���󂯕t���Ȃ��B<br>
���A���̂R���̃m�[�g�͊��ɁA�����傪���Ȃ����A�����ȔN�����o���Ă��邩��ȁc�b�͕ʂ��B<br>
�����A<font color=\"red\">�m�[�g�͎��Ԃ�m���Ă���</font>�񂾁B";
}
	if($ran==6){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
���Â̐̂���󂯌p����鑶�݁c�B<br>
�b�͕ς�邪�c�B���F�E�ԁE���A�����m�A���݊m�F�����R�̐��E���B<br>
�����炠�鐢�E�Ȃ񂾂낤�ȁH<br>
�����āA�������݂��������̂Ȃ񂾂낤�ȁH<br>
<font color=\"red\">�ǂ̐��E�ɂ������Ȃ�����</font>���Ă����̂�������āA�m���Ă邩�H";
}
	if($ran==7){
$jyouhou="�����E�ɑ��݂���ƌ����鈫���̃m�[�g�R���c�B<br>
����́A���Â̐̂ɖ��̋�Ԃ�����ꂽ���킾�����������c�B<br>
�����̎g����́A�g�[�}�X�Ƃ������������������B�M�ߐ��̂Ȃ����ł��܂Ȃ����ȁc�B<br>
�g�[�}�X�ƌ����΁A���Ƃ��Ƃ��̐��E�̑��݂���Ȃ��񂾂낤�H<br>
�j����Ӗ�����_�̖��O���B<br>
<font color=\"red\">�j��</font>���c�B�ِ��E�ɂ́A�j��̐_�a������Ƃ������c�܁A�֌W�Ȃ��ȁB";
}
	}
	if($in{'ps_no'}==19){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="���̋�ԂƂ����̂́B���̐��E�̂ǂ���T���Ă��Ȃ��̂���B<br>
���j�͕ς��Ȃ��B�����𒴂���Ƃ���������V�g�Ȃ�ʂ����c�B<br>
���́A���ɋA���B�y�b�g�̍����A���̖`���҂����̓y�b�g��i��������A�C�e�����x�ɂ����v���ĂȂ����c<br>
��͂�A�������ɋA���ׂ����́B<br>
���������킯�ŁA���̎g�����ɍ�������A���ɋA�����Ă�����Ɨǂ����낤�B<br>
���ʂ̃y�b�g�͂��̐��E�ɑ����Ă��܂��Ă��邪�c���Ɗ֌W�������̂��P�C�A�����͂����B<br>
���̂Ƃ��́A�����ЂƂ̖������A���Ȃ킿�N�̃I���W�i������������Ă��邱�Ƃ����������B";
}
	}
	if($in{'ps_no'}==20){
	$ran=int(rand(4));
	if($ran<3){
$jyouhou="���������@�c���̖����M�K�u���C�N�B<br>
���̎g����́A���E�ł��L�����B<br>
���̖��@�́A�S�Ă��󂷖��@�B���̈З͎͂����@���e�I�Ɠ����A���邢�͂���ȏ�ł���ƌ����B<br>
���̖��@�́A�N�ł��g����B�������A�󂷂��Ƃ����ӂł���Ȃ�΁B<br>
���̖��@�́A�g��������ōX�ɋ��͂ɂȂ�\��\�\\��\���߂Ă���B<br>
�������A���݂�j�󂵂悤�Ȃ�āA�傻�ꂽ���Ƃ��l����񂶂�Ȃ����B";
}
	if($ran==3){
$jyouhou="���������@�̏C�����B<br>
����͑�ϖʓ|���낤�B�Œ�1000���c����2000���͗~�������c�B<br>
���ɏh��p���[���W�߂�̂́A�e�Ղł͂Ȃ�����ȁB<br>
�Ƃ���ŁA���̖��@�ɂ͂P�̒����ƁA�P�̓���Ȏg����������B<br>
���̓���Ȏg����������ƁA���܂ɔ��ɍ����U���͂𔭊�����B<br>
�ÃA�r���e�B���֌W���Ă���Ƃ������Ƃ����c���ʂȐ킢�œ��ɗL�����B<br>";
}
	}
	if($in{'ps_no'}==21){
	$ran=int(rand(6));
	if($ran==0){
$jyouhou="�����@�t�@�C�K�́A�U���͂��グ�鍕���@�����B<br>
�ԐF�̃m�[�g��}���g�𑕔����邱�ƂŁA�X�ɍU���͂̏㏸�����邱�Ƃ��ł��邼�B<br>
�ȂɁA�����炻��ȏ��v��Ȃ����āI�H�@�܂����������Ȃ�c�B";
}
	if($ran==1){
$jyouhou="�����@�u���U�K�́A�G�̍U���͂������鍕���@�����B<br>
�F�̃m�[�g��}���g�𑕔����邱�ƂŁA���g�̍U���͂��㏸�����邱�Ƃ��ł��邼�B<br>
�ȂɁA�����炻��ȏ��v��Ȃ����āI�H�@�܂����������Ȃ�c�B";
}
	if($ran==2){
$jyouhou="�����@�T���_�K�́A�����͂��グ�鍕���@�����B<br>
���F�̃m�[�g��}���g�𑕔����邱�ƂŁA���g�̍U���͂��㏸�����邱�Ƃ��ł��邼�B<br>
�ȂɁA�����炻��ȏ��v��Ȃ����āI�H�@�܂����������Ȃ�c�B";
}
	if($ran==3){
$jyouhou="�����@�G�A���K�́A�G�̉���������鍕���@�����B<br>
�ȂɁA����ȍ����@�A�X�ɂ͔����ĂȂ����āI�H<br>
���̒ʂ�B���̖��@�͔����A�����Đ��䂪���ɍ���Ȃ񂾁B<br>
���ׂ̈ɁA�����������鑕���A����������鑕�������邪�c<br>
�Œ�ł������������鑕���������Ă��Ȃ��Ƃ����Ȃ�����ȁA�X�Ŕ����Ă��N������Ȃ��̂��B";
}
	if($ran==4){
$jyouhou="�����@�G�A���K�̔����ɕK�v�ȑ����Ƃ́B<br>
�����́A�X�J�C�X�s�A�ƁA�X�J�C�A�N�X������������Ί������B<br>
�K�v�ȍ����΂���������ȁA����������񂾂��ȁB";
}
	if($ran==5){
$jyouhou="�����@�G�A���K�̐���ɕK�v�ȑ����Ƃ́B<br>
�����́A�܂��A���荢��B<br>
�`���𑱂��Ă���΁A�����킩�邾�낤�c�B";
}
	}
	if($in{'ps_no'}==22){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="�`���C�i�Ƃ����V���E�������Ƃ����l�Ԃ�����񂾁B<br>
�܂�����Ȃ��Ƒ��ł͕��������ƂȂ����A�ǂ����K�Z�l�^���낤�Ǝv���񂾂��ˁA�����[�������H<br>
���ɂ��ƁA���̒n�ɋ���l�����͊F�A���ꂼ��̎��y�b�g�������Ă�����������B<br>
�����A�y�b�g�̐S�𗝉��������ʁA���������`��҂ݏo�����l����������炵���c�B���̉��`�����m��񂪁c�B<br>
�Ȃ�ł��A�����̉��`���C������ׂɂ́A�Ƃ�ł��Ȃ��`�o���K�v���Ƃ��B<br>
�`�o���グ����@�͂��������͖������c�Ⴆ�΁A�`�o���グ�邱�Ƃ��ړI�Ȃ�100��]���𗘗p����Ɨǂ������ȁc�B";
}
	}
	if(int(rand(100))==0 and $chara[135]>2){
$jyouhou.="<font size=5 color=\"red\"><b><br><br>���������I���������v���o�����I<br>
����̏��Ƃ͊֌W�Ȃ��񂾂��A�����̏�񂪂���񂾁I<br>
\�\\��\�����m�ɂ��ĂȂ񂾂���B<br>
�P�O�O�O���̔�p�ł����Đ��`�̌��𐬒�������̂����炵�����I<br>
�������s���ĉ�ꂿ�܂�����V���b�N����Ȃ��c�I<br>
���������A���̏��̓A���^�����狳�����񂾂��H<br>
���̐l�ɂƂ��Ă͈Ӗ����Ȃ��Ȃ����Ƃ�����ȁI�I</b></font>";
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>��񉮂̃}�X�^�[</B><BR>
�u���x����`�I�ł́A�����悤�I<br>
$jyouhou
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub mem_sts {

	&chara_load;

	&chara_check;

	open(IN,"alldata.cgi");
	@member_data = <IN>;
	close(IN);
	$i=1;$hit=0;
	foreach(@member_data){
		@mem = split(/<>/);
		if($mem[4] eq $in{'taisyo'}){$hit=1;last;}
		$i++;
	}
	if($hit!=1){&error("����ȃL����������܂���");}
	open(IN,"./item/$mem[0].cgi");
	$mitem_log = <IN>;
	close(IN);
	@mitem = split(/<>/,$mitem_log);

	if ($mem[5]) { $esex = "�j"; } else { $esex = "��"; }
	if($mem[70]!=1){$next_ex = $mem[18] * ($lv_up + $mem[37] * 150 - $mem[32] * 50);}
	else{$next_ex = $mem[18] * ($lv_up * 10 - $mem[32] * 50) * 10;}

	# ��{�l�Z�o
	$divpm = int($memmaxpm / 100);
$hit_ritu = int($mem[9] / 3 + $mem[11] / 10 + $mitem[10] / 3) + 40 + $mitem[2] + $mitem[16];
$sake = int($mem[9] / 10 + $mem[11] / 20 + $mitem[10]/10) + $mitem[5] + $mitem[17];
$waza_ritu = int(($mem[11] / 10)) + 10 + $a_wazaup;
if($waza_ritu > 90){$waza_ritu = 90;}
$hissatu_ritu = $waza_ritu + int($mem[12]/4);

	if($mitem[20]){$bukilv="+ $mitem[20]";}
	if($mitem[22]){$bogulv="+ $mitem[22]";}
	if($mem[64]==0 and $mem[65]==0){$mem[64]=50;$mem[65]=50;}

	if($mem[0] eq "jupiter"){
		$mitem[0] = "????";
		$mitem[1] = "????";
		$mitem[3] = "????";
		$mitem[4] = "????";
		$mitem[6] = "????";
		$hit_ritu = "????";
		$sake = "????";
	}

	&header;

	print <<"EOM";
<table align="center"><TR><TD><font size=5>$mem[4]����̃X�e�[�^�X���</font></TD><TD>
</TD></table>
<hr size=0>
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td></tr>
<td rowspan="7" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$mem[6]]">
<tr><td id="td2" class="b2">����</td><td align="right" class="b2">$mitem[0] $bukilv</td>
<td id="td2" class="b1">�U����</td><td align="right" class="b2">$mitem[1]</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="right" class="b2">$mitem[3] $bogulv</td>
<td id="td2" class="b1">�h���</td><td align="right" class="b2">$mitem[4]</td></tr>
<tr><td id="td2" class="b2">�A�N�Z�T���[</td><td align="right" class="b2">$mitem[6]</td>
<td id="td2" class="b1">�A�풆�A����</td><td align="right" class="b2">$mem[20]</td></tr>
<tr>
<td id="td2" class="b2">���݂̐��E</td><td align="center" class="b2">
EOM
if($mem[140]==2){print "�C�G���[���[���h</td>";}
elsif($mem[140]==3){print "���b�h���[���h</td>";}
elsif($mem[140]==4){print "�h���S�����[���h</td>";}
elsif($mem[140]==5){print "�V�E</td>";}
else{print "�W���s�^���[���h</td>";}
print "<td id=\"td2\" class=\"b2\">��</td><td align=\"center\" class=\"b2\">";
if($mem[131]){print "�C�G���[���[���h<br>";}
if($mem[132]){print "���b�h���[���h<br>";}
if($mem[133]){print "�h���S�����[���h<br>";}
if($mem[315]){print "�V�E<br>";}
	print <<"EOM";
</td></table>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">�y�b�g�f�[�^</td></tr>
<td rowspan="7" align="center" valign=bottom class="b2"><img src="$img_path_pet/$egg_img[$mem[45]]">
<tr><td id="td2" class="b2">��</td><td align="center" class="b2">$mem[39]</td>
<td id="td2" class="b2">���O</td><td align="center" class="b2">$mem[138]</td>
</tr>
<tr>
<td id="td2" class="b2">HP</td><td align="center" class="b2">$mem[42]\/$mem[43]</td>
<td id="td2" class="b2">�U����</td><td align="center" class="b2">$mem[44]</td>
</tr>
<tr>
<td id="td2" class="b2">�y�b�g���x��</td><td align="center" class="b2">$mem[46]</td>
<td id="td2" class="b2">�y�b�g�o���l</td><td align="center" class="b2">$mem[40]\/$mem[41]</td>
</tr>
</td>
</tr></table></td>

<table width='50%'>
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr>
<td class="b1" id="td2">�Ȃ܂�</td><td class="b2">$mem[4]</td>
<td class="b1" id="td2">����</td><td class="b2">$esex</td></tr>
<tr><td class="b1" id="td2">�P�Ǔx</td><td class="b2">$mem[64]</td>
<td id="td2" class="b1">���l�x</td><td class="b2"><b>$mem[65]</b></td></tr>
<tr><td class="b1" id="td2">�W���u</td><td class="b2">$mem_syoku[$mem[14]]</td>
<td id="td2" class="b1">�W���uLV</td><td class="b2"><b>$mem[33]</b></td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$mem[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$mem[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$mem[15]\/$mem[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$mem[19]</td></tr>
<tr><td class="b1" id="td2">STR</td><td align="left" class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$mem[7] + $mitem[8]</b></td>
<td class="b1" id="td2">INT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$mem[8] + $mitem[9]</b></td></tr>
<tr><td class="b1" id="td2">DEX</td><td align="left" class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$mem[9] + $mitem[10]</b></td>
<td class="b1" id="td2">VIT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$mem[10] + $mitem[11]</b></td></tr>
<tr><td class="b1" id="td2">LUK</td><td align="left" class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$mem[11] + $mitem[12]</b></td>
<td class="b1" id="td2">EGO</td><td align="left" class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$mem[12] + $mitem[13]</b></td></tr>
<tr><td id="td2" class="b2">������</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu</b></td>
<td id="td2" class="b2">���</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$sake</b></td></tr>
<tr>
<td id="td2" class="b2">��S��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $mitem[17]%</b></td>
<td id="td2" class="b2">�K�E��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhissatu height=$bh><br><b>$hissatu_ritu + $mitem[17]%</b></td></tr>
<tr>
<td id="td2" class="b2">�̍�</td><td align="left" class="b2"><font color="$yellow">$shogo[$mem[32]]</font></td>
<td id="td2" class="b2">�M���h</td><td align="left" class="b2">$mem[66]</td>
</tr>
<tr>
<td id="td2" class="b2">�]����</td><td align="left" class="b2">$mem[37]</td>
<td id="td2" class="b2">���x������</td><td align="left" class="b2">$i��</td>
</tr>
</table>
</table>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}