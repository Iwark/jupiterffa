#!/usr/bin/perl

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
#------------------------------------------------------#
# �]���̐_�a edit by ���J
# http://cgi-games.com/drop/
#------------------------------------------------------#
#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B         #
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B       #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B       #
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
$tenseibairitu = 100;

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
<form action="tensei.cgi" method="post">
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

$mitensyoku.="���ݓ]���ł���܂��}�X�^�[���Ă��Ȃ��E�Ƃ�<br><table><tr>";
$tensyokuok.= "���ݓ]���ł���E�Ƃ�<br><table><tr>";

	$i=0;$hit=0;$mhit=0;
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
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
		$i++;
	}
	if(!$hit) { $tensyokuok.= "<td>����܂���</td>"; }
	if(!$mhit) { $mitensyoku.="<td>����܂���</td>"; }

	&header;

	if (!$chara[37]) { $chara[37] = 0; }
	$tenseiryoukin = 1000000 * $chara[37];

	print <<"EOM";
<h1>�]���̐_�a</h1><hr>
�����ł͓]�����ł��܂��B�]������ɂ�$tenseiryoukin\G�ƃ��x����$tenseilevel�K�v�ł��B<br>
�� �]������ƃ��x����1�ɂȂ�A�o���l�E�\\�͒l�����Z�b�g�A�E�Ƃ������_���ɕς��܂��B<br>
�����͓]�E�Ɠ]���̉񐔁~100��G�ł��B�X�e�[�^�X�|�C���g���]�E�Ɠ]���̉񐔁~20�|�C���g�����܂��B<br>
EOM
if($chara[70]<1){
	print <<"EOM";
$tensyokuok</tr></table><br>
$mitensyoku</tr></table><br>
EOM
}
	print <<"EOM";
<form action="tensei.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[21]) {
		print "�������ł��B\n";
	}elsif ($chara[19]<$tenseiryoukin) {
		print "����������܂���B\n";
	}elsif ($chara[70]>=2) {
		print "�]���ł��܂���B\n";
	}elsif($chara[18]>=100 and $chara[33]>=100) {
		print "<input type=\"submit\" class=btn value=\"�]������\">\n";
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

sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$tenseiryoukin = 1000000 * $chara[37];

	if($chara[33]<$tenseilevel) {&error("���x��������܂���");}

	if($tenseiryoukin>$chara[19]){&error("����������܂���");}
	else{$chara[19] -= $tenseiryoukin;}

	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$syoku_master[$chara[14]] = $chara[33];

	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;

if($chara[70]!=1){
	open(IN,"$syoku_file");
	@syoku = <IN>;
	close(IN);

	$i=0;$hit=0;@ten_sei=();
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {$hit++;}
		$i++;
	}
}else{
	open(IN,"$syoku2_file");
	@syoku = <IN>;
	close(IN);

	$hit=0;
	foreach (@syoku) {
		if($chara[37] >= $_){$hit++;}
	}
}
	$ksyoku = int(rand($hit + 1));
if($chara[70]!=1){
	$hit=0;$i=0;@ten_sei=();
	foreach (@syoku) {
		s/\n//i;
		s/\r//i;
		@pre = split(/<>/,$_,2);
		@syoku_require = split(/<>/,$pre[1]);
		$is=0;
		$shit=0;
		foreach (@syoku_require) {
			if ($_ * 100 > $syoku_master[$is]) {$shit = 1;}
			$is++;
		}
		if (!$shit) {$hit++;}
		if($ksyoku == $hit){$chara[14]=$i;last;}
		$i++;
	}
}else{
	$hit=0;$i=0;
	foreach (@syoku) {
		$shit=0;
		if($chara[37] >= $_){
			if($chara[37] >= $_){$hit++;}
		}
		if($ksyoku == $hit){$chara[14]=$i;last;}
		$i++;
	}
}
	if ($master_tac) { $chara[30] = 0; }
	$chara[33] = $syoku_master[$chara[14]];

	if (!$chara[33]) { $chara[33] = 1; }

	if ($chara[33]) {
		if($chara[70]!=1){
			$chara[16] = $kiso_hp + int(rand($chara[37]*100));
			$chara[15] = $chara[16];
			$chara[17] = 0;
			$chara[18] = 1;
			$chara[35] = 20 * $chara[37];
			$chara[7] = 1;
			$chara[8] = 1;
			$chara[9] = 1;
			$chara[10] = 1;
			$chara[11] = 1;
			$chara[12] = 1;
		}
		$chara[37] += 1;
		$chara[13] += 1;
	}

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

	$boss="$chara[4]�l��$chara_syoku[$chara[14]]�ɓ]�����܂���";
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

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	
	$next_ex = $chara[18] * $lv_up;

	print <<"EOM";
<h1> �]�����I�����܂���</h1><hr size=0><br>
���x�� : $chara[18]<br>
�E�� : $chara_syoku[$chara[14]]<br>
�o���n : $chara[17] / $next_ex<br>
<form action="$script" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&shopfooter;

	&footer;

	exit;
}
