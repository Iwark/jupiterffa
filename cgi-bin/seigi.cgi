#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

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
<form action="seigi.cgi" >
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

	&item_load;

	&header;
	if($chara[315]==1){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h�����̃y�b�g</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u�V�E�ł̏C�s�͏������H<br>
���͂ȁA�����ŋߏC�s���Ă�̂��B�V�E�łȁc�B<br>
�v
</FONT>
EOM
	}elsif($chara[304]==4){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h�����̃y�b�g</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u�҂��Ă���$chara[4]�I�I<br>
�A���N�h�����͏d�ǂ��B�P��ꂽ���ɋ��낵���Í����@���������Ă��āA�񕜂��ł���B<br>
�A���N�h�����ɏP���|���������m�ɂ͉�������Ƃ�����B�����E�E���q���B<br>
���̎��E�E�E<br>
�����@�ɂ���āA�A���N�h�����͉��q�Ƌ��ɁA�ˑR�����Ɍ��ꂽ�B<br>
�܂����̌��<font size=5><b>����</b></font>���q�����ނ����񂾂��ȁB<br>
�������ǂ������m���Ă邾��B���̒n��ł͈����E�ƍł������ꏊ�ɂ���̂��B<br>
�����Ȃ�̃t�B�[���h�̌��ςɂ��Ă���Ȃ��������q����<font size=5><b>���E����</b></font>�Ȃ�A���̏������B<br>
$chara[4]�Ƃ̓�l������Ȃ�A���q��|�����Ƃ���ł�����������Ȃ��B<br>
�E�E�E�Ƃ͌����Ă��A��x�������@�ɂ����鈫���ł͂Ȃ��B���c�͓�x�ƃR�R�ɂ͗��Ȃ����낤�B<br>
�����ł��A���ꂩ��$chara[4]�́A�V�E�ɍs���A�z����|���͂𓾂Ȃ���΂Ȃ�Ȃ��B<br>
�����ƓV�E�ł́A�����E�ŉ��q�A���邢�͈����E�������|���p����ɓ������͂����B<br>
�R�̃m�[�g������΁A�V�E�ւ̌������̂͗e�Ղ��B
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kagi>
<input type=submit class=btn value="�V�E�ւ̌������">
</form>
�v
</FONT>
EOM
	}elsif($chara[304]==5){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h�����̃y�b�g</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u�҂��Ă���$chara[4]�I�I<br>
�A���N�h�����ɕs�ӑł����d�|�����炵������˂����I���ɉ��ƈꏏ�ɐ��E�������Ă��Ƃ��H<br>
�����c�O�������ȁI�A���N�h�����͊��ɑS�����Ă��邺�B<br>
���̎��E�E�E<br>
�����@�ɂ���Ă����֔��ł����A���N�h�����́A�������܃q�[���K�łg�o��S���������̂��B<br>
�������͖������B<br>
�A���N�h�����͑S���{���Ă��Ȃ��悤���������ȁB<br>
�ނ���A���N�h�����́A$chara[4]�Ɏ~�߂��ėǂ������ƍl���Ă���悤�������B<br>
�A���N�h�����́c�����B�̗͗ʂ��A�\�񕪂ɕ]�����Ă�������ł��A�܂��Â����Ă����ƌ����Ă����B<br>
���͓V�E�֍s���A�X�Ȃ�C�s�����Ă���B<br>
���ꂩ��$chara[4]���V�E�֍s���A�����B��|���͂𓾂Ȃ���΂Ȃ�Ȃ��B<br>
�V�E�ł̏C�s�́A�����E�̍Ő[���ɋ���Ƃ����A�����E����|���ׂɕK�{���낤�B<br>
�R�̃m�[�g������΁A�V�E�ւ̌������̂͗e�Ղ��B
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kagi>
<input type=submit class=btn value="�V�E�ւ̌������">
</form>
�v
</FONT>
EOM
	}elsif($chara[128]==5){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h�����̃y�b�g</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u�܂��A����΂��B�v
</FONT>
EOM
	}elsif($chara[128]==4){
		if($item[1]>=9999 or $item[2]>=9999){
		if($chara[24]==1400){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h�����̃y�b�g</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u$chara[4]���A����͐��b�ɂȂ����ȁB<br>
�A���N�h��������`���𗊂܂�Ă���B���̌��t��`���悤�B<br>
<font color="yellow">
�{���͒��ړ`�����������̂����A�������Ă��܂����B�����炭���͍��A�����E�ɋ��邱�Ƃ��낤�B<br>
$chara[4]�A�N�̕��킪�V���Ȓi�K�ɒB���悤�Ƃ��Ă��邱�Ƃ𕷂����B����ɂ��ē`���Ă����˂΂Ȃ�Ȃ��B<br>
���̋�Ԃœ��肵������A���̐^�����̓}�e���A��Z�����Ƃ��ł���Ƃ������Ƃɂ���B<br>
�}�e���A�Ƃ́A�����B�̍��̂��Ƃł���B�����̍����h��������́A���낵���З͂������ƂɂȂ�B<br>
���A���̕���̓}�e���A��Z�������������������Ă����Ԃ��B<br>
���������c�K�v�Ȃ̂́A�S�̌^��I�сA�����i�������邱�Ƃ��B<br>
�S�̌^�ɂ��Ă͏�񉮂ŕ��������Ƃ��낤�B����A�N���Ȃ����E�ƂɑΉ������^�ɐi�����邱�ƂɂȂ�B<br>
�����ŐV���ɖ��O�����Ȃ����A�i��������̂��B�������E�Ƃ��ς������Ȃ����ꍇ�A�����Ń`�F���W���邱�Ƃ��o����B<br>
�������A�Q���ӂ��K�v���B�܂��A�O�̐E�ƂŏK�������A�r���e�B�͎����Ă��܂����B<br>
���ꂩ��A�O���������̔g����������Ԃ̂��߁A�E�Ƃ�I�Ԃ��Ƃ͏o���Ȃ��B�S�̂����A�����_���ɂȂ��Ă��܂����B<br>
��x�����i����������A�E�ƃ`�F���W�͍���ɂȂ邾�낤�B�����������獡�����X�g�`�����X��������Ȃ��B<br>
�^��ς���̂́c����ȃ}�e���A����肷�邱�Ƃ��ł���Ώo���邩������Ȃ����c����ƌ����Ă������B<br>
�����i����������́A���̌��ň�����|���A�}�e���A����肷�邱�Ƃ��o����悤�ɂȂ�B<br>
����A���m�ɂ̓}�e���A�̌��ƂȂ錳�f�A���ȁB<br>
�����}�e���A�����Z�p�̎��i�͎����Ă���̂����c�A�܂��A�֗����Ő������ĖႤ�Ɨǂ����낤�B<br>
�}�e���A�ɂ͑Ή�����^������B�܂����̕ӂ̂��Ƃ́A�֗����ŕ����Ă���B<br>
</font>�v
</FONT>
<hr size=0>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=change>
<input type=submit class=btn value="�E�ƃ`�F���W�I�I">
</form>
<br>����ɐV���Ȗ��O�����邱�Ƃ��ł��܂��B<br>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=buki2>
<input type="text" name="bname" value="" size=40>
<input type=submit class=btn value="�����i��������">
</form>
EOM
		}
		}else{
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u�����܂����Ȃ����ȁB��͎����ŕ���𐬒������Ă����̂��B�v
</FONT>
<hr size=0>
EOM
		}
	}elsif($chara[128]==3){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u$chara[4]���E�E�E�B���̏C�s�͏��������A����̒��q�͂ǂ����H<br>
EOM
if($chara[24]==1400){
	if($item[1]<1000 and $item[2]<1000){
	print <<"EOM";
�E�E�E�_�����ȁB�܂��A�����̊ق̑���ɂ͎��������Ȃ��̂��H<br>
�������̑���ŋ�킵�Ă���悤�ł͈����E�ւ̐i���ȂǕs\��\�\\�����B<br>
�悵�A�����ɂł͂Ȃ����c�P���P�x�܂łȂ�A�N�̕���̏C�s����`�����ł͂Ȃ����B�v<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=syugyou>
<input type=hidden name=item value=1>
<input type=submit class=btn value="�U���͂�b���Ă��炤">
</form>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=syugyou>
<input type=hidden name=item value=2>
<input type=submit class=btn value="�����͂�b���Ă��炤">
</form>
EOM
	}elsif($item[1]>3000 and $item[2]>3000){
	print <<"EOM";
�E�E�E�ق��A�ƂĂ��ǂ�����ɂȂ��Ă��Ă���ł͂Ȃ����B<br>
���̕�������g�����Ȃ�������ΐV�����W���u�ɂȂ�Ɨǂ����낤�B<br>
�ǂ����A���V�ɂȂ�C�͂��邩�H�v<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=54>
<input type=submit class=btn value="���V�ɂȂ�">
</form>
EOM
	}elsif($item[1]>1000 and $item[2]>1000){
	print <<"EOM";
�E�E�E�ق��A���\�����X�オ���Ă��Ă���悤���ȁB<br>
���̕�������g�����Ȃ�������ΐV�����W���u�ɂȂ�Ɨǂ����낤�B<br>
�ǂ����A���C���ɂȂ�C�͂��邩�H�v<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=53>
<input type=submit class=btn value="���C��">
</form>
EOM
	}elsif($item[1]>1000 and $item[2]<1000){
	print <<"EOM";
�E�E�E�ق��A�U���͂����X�オ���Ă��Ă���悤���ȁB<br>
���̕�������g�����Ȃ�������ΐV�����W���u�ɂȂ�Ɨǂ����낤�B<br>
�ǂ����A�单�V�ɂȂ�C�͂��邩�H�v<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=51>
<input type=submit class=btn value="�单�V�ɂȂ�">
</form>
EOM
	}elsif($item[1]<1000 and $item[2]>1000){
	print <<"EOM";
�E�E�E�ق��A�����͂����X�オ���Ă��Ă���悤���ȁB<br>
���̕�������g�����Ȃ�������ΐV�����W���u�ɂȂ�Ɨǂ����낤�B<br>
�ǂ����A�����ɂȂ�C�͂��邩�H�v<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=52>
<input type=submit class=btn value="�����ɂȂ�">
</form>
EOM
	}
}else{
	print <<"EOM";
�����Ɏ����Ă�����A���Ă�邼�B�v
EOM
}
	print <<"EOM";
</FONT>
<hr size=0>
EOM
	}elsif($chara[128]==2){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u��͂�A�z�͋��G�������ȁB�����炭�A���̎���l�ł͏��ĂȂ��������낤�B<br>
�����܂��܂��C�s������Ȃ��ȁc�B<br>
���ꂩ��A���͉��߂ďC�s�����Ȃ����A�����E�ɓ˓�������肾�B<br>
$chara[4]���A�����Ƃ��̂��肾�낤�B<br>
�E�E�E�A���̕���������Ă����B�����E�Ő키�̂ɂ́A��������l�ԊE�̑����ł͕s\�\\�����B<br>
�����ɐ��`�̌��Ƃ����ǂ��A����͓������ƁB<br>
���̕���́A�w���̋�ԁx�Ƃ����ꏊ�œ��肵���A���̐��E�ɒa�������΂���̕��킾�B<br>
���O���܂��Ȃ����A�U���͂��P�����A���̉�\�\\���͖������B<br>
�����̊قŃ}�e���A����肵�A������p�̍ŋ��̕������肠����Ɨǂ����낤�B�v
</FONT>
<hr size=0>
<br>����ɖ��O�����Ă��������B<br>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=buki>
<input type="text" name="bname" value="" size=40>
<input type=submit class=btn value="�󂯎��">
</form>
EOM
	}elsif($chara[128]==1 or $chara[0] eq "jupiter"){
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>���`�̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
�u�悤�������`�̊قցB<br>
��R��喂���Ƃ̌���̕���ֈē��������܂��傤�B�v
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sandai>
<input type=submit class=btn value="��낵���B">
</form>
EOM
	}else{
	print <<"EOM";
<h1>���`�̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>���`�̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
�u�悤�������`�̊قցB<br>
���Ȃ����A��R��喂���ɏ��Ă邩�ǂ����e�X�g�������܂��傤�B<br>
���ɏ����Ƃ��o������A��R��喂���Ƃ̌���̕���ֈē��������܂��傤�B�v
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sbattle>
<input type=submit class=btn value="���킷��">
</form>
EOM
	}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub sbattle {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&item_load;

	$khp_flg = $chara[15];

	$mhp_flg = 30000000;

	$i=1;
	$j=0;
	@battle_date=();

	while($i<=$turn) {

		&shokika;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;

	}

	&sentoukeka;
	
	&hp_after;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><br><B>�o�g���I</B></FONT>
EOM
	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}
sub shokika {
	if($item[0] eq "���`�̌�"){$dmg = int(rand($chara[18]*3000));}
	else{$dmg = 1;}
	if($item[3] eq "���`�̃}���g"){$mdmg = int(rand($chara[16]/4));}
	else{$mdmg=int(rand($chara[16]*2));}
	$com = "";
	$mcom = "���`�̎g�҂��P�����������I�I";
	if($item[0] ne "���`�̌�"){
		$mcom.= "<br><font size=\"5\" color=\"yellow\">���`�̌��ȊO�Ŏ��������邱�ƂȂǂł��Ȃ���</font>"
	}
	if($item[3] ne "���`�̃}���g"){
		$mcom.= "<br><font size=\"5\" color=\"yellow\">���`�̃}���g���Ȃ��Ɏ��̍U���͖h���Ȃ���</font><br>"
	}
}
sub hp_sum {

	if($khp_flg<1){$dmg = 0;}
	if($mhp_flg<1){$mdmg = 0;}

	$khp_flg = $khp_flg - $mdmg;
	$mhp_flg = $mhp_flg - $dmg;

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mhp_flg > 30000000){
		$mhp_flg = 30000000;
	}
}
sub winlose {
	if ($mhp_flg<=0){ 
		$win = 1; last; #����
	}elsif ($khp_flg<1) {
		$win = 4; last; #����
	}else{ $win = 2; } #��������
}
sub monsbattle_sts {

	$battle_date[$j] = <<"EOM";
	<TABLE BORDER=0 align="center">
	<TR>
	<TD COLSPAN= "3" ALIGN= "center">
	$i�^�[��
	</TD>
	</TR>
EOM
	if ($i == 1) {
		$battle_date[$j] .= <<"EOM";
		<TD>
EOM
		if($khp_flg>=0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$chara[6]]">
EOM
		}
		$battle_date[$j] .= <<"EOM";
		</TD><TD></TD><TD></TD><TD>
EOM
		if($mhp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[116]">
EOM
		}
	}
	$battle_date[$j] .= <<"EOM";
	</TD>
	<TR><TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	�Ȃ܂�	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	�E��	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($khp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$chara[4]		</TD>
		<TD class= "b2">	$khp_flg\/$chara[16]	</TD>
		<TD class= "b2">	$chara_syoku[$chara[14]]</TD>
		<TD class= "b2">	$chara[18]		</TD></TR>
EOM
	}
	$battle_date[$j] .= <<"EOM";
	</TABLE></TD><TD></TD><TD><FONT SIZE=5 COLOR= "#9999DD">VS</FONT></TD>
	<TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	�Ȃ܂�	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	�E��	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($mhp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	���`�̎g��		</TD>
		<TD class= "b2">	$mhp_flg\/30000000	</TD>
		<TD class= "b2">	�����X�^�[		</TD>
		<TD class= "b2">	120			</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]�̍U���I�I</td></tr>
EOM
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com ���`�̎g�� �� <font class= "yellow">$dmg</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">���`�̎g�҂̍U���I�I</td></tr>
EOM
	if($mhp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$mcom $chara[4] �� <font class= "yellow">$mdmg</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
	$battle_date[$j] .= "</table>";
}
sub sentoukeka{
	if ($win==1) {
		$chara[22] += 1;
 		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I</font></b><br>";
	} elsif ($win==2) {
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
	if($chara[36]==1){
		if(!$lvup or $chara[38]>3000){
			if($chara[19]>=int($yado_dai*$chara[18])){
				$chara[15] = $chara[16];
				$chara[42] = $chara[43];
				$chara[19] -=int($yado_dai*$chara[18]);
				print "<b><font size=2>$chara[4]�́A�h���ɍs�����B</font></b><br>";
			}else{
	print "<b><font size=2>$chara[4]�́A�h���ɍs�����Ƃ���������������Ȃ������B</font></b><br>";
			}
		}
	}
	&chara_regist;
}
sub hp_after{
	$chara[15] = $khp_flg;
	if ($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	if ($chara[15] <= 0) { $chara[15] = 1; }
}

#----------------------#
# �퓬��̃t�b�^�[���� #
#----------------------#
sub mons_footer{
	if($win==3){
		print "$comment (��)<br>\n";
	} elsif($win==1){
		print "$comment <br>\n";
	print <<"EOM";
<B>���`�̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
�u���܂��ˁI�I<br>
���Ȃ��Ȃ�A��R��喂���ɏ��Ă��\�\\��������܂��B<br>
�t���Ă��Ă��������B�v
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=win>
<input type=submit class=btn value="���Ă���">
</form>
EOM
	} elsif($win==2){
		print "$comment <br>\n";
	} else {
		print "$comment (��)<br>\n";
	}

	print <<"EOM";
<form action="$script">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}
sub win{

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}
	&header;
	if($chara[128]!=1){
		$chara[128]=1;
		$i_no="0047";
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $i_no){last;}
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	print <<"EOM";
<B>���`�̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
�u����H���Ȃ��A<b>���`�̃A�N�Z�T���[</b>���������łȂ���ł��ˁB����������܂��傤�B<br>
����������A������x���Ă��������B�v
</FONT>
<hr size=0>
<br>
EOM
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');

	&shopfooter;

	&footer;

	exit;
}

sub sandai {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>����̕���</h1>
<hr size=0>
<FONT SIZE=3>
<B>��R��喂��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
�u�ނ��B�M�l�́I�I�����Ă����̂��I�A���N�h�����I<br>
�������̂ӂ������i�D�́c�B�ǂ�����Ă����֗����I�H�v<br><br>
<B>���`�̎g�ҁ@���߁@�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br><br>
�u���͂⏉��喂���A��Q��喂���ł���A�l�ԊE�̋��ҒB�̊Ԃł͈����C�̎G�������c�B<br>
�����܂ł̓��̂�ɋ����҂Ȃǈ�C�����Ȃ�������B<br>
�������A�M�l�����͖��f�Ȃ��B�����E�Ɖ����_�������ł�������������ȁB<br>
�����Łc�A����͏����l��A��Ă����B�u�l�ԊE�̋��ҁv���B<br>
$chara[4]�A�܂����ȏЉ�����Ă��Ȃ������ȁB<br>
���̓A���N�h�����B���̎p�́A���`�̊قł̉��̎p�c�B<br>
�������A�^�̗͂�������A�z�Ɛ킨���B<br>
���͂��Ă���I�v
</FONT>
<hr size=0>
<br>
<form action="./maoubattle.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=maou>
<input type=submit class=btn value="�키">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

sub buki{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'bname'} eq ""){
		&error("����ɖ��O�����Ă��������B$back_form");
	}
	if (length($in{'bname'}) > 20) {
		&error("����̖��O���������܂��B$back_form");
	}

	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($i_no == 1400) { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}

	push(@souko_item,"$i_no<>$in{'bname'}<>$i_dmg<>$i_gold<>$ihit<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	$chara[128]=3;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>������p�̕���w$in{'bname'}�x���󂯎�����I</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub change {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
	if($chara[128]==4){
		$lock_file = "$lockfolder/syoku$in{'id'}.lock";
		&lock($lock_file,'SK');
		&syoku_load;
		$syoku_master[51] = 0;
		$syoku_master[52] = 0;
		$syoku_master[53] = 0;
		$syoku_master[54] = 0;
		&syoku_regist;
		&unlock($lock_file,'SK');
		if($chara[51]==71 or $chara[51]==72 or $chara[51]==73 or $chara[51]==74){$chara[51]=0;$chara[13]+=650;}
		if($chara[52]==71 or $chara[52]==72 or $chara[52]==73 or $chara[52]==74){$chara[52]=0;$chara[13]+=650;}
		if($chara[53]==71 or $chara[53]==72 or $chara[53]==73 or $chara[53]==74){$chara[53]=0;$chara[13]+=650;}
		if($chara[54]==71 or $chara[54]==72 or $chara[54]==73 or $chara[54]==74){$chara[54]=0;$chara[13]+=650;}
		$chara[14]=51+int(rand(4));
		$comment="�A���N�h�����̃y�b�g";
	}else{
		$chara[14]=$in{'item'};
		$comment="�A���N�h����";
		$chara[128]=4;
	}

	$chara[33]=1;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l���V�����^�E�ɂȂ�܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$comment</B><BR>
�u���ށc�B�����ɐV���ȐE�ɂȂꂽ�悤���ȁB���ꂩ�������΂�Ȃ����B
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub syugyou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[147]==$mday){&error("�����͂����C�s���܂�����B");}
	else{$chara[147] = $mday;}

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($in{'item'} == 1) {
		$kougeki=int(rand(100));
		$item[1]+=$kougeki;
		$st="����̍U���͂�$kougeki�|�C���g�㏸���܂����B";
	}elsif($in{'item'} == 2){
		$hit=int(rand(100));
		$item[2]+=$hit;
		$st="����̖����͂�$hit�|�C���g�㏸���܂����B";
	}else{
		&error("�G���[�B$back_form");
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
<B>�����A�C�s���������A$st</B><BR>
</font>
<br>
<form action="seigi.cgi" >
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
sub buki2{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&syoku_load;

	if($syoku_master[51]==100){$msyoku=1;}
	elsif($syoku_master[52]==100){$msyoku=2;}
	elsif($syoku_master[53]==100){$msyoku=3;}
	elsif($syoku_master[54]==100){$msyoku=4;}
	else{&error("�K�v�E�Ƃ��}�X�^�[���Ă��Ȃ��󋵂ł��B$back_form");}

	if ($in{'bname'} eq ""){
		&error("����ɖ��O�����Ă��������B$back_form");
	}
	if (length($in{'bname'}) > 20) {
		&error("����̖��O���������܂��B$back_form");
	}

	$item[0] = $in{'bname'};
	$item[28] = $msyoku;
	$item[29] = 1;
	$item[30] = 1;

	$chara[26] = $host;

	$chara[128]=5;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>�V���Ȏ�����p�̕���w$in{'bname'}�x���󂯎�����I</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kagi{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$red=0;$blue=0;$yellow=0;$i=1;
	foreach(@souko_item){
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($iname eq "���b�h�m�[�g"){$red=$i;}
		if($iname eq "�u���[�m�[�g"){$blue=$i;}
		if($iname eq "�C�G���[�m�[�g"){$yellow=$i;}
		$i++;
	}
	if(!$red){&error("���b�h�m�[�g���q�ɂɂ���܂���");}
	elsif(!$blue){&error("�u���[�m�[�g���q�ɂɂ���܂���");}
	elsif(!$yellow){&error("�C�G���[�m�[�g���q�ɂɂ���܂���");}
	else{
		$red-=1;$blue=0;$yellow=0;
		splice(@souko_item,$red,1);
		foreach(@souko_item){
			($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
			if($iname eq "�u���[�m�[�g"){splice(@souko_item,$blue,1);}
			$blue++;
		}
		foreach(@souko_item){
			($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
			if($iname eq "�C�G���[�m�[�g"){splice(@souko_item,$yellow,1);}
			$yellow++;
		}
		$chara[315]=1;
	}
	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red"><br><br>
<B>�V�E�ւ̌���������I�I�I</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub syoku_regist {

	$new_syoku = '';

	for ($s=0;$s<=$chara[14];$s++) {
		if (!$syoku_master[$s]){
			$syoku_master[$s] = 0;
		}
	}

	$new_syoku = join('<>',@syoku_master);

	$new_syoku .= "<>";

	open(OUT,">./syoku/$in{'id'}.cgi");
	print OUT $new_syoku;
	close(OUT);

}