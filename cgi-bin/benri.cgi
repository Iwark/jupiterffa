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
<form action="benri.cgi" >
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

	&item_load;

	&header;

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	open(IN,"mayaku.cgi");
	@mayaku_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>�֗���</h1>
<hr size=0>
<FONT SIZE=3>
<B>�֗����̂��Z����</B><BR>
�u����ɂ��́B�h���[�����[���h��������z���Ă����֗����̃X�e�B�[�u���ł��B<br>
�����A�h���[�����[���h�̌��H�@����͂�����Ɣ���Ȃ��Ȃ��c(�E���E)<br>
�����ł́A�N�̎����Ă��鈫���E�̃A�C�e��(<font color="red" size=4>����</font>)��l�ԊE�p�ɒ������Ďg�����Ƃ��ł����B<br>
<font color="red" size=4>����</font>�ɂ��Ă̐����́A��񉮂̂�������Ƃ��ɕ����Ă��������B<br>
���������΍ŋߒ킪�J�W�m�̌o�c���n�߂��̂ŁA��������s���邩��ǂ�������s���Ă݂Ă��������B<br>
EOM
if($chara[24]==1400){
	print <<"EOM";
<font color="yellow">
�����A�N�A���̕���͂ǂ��Ŏ�ɓ��ꂽ�́I�H<br>
����͐������킾��B�����^���邱�ƂŐ������镐�킾�B<br>
����ɁA�����E���猳�f����ɓ���āA�w�}�e���A�x����肷�邱�Ƃ��ł���΁A����ɓ���Ȕ\\�͂�^���邱�Ƃ��ł���񂾁I<br>
�}�e���A�̐����́A�X�̉��ɂ���}�e���A���ōs���Ă����B�}�e���A�����Z�p�������Ă���̂́A���̐��E�ł͂��������Ȃ̂��I<br>
�������A���̕��킪����i�K�ɒB����܂ł́A�}�e���A���֒ʂ��킯�ɂ͂����Ȃ��ȁc�Ƃ������A���ʂ�����ȁc�B<br>
</font>
EOM
}
if($chara[18]>2000){
	print <<"EOM";
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=submit class=btn value="�J�W�m��">
</form>
EOM
}
	print <<"EOM";
�v
</FONT>
<hr size=0>
<br>
EOM
	print <<"EOM";
<table><tr><th></th><th>����</th><th>��</th><th>�Ώ�</th></tr>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=mayaku>
EOM
	$i=0;
	foreach(@mayaku){
		if($_>0){
			foreach(@mayaku_data){
				($mayano,$mayaname,$mayakind) = split(/<>/);
				if($mayano == $i){last;}
			}
			print "<tr><th>";
			if($mayakind==0){
				$kind="�I���W�i������";
				if($chara[24]==1400){
					$c=$i+1;
					print "<input type=radio name=item_no value=$c>";
				}else{
					print "�~";
				}
			}
			if($mayakind==1){
				$kind="�y�b�g(Lv1000�̃y�b�g�̂�)";
				if($chara[46]==1000){
					$c=$i+1;
					print "<input type=radio name=item_no value=$c>";
				}else{
					print "�~";
				}
			}
			if($mayakind==2){
				$kind="�y�b�g";
				$c=$i+1;
				print "<input type=radio name=item_no value=$c>";
			}
			print "</th><th>$mayaname</th><th>$_</th><th>$kind</th></tr>";
		}
		$i++;
	}
	print <<"EOM";
</table><br>
<input type=submit class=btn value="�g�p����">
</form>
<hr size=0>
EOM
if($chara[128]==5 and $chara[24]==1400){
	print <<"EOM";
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia>
<input type=submit class=btn value="�}�e���A����">
</form>
<hr size=0>
EOM
}
if($chara[24]==1400){
$next_ex = $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;
	print <<"EOM";
<br>���݂̌o���l�F$chara[17]/$next_ex<br><br>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=seityou>
</form>
EOM
}
	$new_chara = $chara_log;

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

	$chara[146]+=3;
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�͂��A�ǁ[����</B><BR></font>
<br>
<form action="benri.cgi" >
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
sub seityou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($in{'abi'} eq "") {
		&error("�^����o���l�����͂���Ă��܂���B$back_form");
	}
	if ($in{'abi'} =~ m/[^0-9]/){
		&error("�^����o���l�ɐ����ȊO�̕������܂܂�Ă��܂��B$back_form"); 
	}
	if ($in{'abi'} > $chara[17]){
		&error("�^����o���l�������Ă���o���l���������ł��B$back_form"); 
	}

	$item[26]+=$in{'abi'};
	$chara[17]-=$in{'abi'};
	if(!$item[27]){$item[27]=1;}
	if($item[27]<=10){
		while($item[26] >= $item[27] * 10000000 ){
		$item[1]+=10;
		$item[2]+=5;
		$item[26]-=$item[27] * 10000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]�̃��x����$item[27]�ɂ��������I�U���́{�P�O�A�������{�T</font><br>";
		}
	}elsif($item[27]<=100){
		while($item[26] >= $item[27] * 50000000 ){
		$item[1]+=20;
		$item[2]+=10;
		$item[26]-=$item[27] * 50000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]�̃��x����$item[27]�ɂ��������I�U���́{�Q�O�A�������{�P�O</font><br>";
		}
	}else{
		while($item[26] >= $item[27] * 100000000 ){
		$item[1]+=30;
		$item[2]+=15;
		$item[26]-=$item[27] * 100000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]�̃��x����$item[27]�ɂ��������I�U���́{�R�O�A�������{�P�T</font><br>";
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
<B>�����$in{'abi'}�̌o���l��^�����B</B><BR>
$lvup</font>
<br>
<form action="benri.cgi" >
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
sub mayaku {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if(!$in{'item_no'}){&error("�����ƑI��ł�������");}
	else{$item_no=$in{'item_no'}-1;}

	if($item_no==0 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(30)+30);
		}else{
			$up=int(rand(100)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up�オ�����I</font><br>";
	}elsif($item_no==1 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(30)+30);
		}else{
			$up=int(rand(100)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up�オ�����I</font><br>";
	}elsif($item_no==2 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(30)+30);
			$up2=int(rand(30)+30);
		}else{
			$up1=int(rand(100)+100);
			$up2=int(rand(100)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up1�オ�����I</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up2�オ�����I</font><br>";
	}elsif($item_no==3 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(60)+30);
		}else{
			$up=int(rand(200)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up�オ�����I</font><br>";
	}elsif($item_no==4 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(60)+30);
		}else{
			$up=int(rand(200)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up�オ�����I</font><br>";
	}elsif($item_no==5 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(60)+30);
			$up2=int(rand(60)+30);
		}else{
			$up1=int(rand(200)+100);
			$up2=int(rand(200)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up1�オ�����I</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up2�オ�����I</font><br>";
	}elsif($item_no==6 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(90)+30);
		}else{
			$up=int(rand(300)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up�オ�����I</font><br>";
	}elsif($item_no==7 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(90)+30);
		}else{
			$up=int(rand(300)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up�オ�����I</font><br>";
	}elsif($item_no==8 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(90)+30);
			$up2=int(rand(90)+30);
		}else{
			$up1=int(rand(300)+100);
			$up2=int(rand(300)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]�̍U���͂�$up1�オ�����I</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]�̖����͂�$up2�オ�����I</font><br>";
	}elsif($item_no==10 and $chara[46]==1000){
		$up=int(rand(10000000)+10000000);
		$chara[44]+=$up;
		$lvup.="<font color=\"red\" size=5>$chara[39]�̍U���͂�$up�オ�����I</font><br>";
	}elsif($item_no==11 and $chara[46]==1000){
		$up=int(rand(1000000)+1000000);
		$chara[43]+=$up;
		$chara[42]=$chara[43];
		$lvup.="<font color=\"red\" size=5>$chara[39]��HP��$up�オ�����I</font><br>";
	}elsif($item_no==12){
		$up=int(rand(100)+1);
		if($chara[46]+$up>1000){
			$chara[46]=1000;
			$lvup.="<font color=\"red\" size=5>$chara[39]�̃��x����1000�ɂȂ����I</font><br>";
		}elsif($chara[46]+$up>20 and $chara[46]+$up<120){
			$chara[46]=20;
			$lvup.="<font color=\"red\" size=5>$chara[39]�̃��x����20�ɂȂ����I</font><br>";
		}else{
			$chara[46]+=$up;
			$lvup.="<font color=\"red\" size=5>$chara[39]��HP��$up�オ�����I</font><br>";
		}
	}

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	$mayaku[$item_no]-=1;
	$new_mayaku = '';
	$new_mayaku = join('<>',@mayaku);
	$new_mayaku .= '<>';
	open(OUT,">./mayaku/$chara[0].cgi");
	print OUT $new_mayaku;
	close(OUT);

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>������g�p�����B</B><BR>
$lvup</font>
<br>
<form action="benri.cgi" >
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
sub materia{

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if(!$isi[29]){$isi[29]=0;}
	if(!$isi[30]){$isi[30]=0;}
	if(!$isi[31]){$isi[31]=0;}
	if(!$isi[32]){$isi[32]=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);

	&header;

	print << "EOM";
<h1>�}�e���A��</h1><hr>
<font size=3>
<B>�֗����̂��Z����</B><BR>
�u�������}�e���A�����B���f����}�e���A�𐸐����A����ɓZ���ꏊ�Ȃ̂��I<br>
�}�e���A�����̍ۂ̒��ӎ�����������Ă������B<br>
�@�}�e���A��t�����鐔��<font color="red" size=4>�L���p</font>�ƌĂԁB<br>
<font color="red" size=4>������Ԃ̃L���p�͂P�ł���A�ő�L���p�͂S</font>���B�L���p���グ��̂ɂ͓���ȃ}�e���A���K�v���B<br>
�A����̌^�ɂ���ēK������}�e���A���Ⴄ�B<font color="red" size=4>�s�K���̃}�e���A��Z���ׂɂ́A�L���p���Q�K�v</font>���B<br>
�i�������A���������}�e���A������̌^�ɓK�����Ă��邩�ǂ����́A\�\\�ߒm�邱�Ƃ��o����B�j<br>
�B�}�e���A�́A��������B�i��������̂ɂ����f���g���B�i���悪��������悤�ȃ}�e���A�����݂��邩������Ȃ��ȁB<br>
�C<font color="red" size=4>�ŏI�`�Ԃ܂Ői������ƁA�K�v�L���p���P������</font>�B�s�K���}�e���A���ƁA�K�v�L���p���R�ɂȂ�B<br>
�D<font color="red" size=4>�����^�̃}�e���A�͂Q�܂�</font>�����t�����Ȃ��B�܂��A����}�e���A�𕡐��Z�����Ƃ͏o���Ȃ��B<br>
<br>
�ȏ�B�}�e���A�����ɂ��A�}�e���A�����ɂ��A�q��łȂ����̌��f���K�v�ɂȂ�B<br>
����ɁA�ǂ̂��炢�A�ǂ̌��f��g�ݍ��킹��΂ǂ̃}�e���A���o����̂��A����͂���Ă݂Ȃ��Ƃ킩��Ȃ��B<br>
�قڑS�Ẵ}�e���A�́A�����͂�����ȁB���f��΃R���̂悤�ɊȒP�ɏW�߂���Ƃ͎v��Ȃ��ق����������B�v<br></font>
<hr>
���݂̃L���p�F$item[29] / $item[30]<br>
<table><tr><th>���݂̃}�e���A</th><th>���x��</th><th>���E���x��(�ŏI�`��)</th></tr>
EOM
	foreach(@mtdata){
		@mt = split(/<>/);
		for($i=31;$i<39;$i++){
			$mtt=int($item[$i]/100+1);
			if($item[$i]%100 == $mt[0]){print "<tr><th>$mt[2]</th><th>$mtt</th><th>$mt[7]</th></tr>";}
		}
	}
	print << "EOM";
</table>
<table width='20%' border=0>
<form action="benri.cgi" >
<table><tr><th>���f</th><th>��</th><th>�g�p��</th></tr>
<tr><td>�΂̌��f</td><td>$isi[29]</td><td><input type="text" name="hi" size="4"></td></tr>
<tr><td>���̌��f</td><td>$isi[30]</td><td><input type="text" name="mizu" size="4"></td></tr>
<tr><td>�ł̌��f</td><td>$isi[31]</td><td><input type="text" name="yami" size="4"></td></tr>
<tr><td>���̌��f</td><td>$isi[32]</td><td><input type="text" name="hikari" size="4"></td></tr>
</table>
<input type="hidden" name="mode" value="seisei">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�}�e���A�����ɒ���"></form>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="�}�e���A�̕t���ւ�">
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub materia2{

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if(!$isi[29]){$isi[29]=0;}
	if(!$isi[30]){$isi[30]=0;}
	if(!$isi[31]){$isi[31]=0;}
	if(!$isi[32]){$isi[32]=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	&header;

	print << "EOM";
<h1>�}�e���A��</h1><hr>
<font size=3>
<B>�֗����̂��Z����</B><BR>
�u�����̓}�e���A�q�ɂ��B<br>
�N�̃}�e���A���O������A�����ł��邼�B<br>
�}�e���A�̕ۊǂ́A���ŐV�ݔ��ŁA���ŐV�̒��ӂ𕥂��čs���Ă���B<br>
�c��Ȕ�p���������Ă��邪�c�܂�$chara[4]�́A�����Ŏg�킹�Ă����悤�B�v<br></font>
<hr>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="hazusu">
���݂̃L���p�F$item[29] / $item[30]<br>
<table><tr><th></th><th>���݂̃}�e���A</th><th>���x��</th><th>���E���x��(�ŏI�`��)</th></tr>
EOM
	foreach(@mtdata){
		@mt = split(/<>/);
		for($i=31;$i<39;$i++){
			$mtt=int($item[$i]/100+1);
			if($item[$i]%100 == $mt[0]){
				print << "EOM";
<tr>
<th><input type=radio name=item_no value="$i"></th>
<th>$mt[2]</th>
<th>$mtt</th>
<th>$mt[7]</th>
</tr>
EOM
			}
		}
	}
	print << "EOM";
</table>
<input type=submit class=btn value="�}�e���A���O��">
</form>
<table>
<br>
<h3>�}�e���A�q��</h3>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="soubi">
<table>
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>���x��</th><th nowrap>���E���x��</th></tr>
EOM
	$i=1;
	foreach(@mtcdata){
		@mtc = split(/<>/);
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no value=$i>
</td>
<td class=b1 nowrap>$mtc[2]</td>
<td align=right class=b1>$mtc[3]</td>
<td align=right class=b1>$mtc[4]</td>
</tr>
EOM
		$i++;
	}
		print << "EOM";
</table>
<input type=submit class=btn value="�}�e���A��Z��">
</form>
<hr>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia>
<input type=submit class=btn value="�߂�">
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub seisei{

	&chara_load;

	&chara_check;

	&item_load;

	if ($in{'hi'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'mizu'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'yami'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}
	if ($in{'hikari'} =~ m/[^0-9]/){
		&error("�����ȊO�����͂���Ă��܂��B$back_form"); 
	}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$hi=$in{'hi'};
	if($hi > $isi[29]){&error("�΂̌��f������܂���B$back_form");}
	$mizu=$in{'mizu'};
	if($mizu > $isi[30]){&error("���̌��f������܂���B$back_form");}
	$yami=$in{'yami'};
	if($yami > $isi[31]){&error("�ł̌��f������܂���B$back_form");}
	$hikari=$in{'hikari'};
	if($hikari > $isi[32]){&error("���̌��f������܂���B$back_form");}
	$goukei=$hi+$mizu+$yami+$hikari;
	if(!$goukei){&error("���f���P���g���Ă��܂���B$back_form");}
	if(!$hi){$hi=0;}if(!$mizu){$mizu=0;}if(!$yami){$yami=0;}if(!$hikari){$hikari=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	foreach(@mtdata){
		@mt = split(/<>/);
		if($mt[3] <= $hi and $mt[4] <= $mizu and $mt[5] <= $yami and $mt[6] <= $hikari){last;}
	}
	if($mt[1] == $item[28]){
		$cap=1;
	}elsif($mt[1]==5){
		if($item[30]==4){
			&error("����ȏ�L���p���グ�邱�Ƃ͏o���܂���B$back_form");
		}else{
			$cap=0;
		}
	}elsif($mt[1]==6){
		if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
		$cap=0;
	}else{
		$cap=2;
	}
	if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-2){$cap=1;}elsif($item[31]%100 == $mt[0]){$cap=0;}
	if($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-2){$cap=1;}elsif($item[32]%100 == $mt[0]){$cap=0;}
	if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-2){$cap=1;}elsif($item[33]%100 == $mt[0]){$cap=0;}
	if($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-2){$cap=1;}elsif($item[34]%100 == $mt[0]){$cap=0;}
	if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-2){$cap=1;}elsif($item[35]%100 == $mt[0]){$cap=0;}
	if($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-2){$cap=1;}elsif($item[36]%100 == $mt[0]){$cap=0;}
	if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-2){$cap=1;}elsif($item[37]%100 == $mt[0]){$cap=0;}
	if($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-2){$cap=1;}elsif($item[38]%100 == $mt[0]){$cap=0;}

	if($item[29] < $cap){&error("�L���p������܂���B$back_form");}
	
	if($mt[1] == 1){
		if($item[31] and $item[32] and $item[31]%100 != $mt[0] and $item[32]%100 != $mt[0]){
			&error("����ȏ㕨���^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[31]%100 == $mt[0]){
			if(int($item[31]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}elsif($item[32]%100 == $mt[0]){
			if(int($item[32]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}else{
			$com1="�����^�̃}�e���A���o�������ł����A";
		}
	}
	if($mt[1] == 2){
		if($item[33] and $item[34] and $item[33]%100 != $mt[0] and $item[34]%100 != $mt[0]){
			&error("����ȏ�K�E�^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[33]%100 == $mt[0]){
			if(int($item[33]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}elsif($item[34]%100 == $mt[0]){
			if(int($item[34]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}else{
			$com1="�K�E�^�̃}�e���A���o�������ł����A";
		}
	}
	if($mt[1] == 3){
		if($item[35] and $item[36] and $item[35]%100 != $mt[0] and $item[36]%100 != $mt[0]){
			&error("����ȏ�\�͌^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[35]%100 == $mt[0]){
			if(int($item[35]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}elsif($item[36]%100 == $mt[0]){
			if(int($item[36]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}else{
			$com1="�\\��\�^�̃}�e���A���o�������ł����A";
		}
	}
	if($mt[1] == 4){
		if($item[37] and $item[38] and $item[37]%100 != $mt[0] and $item[38]%100 != $mt[0]){
			&error("����ȏ����^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[37]%100 == $mt[0]){
			if(int($item[37]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}elsif($item[38]%100 == $mt[0]){
			if(int($item[38]/100)==$mt[7]-1){
				&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
			}else{
				$com1="$mt[2]���i���������ł����A";
			}
		}else{
			$com1="����^�̃}�e���A���o�������ł����A";
		}
	}
	if($mt[1] == 5){$com1="�L���p�A�b�v���o�������ł����A";}
	if($mt[1] == 6){$com1="�^�E�`�F���W���o�������ł���";}
	if($mt[1] == 5 or $mt[1] == 6 or $goukei>=90){$com2="�����͂قڊm���ł��傤�B";}
	elsif($goukei>=75){$com2="�������Ă����������Ȃ��ł��傤�B";}
	elsif($goukei>=50){$com2="�����͉^����ł��B";}
	elsif($goukei>=25){$com2="�������錩���݂͒Ⴂ�ł��B";}
	elsif($goukei>=10){$com2="�܂��A�܂����s����ł��傤�B";}
	else{$com2="�قڊm���Ɏ��s���܂��B";}

	&header;

	print << "EOM";
<h2>�΂̌��f$hi�A���̌��f$mizu�A�ł̌��f$yami�A���̌��f$hikari���g���܂��B<br>
$com1$com2���s���܂����H<hr></h2>
<form action="benri.cgi" >
<input type="hidden" name="hi" value=$hi>
<input type="hidden" name="mizu" value=$mizu>
<input type="hidden" name="yami" value=$yami>
<input type="hidden" name="hikari" value=$hikari>
<input type="hidden" name="mode" value="jikko">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="���s����"></form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub jikko{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$hi=$in{'hi'};
	if($hi > $isi[29]){&error("�΂̌��f������܂���B$back_form");}
	$mizu=$in{'mizu'};
	if($mizu > $isi[30]){&error("���̌��f������܂���B$back_form");}
	$yami=$in{'yami'};
	if($yami > $isi[31]){&error("�ł̌��f������܂���B$back_form");}
	$hikari=$in{'hikari'};
	if($hikari > $isi[32]){&error("���̌��f������܂���B$back_form");}
	$goukei=$hi+$mizu+$yami+$hikari;
	if(!$goukei){&error("���f���P���g���Ă��܂���B$back_form");}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	foreach(@mtdata){
		@mt = split(/<>/);
		if($mt[3] <= $hi and $mt[4] <= $mizu and $mt[5] <= $yami and $mt[6] <= $hikari){last;}
	}
	if($mt[1] == $item[28]){
		$cap=1;
	}elsif($mt[1]==5){
		if($item[30]==4){
			&error("����ȏ�L���p���グ�邱�Ƃ͏o���܂���B$back_form");
		}else{
			$cap=0;
		}
	}elsif($mt[1]==6){
		if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
		$cap=0;
	}else{
		$cap=2;
	}
	if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-2){$cap=1;}elsif($item[31]%100 == $mt[0]){$cap=0;}
	if($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-2){$cap=1;}elsif($item[32]%100 == $mt[0]){$cap=0;}
	if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-2){$cap=1;}elsif($item[33]%100 == $mt[0]){$cap=0;}
	if($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-2){$cap=1;}elsif($item[34]%100 == $mt[0]){$cap=0;}
	if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-2){$cap=1;}elsif($item[35]%100 == $mt[0]){$cap=0;}
	if($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-2){$cap=1;}elsif($item[36]%100 == $mt[0]){$cap=0;}
	if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-2){$cap=1;}elsif($item[37]%100 == $mt[0]){$cap=0;}
	if($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-2){$cap=1;}elsif($item[38]%100 == $mt[0]){$cap=0;}

	if($item[29] < $cap){&error("�L���p������܂���B$back_form");}
	
	if($mt[1] == 1){
		if($item[31] and $item[32] and $item[31]%100 != $mt[0] and $item[32]%100 != $mt[0]){
			&error("����ȏ㕨���^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}elsif($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}
	}
	if($mt[1] == 2){
		if($item[33] and $item[34] and $item[33]%100 != $mt[0] and $item[34]%100 != $mt[0]){
			&error("����ȏ�K�E�^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}elsif($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}
	}
	if($mt[1] == 3){
		if($item[35] and $item[36] and $item[35]%100 != $mt[0] and $item[36]%100 != $mt[0]){
			&error("����ȏ�\�͌^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}elsif($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}
	}
	if($mt[1] == 4){
		if($item[37] and $item[38] and $item[37]%100 != $mt[0] and $item[38]%100 != $mt[0]){
			&error("����ȏ����^�̃A�r��Z�����Ƃ͏o���܂���B$back_form");
		}
		if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}elsif($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-1){
			&error("����ȏ�$mt[2]��i�������邱�Ƃ͏o���܂���B$back_form");
		}
	}

	$isi[29]-=$hi;
	$isi[30]-=$mizu;
	$isi[31]-=$yami;
	$isi[32]-=$hikari;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);
	if($mt[0]<5){$goukei=int($goukei*1.5);}
	if($mt[1] == 5){
		$item[29]+=1;
		$item[30]+=1;
		$com="�L���p�A�b�v�ɐ������܂����I";
	}elsif($mt[1] == 6){
		$lock_file = "$lockfolder/syoku$in{'id'}.lock";	
		&lock($lock_file,'SK');
		&syoku_load;
		$syoku_master[51] = 0;
		$syoku_master[52] = 0;
		$syoku_master[53] = 0;
		$syoku_master[54] = 0;
		&syoku_regist;
		&unlock($lock_file,'SK');
		if($chara[51]==71 or $chara[51]==72 or $chara[51]==73 or $chara[51]==74){$chara[51]=0;$chara[13]+=650;}
		if($chara[52]==71 or $chara[52]==72 or $chara[52]==73 or $chara[52]==74){$chara[52]=0;$chara[13]+=650;}
		if($chara[53]==71 or $chara[53]==72 or $chara[53]==73 or $chara[53]==74){$chara[53]=0;$chara[13]+=650;}
		if($chara[54]==71 or $chara[54]==72 or $chara[54]==73 or $chara[54]==74){$chara[54]=0;$chara[13]+=650;}
		$chara[14]=51+int(rand(4));
	
		$chara[33]=1;
		if($mt[0]==98){$chara[33]=80;}
		&chara_regist;
		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
		$com="�^�E�`�F���W�ɐ������܂����I";
	}elsif(int(rand(100))<$goukei){
		if($mt[1] == 1){
			if($item[31]%100 == $mt[0]){
				$item[31]+=100;
				if(int($item[31]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[32]%100 == $mt[0]){
				$item[32]+=100;
				if(int($item[32]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[31]){
				$item[32]=$mt[0];
			}else{
				$item[31]=$mt[0];
			}
		}
		if($mt[1] == 2){
			if($item[33]%100 == $mt[0]){
				$item[33]+=100;
				if(int($item[33]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[34]%100 == $mt[0]){
				$item[34]+=100;
				if(int($item[34]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[33]){
				$item[34]=$mt[0];
			}else{
				$item[33]=$mt[0];
			}
		}
		if($mt[1] == 3){
			if($item[35]%100 == $mt[0]){
				$item[35]+=100;
				if(int($item[35]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[36]%100 == $mt[0]){
				$item[36]+=100;
				if(int($item[36]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[35]){
				$item[36]=$mt[0];
			}else{
				$item[35]=$mt[0];
			}
		}
		if($mt[1] == 4){
			if($item[37]%100 == $mt[0]){
				$item[37]+=100;
				if(int($item[37]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[38]%100 == $mt[0]){
				$item[38]+=100;
				if(int($item[38]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[37]){
				$item[38]=$mt[0];
			}else{
				$item[37]=$mt[0];
			}
		}
		$item[29]-=$cap;
		$com="$mt[2]�̐����ɐ������܂����I$item[0]�ɓZ���܂��I�I�I�I";
	}else{
		$com="�}�e���A�����Ɏ��s���܂������(��)";
	}

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$com</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub soubi{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	if(!$in{'item_no'}){
		&error("�I�����Ă��������B");
	}
	$i=0;
	foreach(@mtcdata){
		@mtc = split(/<>/);
		if($i == $in{'item_no'}-1){last;}
		$i++;
	}
	if($mtc[1] == $item[28]){
		$cap=1;
	}else{
		$cap=2;
	}
	if($mtc[3]==$mtc[4]){ $cap++; }

	if($item[29] < $cap){&error("�L���p������܂���B$back_form");}
	
	if($mtc[1] == 1){
		if($item[31] and $item[32]){
			&error("����ȏ㕨���^�̃}�e���A��Z�����Ƃ͏o���܂���B$back_form");
		}elsif($item[31]%100 == $mtc[0] or $item[32]%100 == $mtc[0]){
			&error("���ɓ����}�e���A��Z���Ă��܂��B$back_form");
		}elsif($item[31]){
			$item[32]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[31]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 2){
		if($item[33] and $item[34]){
			&error("����ȏ�K�E�^�̃}�e���A��Z�����Ƃ͏o���܂���B$back_form");
		}elsif($item[33]%100 == $mtc[0] or $item[34]%100 == $mtc[0]){
			&error("���ɓ����}�e���A��Z���Ă��܂��B$back_form");
		}elsif($item[33]){
			$item[34]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[33]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 3){
		if($item[35] and $item[36]){
			&error("����ȏ�\�͌^�̃}�e���A��Z�����Ƃ͏o���܂���B$back_form");
		}elsif($item[35]%100 == $mtc[0] or $item[36]%100 == $mtc[0]){
			&error("���ɓ����}�e���A��Z���Ă��܂��B$back_form");
		}elsif($item[35]){
			$item[36]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[35]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 4){
		if($item[37] and $item[38]){
			&error("����ȏ����^�̃}�e���A��Z�����Ƃ͏o���܂���B$back_form");
		}elsif($item[37]%100 == $mtc[0] or $item[38]%100 == $mtc[0]){
			&error("���ɓ����}�e���A��Z���Ă��܂��B$back_form");
		}elsif($item[37]){
			$item[38]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[37]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}

	$item[29]-=$cap;

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	splice(@mtcdata,$i,1);

	open(OUT,">materia/$chara[0].cgi");
	print OUT @mtcdata;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$mtc[2]��Z���܂����B</B><BR><br><br>
</font>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub hazusu{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	if(!$in{'item_no'}){
		&error("�I�����Ă��������B");
	}

	$ino = $in{'item_no'};

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	$hit=0;
	foreach(@mtdata){
		@mt = split(/<>/);
		if($item[$ino]%100 == $mt[0]){$hit=1;last;}
	}
	if($hit!=1){ &error("�G���[�B");}
	$mtt = int($item[$ino]/100)+1;

	push(@mtcdata,"$mt[0]<>$mt[1]<>$mt[2]<>$mtt<>$mt[7]<>\n");

	if($mt[1] == $item[28]){
		$cap=1;
	}else{
		$cap=2;
	}
	if($mtt==$mt[7]){ $cap++; }

	$item[$ino] = 0;
	$item[29] += $cap;

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	open(OUT,">materia/$chara[0].cgi");
	print OUT @mtcdata;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$mt[2]���O���܂����B</B><BR><br><br>
</font>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="�߂�">
</form>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub syoku_regist {

	$new_syoku = '';

	for ($s=0;$s<=$chara[14];$s++) {
		if (!$syoku_master[$s]){
			$syoku_master[$s] = 0;
		}
	}

	$new_syoku = join('<>',@syoku_master);

	$new_syoku .= "<>";

	open(OUT,">./syoku/$in{'id'}.cgi");
	print OUT $new_syoku;
	close(OUT);

}