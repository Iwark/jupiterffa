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

	$back_form = << "EOM";
<br>
<form action="$script_souko" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

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

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
if($item[20]==10 and $chara[24]==1400){$g="yellow";}elsif($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="pink";}else{$g="";}
	if($item[22]==10){$w="red";}else{$w="";}

	$bukikoka = "�U���� $item[1]<br>������ $item[2]<br>���� $item[24]";
	$bogukoka = "�h��� $item[4]<br>��� $item[5]<br>���� $item[25]";
	$acskoka = "���� $item[19]";

	&header;

	print <<"EOM";
<h1>�A�C�e���q��</h1>
<hr size=0>

<FONT SIZE=3>
<B>�q�ɊǗ��l</B><BR>
�u
$chara[4]�l�ɗa�����Ă��铹��͉��̂悤�ɂȂ��Ă���܂�
�v
EOM
	if($chara[18]>30000){
		print <<"EOM";
<form action="azukari.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�a���菊��">
</form>
EOM
	}
	print <<"EOM";
</FONT>
<br><hr>���݂̑���<br>
<table>
<tr>
<td id="td2" class="b2">����</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
EOM
	if ($chara[24]) {
	print <<"EOM";
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_hazusi">
<input type=submit class=btn value="�O��">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
<tr>
<td id="td2" class="b2">�h��</td><td align="right" class="b2">
<A onmouseover="up('$bogukoka')"; onMouseout="kes()"><font color="$w">$item[3] $bogulv</font></A></td>
EOM
	if ($chara[29]) {
	print <<"EOM";
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_hazusi">
<input type=submit class=btn value="�O��">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
<tr>
<td id="td2" class="b2">�����i</td><td align="right" class="b2">
<A onmouseover="up('$acskoka')"; onMouseout="kes()">$item[6]</A></td>
EOM
	if ($chara[31]) {
	print <<"EOM";
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="acs_hazusi">
<input type=submit class=btn value="�O��">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
</table>
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
����q��
<table width = "98%">
<tr><th></th><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���l</th></tr>
EOM
	$i = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
if($iname){
		if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
			$igold = int($igold / 4) * 3;
		}else{	$igold = int($igold / 3) * 2;}
		if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
		open(IN,"$item_file");
		@item_item = <IN>;
		close(IN);
		foreach(@item_item){
			($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
			if($ino eq $ci_no) {last;}
		}
		if(!$koka){$koka="���ɂȂ�";}
		$bukikoka = "�U���� $idmg<br>������ $ihit<br>���� $koka";
			print << "EOM";
<tr>
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="��������">
</td>
</form>
<form action="$script_souko" >
EOM
if($ci_no ==1400){
	print <<"EOM";
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_delete">
<input type=submit class=btn value="����" disabled>
</td>
</form>
EOM
}else{
	print <<"EOM";
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="item_delete">
<input type=submit class=btn value="����">
</td>
</form>
EOM
}
	print <<"EOM";
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
}
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
�h��q��
<table width = "98%">
<tr><th></th><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���l</th></tr>
EOM
	$i = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
if($iname){
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibogu="+ $ilv";}else{$ibogu="";}
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$bogukoka = "�h��� $idmg<br>��� $ihit<br>���� $koka";
		print << "EOM";
<tr>
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="def_soubi">
<input type=submit class=btn value="��������">
</td>
</form>
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="def_delete">
<input type=submit class=btn value="����">
</td>
</form>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
}
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
�����i�q��
<table width = "98%">
<tr><th></th><th></th><th>�Ȃ܂�</th><th>���l</th></tr>
EOM

	$i = 0;
	foreach (@souko_acs) {
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
if($ai_name){
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="acs_soubi">
<input type=submit class=btn value="��������">
</td>
</form>
<form action="$script_souko" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$i">
<input type=hidden name=mode value="acs_delete">
<input type=submit class=btn value="����">
</td>
</form>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$i++;
}
	}
		print << "EOM";
</table>
</td></table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#------------#
#  ���푕��  #
#------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/,$souko_item[$in{'item_no'}]);

	if ($chara[24]) {
		open(IN,"$item_file");
		@battle_item = <IN>;
		close(IN);
		foreach(@battle_item){
			($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
			if($chara[24] eq $ci_no) {last;}
		}
		$souko_item[$in{'item_no'}] = "$ci_no<>$item[0]<>$item[1]<>$ci_gold<>$item[2]<>$item[20]<>$item[21]<>\n";
	} else {
		$souko_item[$in{'item_no'}] = ();
	}
	if($ino == "1356"){ $chara[59] = 10; }
	elsif($ci_no == "1356" and $ino == "1358"){ $chara[59] = 10; }
	elsif($ci_no == "1356"){ $chara[59] = 0; }

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SI');
	open(IN,"$item_file");
	@item_item = <IN>;
	close(IN);
	foreach(@item_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$chara[24] = $ino;
	$item[0] = $iname;
	$item[1] = $idmg;
	$item[2] = $ihit;
	$item[20]= $ilv;
	$item[21]= $iexp;
	$item[24]= $koka;
	if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$iname $bukilv�𑕔����܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  �������  #
#------------#
sub item_hazusi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&item_load;

	$chara[26] = $host;

	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($chara[24] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$chara[24]<>$item[0]<>$item[1]<>$i_gold<>$item[2]<>$item[20]<>$item[21]<>\n");
	if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}
	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');
	if($chara[24] == "1356"){ $chara[59] = 0; }

	$chara[24] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');

	&item_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$i_name $bukilv���O���܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ����𔄂�@  #
#----------------#
sub item_delete {
	
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&get_host;

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/,$souko_item[$in{'item_no'}]);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($igold / 4) * 3;
	}else{	$ui_gold = int($igold / 3) * 2;}
	if($ilv){$bukilv="+ $ilv";}else{$bukilv="";}
	if (!$in{'kakunin'}){

		&unlock($lock_file,'SI');

		&header;

		print << "EOM";
<center>
<h2>�{����$iname $bukilv�𔄂�܂����H</h2>
<form action="$script_souko" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$in{'item_no'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="item_delete">
<input type=submit class=btn value="����">
</form>
</center>
EOM

		$new_chara = $chara_log;

		&shopfooter;

		&footer;

		exit;

	}

	$chara[19] += $ui_gold;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$souko_item[$in{'item_no'}] = ();

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SI');

	&header;

	print <<"EOM";
<h1>$iname $bukilv�𔄂�܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  �h���  #
#------------#
sub def_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/,$souko_item[$in{'item_no'}]);

	if ($chara[29]) {
		open(IN,"$def_file");
		@battle_def = <IN>;
		close(IN);
		foreach(@battle_def){
			($cd_no,$a,$b,$cd_gold,$c,$koka) = split(/<>/);
			if($chara[29] eq $cd_no) {last;}
		}
		$souko_item[$in{'item_no'}] = "$cd_no<>$item[3]<>$item[4]<>$cd_gold<>$item[5]<>$item[22]<>$item[23]<>\n";
	} else {
		$souko_item[$in{'item_no'}] = ();
	}

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SD');
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$chara[29] = $ino;
	$item[3] = $iname;
	$item[4] = $idmg;
	$item[5] = $ihit;
	$item[22]= $ilv;
	$item[23]= $iexp;
	$item[25]= $koka;
	if($item[22]){$bogulv="+ $item[22]";}else{$bogulv="";}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$iname $bogulv�𑕔����܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  �h�����  #
#------------#
sub def_hazusi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&item_load;

	$chara[26] = $host;

	open(IN,"$def_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($chara[29] eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$chara[29]<>$item[3]<>$item[4]<>$i_gold<>$item[5]<>$item[22]<>$item[23]<>\n");
	if($item[22]){$bogulv="+ $item[22]";}else{$bogulv="";}
	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SD');

	$chara[29] = 0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');

	&def_lose;

	&item_regist;
	&unlock($lock_file,'IM');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$i_name $bogulv���O���܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �h��𔄂�@  #
#----------------#
sub def_delete {
	
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&get_host;

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/,$souko_item[$in{'item_no'}]);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($igold / 4) * 3;
	}else{	$ui_gold = int($igold / 3) * 2;}
	if($ilv){$bogulv="+ $ilv";}else{$bogulv="";}

	if (!$in{'kakunin'}){

		&unlock($lock_file,'SD');

		&header;

		print << "EOM";
<center>
<h2>�{����$iname $bogulv�𔄂�܂����H</h2>
<form action="$script_souko" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$in{'item_no'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="def_delete">
<input type=submit class=btn value="����">
</form>
</center>
EOM

		$new_chara = $chara_log;

		&shopfooter;

		&footer;

		exit;

	}

	$souko_item[$in{'item_no'}] = ();

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SD');

	&header;

	print <<"EOM";
<h1>$iname $bogulv�𔄂�܂���</h1>
<hr size=0>
EOM

	$chara[19] += $ui_gold;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  ��������  #
#------------#
sub acs_soubi {
	

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	@acs_data = split(/<>/,$souko_item[$in{'item_no'}]);

	if ($chara[31]) {
		&acs_read($chara[31]);
		$souko_item[$in{'item_no'}] = "$a_no<>$item[6]<>$a_gold<>$item[7]<>$item[8]<>$item[9]<>$item[10]<>$item[11]<>$item[12]<>$item[13]<>$item[16]<>$item[17]<>$item[18]<>$item[19]<>\n";
	} else {
		$souko_item[$in{'item_no'}] = ();
	}

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SA');

	$chara[31] = $acs_data[0];
	$item[6] = $acs_data[1];
	for ($i=3;$i<=9;$i++) {
		$s = $i + 4;
		$item[$s] = $acs_data[$i];
	}
	$item[16] = $acs_data[10];
	$item[17] = $acs_data[11];
	$item[18] = $acs_data[12];
	$item[19] = $acs_data[13];

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$acs_data[1]�𑕔����܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#------------#
#  �h�����  #
#------------#
sub acs_hazusi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$acs_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		$acs_array = $_;
		@acs_data = split(/<>/);
		if($chara[31] eq "$acs_data[0]") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$acs_array");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SA');

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
<FONT SIZE=3>
<B>$acs_data[1]���O���܂���</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �����𔄂�@  #
#----------------#
sub acs_delete {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&get_host;

	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/acsesa$in{'id'}.lock";
	&lock($lock_file,'SA');
	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item[$in{'item_no'}] =~ s/\n//g;
	$souko_item[$in{'item_no'}] =~ s/\r//g;

	($ino,$iname,$igold,,,,,,,,,,,) = split(/<>/,$souko_item[$in{'item_no'}]);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ui_gold = int($igold / 4) * 3;
	}else{	$ui_gold = int($igold / 3) * 2;}

	if (!$in{'kakunin'}){

		&unlock($lock_file,'SA');

		&header;

		print << "EOM";
<center>
<h2>�{����$iname�𔄂�܂����H</h2>
<form action="$script_souko" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no value="$in{'item_no'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="acs_delete">
<input type=submit class=btn value="����">
</form>
</center>
EOM

		$new_chara = $chara_log;
		&shopfooter;

		&footer;

		exit;

	}

	$souko_item[$in{'item_no'}] = ();

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);
	&unlock($lock_file,'SA');


	&header;

	print <<"EOM";
<h1>$iname�𔄂�܂���</h1>
<hr size=0>
EOM

	$chara[19] += $ui_gold;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&shopfooter;

	&footer;

	exit;
}
