#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

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

if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="seizou.cgi" >
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

&haigo;

&error;

exit;

#----------#
#  �z����  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	if($chara[63]>=1){&error("�������ł��I�I");}

	&header;

	print <<"EOM";
<h1>������</h1>
<hr size=0>
<FONT SIZE=3>
<B>�������̃}�X�^�[</B><BR>
�u��H�A���܂�<B>$chara[4]</B>����Ȃ����B<br>
�����ł͐������ł��邺�E�E�E<br>
�����Ɏg�p����A�C�e���͍U��킩�Ȃ񂩂ŗp�ӂ��Ƃ��񂾂ȁB<br>
���ꂩ�E�E�E�܂��A�ł̑g�D���甃���Ă��������낤�c�B<br>
���������m���͂��悻75�����ĂƂ����B�܂����͂͐s�������B<br>
�܂��A�����΂̊����ƁA���ꍇ���΂ɂ�鐻���A�C�e���̐������ł��邼�B<br>
�����΂͂P��10���f�A���ꍇ���΂ɂ�鐻���i�̐����������͂V�T�����B<br>
����ɂ���ɁA�ŋ߉�ꂽ�����̃��T�C�N�����n�߂��񂾁B�������ŉ�ꂽ��A�����Ă����B<br>
�����A�C�e��������Ă�邺�H�������A�p���[�l���Ⴂ�Ɗm�����Ⴂ��ɗǂ������A�C�e���͂ł��Ȃ����B�v
</FONT>
<br>���݂̏������F$chara[19] �f<br>
�����΂̏����F$chara[99] ��<br>
��ꂽ�����̗݌v�p���[�F$chara[85]<br>
<br>
EOM
if($chara[99]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kankin">
<input type=submit class=btn value="�����Ί���">
</form>
EOM
}
if($chara[98]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tokusyu">
<input type=submit class=btn value="���ꍇ���ΐ���">
</form>
EOM
}
if($chara[85]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="recycle">
<input type=submit class=btn value="��ꂽ�����̃��T�C�N��">
</form>
EOM
}
if($chara[136]>=10){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kinka">
<input type=submit class=btn value="���݂P�O��������">
</form>
EOM
}
if($chara[18]>=100){
	print <<"EOM";
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="kaisya" value="1">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<input type=submit class=btn value="�ł̑g�D���獂�z�ōw��">
</td>
</form>
EOM
}
	print <<"EOM";
<table width = "100%">
<tr>
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="seizou">
<td width = "50%" align = "center" valign = "top">
�����g�p�i�m���P
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>������</th></tr>
EOM
	for ($i=71;$i<=82;$i++) {
		if($chara[$i]){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($syoukyu,$sno,$sname) = split(/<>/);
				if($sno eq $i){last;}
			}
			print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$sno">
</td>
<td class=b1 nowrap>$sname</td>
<td align=right class=b1>$chara[$i]</td>
</tr>
EOM
		}
	}
		print << "EOM";
</table>
</td>
<td width = "50%" align = "center" valign = "top">
�����g�p�i�m���Q
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>������</th></tr>
EOM
	for ($i=71;$i<=82;$i++) {
		if($chara[$i]){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($syoukyu2,$sno2,$sname2) = split(/<>/);
				if($sno2 eq $i){last;}
			}
			print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$sno2">
</td>
<td class=b1 nowrap>$sname2</td>
<td align=right class=b1>$chara[$i]</td>
</tr>
EOM
		}
	}
		print << "EOM";
</table>
</td>
<table>
<br><br>
<input type=submit class=btn value="��������">
</table>
</form>
</table>
EOM
if($chara[70]>=1 and $chara[18]>=100){
		print << "EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tsusinsell">
<table width="98%">
<tr><td class=b1 align=\"center\">�����F</td>
EOM
$hit=0;
for ($iti=71;$iti<=82;$iti++) {
	if($chara[$iti]){
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($itiyoukyu,$itino,$itiname) = split(/<>/);
			if($itino eq $iti){$hit=1;last;}
		}
		print "<td class=b1 align=\"center\"><input type=radio name=jibun value=\"$itino\"></td>";
		print "<td class=b1 align=\"center\">$itiname</td>";
	}
}
	print "</tr><tr><td class=b1 align=\"center\">����F</td>";
foreach(@seisan_data){
	($itiyoukyu,$ititno,$ititname) = split(/<>/);
	if($itino eq $iti){$hit=1;last;}
	print "<td class=b1 align=\"center\"><input type=radio name=aite value=\"$ititno\"></td>";
	print "<td class=b1 align=\"center\">$ititname</td>";
}
	print "</tr></table>";
if($hit){print "<p><input type=submit class=btn value=\"������������\"></form>";}
		print << "EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tsusinbuy">
<table width="40%">
<tr><th></th><th>���O</th><th>�A�C�e��</th><th>�Ώ�</th><th>�o�ߓ���</th></tr>
EOM
	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	$tx=0;
	foreach(@seizou_tsusin){
		($tsusinid,$tsusinname,$tsusinitem,$tsusinitemname,$tsusintaisyo,$tsusintaisyoname,$tsusintime) = split(/<>/);
		$tsusintime=int(($koktime-$tsusintime)/86400);
		if($tsusintime > 7){splice(@seizou_tsusin,$tx,1);}
			print << "EOM";
			<tr>
			<td class=b1 align="center">
EOM
			if($chara[0] ne $tsusinid){ print "<input type=radio name=tsusin value=\"$tx\">"; }
			print << "EOM";
			</td>
			<td class=b1 align="center">$tsusinname</td>
			<td class=b1 align="center">$tsusinitemname</td>
			<td align="center" class=b1>$tsusintaisyoname</td>
			<td align="center" class=b1>$tsusintime</td>
			</tr>
EOM
		$tx++;
	}
	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);
		print << "EOM";
</table><p>
<input type=submit class=btn value="��������">
</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	�@�@����  	   #
#--------------------------#
sub seizou {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$item_no1=$in{'item_no1'};
	$item_no2=$in{'item_no2'};
	if($item_no1 eq $item_no2 and $chara[$item_no1] < 2){&error("�����A�C�e���̐�������܂���B$back_form");}
	elsif($chara[$item_no1] <1 or $chara[$item_no2] < 1){&error("�����A�C�e���̐�������܂���B$back_form");}

	open(IN,"seizoudata.cgi");
	@seizou_data = <IN>;
	close(IN);

	$hit=0;
	foreach(@seizou_data){
		($bango1,$bango2,$ssno) = split(/<>/);
		if($bango1 eq $item_no1 and $bango2 eq $item_no2){$hit=1;last;}
		elsif($bango2 eq $item_no1 and $bango1 eq $item_no2){$hit=1;last;}
	}
	if(!$hit or !$ssno){&error("�����悪������܂���B$back_form");}
if(int(rand(4))<3){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_item_num = @souko_item;
	$souko_def_num = @souko_def;
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}
	if ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}
	if ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}
	if($ssno < 1000){
		open(IN,"$acs_file");
		@log_acs = <IN>;
		close(IN);

		$hit=0;
		foreach(@log_acs){
			($i_no,$i_name,$i_gold,$i_tokusyu,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$ihit,$i_kai,$i_hissatu,$i_setumei) = split(/<>/);
		if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("�A�N�Z��������܂���B$back_form");}
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno < 2000 and $ssno > 1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("���킪������܂���B$back_form");}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$seizouname=$i_name;
	}	
	elsif($ssno < 3000 and $ssno > 2000){
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($i_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("�h�������܂���B$back_form");}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno > 7000 and $ssno<8000){
		$ssno=$ssno-7000;
		$chara[$ssno]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$seizouname=$sname3;
	}
	else{&error("�A�C�e����������܂���I$back_form");}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l��$seizouname�̐����ɐ������܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

}else{$hh=1;$chara[85]+=1000;}

	$chara[$item_no1]-=1;
	$chara[$item_no2]-=1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($hh==0){
	print <<"EOM";
<FONT SIZE=3>
<B>�����ɐ������A$seizouname�𐻑����܂����B</B><BR>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>�����Ɏ��s���܂����B��</B><BR>
<hr size=0>
EOM
}
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	�����Ί���  	   #
#--------------------------#
sub kankin {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[99]){&error("�����΂�����܂���B$back_form");}

	$chara[99]-=1;

	$chara[19]+=100000;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�����΂��������A10���f���肵�܂����B</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	���ꍇ����  	   #
#--------------------------#
sub tokusyu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[98]){&error("���ꍇ���΂�����܂���B$back_form");}

	$chara[98]-=1;
	$rand=int(rand(100));$dhit=0;
	if($rand < 25){		$mes="�����Ɏ��s���܂����i���j";$dhit=1
	}elsif($rand < 75){	$mes="�Ő΂𐻑����܂����B";$chara[71]+=1;$seizouname="�Ő�";
	}elsif($rand < 85){	$mes="�������𐻑����܂����B";$chara[72]+=1;$seizouname="������";
	}elsif($rand < 90){	$mes="���΂𐻑����܂����B";$chara[73]+=1;$seizouname="����";
	}elsif($rand < 94){	$mes="�󓤂𐻑����܂����B";$chara[74]+=1;$seizouname="��";
	}elsif($rand < 97){	$mes="�_�[�N�}�^�[�𐻑����܂����B";$chara[75]+=1;$seizouname="�_�[�N�}�^�[";
	}elsif($rand < 99){	$mes="�Z�u���X�^�[�𐻑����܂����B";$chara[76]+=1;$seizouname="�Z�u���X�^�[";
	}else{			$mes="�M���΂𐻑����܂����B";$chara[77]+=1;$seizouname="�M����";
	}
	if($dhit==0){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l�����ꍇ���΂���$seizouname�̐����ɐ������܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	���T�C�N��  	   #
#--------------------------#
sub recycle {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[85]){&error("��ꂽ����������܂���B$back_form");}

	$rand=int(rand($chara[85]));
	$chara[85]=0;$dhit=0;
	if($rand < 25){		$mes="�����Ɏ��s���܂����i���j";$dhit=1;
	}elsif($rand < 250){	$mes="�Ő΂𐻑����܂����B";$chara[71]+=1;$seizouname="�Ő�";
	}elsif($rand < 2500){	$mes="�������𐻑����܂����B";$chara[72]+=1;$seizouname="������";
	}elsif($rand < 4500){	$mes="���΂𐻑����܂����B";$chara[73]+=1;$seizouname="����";
	}elsif($rand < 8000){	$mes="�󓤂𐻑����܂����B";$chara[74]+=1;$seizouname="��";
	}elsif($rand < 15000){	$mes="�_�[�N�}�^�[�𐻑����܂����B";$chara[75]+=1;$seizouname="�_�[�N�}�^�[";
	}elsif($rand < 20000){	$mes="�Z�u���X�^�[�𐻑����܂����B";$chara[76]+=1;$seizouname="�Z�u���X�^�[";
	}elsif($rand < 30000){	$mes="�M���΂𐻑����܂����B";$chara[77]+=1;$seizouname="�M����";
	}else{			$mes="�����̐΂𐻑����܂����B";$chara[78]+=1;$seizouname="�����̐�";
	}
	if($rand > 7500000){	$mes.="\n���������@�M�K�u���C�N���擾�����B";$chara[59]=51;}
	if($dhit==0){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l�����T�C�N���ɂ�$seizouname�̐����ɐ������܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	�ʐM���p  	   #
#--------------------------#
sub tsusinsell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	if(!$in{'jibun'}){&error("�����̕���I�����Ă��������B$back_form");}
	if(!$in{'aite'}){&error("����̕���I�����Ă��������B$back_form");}
	if($chara[$in{'jibun'}] < 1){&error("�����A�C�e���̐�������܂���B$back_form");}

	open(IN,"seisan.cgi");
	@seisan_data = <IN>;
	close(IN);
	foreach(@seisan_data){
		($ssyoukyu,$ssno,$ssname) = split(/<>/);
		if($in{'jibun'}==$ssno){$jibun=$ssname;}
		if($in{'aite'}==$ssno){$aite=$ssname;}
	}

	push(@seizou_tsusin,"$chara[0]<>$chara[4]<>$in{'jibun'}<>$jibun<>$in{'aite'}<>$aite<>$koktime<>\n");

	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);

	$chara[$in{'jibun'}]-=1;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�����������J�n���鏀�����I�����܂����B��͓����u�����҂�҂̂݁c�B</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	�ʐM�w��  	   #
#--------------------------#
sub tsusinbuy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	$tx=0;$hit=0;
	foreach(@seizou_tsusin){
		($tsusinid,$tsusinname,$tsusinitem,$tsusinitemname,$tsusintaisyo,$tsusintaisyoname) = split(/<>/);
		if($in{'tsusin'} == $tx){$hit=1;last;}
		$tx++;
	}
	if(!$hit){&error("�I�����Ă��܂���B$back_form");}
	$item_no1=$tsusinitem;
	$item_no2=$tsusintaisyo;
	if($chara[$item_no2] < 1){&error("�����A�C�e���̐�������܂���B$back_form");}

	splice(@seizou_tsusin,$tx,1);

	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);

	open(IN,"seizoudata.cgi");
	@seizou_data = <IN>;
	close(IN);

	$hit=0;
	foreach(@seizou_data){
		($bango1,$bango2,$ssno) = split(/<>/);
		if($bango1 eq $item_no1 and $bango2 eq $item_no2){$hit=1;last;}
		elsif($bango2 eq $item_no1 and $bango1 eq $item_no2){$hit=1;last;}
	}
	if(!$hit or !$ssno){&error("�����悪������܂���B$back_form");}
if(int(rand(4))<2){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	$lock_file = "$lockfolder/sitem$tsusinid.lock";
	&lock($lock_file,'ST');

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_item_num = @souko_item;
	$souko_def_num = @souko_def;
	$souko_acs_num = @souko_acs;

	open(IN,"$souko_folder/item/$tsusinid.cgi");
	@souko_item2 = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$tsusinid.cgi");
	@souko_def2 = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$tsusinid.cgi");
	@souko_acs2 = <IN>;
	close(IN);

	$souko_item_num2 = @souko_item2;
	$souko_def_num2 = @souko_def2;
	$souko_acs_num2 = @souko_acs2;

	if ($souko_item_num >= $item_max or $souko_item_num2 >= $item_max) {
		&error("����������̕���q�ɂ������ς��ł��I$back_form");
	}
	if ($souko_def_num >= $def_max or $souko_def_num2 >= $def_max) {
		&error("����������̖h��q�ɂ������ς��ł��I$back_form");
	}
	if ($souko_acs_num >= $acs_max or $souko_acs_num2 >= $acs_max) {
		&error("����������̃A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}
	if($ssno < 1000){
		open(IN,"$acs_file");
		@log_acs = <IN>;
		close(IN);

		$hit=0;
		foreach(@log_acs){
			($i_no,$i_name,$i_gold,$i_tokusyu,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$ihit,$i_kai,$i_hissatu,$i_setumei) = split(/<>/);
		if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("�A�N�Z��������܂���B$back_form");}
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		push(@souko_acs2,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$tsusinid.cgi");
		print OUT @souko_acs2;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno < 2000 and $ssno > 1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("���킪������܂���B$back_form");}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		push(@souko_item2,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$tsusinid.cgi");
		print OUT @souko_item2;
		close(OUT);
		$seizouname=$i_name;
	}	
	elsif($ssno < 3000 and $ssno > 2000){
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($i_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("�h�������܂���B$back_form");}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		push(@souko_def2,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$tsusinid.cgi");
		print OUT @souko_def2;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno > 7000 and $ssno<8000){
		$ssno=$ssno-7000;
		$chara[$ssno]+=1;
			$lock_file = "$lockfolder/$tsusinid.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$tsusinid.cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$tsusinid.lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);
			$mem1[$ssno]+=1;
			$new_chara = '';

			$new_chara = join('<>',@mem1);

			$new_chara .= '<>';

			open(OUT,">./charalog/$tsusinid.cgi");
			print OUT $new_chara;
			close(OUT);
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$seizouname=$sname3;
	}
	else{&error("�A�C�e����������܂���I$back_form");}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l��$tsusinname�l�Ƌ�����$seizouname�̐����ɐ������܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

}else{
		$hh=1;
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]�l��$tsusinname�l�Ƌ�����$seizouname�̐����ɒ��킵�܂��������s���܂����c�B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
}

	$chara[$item_no2]-=1;

	&unlock($lock_file,'ST');
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($hh==0){
	print <<"EOM";
<FONT SIZE=3>
<B>�����ɐ������A$tsusinname�l�Ƌ�����$seizouname�𐻑����܂����B</B><BR>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>�����Ɏ��s���܂����B��</B><BR>
<hr size=0>
EOM
}
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
if($in{'ok'}==1){
	$ps_gold = $chara[18]*10000;
	if($in{'kaisya'}!=1){&error("�G���[�ł񂪂ȁB");}
	if($chara[19] < $ps_gold) { &error("����������܂���"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;
if(int(rand(2))!=1){
	$ps_no=71+int(rand(12));
	if($ps_no>71){
	$ps_no=71+int(rand(12));
	if($ps_no>72){
	$ps_no=71+int(rand(12));
	if($ps_no>73){
	$ps_no=71+int(rand(12));
	if($ps_no>74){
	$ps_no=71+int(rand(12));
	if($ps_no>75){
	$ps_no=71+int(rand(12));
	if($ps_no>76){
	$ps_no=71+int(rand(12));
	if($ps_no>77){
	$ps_no=71+int(rand(12));
	if($ps_no>78){
	$ps_no=71+int(rand(12));
	if($ps_no>79){
	$ps_no=71+int(rand(12));
	if($ps_no>80){
	$ps_no=71+int(rand(12));
	if($ps_no>81){
	$ps_no=71+int(rand(12));
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	if($chara[70]>1 and $ps_no<80){$ps_no+=int(rand(4));}
	$chara[$ps_no] += 1;
}else{
	$bossyu=$chara[34]+$chara[19];
	$chara[93]=$bossyu;
	$chara[34]=0;
	$chara[19]=0;
	$chara[84]=1;
	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=2;
	$chara[65]+=2;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>��@��Ђ������悤��!!!!�m���Ă�����!!!!<br>
$chara[4]�͑ߕ߂���A�S�Ă̏�������v�����ꂽ�I�I�I�I���l�ɓ���߂Â��܂����B�C�����ĂˁB</B><BR>
</font>
<hr size=0>
EOM
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]�l���ߕ߂���܂����B�v�����z�F$bossyu�f�B";

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

	exit;

}
	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���������i����ɓ��ꂽ�B</B><BR>
</font>
<hr size=0>
EOM
}else{
	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�{���ɔ����܂����H</B><BR>
</font>
<hr size=0>
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="kaisya" value="1">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<input type=hidden name=ok value=1>
<input type=submit class=btn value="�ł̑g�D���獂�z�ōw��">
</td>
</form>
EOM
}

	&shopfooter;

	&footer;

	exit;
}
sub kinka {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[136]<10){&error("���݂�����܂���");}
	else{
		$chara[136]-=10;
		$chara[85]+=2000000;
	}

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�΂��΂��A���݁B</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}