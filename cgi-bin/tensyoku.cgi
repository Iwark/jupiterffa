#!/usr/bin/perl --

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͂����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@edit by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# syoku_regist�Ăяo��
require 'battle.pl';

# shopfooter�Ăяo��
require 'item.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# �]���ɕK�v�ȗ����̔{��(�]���񐔁~�H���{)
$tenseibairitu = 50;

# �]���ɕK�v�ȃ��x���̐ݒ�
$tenseilevel = 100;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if ($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="$script_tensyoku" method="post">
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

if ($mode) { &$mode; }
&tensyoku;

exit;

#------------#
# �]�E�̐_�a #
#------------#
sub tensyoku {

	&chara_load;

	&chara_check;

	&syoku_load;

	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

$mitensyoku.="���ݓ]�E�ł���܂��}�X�^�[���Ă��Ȃ��E�Ƃ�<br><table><tr>";
$tensyokuok.= "���ݓ]�E�ł���E�Ƃ�<br><table><tr>";

	$i=0;$hit=0;$mhit=0;
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		($ten) = split(/<>/);
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		if($chara[37] >= $ten){
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {
		$tensyokuok.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
		$selection.="<option value=\"$i\">$chara_syoku[$i]</option>\n";
		$hit+=1;
			if($hit % 5 == 0){$tensyokuok.="</tr><tr>";}
			if ($syoku_master[$i] < 100) {
				$mitensyoku.="<td><font color=white size=3>\[$chara_syoku[$i]\]</font></td>";
				$mhit+=1;
				if($mhit % 5 == 0){$mitensyoku.="</tr><tr>";}

			}
		}
		}
		$i++;
	}
	if(!$hit) { $tensyokuok.= "<td>����܂���</td>"; }
	if(!$mhit) { $mitensyoku.="<td>����܂���</td>"; }

	&header;

	$tensyokuryoukin = $chara[37] * 500000;

	print <<"EOM";
<h1>�]�E�̐_�a</h1><hr>
�����ł͓]�E���ł��܂��B�]�E����ɂ�$tensyokuryoukin G�ƃ��x��$tenseilevel���K�v�ł��B<br>
�� �]�E����ƃ��x����1�ɂȂ�A�o���l�E�\\�͒l�����Z�b�g����܂��B<br>
�����͓]�E�Ɠ]���̉񐔁~50��G�ł��B�X�e�[�^�X�|�C���g���]�E�Ɠ]���̉񐔁~20�|�C���g�����܂��B<br>
$tensyokuok</tr></table><br>
$mitensyoku</tr></table><br>
<form action="$script_tensyoku" method="post">
<select name=syoku>
<option value="no">�I�����Ă�������
$selection
</select>
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[21]) {
		print "�������ł��B\n";
	}elsif ($chara[19]<$tensyokuryoukin) {
		print "����������܂���B\n";
	}elsif($chara[18]>=$tenseilevel) {
		print "<input type=\"submit\" class=btn value=\"�]�E����\">\n";
	}else{
		print "���x��������܂���B\n";
	}
	
	print <<"EOM";
</form>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#--------#
#  �]�E  #
#--------#
sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'syoku'} eq 'no') {
		&error("�E�Ƃ�I�����Ă��������B$back_form");
	}

	$tensyokuryoukin = $chara[37] * 500000;

	if($chara[19] < $tensyokuryoukin){&error("����������܂���$back_form");}
	else{$chara[19] -= $tensyokuryoukin;}
	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$syoku_master[$chara[14]] = $chara[33];

	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;

	$chara[14] = $in{'syoku'};
	if ($master_tac) { $chara[30] = 0; }	# �]�E��̐�p�N���A
	$chara[33] = $syoku_master[$chara[14]];

	if (!$chara[33]) { $chara[33] = 1; }

		$chara[16] = $kiso_hp + int(rand($chara[37]*100));
		$chara[15] = $chara[16];
		$chara[17] = 0;
		$chara[18] = 1;
		$chara[37] += 1;
		$chara[35] = 20 * $chara[37];
		$chara[7] = 1;
		$chara[8] = 1;
		$chara[9] = 1;
		$chara[10] = 1;
		$chara[11] = 1;
		$chara[12] = 1;
		$chara[13] += 1;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;
	$year = $year +1900;

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$boss="$chara[4]�l��$chara_syoku[$chara[14]]�ɓ]�E���܂���";
	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$boss</span>";

	unshift(@CLOG,"kokuti<>���m<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<>$boss<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	print <<"EOM";
<h1>$chara_syoku[$chara[14]]�ɓ]�E���܂���</h1><hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
