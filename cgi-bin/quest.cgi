#!/usr/local/bin/perl

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
<form action="quest.cgi" method="post">
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

&quest_view;

exit;

#----------------#
#  �N�G�X�g�\��  #
#----------------#
sub quest_view {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�����N�G�X�g</h1>
<hr size=0>

<FONT SIZE=3>
<B>���莆</B><BR>
�u�����ȃ����X�^�[��|���Ă����`���҂��W���Ă��܂��B<br>
��x�Ɏ󂯂���N�G�X�g�͂R�܂ŁA�ォ�珇�ԂɎ󂯂Ă��������B�v
EOM
if($chara[135]==7){
	print <<"EOM";
<form action="quest.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="special">
<input type=submit class=btn value="���ʃN�G�X�g��"></td>
</form>
EOM
}
	print <<"EOM";
</FONT>
<br><br>
�����N�G�X�g���e
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy>
<table>
<tr>
<th>No.</th><th>�Ώ�</th><th>��V</th><th>�i�s���</th></tr>
EOM
	open(IN,"inquest.cgi");
	@quest_item = <IN>;
	close(IN);

	foreach(@quest_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 100;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp�o���l";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>��</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>�i�s��</th></tr>";
		}
		else{
			print "<th>����</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno>
<option value="no">�I�����Ă�������
$selection
</select>
<input type=submit class=btn value="�����󂯂�">
<br>
</table>
</form>
�^�Ɨ͂������āA�Ȃ����m�b�͍T���߂Ł[�B���x���͍��߂Ł[�B
EOM
if($chara[127]==2){
	print <<"EOM";
<br><br>
�����N�G�X�g���e
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy2>
<table>
<tr>
<th>No.</th><th>�Ώ�</th><th>��V</th><th>�i�s���</th></tr>
EOM
	open(IN,"inquest2.cgi");
	@quest2_item = <IN>;
	close(IN);

	foreach(@quest2_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 150;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp�o���l";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem2.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>��</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>�i�s��</th></tr>";
		}
		else{
			print "<th>����</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno2>
<option value="no">�I�����Ă�������
$selection
</select>
<table><input type=submit class=btn value="�����󂯂�">
<br>
</table>
</form>
EOM
if($chara[188]>0){
	print <<"EOM";
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest2_tobasi>
<select name=questno2>
<option value="no">�I�����Ă�������
$selection
</select>
<table><input type=submit class=btn value="�Ԃ���΂�">
<br>
</table>
</form>
EOM
}
}
if($chara[127]==2 and $chara[18]>=1500 and $chara[7]>99 and $chara[8]<100 and $chara[11]>1000){
	print <<"EOM";
<br><br>
���܂�
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy3>
<table>
<tr>
<th>No.</th><th>�ړI</th><th>��V</th><th>�i�s���</th></tr>
EOM
	open(IN,"inquest3.cgi");
	@quest3_item = <IN>;
	close(IN);
	$selection="";
	foreach(@quest3_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 195;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp�o���l";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem3.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>��</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>�i�s��</th></tr>";
		}
		else{
			print "<th>����</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno3>
<option value="no">�I�����Ă�������
$selection
</select>
<input type=submit class=btn value="�����󂯂�">
<br>
</table>
</form>
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

sub special {

	&chara_load;

	&chara_check;

	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest_data = split(/<>/,$questdata);

	$hit=0;
	foreach(@quest_data){
		if($_>0){$hit=1;last;}
	}

	&header;

	print <<"EOM";
<h1>�X�y�V�����E�N�G�X�g</h1>
<hr size=0>

<FONT SIZE=3>
<B>���莆</B><BR>
�u�ȉ��̈������A�����E�œ|���Ă��������B�����̃N�G�X�g�͉��x�ł��󂯂��܂����A�����Ɏ󂯂���̂͂P�܂łł��B�v
</FONT>
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy4>
<table>
<tr><th>No.</th><th>�Ώ�</th><th>��V</th></tr>
<tr><th> 1 </th><th>�X�m��</th><th>�΂̌��f</th></tr>
<tr><th> 2 </th><th>�X�m��</th><th>���̌��f</th></tr>
<tr><th> 3 </th><th>�X�m�~</th><th>�ł̌��f</th></tr>
<tr><th> 4 </th><th>�X�m�~</th><th>���̌��f</th></tr>
</table>
<br><br>
<select name=questno>
<option value="no">�I�����Ă�������</option>\n
<option value="1">1�D�X�m��</option>\n
<option value="2">2�D�X�m��</option>\n
<option value="3">3�D�X�m�~</option>\n
<option value="4">4�D�X�m�~</option>\n
</select>
EOM
if($hit!=1){print "<input type=submit class=btn value=\"�����󂯂�\">";}
	print <<"EOM";
<br>
</table>
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub quest_buy {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno'} eq 'no'){
		&error("�󂯂�N�G�X�g��I�����Ă�������$back_form");
	}

	for($i=101;$i<127;$i++){
		if($chara[$i]=="" and $i < $in{'questno'}){
			&error("�O�̃N�G�X�g�̒��Ɏ󂯂Ă��Ȃ��N�G�X�g������܂��B$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("��x�Ɏ󂯂���N�G�X�g�͂R�܂łł��B$back_form");}

	$quest_no = $in{'questno'};
	if($chara[$quest_no] != ""){
	&error("���ɂ��̃N�G�X�g�͎󂯂Ă��܂�$back_form");
	} else { $chara[$quest_no] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>�����󂯂܂����B</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub quest_buy2 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno2'} eq 'no'){
		&error("�󂯂�N�G�X�g��I�����Ă�������$back_form");
	}

	for($i=151;$i<180;$i++){
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("��x�Ɏ󂯂���N�G�X�g�͂R�܂łł��B$back_form");}

	$quest_no2 = $in{'questno2'};
	if($chara[$quest_no2] != ""){
	&error("���ɂ��̃N�G�X�g�͎󂯂Ă��܂�$back_form");
	} else { $chara[$quest_no2] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>�����󂯂܂����B</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest_buy3 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno3'} eq 'no'){
	&error("�󂯂�N�G�X�g��I�����Ă�������$back_form");
	}

	for($i=196;$i<200;$i++){
		if($chara[$i]=="" and $i < $in{'questno3'}){
			&error("�O�̃N�G�X�g�̒��Ɏ󂯂Ă��Ȃ��N�G�X�g������܂��B$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("��x�Ɏ󂯂���N�G�X�g�͂R�܂łł��B$back_form");}

	$quest_no3 = $in{'questno3'};
	if($chara[$quest_no3] != ""){
	&error("���ɂ��̃N�G�X�g�͎󂯂Ă��܂�$back_form");
	} else { $chara[$quest_no3] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>�����󂯂܂����B</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest_buy4 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest_data = split(/<>/,$questdata);
	$hit=0;
	foreach(@quest_data){
		if($_>0){$hit=1;last;}
	}

	if($in{'questno'} eq 'no'){
	&error("�󂯂�N�G�X�g��I�����Ă�������$back_form");
	}
	if($hit==1){&error("��x�Ɏ󂯂���N�G�X�g�͂P�܂łł��B$back_form");}

	$quest_no = $in{'questno'};
	
	$quest_data[$quest_no] = 1;

	$new_data = '';
	$new_data = join('<>',@quest_data);
	$new_data .= '<>';
	open(OUT,">./quest/$chara[0].cgi");
	print OUT $new_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>�����󂯂܂����B</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest2_tobasi {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno2'} eq 'no'){
	&error("�Ԃ���΂��N�G�X�g��I�����Ă�������$back_form");
	}

	for($i=151;$i<180;$i++){
		if($chara[$i]=="" and $i < $in{'questno2'}){
			&error("�O�̃N�G�X�g�̒��ɏI�����Ă��Ȃ��N�G�X�g������܂��B$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}

	$quest_no2 = $in{'questno2'};
	if($chara[$quest_no2] != ""){
	&error("���ɂ��̃N�G�X�g�͎󂯂Ă��܂�$back_form");
	}elsif($quest_no2 > 166){
	&error("���̃N�G�X�g�͂Ԃ���΂��܂���$back_form");
	}else{ $chara[$quest_no2] = 2; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>����Ȃ��N�G�X�g���Ԃ���΂��܂����B</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}