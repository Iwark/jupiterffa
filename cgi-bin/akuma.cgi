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
<form action="akuma.cgi" >
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

	$test=0;
	if($chara[0] eq "jupiter"){$test=1;}
	$taisei=$chara[135]+1;
	if($taisei>30){$taisei=30;}
	print <<"EOM";
<h1>�����̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�����̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
�u�K�n�n�n�n�n�A�悤���������̊قցI<br>
��������A<font color="red">�y�j���Ɠ��j���̂�</font>�P���P��܂ň����E�ɓ˓��ł��邼�K�n�n�n�I<br>
�n�߂Ɍ����Ă������A�����E�͑ϐ��̖����҂ɂ͂ƂĂ��ς��؂�Ȃ��t�B�[���h���B<br>
�ǂ�Ȃɋ����ł��A�������ƁB���̂��ʂ���<font color="red" size="5">$taisei</font>�^�[�����炢�Ȃ�ς����邾�낤�ȁB<br>
�����B�̎��A�C�e���͐������A�����A�_���ɂ��Ă��o�債�Ē��ނ��Ƃ��ȃK�n�n�n�I<br>
�܂������E�ɒ��킷��O�ɁA�܂��͈����E���V�~�����[�g�����w���z�����E�PF�`�VF�x�őϐ���t����Ɨǂ����낤�B<br>
���z�ƌ����Ă��ꉞ�{���̈����Ȃ񂾂��ȃK�n�n�I�������ڂ�ŁA�}�e���A���f�̓h���b�v�ł��Ȃ����I�K�n�n�I<br>
�Ȃ��A�����E�ɒ���ł���̂͂P�O�b�ɂP��܂łŁA���z�łP����|���Ȃ��悤���ƒ���͔F�߂��Ȃ��ȁB<br>
EOM
if($chara[146]>0){
	print <<"EOM";
<br><font color="red" size=4>���A�����E�`�P�b�g��$chara[146]�������Ă�̂��I����������΁A���ł�����ł��邺�`�K�n�n�n�n�I</font>
EOM
}
if($wday==2){
	print <<"EOM";
<br><font color="red" size=4>�Ηj���͋C�����ǂ��A�`�P�b�g�������Ă����ʂ�10���f�ň����E�ւ̓˓��������悤�K�n�n�n�n�I</font>
EOM
}
	print <<"EOM";
�v
</FONT>
<hr size=0>
<br>

<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=1>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�PF�ɒ��킷��">
</form>
EOM
if($chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=2>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�QF�ɒ��킷��">
</form>
EOM
}
if($chara[135]>=2){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=3>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�RF�ɒ��킷��">
</form>
EOM
}
if($chara[135]>=3){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=4>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�SF�ɒ��킷��">
</form>
EOM
}
if($chara[135]>=4){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=5>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�TF�ɒ��킷��">
</form>
EOM
}
if($chara[135]>=5){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=6>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�UF�ɒ��킷��">
</form>
EOM
}
if($chara[135]>=6){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=7>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="���z�����E�VF�ɒ��킷��">
</form>
EOM
}
if($chara[304]==1 or $chara[304]==2 or $chara[0] eq "jupiter"){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc>
<input type=submit class=btn value="�����E�ɓ˓�����">
</form>
EOM
}elsif(time()-$chara[314]>=10 and $chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=8>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="�����E�ɓ˓�����">
</form>
EOM
}
if($chara[304]==4 or $chara[304]==5){
if(time()-$chara[314]>=10 and $chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=9>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="�����E�̉��֐i��">
</form>
EOM
}
}
if($chara[128]>=5 and $chara[135]>=4 and !$chara[304]){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yuwaku>
<input type=submit class=btn value="�����̗��ݎ�">
</form>
EOM
}
if($chara[304]==3){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yuwaku2>
<input type=submit class=btn value="��V���󂯎��">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub yuwaku {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�����̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�����̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
�u���A���ʂ��A���X�����ȁE�E�E�B���͗��ݎ�������񂾁c�B<br>
�V�E���爫���E�ɕ����ꂽ�A���N�h�����Ƃ����g�҂���������񂾁c�B<br>
���c���~�߂邱�Ƃ��o������A�S��̌��f��40�������悤�Ǝv���񂾂��c�B�v<br><br>
</FONT>
<hr size=0>
<br>
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yes>
<input type=hidden name=yes value=1>
<input type=submit class=btn value="�����󂯂�">
</form>
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yes>
<input type=hidden name=yes value=2>
<input type=submit class=btn value="�����󂯂Ȃ�">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub yuwaku2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[304] !=3 ){&error("ERROR!");}

		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$isi[29]+=40;
		$isi[30]+=40;
		$isi[31]+=40;
		$isi[32]+=40;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
	$chara[304]=5;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�����̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�����̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
�u�悭����Ă��ꂽ�ȁA����̌��f�Z�b�g���I�v<br><br>
<font color="red" size=5>�΁A���A�ŁA���̌��f��40����ɓ��ꂽ�I</font>
</FONT>
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub yes {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[304]>0){&error("���ɑI�����܂�����B");}

	&get_host;

	$chara[304]=$in{'yes'};

	if($in{'yes'}==1){
		$com="���႟�A���񂾂��I�I";
	}else{
		$com="�����A�M�l�ɂ͂������܂�B";
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�����̊�</h1>
<hr size=0>
<FONT SIZE=3>
<B>�����̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
�u$com�v<br><br>
</FONT>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub anc {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�����E</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u��͂藈�����A$chara[4]�B<br>
����ȃG�l���M�[��������ȁE�E�E�����E���͂܂������͂������c�B<br>
���������́A�����E�ł��ɂ߂Ċ댯�ȃt�B�[���h�ɑ������낤�B<br>
�����A���̎��ł��A�����ɂ͎����҂��Ă��邩������Ȃ��E�E�E���邩�H<br>
�v<br><br>
</FONT>
<hr size=0>
<br>
EOM
if($chara[304]==1){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc1>
<input type=submit class=btn value="�A���N�h�����ɏP���|����">
</form>
EOM
}else{
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc2>
<input type=submit class=btn value="���Ă���">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub anc1 {

	&chara_load;

	&chara_check;

	$chara[304]=3;
	&chara_regist;

	&header;

	print <<"EOM";
<h1>�����E</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u��������A$chara[4]�I�H<br>
<br>
���ӂ��B�s�o�E�E�E�B�v<br><br>
<font color="red" size=5>�A���N�h�����ɒv�����𕉂킹���I</font>
</FONT>
<br><br><br><br>
�����ăA���N�h�����͏������E�E�E�B
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub anc2 {

	&chara_load;

	&chara_check;

	$chara[304]=4;
	&chara_regist;

	&header;

	print <<"EOM";
<h1>�����E</h1>
<hr size=0>
<FONT SIZE=3>
<B>�A���N�h����</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
�u���ӂ��B�s�o�E�E�E�B�v<br><br>
<font color="red" size=5>�┯�̌��m�����ł��ăA���N�h�����ɏP�����������I<br>
�A���N�h�����͒v�����𕉂����I</font>
</FONT>
<br><br><br><br>
�����ăA���N�h�����Ƌ┯�̌��m�͏����Ă��܂����E�E�E�B<br>
$chara[4]�͎d���Ȃ����ɖ߂邱�Ƃɂ����E�E�E�B<br>
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}