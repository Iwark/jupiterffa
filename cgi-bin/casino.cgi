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

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="casino.cgi" >
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

&sakaba;

&error;

exit;

#----------#
#  ���  #
#----------#
sub sakaba {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�J�W�m</h1>
<hr size=0>
<FONT SIZE=3>
<B>�J�W�m�̃I�[�i�[</B><BR>
�u����ɂ��́B�h���[�����[���h��������z���Ă����֗����̃X�e�B�[�u���̒�ł��B<br>
�����A�h���[�����[���h�̌��H�@����͂�����Ɣ���Ȃ��Ȃ��c(�E���E)<br>
�����ł́A�R�C���𔃂��āA������Ƃ����Q�[�������邱�Ƃ��ł����B<br>
���ĂΖׂ���B������Ζv�����B���܂��܂����z����A���Ȃ���B�R�C����100��1��G���B<br>
�R�C���͊������邱�Ƃ��ł��邪�A���A�R�C���ƌ����ł���A�C�e���𒲒B��������A����Ă������ق����������B<br>
���Ȃ݂ɁA�������Ă���R�C����1000���𒴂���ƁA�������Ƃ͂ł��Ȃ�����A�q���ŏ������Ȃ��̂��B�v
</FONT>
<hr size=0>
���݂̏������F$chara[19]G<br>
���݂̃R�C���F$chara[148]��
<br>

<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=buycoin>
<input type=submit class=btn value="�R�C���𔃂�">(�P�O�O���P��G)
</form>
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sellcoin>
<input type=submit class=btn value="�R�C���𔄂�">(�P�O�O���P��G)
</form>
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=trade>
<input type=submit class=btn value="�R�C���ƃA�C�e������������">
</form>
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=monster>
<input type=submit class=btn value="���Z��">
</form>
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=runaway>
<input type=submit class=btn value="�����i�E�F�C">
</form>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=tower>
<input type=submit class=btn value="�R�C���^���[">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub buycoin {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[19] < 100000000) {
		&error("����������܂���$back_form"); 
	}elsif($chara[148]>1000){
		&error("����ȏ�R�C���͔����܂���B$back_form");
	}else{
		$chara[19] = $chara[19] - 100000000;
		$chara[148]+=100;
	}
	
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�������</B><BR></font>
<br>
<form action="casino.cgi" >
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
sub sellcoin {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[148] < 100) {
		&error("�R�C��������܂���$back_form"); 
	}else{
		$chara[19] = $chara[19] + 100000000;
		$chara[148]-=100;
	}
	
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�������</B><BR></font>
<br>
<form action="casino.cgi" >
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
sub trade {

	&chara_load;

	&chara_check;

	&header;

	$new_chara = $chara_log;

	print <<"EOM";
<h1>�R�C���ƃA�C�e��������</h1>
<hr size=0>
<FONT SIZE=3>
<B>�J�W�m�̃I�[�i�[</B><BR>
�u�����A�����ɂ���̂��������ł���A�C�e������B<br>
�܂��܂����B�����B�Z�M�̖���������Ƃ����ƒD���Ă������Ȃ��E�E�E�B�v
</FONT>
<hr size=0>
���݂̏������F$chara[19]G<br>
���݂̃R�C���F$chara[148]��
<br>
<table><tr><th></th><th>�A�C�e��</th><th>�K�v�ȃR�C��</th></tr>
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=present>
<tr><th><input type=radio name=item_no value=1></th><th>�ŋ�ԃ`�P�b�g10���Z�b�g</th><th>3000</th></tr>
<tr><th><input type=radio name=item_no value=2></th><th>�����E�`�P�b�g</th><th>5000</th></tr>
<tr><th><input type=radio name=item_no value=3></th><th>(�E)�M�����u���[�@</th><th>10000</th></tr>
<tr><th><input type=radio name=item_no value=4></th><th>�V�F�h�����b�NA</th><th>7500</th></tr>
<tr><th><input type=radio name=item_no value=5></th><th>�V�F�h�����b�NV</th><th>7500</th></tr>
<tr><th><input type=radio name=item_no value=6></th><th>�V�F�h�����b�NP</th><th>15000</th></tr>
<tr><th><input type=radio name=item_no value=7></th><th>(�E)�M�����u���[�A</th><th>30000</th></tr>
<tr><th><input type=radio name=item_no value=8></th><th>�ŋ�ԃ`�P�b�g100���Z�b�g</th><th>30000</th></tr>
<tr><th><input type=radio name=item_no value=9></th><th>�����E�`�P�b�g10���Z�b�g</th><th>50000</th></tr>
<tr><th><input type=radio name=item_no value=10></th><th>(�E)�M�����u���[�B</th><th>100000</th></tr>
<tr><th><input type=radio name=item_no value=11></th><th>�����X�^�[�̍�</th><th>10000</th></tr>
</table>
<input type=submit class=btn value="��������">
</form>
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub present {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'item_no'}==1){
		if($chara[148]<3000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=3000;
			$chara[189]+=10;
		}
	}elsif($in{'item_no'}==2){
		if($chara[148]<5000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=5000;
			$chara[146]+=1;
		}
	}elsif($in{'item_no'}==3){
		if($chara[148]<10000){
			&error("�R�C��������܂���B");
		}else{
			if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
			$chara[148]-=10000;
			$chara[14]=55;
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
			$eg="$chara[4]�l���M�����u���[�@�ɂȂ�܂����B";
			unshift(@chat_mes,"<>���m<>$mon��$mday��$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");
			open(OUT,">$chat_file");
			print OUT @chat_mes;
			close(OUT);
			&unlock($lock_file,'MS');
		}
	}elsif($in{'item_no'}==4){
		if($chara[148]<7500){
			&error("�R�C��������܂���B");
		}else{
			open(IN,"./mayaku/$chara[0].cgi");
			$mayaku_list = <IN>;
			close(IN);
			@mayaku = split(/<>/,$mayaku_list);
			$mayaku[10]+=1;
			$new_mayaku = '';
			$new_mayaku = join('<>',@mayaku);
			$new_mayaku .= '<>';
			open(OUT,">./mayaku/$chara[0].cgi");
			print OUT $new_mayaku;
			close(OUT);
			$chara[148]-=7500;
		}
	}elsif($in{'item_no'}==5){
		if($chara[148]<7500){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=7500;
			open(IN,"./mayaku/$chara[0].cgi");
			$mayaku_list = <IN>;
			close(IN);
			@mayaku = split(/<>/,$mayaku_list);
			$mayaku[11]+=1;
			$new_mayaku = '';
			$new_mayaku = join('<>',@mayaku);
			$new_mayaku .= '<>';
			open(OUT,">./mayaku/$chara[0].cgi");
			print OUT $new_mayaku;
			close(OUT);
		}
	}elsif($in{'item_no'}==6){
		if($chara[148]<15000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=15000;
			open(IN,"./mayaku/$chara[0].cgi");
			$mayaku_list = <IN>;
			close(IN);
			@mayaku = split(/<>/,$mayaku_list);
			$mayaku[12]+=1;
			$new_mayaku = '';
			$new_mayaku = join('<>',@mayaku);
			$new_mayaku .= '<>';
			open(OUT,">./mayaku/$chara[0].cgi");
			print OUT $new_mayaku;
			close(OUT);
		}
	}elsif($in{'item_no'}==7){
		if($chara[148]<30000){
			&error("�R�C��������܂���B");
		}else{
			if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
			$chara[148]-=30000;
			$chara[14]=56;
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
			$eg="$chara[4]�l���M�����u���[�A�ɂȂ�܂����B";
			unshift(@chat_mes,"<>���m<>$mon��$mday��$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");
			open(OUT,">$chat_file");
			print OUT @chat_mes;
			close(OUT);
			&unlock($lock_file,'MS');
		}
	}elsif($in{'item_no'}==8){
		if($chara[148]<30000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=30000;
			$chara[189]+=100;
		}
	}elsif($in{'item_no'}==9){
		if($chara[148]<50000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=50000;
			$chara[146]+=10;
		}
	}elsif($in{'item_no'}==10){
		if($chara[148]<100000){
			&error("�R�C��������܂���B");
		}else{
			if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
			$chara[148]-=100000;
			$chara[14]=57;
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
			$eg="$chara[4]�l���M�����u���[�B�ɂȂ�܂����B";
			unshift(@chat_mes,"<>���m<>$mon��$mday��$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");
			open(OUT,">$chat_file");
			print OUT @chat_mes;
			close(OUT);
			&unlock($lock_file,'MS');
		}
	}elsif($in{'item_no'}==11){
		if($chara[148]<10000){
			&error("�R�C��������܂���B");
		}else{
			$chara[148]-=10000;
			open(IN,"$pet_file");
			@item_array = <IN>;
			close(IN);
			$hit=0;$gxu=0;
			while($hit!=1 and $gxu<10){
				$pmons=int(rand(100)+3401);
				foreach(@item_array){
				($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
					if($phi_no == $pmons) {
						$pmons-=3200;
						if($chara[$pmons]>0){last;}
						else{$hit=1;last;}
					}
				}
				$gxu++;
			}
			if(!$hit){$comment .= "���̓���Ɏ��s�����c(��)<br>";}
			else{
				$comment .= "$phi_name�̍�����肵���I�I<br>";
				$chara[$pmons]+=1;
			}
		}
	}else{
		&error("����������̂�I�����Ă��������B");
	}
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���������B$comment</B><BR></font>
<br>
<form action="casino.cgi" >
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
sub monster {

	&chara_load;

	&chara_check;

	&header;

	open(IN,"./tougi.cgi");
	@monster = <IN>;
	close(IN);
	open(IN,"./tougimons.cgi");
	@monsters = <IN>;
	close(IN);
	$hit=0;
	$jik=0;
	if($hour>=12){$jik=1;}
	$kee="$mday$jik";
	if( ! open IN , "./tougikekka/$kee.cgi"){ $hit=2; }
	foreach(@monster){
		@tmon = split(/<>/);
		if($tmon[0] == $mday and $tmon[10] == $jik and $tmon[11] == $mon){
			$hit+=1;
			$no1=$tmon[1];$no2=$tmon[2];$no3=$tmon[3];$no4=$tmon[4];
			$un1=$tmon[5];$un2=$tmon[6];$un3=$tmon[7];$un4=$tmon[8];
			$syougun=$tmon[9];
			($tname1,$thp1,$tdmg1,$thit1,$twaza1,$tstr1) = split(/<>/,$monsters[$no1]);
			($tname2,$thp2,$tdmg2,$thit2,$twaza2,$tstr2) = split(/<>/,$monsters[$no2]);
			($tname3,$thp3,$tdmg3,$thit3,$twaza3,$tstr3) = split(/<>/,$monsters[$no3]);
			($tname4,$thp4,$tdmg4,$thit4,$twaza4,$tstr4) = split(/<>/,$monsters[$no4]);
			$kee="$mday$jik";
			open(IN,"./tougikekka/kekka$kee.cgi");
			$twin = <IN>;
			close(IN);
			if($twin==1){$tstr1-=1;}if($twin==2){$tstr2-=1;}if($twin==3){$tstr3-=1;}if($twin==4){$tstr4-=1;}
			last;
		}
	}
	if($hit==0){
		$tmax=@monsters;
		$no1=int(rand($tmax));
		$no2=int(rand($tmax));
		$no3=int(rand($tmax));
		$no4=int(rand($tmax));
		$un1=int(rand(1000));
		$un2=int(rand(1000));
		$un3=int(rand(1000));
		$un4=int(rand(1000));
		$syougun=int(rand(56));
		if($mon==3 and $mday==25){
			$no1=21;$no2=22;$no3=23;$no4=24;
			$un1=1000;$un2=1000;$un3=1000;$un4=1000;
			$syougun=0;
		}
		push(@monster,"$mday<>$no1<>$no2<>$no3<>$no4<>$un1<>$un2<>$un3<>$un4<>$syougun<>$jik<>$mon<>\n");
		
		open(OUT,">tougi.cgi");
		print OUT @monster;
		close(OUT);
	}
	if($hit!=1){
		($tname1,$thp1,$tdmg1,$thit1,$twaza1,$tstr1) = split(/<>/,$monsters[$no1]);
		($tname2,$thp2,$tdmg2,$thit2,$twaza2,$tstr2) = split(/<>/,$monsters[$no2]);
		($tname3,$thp3,$tdmg3,$thit3,$twaza3,$tstr3) = split(/<>/,$monsters[$no3]);
		($tname4,$thp4,$tdmg4,$thit4,$twaza4,$tstr4) = split(/<>/,$monsters[$no4]);

		$tmhp1=$thp1+int(rand($un1*10));
		$tmhp2=$thp2+int(rand($un2*10));
		$tmhp3=$thp3+int(rand($un3*10));
		$tmhp4=$thp4+int(rand($un4*10));
		$thp1_flg=$tmhp1;
		$thp2_flg=$tmhp2;
		$thp3_flg=$tmhp3;
		$thp4_flg=$tmhp4;
		@kekka=();
		$j=0;
		$i=1;
		while($i<=$turn) {
			&shokika;
			&twaza;
			&tbattle_sts;
			&hp_sum;
			&winlose;
			$i++;
			$j++;
		}
		&sentoukeka;
		$kee="$mday$jik";

		open(OUT,">tougikekka/$kee.cgi");
		print OUT @kekka;
		close(OUT);
		open(OUT,">tougikekka/kekka$kee.cgi");
		print OUT $win;
		close(OUT);
		if($win!=5){
			$tstr=${'tstr'.$win} + 1;
			${'thp'.$win}+=500;
			${'tdmg'.$win}+=100;
			$monsters[${'no'.$win}]="${'tname'.$win}<>${'thp'.$win}<>${'tdmg'.$win}<>${'thit'.$win}<>${'twaza'.$win}<>$tstr<>\n";
			open(OUT,">tougimons.cgi");
			print OUT @monsters;
			close(OUT);
		}
	}
	for($ti=1;$ti<5;$ti++){
		if(${'thp'.$ti}>=15000){${'thpf'.$ti}="S";}
		elsif(${'thp'.$ti}>=12000){${'thpf'.$ti}="A";}
		elsif(${'thp'.$ti}>=9000){${'thpf'.$ti}="B";}
		elsif(${'thp'.$ti}>=6000){${'thpf'.$ti}="C";}
		else{${'thpf'.$ti}="D";}
		if(${'tdmg'.$ti}>2000){${'tdmgf'.$ti}="S";}
		elsif(${'tdmg'.$ti}>1300){${'tdmgf'.$ti}="A";}
		elsif(${'tdmg'.$ti}>1000){${'tdmgf'.$ti}="B";}
		elsif(${'tdmg'.$ti}>800){${'tdmgf'.$ti}="C";}
		else{${'tdmgf'.$ti}="D";}
		if(${'thit'.$ti}>60){${'thitf'.$ti}="S";}
		elsif(${'thit'.$ti}>50){${'thitf'.$ti}="A";}
		elsif(${'thit'.$ti}>35){${'thitf'.$ti}="B";}
		elsif(${'thit'.$ti}>20){${'thitf'.$ti}="C";}
		else{${'thitf'.$ti}="D";}
		open(IN,"./tougicomment.cgi");
		@tougicomment = <IN>;
		close(IN);
		$comnumb=@tougicomment-4;
		if(${'tname'.$ti} eq "��������"){@com = split(/<>/,$tougicomment[$comnumb]);}
		elsif(${'tname'.$ti} eq "�Ђ܂��"){@com = split(/<>/,$tougicomment[$comnumb+1]);}
		elsif(${'tname'.$ti} eq "�ɂ�"){@com = split(/<>/,$tougicomment[$comnumb+2]);}
		elsif(${'tname'.$ti} eq "����"){@com = split(/<>/,$tougicomment[$comnumb+3]);}
		else{@com = split(/<>/,$tougicomment[int(rand($comnumb))]);}
		if(${'un'.$ti}>800){${'tyousi'.$ti}=$com[0];}
		elsif(${'un'.$ti}>500){${'tyousi'.$ti}=$com[1];}
		elsif(${'un'.$ti}>200){${'tyousi'.$ti}=$com[2];}
		else{${'tyousi'.$ti}=$com[3];}
		$unf1=int($un1/10);
		$unf2=int($un2/10);
		$unf3=int($un3/10);
		$unf4=int($un4/10);
	}

	$new_chara = $chara_log;

	open(IN,"./tougigold.cgi");
	@tougigold = <IN>;
	close(IN);
	$tkazu=0;
	$tkane=0;
	foreach(@tougigold){
		@tgold = split(/<>/);
		if($tgold[0] eq $chara[0] and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){$kakekin=$tgold[4];$kakeno=$tgold[5];}
		if($tgold[1] == $year and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){
			${'tkazu'.$tgold[5]}++;
			${'tkane'.$tgold[5]}+=$tgold[4];
		}
	}
	$tkane=$tkane1+$tkane2+$tkane3+$tkane4;
	#$tstr1=0;$tstr2=0;$tstr3=0;$tstr4=0;
	$tstr=$tstr1+$tstr2+$tstr3+$tstr4;
	$tstrup=int($tkane/$tstr);
	$tstr*=$tstrup;$tstr1*=$tstrup;$tstr2*=$tstrup;$tstr3*=$tstrup;$tstr4*=$tstrup;
	if($tkazu1==0){$tkake1=10;}else{$tkake1=int(($tkane+$tstr)/($tkane1+$tstr1)*10)/10;}
	if($tkazu2==0){$tkake2=10;}else{$tkake2=int(($tkane+$tstr)/($tkane2+$tstr2)*10)/10;}
	if($tkazu3==0){$tkake3=10;}else{$tkake3=int(($tkane+$tstr)/($tkane3+$tstr3)*10)/10;}
	if($tkazu4==0){$tkake4=10;}else{$tkake4=int(($tkane+$tstr)/($tkane4+$tstr4)*10)/10;}
	$tkake1+=0.3;$tkake2+=0.3;$tkake3+=0.3;$tkake4+=0.3;
	if($tkake1>10){$tkake1=10;}if($tkake2>10){$tkake2=10;}if($tkake3>10){$tkake3=10;}if($tkake4>10){$tkake4=10;}

	print <<"EOM";
<h1>���Z��</h1>
<hr size=0>
<FONT SIZE=3>
<B>���Z��̂�������</B><BR>
�u���႟�A���Z��̐��������邺�H<br>
�悵�B<br>
�����ȁB<br>
�P��<font color="red" size=4>�Q</font>��A�����X�^�[���S�C�A�킢�����I(0���`12���A12���`24��)<br>
�������X�^�[��\\�z\���āA�q����B���ꂾ�����I<br>
���ʂ�0���܂���12���ɏo��I�q���ɏ������ꍇ�́A�����ƃR�C�����󂯎��ɗ���񂾂��B<br>
�R�C���͂P�����Œ�P�O���ȏ�q���Ă��炤���B(�R�����܂œq�����܂��B)<br>
���Ȃ݂Ɉ��������̏ꍇ�̓R�C���͑S�Ėv���ƂȂ邺�B<br>
<font color="red" size=4><b>�{���͓q�����l�̐���R�C���ŕϓ�</b></font>���A���݂̔{���͎Q�l���x�ɂ����Ȃ�Ȃ����璍�ӂ��B�v
</FONT><br>
EOM
if($chara[0] eq "jupiter" and $chara[149]){
	print <<"EOM";
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=kekka>
<input type=submit class=btn value="����̌��ʂ�����">
</form>
EOM
}
$kee="$mday$jik";
if($chara[149] and $chara[149] ne "$kee"){
	print <<"EOM";
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=kekka>
<input type=submit class=btn value="�O��̌��ʂ�����">
</form>
EOM
}
	print <<"EOM";
<hr size=0>
���݂̃R�C���F$chara[148]��<br>
���Ȃ��͍���A$kakeno�Ԗڂ̃����X�^�[��$kakekin�R�C���q���Ă��܂��B<br>
<table><tr><th></th><th>���O</th><th>HP</th><th>�U����</th><th>������</th><th>���q</th><th>�R�����g</th><th>���݂̔{��</th></tr>
<form action="casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tbattle>
<tr><th><input type=radio name=item_no value=1></th>
<th>$tname1</th><th>$thpf1</th><th>$tdmgf1</th><th>$thitf1</th><th>$unf1</th><th>$tyousi1</th><th>$tkake1</th></tr>
<tr><th><input type=radio name=item_no value=2></th>
<th>$tname2</th><th>$thpf2</th><th>$tdmgf2</th><th>$thitf2</th><th>$unf2</th><th>$tyousi2</th><th>$tkake2</th></tr>
<tr><th><input type=radio name=item_no value=3></th>
<th>$tname3</th><th>$thpf3</th><th>$tdmgf3</th><th>$thitf3</th><th>$unf3</th><th>$tyousi3</th><th>$tkake3</th></tr>
<tr><th><input type=radio name=item_no value=4></th>
<th>$tname4</th><th>$thpf4</th><th>$tdmgf4</th><th>$thitf4</th><th>$unf4</th><th>$tyousi4</th><th>$tkake4</th></tr>
</table><br>
�R�C��<input type="text" name="coin" value="" size=10>��
<input type=submit class=btn value="�q����">
</form>
<hr size=0>
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub runaway {

	&chara_load;

	&chara_check;

	&header;

	open(IN,"./runaway.cgi");
	@runaway = <IN>;
	close(IN);
	$runmax=@runaway;
	$runmax-=1;
	$runsum=0;$hit=0;
	foreach(@runaway){
		@run = split(/<>/);
		if($run[0]==$year and $run[1]==$mon and $run[2]==$mday and $run[3]==$hour){
			$hit=1;
			if($run[4] != 1){$runsum+=$run[4];}
			if($run[5] != 1){$runsum+=$run[5];}
			if($run[6] != 1){$runsum+=$run[6];}
			if($run[7] != 1){$runsum+=$run[7];}
			last;
		}
	}
	if($hit!=1){
		@mrun = split(/<>/,$runaway[$runmax]);
		$runfile = "$mrun[2]$mrun[3]";
		open(IN,"./runkekka/$runfile.cgi");
		$run_kekka = <IN>;
		close(IN);
		@runkekka = split(/<>/,$run_kekka);
		$runsage=0;
		if($runkekka[0]==1){$mrun[4]=1;$runsage+=5;}else{$mrun[4]+=0.1;$runsum+=$mrun[4];}
		if($runkekka[1]==1){$mrun[5]=1;$runsage+=5;}else{$mrun[5]+=0.1;$runsum+=$mrun[5];}
		if($runkekka[2]==1){$mrun[6]=1;$runsage+=5;}else{$mrun[6]+=0.1;$runsum+=$mrun[6];}
		if($runkekka[3]==1){$mrun[7]=1;$runsage+=5;}else{$mrun[7]+=0.1;$runsum+=$mrun[7];}
		push(@runaway,"$year<>$mon<>$mday<>$hour<>$mrun[4]<>$mrun[5]<>$mrun[6]<>$mrun[7]<>\n");
		open(OUT,">runaway.cgi");
		print OUT @runaway;
		close(OUT);
		$k1=0;$k2=0;$k3=0;$k4=0;
		@runper=();
		if($runsum==0){
			$runper[4]=0;$runper[5]=0;$runper[6]=0;$runper[7]=0;
		}else{
			$i=0; $runsage=0;
			foreach(@mrun){
			if($mrun[$i]==1 and $i>3){$runper[$i]=0;$runsage+=5;}elsif($i>3){$runper[$i]=int($mrun[$i]/$runsum*100);}
				$i++;
			}
		}
		if($runper[4]!=0){$runper[4]-=$runsage;}
		if($runper[5]!=0){$runper[5]-=$runsage;}
		if($runper[6]!=0){$runper[6]-=$runsage;}
		if($runper[7]!=0){$runper[7]-=$runsage;}

		if($runper[4]>int(rand(100))){$k1=1;}
		if($runper[5]>int(rand(100))){$k2=1;}
		if($runper[6]>int(rand(100))){$k3=1;}
		if($runper[7]>int(rand(100))){$k4=1;}
		$rkekka="$k1<>$k2<>$k3<>$k4<>\n";
		$kee="$mday$hour";
		open(OUT,">runkekka/$kee.cgi");
		print OUT $rkekka;
		close(OUT);
		open(IN,"./runaway.cgi");
		@runaway = <IN>;
		close(IN);
		$runsum=0;
		foreach(@runaway){
			@run = split(/<>/);
			if($run[0]==$year and $run[1]==$mon and $run[2]==$mday and $run[3]==$hour){
				if($run[4] != 1){$runsum+=$run[4];}
				if($run[5] != 1){$runsum+=$run[5];}
				if($run[6] != 1){$runsum+=$run[6];}
				if($run[7] != 1){$runsum+=$run[7];}
				last;
			}
		}
	}
	@runper=();
	if($runsum==0){
		$runper[4]=0;$runper[5]=0;$runper[6]=0;$runper[7]=0;
	}else{
		$i=0; $runsage=0;
		foreach(@run){
			if($run[$i]==1 and $i>3){$runper[$i]=0;$runsage+=5;}elsif($i>3){$runper[$i]=int($run[$i]/$runsum*100);}
			$i++;
		}
	}
	if($runper[4]!=0){$runper[4]-=$runsage;}
	if($runper[5]!=0){$runper[5]-=$runsage;}
	if($runper[6]!=0){$runper[6]-=$runsage;}
	if($runper[7]!=0){$runper[7]-=$runsage;}

	$new_chara = $chara_log;

	open(IN,"./rungold.cgi");
	@run_gold = <IN>;
	close(IN);
	$hit=0;
	foreach(@run_gold){
		@rungold = split(/<>/);
		if($rungold[0] eq $chara[0]){
			$hit=1;
			if($rungold[1] == $year and $rungold[2] == $mon and $rungold[3] == $mday and $rungold[4] == $hour){
				$hit=2;
				$kakeno=$rungold[5];
				$kakekin=$rungold[6];
				last;
			}
		}
	}
	print <<"EOM";
<h1>�����i�E�F�C</h1>
<hr size=0>
<FONT SIZE=3>
<B>�����i�E�F�C�̎�t</B><BR>
�u��ف[���I$chara[4]����Ȃ����A���C�����H�@����"�����i�E�F�C"�̐������n�߂��`�H<br>
�悵�B<br>
�����ȁB<br>
�P���ԂɂP�x�A�S�����P�A�������Ԃ��󂵂��Ⴄ���Ă����ݒ肳�B<br>
�킩��̂́A�������Ƃ̋S������m���B<br>
���Ȃ݂ɁA�S������m���̍��������قǔ{����������B<br>
�R�C���͂P�����Œ�P�O���ȏ�q���Ă��炤��B(�P�����܂œq�����܂�)<br>
�N�̓q���������ɋS�����Ă��܂�����N�̓q�����R�C���͖v���B���Ȃ���ΌN�̏����Ƃ����킯���B<br>
�O��P�����󂯂������ɂ͋S�����Ȃ�����A�q���邱�Ƃ͂ł��Ȃ���B�v
</FONT><br>
EOM
if($hit==1){
	print <<"EOM";
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=runkekka>
<input type=submit class=btn value="�O��̌��ʂ�����">
</form>
EOM
}
	print <<"EOM";
<hr size=0>
���݂̃R�C���F$chara[148]��<br>
���Ȃ��͍���A$kakeno�Ԗڂ̌�����$kakekin�R�C���q���Ă��܂��B<br>
<table><tr><th></th><th>���O</th><th>�S������m��</th><th>�{��</th></tr>
<form action="casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=runkake>
EOM
if($run[4]!=1){print "<tr><th><input type=radio name=item_no value=1></th><th>�h��</th><th>$runper[4]��</th><th>$run[4]</th></tr>";}
else{print "<tr><th>�~</th><th>�h��</th><th>$runper[4]��</th><th>$run[4]</th></tr>";}
if($run[5]!=1){print "<tr><th><input type=radio name=item_no value=2></th><th>���X�X</th><th>$runper[5]��</th><th>$run[5]</th></tr>";}
else{print "<tr><th>�~</th><th>���X�X</th><th>$runper[5]��</th><th>$run[5]</th></tr>";}
if($run[6]!=1){print "<tr><th><input type=radio name=item_no value=3></th><th>��s</th><th>$runper[6]��</th><th>$run[6]</th></tr>";}
else{print "<tr><th>�~</th><th>��s</th><th>$runper[6]��</th><th>$run[6]</th></tr>";}
if($run[7]!=1){print "<tr><th><input type=radio name=item_no value=4></th><th>�q��</th><th>$runper[7]��</th><th>$run[7]</th></tr>";}
else{print "<tr><th>�~</th><th>�q��</th><th>$runper[7]��</th><th>$run[7]</th></tr>";}
	print <<"EOM";
</table><br>
�R�C��<input type="text" name="coin" value="" size=10>��
<input type=submit class=btn value="�q����">
</form>
<hr size=0>
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub tower {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>�R�C���^���[</h1>
<hr size=0>
<FONT SIZE=3>
<B>�R�C���^���[��t</B><BR>
�u$chara[4]����ł��ˁB�R�C���^���[�ɂ��Ă��ē������Ă��������܂��B<br>
�R�C���^���[�́A���Ȃ����g�����킷�邱�Ƃ̂ł���_���W�����ł��B<br>
����̎������݂͈�؋֎~�A�A�r���e�B���g���܂���B<br>
�悭�l�����X�e�[�^�X�Œ��킵�Ă��������B<br>
<br>
�R�C���͍Œ�10���A�ő�100���A�����ɓq���邱�ƂɂȂ�܂��B<br>
�_���W�����̊e�K���N���A����x�ɕ�V���󂯎��or�i�ނ��Ƃ̑I�����ł��܂��B<br>
�i�߂ΐi�ނقǃR�C���������邱�ƂɂȂ�܂����A������Γq������(����������)�A�Ȃ��Ȃ��Ă��܂��܂��B<br>
�P���ɒ��킷��񐔂ɓ��ɐ����͂���܂��񂪁A�P�K���ƂɂR���̐������Ԃ�������܂��B<br>
�҂����Ԃ̊Ԃ́A�������Ă��Ă����R�ł��B<br>
�v

</FONT><br>
EOM

if($chara[311]>0 and (time()-$chara[312])>=180){
	print <<"EOM";
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=runkekka>
<input type=submit class=btn value="���̊K��">
</form>
EOM
}elsif($chara[311]>0){
	$cointime = time()-$chara[312];
	print "����̒���܂łɂ͌�$cointime�b������܂��B";
}else{
	print <<"EOM";
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=runkekka>
<input type=submit class=btn value="���킷��">
</form>
EOM
}
	print <<"EOM";
<hr size=0>
<form action="casino.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�߂�">
</form>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub tbattle {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$jik=0;
	if($hour>=12){$jik=1;}

	if ($in{'coin'} =~ m/[^0-9]/){
		&error("�q����R�C���ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
	}else{
		$coin=$in{'coin'};
	}
	if($coin<10){
		&error("�R�C����10���ȏ�q���Ă��������B$back_form"); 
	}elsif($coin>30000){
		&error("�R�C���͂R�����܂ł����q�����܂���B$back_form"); 
	}elsif($chara[148] < $coin) {
		&error("�R�C��������܂���B$back_form"); 
	}elsif($chara[149]){
		&error("���ɓq���܂����B���ʂ����Ă��Ȃ��킢������΁A��Ɍ��ʂ����Ă��������B$back_form"); 
	}else{
		$chara[149]="$mday$jik";
		$chara[148]-=$coin;
		open(IN,"./tougigold.cgi");
		@tougigold = <IN>;
		close(IN);
		$hit=0;$i=0;
		foreach(@tougigold){
			@tgold = split(/<>/);
			if($tgold[0] eq $chara[0]){
				$hit=1;
				$tougigold[$i]="$chara[0]<>$year<>$mon<>$mday<>$coin<>$in{'item_no'}<>$jik<>\n";
				last;
			}
			$i++;
		}
		if($hit!=1){push(@tougigold,"$chara[0]<>$year<>$mon<>$mday<>$coin<>$in{'item_no'}<>$jik<>\n");}
		open(OUT,">tougigold.cgi");
		print OUT @tougigold;
		close(OUT);
	}
	
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�q���܂����B</B><BR></font>
<br>
<form action="casino.cgi" >
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
sub runkake {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($in{'coin'} =~ m/[^0-9]/){
		&error("�q����R�C���ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
	}elsif(!$in{'item_no'}){
		&error("�q���錚����I�����Ă��������B$back_form"); 
	}else{
		$coin=$in{'coin'};
	}

	open(IN,"./rungold.cgi");
	@run_gold = <IN>;
	close(IN);
	$hit=0;
	foreach(@run_gold){
		@rungold = split(/<>/);
		if($rungold[0] eq $chara[0]){
			$hit=1;
			last;
		}
	}

	if($coin<10){
		&error("�R�C����10���ȏ�q���Ă��������B$back_form"); 
	}elsif($coin>10000){
		&error("�R�C���͂P�����܂ł����q�����܂���B$back_form"); 
	}elsif($chara[148] < $coin) {
		&error("�R�C��������܂���B$back_form"); 
	}elsif($hit){
		&error("���ɓq���܂����B���ʂ����Ă��Ȃ��킢������΁A��Ɍ��ʂ����Ă��������B$back_form"); 
	}else{
		$chara[148]-=$coin;
		push(@run_gold,"$chara[0]<>$year<>$mon<>$mday<>$hour<>$in{'item_no'}<>$coin<>\n");
		open(OUT,">rungold.cgi");
		print OUT @run_gold;
		close(OUT);
	}
	
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�q���܂����B</B><BR></font>
<br>
<form action="casino.cgi" >
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
sub kekka {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;
	
	$mes="";

	open(IN,"./tougigold.cgi");
	@tougigold = <IN>;
	close(IN);
	$tkazu=0;
	$tkane=0;
	foreach(@tougigold){
		@tgold = split(/<>/);
		$kee="$tgold[3]$tgold[6]";
		if($tgold[0] eq $chara[0]){$kakekin=$tgold[4];$kakeno=$tgold[5];}
		if($tgold[1] == $year and $tgold[2] == $mon and $kee == $chara[149]){
			${'tkazu'.$tgold[5]}++;
			${'tkane'.$tgold[5]}+=$tgold[4];
		}
	}
	if(!$tkane1){$tkane1=1;}if(!$tkane2){$tkane2=1;}if(!$tkane3){$tkane3=1;}if(!$tkane4){$tkane4=1;}

	open(IN,"./tougi.cgi");
	@monster = <IN>;
	close(IN);
	open(IN,"./tougimons.cgi");
	@monsters = <IN>;
	close(IN);
	foreach(@monster){
		@tmon = split(/<>/);
		if($tmon[0] == $tgold[3] and $tmon[10] == $tgold[6] and $tmon[11] == $tgold[1]){
			$no1=$tmon[1];$no2=$tmon[2];$no3=$tmon[3];$no4=$tmon[4];
			($tname1,$thp1,$tdmg1,$thit1,$twaza1,$tstr1) = split(/<>/,$monsters[$no1]);
			($tname2,$thp2,$tdmg2,$thit2,$twaza2,$tstr2) = split(/<>/,$monsters[$no2]);
			($tname3,$thp3,$tdmg3,$thit3,$twaza3,$tstr3) = split(/<>/,$monsters[$no3]);
			($tname4,$thp4,$tdmg4,$thit4,$twaza4,$tstr4) = split(/<>/,$monsters[$no4]);
			last;
		}
	}

	$tkane=$tkane1+$tkane2+$tkane3+$tkane4;
	$tstr=$tstr1+$tstr2+$tstr3+$tstr4;
	if(!$tstr){$tstr=1;}
	$tstrup=int($tkane/$tstr);
	$tstr*=$tstrup;$tstr1*=$tstrup;$tstr2*=$tstrup;$tstr3*=$tstrup;$tstr4*=$tstrup;
	if($kakeno==1){$tkake=int(($tkane+$tstr)/($tkane1+$tstr1)*10)/10;}
	if($kakeno==2){$tkake=int(($tkane+$tstr)/($tkane2+$tstr2)*10)/10;}
	if($kakeno==3){$tkake=int(($tkane+$tstr)/($tkane3+$tstr3)*10)/10;}
	if($kakeno==4){$tkake=int(($tkane+$tstr)/($tkane4+$tstr4)*10)/10;}
	$tkake+=0.3;
	if($tkake>10){$tkake=10;}
	$getgold=int($kakekin * $tkake);

	$mes.="���Ȃ���$kakeno�Ԗڂ̃����X�^�[��$kakekin�R�C���q���܂����B����̔{����$tkake�{�ł��B�������Ă����$getgold�R�C������ł��܂��B<br>";

	open(IN,"./tougikekka/$chara[149].cgi");
	@kekka = <IN>;
	close(IN);
	open(IN,"./tougikekka/kekka$chara[149].cgi");
	$kekkano = <IN>;
	close(IN);

	if($kekkano == $kakeno){
		$syouri="���Ȃ��̏����ł��I�R�C��$getgold���Q�b�g�I�I";
		$chara[148]+=$getgold;
	}elsif($kekkano == 5){
		$getgold=int($kakekin/4);
		$syouri="���������������̂ŃR�C����$getgold���Ҍ�����܂����B";
		$chara[148]+=$getgold;
	}else{
		$syouri="�c�O�Ȃ��獡��͂��Ȃ��̔s�k�ł��E�E�E�B";
	}

	$chara[149]=0;
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR></font>
<br><font size=4>
EOM
	$i=0;
	foreach(@kekka) {
		print "$kekka[$i]";
		$i++;
	}
	print <<"EOM";
<br></font>
<FONT SIZE=3>
<B>$syouri</B><BR></font><br>
<form action="casino.cgi" >
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
sub runkekka {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;
	
	$mes="";

	open(IN,"./runaway.cgi");
	@runaway = <IN>;
	close(IN);
	$runsum=0;

	open(IN,"./rungold.cgi");
	@rungold = <IN>;
	close(IN);
	$g=0;
	foreach(@rungold){
		@rgold = split(/<>/);
		if($rgold[0] eq $chara[0]){$kakekin=$rgold[6];$kakeno=$rgold[5];last;}
		$g++;
	}

	foreach(@runaway){
		@run = split(/<>/);
		if($run[0]==$rgold[1] and $run[1]==$rgold[2] and $run[2]==$rgold[3] and $run[3]==$rgold[4]){
			if($run[4] != 1){$runsum+=$run[4];}
			if($run[5] != 1){$runsum+=$run[5];}
			if($run[6] != 1){$runsum+=$run[6];}
			if($run[7] != 1){$runsum+=$run[7];}
			last;
		}
	}
	$kakerno=$kakeno+3;
	$rkake=$run[$kakerno];
	$getgold=int($kakekin * $rkake);

	$mes.="���Ȃ���$kakeno�Ԗڂ̌��������Ȃ�����$kakekin�R�C���q���܂����B����̔{����$rkake�{�ł��B�������Ă����$getgold�R�C������ł��܂��B<br>";

	$kee="$run[2]$run[3]";

	open(IN,"./runkekka/$kee.cgi");
	$rkekka = <IN>;
	close(IN);
	@rkekka = split(/<>/,$rkekka);
	$kakeno-=1;

	if($rkekka[$kakeno] == 1){
		$mes.="�S�P���B<br>";
		$mes.="�c�O�Ȃ��獡��͂��Ȃ��̔s�k�ł��E�E�E�B";
	}else{
		$mes.="�S�́A���Ȃ��̌������P�����܂���ł����B<br>";
		$mes.="<font color=\"red\" size=6>���Ȃ��̏����ł��I�R�C��$getgold���Q�b�g�I�I</font>";
		$chara[148]+=$getgold;
	}

	splice(@rungold,$g,1);

	open(OUT,">rungold.cgi");
	print OUT @rungold;
	close(OUT);
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR></font>
<br>
<br><br>
<form action="casino.cgi" >
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

sub shokika {
	$com1 = "";
	$com2 = "";
	$com3 = "";
	$com4 = "";
	$dmg1 = $tdmg1 + int(rand($un1));
	$dmg2 = $tdmg2 + int(rand($un2));
	$dmg3 = $tdmg3 + int(rand($un3));
	$dmg4 = $tdmg4 + int(rand($un4));
	$dmg5 = 0;
	$hit1 = $thit1+int(rand($un1/15));
	$hit2 = $thit2+int(rand($un2/15));
	$hit3 = $thit3+int(rand($un3/15));
	$hit4 = $thit4+int(rand($un4/15));
	if($hit1 < int(rand(80))){$dmg1=0;$com1="�������O�ꂽ�I";}
	elsif($thp1_flg < 2000 and int(rand(3))==0){$dmg1=$dmg1*2;$com1="<font color=\"red\" size=5>�I�[�o�[�h���C�u�I</font>";}
	if($hit2 < int(rand(80))){$dmg2=0;$com2="�������O�ꂽ�I";}
	elsif($thp2_flg < 2000 and int(rand(3))==0){$dmg2=$dmg2*2;$com2="<font color=\"red\" size=5>�I�[�o�[�h���C�u�I</font>";}
	if($hit3 < int(rand(80))){$dmg3=0;$com3="�������O�ꂽ�I";}
	elsif($thp3_flg < 2000 and int(rand(3))==0){$dmg3=$dmg3*2;$com3="<font color=\"red\" size=5>�I�[�o�[�h���C�u�I</font>";}
	if($hit4 < int(rand(80))){$dmg4=0;$com4="�������O�ꂽ�I";}
	elsif($thp4_flg < 2000 and int(rand(3))==0){$dmg4=$dmg4*2;$com4="<font color=\"red\" size=5>�I�[�o�[�h���C�u�I</font>";}
	$taisyo1=0;
	$taisyo2=0;
	$taisyo3=0;
	$taisyo4=0;
	$taisyo5=0;
	$tsyougun=0;
	if($syougun > int(rand(100))){
		$tsyougun=int(rand(4)+1);
		if($tsyougun==1){
			$taisyo5=int(rand(4)+1);
			if($taisyo5 == 1 and $thp1_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 2 and $thp2_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 3 and $thp3_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 4 and $thp4_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			else{
				$dmg5 = int(rand(8000));
				if($taisyo5 == 1){$com5="���R�̓ˌ��I$tname1��<font class= \"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==2){$com5="���R�̓ˌ��I$tname2��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==3){$com5="���R�̓ˌ��I$tname3��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==4){$com5="���R�̓ˌ��I$tname4��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
			}
		}elsif($tsyougun==2){
			$taisyo5=int(rand(4)+1);
			if($taisyo5 == 1 and $thp1_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 2 and $thp2_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 3 and $thp3_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 4 and $thp4_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			else{
				$dmg5 = int(rand(18000));
				if($taisyo5 == 1){$com5="���R�̖ҍU�I$tname1��<font class= \"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==2){$com5="���R�̖ҍU�I$tname2��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==3){$com5="���R�̖ҍU�I$tname3��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
				elsif($taisyo5==4){$com5="���R�̖ҍU�I$tname4��<font class=\"yellow\">$dmg5</font>�̃_���[�W�I�I";}
			}
		}elsif($tsyougun==3){
			$taisyo5=int(rand(8)+1);
			if($taisyo5 > 4){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 1 and $thp1_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 2 and $thp2_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 3 and $thp3_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 4 and $thp4_flg < 1){$com5="���R�͗l�q�����Ă���B";}
			else{
				if($taisyo5 == 1){
					$thp1_flg=$tmhp1;
					$com5="���R�̉񕜁I$tname1��<font class= \"yellow\">��</font>�����I";
				}elsif($taisyo5==2){
					$thp2_flg=$tmhp2;
					$com5="���R�̉񕜁I$tname2��<font class=\"yellow\">��</font>�����I";
				}elsif($taisyo5==3){
					$thp3_flg=$tmhp3;
					$com5="���R�̉񕜁I$tname3��<font class=\"yellow\">��</font>�����I";
				}elsif($taisyo5==4){
					$thp4_flg=$tmhp4;
					$com5="���R�̉񕜁I$tname4��<font class=\"yellow\">��</font>�����I";
				}
			}
		}else{
			$taisyo5=int(rand(8)+1);
			if($taisyo5 > 4){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 1 and $thp1_flg > 0){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 2 and $thp2_flg > 0){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 3 and $thp3_flg > 0){$com5="���R�͗l�q�����Ă���B";}
			elsif($taisyo5 == 4 and $thp4_flg > 0){$com5="���R�͗l�q�����Ă���B";}
			else{
				if($taisyo5 == 1){
					$thp1_flg=int($tmhp1/2);
					$com5="���R�̑h���I$tname1��<font class= \"yellow\">�h��</font>�����I";
				}elsif($taisyo5==2){
					$thp2_flg=int($tmhp2/2);
					$com5="���R�̑h���I$tname2��<font class=\"yellow\">�h��</font>�����I";
				}elsif($taisyo5==3){
					$thp3_flg=int($tmhp3/2);
					$com5="���R�̑h���I$tname3��<font class=\"yellow\">�h��</font>�����I";
				}elsif($taisyo5==4){
					$thp4_flg=int($tmhp4/2);
					$com5="���R�̑h���I$tname4��<font class=\"yellow\">�h��</font>�����I";
				}
			}
		}
	}
	if($thp3_flg<1 and $thp4_flg<1){$taisyo1=2;}
	elsif($thp2_flg<1 and $thp4_flg<1){$taisyo1=3;}
	elsif($thp2_flg<1 and $thp3_flg<1){$taisyo1=4;}
	elsif($thp2_flg<1){$taisyo1=int(rand(2)+3);}
	elsif($thp3_flg<1){$taisyo1=int(rand(2)+1)*2;}
	elsif($thp4_flg<1){$taisyo1=int(rand(2)+2);}
	else{$taisyo1=int(rand(3)+2);}
	if($thp3_flg<1 and $thp4_flg<1){$taisyo2=1;}
	elsif($thp1_flg<1 and $thp4_flg<1){$taisyo2=3;}
	elsif($thp1_flg<1 and $thp3_flg<1){$taisyo2=4;}
	elsif($thp1_flg<1){$taisyo2=int(rand(2)+3);}
	elsif($thp3_flg<1){$taisyo2=int(rand(2))*3+1;}
	elsif($thp4_flg<1){$taisyo2=int(rand(2))*2+1;}
	else{$s=int(rand(3));if($s==0){$taisyo2=1;}elsif($s==1){$taisyo2=3;}elsif($s==2){$taisyo2=4;}}
	if($thp2_flg<1 and $thp4_flg<1){$taisyo3=1;}
	elsif($thp1_flg<1 and $thp4_flg<1){$taisyo3=2;}
	elsif($thp1_flg<1 and $thp2_flg<1){$taisyo3=4;}
	elsif($thp1_flg<1){$taisyo3=int(rand(2)+1)*2;}
	elsif($thp2_flg<1){$taisyo3=int(rand(2))*3+1;}
	elsif($thp4_flg<1){$taisyo3=int(rand(2))+1;}
	else{$s=int(rand(3));if($s==0){$taisyo3=1;}elsif($s==1){$taisyo3=2;}elsif($s==2){$taisyo3=4;}}
	if($thp2_flg<1 and $thp3_flg<1){$taisyo4=1;}
	elsif($thp1_flg<1 and $thp3_flg<1){$taisyo4=2;}
	elsif($thp1_flg<1 and $thp2_flg<1){$taisyo4=3;}
	elsif($thp1_flg<1){$taisyo4=int(rand(2)+2);}
	elsif($thp2_flg<1){$taisyo4=int(rand(2))*2+1;}
	elsif($thp3_flg<1){$taisyo4=int(rand(2)+1);}
	else{$taisyo4=int(rand(3)+1);}
}
sub twaza{
	for($wi=1;$wi<5;$wi++){
		if(${'thp'.$wi.'_flg'}>0){
			#����
			if(${'twaza'.$wi} == 1 and int(rand(100))<30){
				${'dmg'.${'taisyo'.$wi}} = int(${'dmg'.${'taisyo'.$wi}}/2);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���ށI</font>${'tname'.${'taisyo'.$wi}}�̕���𓐂�Ń_���[�W�𔼌��������I";
			}
			#�x��
			if(${'twaza'.$wi} == 2 and int(rand(100))<20){
				$yasumu = int(rand(${'dmg'.$wi}));
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'dmg'.$wi} = 0;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�x�ށI</font>HP��$yasumu�񕜂����I";
			}
			#�j��
			if(${'twaza'.$wi} == 3 and int(rand(100))<30){
				$yasumu = int(rand(${'dmg'.$wi}/3));
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�j���I</font>HP��$yasumu�񕜂����I";
			}
			#�ːi
			if(${'twaza'.$wi} == 4 and int(rand(100))<40){
				${'dmg'.$wi} = ${'dmg'.$wi}*2;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�ːi�I</font>�ǂ��I";
			}
			#����
			if(${'twaza'.$wi} == 5 and int(rand(100))<10){
				if(${'dmg'.$wi} == 0){ ${'dmg'.$wi} = int(rand(10000));}
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z����I</font>����ōU���͊O��Ȃ��I";
			}
			#�K����
			if(${'twaza'.$wi} == 6 and int(rand(100))<10){
				${'dmg'.$wi} = ${'dmg'.$wi}*3;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�K�����I</font>�ɂ��낤�I";
			}
			#����
			if(${'twaza'.$wi} == 7 and int(rand(100))<20){
				${'dmg'.$wi} = 500 * int(rand(10)+1);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���ԁI</font>�A���Ԃ��܂ŁI";
			}
			#�A���U��
			if(${'twaza'.$wi} == 8 and int(rand(100))<40){
				${'dmg'.$wi} = ${'dmg'.$wi}*2;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�A���U���I</font>�����I";
			}
			#���p���`
			if(${'twaza'.$wi} == 9 and int(rand(100))<45){
				${'dmg'.$wi} = ${'dmg'.$wi}*2;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���p���`�I</font>������I";
			}
			#��]
			if(${'twaza'.$wi} == 10 and int(rand(100))<20){
				${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(4)+1);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z��]�I</font>���邮�邮��I";
			}
			#�t�]��
			if(${'twaza'.$wi} == 11 and int(rand(100))<10){
				if(${'thp'.$wi.'_flg'} < ${'tmhp'.$wi}/10){ ${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(8)+2); }
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�t�]���I</font>�ǂ���!?";
			}
			#���Q
			if(${'twaza'.$wi} == 12 and int(rand(100))<30){
				$yasumu = int(rand(${'dmg'.$wi}));
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'dmg'.$wi} = 0;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���Q�I</font>HP��$yasumu�񕜂����I";
			}
			#�ÎE
			if(${'twaza'.$wi} == 13 and int(rand(100))<10){
				if(int(rand(2))==0){
					${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(8)+2);
					${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�ÎE�I</font>�����I�I";
				}else {
					${'thp'.$wi.'_flg'} = 1;
					${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�ÎE�I</font>���s�I�I";
				}
			}
			#�x��
			if(${'twaza'.$wi} == 14 and int(rand(100))<20){
				$yasumu = int(rand(${'dmg'.$wi}));
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�x��I</font>HP��$yasumu�񕜂����I";
			}
			#�Ԃ񉣂�
			if(${'twaza'.$wi} == 15 and int(rand(100))<10){
				${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(4)+1);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�Ԃ񉣂�I</font>�����ꂥ���I";
			}
			#����
			if(${'twaza'.$wi} == 16 and int(rand(100))<30){
				${'dmg'.$wi} = int(${'dmg'.$wi}*int(rand(4)+1)/int(rand(2)+1));
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���́I</font>�����������I";
			}
			#���I��
			if(${'twaza'.$wi} == 17 and int(rand(100))<15){
				${'dmg'.$wi} += int(rand(${'thp'.$wi.'_flg'}/2));
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���I�݁I</font>�V���[�[�I";
			}
			#����
			if(${'twaza'.$wi} == 18 and int(rand(100))<3){
				${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(8)+2);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���I</font>���������c�H";
			}
			#��
			if(${'twaza'.$wi} == 19 and int(rand(100))<30){
				${'dmg'.$wi} = ${'dmg'.$wi}*2;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�󕗁I</font>�т�΂��I";
			}
			#���@���M�K�u���C�N
			if(${'twaza'.$wi} == 20 and int(rand(100))<20){
				${'dmg'.$wi} = ${'dmg'.$wi}*int(rand(4)+1);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���@���M�K�u���C�N�I</font>�ނ�I";
			}
			#���Y
			if(${'twaza'.$wi} == 21 and int(rand(100))<20){
				$sikei=int(rand(4)+1);
				if( ${'thp'.$sikei.'_flg'} > 0 ){ ${'thp'.$sikei.'_flg'} = 1; }
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z���Y�I</font>�N�n�n�n�n�I�I";
			}
			#�̂ق̂�
			if(${'twaza'.$wi} == 22 and int(rand(100))<20){
				$yasumu = int(rand($thp1_flg + $thp2_flg + $thp3_flg + $thp4_flg)/3);
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�̂ق́`��I</font>HP��$yasumu�񕜂����I";
			}
			#��邠����
			if(${'twaza'.$wi} == 23 and int(rand(100))<30){
				if(${'thp'.$wi.'_flg'} < ${'tmhp'.$wi}/3){ ${'dmg'.$wi} += int(rand(${'thp'.$wi.'_flg'})); }
				else{ ${'dmg'.$wi} += int(rand(${'thp'.$wi.'_flg'}/4)); }
				${'dmg'.$wi} = int(${'dmg'.$wi} *1.3);
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z��邠�����I</font>";
			}
			#�S�ŏ���
			if(${'twaza'.$wi} == 24 and int(rand(100))<20){
				$onidame = ${'dmg'.$wi} + int(rand(1000));
				$dmg1=0; $dmg2=0; $dmg3=0; $dmg4=0;
				${'dmg'.$wi} = $onidame;
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�S�ŏ����I</font>�F�r�r���ē������~�܂����I�S�łƓ�l�ŏP��������I";
			}
			#�a��
			if(${'twaza'.$wi} == 25 and int(rand(100))<35){
				$hit=0;
				for($aricount=0;$aricount<5;$aricount++){
					$ari = int(rand(4)+1);
					if($ari!=$wi and ${'thp'.$ari.'_flg'}>0 and $hit!=1){
						if($ari!=1){ $taisyo1=$ari; }
						if($ari!=2){ $taisyo2=$ari; }
						if($ari!=3){ $taisyo3=$ari; }
						if($ari!=4){ $taisyo4=$ari; }
						${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�a�ˁI</font>${'tname'.$ari}���W���U���I";
						$hit=1;
					}
				}
			}
			#�V��
			if(${'twaza'.$wi} == 26 and int(rand(100))<10){
				$yasumu = int(rand($dmg1 + $dmg2 + $dmg3 + $dmg4));
				if(${'dmg'.$wi}>0){ ${'dmg'.$wi} += $yasumu; }
				${'thp'.$wi.'_flg'} += $yasumu;
				if(${'thp'.$wi.'_flg'} > ${'tmhp'.$wi}){${'thp'.$wi.'_flg'}=${'tmhp'.$wi};}
				${'com'.$wi}.="<font class= \"yellow\" size=4>�K�E�Z�V���I</font>HP��$yasumu�񕜂����I";
			}
		}
	}
}
sub hp_sum {

	if($thp1_flg<1){$dmg1 = 0;}
	if($thp2_flg<1){$dmg2 = 0;}
	if($thp3_flg<1){$dmg3 = 0;}
	if($thp4_flg<1){$dmg4 = 0;}

	for($tai=1;$tai<6;$tai++){
		if (${'taisyo'.$tai} ==1){
			$thp1_flg = $thp1_flg - ${'dmg'.$tai};
		}elsif(${'taisyo'.$tai} ==2) {
			$thp2_flg = $thp2_flg - ${'dmg'.$tai};
		}elsif(${'taisyo'.$tai} ==3){
			$thp3_flg = $thp3_flg - ${'dmg'.$tai};
		}elsif(${'taisyo'.$tai} ==4){
			$thp4_flg = $thp4_flg - ${'dmg'.$tai};
		}
	}
}
sub winlose {
	if($thp1_flg<1 and $thp2_flg<1 and $thp3_flg<1 and $thp4_flg<1){
		#$win = 5;
		$thp1_flg= int($tmhp1/10);
		$thp2_flg= int($tmhp2/10);
		$thp3_flg= int($tmhp3/10);
		$thp4_flg= int($tmhp4/10);
	}elsif ($thp2_flg<1 and $thp3_flg<1 and $thp4_flg<1){ 
		$win = 1; last;
	}elsif ($thp1_flg<1 and $thp3_flg<1 and $thp4_flg<1) {
		$win = 2; last;
	}elsif ($thp1_flg<1 and $thp2_flg<1 and $thp4_flg<1) {
		$win = 3; last;
	}elsif ($thp1_flg<1 and $thp2_flg<1 and $thp3_flg<1) {
		$win = 4; last;
	}else{ $win = 5; }
}

sub tbattle_sts {

		$kekka[$j] = <<"EOM";
	<TABLE BORDER=0 align="center">
	<TR><TD COLSPAN= "3" ALIGN= "center">$i�^�[��</TD></TR>
	<TABLE BORDER=0 align="center">
	<TR><TD CLASS= "b1" id= "td2">�Ȃ܂�</TD><TD CLASS= "b1" id= "td2">HP</TD></TR>
EOM
	if($thp1_flg>0){
		$kekka[$j] .= <<"EOM";
		<TR><TD class= "b2">	$tname1			</TD>
		<TD class= "b2">	$thp1_flg\/$tmhp1	</TD></TR>
EOM
	}
	if($thp2_flg>0){
		$kekka[$j] .= <<"EOM";
		<TR><TD class= "b2">	$tname2			</TD>
		<TD class= "b2">	$thp2_flg\/$tmhp2	</TD></TR>
EOM
	}
	if($thp3_flg>0){
		$kekka[$j] .= <<"EOM";
		<TR><TD class= "b2">	$tname3			</TD>
		<TD class= "b2">	$thp3_flg\/$tmhp3	</TD></TR>
EOM
	}
	if($thp4_flg>0){
		$kekka[$j] .= <<"EOM";
		<TR><TD class= "b2">	$tname4			</TD>
		<TD class= "b2">	$thp4_flg\/$tmhp4	</TD></TR>
EOM
	}
	$kekka[$j] .= <<"EOM";
	</TABLE>
	<table align="center">
	<tr><td class="b1" id="td2">�퓬�I�I</td></tr>
EOM
	for($tai=0;$tai<5;$tai++){
		if(${'taisyo'.$tai}==1){${'mname'.$tai}=$tname1;}
		if(${'taisyo'.$tai}==2){${'mname'.$tai}=$tname2;}
		if(${'taisyo'.$tai}==3){${'mname'.$tai}=$tname3;}
		if(${'taisyo'.$tai}==4){${'mname'.$tai}=$tname4;}
	}
	if($thp1_flg > 0){
		$kekka[$j] .= <<"EOM";
		<tr><td class="b2"><br>$tname1�̍U���I�I$com1 $mname1 �� <font class= "yellow">$dmg1</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
	if($thp2_flg > 0){
		$kekka[$j] .= <<"EOM";
		<tr><td class="b2"><br>$tname2�̍U���I�I$com2 $mname2 �� <font class= "yellow">$dmg2</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
	if($thp3_flg > 0){
		$kekka[$j] .= <<"EOM";
		<tr><td class="b2"><br>$tname3�̍U���I�I$com3 $mname3 �� <font class= "yellow">$dmg3</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
	if($thp4_flg > 0){
		$kekka[$j] .= <<"EOM";
		<tr><td class="b2"><br>$tname4�̍U���I�I$com4 $mname4 �� <font class= "yellow">$dmg4</font> �̃_���[�W��^�����B<br>�@</td></tr>
EOM
	}
	if($tsyougun){
		$kekka[$j] .= <<"EOM";
		<tr><td class="b2"><br><font color="red">���R�����ꂽ�I�I$com5</font><br>�@</td></tr>
EOM
	}
	$kekka[$j] .= "</table></table>";
}
sub sentoukeka{
	if($win==1){
 		$kekka[31] = "<b><font size=5>$tname1�̏����I</font></b><br>";
	}elsif($win==2){
		$kekka[31] = "<b><font size=5>$tname2�̏����I</font></b><br>";
	}elsif($win==3){
		$kekka[31] = "<b><font size=5>$tname3�̏����I</font></b><br>";
	}elsif($win==4){
		$kekka[31] = "<b><font size=5>$tname4�̏����I</font></b><br>";
	} else {
		$kekka[31] = "<b><font size=5>�Ȃ�ƁA���������c�B</font></b><br>";
	}
}
sub mons_footer{
	if($win==3){
		print "$comment (��)<br>\n";
	} elsif($win==1){
		print "$comment <br>\n";
	print <<"EOM";
<B>���`�̎g��</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
�u���܂��ˁI�I<br>
���Ȃ��Ȃ�A��R��喂���ɏ��Ă��\�\\��������܂��B<br>
�t���Ă��Ă��������B�v
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=win>
<input type=submit class=btn value="���Ă���">
</form>
EOM
	} elsif($win==2){
		print "$comment <br>\n";
	} else {
		print "$comment (��)<br>\n";
	}
	&chara_regist;

	print <<"EOM";
<form action="$script">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}
