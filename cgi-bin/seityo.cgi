#!/usr/local/bin/perl

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
<form action="seityo.cgi" >
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

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
	if($item[20]==10){$g="red";}else{$g="";}
	if($item[22]==10){$w="red";}else{$w="";}
	if($chara[24]<1016){$rare1=1;}
	elsif($chara[24]<1031){$rare1=2;}
	elsif($chara[24]<1046){$rare1=3;}
	elsif($chara[24]<1061){$rare1=4;}
	elsif($chara[24]<1076){$rare1=5;}
	else{$rare1=10;}
	if($chara[29]<2016){$rare2=1;}
	elsif($chara[29]<2031){$rare2=2;}
	elsif($chara[29]<2046){$rare2=3;}
	elsif($chara[29]<2061){$rare2=4;}
	elsif($chara[29]<2076){$rare2=5;}
	else{$rare2=10;}
	$bukikoka = "�U���� $item[1]<br>������ $item[2]<br>���� $item[24]";
	$bogukoka = "�h��� $item[4]<br>��� $item[5]<br>���� $item[25]";
	$acskoka = "���� $item[19]";

	&header;

	print <<"EOM";
<h1>������</h1>
<hr size=0>

<FONT SIZE=3>
<B>�������̐l</B><BR>
�u�����𐬒������邱�Ƃ��ł��邼�B�l�i�́A�����N�~100000�f�����A����ȑ�����1000000G�����B<br>
�������邩�ǂ����́A�����̋����A�����ĉ^���悾���B�H�ɉ��邩�璍�ӂ���񂾂Ȃ�<br>
�������{�^�����ƁA��������m�����オ��B����ɉ���m�����オ�邼�B�v
</FONT><br>
�������F$chara[19]G
<br><hr>���݂̑���<br>
<table>
<tr>
<td id="td2" class="b2">����</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
EOM
	if ($chara[24] > 1090 and $chara[24] < 1101){
	}elsif($chara[24] > 1200 and $chara[24] < 1228){
	}elsif ($chara[24] and $chara[24]>0 and $chara[24]<4000 and $chara[19]>$rare1*100000 and $chara[24]!=1400) {
	print <<"EOM";
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=submit class=btn value="����">
</td>
</form>
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_kaji">
<input type=hidden name=kou value=1>
<input type=submit class=btn value="������">
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
	if ($chara[29] > 2090 and $chara[29] < 2101){
	}elsif($chara[29] > 2200 and $chara[29] < 2228){
	}elsif ($chara[29] and $chara[29]>0 and $chara[29]<4000 and $chara[19] > $rare2*100000) {
	print <<"EOM";
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=submit class=btn value="����">
</td>
</form>
<form action="seityo.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="def_kaji">
<input type=hidden name=kou value=1>
<input type=submit class=btn value="������">
</td>
</form>
EOM
	}
	print <<"EOM";
</tr>
</table>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#------------#
#  ���푕��  #
#------------#
sub item_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[24]==1240 and $chara[135]>2){$rare1=1000000;}
	elsif($chara[24]<1016){$rare1=1;}
	elsif($chara[24]<1031){$rare1=2;}
	elsif($chara[24]<1046){$rare1=3;}
	elsif($chara[24]<1061){$rare1=4;}
	elsif($chara[24]<1076){$rare1=5;}
	else{$rare1=10;}

	if($chara[19] < $rare1*100000){&error("����������܂����[�B");}
	else{$chara[19] -= $rare1*100000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[20]<5){$ss=20;}
	elsif($item[20]<7){$ss=30;}
	elsif($item[20]<9){$ss=40;}
	elsif($item[20]<11){$ss=50;}
	$kowa=0;
	if($in{'kou'}==1){$ss+=10;$kowa=5;}
	if($rr<$ss+2 or $chara[93]){
		$chara[24]+=1;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit,$si_koka) = split(/<>/);
			if($chara[24]==1241 and $chara[135]>2){
				$chara[24]=1339;
				$item[0]="����";
				$item[1]=0;
				$item[2]=0;
				$item[20]=0;
				$item[21]=0;
				$si_koka="���Ŏ������(�H)";
				$item[24]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[24] == 1005 and $in{'kou'}==1){
				$chara[24]=1131;
				$item[0]="�������イ";
				$item[1]=1;
				$item[2]=-100;
				$item[20]=0;
				$item[21]=0;
				$si_koka="�����X�^�[��߂炦���邼���I";
				$item[24]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[24] eq "$si_no"){
				$item[0]=$si_name;
				$item[1]=$si_dmg;
				$item[2]=$si_hit;
				$item[20]=0;
				$item[21]=0;
				if(!$si_koka){$si_koka="���ɂȂ�";}
				$item[24]=$si_koka;
				$hit=1;
				last;
			}
		}
		if(!$hit) {$chara[24]-=1;}
		$mes="�����ɐ������܂���";
	}else{
		if(int(rand(10))>$kowa){$mes="�����Ɏ��s���܂���";
		}else{
		if($item[1]>504){$chara[85]+=50000;}
		elsif($item[1]>203){$chara[85]+=10000;}
		elsif($item[1]>152){$chara[85]+=1000;}
		elsif($item[1]>93){$chara[85]+=300;}
		elsif($item[1]>43){$chara[85]+=75;}
		else{$chara[85]+=1;}
		&item_lose;
		$chara[24]=0;
		$mes="�����Ɏ��s���A����ɉ��Ă��܂����I�I";
		}
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

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

#------------#
#  �h���  #
#------------#
sub def_kaji {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;
	if($chara[29]<2016){$rare2=1;}
	elsif($chara[29]<2031){$rare2=2;}
	elsif($chara[29]<2046){$rare2=3;}
	elsif($chara[29]<2061){$rare2=4;}
	elsif($chara[29]<2076){$rare2=5;}
	else{$rare2=10;}

	if($chara[19] < $rare2*100000){&error("����������܂����[�B");}
	else{$chara[19] -= $rare2*100000;}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$rr=int(rand(100));
	if($item[22]<5){$ss=20;}
	elsif($item[22]<7){$ss=30;}
	elsif($item[22]<9){$ss=40;}
	elsif($item[22]<11){$ss=50;}
	$kowa=0;
	if($in{'kou'}==1){$ss+=10;$kowa=5;}
	if($rr<$ss+2 or $chara[93]){
		$chara[29]+=1;
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit,$si_koka) = split(/<>/);
			if($chara[29] == 2132 and $in{'kou'}==1){
				$chara[29]=2134;
				$item[3]="���p�X�q";
				$item[4]=208;
				$item[5]=70;
				$item[22]=0;
				$item[23]=0;
				$si_koka="�����������X�q";
				$item[25]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[29] == 2133 and $in{'kou'}==1){
				$chara[29]=2143;
				$item[3]="���~�b�^�[";
				$item[4]=500;
				$item[5]=50;
				$item[22]=0;
				$item[23]=0;
				$si_koka="����̈󂪂���B";
				$item[25]=$si_koka;
				$hit=1;
				last;
			}elsif($chara[29] eq "$si_no"){
				$item[3]=$si_name;
				$item[4]=$si_dmg;
				$item[5]=$si_hit;
				$item[22]=0;
				$item[23]=0;
				if(!$si_koka){$si_koka="���ɂȂ�";}
				$item[25]=$si_koka;
				$hit=1;
				last;
			}
		}
		if(!$hit) {$chara[29]-=1;}
		$mes="�����ɐ������܂���";
	}else{
		if(int(rand(10))>$kowa){
			$mes="�����Ɏ��s���܂���";
		}else{
		if($item[4]>704){$chara[85]+=50000;}
		elsif($item[4]>404){$chara[85]+=10000;}
		elsif($item[4]>199){$chara[85]+=1000;}
		elsif($item[4]>103){$chara[85]+=100;}
		elsif($item[4]>52){$chara[85]+=10;}
		else{$chara[85]+=1;}
		&def_lose;
		$chara[29]=0;
		$mes="�����Ɏ��s���A����ɉ��Ă��܂����I�I";
		}
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

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