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

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) { &error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B"); }
&decode;

	$back_form = << "EOM";
<br>
<form action="./abilitychange.cgi" >
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

&senjutu;

exit;

#----------------#
#  ��p�\��      #
#----------------#
sub senjutu {

	&chara_load;

	&chara_check;

	$ahit=0;
	$bhit=0;
	$chit=0;
	$dhit=0;
	$ehit=0;
	$fhit=0;
	$ghit=0;
	$hhit=0;
	@dou_ability = "0<>1<>0<>�Ȃ�<>���A�r���e�B�Ȃ��Ő킢�܂�<>0<>\n";
	@sei_ability = "0<>0<>0<>�Ȃ�<>�ÃA�r���e�B�Ȃ��Ő킢�܂�<>0<>\n";

	# ���݂̐E�Ƃ̃A�r���e�B�ǂݍ���
	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		if (!$ks_ms || ($ks_ms && $chara[33] >= 100)) {
			#���A�r���e�B
			if($dousei==1){
				push(@dou_ability,"$_");
				if($chara[51] eq "$ks_no"){
					$ahit = 1;
					$nowdou1_tac = $ks_name;
					$nowdou1_tac_ex = $ks_plus;
				}
				if($chara[52] eq "$ks_no"){
					$bhit = 1;
					$nowdou2_tac = $ks_name;
					$nowdou2_tac_ex = $ks_plus;
				}
				if($chara[53] eq "$ks_no"){
					$chit = 1;
					$nowdou3_tac = $ks_name;
					$nowdou3_tac_ex = $ks_plus;
				}
				if($chara[54] eq "$ks_no"){
					$dhit = 1;
					$nowdou4_tac = $ks_name;
					$nowdou4_tac_ex = $ks_plus;
				}
			}
			#�ÃA�r���e�B
			if($dousei==0){
				push(@sei_ability,"$_");
				if($chara[55] eq "$ks_no"){
					$ehit = 1;
					$nowsei1_tac = $ks_name;
					$nowsei1_tac_ex = $ks_plus;
				}
				if($chara[56] eq "$ks_no"){
					$fhit = 1;
					$nowsei2_tac = $ks_name;
					$nowsei2_tac_ex = $ks_plus;
				}
				if($chara[57] eq "$ks_no"){
					$ghit = 1;
					$nowsei3_tac = $ks_name;
					$nowsei3_tac_ex = $ks_plus;
				}
				if($chara[58] eq "$ks_no"){
					$hhit = 1;
					$nowsei4_tac = $ks_name;
					$nowsei4_tac_ex = $ks_plus;
				}
			}
		}
	}

	#�}�X�^�[������p�̃C���N���[�h
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 100 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				foreach (@gettac){
				($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
				if($dousei==1){
					push(@dou_ability,"$_");
					if($chara[51] eq "$ks_no"){
						$ahit = 1;
						$nowdou1_tac = $ks_name;
						$nowdou1_tac_ex = $ks_plus;
					}
					if($chara[52] eq "$ks_no"){
						$bhit = 1;
						$nowdou2_tac = $ks_name;
						$nowdou2_tac_ex = $ks_plus;
					}
					if($chara[53] eq "$ks_no"){
						$chit = 1;
						$nowdou3_tac = $ks_name;
						$nowdou3_tac_ex = $ks_plus;
					}
					if($chara[54] eq "$ks_no"){
						$dhit = 1;
						$nowdou4_tac = $ks_name;
						$nowdou4_tac_ex = $ks_plus;
					}
				}
				if($dousei==0){
					push(@sei_ability,"$_");
					if($chara[55] eq "$ks_no"){
						$ehit = 1;
						$nowsei1_tac = $ks_name;
						$nowsei1_tac_ex = $ks_plus;
					}
					if($chara[56] eq "$ks_no"){
						$fhit = 1;
						$nowsei2_tac = $ks_name;
						$nowsei2_tac_ex = $ks_plus;
					}
					if($chara[57] eq "$ks_no"){
						$ghit = 1;
						$nowsei3_tac = $ks_name;
						$nowsei3_tac_ex = $ks_plus;
					}
					if($chara[58] eq "$ks_no"){
						$hhit = 1;
						$nowsei4_tac = $ks_name;
						$nowsei4_tac_ex = $ks_plus;
					}
				}
				}
			}
			$i++;
		}
	}

	if(!$ahit) {$nowdou1_tac = "�Ȃ�";$nowdou1_tac_ex = "���P�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$bhit) {$nowdou2_tac = "�Ȃ�";$nowdou2_tac_ex = "���Q�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$chit) {$nowdou3_tac = "�Ȃ�";$nowdou3_tac_ex = "���R�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$dhit) {$nowdou4_tac = "�Ȃ�";$nowdou4_tac_ex = "���S�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$ehit) {$nowsei1_tac = "�Ȃ�";$nowsei1_tac_ex = "�ÂP�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$fhit) {$nowsei2_tac = "�Ȃ�";$nowsei2_tac_ex = "�ÂQ�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$ghit) {$nowsei3_tac = "�Ȃ�";$nowsei3_tac_ex = "�ÂR�A�r���e�B�Ȃ��Ő킢�܂�";}
	if(!$hhit) {$nowsei4_tac = "�Ȃ�";$nowsei4_tac_ex = "�ÂS�A�r���e�B�Ȃ��Ő킢�܂�";}

	&header;

	print <<"EOM";
<h1>�A�r���e�B�`�F���W</h1>
�A�r���e�B�`�F���W���s���܂�<br>
���A�r���e�B�F�퓬���Ɉ��m���Ŕ���<br>
�ÃA�r���e�B�F��ɔ���<br>
�A�r���e�B�̓A�r���e�B�|�C���g�ɉ����ēo�^�ł��܂��B<br>
���F���@�������ɁA���̎�̖��@�����A�r���e�B���O���ƁA���ݑ������Ă��閂�@�������܂��B<br>
���݂̃A�r���e�B�|�C���g�F$chara[13]
<hr size=0>
<BR>
<form action="abilitychange.cgi" >
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">���݂̃A�r���e�B</td></tr>
<td class=b1>���O</td><td class=b1>�v���l</td><td class=b1>����</td>\n
<tr><td class=b1><input type=radio name=ab value="1">
���A�r���e�B�P</td><td class=b1>$nowdou1_tac</td><td class=b1>$nowdou1_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="2">
���A�r���e�B�Q</td><td class=b1>$nowdou2_tac</td><td class=b1>$nowdou2_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="3">
���A�r���e�B�R</td><td class=b1>$nowdou3_tac</td><td class=b1>$nowdou3_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="4">
���A�r���e�B�S</td><td class=b1>$nowdou4_tac</td><td class=b1>$nowdou4_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="5">
�ÃA�r���e�B�P</td><td class=b1>$nowsei1_tac</td><td class=b1>$nowsei1_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="6">
�ÃA�r���e�B�Q</td><td class=b1>$nowsei2_tac</td><td class=b1>$nowsei2_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="7">
�ÃA�r���e�B�R</td><td class=b1>$nowsei3_tac</td><td class=b1>$nowsei3_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="8">
�ÃA�r���e�B�S</td><td class=b1>$nowsei4_tac</td><td class=b1>$nowsei4_tac_ex</td>
</tr>
</td>
</tr>
</table>
</td>
EOM
	print <<"EOM";
<td valign="top">
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">���A�r���e�B</td></tr>
<tr>
<td class=b1></td><td class=b1>���O</td><td class=b1>�v���l</td><td class=b1>����</td>\n
EOM
	foreach(@dou_ability){
		($s_no,$s_dousei,$s_youkyu,$s_name,$s_plus,$s_ms) = split(/<>/);
		print "<tr>\n";
		print "<td class=b1><input type=radio name=senjutu_no value=\"$s_no\"></td><td class=b1>$s_name</td><td class=b1>$s_youkyu</td><td class=b1>$s_plus</td>\n";
		print "</tr>\n";
	}
	print <<"EOM";
</td>
</tr>
</table>
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">�ÃA�r���e�B</td></tr>
<tr>
<td class=b1></td><td class=b1>���O</td><td class=b1>�v���l</td><td class=b1>����</td>\n
EOM
	foreach(@sei_ability){
		($t_no,$t_dousei,$t_youkyu,$t_name,$t_plus,$t_ms) = split(/<>/);
		if($t_name){
			print "<tr>\n";
			print "<td class=b1><input type=radio name=senjutu_no value=\"$t_no\"></td><td class=b1>$t_name</td><td class=b1>$t_youkyu</td><td class=b1>$t_plus</td>\n";
			print "</tr>\n";
		}
	}
	print <<"EOM";
</td>
</tr>
</table>
</table>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=senjutu_henkou>
<input type=submit class=btn value="�ύX����">
</form>
<form action="$script" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

#----------------#
#  ��p�ύX      #
#----------------#
sub senjutu_henkou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'ab'}==""){&error("�����ƑI�����ĂˁO�O$back_form");} 

	$senjutu_no=$in{'ab'}+50;
	@log_senjutu = "0<>0<>1<>�Ȃ�<>���A�r���e�B�Ȃ��Ő킢�܂�<>0<>\n";

	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		# 2004�N7��7���C��
		if(!$ks_ms || ($ks_ms && $chara[33] >= 100)){
			push(@log_senjutu,"$_");
		}
		if($chara[$senjutu_no] eq "$ks_no"){
			$now_youkyu = $youkyu;
		}
	}

	#�}�X�^�[������p�̃C���N���[�h
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 100 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				push(@log_senjutu,@gettac);
				foreach (@gettac){
				($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
				if($chara[$senjutu_no] eq "$ks_no"){
					$now_youkyu = $youkyu;
					last;
				}
				}
			}
			$i++;
		}
	}

	$hit=0;
	foreach(@log_senjutu){
		($s_no,$s_name) = split(/<>/);
		if($in{'senjutu_no'} eq "$s_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����Ȑ�p�͂���܂���"); }

	open(IN,"$tac_file");
	@alltac = <IN>;
	close(IN);

	foreach (@alltac){
		($a_no,$a_dousei,$a_youkyu,$a_name,$a_plus,$a_ms) = split(/<>/);
		if($in{'senjutu_no'} eq $a_no){
			$new_youkyu = $a_youkyu;
			last;
		}
	}

	if($chara[13] + $now_youkyu < $new_youkyu ){&error("�|�C���g������܂���");}
	if($senjutu_no<55 and $a_no ne 0){
		if($a_dousei==0){&error("���A�r���e�B�ł͂���܂���");}
	}
	if($senjutu_no>54){
		if($a_dousei==1){&error("�ÃA�r���e�B�ł͂���܂���$dousei");}
	}
	&get_host;

	#���l��
	if($in{'senjutu_no'}==84){
		if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
			&error("���̃A�r���e�B�͂P���������܂���B");
		}else{
			$chara[16]=int($chara[16]*100);
			$chara[15]=$chara[16];
		}
	}
	#���l������
	if($chara[$senjutu_no]==84 and $in{'senjutu_no'} !=84){
		$chara[16]=int($chara[16]/100);
		$chara[15]=$chara[16];
	}
	
	#�A�r���e�B�����@���A���̎�̖��@�𑕔����Ă��鎞�A
	if($chara[$senjutu_no]==3 and $in{'senjutu_no'} !=3 and $chara[59]<=10){$chara[59]=0;}
	if($chara[$senjutu_no]==13 and $in{'senjutu_no'} !=13 and $chara[59]>10 and $chara[59]<=20){$chara[59]=0;}
	if($chara[$senjutu_no]==27 and $in{'senjutu_no'} !=27 and $chara[59]>20 and $chara[59]<=30){$chara[59]=0;}
	if($chara[$senjutu_no]==31 and $in{'senjutu_no'} !=31 and $chara[59]>30 and $chara[59]<=40){$chara[59]=0;}
	if($chara[$senjutu_no]==35 and $in{'senjutu_no'} !=35 and $chara[59]>40 and $chara[59]<=50){$chara[59]=0;}
	if($in{'senjutu_no'}==55){
		if($chara[55]==55 or $chara[56]==55 or $chara[57]==55 or $chara[58]==55){
			&error("���̃A�r���e�B�͂P���������܂���B");
		}
	}
	#�X�e�[�^�X���㏸
	if($in{'senjutu_no'}==70){
		$chara[7]+=2500;
		$chara[8]+=2500;
		$chara[9]+=2500;
		$chara[10]+=2500;
		$chara[11]+=2500;
		$chara[12]+=2500;
	}
	#�A�r���e�B���X�e�[�^�X���㏸�����Ă��鎞�A
	if($chara[$senjutu_no]==70){
		$chara[7]-=2500;
		$chara[8]-=2500;
		$chara[9]-=2500;
		$chara[10]-=2500;
		$chara[11]-=2500;
		$chara[12]-=2500;
		if($chara[7]<1){$chara[7]=1;}
		if($chara[8]<1){$chara[8]=1;}
		if($chara[9]<1){$chara[9]=1;}
		if($chara[10]<1){$chara[10]=1;}
		if($chara[11]<1){$chara[11]=1;}
		if($chara[12]<1){$chara[12]=1;}
	}

	$chara[$senjutu_no] = $in{'senjutu_no'};

	$chara[13]=$chara[13]+$now_youkyu-$new_youkyu;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�A�r���e�B��ύX���܂���</h1>
<hr size=0>
<form action="./abilitychange.cgi" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�߂�">
</form><br><br>
<form action="$script" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="�X�e�[�^�X��ʂ�">
</form>
EOM

	&footer;

	exit;
}

