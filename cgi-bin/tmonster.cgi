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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

require 'sankasya.pl';

# �퓬���C�u�����̓ǂݍ���
require 'tbattle.pl';
# �����X�^�[��p���C�u����
require 'tmbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

if ($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

# ���̃t�@�C���p�ݒ�
$temp_back = "$mode\_back";
$temp_midi = "$mode\_midi";
$backgif = $$temp_back;
$midi = $$temp_midi;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");
	}
}
if($mode == 1){&monster;}
else{&$mode;}

exit;

#----------------------#
#  �����X�^�[�Ƃ̐퓬  #
#----------------------#
sub monster {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&guest_list;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	$ntime = time();
	$b_time = $m_time;
	$ztime = $ntime - $chara[27];
	$ztime = $b_time - $ztime;

	if ($ztime > 0) { &mons_error; }

	&time_check;

	&item_load;

	&acs_add;

	if ($in{'tmons_file'} eq "monster0"){$place = 0;}
	if ($in{'tmons_file'} eq "monster1"){$place = 1;}
	if ($in{'tmons_file'} eq "monster2"){$place = 2;}
	if ($in{'tmons_file'} eq "monster3"){$place = 3;}
	if ($in{'tmons_file'} eq "monster4"){$place = 4;}
	if ($in{'tmons_file'} eq "monster5"){$place = 5;}
	if ($in{'tmons_file'} eq "monster6"){$place = 6;}
	if ($in{'tmons_file'} eq "monster7"){$place = 7;}
	if ($in{'tmons_file'} eq "monster8"){$place = 8;}
	if ($in{'tmons_file'} eq "monster9"){$place = 9;}
	if ($in{'tmons_file'} eq "monster10"){$place = 10;}
	if ($in{'tmons_file'} eq "monster12"){$place = 12;}
	if ($in{'tmons_file'} eq "monster27"){$place = 27;}

	#�{�X�����邩�`�F�b�N

	open(IN,"./data/bosson.ini");
	@bosson_data = <IN>;
	close(IN);
	foreach(@bosson_data){
		($name,$on) = split(/<>/);
		if($on){
			if($on==$place){
				#�{�X�L����
				open(IN,"$boss_monster");
				@MONSTER = <IN>;
				close(IN);
				last;
			}	
		}
	}
	if($on and $on==$place){}
	else{
		if($chara[70]!=1){$monster_file = "$in{'tmons_file'}\_monster";}
		else{$monster_file = "$in{'tmons_file'}\_2monster";}
		open(IN,"$$monster_file");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		if($place==0){$kazu=2;}
		elsif($place==1){$kazu=3;}
		elsif($place==2){$kazu=3;}
		elsif($place==3){$kazu=3;}
		elsif($place==4){$kazu=4;}
		elsif($place==5){$kazu=4;}
		elsif($place==6){$kazu=5;}
		elsif($place==7){$kazu=5;}
	}

	&mons_read;
	#�����̃����o�[����
	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data){
		($pp_name,$pp_leader,$pp_lv,$pp_mem,$pp_com,$pp_mem1,$pp_mem2,$pp_mem3) = split(/<>/);
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,6);
		@battle_mem = split(/<>/,$pre[5]);
		if($pp_name eq $chara[61]){
			if($pp_mem1 eq $chara[0]){
				$pmem1=$pp_mem2;
				$pmem2=$pp_mem3;
			}
			elsif($pp_mem2 eq $chara[0]){
				$pmem1=$pp_mem1;
				$pmem2=$pp_mem3;
			}
			elsif($pp_mem3 eq $chara[0]){
				$pmem1=$pp_mem1;
				$pmem2=$pp_mem2;
			}
			$lock_file = "$lockfolder/$pmem1.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pmem1.cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pmem1.lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);

			$lock_file = "$lockfolder/$pmem2.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pmem2.cgi");
			$member2_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pmem2.lock";
			&unlock($lock_file,'DR');
			@mem2 = split(/<>/,$member2_data);

			$member=1;
			if($pmem1){
				open(IN,"./item/$pmem1.cgi");
				$mem1item_log = <IN>;
				close(IN);
				@mem1item = split(/<>/,$mem1item_log);
				$member+=1;
			}
			if($pmem2){
				open(IN,"./item/$pmem2.cgi");
				$mem2item_log = <IN>;
				close(IN);
				@mem2item = split(/<>/,$mem2item_log);
				$member+=1;
			}
		}
	}
	
	$khp_flg = $chara[15];
	if($member>1){
		$ze = $mem1[37] * 100 + $mem1[18];
		$zee = $chara[37] * 100 + $chara[18];
		if($ze < $zee + 300 and $ze > $zee - 300){$mem1hp_flg = $mem1[15];}
	}
	if($member>2){
		$ze = $mem2[37] * 100 + $mem2[18];
		$zee = $chara[37] * 100 + $chara[18];
		if($ze < $zee + 300 and $ze > $zee - 300){$mem2hp_flg = $mem2[15];}
	}
	if($chara[42]){
		$mem3hp_flg = $chara[42];
	}
	if($on and $on==$place){$smem1hp_flg = $msp1;}
	else{$smem1hp_flg = int(rand($mrand1)) + $msp1;}
	if($on and $on==$place){$smem1hp = $maxhp1;}
	else{$smem1hp = $smem1hp_flg;}
	if($on and $on==$place){$smem2hp_flg = $msp2;}
	else{$smem2hp_flg = int(rand($mrand1)) + $msp2;}
	if($on and $on==$place){$smem2hp = $maxhp2;}
	else{$smem2hp = $smem2hp_flg;}
	if($on and $on==$place){$smem1hp_flg = $msp3;}
	else{$smem3hp_flg = int(rand($mrand3)) + $msp3;}
	if($on and $on==$place){$smem3hp = $maxhp3;}
	else{$smem3hp = $smem3hp_flg;}
	if($on and $on==$place){$smem4hp_flg = $msp4;}
	else{$smem4hp_flg = int(rand($mrand4)) + $msp4;}
	if($on and $on==$place){$smem4hp = $maxhp4;}
	else{$smem4hp = $smem4hp_flg;}

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();
	if($chara[20]<1 or $chara[20]>10){$chara[20] = 1;}
	else{$chara[20]= $chara[20]+ $chara[20]/10;}

	if($member==2){$turn=$turn2;}
	if($member==3){$turn=$turn3;}
	while($i<=30) {
		
		&shokika;

		&tyousensya;

		&tyosenwaza;
		&mons_waza;

		&acs_waza;
		&mons_atowaza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;
	
	&acs_sub;

	&hp_after;

	&levelup;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><br><B>�o�g���I</B></FONT>
EOM
	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

#----------------------#
#  ���e�̏�̐퓬      #
#----------------------#
sub genei {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	&time_check;

	if ($chara[27]%5 != 0) {
		&error("���������Ă��܂��čs���܂���ł���");
	}

	&item_load;

	&acs_add;

	if($chara[70]!=1){
		if ($chara[18] < $genei_low) {$monster_file=$monster0_monster;}
		elsif ($chara[18] < $genei_normal) {$monster_file=$monster1_monster;}
		elsif ($chara[18] < $genei_mid) {$monster_file=$monster2_monster;}
		elsif ($chara[18] < $genei_high) {$monster_file=$monster3_monster;}
		elsif ($chara[18] < $genei_dark) {$monster_file=$monster4_monster;}
		else {$monster_file=$monster5_monster;}
	}else{
		if ($chara[18] < $genei_low * 10) {$monster_file=$monster0_2monster;}
		elsif ($chara[18] < $genei_normal * 10) {$monster_file=$monster1_2monster;}
		elsif ($chara[18] < $genei_mid * 10) {$monster_file=$monster2_2monster;}
		elsif ($chara[18] < $genei_high * 10) {$monster_file=$monster3_2monster;}
		elsif ($chara[18] < $genei_dark * 10) {$monster_file=$monster4_2monster;}
		else {$monster_file=$monster5_monster;}
	}

	$place = 20;

	open(IN,"$monster_file");
	@MONSTER = <IN>;
	close(IN);
	$r_no = @MONSTER;
	$r_no = int(rand($r_no));

	$on=0;
	&mons_read;

	$khp_flg = $chara[15];
	$php_flg = $chara[42];
	$mhp = int(rand($mrand)) + $msp * 2;
	$mhp_flg = $mhp;

	$i=1;
	$j=0;@battle_date=();

	foreach(1..$turn) {

		&shokika;

		$dmg2 += $item[4];

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	if ($win == 1) {
		if (int(rand(3)) == 0) {
			$otakara = int(rand(100)+1) * int($mgold);
			$chara[19] += $otakara;
			$comment .= "<b><font size=5 color=red>����($otakara�f)�𔭌������I�I�I�I</font></b><br>";
		} else {
			$comment .= "<b><font size=5>�ӂ�ɍ���͌�����Ȃ������E�E�E�B</font></b><br>";
		}
	}

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>���e�̏�</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">$mname</B>�����ꂽ�I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}
	
	&mons_footer;

	&footer;

	exit;
}

#----------------------#
#  �ِ��E�ł̐퓬      #
#----------------------#
sub isekiai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}

	&time_check;

	&item_load;

	&acs_add;

	open(IN,"$isekai_monster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$r_no = int(rand($r_no));

	&mons_read;

	$khp_flg = $chara[15];
	$php_flg = $chara[42];
	$mhp = int(rand($mrand)) + $msp;
	$mhp_flg = $mhp;

	$i=1;
	$j=0;@battle_date=();
	$place = 21;
	foreach(1..$turn) {
		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&hp_after;

	&sentoukeka;

	&acs_sub;

	&levelup;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>�ِ��E</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">$mname</B>�����ꂽ�I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

#----------------#
#  �҂����ԕ\��  #
#----------------#
sub mons_error {

	foreach (keys %lock_flg) {
		if ($lock_flg{$_}) {
			if ($lockkey == 3) {
				foreach (@flock) {
					($flock_pre,$flock_file) = split(/,/);
					if ($flock_file eq $_) {
						last;
					}
				}
			}
			&unlock($_,$flock_pre);
		}
	}

	&header;

	&time_view;

       print <<"EOM";
<center><hr width=400>
<font color=red><B>�܂��퓬�ł��܂���I</B></font><br>
<FORM NAME= "form1">
����<INPUT TYPE= "text" NAME= "clock" SIZE= "3">�b�҂��ĉ�����
</FORM>

<form action= "tmonster.cgi" method= "POST">
<input type= "hidden" name= "mode" value= "monster">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type="hidden" name="tmons_file" value="$in{'tmons_file'}">
<input type= "submit" class= "btn" value= "����ɓ���">
</form>
<form action= "$script" method= "POST">
<input type= "hidden" name= "mode" value= "log_in">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type= "submit" class= "btn" value= "�X�e�[�^�X��ʂ�">
</form>
</center>
<hr width=400>
<script>
function aaa(fm){ 
fm.mes.value="";
fm.mes.focus(); 
return false; 
}
</script>

<FORM action="chat.cgi" method="POST" target="chat" onSubmit="setTimeout(function(){return aaa(this)},10)">
<table border=0 align="center" width='100%'><tr>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="name" value="$chara[4]">
<input type="hidden" name="level" value="$chara[18]">
<input type="hidden" name="chattime" value="1">
<td align="left"><input type="submit" class=btn value="�������X�V">
<INPUT type="text" value="" name="mes" size="100" maxlength="60">�@�@
<INPUT type="text" value="" name="tch" size="3" maxlength="3">ch</td>
</tr>
<tr></FORM>
<td align="left" class="b2">
<iframe src="chat.cgi" width="100%" height="240" frameborder="0" name="chat" allowtransparency="true" scrolling="yes"></iframe>
</td></tr></table>
EOM

	&footer;

	exit;

}