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
<form action="./pet_shop.cgi" method="post">
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

&item_view;

exit;

#----------------#
#  �y�b�g�\���@  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	open(IN,"$pet_file");
	@log_item = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_gold,$si_exp,$si_hp,$si_damage,$si_image,$ps) = split(/<>/);
		if($chara[38] eq "$si_no"){ $hit=1;last; }
	}

	if(!$hit) {
		$si_name="�Ȃ�";
		$si_exp="0";
		$si_gold="0";
		$si_hp="0";
		$si_damage="0";
	}
	$ui_gold = int($si_gold / 3) * 2;
	if ($si_no==3000){$ui_gold = $si_gold;}


	open(IN,"$pet_folder");
	@item_array = <IN>;
	close(IN);

	open(IN,"$pet_folder");
	@ps_array = <IN>;
	close(IN);
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	&header;

	print <<"EOM";
<h1>�y�b�g�V���b�v</h1>
<hr size=0>

<FONT SIZE=3>
<B>�y�b�g�V���b�v�̓X��</B><BR>
�u��������Ⴂ�I�����ł͂ˁA�y�b�g�̗����������ł���I<BR>
�@���A�Ȃ񂾂��A<B>$chara[4]</B>����Ȃ����B���C�ɂ��Ă������H
<BR>
�@�ӂӁA�ŋ�<B>�y�b�g�X�L��</B>�����ׂ����񂾂�A�����Ă��������H�X�L���͂P�܂ł����I
<BR><BR>���������I���͂P�������ĂȂ������̈������͂ł����B
<br>�퓬���͗����󂳂Ȃ��悤�ɒ��ӂ���񂾂��I�������ꂽ�炱�����ň������̂ɂ����������邼�B�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
<table>
<tr>
<th></th><th></th><th>No.</th><th>�Ȃ܂�</th><th>HP</th><th>�U����</th><th>���i</th></tr>
<th>
<form action="./pet_shop.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) {
	if ($si_no==3000){print "<input type=submit class=btn value=\"�n��\">";}
	else{print "<input type=submit class=btn value=\"����\">";}
}
	print <<"EOM";
</th></form><th>���݂̃y�b�g</th><th>$pename</th><th>$si_hp</th><th>$si_damage</th><th>$ui_gold</th></tr></table>
<form action="./pet_shop.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$igold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
		if($ino == 3007){
			if($chara[31] eq "0032"){
				print "<tr><td class=b1 align=\"center\">\n";
				print "<input type=radio name=item_no value=\"$ino\">";
				print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td class=b1>$i_hp</td><td class=b1>$i_damage</td><td align=right class=b1>$igold</td>\n";
				print "</tr>\n";
			}
		}else{
			print "<tr><td class=b1 align=\"center\">\n";
			if ($chara[19] >= $igold and $chara[70]!=1) {
				print "<input type=radio name=item_no value=\"$ino\">";
			} else {
				print "�~";
			}
			print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td class=b1>$i_hp</td><td class=b1>$i_damage</td><td align=right class=b1>$igold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="���𔃂�">
</form>
EOM

if ($chara[38]>3100) {
	print <<"EOM";
���݂̃y�b�g�X�L��NO�F$chara[47]
<form action="./pet_shop.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<table>
<tr>
<th></th><th>No.</th><th>�X�L��</th><th>�l�i</th><th>������</th><th>����</th></tr>
<th>
EOM
if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=1>";}
else{print "�~";}
	print <<"EOM";
</th>
<th>001</th><th>�q�[�����O</th><th>50000G</th><th>�Q�T��</th>
<th>�L�������񕜂��Ă���܂��B</th></tr>

<th>
EOM
if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=2>";}
else{print "�~";}
	print <<"EOM";
</th>
<th>002</th><th>\��\�\\��</th><th>50000G</th><th>�P�O��</th>
<th>\��\�\\�ꂵ�đ�_���[�W�B</th></tr>

<th>
EOM
if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=3>";}
else{print "�~";}
	print <<"EOM";
</th>
<th>003</th><th>\��\�e\</th><th>100000G</th><th>�T�O��</th>
<th>\��\�e\�𔭓����A���͂t�o�B</th></tr>

<th>
EOM
if ($chara[19] >= 500000) {print "<input type=radio name=ps_no value=19>";}
else{print "�~";}
	print <<"EOM";
</th>
<th>004</th><th>�N���X�J�E���^�[</th><th>500000G</th><th>�R�O��</th>
<th>����̍U��������āA�{�̈З͂ōU���I�I</th></tr>

</table>
<br><br>
<input type=submit class=btn value="�X�L���𔃂�">
</form>
EOM
}else{
	print <<"EOM";
<br><br>�y�b�g�������ĂȂ��̂ŃX�L���͔����܂���B
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$pet_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	if($chara[38]>3000){ &error("���Ɍ��ݎ����Ă��܂��I$back_form"); }
	foreach(@item_array){
		($i_no,$i_name,$i_gold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���$back_form"); }
	if($chara[19] < $i_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;

	$chara[38] = $i_no;
	$chara[39] = $i_name;
	$chara[40] = 0;
	$chara[41] = $i_exp;
	$chara[42] = $i_hp;
	$chara[43] = $i_hp;
	$chara[44] = $i_damage;
	$chara[45] = $i_image;
	$chara[46] = 1;
	$chara[47] = $ps;
	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�y�b�g�V���b�v�̓X��</B><BR>
�u���x����`�I<br>
�����������Ĉ�Ă邱�Ƃ��d�v�����I�퓬�Ŏ��񂾂���邩������Ȃ����璍�ӂ����I
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_sell {
	

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_gold,$i_exp,$i_hp,$i_image,$ps) = split(/<>/);
		if($chara[38] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���$back_form"); }
	if(!$chara[38]) { &error("����ȃA�C�e���͑��݂��܂���$back_form"); }
	if($i_no==3000){
		if($chara[19] < 30000) { &error("����������܂���$back_form"); }
	}
	$ui_gold = int($i_gold / 3) * 2;
	if ($i_no==3000){$ui_gold = $i_gold;}
	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[38] = 0;
	$chara[39] = "�Ȃ�";
	$chara[40] = 0;
	$chara[41] = 0;
	$chara[42] = 0;
	$chara[43] = 0;
	$chara[44] = 0;
	$chara[45] = 0;
	$chara[46] = 0;
	$chara[47] = 0;
	$chara[138] ="";
	&chara_regist;
	&header;
if ($si_no=3000){
	print <<"EOM";
<h1>$i_name����������Ă��炢�܂���</h1>
<hr size=0>
EOM
}else{
	print <<"EOM";
<h1>$i_name�𔄂�܂���</h1>
<hr size=0>
EOM
}
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �@�X�L������  #
#----------------#
sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("���������X�L����I��ł�������$back_form"); }

	if ($in{'ps_no'}==1){$ps_gold = 50000;}
	if ($in{'ps_no'}==2){$ps_gold = 50000;}
	if ($in{'ps_no'}==3){$ps_gold = 100000;}
	if ($in{'ps_no'}==19){$ps_gold = 500000;}

	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[47] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�y�b�g�V���b�v�̓X��</B><BR>
�u���x����`�I<br>
���ɃX�L�������X�����Ă��Ȃ�A�����͖Y�ꂿ�܂������ȁI���n�n�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
