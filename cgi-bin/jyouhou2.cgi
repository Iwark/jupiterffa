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
<form action="jyouhou2.cgi" method="post">
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
<h1>���ver2</h1>
<hr size=0>
<FONT SIZE=3>
<B>��񉮂̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�����ł͊��S��JupiterFFA�̍U����񂪕����邼�B�������A�����p���B<br>
����؂������ė����B����@�H����́A�閧���B<br>
�l�^�o�������ȓz�́A�����Ă���񂶂�Ȃ����B<br>
�����ŕ��������e���A�`���b�g�⑼�̃T�C�g�ȂǂɁA��΂ɘR�炵�Ă͂����Ȃ����B<br>
��������e�́A����؂̃��x���ɉ����ĕς�邼�B�v
</FONT>
<br>���݂̏������F$chara[19] �f
<hr size=0>
EOM
	if ($chara[30] == 1000){print"���Z�@���Z�b�g����Ă��܂��B";}
	if ($chara[30] == 2000){print"���Z�A���Z�b�g����Ă��܂��B";}
	if ($chara[30] == 3000){print"���Z�@�ƇA���Z�b�g����Ă��܂��B";}
	if ($chara[31] == "0015") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="G����������(1000G) : 4��">
		</form><br>
EOM
	}elsif ($chara[31] == "0013") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="F����������(10000G) : 2��">
		</form><br>
EOM
	}elsif ($chara[31] == "0016") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="E����������(30000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0017") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="D����������(50000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0018") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="C����������(100000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0019") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="B����������(300000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0020") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="A����������(500000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0021") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="S����������(1000000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0022") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="SS����������(10000000G) : 1��">
		</form><br>
EOM
	}elsif ($chara[31] == "0030" or $chara[0] eq "jupiter") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=pass>
		<input type=submit class=btn value="�p�X�R�[�h���g�p����B">
		</form><br>
EOM
	}else{
		print <<"EOM";
		����؂�����܂���
EOM
	}
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=sc>
	<input type=submit class=btn value="�X�J�E�^�[ ver2">
	</form>
EOM
if($chara[90]>999){
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=rg>
	<input type=submit class=btn value="���W�X�g">(���W�X�g�l�F$chara[89])
	</form>
EOM
}
if($chara[18]>2000){
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=anjou>
	<input type=submit class=btn value="�H�H�H">
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
sub jyoho_buy {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$aplace0="���������e���B�[�k";$aplace1="���A�����H�X";$aplace2="��Ȃ��̓D��";
	$aplace3="�ŎR���`���������b�c";$aplace4="�_�[�N�E�G���A";$aplace5="�_�̓��G�����@�[�k";
	$aplace6="�X�y�V�����G���[�g";$aplace7="���҂䂭�ꏊ";$aplace8="�C�G���[���[���h";
	$aplace9="���b�h���[���h";$aplace10="�h���S�����[���h";$aplace11="�h���S���w�u��";
	$aplace12="�������̏�";$aplace13="�V�E�ւ̓���";$aplace14="�V�E�̕���";

	if ($chara[31] == "0015"){
		if($chara[19] < 1000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 1000; }
		$jyouhou="��񂻂̂P�F�퓬�͂�1000�̔{���̎��A�o���l���Q�{�ɂȂ�B�����������K�{�B<br>";
		$jyouhou.="��񂻂̂Q�F�����i�𐬒�������ƃ��A�A�C�e���ɂȂ邱�Ƃ������B<br>";
		$jyouhou.="��񂻂̂R�F��ꂽ�����̗݌v�p���[�͍Œ�P�O�O�A�ł���΂T�O�O�͗~�����ȁB<br>";
		$jyouhou.="��񂻂̂S�F�퓬�͂�����v������o���l��{�̂܂܂ɂ�������@������炵���ȁB<br>";
	}
	if ($chara[31] == "0013"){
		if($chara[19] < 10000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 10000; }
		$jyouhou = <<"EOM";
		��񂻂̂P�F��������K��������������@��<br>
		�@�܂��A�����ɂȂ�A�C�e�����W�߂܂��B(�q�ɂ̒��ɁB)<br>
		�A�����̋��Ԃ֍s���A�x���ɑߕ߂���܂��B<br>
		�B���̂܂܂ǂ��ւ��s�����ɁA�q�ɂ֍s���A�v��Ȃ��A�C�e���𔄂�܂��B<br>
		�C���������܂��B�K�������������B�����l�ł����B<br>
		���炩���ߐ�����p���̔��l�����A�C�e���ƁA������Ђ֍s����p���K�v�ɂȂ�܂��B<br>
		���l�ɂȂ��Ă���Ə������₷���Ǝv���܂��B<br><br>
		��񂻂̂Q�F���d������؂̊ȒP����@��<br>
		�@���b�h���[���h�֍s���܂��B<br>
		�A��s����100���f�����o���܂��B<br>
		�B�����i�X�łf������؂��w�����܂��B<br>
		�C�q�ɂ��m�F���܂��B�I���B<br>
EOM
	}
	if ($chara[31] == "0016"){
		if($chara[19] < 30000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 30000; }
		$jyouhou = <<"EOM";
		��񂻂̂P�F���������V�s�m���P��<br>
		�ł̐΁{�ł̐΁��_�[�N�i�C�t�i�����N�Q����j<br>
		�ł̐΁{���������J�I�X�\\�[�h�i�����N�R����j<br>
		�������{�����������̌��i�����N�R����j<br><br>

		��񂻂̂Q�F���������V�s�m���Q�̈ꕔ��<br>
		�����{���������������i�����N�T�h��j<br>
		�����{���҂̏؁��r�������<br>
		�����{�_�[�N�}�^�[�������i�����N�S����j<br>
EOM
	}
	if ($chara[31] == "0017"){
		if($chara[19] < 50000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 50000; }
		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
		$jyouhou = <<"EOM";
		<table>
		<tr><th>���O</th><th>�o���ꏊ</th><th>�퓬��</th></tr><tr>
EOM
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			if($abasyo==5 or $abasyo==6){$jyouhou.="<th>$aname</th><th>${'aplace'.$abasyo}</th><th>$power</th></tr>";}
		}
		$jyouhou.="</table>";
	}
	if ($chara[31] == "0018"){
		if($chara[19] < 100000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 100000; }
		$jyouhou = <<"EOM";
���~�Ŗׂ�����@���c�B�ŉ_�ɐi�񂾂�K���ׂ���Ȃ��悤�ɂł��Ă��邩��ȁc�B<br>
������ɍs��������Ε�V���Ⴆ��Ƃ����A�Â�㩂Ɉ��������鏉�S�҂��{���ɑ����B<br>
�������B���~�Ŗׂ�������΁A�܂��A�S�Ă̕��p�A�������炢�����i�ނ񂾁B<br>
�������ȁA�S�����炢�i�ނƂ������낤�B���̂��ƁA�~�������̂̂�������֐i�ނƂ����B<br>
����ŁA��������N���ׂ����邾�낤�B�N���ɗ��R�𕷂���Ă��A�����Ă���ׂ�񂶂�Ȃ�����<br>
�b���H�債����񖳂�������B���Ȃ��ق���������B�Ƃł������Ă����񂾂�
EOM
	}
	if ($chara[31] == "0019"){
		if($chara[19] < 300000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 300000; }
		$jyouhou = <<"EOM";
�y�b�g���ߊl�ł��邱�Ƃ͒m���Ă��ȁH<br>
�������Ȃ����̕��퉮�Ŕ����Ă�A�C�e���̂����A������������ƁA����ȕ���ɐ���������̂�����B<br>
�����������āA�y�b�g�͎������ɁA�ߊl�ł���G��|���ƁA�����𖞂����Ă���Εߊl���邱�Ƃ��ł���񂾁B<br>
�����āA�ߊl�����y�b�g�́A�����̃��x���܂ŁA���x�����オ��B���O��1000���x���𒴂��Ă���Ȃ�A���E��1000���x�����B<br>
�y�b�g��1000���x���ɂȂ�ƁA���������B���̗p�r�̓y�b�g�ɂ���ĈႤ���A�����y�b�g�Ɏg���ƁA�i�������肷��ȁB<br>
�Ⴆ�΁A�V�^�E�C���X�ɐV�^�E�C���X�̍����g���ƐV�^�E�C���X2�ɐi������B<br>
�I�[�K�Ƀ^�k�L�}���̍����g���ƁA�M�K���g�I�[�N�ɐi������A�Ƃ����悤�ɂ��ȁB<br>
�������A�M�K���g�I�[�N�͏��ՂŒ��Ԃɂ���ׂ��y�b�g�ł͂Ȃ��ȁB<br>
�����͋ɒ[�ɐ������x������A�h�w�K���u�h�ł���ɓ��ꂽ��A���̃y�b�g�ƕ��s���ă��x�����グ���ق����������낤�c�B<br>
��H�w�K���u�H�����ɂ��Ă̏��͂܂����x���ȁB�K�b�n�b�n��<br>
�܂��Ƃ������A�Ȃɂ���z�͐������x���B������萔�{�����h���~�r���h�ł����A����Ȃɒx���Ȃ����c<br>
��H���~�r���H�����ɂ��Ă̏��͂܂����x���ȁB�K�b�n�b�n��<br>
�ŁA���_�Ƃ��āA���̂����߂����ȁB�܂��̓^�k�L�}������ĂĂ����̂��������낤�B<br>
�����x���͕��ʁB�p���[�������̑����̊���Ɍ��\�����B���ƂŃM�K���g�I�[�N����낤�Ƃ������ɍ����K�v�����ȁB<br>
���̒i�K�̓w���n�E���h���ȁB�������������A��ɕK�v�����B�������A�ߊl�̍ۂɂ͏������ɋC������񂾂��B<br>
�������܂��A�y�b�g�ɋ��������߂Ȃ��Ȃ�A�C�ɓ������y�b�g����Ă�Ƃ������B<br>
����̈�ĂĂ��Ȃ��y�b�g����ĂĂ�����A�ӊO�ȓz�ɐi���c�Ȃ�Ă��Ƃ����邾�낤���ȁB<br>
�撣��$chara[4]�B���O���i���o�[�������I(<br>
EOM
	}
	if ($chara[31] == "0020"){
		if($chara[19] < 500000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 500000; }
		$jyouhou="��񂻂̂P�F1000��퓬�͂𑪒肷��ƃ��W�X�g���[�h���o������B";
	}
	if ($chara[31] == "0021"){
		if($chara[19] < 1000000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 1000000; }
		$jyouhou="��񂻂̂P�F�N���e�B�J���R�����g���u���J�e����!!�v�ɂ���ƃN���_��4�{?(�΃����X�^�[�̂�)";
	}
	if ($chara[31] == "0022"){
		if($chara[19] < 10000000) { &error("����������܂���$back_form"); }
		else { $chara[19] = $chara[19] - 10000000; }
		$jyouhou="��񂻂̂P�F�摜�m�����S�U�S�X�ɐݒ肷�邱�ƂŎ擾�o���l��+100��";
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
sub sc {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&item_load;

	$sentou=$chara[8] * 4 + $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10 + $chara[8]/10 + 1);
	$sentou+=int($chara[16]/2) + $item[4] * (4 + int($chara[10]/10+1));
	$sentou+=(int(($chara[11] / 10)) + 10 + int($chara[12]/4))*10;
	$sentou+=(int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16])*10;
	$sentou+=(int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17])*10;
	if($item[0] eq "�f��" or $item[3] eq "���i��"){$sentou+=int(rand(10));}
	$chara[90]+=1;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
#		$jyouhou = <<"EOM";
#		<table>
#		<tr><th>���O</th><th>�o���ꏊ</th><th>�퓬��</th></tr><tr>
#EOM
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			${'asentou'.$abasyo}+=$power;
			${'akazu'.$abasyo}+=1;
#			$jyouhou.="<th>$aname</th><th>${'aplace'.$abasyo}</th><th>$power</th></tr>";
		}
#		$jyouhou.="</table>";

	$aplace0="���������e���B�[�k";$aplace1="���A�����H�X";$aplace2="��Ȃ��̓D��";
	$aplace3="�ŎR���`���������b�c";$aplace4="�_�[�N�E�G���A";$aplace5="�_�̓��G�����@�[�k";
	$aplace6="�X�y�V�����G���[�g";$aplace7="���҂䂭�ꏊ";$aplace8="�C�G���[���[���h";
	$aplace9="���b�h���[���h";$aplace10="�h���S�����[���h";$aplace11="�h���S���w�u��";
	$aplace12="�������̏�";$aplace13="�V�E�ւ̓���";$aplace14="�V�E�̕���";
	$bsentou=0;$csentou=0;$dsentou=0;$esentou=0;$bbasyo="";$cbasyo="";$dbasyo="";$ebasyo="";
	for($as=0;$as<15;$as++){
		if(${'akazu'.$as}){${'asentou'.$as}=int(${'asentou'.$as}/${'akazu'.$as});}
		if(${'asentou'.$as}<$sentou){
			if($bsentou<${'asentou'.$as}){
				$bsentou=${'asentou'.$as};$bbasyo=${'aplace'.$as};
				if($ebasyo){
					$csentou=$esentou;
					$cbasyo=$ebasyo;
				}
				$esentou=${'asentou'.$as};
				$ebasyo=${'aplace'.$as};
			}
		}else{
			if(!$dsentou or $dsentou>${'asentou'.$as}){
				$dsentou=${'asentou'.$as};
				$dbasyo=${'aplace'.$as};
			}
		}
	}
	$jyouhou.="���Ȃ��̐퓬�͂�<font color=\"yellow\">$bbasyo</font>�̃����X�^�[���ł��B<br>";
	$jyouhou.="�G���⒇�Ԃ̋������l�����Ď��M���������<font color=\"yellow\">$cbasyo</font>�A<br>";
	$jyouhou.="���M������Ȃ��<font color=\"yellow\">$dbasyo</font>�ɒ��ނƗǂ��ł��傤�B<br>";

if($chara[0] eq "jupiter"){
		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			$alv=int($power/100)+1;
	$gggg.="$abasyo<>$aname<>$azoku<>$alv<>$amex<>$arand<>$asp<>$admg<>$akahi<>$amonstac<>$amons_ritu<>$agold<>$aimg<><br>";
		}
}
	&header;

	print <<"EOM";
<h1>���Ȃ��̐퓬�͂́A$sentou�ł��B</h1><br>
<h2>$jyouhou</h2>
$gggg
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub rg {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&item_load;

	$sentou=$chara[8] * 4 + $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10 + $chara[8]/10 + 1);
	$sentou+=int($chara[16]/2) + $item[4] * (4 + int($chara[10]/10+1));
	$sentou+=(int(($chara[11] / 10)) + 10 + int($chara[12]/4))*10;
	$sentou+=(int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16])*10;
	$sentou+=(int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17])*10;
	$chara[89]=$sentou;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>���Ȃ��̌��݂̐퓬��$sentou���A���W�X�g���܂����B</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �p�X�R�[�h�@  #
#----------------#
sub pass {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[31] == "0030" or $chara[0] eq "jupiter"){
	$hokaku = <<"EOM";
	<form action="jyouhou2.cgi" method="post">
	<input type=hidden name=id value="$chara[0]">
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=hokaku>
	<input type=submit class=btn value="�ߊl��\�\\�y�b�g">
	</form>
EOM
	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;
	$jyouhou="<table><tr><th>�m���D</th><th>�����</th><th>���e</th><th>�ԓ���</th><th>����</th></tr>";
	foreach(@member_data){
		($no,$q_name,$q_com,$a_name,$a_com) = split(/<>/);
		if($no>$i-60){
			$jyouhou.="	<tr>
			<th>$no</th>
			<th><font size=2.9>$q_name</font></th><th><font size=2.9>�u$q_com�v</font></th>
			<th><font size=2.9>$a_name</font></th><th><font size=2.9>�u$a_com�v</font></th>
			</tr>";
		}
	}
	$jyouhou.="</table>";
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=toukou>
������e�@�F<input type="text" name="com" value="" size=40><br>
<br>�@�@
<input type=submit class=btn value="���₷��">
</form>

EOM
if($chara[0] eq "jupiter"){
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kaitou>
No.:<input type="text" name="no" value="" size=10><br>
�񓚓��e�@�F<input type="text" name="com" value="" size=40><br>
<br>�@�@
<input type=submit class=btn value="�񓚂���">
</form>
EOM
}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>���W���s�^���̉��ł����k���I(�ʖ��@���f����)</B><BR><br>
�u�����ŕ����ƁA(���W���s�^���̋C����������)���ł������Ă����݂�������I<br>
����܂��R�������肷��ƁA���W���s�^���͕ԐM���Ă���Ȃ���I<br>
���ƁA���N��ɕԓ��������肵�Ă�(���Ȃ������Ƃ��Ă�)�{��Ȃ��悤�ɁI<br>
�Ƃ肠�����A�\\�������͍̂ŐV��60���B���O�����͂����ł���悤�ɂ��邩���c<br><br>
�ߊl��\�\\�y�b�g�ɂ��ẮA��$hokaku
$jyouhou
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub toukou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($chara[31] != "0030" and $chara[0] ne "jupiter"){&error("�p�X�R�[�h�����Ă����o�J����$back_form");}
	else{
		if ($in{'com'} eq "") {
			&error("���e����͂��Ȃ��ŉ��𕷂��H$back_form");
		}
	}

	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;$i+=1;

	push(@member_data,"$i<>$chara[4]<>$in{'com'}<><><>\n");

	open(OUT,">passcode.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>����𓊍e���܂����B</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kaitou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($chara[31] != "0030" and $chara[0] ne "jupiter"){&error("�p�X�R�[�h�����Ă����o�J����$back_form");}
	else{
		if ($in{'com'} eq "") {
			&error("���e����͂��Ȃ��ŉ��𕷂��H$back_form");
		}
		if ($in{'no'} eq "") {
			&error("�i���o�[����͂����B$back_form");
		}
	}

	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		($no,$q_name,$q_com,$a_name,$a_com) = split(/<>/);
		if($in{'no'} == $no){
			$member_data[$i]="$no<>$q_name<>$q_com<>$chara[4]<>$in{'com'}<>\n";
			last;
		}
		$i++;
	}

	open(OUT,">passcode.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>����ɉ񓚂��܂����B</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub hokaku {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[31] == "0030" or $chara[0] and "jupiter"){
	open(IN,"hokakukanou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;$no=0;
	$jyouhou="<table><tr><th>�y�b�g��</th><th>�ߊl�ꏊ</th><th>�ߊl���@</th><th>���l</th><th>�y�b�g��</th><th>�ߊl�ꏊ</th><th>�ߊl���@</th><th>���l</th></tr>";
	foreach(@member_data){
		($name,$basyo,$houhou,$bikou) = split(/<>/);
		if($no>$i-100){
			if($no % 2 == 0){$jyouhou.="<tr>";}
			$jyouhou.="	<th><font size=2.9>$name</font></th><th><font size=2.9>$basyo</font></th>
					<th><font size=2.9>$houhou</font></th><th><font size=2.9>$bikou</font></th>";
			if($no % 2 == 1){$jyouhou.="</tr>";}
		}
		$no++;
	}
	$jyouhou.="</table>";
if($chara[0] eq "jupiter"){
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ptoukou>
�y�b�g��:<input type="text" name="name" value="" size=40><br>
�ߊl�ꏊ�@�F<input type="text" name="basyo" value="" size=40><br>
�ߊl���@�@�F<input type="text" name="houhou" value="" size=40><br>
�ߊl���l�@�F<input type="text" name="bikou" value="" size=40><br>
<br>�@�@
<input type=submit class=btn value="���e����">
</form>
EOM
}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>���W���s�^���̉��ł����k���I(�ʖ��@���f����)</B><BR><br>
�u�����ł́A�ߊl�y�b�g�ɂ��āA�������B���͂Ō��������l�͌���񂶂�Ȃ����B<br>
�Ƃ肠�����A�\\�������͍̂ŐV��100���B���O�����͂����ł���悤�ɂ��邩���c<br><br>
$jyouhou
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub ptoukou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"hokakukanou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		($name,$basyo,$houhou,$bikou) = split(/<>/);
		if($name eq $in{'name'}){
			$hit=1;
			if($in{'basyo'}){$basyo=$in{'basyo'};}
			if($in{'houhou'}){$houhou=$in{'houhou'};}
			if($in{'bikou'}){$bikou=$in{'bikou'};}
			$member_data[$i]="$in{'name'}<>$basyo<>$houhou<>$bikou<>\n";
		}
		$i++;
	}
	if($hit != 1){
		push(@member_data,"$in{'name'}<>$in{'basyo'}<>$in{'houhou'}<>$in{'bikou'}<>\n");
	}

	open(OUT,">hokakukanou.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�y�b�g�ɂ��ē��e���܂����B</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub anjou {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	open(IN,"data/angou.ini");
	$angou = <IN>;
	close(IN);

	$i=0;
	while ($angou =~ /([\x00-\x7f]|..)/g) {
		$angou1[$i]="$1";
		$i++;
	}

	$i=0;
	foreach(@angou1){
		if("$_" eq "��"){$angou1[$i]="a";}if("$_" eq "��"){$angou1[$i]="b";}
		if("$_" eq "��"){$angou1[$i]="c";}if("$_" eq "��"){$angou1[$i]="d";}
		if("$_" eq "��"){$angou1[$i]="e";}if("$_" eq "��"){$angou1[$i]="f";}
		if("$_" eq "��"){$angou1[$i]="g";}if("$_" eq "��"){$angou1[$i]="h";}
		if("$_" eq "��"){$angou1[$i]="i";}if("$_" eq "��"){$angou1[$i]="j";}
		if("$_" eq "��"){$angou1[$i]="k";}if("$_" eq "��"){$angou1[$i]="l";}
		if("$_" eq "��"){$angou1[$i]="m";}if("$_" eq "��"){$angou1[$i]="n";}
		if("$_" eq "��"){$angou1[$i]="o";}if("$_" eq "��"){$angou1[$i]="p";}
		if("$_" eq "��"){$angou1[$i]="q";}if("$_" eq "��"){$angou1[$i]="r";}
		if("$_" eq "��"){$angou1[$i]="s";}if("$_" eq "��"){$angou1[$i]="t";}
		if("$_" eq "��"){$angou1[$i]="u";}if("$_" eq "��"){$angou1[$i]="v";}
		if("$_" eq "��"){$angou1[$i]="w";}if("$_" eq "��"){$angou1[$i]="x";}
		if("$_" eq "��"){$angou1[$i]="y";}if("$_" eq "��"){$angou1[$i]="z";}
		if("$_" eq "��"){$angou1[$i]="A";}if("$_" eq "��"){$angou1[$i]="B";}
		if("$_" eq "��"){$angou1[$i]="C";}if("$_" eq "��"){$angou1[$i]="D";}
		if("$_" eq "��"){$angou1[$i]="E";}if("$_" eq "��"){$angou1[$i]="F";}
		if("$_" eq "��"){$angou1[$i]="G";}if("$_" eq "��"){$angou1[$i]="H";}
		if("$_" eq "��"){$angou1[$i]="I";}if("$_" eq "��"){$angou1[$i]="J";}
		if("$_" eq "��"){$angou1[$i]="K";}if("$_" eq "��"){$angou1[$i]="L";}
		if("$_" eq "��"){$angou1[$i]="M";}if("$_" eq "��"){$angou1[$i]="N";}
		if("$_" eq "��"){$angou1[$i]="O";}if("$_" eq "��"){$angou1[$i]="P";}
		if("$_" eq "��"){$angou1[$i]="Q";}if("$_" eq "��"){$angou1[$i]="R";}
		if("$_" eq "��"){$angou1[$i]="S";}if("$_" eq "��"){$angou1[$i]="T";}
		$i++;
	}
	open(OUT,">data/angou1.ini");
	print OUT @angou1;
	close(OUT);

	&header;

	print <<"EOM";
<h1>@angou1</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}