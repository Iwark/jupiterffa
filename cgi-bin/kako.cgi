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
<form action="kako.cgi" >
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

	if($chara[190]){
		$hit=0;
		if($chara[190]>2000){
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($chara[190] eq "$si_no"){$hit=1;last;}
			}
		}elsif($chara[190]>1000){
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($chara[190] eq "$si_no"){$hit=1;last;}
			}
		}else{
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $chara[190]){$hit=1;last;}
			}
		}
		if($hit){$setu="$i_name�ł��B";}else{$setu="�����ł��Ȃ����ꑕ���ł��B";}
	}else{
		$setu="����܂���B";
	}

	open(IN,"./kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	open(IN,"kakodata.cgi");
	@kako_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>���H��</h1>
<hr size=0>
<FONT SIZE=3>
<B>���H���̏��̐l</B><BR>
�u����H<B>$chara[4]</B>����ł��ˁE�E�E�H<br>
�嗤�������Ă������H���ł��B��낵���ˁO�O<br>
�F��Ȃ��Ƃ�����Ă邯�ǁA���͏������Ȃ́B<br>
�������Ԃő�������ꂽ�玄�̂Ƃ���Ɏ����Ă��Ȃ����B�����ł��邩�����Ă݂邩��B<br>
�ŋ�Ԃŉ�ꂽ�A�C�e�����������邱�Ƃ��ł��邯�Ǎ������B�v
</FONT>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="home.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="��n">
</form>
EOM
}
	print <<"EOM";
<hr size=0>
���H�ł���A�C�e���́c�B
<table><tr><th></th><th>�������</th><th>�K�v�ȑf�ނP</th><th>�K�v�ȑf�ނQ</th><th>�K�v�ȑf�ނR</th></tr>
<form action="kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kako>
EOM
	$i=0;
	foreach (@kako_data) {
		($ano,$aname,$bno,$bkazu,$cno,$ckazu,$dno,$dkazu) = split(/<>/);
		$bhit=0;$chit=0;$dhit=0;
		if($bkazu>0 and $isi[$bno]>0){$bhit=1;}
		if($ckazu>0 and $isi[$cno]>0){$chit=1;}
		if($dkazu>0 and $isi[$dno]>0){$dhit=1;}
		if($bhit==1 or $chit==1 or $dhit==1){
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			$g=0;$bname="";$cname="";$dname="";
			foreach(@sozai_data){
				($sozainame) = split(/<>/);
				if($g == $bno and $bkazu>0) {$bname="$sozainame�~$bkazu";}
				if($g == $cno and $ckazu>0) {$cname="$sozainame�~$ckazu";}
				if($g == $dno and $dkazu>0) {$dname="$sozainame�~$dkazu";}
				$g++;
			}
			print "<tr><th>";
			if($isi[$bno]>=$bkazu and $isi[$cno]>=$ckazu and $isi[$dno]>=$dkazu){
				$c=$i+1;
				print "<input type=radio name=item_no value=$c>";
			}else{
				print "�~";
			}
			print "</th><th>$aname</th><th>$bname</th><th>$cname</th><th>$dname</th></tr>";
		}
		$i++;
	}

	print <<"EOM";
</table><br>
<input type=submit class=btn value="���H����">
</form>
<hr size=0>
�����ł��鑕���́E�E�E$setu<br>
EOM
if($hit==1){
	$kane=int($chara[18]/100)*10000000;
	if($kane>5000000000){$kane=5000000000;}
	print <<"EOM";
�������܂����H($kane G)<br>
<form action="./kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=hidden name=hmod value=1>
<input type=submit class=btn value="����">
</form>
EOM
}
if($chara[200]==1){$setu="�ŕ����̌��ł��B";}
elsif($chara[200]==2){$setu="�ł̉H�߂ł��B";}
elsif($chara[200]==3){$setu="�ł̈߂ł��B";}
else{$setu="����܂���B";}
	print <<"EOM";
<hr size=0>
(�ŋ�Ԃŉ�ꂽ)�����ł��鑕���́E�E�E$setu<br>
EOM
if($chara[200]>0){
	$kane=int($chara[18]/100)*30000000;
	if($kane>5000000000){$kane=5000000000;}
	print <<"EOM";
�������܂����H($kane G)<br>
<form action="./kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=hidden name=hmod value=2>
<input type=submit class=btn value="����">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  ��񔃂��@�@  #
#----------------#
sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'hmod'}==1){$kane=int($chara[18]/100)*10000000;}
	else{$kane=int($chara[18]/100)*30000000;}
	if($kane>5000000000){$kane=5000000000;}

	if($chara[19]<$kane){&error("����������܂���");}
	else{$chara[19]-=$kane;}

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

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}
	elsif ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I");
	}
	elsif ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}

	if($chara[190] or $chara[200]){
		$hit=0;
		if($chara[190]>2000 or $chara[200]==2){
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($in{'hmod'}==1 and $chara[190] eq "$si_no"){$hit=1;last;}
				if($in{'hmod'}==2 and $i_name eq "�ł̉H��" and $chara[200]==2){$hit=1;last;}
			}
		}
		if($hit!=1){
			if($chara[190]>1000 or $chara[200]==1){
				if($in{'hmod'}==1){
					open(IN,"$item_file");
					@log_item = <IN>;
					close(IN);
					foreach(@log_item){
						($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
						if($chara[190] eq "$si_no"){$hit=2;last;}
					}
				}elsif($in{'hmod'}==2 and $chara[200]==1){
					open(IN,"data/item/stitem.ini");
					@log_item = <IN>;
					close(IN);
					foreach(@log_item){
						($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
						if($i_name eq "�ŕ����̌�"){$hit=2;last;}
					}
				}
			}
		}
		if($hit!=1 and $hit!=2){
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if($in{'hmod'}==1 and "$ai_no" eq "$chara[190]"){$hit=3;last;}
				if($in{'hmod'}==2 and $chara[200]==3 and $i_name eq "�ł̈�"){$hit=3;last;}
			}
		}
		if($hit==1){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_def,"$si_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
		}elsif($hit==2){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_item,"$si_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
		}elsif($hit==3){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_acs,"$ai_no<>$i_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
		}else{
			&error("$chara[190]�G���[$in{'hmod'}");
		}
	}else{&error("�G���[$chara[200]");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$i_name�𕜌����܂����B<br>
</font>
<br>
<form action="kako.cgi" >
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
sub kako {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if(!$in{'item_no'}){&error("�����ƑI��ł�������");}
	else{$item_no=$in{'item_no'}-1;}

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

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}
	elsif ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I");
	}
	elsif ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}

	open(IN,"kakodata.cgi");
	@kako_data = <IN>;
	close(IN);
	$i=0;
	foreach (@kako_data) {
		($ano,$aname,$bno,$bkazu,$cno,$ckazu,$dno,$dkazu) = split(/<>/);
		if($item_no==$i){last;}
		$i++;
	}

	open(IN,"./kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	$jjjj=0;$tttt=0;
	if($ano>9000){
		$ano-=9000;
		if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
		$chara[14]=$ano;
		$chara[33]=1;
		$hit=4;
		$jjjj=1;
	}elsif($ano>3000){
		$ano-=3000;
		$isi[$ano]+=1;
		$tttt=1;
		$so=0;
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		foreach(@sozai_data){
			($i_name) = split(/<>/);
			if($so == $ano) {$hit=4;last;}
			$so++;
		}
	}elsif($ano>2000){
		open(IN,"$def_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ano eq "$si_no"){$hit=1;last;}
		}
	}elsif($ano>1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($ano eq "$si_no"){$hit=2;last;}
		}
	}else{
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $ano){$hit=3;last;}
		}
	}

	if($hit==1){
		push(@souko_def,"$si_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}elsif($hit==2){
		push(@souko_item,"$si_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($hit==3){
		push(@souko_acs,"$ai_no<>$i_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}elsif($hit==4){
	}else{
		&error("�G���[");
	}
	if($bkazu>0){$isi[$bno]-=$bkazu;if($isi[$bno]<0){&error("�G���[�Qb");}}
	if($ckazu>0){$isi[$cno]-=$ckazu;if($isi[$cno]<0){&error("�G���[�Qc");}}
	if($dkazu>0){$isi[$dno]-=$dkazu;if($isi[$dno]<0){&error("�G���[�Qd");}}
	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		if($jjjj==1){$eg="$chara[4]�l�����ʐE�ɂȂ�܂����B";}
		elsif($tttt!=1){$eg="$chara[4]�l�����H�ɂ����$i_name����肵�܂����B";}
		if($eg){unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");}

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
if($jjjj==1){
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
���߂łƂ��������܂��I���ʐE�ɂȂ�܂����I<br>
</font>
<br>
<form action="kako.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
���H�ɂ����$i_name����肵�܂����B<br>
</font>
<br>
<form action="kako.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM
}

	&shopfooter;

	&footer;

	exit;
}