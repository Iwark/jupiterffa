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
<form action="shops.cgi" method="post">
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
#  �A�C�e���\��  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"$item_file");
	@log_item = <IN>;
	close(IN);

	open(IN,"$def_file");
	@log_def = <IN>;
	close(IN);

	open(IN,"$acs_file");
	@log_acs = <IN>;
	close(IN);

	open(IN,"$pet_file");
	@log_pet = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold) = split(/<>/);
		if($chara[24] eq "$si_no"){ $hit=1;last; }
	}
	if(!$hit) {$si_name="�f��";$si_dmg="0";$si_gold="0";}
	if($chara[24]==1400){
		$hit=0;
		$si_name=$item[0];
		$si_dmg=$item[1];
	}
	$hitd=0;
	foreach(@log_def){
		($di_no,$di_name,$di_dmg,$di_gold) = split(/<>/);
		if($chara[29] eq "$di_no"){ $hitd=1;last; }
	}
	if(!$hitd) {$di_name="���i��";$di_dmg="0";$di_gold="0";}

	$hita=0;
	foreach(@log_acs){
		($a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($chara[31] eq "$a_no"){ $hita=1;last; }
	}

	if(!$hita) {$a_name="�Ȃ�";$a_gold="0";$a_ex = "-";}

	$hitp=0;
	foreach(@log_pet){
		($pi_no,$pi_name,$pi_gold,$pi_exp,$pi_hp,$pi_damage,$pi_image,$ps) = split(/<>/);
		if($chara[38] eq "$pi_no"){ $hitp=1;last; }
	}
	if(!$hitp) {$pi_name="�Ȃ�";$pi_exp="0";$pi_gold="0";$pi_hp="0";$pi_damage="0";}

	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($si_gold / 4) * 3;
		$udi_gold = int($di_gold / 4) * 3;
		$uai_gold = int($a_gold / 4) * 3;
	}else{
		$ui_gold = int($si_gold / 3) * 2;
		$udi_gold = int($di_gold / 3) * 2;
		$uai_gold = int($a_gold / 3) * 2;
	}
	$upi_gold = int($pi_gold / 3) * 2;
	if ($pi_no==3000){$upi_gold = $pi_gold;}

	open(IN,"$item_folder");
	@item_array = <IN>;
	close(IN);

	open(IN,"$def_folder");
	@def_array = <IN>;
	close(IN);

	open(IN,"$acs_folder");
	@acs_array = <IN>;
	close(IN);

	open(IN,"$pet_folder");
	@pet_array = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";$si_dmg += $item[20];}
	if($item[22]){$bogulv="+ $item[22]";$di_dmg += $item[22];}

	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}

	&header;

	print <<"EOM";
<h1>���X�X</h1>
<hr size=0>

<FONT SIZE=3>
<B>���X�X�̃}�X�^�[</B><BR>
�u��������Ⴂ�I����A�h��A�����i�A�����Ė��@�A����Ƀy�b�g�̗��A�X�L���ƁA���낢��Ƒ����Ă��`�B<BR>
�@���A�Ȃ񂾂��A<B>$chara[4]</B>����Ȃ����B���C�ɂ��Ă������H
<BR>
�@�܂��A������茩�Ă����Ă���B
<BR><BR>���������I�ŋߑ����i�̉������͂��߂��񂾁B�v<br>
</FONT>
EOM
if($chara[18]>200){
	print <<"EOM";
<br>
<form action="stshops.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�����X�X��"></td>
</form>
EOM
}
	print <<"EOM";
<br><hr>���݂̏������F$chara[19] �f<br>
���݂̖��@ NO�F$chara[59]<br>
���݂̃y�b�g�X�L��NO�F$chara[47]
<table>
<tr>
<th></th><th></th><th>�Ȃ܂�</th><th>HP,�З�,����</th><th>���l</th></tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̕���</th><th>$si_name $bukilv</th><th>$si_dmg</th><th>$ui_gold</th>
</tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_sell>
EOM
if ($hitd) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̖h��</th><th>$di_name $bogulv</th><th>$di_dmg</th><th>$udi_gold</th>
</tr>
<tr>
<form action="shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_sell>
EOM
if ($hita) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̑����i</th><th>$a_name</th><th>$a_ex</th><th>$uai_gold</th>
</tr>
<tr>
<form action="./shops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=pet_sell>
<input type=submit class=btn value="����">
</th></form><th>���݂̃y�b�g</th><th>$pename</th><th>HP $pi_hp,�U���� $pi_damage</th><th>$upi_gold</th>
</tr>
</table>
<table>
<tr>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $igold) {
			print "<input type=radio name=item_no value=\"$ino\">";
		} else {
			print "�~";
		}
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="����𔃂�">
</form>
</td>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@def_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		if ($chara[19] >= $igold) {
			print "<input type=radio name=item_no value=\"$ino\">";
		} else {
			print "�~";
		}
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_buy>
<input type=submit class=btn value="�h��𔃂�">
</form>
</td>
<td>
<form action="shops.cgi" method="post">
<table>
EOM

	foreach (@acs_array) {
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($ai_no eq "0015"){
			if($chara[70]==1){
				print "<tr><td class=b1 align=\"center\">\n";
				if ($chara[19] >= $ai_gold) {
					print "<input type=radio name=item_no value=\"$ai_no\">";
				} else {
					print "�~";
				}
				print "</td><td align=right class=b1>$ai_no</td><td class=b1>$ai_name</td><td align=right class=b1>$ai_msg</td><td align=right class=b1>$ai_gold</td>\n";
				print "</tr>\n";
			}
		}elsif($ai_no eq "0016"){
		}else{
			print "<tr><td class=b1 align=\"center\">\n";
			if ($chara[19] >= $ai_gold) {
				print "<input type=radio name=item_no value=\"$ai_no\">";
			} else {
				print "�~";
			}
			print "</td><td align=right class=b1>$ai_no</td><td class=b1>$ai_name</td><td align=right class=b1>$ai_msg</td><td align=right class=b1>$ai_gold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_buy>
<input type=submit class=btn value="�����i�𔃂�">
</form>
</td>
<td>
<form action="./shops.cgi" method="post">
<table>
EOM

	foreach (@pet_array) {
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
<input type=hidden name=mode value=pet_buy>
<input type=submit class=btn value="���𔃂�">
</form>
</td>
</tr>
</table>
EOM
if ($chara[55]==3 or $chara[56]==3 or $chara[57]==3 or $chara[58]==3){
	print <<"EOM";
	<form action="./shops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=1>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>001</th><th>�t�@�C�A</th><th>50000G</th>
	<th>�����@�t�@�C�A������܂��B�_���[�W���t�o�B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=2>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>002</th><th>�t�@�C��</th><th>75000G</th>
	<th>�����@�t�@�C��������܂��B�_���[�W���t�o�B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=3>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>003</th><th>�t�@�C�K</th><th>200000G</th>
	<th>�����@�t�@�C�K������܂��B�_���[�W��t�o�B</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=4>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>004</th><th>�u���U�h</th><th>50000G</th>
	<th>�����@�u���U�h������܂��B����_���[�W���_�E���B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=5>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>005</th><th>�u���U��</th><th>75000G</th>
	<th>�����@�u���U��������܂��B����_���[�W���_�E���B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=6>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>006</th><th>�u���U�K</th><th>200000G</th>
	<th>�����@�u���U�K������܂��B����_���[�W��_�E���B</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=7>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>007</th><th>�T���_�[</th><th>50000G</th>
	<th>�����@�T���_�[������܂��B�����͏��A�b�v�B</th></tr>
	
	<th>
EOM
	if ($chara[19] >= 75000) {print "<input type=radio name=ps_no value=8>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>008</th><th>�T���_��</th><th>75000G</th>
	<th>�����@�T���_��������܂��B�����͒��A�b�v�B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=9>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>009</th><th>�T���_�K</th><th>200000G</th>
	<th>�����@�T���_�K������܂��B�����͑�A�b�v�B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂ō����@�͔����܂���B
EOM
}
if ($chara[55]==13 or $chara[56]==13 or $chara[57]==13 or $chara[58]==13){
	print <<"EOM";
	<form action="./shops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=11>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>011</th><th>�q�[��</th><th>50000G</th>
	<th>�����@�q�[��������܂��B</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=12>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>012</th><th>�q�[����</th><th>100000G</th>
	<th>�����@�q�[����������܂��B</th></tr>
	<th>
EOM
	if ($chara[19] >= 200000) {print "<input type=radio name=ps_no value=13>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>013</th><th>�q�[���K</th><th>200000G</th>
	<th>�����@�q�[���K������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂Ŕ����@�͔����܂���B
EOM
}
if ($chara[55]==27 or $chara[56]==27 or $chara[57]==27 or $chara[58]==27){
	print <<"EOM";
	<form action="shops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�E�p</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=21>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>021</th><th>���g</th><th>50000G</th>
	<th>�E�p���g������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�E�p�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�E�p�����v���Ȃ��̂ŔE�p�͔����܂���B
EOM
}
if ($chara[55]==31 or $chara[56]==31 or $chara[57]==31 or $chara[58]==31){
	print <<"EOM";
	<form action="./shops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�Ԗ��@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=31>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>031</th><th>�h���C��</th><th>50000G</th>
	<th>�Ԗ��@�h���C��������܂��B</th></tr>

	</table>
	<br><br>
	<input type=submit class=btn value="�Ԗ��@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�Ԗ��@�����v���Ȃ��̂ŐԖ��@�͔����܂���B
EOM
}
if ($chara[55]==35 or $chara[56]==35 or $chara[57]==35 or $chara[58]==35){
	print <<"EOM";
	<form action="./shops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�����@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=41>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>041</th><th>�X���E</th><th>50000G</th>
	<th>�����@�X���E������܂��B</th></tr>
	<tr><th>
EOM
	if ($item[0] eq "�ŕ����̌�" and $item[3] eq "�ł̉H��" and $item[6] eq "�ł̈�"){
		if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=43>";}
		else{print "�~";}
		print <<"EOM";
		</th>
		<th>043</th><th>�_�[�N���e�I</th><th>100000000G</th>
		<th>�����@���`���e�I������܂��B</th></tr>
EOM
	}
		print <<"EOM";
	</table>
	<br><br>
	<input type=submit class=btn value="�����@�𔃂�">
	</form>
EOM
}else{
	print <<"EOM";
	<br><br>���Ȃ��́u�����@�����v���Ȃ��̂Ŏ����@�͔����܂���B
EOM
}
if ($chara[38]>3100) {
	print <<"EOM";
<form action="./shops.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=pps_buy>
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
<br><br>�y�b�g�������ĂȂ��̂Ńy�b�g�X�L���͔����܂���B
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

	open(IN,"$item_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[19] < $i_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���퉮�̃}�X�^�[</B><BR>
�u���x����`�I<br>
����������͂��񂽂̕���q�ɂɑ����Ă�������I
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

	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($chara[24] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if(!$chara[24]) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[24] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&item_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name $bukilv�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub def_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$def_folder");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($d_no,$d_name,$d_dmg,$d_gold,$d_hit) = split(/<>/);
		if($in{'item_no'} eq "$d_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[19] < $d_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $d_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$d_no<>$d_name<>$d_dmg<>$d_gold<>$d_hit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SD');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�h��̃}�X�^�[</B><BR>
�u���x����`�I<br>
�������h��͂��񂽂̖h��q�ɂɑ����Ă�������I
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
sub def_sell {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$def_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold) = split(/<>/);
		if($chara[29] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if(!$chara[29]) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[29] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&def_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name $bogulv�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub acs_buy {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$acs_folder");
	@acs_array = <IN>;
	close(IN);
	if($in{'item_no'} eq "0015" and $chara[83]==1){$item2_no="0016";$chara[83]=0;}
	else{$item2_no=$in{'item_no'};}
	$hit=0;
	foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($item2_no eq "$ai_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[19] < $ai_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ai_gold; }

	$chara[26] = $host;

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("�����i�q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);
	&unlock($lock_file,'SA');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�����i���̃}�X�^�[</B><BR>
�u���x����`�I<br>
�����������i�͂��񂽂̑����i�q�ɂɑ����Ă�������I
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
sub acs_sell {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$acs_file");
	@acs_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@acs_array){
		($i_no,$i_name,$i_gold) = split(/<>/);
		if($chara[31] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if(!$chara[31]) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($i_gold / 4) * 3;
	}else{	$ui_gold = int($i_gold / 3) * 2;}

	$chara[19] = $chara[19] + $ui_gold;
	if($chara[19] > $gold_max){$chara[19] = $gold_max;}

	$chara[31] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&acs_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<h1>$i_name�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'ps_no'}==""){ &error("���������X�L����I��ł�������$back_form"); }

	if ($in{'ps_no'}==1){$ps_gold = 50000;}
	if ($in{'ps_no'}==2){$ps_gold = 75000;}
	if ($in{'ps_no'}==3){$ps_gold = 200000;}
	if ($in{'ps_no'}==4){$ps_gold = 50000;}
	if ($in{'ps_no'}==5){$ps_gold = 75000;}
	if ($in{'ps_no'}==6){$ps_gold = 200000;}
	if ($in{'ps_no'}==7){$ps_gold = 50000;}
	if ($in{'ps_no'}==8){$ps_gold = 75000;}
	if ($in{'ps_no'}==9){$ps_gold = 200000;}
	if ($in{'ps_no'}==11){$ps_gold = 50000;}
	if ($in{'ps_no'}==12){$ps_gold = 100000;}
	if ($in{'ps_no'}==13){$ps_gold = 200000;}
	if ($in{'ps_no'}==21){$ps_gold = 50000;}
	if ($in{'ps_no'}==31){$ps_gold = 50000;}
	if ($in{'ps_no'}==41){$ps_gold = 50000;}
	if ($in{'ps_no'}==43){$ps_gold = 100000000;}
	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[59] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�X�y���V���b�v�̓X��</B><BR>
�u���x����`�I<br>
���ɖ��@�����X�����Ă��Ȃ�A�����Ȃ���I�n�n�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub pet_buy {

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
sub pet_sell {
	

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
sub pps_buy {

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
