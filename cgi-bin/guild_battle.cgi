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
require 'battle.pl';
# �����X�^�[��p���C�u����
require 'mbattle.pl';

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

&$mode;

exit;

#----------------------#
#  �����X�^�[�Ƃ̐퓬  #
#----------------------#
sub guild_battle {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&guest_list;

	if (!$chara[25]) {
		&error("��x�L�����N�^�[�Ɠ����Ă�������");
	}
	if($chara[63]>=1){&error("�������ł��I�I");}
	$koutime=time();
	$kankaku = $chara[144] - $koutime + 600;
	if($kankaku<int(rand(300))){&error("�N�[���^�C���B��x�X�e�[�^�X��ʂɖ߂�܂��傤�B");}

	$chara[139]++;
	if(int(rand(200))==0){$chara[139]=251;}
	if($chara[139] > 200){
		&error("��x�`�����v�Ɠ����Ă�������");
	}
	if($chara[18] > 500 and int(rand(200))==0){
		&error("�ŋߊ撣���Ă�ł���H");
	}
	$ntime = time();
	$b_time = $m_time;
	$ztime = $ntime - $chara[27];
	$ztime = $b_time - $ztime;

	if ($ztime > 0) { &mons_error; }

	&time_check;

	&item_load;

	&acs_add;
	if ($in{'guild_file'} eq "guild0"){$place = 33;}
	if ($in{'guild_file'} eq "guild1"){$place = 34;}
	if ($in{'guild_file'} eq "guild2"){$place = 35;}
	if ($in{'guild_file'} eq "guild2" and $chara[18]<1000){&error("���x��������܂���");}
	if($chara[70]<1){$monster_file = "$in{'guild_file'}\_monster";}
	else{$monster_file = "$in{'guild_file'}\_2monster";}
	open(IN,"$$monster_file");
	@MONSTER = <IN>;
	close(IN);
	$r_no = @MONSTER;
	$kazu=3;
	if ($in{'guild_file'} eq "guild2"){$kazu = 5;}
	&mons_read;
	
	#�M���h�`�F�b�N
	if($chara[66]){
		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$hit=0;
		foreach(@member_data){
			s/\n//i;
			s/\r//i;
			($g_name,$gg_leader,$gg_exp,$gg_lv) = split(/<>/);
			@pre = split(/<>/,$_,8);
			@battle_mem = split(/<>/,$pre[7]);
			if($g_name eq $chara[66]){
				$battle_mem_num = @battle_mem;
				$ht=0;
				for($bgb=0;$bgb<$battle_mem_num;$bgb++){
					if($battle_mem[$bgb] eq $chara[0]){$ht=1;last;}
				}
				if(!$ht){$chara[66]="";}
				$battle_i=0;
				for($bab=0;$bab<10;$bab++){
					$battle_rand = int(rand($battle_mem_num));
					if($battle_mem[$battle_rand] ne $chara[0]){
						if($battle_i==0){
							if(int(rand(2))==0 and $battle_mem[0] ne $chara[0]){
								$gmem1=$battle_mem[0];$bab=0;$battle_i++;
							}
							else{$gmem1=$battle_mem[$battle_rand];$bab=0;$battle_i++;}
						}
						if($battle_i==1 and $gmem1 ne $battle_mem[$battle_rand]){$gmem2=$battle_mem[$battle_rand];$bab=0;$battle_i++;}
						if($battle_i==2 and $gmem1 ne $battle_mem[$battle_rand] and $gmem2 ne $battle_mem[$battle_rand]){$gmem3=$battle_mem[$battle_rand];$bab=0;$battle_i++;}
						$hit+=1;
					}
				}
				last;
			}
		}

		if($battle_i){
			$member=1;
			if($gmem1){
				$lock_file = "$lockfolder/$gmem1.lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$gmem1.cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$gmem1.lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				open(IN,"./item/$gmem1.cgi");
				$mem1item_log = <IN>;
				close(IN);
				@mem1item = split(/<>/,$mem1item_log);
				$member+=1;
			}
			if($gmem2){
				$lock_file = "$lockfolder/$gmem2.lock";
				&lock($lock_file,'ER');
				open(IN,"charalog/$gmem2.cgi");
				$member2_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$gmem2.lock";
				&unlock($lock_file,'ER');
				@mem2 = split(/<>/,$member2_data);
				open(IN,"./item/$gmem2.cgi");
				$mem2item_log = <IN>;
				close(IN);
				@mem2item = split(/<>/,$mem2item_log);
				$member+=1;
			}
			if($gmem3){
				$lock_file = "$lockfolder/$gmem3.lock";
				&lock($lock_file,'ER');
				open(IN,"charalog/$gmem3.cgi");
				$member3_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$gmem3.lock";
				&unlock($lock_file,'ER');
				@mem3 = split(/<>/,$member3_data);
				open(IN,"./item/$gmem3.cgi");
				$mem3item_log = <IN>;
				close(IN);
				@mem3item = split(/<>/,$mem3item_log);
				$member+=1;
			}
		}
	}

	$khp_flg = $chara[15];
	if($member>1){$mem1hp_flg = $mem1[15];}
	if($member>2){$mem2hp_flg = $mem2[15];}
	#if($member>3){$mem3hp_flg = $mem3[15];}

	if($on and $on==$place){
		$smem1hp_flg = $msp1;
		$smem2hp_flg = $msp2;
		$smem3hp_flg = $msp3;
		$smem4hp_flg = $msp4;
		$smem1hp = $maxhp1;
		$smem2hp = $maxhp2;
		$smem3hp = $maxhp3;
		$smem4hp = $maxhp4;
	}else{
		$smem1hp_flg = int(rand($mrand1)) + $msp1;
		$smem2hp_flg = int(rand($mrand2)) + $msp2;
		$smem3hp_flg = int(rand($mrand3)) + $msp3;
		$smem4hp_flg = int(rand($mrand4)) + $msp4;
		$smem1hp = $smem1hp_flg;
		$smem2hp = $smem2hp_flg;
		$smem3hp = $smem3hp_flg;
		$smem4hp = $smem4hp_flg;
	}

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();
	if($chara[20]<1 or $chara[20]>10){$chara[20] = 1;}
	else{$chara[20]= $chara[20]+ $chara[20]/10;}

	if($member<4){$turn=$turn2;}
	if($member==4){$turn=$turn3;}
	foreach(1..$turn) {
		
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
	if($chara[150]>0 and $win==1){
		$chara[150]=$chara[150] - int(rand($gg_lv/100)) - 1;
		if($chara[150]<0){$chara[150]=0;}
		if($chara[150]==0){
			$comment.="<br><font color=\"red\" size=4><B>�P���Ŏ󂯂��_���[�W���S���������B</B></font>"
		}else{
			$comment.="<br><font color=\"red\" size=4><B>�P���Ŏ󂯂��_���[�W�E�E�E�c��$chara[150]</B></font>"
		}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B><br>�o�g���I</B></FONT>
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

	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);
	$gnnt="<option value=\"\">�����₫\n";
	foreach(@guest){
		($gtt,$gnn,$gii) = split(/<>/);
		$gnnt.="<option value=\"$gnn\">$gnn�����\n";
	}

       print <<"EOM";
<center><hr width=400>
<font color=red><B>�܂��퓬�ł��܂���I</B></font><br>
<FORM NAME= "form1">
����<INPUT TYPE= "text" NAME= "clock" SIZE= "3">�b�҂��ĉ�����
</FORM>

<form action= "guild_battle.cgi" method= "POST">
<input type= "hidden" name= "mode" value= "guild_battle">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type="hidden" name="guild_file" value="$in{'guild_file'}">
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
<FORM action="menu.cgi"  target="chat" onSubmit="setTimeout(function(){return aaa(this)},10)">
<table border=0 align="center" width='100%'><tr>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="name" value="$chara[4]">
<input type="hidden" name="level" value="$chara[18]">
<input type="hidden" name="chattime" value="1">
<input type="hidden" name="chan" value="$chara[96]">
<input type="hidden" name="chan2" value="$chara[180]">
��A�`�����l���g�p�F�@<INPUT TYPE="radio" NAME="tch2" VALUE="$chara[96]">ON
<INPUT TYPE="radio" NAME="tch2" VALUE="" checked>OFF
�@�A<INPUT TYPE="radio" NAME="tch3" VALUE="$chara[180]">ON
<INPUT TYPE="radio" NAME="tch3" VALUE="" checked>OFF
�@<select name="sasayaki">$gnnt</select>
<td align="left"><input type="submit" class=btn value="�������X�V">
<INPUT type="text" value="" name="mes" size="100" maxlength="60">�@�@
<INPUT type="text" value="" name="tch" size="3" maxlength="3">ch</td>
</tr>
<tr></FORM>
<td align="left" class="b2">
<iframe src="menu.cgi" width="100%" height="240" frameborder="0" name="chat" allowtransparency="true" scrolling="yes"></iframe>
</td></tr></table>
EOM

	&footer;

	exit;

}