#!/usr/local/bin/perl

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

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
	&error("�o�[�W�����A�b�v���ł�"); 
}
&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&chat;

#----------------#
#--�`���b�g���--#
#----------------#
sub chat {

	&all_data_read;

	&get_time(time());

	if ($in{'tch'} =~ m/[^0-9]/){
		&chat_error("�`�����l���ɐ����ȊO�̕������܂܂�Ă��܂��B"); 
	}

	if($in{'chattime'} and $in{'mes'}) {

		$now_mes = length($in{'mes'});

		foreach (@ban_word) {
			if(index($in{'mes'},$_) >= 0) {
				&chat_error("�\\���͋֎~����Ă��܂�");
			}
		}

		if ($now_mes > $chat_size) {
			&res("���b�Z�[�W���������܂��I���p��$mes_size�����܂łł��I(���ݕ������F$now_mes)<br>");
		}

		foreach (@shut_id) {
			$_ =~ s/\*/\.\*/g;
			if ($in{'id'} =~ /$_/) {
				&chat_error("�������֎~����Ă��܂�");
			}
			if ($in{'id'} == "3333") {
				&chat_error("�������֎~����Ă��܂�");
			}
		}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);

		$mes_sum = @chat_mes;

		if($mes_sum > $mes_max) { pop(@chat_mes); }
		if($in{'tch'}){$tch=$in{'tch'};}
		elsif($in{'tch2'}){$tch=$in{'tch2'};}
		unshift(@chat_mes,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	}

	&header;

	open(IN,"$chat_file");
	@CHAT_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@CHAT_LOG){
		($hid,$hname,$htime,$hmessage,$hhost,$clv,$tch,$sasa) = split(/<>/);
		if ($max_chat < $i) {
			last;
		}
$foncolor=$text;$foncolort=$text;$foncolors=$text;$foncoloru=$text;
if($in{'chan'} and $in{'chan'}==$tch){$kchn=1;}elsif($sasa and $sasa eq $in{'name'}){$kchn=2;}else{$kchn=0;}
if($kchn==1){$foncoloru="red";}elsif($kchn==2){$foncoloru="yellow";$fonmes="(From $hname)";}else{$foncolors=$text;$fonmes="";}
#if($in{'chan'} and $in{'chan'}==$tch){$fonmest="(ch$tch)";}else{$fonmest="";}
if($hname and $hname eq $in{'name'} and $sasa){$foncolort="yellow";$fonmest="(To $sasa)";}else{$foncolort=$text;$fonmest="";}
if($foncoloru ne $text){$foncolor=$foncoloru;}
elsif($foncolors ne $text){$foncolor=$foncolors;}
elsif($foncolort ne $text){$foncolor=$foncolort;}
		print <<"EOM";
<font color="$foncolor">
EOM
if($in{'tch'}==$tch or $kchn==1){
if(!$sasa or $kchn==2 or $hid eq $in{'id'}){
if(!$clvh) { print "<font size=\"$fsize\"><b>$hname</b>>>�u$fonmes$fonmest$hmessage�v$htime\</font>\n";
}else { print "<font size=\"$fsize\"><b>$hname(Lv.$clv)</b>>>�u$hmessage�v$htime\</font>\n"; }
	print <<"EOM";
<br></font>
EOM
}}
		$hit=1;$i++;
	}
	if(!$hit) { print "<hr size=0><font color=$text>���b�Z�[�W�͂���܂���</font>\n"; }
	print <<"EOM";
<hr size=0>
<!--�폜�֎~-->
<center>FFA CHAT by <a href="http://wsr.a-auc.jp/" target="_blank">Right-Blue</a></center>
</body></html>
EOM
	exit;
}

#--------------#
#--�G���[����--#
#--------------#
sub chat_error {

	&header;
	print "<center><h3><b>�v�������������I�I</b></h3>\n";
	print "<font color=red><B>$_[0]</B></font><br><br>\n";
	print "<font size=2><b>����/�X�V�{�^���������Ă�������</b></font></center>\n";
	print "</body></html>\n";
	exit;
}