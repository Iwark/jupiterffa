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
<form action="./hatake.cgi" method="post">
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

&item_view;

exit;

#----------------#
#  �y�b�g�\���@  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	if(!$chara[66]){&error("�ǂ����M���h�ɓ����Ă�");}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	foreach (@all_hatake) {
		@hatake = split(/<>/);
		if($hatake[0] eq $chara[66]){
			$hit=1;last;
		}
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$ghit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){$ghit=1;last;}
	}

	&header;
if($hit==1){
	print <<"EOM";
	<h1>��</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>��������</B><BR>
	�u�M���h���L�̔������[��<br>
	�k���ɗ����̂����H��ς���́[��<br>
	�k����̂͂���l�l������܂ł���B��肷���͂悭�Ȃ��񂶂�B�v
	</FONT>
	<br>
	�y�n�����N�@�F$hatake[1]<br>
	�앨�̗ʁ@�@�F$hatake[2]<br>
	�ł������S�F$hatake[3] (���E��3)<br>
	�������@�@�@�F$hatake[4] (���E��100)<br>
	�P�������S�@�F$hatake[5] (���E��10)<br>
	<br>
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=tagayasu>
	<input type=submit class=btn value="�k��">
	</form>
EOM
if($hatake[2]>100000 and $ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=sellrank>
	<input type=submit class=btn value="�y�n�����N�𔄂�">(100�|�C���g���݂P��)
	</form>
EOM
}
if($hatake[6]==1){
	if($ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="�앨��A����">
	<font color="red">���M���h�}�X�^�[�̂ݐA���邱�Ƃ��ł����Ԃł��B</font>
	</form>
EOM
	}else{
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="�앨��A����" disabled>
	<font color="red">���M���h�}�X�^�[�ȊO�͐A����̋֎~�ߔ��ߒ�</font>
	</form>
EOM
	}
}else{
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="�앨��A����">
	</form>
EOM
}
if($chara[31] eq "0044"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ringo>
	<input type=submit class=btn value="�ł������S��A����(�������Ȃ�܂�)">
	</form>
EOM
}
if($chara[31] eq "0045"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kakasi>
	<input type=submit class=btn value="�������𗧂Ă�(�������Ȃ�܂�)">
	</form>
EOM
}
if($chara[31] eq "0046"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=mikan>
	<input type=submit class=btn value="�`�P�����Ɏd���𗊂�(�����Ȃ��Ȃ�܂�)">
	</form>
EOM
}
if($chara[31] eq "0048"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=petring>
	<input type=submit class=btn value="�y�b�g�����O��A����(�������Ȃ�܂�)">
	</form>
EOM
}
if($chara[31] eq "0054"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=chees>
	<input type=submit class=btn value="�ɏ�̃`�[�Y��A����(�������Ȃ�܂�)">
	</form>
EOM
}
if($ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kinsi>
	<input type=submit class=btn value="�A����̋֎~�ߔ���/����">
	</form>
EOM
}
}else{
	print <<"EOM";
	<h1>��</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>��������</B><BR>
	�u���𔃂��ɗ����̂��`�H�����̂̓M���h�}�X�^�[��������`�B���Ȃ݂�100���f�ł������B�v
	</FONT>
	<br>
	<br>
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kau>
	<input type=submit class=btn value="����">
	</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub kau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($chara[66] and $gg_leader eq $chara[4]){$hit=1;last;}
	}

	if($hit!=1){&error("�M���h���[�_�[�ł͂���܂���");}
	if($chara[19] < 1000000){&error("����������܂���B");}
	else{$chara[19] -= 1000000;}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$hit=0;

	unshift(@all_hatake,"$chara[66]<>1<>0<>\n");

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

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
		$eg="$chara[66]�M���h�������w�����܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
	<br>
	<font size=5>���𔃂��܂���</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub tagayasu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("�]����10�񖢖��͔��d���ł��܂���");}
	if($chara[92]==$mday){&error("�����͂������d�������܂�����B");}
	else{$chara[92] = $mday;}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("����������܂���");}

	$tp=int(rand(4));
	if($chara[31] eq "0029"){$tp+=int(rand(8));}
	if($array[3]>0){$tp+=int($array[3]+1);}
	if($array[5]>0){$tp+=int($array[5]+1);}
	$array[1]+=$tp;
	$array[2]-=int(rand(2));
	if($array[2]<0){$array[2]=0;}
	$kaneget=$array[2]*10000;
	$chara[19]+=$kaneget;

	$new_array = '';
	$new_array = join('<>',@array);

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>
	�����k���܂��B
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	�U�N�b<br>
	<font size=5 color="red">
	$tp�@�|�C���g�A�y�n�����N���オ��A$kaneget �f���肵�܂����B
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub ueru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("�]����10�񖢖��͔��d���ł��܂���");}
	if($chara[92]==$mday){&error("�����͂������d�������܂�����B");}
	else{$chara[92] = $mday;}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$ghit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){$ghit=1;last;}
	}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("����������܂���");}
	elsif($array[6]==1 and $ghit!=1){&error("�A����̋֎~�߂����߂���Ă��܂��I");}
	$up=int(rand($array[1]));
	if($chara[31] eq "0029"){$up+=int(rand($array[1]));}
	if($array[3]>0){$up+=int(rand($array[3]*25));}
	if($array[5]>0){$up+=int(rand($array[5]*20));}
	if($array[2]+$up>100000){$up=100000-$array[2];}
	$array[2]+=$up;
	$array[1]-=int(rand($array[1]/2));
	if($array[1]<0){$array[1]=0;}
	$kaneget=$array[2]*10000;
	$chara[19]+=$kaneget;

	$new_array = '';
	$new_array = join('<>',@array);
	$new_chara .= '<>';

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�앨�A���܂��B</font>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	�O�T�b<br>
	<font size=5 color="red">�앨��$up�A���A$kaneget �f���肵�܂����B</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub ringo {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0044"){&error("�ł������S������܂���");}
	if(!$hit){&error("����������܂���");}
	if($array[3]>2){&error("����ȏ�ł������S�͐A�����܂���");}
	$array[3]+=1;
	$array[2]-=int(rand($array[2]/2));
	if($array[2]<0){$array[2]=0;}

	#$new_array = '';
	#$new_array = join('<>',@array);
	#$new_array =~ s/\n//;
	#$new_array .= "<>\n";

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�ł������S��A���܂��B</font>
	<br><br><br><br><br><br><br>
	�O�T�b<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">�ł������S��A�����B����̍앨���������B</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kakasi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0045"){&error("������������܂���");}
	if(!$hit){&error("����������܂���");}
	if($array[2]>10000){&error("�앨���������Ă������𗧂Ă�X�y�[�X������܂���B");}
	if($array[4]>99){&error("���������������ċC���������B���̂��炢�ɂ��Ă������B");}
	$array[4]+=1;
	$array[2]+=int(rand($array[2]/2));

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�������𗧂Ă܂��B</font>
	<br><br><br><br><br><br><br>
	�O�T�O�T�O�T�b<br>�s�R�[���B
	<br><br><br><br><br><br><br>
	<font size=5 color="red">�������𗧂Ă��B����̍앨���}���Ɉ�����B</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub mikan {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0046"){&error("�`�P���������܂���");}
	if(!$hit){&error("����������܂���");}
	if($array[3]<1){&error("�`�P�����̂���d��������܂���");}
	if($array[5]>9){&error("�P�������S����������悤�ł�");}
	$array[3]-=1;
	$array[5]+=1;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�`�P�����́A�ł������S���������I</font>
	<br><br><br><br><br><br><br>
	�҂��҂��҂��҂�<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">�`�P�����͎d�����I���A�ł������S���P�������S�ɕω������I�I</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub petring {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0048"){&error("�y�b�g�����O������܂���");}
	if(!$hit){&error("����������܂���");}

	$up=int(rand(10000));
	if($array[2]>50000){$up=int($up/2);}
	if($array[2]>100000){$up=int($up/4);}
	$array[2]+=$up;
	$kaneget=$array[2]*100000;
	$chara[19]+=$kaneget;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�����̎w�ւ���Ȃ��񂾃]�A�����A�ȃy�b�g�����O�Ȃ񂾃]�B</font>
	<br><br><br><br><br><br><br>
	�y�ɂ������ĉh�{���₴�������I�I�I<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">�앨���ǂ�ǂ�I$up�������A$kaneget �f���肵�܂����B</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub chees {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0054"){&error("�ɏ�̃`�[�Y������܂���");}
	if(!$hit){&error("����������܂���");}

	$up=int(rand(20000));
	if($array[2]>50000){$up=int($up/2);}
	if($array[2]>100000){$up=int($up/4);}
	if($array[2]>150000){$up=int($up/8);}
	if($array[2]>200000){$up=int($up/20);}
	$array[2]+=$up;
	$kaneget=$array[2]*100000;
	$chara[19]+=$kaneget;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>�V�E�̗͂𓾂邱�Ƃ��o����Ƃ́A�A�܂������_�i�I�I�I</font>
	<br><br><br><br><br><br><br>
	�ɏ�`�[�Y�ŉh�{���₴�������I�I�I<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">�앨���ǂ�ǂ�ǂ�ǂ�ǂǂ�ǂ�I$up�������A$kaneget �f���肵�܂����B</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kinsi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("����������܂���");}

	if($array[6]==0){$array[6]=1;}
	else{$array[6]=0;}

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<font size=5 color="red">
	�A����̋֎~�߂𔭗�/�������܂����I
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub sellrank {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("�]����10�񖢖��͔��d���ł��܂���");}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("����������܂���");}
	if($array[2]<100000){&error("���Y��������܂���");}
	if($array[1]<100){&error("�y�n�����N������܂���");}
	else{
		$array[1]-=100;
		$chara[136] += 1;
	}
	$new_array = '';
	$new_array = join('<>',@array);

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<font size=5 color="red">
	�y�n�����N���P�O�O�|�C���g����A���݂��P�����肵�܂����B
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}