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
<form action="market.cgi" method="post">
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

&itemh;

exit;

#----------------#
#  �A�C�e���\��  #
#----------------#
sub itemh {

	&chara_load;

	&chara_check;

	if($chara[0] eq "test" or $chara[0] eq "test2"){&error("�e�X�g�L�����ł��B");}

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
if($chara[70]<1){
	open(IN,"afreeitem.cgi");
	@item_array = <IN>;
	close(IN);

	open(IN,"afreedef.cgi");
	@def_array = <IN>;
	close(IN);

	open(IN,"afreeacs.cgi");
	@acs_array = <IN>;
	close(IN);
}else{
	open(IN,"freeitem.cgi");
	@item_array = <IN>;
	close(IN);

	open(IN,"freedef.cgi");
	@def_array = <IN>;
	close(IN);

	open(IN,"freeacs.cgi");
	@acs_array = <IN>;
	close(IN);
	$g=0;
	foreach(@acs_array){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if(!$a_name or !$a_no){splice(@acs_array,$g,1);$hit=1;}
		else{$g++;}
	}
	if($hit==1){
		open(OUT,">freeacs.cgi");
		print OUT @acs_array;
		close(OUT);
	}
}
	&header;

	print <<"EOM";
<h1>�t���[�}�[�P�b�g</h1>
<hr size=0>
<FONT SIZE=3><B>�t���[�}�[�P�b�g�̐l</B><BR>
�u<B>$chara[4]</B>���B<br>
��x�ɔ��邱�Ƃ��ł���̂́A<font color="red">����A�h��A�A�N�Z�T���[���ꂼ��S���܂�</font>���B<br>
�����āA<font color="red">�o�i���ꂽ�������ꂼ��30�𒴂���Əo�i���ꂽ���Ԃɏ����Ă���</font>���B<br>
<font color="red">�����ŏo�i�������͔����Ȃ�</font>���璍�ӂ��K�v���B<br>
�܂��A<font color="red">�ő�łQ�O���f</font>�̉��i�ݒ�ƂȂ�B<br>
����Ȃ����i�ŏo�i���Ă��܂��ƁA�o�i�ł��鐔�����邩�璍�ӂ���񂾂ȁB<br>
�܂��A���E�˔j��̐l�Ԃ�1000���x���ȏ�łȂ��ƃA�C�e���̔������ł��Ȃ����B�v<br></FONT>
EOM
if($chara[70]>=1 and $chara[18]>=100){
	print <<"EOM";
<form action="itemya2.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���H�i�f�ރt���[�}�[�P�b�g">
</td>
</form>
EOM
}
	print <<"EOM";
���݂̎������F$chara[19]�@�f
<hr>

<table width = "100%">
	<tr>
	<td width = "30%" align = "center" valign = "top">
	<form action="./market.cgi" method="post">
	<table border=1>
		<tr><th></th><th>���햼</th><th>�U����</th><th>������</th><th>���i</th></tr>
		<tr>
EOM
		$i=0;
		#�o�i�҂̂h�c�A�l�i�A����m���A���O�A�_���[�W�A���A�����A�����A���x���A�o���l
		foreach(@item_array){
			($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
			if($ilv>0){$lvv="+ $ilv";}else{$lvv="";}
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name $lvv</td><td>$i_dmg</td><td>$ihit</td><td>$i_gold</td></tr>
EOM
		$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=buki>
EOM
if($chara[70]==1 and $chara[18]<1000){print "<input type=submit class=btn value=\"�A�C�e���𔃂�\" disabled>";}
else{print "<input type=submit class=btn value=\"�A�C�e���𔃂�\">";}
			print <<"EOM";
	</form>
	</td>

	<td width = "30%" align = "center" valign = "top">
	<form action="./market.cgi" method="post">
	<table border=1>
		<tr><th></th><th>�h�</th><th>�h���</th><th>����</th><th>���i</th></tr>
		<tr>
EOM
		$i=0;
		#�o�i�҂̂h�c�A�l�i�A�h��m���A���O�A�h��́A���A����A�����A���x���A�o���l
		foreach(@def_array){
			($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
			if($ilv>0){$lvv="+ $ilv";}else{$lvv="";}
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name $lvv</td><td>$i_dmg</td><td>$ihit</td><td>$i_gold</td></tr>
EOM
			$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=bougu>
EOM
if($chara[70]==1 and $chara[18]<1000){print "<input type=submit class=btn value=\"�A�C�e���𔃂�\" disabled>";}
else{print "<input type=submit class=btn value=\"�A�C�e���𔃂�\">";}
			print <<"EOM";
	</form>
	</td>

	<td width = "35%" align = "center" valign = "top">
	<form action="./market.cgi" method="post">
	<table border=1>
		<tr><th></th><th>�A�N�Z��</th><th>����</th><th>���i</th></tr>
		<tr>
EOM
		$i=0;
		#�o�i�҂̂h�c�A�l�i�A�A�N�Z�m���A���O�A���A���ʁA�c�A����
		foreach(@acs_array){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$a_name</td><td>$a_ex</td><td>$i_gold</td></tr>
EOM
			$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=acs>
EOM
if($chara[70]==1 and $chara[18]<1000){print "<input type=submit class=btn value=\"�A�C�e���𔃂�\" disabled>";}
else{print "<input type=submit class=btn value=\"�A�C�e���𔃂�\">";}
			print <<"EOM";
	</form>
	</td></tr></table>

<form action="./market.cgi" method="post">
<hr>
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
����
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���l</th></tr>
EOM
	$i = 1;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
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
<td class=b1 align="center">
EOM
if($ino==1400 or $iname eq "���̌�"){
		print << "EOM";
�~
EOM
}else{
		print << "EOM";
<input type=radio name=soubi value=$i>
EOM
}
		print << "EOM";
</td>
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
�h��
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���l</th></tr>
EOM
	$i = 101;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
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
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
�����i
<table width = "98%">
<tr><th></th><th>�Ȃ܂�</th><th>����</th><th>���l</th></tr>
EOM

	$i = 201;
	foreach (@souko_acs) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_msg</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td></table>
<p>
���l�F<input type="text" name="sgold" size=30>G</td>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemu>
EOM
if($chara[70]==1 and $chara[18]<1000){print "<input type=submit class=btn value=\"�o�i����\" disabled>";}
else{print "<input type=submit class=btn value=\"�o�i����\">";}
			print <<"EOM";
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
sub buki {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreeitem.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freeitem.cgi");
		@item_chara = <IN>;
		close(IN);
	}
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u����͂��񂽂̏o�i�����������I<br>
�Ԃ����Ƃ͂ł��Ȃ����ȁA����Ȃ��Ȃ珈�����Ă�낤���H�v</font>
<form action="./market.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemsyobun>
<input type=submit class=btn value="��������">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("����������܂���"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$igold<>$ihit<>$ilv<>$iexp<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreeitem.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freeitem.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	open(IN,"./charalog/$i_id.cgi") || &error("�L�����N�^�[��������܂���$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	$eg="$charan[4]�l���o�i���Ă���$i_name $ibuki���A$chara[4]�l��$i_gold G�ōw�����܂����B";
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u���x����`�I<br>
�����������͂��񂽂̑q�ɂɑ����Ă�������I�v</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub bougu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreedef.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freedef.cgi");
		@item_chara = <IN>;
		close(IN);
	}

	$hit=0;$ii=0;

	foreach(@item_chara){($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u����͂��񂽂̏o�i�����������I<br>
�Ԃ����Ƃ͂ł��Ȃ����ȁA����Ȃ��Ȃ珈�����Ă�낤���H�v</font>
<form action="./market.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=defsyobun>
<input type=submit class=btn value="��������">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("����������܂���"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>$igold<>$ihit<>$ilv<>$iexp<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreedef.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freedef.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	open(IN,"./charalog/$i_id.cgi") || &error("�L�����N�^�[��������܂���$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	$eg="$charan[4]�l���o�i���Ă���$i_name $ibuki���A$chara[4]�l��$i_gold G�ōw�����܂����B";
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u���x����`�I<br>
�����������͂��񂽂̑q�ɂɑ����Ă�������I�v</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub acs {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreeacs.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freeacs.cgi");
		@item_chara = <IN>;
		close(IN);
	}
	$hit=0;$ii=0;

	foreach(@item_chara){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }
	if($i_id eq $chara[0]){

		&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u����͂��񂽂̏o�i�����������I<br>
�Ԃ����Ƃ͂ł��Ȃ����ȁA����Ȃ��Ȃ珈�����Ă�낤���H�v</font>
<form action="./market.cgi" method="post">
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=acssyobun>
<input type=submit class=btn value="��������">
</form>
<hr size=0>
EOM
	}else{

	if($chara[19] < $i_gold) { &error("����������܂���"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_acs,"$a_no<>$a_name<>$a_gold<>$a_kouka<>$a_0up<>$a_1up<>$a_2up<>$a_3up<>$a_4up<>$a_5up<>$a_hitup<>$a_kaihiup<>$a_wazaup<>$a_ex<>\n");

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreeacs.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freeacs.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	open(IN,"./charalog/$i_id.cgi") || &error("�L�����N�^�[��������܂���$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[88] -= 1;
	if($charan[88]<0){$charan[88]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	$eg="$charan[4]�l���t���[�}�[�P�b�g�ɏo�i���Ă���$a_name���A$chara[4]�l��$i_gold G�ōw���Ȃ����܂����B";
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u���x����`�I<br>
�����������͂��񂽂̑q�ɂɑ����Ă�������I�v</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub itemu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	$sgold = $in{'sgold'};

	if(!$soubi) {&error("�A�C�e��������܂���");}
	if(!$sgold) {&error("���z��ݒ肵�Ă�������");}

	$soubi-=1;

	if($in{'sgold'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}
	if($sgold > 2000000000){&error("�������܂��B�ő剿�i�͂Q�O���ł��B");}

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$hit=0;
	$iii=0;

	foreach(@souko_item){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
		if($soubi == $iii) { $hit=1;last; }
		$iii++;
	}
	if($hit==1 and $i_no == 1400){
		&error("���̑����͔���܂���I");
	}elsif($hit==1 and $i_name eq"���̌�"){
		&error("���̑����͔���܂���I");
	}
	if(!$hit){
		$ddd=0;
		$soubi-=100;
		foreach(@souko_def){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
			if($soubi == $ddd) { $hit=2;last; }
		$ddd++;
		}
	}
	if(!$hit){
		$aaa=0;
		$soubi-=100;
		foreach(@souko_acs){
($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($soubi == $aaa) { $hit=3;last; }
		$aaa++;
		}
	}

	if($hit==1){
		if($chara[70]<1){
			open(IN,"afreeitem.cgi");
			@item_chara = <IN>;
			close(IN);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(IN,"freeitem.cgi");
			@item_chara = <IN>;
			close(IN);
		}

		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("�����ɏo�i�ł��镐��̐��͂S�܂łł��B");}
		else{
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@item_chara,"$chara[0]<>$sgold<>$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><>$ilv<>$iexp<>\n");
		if($chara[70]<1){
			open(OUT,">afreeitem.cgi");
			print OUT @item_chara;
			close(OUT);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(OUT,">freeitem.cgi");
			print OUT @item_chara;
			close(OUT);
		}
		splice(@souko_item,$soubi,1);
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		}
	}elsif($hit==2){
		if($chara[70]<1){
			open(IN,"afreedef.cgi");
			@item_chara = <IN>;
			close(IN);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(IN,"freedef.cgi");
			@item_chara = <IN>;
			close(IN);
		}
		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("�����ɏo�i�ł���h��̐��͂S�܂łł��B");}
		else{
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@item_chara,"$chara[0]<>$sgold<>$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><>$ilv<>$iexp<>\n");
		if($chara[70]<1){
			open(OUT,">afreedef.cgi");
			print OUT @item_chara;
			close(OUT);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(OUT,">freedef.cgi");
			print OUT @item_chara;
			close(OUT);
		}
		splice(@souko_def,$soubi,1);
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		}
	}elsif($hit==3){
		if($chara[70]<1){
			open(IN,"afreeacs.cgi");
			@item_chara = <IN>;
			close(IN);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(IN,"freeacs.cgi");
			@item_chara = <IN>;
			close(IN);
		}
		$mankazu=@item_chara;
		if($mankazu>=30){splice(@item_chara,0,1);}
		$ckazu=0;
		foreach(@item_chara){
			@array = split(/<>/);
			if($array[0] eq $chara[0]){$ckazu+=1;}
		}
		$chara[88]=$ckazu;
		if($chara[88]>=4){&error("�����ɏo�i�ł���A�N�Z�T���[�̐��͂S�܂łł��B");}
		else{
		push(@item_chara,"$chara[0]<>$sgold<>$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		if($chara[70]<1){
			open(OUT,">afreeacs.cgi");
			print OUT @item_chara;
			close(OUT);
		}elsif($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(OUT,">freeacs.cgi");
			print OUT @item_chara;
			close(OUT);
		}
		splice(@souko_acs,$soubi,1);
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		}
	}else{
		&error("����ȃA�C�e���͑��݂��܂���");
	}
	$chara[88]++;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�t���[�}�[�P�b�g�ɏo�i���܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub itemsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreeitem.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freeitem.cgi");
		@item_chara = <IN>;
		close(IN);
	}
	$hit=0;$ii=0;

	foreach(@item_chara){
		($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreeitem.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freeitem.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u�������Ă������I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub defsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreedef.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freedef.cgi");
		@item_chara = <IN>;
		close(IN);
	}
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreedef.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freedef.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u�������Ă������I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub acssyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($chara[70]<1){
		open(IN,"afreeacs.cgi");
		@item_chara = <IN>;
		close(IN);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(IN,"freeacs.cgi");
		@item_chara = <IN>;
		close(IN);
	}
	$hit=0;$ii=0;

	foreach(@item_chara){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	if($chara[70]<1){
		open(OUT,">afreeacs.cgi");
		print OUT @item_chara;
		close(OUT);
	}elsif($chara[18]<1000){
		&error("���x��������܂���");
	}else{
		open(OUT,">freeacs.cgi");
		print OUT @item_chara;
		close(OUT);
	}

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u�������Ă������I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}