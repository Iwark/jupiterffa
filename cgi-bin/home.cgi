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
<form action="home.cgi" method="post">
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

	print <<"EOM";
<h1>�Ȃ񂾂��킩��Ȃ���n</h1>
<hr size=0>
<FONT SIZE=3>
<B>��n�̔Ԑl</B><BR>
�u��H�A���܂��͒N���I�H<br>
�����͗�������֎~���A�A��A��b�I�I�v<br>
</FONT>
<hr size=0>
EOM
if($chara[0] eq "jupiter"){
	print "<table><tr><th>���O</th>";
	open(IN,"sozai.cgi");
	@sozai_data = <IN>;
	close(IN);
	$i=0;
	foreach (@sozai_data){
		($name)=split(/<>/);
		print "<th>$name</th>";
		$i++;
	}
	print "<th>���v</th></tr>";
	opendir (DIR,'./kako') or die "$!";
	foreach $entry (readdir(DIR)){
		if ($entry =~ /\.cgi/) {
			open(IN,"./kako/$entry");
			$WORK=<IN>;
			close(IN);
			@membe = split(/<>/,$WORK);
			open(IN,"./charalog/$entry");
			$fm=<IN>;
			close(IN);
			@fmm = split(/<>/,$fm);
			print "<tr><td>$fmm[4]</td>";
			$goukei=0;$g=0;
			foreach (@membe) {
				print "<td>$_</td>";
				$goukei+=$_;
				$g++;
			}
			while($g<$i){print "<td></td>";$g++;}
			print "<td>$goukei</td></tr>";
		}
	}
	closedir(DIR);
	print "</table>";
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}