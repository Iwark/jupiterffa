#!/usr/local/bin/perl
BEGIN{ $| = 1;open(STDERR,">&STDOUT"); }
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
#require 'data/ffadventure.ini';

# �`���b�g���O�t�@�C��
$chat_file = "datalog/chatloog.cgi";
# �`���b�g�\����
$max_chat = 18;
# ���b�Z�[�W�ۑ���
$mes_max = 100;
# �ő僁�b�Z�[�W�T�C�Y(���p������)
$mes_size = 120;
# ID�ł̃`���b�g����(�r�炵�΍�)
$shut_id[0] = "test";
$shut_id[1] = "unnko";
$shut_host[0] = "118.22.98";
$shut_host[1] = "110.67.181";
$shut_host[2] = "111.217.192";
# �`���b�g�Ƀ��x���\�������邩(Yes:1 NO:0)
$clvh = 0;
# �t�H���g�T�C�Y(����2)
$fsize = 2.5;
# �w�i�F���w��
$bgcolor = "#000011";
# �����F���w��
$text = "#aaaaff";

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

		if ($now_mes > $mes_size) {
			&chat_error("���b�Z�[�W���������܂��I���p��$mes_size�����܂łł��I(���ݕ������F$now_mes)<br>");
		}

		foreach (@shut_id) {
			$_ =~ s/\*/\.\*/g;
			if ($in{'id'} =~ /$_/) {
				&chat_error("�������֎~����Ă��܂�");
			}
		}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);

		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;
		$year = $year +1900;
		$kyo="$year$mon$mday";

		open(IN,"datalog/meslog/$kyo.cgi");
		@chat_mes2 = <IN>;
		close(IN);

		@zenkai = split(/<>/,$chat_mes[0]);
		#@zenkai2 = split(/<>/,$chat_mes[1]);
		#$koktime=time();
		#if(($koktime-$zenkai2[6])<60 and $in{'mes'}){&chat_error("�N�[���^�C���ł��B");}
		if($zenkai[0] ne $in{'id'} or $zenkai[3] ne $in{'mes'}){

		$mes_sum = @chat_mes;
		
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		if($in{'tch'}){$tch=$in{'tch'};}
		elsif($in{'tch2'}){$tch=$in{'tch2'};}
		elsif($in{'tch3'}){$tch=$in{'tch3'};}
		#if(!$tch){&chat_error("���C���`���b�g�͌��ݎg�p�ł��܂���B");}
		unshift(@chat_mes,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");
		unshift(@chat_mes2,"$in{'id'}<>$in{'name'}<>$gettime<>$in{'mes'}<>$host<>$in{'level'}<>$tch<>$in{'sasayaki'}<>\n");
		open(OUT,">datalog/meslog/$kyo.cgi");
		print OUT @chat_mes2;
		close(OUT);

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);
		
		}

		&unlock($lock_file,'MS');

	}

	&header;

	open(IN,"$chat_file");
	@CHAT_LOG = <IN>;
	close(IN);

	$hit=0;$i=1;
	foreach(@CHAT_LOG){
		($hid,$hname,$htime,$hmessage,$hhost,$clv,$tch,$sasa,$bakuhatu) = split(/<>/);
		if ($max_chat < $i) {
			last;
		}
	$foncolor=$text;$foncolort=$text;$foncolors=$text;$foncoloru=$text;

	if($in{'chan'} and $in{'chan'}==$tch){
		$kchn=1;
		$foncoloru="red";
	}elsif($sasa and $sasa eq $in{'name'}){
		$kchn=2;
		$foncoloru="yellow";$fonmes="(From $hname)";
	}elsif($in{'chan2'} and $in{'chan2'}==$tch){
		$kchn=3;
		$foncoloru="pink";
	}else{
		$kchn=0;
		$foncolors=$text;$fonmes="";
	}
	if($hname and $hname eq $in{'name'} and $sasa){
		$foncolort="yellow";
		$fonmest="(To $sasa)";
	}else{
		$foncolort=$text;
		$fonmest="";
	}
if($foncoloru ne $text){$foncolor=$foncoloru;}
elsif($foncolors ne $text){$foncolor=$foncolors;}
elsif($foncolort ne $text){$foncolor=$foncolort;}
		print <<"EOM";
<font color="$foncolor">
EOM
if($in{'tch'}==$tch or $kchn==1 or $kchn==3){
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