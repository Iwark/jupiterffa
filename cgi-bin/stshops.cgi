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
<form action="stshops.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
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

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

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

	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($si_gold / 4) * 3;
		$udi_gold = int($di_gold / 4) * 3;
		$uai_gold = int($a_gold / 4) * 3;
	}else{
		$ui_gold = int($si_gold / 3) * 2;
		$udi_gold = int($di_gold / 3) * 2;
		$uai_gold = int($a_gold / 3) * 2;
	}

	open(IN,"data/item/stitem.ini");
	@item_array = <IN>;
	close(IN);

	open(IN,"data/def/stdef.ini");
	@def_array = <IN>;
	close(IN);

	open(IN,"data/def/stacs.ini");
	@acs_array = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";$si_dmg += $item[20];}
	if($item[22]){$bogulv="+ $item[22]";$di_dmg += $item[22];}

	&header;

	print <<"EOM";
<h1>�ł̏��X�X</h1>
<hr size=0>

<FONT SIZE=3>
<B>�ł̏��X�X�̃}�X�^�[</B><BR>
�u��������Ⴂ�I�V�����Ȃ����ł̕���A�h��A�����Ė��@�ƁA���낢��Ƒ����Ă��`�B<BR>
�@���A�Ȃ񂾂��A<B>$chara[4]</B>����Ȃ����B�܂������Ă��̂����H
<BR>
�@�܂��A������茩�Ă����Ă���B
<BR><BR>���������I�ŋߑ����i�̉������͂��߂��񂾁B�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
���݂̖��@ NO�F$chara[59]<br>
<table>
<tr>
<th></th><th></th><th>�Ȃ܂�</th><th>�З�,����</th><th>���l</th></tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
EOM
if ($hit) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̕���</th><th>$si_name $bukilv</th><th>$si_dmg</th><th>$ui_gold</th>
</tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=def_sell>
EOM
if ($hitd) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̖h��</th><th>$di_name $bogulv</th><th>$di_dmg</th><th>$udi_gold</th>
</tr>
<tr>
<form action="stshops.cgi" method="post">
<th><input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=acs_sell>
EOM
if ($hita) { print "<input type=submit class=btn value=\"����\">"; }
	print <<"EOM";
</th></form><th>���݂̑����i</th><th>$a_name</th><th>$a_ex</th><th>$uai_gold</th>
</tr>
</table>
<table>
<tr>
<td>
<form action="stshops.cgi" method="post">
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		if($ino != 1140 or $chara[69]==1){
			print "<tr><td class=b1 align=\"center\">\n";
			print "<input type=radio name=item_no value=\"$ino\">";
			print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
			print "</tr>\n";
		}
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�������Ɏ��">
</form>
</td>
<td>
<form action="stshops.cgi" method="post">
<table>
EOM

	foreach (@def_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		print "<input type=radio name=item_no value=\"$ino\">";
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�h�����Ɏ��">
</form>
</td>
<td>
<form action="stshops.cgi" method="post">
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
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�����i�𔃂�">
</form>
</td>
</tr>
</table>
EOM
if ($chara[55]==27 or $chara[56]==27 or $chara[57]==27 or $chara[58]==27){
	print <<"EOM";
	<form action="stshops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�E�p</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000000) {print "<input type=radio name=ps_no value=22>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>022</th><th>���</th><th>5000000G</th>
	<th>�E�p��������܂��B</th></tr>

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
	<form action="./stshops.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ps_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>�Ԗ��@</th><th>�l�i</th><th>����</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000000) {print "<input type=radio name=ps_no value=32>";}
	else{print "�~";}
	print <<"EOM";
	</th>
	<th>032</th><th>�M�K�h���C��</th><th>5000000G</th>
	<th>�Ԗ��@�M�K�h���C��������܂��B</th></tr>

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

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("$in{'item_no'}����ȃA�C�e���͑��݂��܂���@item_array"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	if($in{'kane'}>0){$chara[19]-=$in{'kane'};}
	elsif($chara[19] < $i_gold) { $bgg=1; }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;
if($bgg!=1){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("����q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�h��q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�����i�q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���������퉮�̃}�X�^�[</B><BR>
�u���x����`�I<br>
����������͂��񂽂̕���q�ɂɑ����Ă�������I
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;
}else{

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red">
<B>���������퉮�̃}�X�^�[</B><BR>
�u�M�l�E�E�E�����Ȃ��̂ɕ������Ɏ��Ƃ͗ǂ��x������<br>
����������ł���������A�n���������낵�����|��̌����邱�ƂɂȂ邼�B
�v</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��������ɖ߂�">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=nigeru>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="����������ē��S����B">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tatakau>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="�X��Ɛ키">
</form>
EOM
if($chara[64]==100){
	print <<"EOM";
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=negiri>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="�l�؂������">
</form>
EOM
}
print "<hr size=0>";
}

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

	if ($in{'ps_no'}==22){$ps_gold = 5000000;}
	if ($in{'ps_no'}==32){$ps_gold = 5000000;}

	if($chara[19] < $ps_gold) { &error("����������܂���$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;

	$chara[59] = $in{'ps_no'};

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�������X�y���V���b�v�̓X��</B><BR>
�u���x����`�I<br>
���ɖ��@�����X�����Ă��Ȃ�A�����Ȃ���I�n�n�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub nigeru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$chara[26] = $host;

if(int(rand(4))==1){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("����q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�h��q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�����i�q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	if($chara[192]==1){
		$chara[192]=2;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>���������X�X�̃}�X�^�[</B><BR>
�u�҂ăS���@�@�@�@<br>
�E�E�E�E�E�E�����A�����������B<br>
�o���Ă��E�E�E�B
�v</font>
<hr size=0>
EOM
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	$chmes="$chara[4]�l���������҂ɒǂ��Ă���悤�ł��B";
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	unshift(@chat_mes,"<><font color=\"yellow\">���m</font><>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$chmes</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]�l�͈��ɐ��܂肷���A�܋���(�܋��F$syoukingaku G)�ƂȂ�܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);
		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");
		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);
	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	$chara[13]-=1;
	if($chara[192]==1){
		$chara[192]=0;
		$chara[19]=int($chara[19]/3);
		$chara[34]=int($chara[34]/3);
		$bb=1;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($bb==1){
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>���������X�X�̃}�X�^�[</B><BR>
�u��������Ǝv���Ă��̂��H�M�l�E�E�E��������ȁB<br>
����������ł���������A�n���������낵�����|��̌����邱�ƂɂȂ�A�ƁB<br>
������Ă��x�����E�E�E�B���O�ɂ͋��낵���􂢂����������̂��B
�v</font>
<B>�ꔭ�t�]�̃~�b�V�����Ɏ��s���Ă��܂����I</B><BR></font>
<FONT SIZE=6 color="red">���o���̂����ɏ������𓐂܂ꂽ�I<br></font>
<FONT SIZE=6 color="red">��s�������ɓ���ꂽ�I�I<br></font>
$back_form
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>���������X�X�̃}�X�^�[</B><BR>
�u��������Ǝv���Ă��̂��H�M�l�E�E�E��������ȁB<br>
����������ł���������A�n���������낵�����|��̌����邱�ƂɂȂ�A�ƁB<br>
������Ă��x�����E�E�E�B���O�ɂ͋��낵���􂢂����������̂��B
�v</font>
$back_form
<hr size=0>
EOM
}
}

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub tatakau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$chara[26] = $host;
	if($chara[18]>5000){$byouyy=int(19701+rand(400));}
	else{$byouyy=int(10000+rand($chara[18]+12500));}
if($byouyy>20000){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("����q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�h��q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($in{'item_no'}<1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("�����i�q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}

	&unlock($lock_file,'SI');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	if($chara[191]==1){
		$chara[191]=2;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>���������X�X�̃}�X�^�[</B><BR>
�u���E�E�E�����͒��q���������B<br><br>
�o���Ă��E�E�E�B
�v</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]�l�����������X�X�̓X�����������悤�ł��B";

	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]�l�͈��ɐ��܂肷���A�܋���(�܋��F$syoukingaku G)�ƂȂ�܂����B";

		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);

		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");

		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[13]-=2;
	if($chara[191]==1){
		$chara[191]=0;
		$chara[19]=int($chara[19]/2);
		$chara[34]=int($chara[34]/2);
		$bb=1;
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	$byouyy-=10000;
if($bb==1){
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy�b�ŏu�E���ꂽ�B</B><BR><BR>
<B>���������X�X�̃}�X�^�[</B><BR>
�u�U�R���B���̒��x�̘r�ł����ւ���񂶂�˂��B�A��ȁBAP�����Ƃ��Ă�����悗
�v
<B>�ꔭ�t�]�̃~�b�V�����Ɏ��s���Ă��܂����I</B><BR></font>
<FONT SIZE=6 color="red">���o���̂����ɏ������𓐂܂ꂽ�I<br></font>
<FONT SIZE=6 color="red">��s�������ɓ���ꂽ�I�I<br></font>
$back_form
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy�b�ŏu�E���ꂽ�B</B><BR><BR>
<B>���������X�X�̃}�X�^�[</B><BR>
�u�U�R���B���̒��x�̘r�ł����ւ���񂶂�˂��B�A��ȁBAP�����Ƃ��Ă�����悗
�v</font>
<br>
<form action="stshops.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM
}
}

	exit;
}

sub negiri {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	if($in{'item_no'}<2000 and $in{'item_no'}>1000){
		open(IN,"data/item/stitem.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<3000 and $in{'item_no'}>2000){
		open(IN,"data/def/stdef.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($in{'item_no'}<1000){
		open(IN,"data/acs/stacs.ini");
		@item_array = <IN>;
		close(IN);
	}

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_no == 1140){
		$i_dmg=$chara[18];
		$ihit=$chara[18];
	}
	$ok=1;
	if($i_gold > 100000000){$kane=int($i_gold / 100);}else{$kane=int($i_gold/2);}
	if($kane > $chara[19]){$ok=0;}

	$chara[26] = $host;

	&header;
if($ok==1){
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>���������퉮�̃}�X�^�[</B><BR>
�u�����E�E�E�m���ɌN�́A�l�̗ǂ������Ȑl�Ԃ��E�E�E�B<br>
�C�ɂ��������I����A���񂽂̔�����l�i�ɒl�������Ă��B<br>
�ǂ����A$kane�f�Ŕ���Ȃ����H�v</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=kane value=$kane>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="����">
</form>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="����Ȃ�">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>���������퉮�̃}�X�^�[</B><BR>
�u�����E�E�E�m���ɌN�́A�l�̗ǂ������Ȑl�Ԃ��E�E�E�B<br>
�����A������Ȃ�ł��N�̏������͒Ⴗ����ȁB���̒l�i�ł͔���Ȃ���B<br>
$kane�f���炢�͗p�ӂ��Ă���B�v</font>
<form action="stshops.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��������ɖ߂�">
</form>
<hr size=0>
EOM
}
	exit;
}