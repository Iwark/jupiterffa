#!/usr/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# shopfooter�Ăяo��
require 'item.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

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
<form action="icon.cgi" method="post">
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

if ($mode) { &$mode; }
&tensyoku;

exit;

#------------#
# �]�E�̐_�a #
#------------#
sub tensyoku {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�A�C�R����</h1><hr>
�A�C�R�����A�b�v���[�h�ł��܂��B<br>
�`���͂f�h�e�������͂i�o�d�f�݂̂ŁA�T�C�Y�͏������z�����肢���܂��B<br>
�܂����ɂ����ɗ���Ă�����ɂ͊֌W�Ȃ��b�ł����A�n�[�h���[�h�̕���p�ł�����ƁB<br>
�܂��A�A�C�R�����A�b�v���[�h�������Ƃ́A�K����p���{�^���������Ă��������B<br>
<font color="red" size=4>�����̃A�b�v���[�h�����摜�ȊO���p������̂͐�΂ɂ�߂Ă��������I�I</font><br>
<font color="red" size=4>����ɉ��x���s������A���M��ɍX�V�{�^��(�e�T)���������肵�Ȃ��ł��������B</font><br>
<font color="red" size=4><br>�摜�͏����߂̂��́A�T�C�Y��20K Bytes�ȉ���ڈ��ɂ��Ă��������B</br></font>
    <form action="upload.cgi" method="post" enctype="multipart/form-data">
      <p><input type="file" name="filename" /></p>
      <p>
         <input type="submit" class=btn value="���M" />
         <input type="reset" class=btn value="���Z�b�g" />
      </p>
    </form>
<form action="./icon.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
�摜No.�F<input type="text" name="no" value="" size=20><br>
<td><input type=submit class=btn value="��p��"></td>
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub uketoru {
	
	&get_host;

	&chara_load;

	&chara_check;

	if (!$in{'no'}){ &error("�摜�i���o�[����͂��Ă��������B$back_form"); }

	open(IN,"senyou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$sakujyo=0;
	foreach (@member_data) {
		($cid,$cno) = split(/<>/);
		if ($cno == $in{'no'}) {
			&error("���ɂ��̃A�C�R���͐�p������Ă��܂��B$back_form");
		}
		if ($cid eq $chara[0]){$sakujyo=$i+1;}
		$i++;
	}
	open(IN,"data/img.cgi");
	@img_data = <IN>;
	close(IN);
	$no_img_data=@img_data;
	if (200>$in{'no'} or 201+$no_img_data<$in{'no'}) {
		&error("��p���ł���ԍ��ł͂Ȃ��悤�ł��B$back_form");
	}
	if($sakujyo){
		$sakujyo=$sakujyo-1;
		splice(@member_data,$sakujyo,1);
	}

	push(@member_data,"$chara[0]<>$in{'no'}<>\n");

	open(OUT,">senyou.cgi");
	print OUT @member_data;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�A�C�R�����̃}�X�^�[</B><BR>
�u��p���������������B
�v</font>
<hr size=0>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}