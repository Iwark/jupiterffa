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
<form action="yashiki.cgi" >
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

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	$chara[186]=0;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&chara_load;

	&header;
if($chara[181]==0){
	print <<"EOM";
<h1>�s�v�c�ȉ��~</h1>
<hr size=0>

<FONT SIZE=3>
<B>�H�H�H�H</B><BR>
�u�悭�����B���̉��~�́A�댯���s�v�c�ȉ��~���c�B<br>
�ʂĂ��Ȃ��������̉��~�ł́A����i�ނ��Ƃɏ�������100���f�����Ă����Ƃ����c�B<br>
����ɁA���̉��~�ɂ͐��X�̋��낵���g���b�v������A�������蔲�����҂������A���������ł���炵���c<br>
�Ƃ������A�������i�ނȂ�A�������ƁA�g���b�v�ɋC������񂾂��c�B�v
</FONT><br>
�������F$chara[19]G
<br>
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu">
<input type=submit class=btn value="�i��">
</td>
</form>
EOM
}else{
$x=$chara[183]-$chara[185];
$y=$chara[182]-$chara[184];
	print <<"EOM";
<h1>���݈ʒu�F($x , $y)</h1>
<hr size=0>
�������F$chara[19]G
<br>
EOM
if($chara[181]>=8){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=182>
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="�k�֐i��">
</td>
</form>
EOM
}
if($chara[181] % 8 >= 1){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=183>
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="���֐i��">
</td>
</form>
EOM
}
if($chara[181] % 4 >= 1){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=184>
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="��֐i��">
</td>
</form>
EOM
}
if($chara[181] % 2 >= 1){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=185>
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="���֐i��">
</td>
</form>
EOM
}
if($chara[187]>100000000){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=1>
<input type=hidden name=mode value="susumu3">
<input type=submit class=btn value="������܂Ŗ߂�">
</td>
</form>
EOM
}
if($chara[187]>1000000000){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=2>
<input type=hidden name=mode value="susumu3">
<input type=submit class=btn value="�W�����v�b�I(300���f)">
</td>
</form>
EOM
}
if($chara[187]>3000000000){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=3>
<input type=hidden name=mode value="susumu3">
<input type=submit class=btn value="���݈ʒu�T�m(300���f)">
</td>
</form>
EOM
}
if($chara[187]>3200000000){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=4>
<input type=hidden name=mode value="susumu3">
<input type=submit class=btn value="����T�m�@(1000���f)">
</td>
</form>
EOM
}
if($chara[187]>5000000000){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=susumi value=5>
<input type=hidden name=mode value="susumu3">
<input type=submit class=btn value="�V���b�t���I�I(2000���f)">
</td>
</form>
EOM
}
}
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="yashiki.cgi" >
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu4">
<input type=submit class=btn value="�m���v�Z">
</td>
</form>
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#------------#
#  ���푕��  #
#------------#
sub susumu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19]<1000000){&error("����������܂���B");}
	else{$chara[19]-=1000000;$chara[187]+=1000000;}

	$chara[26] = $host;
	$hit=0;
	if(int(rand(2))==0){
		$hit=1;
		$chara[181]+=8;
	}
	if(int(rand(2))==0){
		$hit=1;
		$chara[181]+=4;
	}
	if(int(rand(2))==0){
		$hit=1;
		$chara[181]+=2;
	}
	if(int(rand(2))==0){
		$hit=1;
		$chara[181]+=1;
	}
	if($hit==1){
		$mes="��̉��~�̉��ւƐi�݂܂����c";
	}else{$mes="�i�񂾂�s���~�܂肾�����c����Ȃ������c";}
	if($chara[187]>100000000 and int(rand(10))==0){
		$mes.="�܂��͐��Ɠ��ɂS���炢�i��ł݂�̂��������ȁc�B�k���̓����o�Ȃ���Ηǂ����c�B";
	}
	if($chara[187]>300000000 and int(rand(10))==0){
		$mes.="��ɂb������؂ł����肵����ǂ����H";
	}
	if($chara[187]>500000000 and int(rand(10))==0){
		$mes.="�k���ɂ΂���i�ݑ����Ă݂�̂������ȁc�B�ǂ������ɏo��邩������Ȃ��c�B";
	}
	if($chara[187]>1000000000 and int(rand(10))==0){
		$mes.="���~��ɂȂ��̂�(-3,0)�B�k�Ɠ�ւ͂S��A���Ɛ��ւ͉��񂾂������ȁc�B";
	}
	if($chara[187]>10000000000 and int(rand(10))==0){
		$mes.="�A�C�@�C�B�C�@";
	}
	if($chara[187]>15000000000 and int(rand(10))==0){
		$mes.="�C�C�E�C�C�C�E";
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yashiki.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub susumu2 {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19]<1000000){&error("����������܂���B");}
	else{$chara[19]-=1000000;$chara[187]+=1000000;}
	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$souko_item_num = @souko_item;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);
	$souko_def_num = @souko_def;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if($chara[186]==1){&error("�X�V�{�^���͋֎~��ŁB");}
	elsif ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}
	elsif ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I");
	}
	elsif ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}
else{
	if($in{'susumi'}<1){&error("�G���[�B�����ƑI�����Ă�");}

	if(int(rand(50))==0){
		$chara[182]+=int(rand(11)-5);
		$chara[183]+=int(rand(11)-5);
		$chara[184]+=int(rand(11)-5);
		$chara[185]+=int(rand(11)-5);
		if($chara[182]<0){$chara[182]=0;}
		if($chara[183]<0){$chara[183]=0;}
		if($chara[184]<0){$chara[184]=0;}
		if($chara[185]<0){$chara[185]=0;}
		$c=1;
	}
	$chara[$in{'susumi'}]+=1;
	$chara[181]=0;
	$hit=0;$dx=0;
	if($chara[0] eq "jupiter"){$dx+=20;}
	if ($hour == 18){$dx+=5;}
	if($chara[182]>0 and $chara[183]>0 and $chara[184]>0 and $chara[185]>0){$dx+=10;}
	if($chara[182]>1 and $chara[183]>1 and $chara[184]>1 and $chara[185]>1){$dx+=8;}
	if($chara[182]>2 and $chara[183]>2 and $chara[184]>2 and $chara[185]>2){$dx+=6;}
	if($chara[182]>3 and $chara[183]>3 and $chara[184]>3 and $chara[185]>3){$dx+=4;}
	if($chara[182]+$chara[183]+$chara[184]+$chara[185]<4){$dx+=10;}
	if($chara[182]+$chara[183]+$chara[184]+$chara[185]>10){$dx-=10;}
	if($chara[182]+$chara[183]+$chara[184]+$chara[185]>20){$dx-=10;}
	if($chara[182]+$chara[183]+$chara[184]+$chara[185]>30){$dx-=20;}
	if(int(rand(100))<39+$dx){
		$hit=1;
		$chara[181]+=8;
	}
	if(int(rand(100))<34+$dx){
		$hit=1;
		$chara[181]+=4;
	}
	if(int(rand(100))<44+$dx){
		$hit=1;
		$chara[181]+=2;
	}
	if(int(rand(100))<34+$dx){
		$hit=1;
		$chara[181]+=1;
	}
	if($hit==1){
		if($c!=1){$mes="��̉��~�̉��ւƐi�݂܂����c<br>";}
		else{$c=0;$mes="�ǂ����Ƀ��[�v�����݂������I<br>";}
		$x=$chara[183]-$chara[185];
		$y=$chara[182]-$chara[184];
		if($chara[182]==1 and $chara[183]==1 and $chara[184]==1 and $chara[185]==1){
			$mes.="����Ɓc�Ȃ�ƁA500���f�𔭌������I<br>";
			$chara[19]+=5000000;
		}
		if($chara[182]==2 and $chara[183]==1 and $chara[184]==3 and $chara[185]==1){
			$rti=int(rand(3));
			if($rti==0){$i_no=2130;}
			elsif($rti==1){$i_no=2139;}
			else{$i_no=2141;}
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		if($chara[182]==4 and $chara[183]==6 and $chara[184]==4 and $chara[185]==9){
			if($chara[33]<100){
				$mes.="����Ɓc�Ȃ�ƁA���~��m�ɓ]���c�ł��Ȃ������B";
			}else{
				$mes.="����Ɓc�Ȃ�ƁA���~��m�ɓ]�������I";
				$chara[14]=44;
				$chara[33]=1;
				$lock_file = "$lockfolder/messa$in{'id'}.lock";
				&lock($lock_file,'MS');
		
				open(IN,"$chat_file");
				@chat_mes = <IN>;
				close(IN);
				$mes_sum = @chat_mes;
				if($mes_sum > $mes_max) { pop(@chat_mes); }
				($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
				$mon = $mon+1;$year = $year +1900;
				$eg="$chara[4]�l�����~��ɂȂ�܂����B";
				unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

				open(OUT,">$chat_file");
				print OUT @chat_mes;
				close(OUT);

				&unlock($lock_file,'MS');
			}
		}
		if($x==4 and $y==6){
			$mes.="����Ɓc�Ȃ�ƁA�_��̗͂ł`�o���ق�̏����オ�����I<br>";
			$chara[13]+=1;
		}
		if($chara[182]>9 and int(rand(8))==1){
			$mes.="����Ɓc�Ȃ�ƁA�_��̗͂ł`�o�������オ�����I<br>";
			$chara[13]+=int(rand(3)+1);
		}
		if($chara[183]>7 and $chara[185]>7 and $chara[182]<2 and $chara[184]<2 and int(rand(10))==0){
			$i_no=1133;
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		if($chara[182]>10 and $chara[184]>10 and int(rand(10))==0){
			$i_no=1133;
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		if($chara[182]>7 and $chara[183]==0 and $chara[184]==0 and $chara[185]>7 and int(rand(3))==1){
			$i_no=2145;
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		if($chara[183]>19 and int(rand(8))==1){
		if(int(rand(2))==0){
			$i_no=1121;
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}else{
			$i_no=2121;
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		}
		if($chara[183]>9 and int(rand(8))==1){
		if(int(rand(2))==0){
			$i_no=1046+int(rand(36));
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}else{
			$i_no=2046+int(rand(30));
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
		}
		}
		if($chara[182]<3 and $chara[183]>3 and $chara[184]<3 and $chara[185]>3 and int(rand(10))==0){
			$i_no="0029";
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $i_no){last;}
			}
			push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$ai_name���������I<br>";
		}
		if($chara[182]<3 and $chara[183]>6 and $chara[184]<3 and $chara[185]>6 and int(rand(10))==0){
			$i_no="0031";
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $i_no){last;}
			}
			push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
			$mes.="����Ɓc�Ȃ�ƁA$ai_name���������I<br>";
		}
		if($chara[184]>9 and int(rand(8))==1){
			$kane=int(rand(1000)+1);
			$mes.="����Ɓc�Ȃ�ƁA$kane���f�𔭌������I<br>";
			$chara[19]+=$kane * 10000;
		}
		if($chara[185]>9 and int(rand(12))==1){
			$ssno=int(rand(6)+71);
			if(int(rand(4))==0){$ssno+=int(rand(2));}
			if(int(rand(5))==0){$ssno+=int(rand(4));}
			if(int(rand(6))==0){$ssno+=int(rand(4));}
			$chara[$ssno]+=1;
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($syoukyu3,$sno3,$sname3) = split(/<>/);
				if($sno3 eq $ssno){last;}
			}
			$mes.="����Ɓc�Ȃ�ƁA$sname3�𔭌������I<br>";
		}
		if($chara[182]==4 and $chara[183]==0 and $chara[184]==0 and $chara[185]==4){
			$mes.="����Ɓc�Ȃ�ƁA���i���傫���P�ɌX������<br>";
			if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
			$chara[65]-=30;
			$chara[64]+=30;
			if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
			if($chara[65]<0){$chara[65]=0;}
			if($chara[64]>100){$chara[64]=100;}
		}
		if($chara[182]==0 and $chara[183]==5 and $chara[184]==5 and $chara[185]==0){
			$mes.="����Ɓc�Ȃ�ƁA���i���傫�����ɌX������<br>";
			if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
			$chara[64]-=30;
			$chara[65]+=30;
			if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
			if($chara[64]<0){$chara[64]=0;}
			if($chara[65]>100){$chara[65]=100;}
		}
	}else{
		$mes="�i�񂾂�s���~�܂肾�����c����Ȃ������c";
		$chara[182]=0;$chara[183]=0;$chara[184]=0;$chara[185]=0;
	}
	$chara[186]=1;
	&chara_regist;
}
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yashiki.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub susumu3 {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'susumi'}==1){
		if($chara[19]<1000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=1000000;
			$chara[187]+=1000000;
		}
	}elsif($in{'susumi'}==2 or $in{'susumi'}==3){
		if($chara[19]<3000000){
			&error("����������܂���B");
		}elsif($in{'susumi'}==3){
			$chara[19]-=3000000;
		}else{
			$chara[19]-=3000000;
			$chara[187]+=3000000;
		}
	}elsif($in{'susumi'}==4){
		if($chara[19]<10000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=10000000;
			$chara[187]+=10000000;
		}
	}elsif($in{'susumi'}==5){
		if($chara[19]<20000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=20000000;
			$chara[187]+=20000000;
		}
	}else{&error("�G���[");}
	

	$chara[26] = $host;
	$hit=0;
	if($in{'susumi'}==1){
		$hit=1;
		$chara[181]=0;
		$chara[182]=0;
		$chara[183]=0;
		$chara[184]=0;
		$chara[185]=0;
	}elsif($in{'susumi'}==2){
		$chara[182]+=int(rand(9)-4);
		$chara[183]+=int(rand(9)-4);
		$chara[184]+=int(rand(9)-4);
		$chara[185]+=int(rand(9)-4);
		if($chara[182]<0){$chara[182]=0;}
		if($chara[183]<0){$chara[183]=0;}
		if($chara[184]<0){$chara[184]=0;}
		if($chara[185]<0){$chara[185]=0;}
		$chara[181]=int(rand(19)-3);
		if($chara[181]<1){
			$chara[182]=0;
			$chara[183]=0;
			$chara[184]=0;
			$chara[185]=0;
			$hit=2;
			$chara[181]=0;
		}else{
			if($chara[181]>3){
				$chara[181]-=3;
			}
			$hit=3;
		}
	}elsif($in{'susumi'}==3){
		$hit=4;
	}elsif($in{'susumi'}==4){
		$hit=5;
	}elsif($in{'susumi'}==5){
		$chara[181]=int(rand(17)-1);
		if($chara[181]<1){
			$chara[182]=0;
			$chara[183]=0;
			$chara[184]=0;
			$chara[185]=0;
			$hit=6;
			$chara[181]=0;
		}else{
			if($chara[181]>3){
				$chara[181]-=3;
			}
			$hit=7;
		}
	}else{
		&error("�G���[�B");
	}
	
	if($hit==1){
		$mes="���~�̓�����܂Ŗ߂�܂����B";
	}elsif($hit==2){
		$mes="�W�����v������A�s���~�܂肾�����c�G";
	}elsif($hit==3){
		$mes="�W�����v���܂����B";
	}elsif($hit==4){
		$mes="���݈ʒu�́A�k�F$chara[182]�G���F$chara[183]�G��F$chara[184]�G���F$chara[185]";
	}elsif($hit==5){
		if($chara[0] eq "jupiter"){
		$mes = << "EOM";
		<table>
		<tr><th>�k</th><th>��</th><th>��</th><th>��</th><th>��V</th></tr>
		<tr><th>7��</th><th>0</th><th>0</th><th>7��</th><th>�L�Z</th></tr>
		<tr><th>4</th><th>0</th><th>0</th><th>4</th><th>�P�|�C���g�{�R�O</th></tr>
		<tr><th>0</th><th>5</th><th>5</th><th>0</th><th>���|�C���g�{�R�O</th></tr>
		<tr><th>1</th><th>1</th><th>1</th><th>1</th><th>500���f</th></tr>
		<tr><th>2</th><th>1</th><th>3</th><th>1</th><th>���ʂ̏��E���d�̊Z�E�O�p�X�q</th></tr>
		<tr><th>4</th><th>6</th><th>4</th><th>9</th><th>���~��</th></tr>
		<tr><th>9��</th><th>�~</th><th>�~</th><th>�~</th><th>�_��̗�(AP+)</th></tr>
		<tr><th>2��</th><th>7��</th><th>2��</th><th>7��</th><th>�y�b�g�j�E��</th></tr>
		<tr><th>10��</th><th>�~</th><th>10��</th><th>�~</th><th>�y�b�g�j�E��</th></tr>
		<tr><th>�~</th><th>19��</th><th>�~</th><th>�~</th><th>���~����</th></tr>
		<tr><th>�~</th><th>9��</th><th>�~</th><th>�~</th><th>����</th></tr>
		<tr><th>3��</th><th>3��</th><th>3��</th><th>3��</th><th>�n�̕�</th></tr>
		<tr><th>3��</th><th>6��</th><th>3��</th><th>6��</th><th>�w�K���u</th></tr>
		<tr><th>�~</th><th>�~</th><th>9��</th><th>�~</th><th>��</th></tr>
		<tr><th>�~</th><th>�~</th><th>�~</th><th>9��</th><th>�����i</th></tr>
		</table>
EOM
		}else{
			$mes = "<table><tr><th>�k</th><th>��</th><th>��</th><th>��</th><th>��V</th></tr>";
	if(int(rand(1000))==0){$mes .= "<tr><th>7��</th><th>0</th><th>0</th><th>7��</th><th>�L�Z</th></tr>";}
	if(int(rand(1000))==0){$mes .= "<tr><th>4</th><th>0</th><th>0</th><th>4</th><th>�P�|�C���g�{�R�O</th></tr>";}
	if(int(rand(1000))==0){$mes .= "<tr><th>0</th><th>5</th><th>5</th><th>0</th><th>���|�C���g�{�R�O</th></tr>";}
	if($hour<2){$mes .= "<tr><th>1</th><th>1</th><th>1</th><th>1</th><th>500���f</th></tr>";}
	if($hour<4){$mes .= "<tr><th>2</th><th>1</th><th>3</th><th>1</th><th>���ʂ̏��E���d�̊Z�E�O�p�X�q</th></tr>";}
	if($hour<6){$mes .= "<tr><tr><th>4</th><th>6</th><th>4</th><th>9</th><th>���~��</th></tr></tr>";}
	if($hour<8){$mes .= "<tr><tr><th>9��</th><th>�~</th><th>�~</th><th>�~</th><th>�_��̗�(AP+)</th></tr></tr>";}
	if($hour<10){$mes .= "<tr><tr><th>2��</th><th>7��</th><th>2��</th><th>7��</th><th>�y�b�g�j�E��</th></tr></tr>";}
	if($hour<12){$mes .= "<tr><tr><th>10��</th><th>�~</th><th>10��</th><th>�~</th><th>�y�b�g�j�E��</th></tr></tr>";}
	if($hour<14){$mes .= "<tr><tr><th>�~</th><th>19��</th><th>�~</th><th>�~</th><th>���~����</th></tr></tr>";}
	if($hour<16){$mes .= "<tr><tr><th>�~</th><th>9��</th><th>�~</th><th>�~</th><th>����</th></tr></tr>";}
	if($hour<18){$mes .= "<tr><tr><th>3��</th><th>3��</th><th>3��</th><th>3��</th><th>�n�̕�</th></tr></tr>";}
	if($hour<20){$mes .= "<tr><tr><th>3��</th><th>6��</th><th>3��</th><th>6��</th><th>�w�K���u</th></tr></tr>";}
	if($hour<22){$mes .= "<tr><tr><th>�~</th><th>�~</th><th>9��</th><th>�~</th><th>��</th></tr></tr>";}
	if($hour<24){$mes .= "<tr><tr><th>�~</th><th>�~</th><th>�~</th><th>9��</th><th>�����i</th></tr></tr>";}
			$mes .= "</table>";
		}
	}elsif($hit==6){
		$mes="�V���b�t�����s�b�I�I(��)";
	}elsif($hit==7){
		$mes="�V���b�t�����܂����B";
	}else{$mes="�i�񂾂�s���~�܂肾�����c����Ȃ������c";}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yashiki.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub susumu4 {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	# ������ɓ���B
	$stop0=int( 0.5 * 0.5 * 0.5 * 0.5 * 1000 ) / 10;
	$mes="������ōs���~�܂�ɂȂ�m����<font size=6 color=\"red\">$stop0��</font>�ł��B<br>";
	$ok=100-$stop0;
	$mes.="�]���āA�i�s�m����<font size=6 color=\"red\">$ok��</font>�ł��B<br>";
	$cost0=(10000 * $ok) + (20000 * $stop0) + (300 * $stop0 * $stop0);
	$kane0=int($cost0/10000);
	$mes.="�������˔j����̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane0���f</font>�ł��B<br>";
	$mes.="�ȉ��A�P�W���`�P�X���̐i�s�m���t�o�^�C���ɍs�������̂Ƃ��܂�<br>";

	$mes.="�P���`�W��<br>";
	$stop1=int( 0.46 * 0.51 * 0.41 * 0.51 * 1000 ) / 10;
	$ok1=100-$stop1;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok1��</font>�ł��B<br>";
	$ok1=$ok1/100;
	$ok=$ok/100*($ok1 ** 8);
	$ok11=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok11��</font>�ł��B<br>";
	$stop11=100-$ok11;
	$cost1=(80000 * $ok11) + (160000 * $stop11) + (2400 * $stop11 * $stop11) + (32 * $stop11 ** 3);
	$kane1=int($cost1/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane1���f</font>�ł��B<br>";

	$mes.="�X���`�P�O��<br>";
	$stop2=int( 0.38 * 0.43 * 0.33 * 0.43 * 1000 ) / 10;
	$ok2=100-$stop2;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok2��</font>�ł��B<br>";
	$ok2=$ok2/100;
	$ok=$ok*($ok2 ** 2);
	$ok22=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok22��</font>�ł��B<br>";
	$stop22=100-$ok22;
	$cost2=(100000 * $ok22) + (200000 * $stop22) + (3000 * $stop22 * $stop22) + (40 * $stop22 ** 3);
	$kane2=int($cost2/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane2���f</font>�ł��B<br>";

	$mes.="�P�P���`�P�Q��<br>";
	$stop3=int( 0.48 * 0.53 * 0.43 * 0.53 * 1000 ) / 10;
	$ok3=100-$stop3;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok3��</font>�ł��B<br>";
	$ok3=$ok3/100;
	$ok=$ok*($ok3 ** 2);
	$ok33=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok33��</font>�ł��B<br>";
	$stop33=100-$ok33;
	$cost3=(120000 * $ok33) + (240000 * $stop33) + (3600 * $stop33 * $stop33) + (48 * $stop33 ** 3);
	$kane3=int($cost3/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane3���f</font>�ł��B<br>";

	$mes.="�P�R���`�P�U��<br>";
	$stop4=int( 0.42 * 0.47 * 0.37 * 0.47 * 1000 ) / 10;
	$ok4=100-$stop4;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok4��</font>�ł��B<br>";
	$ok4=$ok4/100;
	$ok=$ok*($ok4 ** 4);
	$ok44=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok44��</font>�ł��B<br>";
	$stop44=100-$ok44;
	$cost4=(160000 * $ok44) + (320000 * $stop44) + (4800 * $stop44 * $stop44) + (64 * $stop44 ** 3);
	$kane4=int($cost4/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane4���f</font>�ł��B<br>";

	$mes.="�P�V���`�Q�O��<br>";
	$stop5=int( 0.38 * 0.43 * 0.33 * 0.43 * 1000 ) / 10;
	$ok5=100-$stop5;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok5��</font>�ł��B<br>";
	$ok5=$ok5/100;
	$ok=$ok*($ok5 ** 4);
	$ok55=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok55��</font>�ł��B<br>";
	$stop55=100-$ok55;
	$cost5=(200000 * $ok55) + (400000 * $stop55) + (6000 * $stop55 * $stop55) + (80 * $stop55 ** 3);
	$kane5=int($cost5/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane5���f</font>�ł��B<br>";

	$mes.="�Q�P���`�R�O��<br>";
	$stop6=int( 0.48 * 0.53 * 0.43 * 0.53 * 1000 ) / 10;
	$ok6=100-$stop6;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok6��</font>�ł��B<br>";
	$ok6=$ok6/100;
	$ok=$ok*($ok6 ** 10);
	$ok66=int($ok*10000)/100;
	$mes.="�����܂Ői�߂�m���́A<font size=6 color=\"red\">$ok66��</font>�ł��B<br>";
	$stop66=100-$ok66;
	$cost6=(300000 * $ok66) + (600000 * $stop66) + (9000 * $stop66 * $stop66) + (120 * $stop66 ** 3);
	$kane6=int($cost6/10000);
	$mes.="�����܂Ői�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane6���f</font>�ł��B<br>";

	$mes.="�R�P���`<br>";
	$stop7=int( 0.68 * 0.73 * 0.63 * 0.73 * 1000 ) / 10;
	$ok7=100-$stop7;
	$mes.="�P���i�߂�m���́A<font size=6 color=\"red\">$ok7��</font>�ł��B<br>";
	$ok7=$ok7/100;
	$ok=$ok*($ok7 ** 2);
	$ok77=int($ok*10000)/100;
	$mes.="�P�̕��p�ɂQ�O�i�߂�m���́A<font size=6 color=\"red\">$ok77��</font>�ł��B<br>";
	$stop77=100-$ok77;
	$cost7=(320000 * $ok77) + (640000 * $stop77) + (9600 * $stop77 * $stop77) + (128 * $stop77 ** 3);
	$kane7=int($cost7/10000);
	$mes.="�P�̕��p�ɂQ�O�i�ނ̂ɂ����镽�ϋ��z��<font size=6 color=\"red\">$kane7���f</font>�ł��B<br>";

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yashiki.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}