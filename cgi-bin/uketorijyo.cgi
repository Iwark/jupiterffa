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
<form action="uketorijyo.cgi" method="post">
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

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$g=0;
	foreach(@member_data){
		($name,$no,$kazu) = split(/<>/);
		if($name eq $chara[4]){$hit=1;last;}
		$g++;
	}
	if($hit==1 and $no==189){
		$suke="�ŋ�ԃ`�P�b�g";
	}elsif($hit==1 and $no==301){
		$suke="�΂̐�";
	}elsif($hit==1 and $no==302){
		$suke="���̐�";
	}
	print <<"EOM";
<h1>��揊</h1>
<hr size=0>
<FONT SIZE=3>
<B>��揊�̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�N������a�����Ă���̂����������ȁH�v<br>
�������ł́A��ɃC�x���g�Ŋl�������A�C�e���Ȃǂ��󂯎�邱�Ƃ��ł��܂��B<br>
</FONT>
<hr size=0>
EOM
if($hit==1){
	print <<"EOM";
$suke��$kazu�A�a�����Ă��܂��B�󂯎��܂����H
<form action="./uketorijyo.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<input type=submit class=btn value="�󂯎��">
</form>
EOM
}else{
	print <<"EOM";
�a�����Ă�����̂͂���܂���B<br>
(���a���萔�F$g)
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
sub uketoru {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$g=0;
	foreach(@member_data){
		($name,$no,$kazu) = split(/<>/);
		if($name eq $chara[4]){
			$hit=1;
			splice(@member_data,$g,1);
			open(OUT,">uketori.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$g++;
	}
	if($hit==1 and $no==189){
		$suke="�ŋ�ԃ`�P�b�g";
	}elsif($hit==1 and $no==301){
		$suke="�΂̐�";
	}elsif($hit==1 and $no==302){
		$suke="���̐�";
	}

	$chara[$no]+=$kazu;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$suke��$kazu�A�󂯎��܂����B<br>
</font>
<br>
<form action="uketorijyo.cgi" method="post">
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
sub uketoru2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[301] == $chara[18] and $chara[302] == $chara[17]){&error("���̃A�C�e���͊��Ɏ󂯎��܂���");}
	else{$chara[301]=$chara[18];$chara[302]=$chara[17];}

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$i_no=$chara[4];
	$i_name=$in{'mono'};
	$i_dmg=1;
	push(@member_data,"$i_no<>$i_name<>$i_dmg<>\n");
	open(OUT,">uketori.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	if($i_name==189){
		$suke="�ŋ�ԃ`�P�b�g";
	}elsif($i_name==301){
		$suke="�΂̐�";
	}elsif($i_name==302){
		$suke="���̐�";
	}
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$suke����揊�ɓ͂��܂���<br>
</font>
<br>
<form action="uketorijyo.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="��揊��">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}