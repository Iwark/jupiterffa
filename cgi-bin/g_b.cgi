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
<form action="g_b.cgi" method="post">
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

	open(IN,"siro.cgi");
	@siro_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>�U����t��</h1>
<hr size=0>
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�U���͈ꎞ�ԂɂɈ��܂ŁA���B<br>
����x�z����΁A�A�C�e���𐶎Y���邱�Ƃ��ł���B<br>
���̃M���h������Ă���T���o���Ă��Ȃ���ł͐킦�Ȃ����B<br>
�����̃��x������̐������x�����Ⴍ�Ȃ��Ɛ킦�Ȃ����B�v
</FONT>
<hr size=0>
EOM
if($chara[67]==$mday + $hour){print "�O��U���ɎQ�����Ă���P���Ԍo���Ă��܂���B";}
if($chara[66]){
	print <<"EOM";
<form action="./koujyou.cgi" method="post">
<table border=1>
���݂̏�x�z�M���h
<th colspan="2">��</th><th>�������x��</th><th>�M���h��</th><th>�x�z��</th><th>�퓬�Ԋu</th><th>���Y�i</th><th>���Y�x</th></tr><tr>
EOM
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$koutime=time();$koubut="";$hit=0;
	foreach(@siro_data){
		($siro_name,$siro_seigen,$gg_name,$sihaisya,$sihaisyaid,$kankaku,$seisanhin,$seisando,$maxseisando) = split(/<>/);
		$kankaku = 5 - int(($koutime - $kankaku)/60);
		if($kankaku<0){$kankaku=0;}
		if($siro_name and $siro_name ne "�ے���"){
			print "<tr>";
			if($gg_name ne $chara[66] and $kankaku==0 and $chara[67]!=$mday + $hour and $siro_seigen >= $chara[18]){
				print "<td><input type=radio name=siro_name value=$siro_name></td>";
			}
			else{
				print "<td>�@</td>";
			}
			print <<"EOM";
			<td align=center>$siro_name</td>
			<td align=center>$siro_seigen</td>
			<td align=center>$gg_name</td>
			<td align=center>$sihaisya</td>
			<td align=center>�c��$kankaku��</td>
			<td align=center>$seisanhin</td>
			<td align=center>$seisando\/$maxseisando</td>
EOM
		}
	}
	print <<"EOM";
</tr>
</table>
<p>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=koujyou>
<input type=submit class=btn value="�U���ɒ���">
</form>
<p>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="./g_b.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=syoutyou>
<td><input type=submit class=btn value="�ے��탁���o�[�Z���N�g"></td>
</form>
<form action="./koujyou.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=syoutyou>
<input type=hidden name=siro_name value="�ے���">
<td><input type=submit class=btn value="�ے���"></td>
</form>
EOM
}
open(IN,"seisanmati.cgi");
@seisanmati_data = <IN>;
close(IN);
$hit=0;
foreach(@seisanmati_data){
	($seisansya,$seisanmatihin) = split(/<>/);
	if($seisansya eq $chara[4]){$hit++;}
}
if($hit){
	print <<"EOM";
�󂯎��鐶�Y�i��$hit����܂��B
<form action="./g_b.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<td><input type=submit class=btn value="�󂯎��"></td>
</form>
EOM
}
}else{
	print "�M���h�ɏ������Ă��܂���B";
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

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"seisanmati.cgi");
	@seisanmati_data = <IN>;
	close(IN);
	$hit=0;$se_i=0;
	foreach(@seisanmati_data){
		($sid,$sname) = split(/<>/);
		if($chara[4] eq $sid){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($ssyoukyu,$ssno,$ssname) = split(/<>/);
				if($sname eq $ssname){$chara[$ssno]+=1;$hit=1;$seisanmati_data[$se_i]="";}
			}
		}
		$se_i++;
	}
	if(!$hit){&error("�󂯎��鐶�Y��������܂���B$back_form");}

	open(OUT,">seisanmati.cgi");
	print OUT @seisanmati_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�}�X�^�[</B><BR>
�u���Y�i���󂯎������<br>
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub syoutyou {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	open(IN,"datalog/guest.dat");
	@guest_data = <IN>;
	close(IN);
	$hit=0;$i=0;$ct="";
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){$hit=1;last;}
		$i++;
	}
	if($hit!=1 or $array[1] ne $chara[4]){
		&error("�G���[�����B�M���h�ɏ������Ă��Ȃ����A�M���}�X�ł͂���܂���B");
	}else{
	
		&header;

		print <<"EOM";
<form action="g_b.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="select">
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>���O</th><th>���x��</th></tr>
EOM
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
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
			$guhit=0;
			foreach(@guest_data){
				@guests = split(/<>/);
				if($mem[4] eq $guests[1]){$guhit=1;last;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				$ht=1;
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
		print <<"EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>���O</th><th>���x��</th></tr>
<tr><td><input type="radio" name="mem1" value=$chara[4]></td>
EOM
if($chara[70]<1){$sou=$chara[18]+$chara[37]*100;}
else{$sou=$chara[18];}
if($chara[70]<1){
	print "<td>$chara[4]</td><td>$sou</td></tr>";
}else{
	print "<td><font color=\"yellow\">$chara[4]</font></td><td>$sou</td></tr>";
}
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
		$battle_mem_num = @battle_mem;
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
			$guhit=0;
			foreach(@guest_data){
				if($mem[4] eq $_){$guhit=1;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
		print <<"EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>���O</th><th>���x��</th></tr>
<tr><td><input type="radio" name="mem1" value=$chara[4]></td>
EOM
if($chara[70]<1){$sou=$chara[18]+$chara[37]*100;}
else{$sou=$chara[18];}
if($chara[70]<1){
	print "<td>$chara[4]</td><td>$sou</td></tr>";
}else{
	print "<td><font color=\"yellow\">$chara[4]</font></td><td>$sou</td></tr>";
}
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
		$battle_mem_num = @battle_mem;
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
			$guhit=0;
			foreach(@guest_data){
				if($mem[4] eq $_){$guhit=1;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
	}
	print <<"EOM";
</table>
</td>
</tr>
</table>
EOM
if($ht!=1){
	print "���݃��O�C�����Ă���M���h�����o�[�����܂���";
}else{
	print <<"EOM";
<input type=submit class=btn value="�Z���N�g">
EOM
}
	print <<"EOM";
</form>
<form action="g_b.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�߂�">
</form>
EOM

	&footer;

	exit;
}