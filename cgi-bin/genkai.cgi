#!/usr/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
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
<form action="genkai.cgi" >
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

	$hit=0;
	foreach (@syoku_master) {if($_ >= 100){$hit++;}}

	&header;

	print <<"EOM";
<h1>���E�˔j</h1><hr>
���E�˔j�̏����F<br>
�@�P�W�̃W���u���}�X�^�[���Ă��邱�ƁB<br>
�A��ꓢ���N�G�X�g���N���A���Ă��邱�ƁB<br>
�B�R�̌���L���Ă��邱�ƁB<br>
<font color="red" size=4>
���E�˔j������ƁA�V���Ȏ{�݁E�V�X�e���E�E�ƂȂǂ���R����܂��B<br>
�S���V�����v���C���邪���Ƃ��A���x����E�ƂȂǂ̓��Z�b�g�����̂Œ��ӂ��Ă��������B<br>
</font><br>
<form action="genkai.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tensyoku_change">
EOM

	if (!$chara[131] or !$chara[132] or !$chara[133]) {
		print "�R�̌���L���Ă��܂���B\n";
	}elsif ($chara[127]!=2) {
		print "��ꓢ���N�G�X�g���N���A���Ă��܂���B\n";
	}elsif($hit < 18) {
		print "�P�W�̃W���u���}�X�^�[���Ă��܂���B$hit\n";
	}else{
		print "<input type=\"submit\" class=btn value=\"���E�˔j\">\n";
	}
	
	print <<"EOM";
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
#------------#
# ���E�˔j�@ #
#------------#
sub tensyoku_change {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;
#-----------------------------------------------------�����𖞂����Ă��邩�`�F�b�N
	if($tenseiryoukin>$chara[19]){&error("�����𖞂����Ă��܂���B");}
#-----------------------------------------------------�E�ƃf�[�^�̏���
	$lock_file = "$lockfolder/syoku$in{'id'}.lock";
	&lock($lock_file,'SK');
	&syoku_load;

	$num = @syoku_master;

	for($i=0;$i<=$num;$i++){
		$syoku_master[$i] = 0;
	}
	&syoku_regist;
	&unlock($lock_file,'SK');

	&get_host;
#-----------------------------------------------------�A�C�e���E�y�b�g�̏���
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&item_lose;

	&def_lose;

	&acs_lose;

	&pet_lose;

	&souko_lose;

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[61]){
			if($array[5] eq $chara[0] and $array[6]){
				$lock_file = "$lockfolder/$array[6].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[6].cgi");
				$member2_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[6].lock";
				&unlock($lock_file,'DR');
				@mem2 = split(/<>/,$member2_data);
				$array[1]=$mem2[4];
				$solv=$mem2[18]+$mem2[37]*100;
				$array[2]=$solv;
				$array[3]-=1;
				splice(@array,5,1);
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}elsif($array[5] eq $chara[0]){
				splice(@member_data,$i,1);
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
			elsif($array[6] eq $chara[0]){splice(@array,6,1);$hit=1;}
			elsif($array[7] eq $chara[0]){splice(@array,7,1);$hit=1;}
			if($hit){
				$array[3]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array =~ s/\n//;
				$new_array .= "\n";
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}

	&item_regist;
	&unlock($lock_file,'IM');

#-----------------------------------------------------�X�e�[�^�X���Z�b�g
	if ($chara[33]) {
		$chara[16] = $kiso_hp;
		$chara[15] = $chara[16];
		$chara[17] = 0;
		$chara[18] = 1;
		$chara[19] = 1;
		$chara[24] = 0;
		$chara[29] = 0;
		$chara[31] = 0;
		$chara[34] = 0;
		$chara[37] = 0;
		$chara[35] = 20;
		$chara[51] = 0;
		$chara[52] = 0;
		$chara[53] = 0;
		$chara[54] = 0;
		$chara[55] = 0;
		$chara[56] = 0;
		$chara[57] = 0;
		$chara[58] = 0;
		$chara[59] = 0;
		$chara[61] = "";
		$chara[97] = "";
		$chara[98] = "";
		$chara[99] = "";
		$chara[100] = "";
		$chara[7] = 1;
		$chara[8] = 1;
		$chara[9] = 1;
		$chara[10] = 1;
		$chara[11] = 1;
		$chara[12] = 1;
		$chara[13] = 4;
		$chara[70] = 1;
		$chara[14]=18;
		$chara[33] = 1;
		$chara[140] = 0;
		$chara[71] = 0;
		$chara[72] = 0;
		$chara[73] = 0;
		$chara[74] = 0;
		$chara[75] = 0;
		$chara[76] = 0;
		$chara[77] = 0;
		$chara[78] = 0;
		$chara[79] = 0;
		$chara[80] = 0;
		$chara[81] = 0;
		$chara[82] = 0;
	}
#-----------------------------------------------------���m
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

	$boss="<font color=\"yellow\">$chara[4]�l�����E�˔j��$chara_syoku[$chara[14]]�ƂȂ�A�n�[�h���[�h�Ɉڍs���܂����B</font>";
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
#-----------------------------------------------------���W�X�g�E�w�b�_�[
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	
#-----------------------------------------------------�\��
	print <<"EOM";
<h1> ���E�˔j���܂����B</h1><hr size=0><br>
<form action="$script" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&shopfooter;

	&footer;

	exit;
}
