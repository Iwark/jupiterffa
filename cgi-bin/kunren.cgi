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

require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

require 'mbattle.pl';

require 'battle.pl';

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
<form action="kunren.cgi" >
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

&haigo;

&error;

exit;

#----------#
#  �z����  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�P����</h1>
<hr size=0>
<FONT SIZE=3>
<B>�P�����̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�����ł́A����񂾋M�l�̍�����@���Ȃ����Ă�邺���B<br>
�����Ő�������Ō�A�M�l�̗͉̑͂񕜕s\�\\�Ȃ܂łɃ_���[�W�𕉂����낤���Ȃ��B<br>
�܁A���̑��蓾����̂͑������낤���c�B<br>
�����Ŏ󂯂��_���[�W�͓���ȉ񕜖@���K�v���B<br>
�Ƃ肠�����񕜑������̓M���h�ɉ������邱�Ƃ��ȁB�v
</FONT>
EOM

if($chara[150]>0 and $chara[0] ne "jupiter"){print "�O��̌P���̃_���[�W���񕜂��Ă��܂���B";}
else{
print <<"EOM";
<form action="./kunren.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=kunren>
<input type=submit class=btn value="�P���ɒ���">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub kunren {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if($chara[150]>0 and $chara[0] ne "jupiter"){&error("�O��̌P���̃_���[�W���񕜂��Ă��܂���B");}
	if($chara[70]<1){&error("���E�˔j�Ґ�p�{�݂ł��B");}

	$chara[150]=10;

	&item_load;

	&acs_add;

	if($chara[18]<150){$kunren_monster="kunren_monster1";}
	elsif($chara[18]<200){$kunren_monster="kunren_monster2";}
	elsif($chara[18]<250){$kunren_monster="kunren_monster3";}
	else{$kunren_monster="kunren_monster4";}

	open(IN,"$$kunren_monster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$kazu=5;

	&mons_read;

	$khp_flg = $chara[15];

	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem2hp_flg = int(rand($mrand2)) + $msp2;
	$smem3hp_flg = int(rand($mrand3)) + $msp3;
	$smem4hp_flg = int(rand($mrand4)) + $msp4;
	$smem1hp = $smem1hp_flg;
	$smem2hp = $smem2hp_flg;
	$smem3hp = $smem3hp_flg;
	$smem4hp = $smem4hp_flg;
	
	if($chara[24]==9999 or $chara[24]==0){$sudedmg=1;}

	$i=1;
	$j=0;@battle_date=();
	$place = 29;
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

	if ($win==1) {
 		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I</font></b><br>";
		&quest;
	} elsif ($win==2) {
		$comment .= "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}

	&acs_sub;

	if($win==1){
		$jup=int(rand(4));
		$comment.= <<"EOM";
		<FONT SIZE=4 color="red">
		<B>�W���u���x����$jup�オ��܂����B</B><BR>
		<hr size=0>
EOM
		$klvbf=$chara[33];
		$chara[33] += $jup;
		#�W���u�}�X�^�[�̏���
		if ($chara[33] > 99 && $klvbf <=99) {
			$comment .= "<font class=red size=5>$chara_syoku[$chara[14]]���}�X�^�[�����I�I</font><br>";
			$lock_file = "$lockfolder/syoku$in{'id'}.lock";
			&lock($lock_file,'SK');
			&syoku_load;

			$syoku_master[$chara[14]] = 100;

			&syoku_regist;
			&unlock($lock_file,'SK');
		}
		if ($chara[33] > 100) { $chara[33]=100; }

		$chara[15] = $chara[16];
	}
		
	if(int(rand(5))<2){
		$comment.= <<"EOM";
		<FONT SIZE=4 color="red">
		<B>����t�P�����ĊF���猩�����ꂽ�B�P�l�x���P�オ�����B</B><BR>
		<hr size=0>
EOM
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$chara[64]+=1;
		$chara[65]-=1;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[64]>100){$chara[64]=100;}
		if($chara[65]<0){$chara[65]=0;}
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>�P����</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">�o�g���I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	print "$comment<br>\n";
	print <<"EOM";
<form action="$script" >
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
	&footer;

	exit;
}