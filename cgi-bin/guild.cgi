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
<form action="guild.cgi" >
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

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);

	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){last;}
	}

	open(OUT,">guildlog/$mon$mday.cgi");
	print OUT @member_data;
	close(OUT);

	print <<"EOM";
<h1>�M���h�Љ</h1>
<hr size=0>
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�M���h���������鎞�́A8�����ȓ��ŃM���h���A30���ȓ��ŃR�����g��ݒ肵�ĂȁB<br>
�����A�ɐݒ肷��l�́A�]���E�񐔁~�P�O�O�{���x�����B������z���Ă��Ȃ��҂͓���Ȃ��B<br>
���F�����ɂ́A�N�G�X�g���e�ŏI�������I���Ă���K�v������܂��B<br>
���S�̂��߁A���U����O�ɁA�����o�[�ɒE�ނ��Ă��炤�悤�ɂ��Ă��������B<br>
�M���h����ς��鎞�́A�����o�[�̕��ɓ���Ȃ����Ă��炤���ƂɂȂ邩������܂���B�v
</FONT>
<hr size=0>
EOM
if($chara[66] and $gg_leader eq $chara[4]){
	print <<"EOM";
<table>
<tr>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=henko>
�R�����g�@�F<input type="text" name="g_com" value="" size=40><br>
�����@�@�F<input type="text" name="g_sei" value="" size=10><br>
<br>�@�@
<input type=submit class=btn value="�M���h���ύX">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=memnin>
<br>�@�@
<input type=submit class=btn value="�����o�[�l������">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kaisan>
<br>�@�@
<input type=submit class=btn value="���U">
</form>
</td>
</tr>
<tr>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=keru>
�Ώۖ��F<input type="text" name="keri" value="" size=10><br>
<br>�@�@
<input type=submit class=btn value="�����o�[�̋����E��">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=master>
�Ώۖ��F<input type="text" name="master" value="" size=10><br>
<br>�@�@
<input type=submit class=btn value="�}�X�^�[���̈ڏ�">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=toppa>
�˔j�Ґ���
<input type="radio" name="toppa" value="0" size=10>OFF
<input type="radio" name="toppa" value="1" size=10>ON<br>
<br>�@�@
<input type=submit class=btn value="�˔j�҂��W����">
</form>
</td>
</tr>
</table>
EOM
}else{
	print <<"EOM";
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
�M���h���F<input type="text" name="g_name" value="" size=40><br>
�R�����g�@�F<input type="text" name="g_com" value="" size=40><br>
�����@�@�F<input type="text" name="g_sei" value="" size=10><br>
<br>�@�@
<input type=submit class=btn value="�M���h����">(10���f)
</form>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=dattai>
<br>�@�@
<input type=submit class=btn value="�E��">
</form>
EOM
}
	print <<"EOM";
<table border=1>
<th colspan="3">�M���h��</th><th>���[�_�[</th><th>�M���h���x��</th><th>�����o�[��</th><th>����</th><th>�˔j����</th><th>�R�����g</th></tr><tr>
EOM
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$gd=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_mem){
			$topp = "��";
			open(IN,"allguild2.cgi");
			@member_data2 = <IN>;
			close(IN);
			foreach(@member_data2){
				($gne,$gto) = split(/<>/);
				if($gg_name eq $gne){if($gto==1){$topp = "�L";}last;}
			}
			$gg_maxmem=$gg_lv + 4;
			print <<"EOM";
			<tr>
			<td>
			<form action="./guild.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=kanyu>
			<input type=hidden name=kanyu_id value=$gg_name>
			<input type=submit class=btn value="����">
			</form>
			</td>
			<td>
			<form action="./guild.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=hyouji>
			<input type=hidden name=hyouji_id value=$gg_name>
			<input type=submit class=btn value="�����o�[">
			</form>
			</td>
			<td align=center>$gg_name</td>
			<td align=center>$gg_leader</td>
			<td align=center>$gg_lv</td>
			<td align=center>$gg_mem\/$gg_maxmem</td>
			<td align=center>$gg_sei</td>
			<td>$topp</td>
			<td>$gg_com</td></tr>
EOM
		}
		$gd++;
	}
	print <<"EOM";
</tr>
</table>
<p>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[0] eq "test" or $chara[0] eq "test2"){
		&error("test�L�����̓M���h���쐬�ł��܂���B$back_form");
	}
	if($chara[127]!=2){
		&error("�N�G�X�g���e�ŏI�������I���Ă��Ȃ����߃M���h�����܂���B$back_form");
	}
	if ($chara[66]){&error("���ɃM���h�ɏ������Ă��܂��B$back_form");}
	else{
		if ($in{'g_name'} eq "") {
			&error("�M���h�������͂���Ă��܂���B$back_form");
		}
		if (length($in{'g_name'}) > 16) {
			&error("�M���h�����������܂��B$back_form");
		}
		if (length($in{'g_com'}) > 60) {
			&error("�R�����g���������܂��B$back_form");
		}
		if ($in{'g_sei'} =~ m/[^0-9]/){
			&error("�������x���ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
		}
	}
	if($chara[19]<1000000000){
		&error("����������܂���");
	}else{
		$chara[19]-=1000000000;
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;

	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_name eq $in{'g_name'}){&error("�M���h����ς��Ă��������B$back_form");}
	}

	push(@member_data,"$in{'g_name'}<>$chara[4]<>0<>1<>1<>$in{'g_sei'}<>$in{'g_com'}<>$chara[0]<>\n");

	open(OUT,">allguild.cgi");
	print OUT @member_data;
	close(OUT);

	$chara[66]=$in{'g_name'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h����������I�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub kanyu {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[0] eq "test"){
		&error("test�L�����̓M���h�ɉ����ł��܂���B$back_form");
	}
	$gutime=time();
	$gutime=int($gutime/3600) - 12;
	if($chara[68] > $gutime){
		&error("�O��M���h�ɉ������Ă���̎��Ԃ��Z�����܂��B$chara[68] / $gutime $back_form");
	};

	if ($chara[66]){&error("���ɃM���h�ɏ������Ă��܂��B$back_form");}
	elsif($in{'kanyu_id'} eq "") {&error("�������I�����Ă��������B$back_form");}

	open(IN,"allguild2.cgi");
	@member_data2 = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data2){
		@array2 = split(/<>/);
		if($array2[0] eq $in{'kanyu_id'}){$hit=1;last;}
	}
	
	if ($hit == 1 and $chara[70]<1 and $array2[1]==1){&error("�˔j�҂݂̂������悤��������Ă��܂��B$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $in{'kanyu_id'}){
			$gg_maxmem=$array[3] + 4;
			if($array[4] >= $gg_maxmem){&error("���̃M���h�͖����ł��B$back_form");}
			if(!$chara[37] or $chara[70]==1){if($chara[18] < $array[5]){&error("�������ł��B$back_form");}}
			elsif($chara[18] + $chara[37] * 100 < $array[5]){&error("�������ł��B$back_form");}
			$array[4]+=1;
			$new_array = '';
			$new_array = join('<>',@array);
			$new_array =~ s/\n//;
			$new_array .= "$chara[0]<>\n";
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}


	$chara[66]=$in{'kanyu_id'};

	$gutime=time();
	$gutime=int($gutime/3600);
	$chara[68]=$gutime;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h�ɉ����������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub dattai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[66]){

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=0;$g<$gg_maxmem+10;$g++){
				if($array[$g] eq $chara[0]){splice(@array,$g,1);$hit=1;last;}
			}
			if($hit){
				$array[4]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array =~ s/\n//;
				$new_array .= "<>\n";
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
			#if(!$hit){&error("�E�ގ��s $back_form");}
		}
		$i++;
	}

	$chara[66]="";

	}else{&error("�M���h�ɓ����Ă܂���B$back_form");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h�E�ނ������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub henko {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if (length($in{'g_com'}) > 60) {
		&error("�R�����g���������܂��B$back_form");
	}
	if ($in{'g_sei'} =~ m/[^0-9]/){
		&error("�������x���ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			if($in{'g_sei'}){$array[5] = $in{'g_sei'};}
			if($in{'g_com'}){$array[6] = $in{'g_com'};}
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h���ύX�������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub kaisan {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$member_data[$i]="";
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	$chara[66]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h���ύX�������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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
#----------------#
#  ��񔃂��@�@  #
#----------------#
sub keru {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=8;$g<=@array;$g++){
				$lock_file = "$lockfolder/$array[$g].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[$g].cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[$g].lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				if($mem1[4] eq $in{'keri'}){splice(@array,$g,1);$hit=1;last;}
			}
			if($hit){
				$array[4]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}
	if(!$hit){&error("����ȃL����������܂���$back_form");}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h���ύX�������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub hyouji {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	$ima = time();

	if($in{'hyouji_id'} eq "") {&error("�M���h��I�����Ă��������B$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				if($mem[70]<1){$sou=$mem[18]+$mem[37]*100;}
				else{$sou=$mem[18];}
				$rdate = $mem[27];
				$niti = $ima - $rdate;
				if(int($niti / (60*60*24))==0){
					$niti=int($niti / (60*60));
					$kniti="$niti���ԑO";
				}else{
					$niti = int($niti / (60*60*24));
					$kniti="$niti���O";
				}
				if($mem[4]){
					if($mem[70]<1){
						$ct.= "<tr><td>$mem[4]</td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
					}elsif($mem[70]<2){
$ct.= "<tr><td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
					}else{
$ct.= "<tr><td><font color=\"red\">$mem[4]</font></td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
					}
				}
			}
			last;
		}
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";

<B></B><p>
<table border=1>
<th>���O</th><th>���x��</th><th>�o�O�`�F�b�N�p</th><th>�Ō�̃��O�C��</th>
$ct<p>
</table>
<br>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvsort">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="���x�����ɕ��ёւ�">
</form>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="jogai">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="�o�O���Ă�l���O">
</form>
EOM
}

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub memnin {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){$hit=1;last;}
		$i++;
	}
	if($hit){
		$g=0;
		foreach(@array){
			if(!$_ and $g>6){splice(@array,$g,1);}
			$g++;
		}
		$memmem=@array;
		$array[4]=$memmem - 8;
		$new_array = '';
		$new_array = join('<>',@array);
		$member_data[$i]=$new_array;
		open(OUT,">allguild.cgi");
		print OUT @member_data;
		close(OUT);
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�����o�[�̐l���𒲐��������B�v</font>
<br>
<form action="guild.cgi" >
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

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub master {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if(!$in{'master'}){&error("�����Ɠ��͂��Ă�������");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=8;$g<=@array;$g++){
				$lock_file = "$lockfolder/$array[$g].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[$g].cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[$g].lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				if($mem1[4] eq $in{'master'}){
					$array[1]=$mem1[4];
					$array[7]=$mem1[0];
					$array[$g]=$chara[0];
					$hit=1;
					last;
				}
			}
			if($hit){
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}
	if(!$hit){&error("����ȃL����������܂���$back_form");}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h���ύX�������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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
sub toppa {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild2.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$member_data[$i]="$chara[66]<>$in{'toppa'}<>\n";
			$hit=1;
			last;
		}
		$i++;
	}
	if(!$hit){
		push(@member_data,"$chara[66]<>$in{'toppa'}<>\n");
	}
	open(OUT,">allguild2.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u�M���h���ύX�������I<br>
�v</font>
<br>
<form action="guild.cgi" >
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
sub lvsort {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	$ima = time();

	if($in{'hyouji_id'} eq "") {&error("�M���h��I�����Ă��������B$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			$a=0;$b=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				$rdate = $mem[27];
				$niti = $ima - $rdate;
				if(int($niti / (60*60*24))==0){
					$niti=int($niti / (60*60));
					$kniti="$niti���ԑO";
				}else{
					$niti = int($niti / (60*60*24));
					$kniti="$niti���O";
				}
				if($mem[70]<1){
					$sou=$mem[18]+$mem[37]*100;
					$tmaename[$a]=$mem[4];
					$tmaelv[$a]=$sou;
					$tmaeniti[$a]=$kniti;
					$tmaeguild[$a]=$mem[66];
					$a++;
				}else{
					$sou=$mem[18];
					$tgoname[$b]=$mem[4];
					$tgolv[$b]=$sou;
					$tgoniti[$b]=$kniti;
					$tgoguild[$b]=$mem[66];
					$b++;
				}
			}
			@gosort = sort { $b <=> $a } @tgolv;
			@maesort = sort { $b <=> $a } @tmaelv;
			for($aa=0;$aa<$b;$aa++){
				if($gosort[$aa]){
					$t=0;$cc=$aa-1;
					foreach(@tgolv){
						if($aa==0 and $_ == $gosort[$aa]){last;}
						elsif($_ == $gosort[$aa] and $gonamesort[$cc] ne $tgoname[$t]){last;}
						$t++;
					}
					$gonamesort[$aa]=$tgoname[$t];
$ct.= "<tr><td><font color=\"yellow\">$gonamesort[$aa]</font></td><td>$tgolv[$t]</td><td>$tgoguild[$t]</td><td>$tgoniti[$t]</td></tr>";
				}
			}
			for($bb=0;$bb<$a;$bb++){
				if($maesort[$bb]){
					$t=0;$dd=$bb-1;
					foreach(@tmaelv){
						if($bb==0 and $_ == $maesort[$bb]){last;}
						elsif($_ == $maesort[$bb] and $maenamesort[$dd] ne $tmaename[$t]){last;}
						$t++;
					}
					$maenamesort[$bb]=$tmaename[$t];
$ct.= "<tr><td>$maenamesort[$bb]</font></td><td>$tmaelv[$t]</td><td>$tmaeguild[$t]</td><td>$tmaeniti[$t]</td></tr>";
				}
			}
			last;
		}
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";

<B></B><p>
<table border=1>
<th>���O</th><th>���x��</th><th>�o�O�`�F�b�N�p</th><th>�Ō�̃��O�C��</th>
$ct<p>
</table>
<br>
EOM
	print <<"EOM";
<form action="guild.cgi" >
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

sub jogai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'hyouji_id'} eq "") {&error("�M���h��I�����Ă��������B$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";$t=0;
	foreach(@member_data){
		#s/\n//i;
		#s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				if($mem[66] ne $g_name){
					splice(@battle_mem,$bgb,1);
					#$bgb-=1;
				}
			}
			last;
		}
		$t++;
	}
	$member_data[$t] = "$pre[0]<>$pre[1]<>$pre[2]<>$pre[3]<>$pre[4]<>$pre[5]<>$pre[6]<>";
	$i=0;
	while($battle_mem[$i]){
		$member_data[$t].="$battle_mem[$i]<>";
		$i++;
	}
	$member_data[$t].="\n";

	open(OUT,">allguild.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";

<B></B><p>
<br>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvsort">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="���x�����ɕ��ёւ�">
</form>
<form action="guild.cgi" >
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
