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
<form action="$script" method="post">
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

&error;

exit;

#--------#
#  �h��  #
#--------#
sub yado {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

        #�h��v�Z
        $yado_daix=int($yado_dai*$chara[18]);
	$com="";
	if($yado_daix>100000 and int(rand(100))==0 and $chara[15] != $chara[16]){
		$chara[305]+=1;
		$com="���y�Y�ɏh���݂���ɓ��ꂽ�I";
	}
($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
$mon = $mon+1;
$year = $year +1900;
	if($mon==1 and $mday==1 and $year != $chara[306]){
		$chara[306]=$year;
		if($chara[18]<=10000){
			$okane=$year * int($chara[18]/10+10) * 10000;
			$chara[19]+=$okane;
			$com="�����܂��Ă��߂łƂ��C�x���g�I���N�ʂ�$okane�f��ɓ��ꂽ�I";
		}else{
			$chara[305]+=$year;
			$com="�����܂��Ă��߂łƂ��C�x���g�I���y�Y�ɏh���݂�$year��ɓ��ꂽ�I";
		}
	}
		
	$chara[15] = $chara[16];
	$chara[42] = $chara[43];
	$chara[19] -= $yado_daix;
	$chara[28] = $boss;
	$chara[17]=int($chara[17]);
	$chara[40]=int($chara[40]);

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;
	$xtime = $vtime + 1;
	$ztime = $vtime + 1;
	if($ztime < 10){$chara[139]=0;}
	if ($chara[19] < 0) { &error("����������܂���I$back_form"); }

	&chara_regist;
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/cmp.lock";
	&lock($lock_file,'BT');

	if($chara[140]==2){&read_winner2;$wt="winner2_file";}
	elsif($chara[140]==3){&read_winner3;$wt="winner3_file";}
	elsif($chara[140]==4){&read_winner4;$wt="winner4_file";}
	elsif($chara[140]==5){&read_winner5;$wt="winner5_file";}
	else{&read_winner;$wt="winner_file";}

	if ($winner[0] eq $chara[0]) {
		$winner[15] = $winner[16];
		$new_winner = '';
		foreach(@winner){
			$new_winner .="$_<>";
		}
		open(OUT,">$winner$$wt");
		print OUT $new_winner;
		close(OUT);
	}

	&unlock($lock_file,'BT');

	&header;

	print <<"EOM";
<h1>�h��</h1>
<hr size=0>
<FONT SIZE=3>
$yado_daix�f���g�p���A�̗͂�S�񕜂��܂����I<br>
$com</FONT>
EOM
if($chara[305]>100 and int(rand(30))==0){
	print <<"EOM";
<FONT SIZE=3>
�A�蓹�A�Ȃ�ƁA�������󂩂�����������C�|��Ă���̂������܂����B<br>
�h���݂�100������Ό��f���P���ꂻ���ł��B<br>
���݁A�h���݂�$chara[305]�������Ă��܂��B<br>
�h����100�Ɖ����̌��f���������Ă��炢�܂����H</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti>
<input type=submit class=btn value="�������Ă��炤">
</form>
EOM
}elsif($chara[305]>30 and int(rand(10))==0){
	print <<"EOM";
<FONT SIZE=3>
�A�蓹�A�Ȃ�ƁA�������󂩂����V�g����C�|��Ă���̂������܂����B<br>
�h���݂�30������Ό��C���o���Ă��ꂻ���ł��B<br>
���݁A�h���݂�$chara[305]�������Ă��܂��B<br>
�h����30�������܂����H</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti2>
<input type=submit class=btn value="������">
</form>
EOM
}elsif($chara[305]>20 and int(rand(10))==0){
	print <<"EOM";
<FONT SIZE=3>
�A�蓹�A�Ȃ�ƁA�����͌��Ȃ����n���l�𔭌����܂����B<br>
�h���݂�20���炢�~�������Ȋ�����Ă��܂��B<br>
���݁A�h���݂�$chara[305]�������Ă��܂��B<br>
�h����20�������܂����H</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti3>
<input type=submit class=btn value="������">
</form>
EOM
}elsif($chara[305]>0){
	print <<"EOM";
<FONT SIZE=3>
���݁A�h���݂�$chara[305]�������Ă��܂��B<br>
������ԉɂ������Ă��邨�݂ŁA�����ȏh�ł����Ⴆ�܂���B<br>
�����A���̂��݂�T�����߂邨�ꂳ�񂪌���āA���A�ȃA�C�e���ƌ������Ă���邾�Ȃ�āA<br>
����Ȗϑz������Ă͂����܂���B�B</FONT>
EOM
}
	&shopfooter;

	&footer;

	exit;
}

#--------#
#  �h��  #
#--------#
sub moti {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 100) { &error("���݂�����܂���I$back_form"); }
	else {
		$chara[305] -= 100;
		$chara[308] += 1;
		$gishi=int(rand(4)+29);
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		$so=0;
		foreach(@sozai_data){
			($sozainame) = split(/<>/);
			if($so == $gishi) {last;}
			$so++;
		}
		@isi[$gishi]+=1;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$com = "<font class=\"red\" size=5>$sozainame����ɓ��ꂽ�b�I�I</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�h��</h1>
<hr size=0>
<FONT SIZE=3>
�����ɏh���݂�100�������I<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub moti2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 30) { &error("���݂�����܂���I$back_form"); }
	else {
		$chara[305] -= 30;
		$chara[307] += 1;
		$gishi=int(rand(21)+12);
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		$so=0;
		foreach(@sozai_data){
			($sozainame) = split(/<>/);
			if($so == $gishi) {last;}
			$so++;
		}
		@isi[$gishi]+=1;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$com = "<font class=\"red\" size=5>�V�g�͂����$sozainame�����ꂽ�b�I�I</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�h��</h1>
<hr size=0>
<FONT SIZE=3>
�V�g�ɏh���݂�30�������I<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub moti3 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 20) { &error("���݂�����܂���I$back_form"); }
	else {
		$chara[305] -= 20;
		$chara[309] += 1;
		$gishi=23;
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		$so=0;
		foreach(@sozai_data){
			($sozainame) = split(/<>/);
			if($so == $gishi) {last;}
			$so++;
		}
		$jizo = int(rand(3)+1);
		@isi[$gishi]+=$jizo;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$com = "<font class=\"red\" size=5>���n���l�͂����$sozainame��$jizo���ꂽ�b�I�I</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�h��</h1>
<hr size=0>
<FONT SIZE=3>
���n���l�ɏh���݂�20�������I<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}