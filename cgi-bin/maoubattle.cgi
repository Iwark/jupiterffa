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
require 'item.pl';
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
sub maou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&item_load;

	&acs_add;

	$place=98;
	
	open(IN,"data/maou.ini");
	@MONSTER = <IN>;
	close(IN);
	$r_no = @MONSTER;
	$kazu=2;

	&mons_read;

	open(IN,"./ancd.cgi");
	$member1_data = <IN>;
	close(IN);
	@mem1 = split(/<>/,$member1_data);
	$member=2;
	open(IN,"./ancditem.cgi");
	$mem1item_log = <IN>;
	close(IN);
	@mem1item = split(/<>/,$mem1item_log);

	$khp_flg = $chara[15];
	$mem1hp_flg = $mem1[15];
	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem1hp = $smem1hp_flg;

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();

	while($i<=$turn) {

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

	&seigi_sentoukeka;
	
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

sub seigi_sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($chara[55]==62 or $chara[56]==62 or $chara[57]==62 or $chara[58]==62)
		{$ygold = $i * int(rand($mgold/10));}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + $ygold + int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
		$chara[128] = 2;
		$comment = "<b><font color=yellow size=5>$chara[4]�̓A���N�h�����Ƌ��ɑ�R��喂������������I</font></b><br>";

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		$chmes="$chara[4]�l����R��喂���𓢔����܂����I";
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		unshift(@chat_mes,"<><font color=\"yellow\">���m</font><>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$chmes</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	} else {
		$mex = 1;
		$chara[28] = $bossd;
		$chara[19] = int(($chara[19] / 2));
		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
		if($khp_flg<=0){$mex= int($mex/10);}
		$chara[17] = $chara[17] + $mex;
		$imex = $mex*int(rand(10)+1);
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
}