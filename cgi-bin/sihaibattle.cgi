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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

if ($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

# ���̃t�@�C���p�ݒ�
$temp_back = "$mode\_back";
$temp_midi = "$mode\_midi";
$backgif = $$temp_back;
$midi = $$temp_midi;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&$mode;

exit;

#----------------------#
#  �����X�^�[�Ƃ̐퓬  #
#----------------------#
sub sihai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[143]==$mday){
		&error("�����͂����킦�܂���B");
	}

	&item_load;

	&acs_add;
	$place=51;

	#����̃����o�[����
	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	$lock_file = "$lockfolder/$sihaisya[0].lock";
	&lock($lock_file,'DR');
	open(IN,"./charalog/$sihaisya[0].cgi");
	$smember1_data = <IN>;
	close(IN);
	$lock_file = "$lockfolder/$sihaisya[0].lock";
	&unlock($lock_file,'DR');
	@smem1 = split(/<>/,$smember1_data);
	open(IN,"./item/$sihaisya[0].cgi");
	$smem1item_log = <IN>;
	close(IN);
	@smem1item = split(/<>/,$smem1item_log);

	$khp_flg = $chara[15];
	if($chara[42]){
		$mem3hp_flg = $chara[42];
	}
	$smem1hp_flg = $smem1[15];
	if($smem1[42]){
		$smem3hp_flg = $smem1[42];
	}

	$i=1;
	$j=0;

	@battle_date=();

	$turn=$turn3;

	while($i<=$turn) {
		
		&shokika;

		&tyousensya;

		&acs_waza;

		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;
	
	&acs_sub;

	&hp_after;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B><br>�o�g���I</B></FONT>
EOM
	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

#------------------#
#�@����҂̍U��  �@#
#------------------#
sub tyousensya {

	if($khp_flg > 0){
		if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}
		if($item[20]==10){$g="red";}else{$g="";}
		$com1 = "$chara[4]�́A<font color=\"$g\">$item[0] $bukilv</font>�ōU���I�I";
		if( ($chara[7] + $item[1]) > ($chara[8] + $item[1]) ){
			$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);
		}else{
			$dmg1 += $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
		}
	}
	if($smem1hp_flg > 0){
		if($smem1item[20]){$bukilv="+ $smem1item[20]";}else{$bukilv="";}
		if($smem1item[20]==10){$g="red";}else{$g="";}
		$scom1 = "$smem1[4]�́A<font color=\"$g\">$smem1item[0] $bukilv</font>�ōU���I�I";
		if( ($smem1[7] + $smem1item[1]) > ($smem1[8] + $smem1item[1]) ){
			$sdmg1 += $smem1[7] * 4 + $smem1item[1] * 4 * int($smem1[7]/10+1);
		}else{
			$sdmg1 += $smem1[8] * 4 + $smem1item[1] * 4 * int($smem1[8]/10+1);
		}
	}
	if($chara[39]){
		# �y�b�g�_���[�W�v�Z
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
		$com4 = "$pename�̍U���I";
	
		$dmg4 = $chara[44];
	}
	if($smem1[39]){
		# �y�b�g�_���[�W�v�Z
	if($smem1[138] eq ""){$spename=$smem1[39];}else{$spename=$smem1[138];}
		$scom3 = "$spename�̍U���I";
	
		$sdmg3 = $smem1[44];
	}
}

#------------------#
#���A�N�Z�T���[����#
#------------------#
sub acs_waza {

	&acskouka;

}

#----------------------#
#����҃A�N�Z�T���[���Z#
#----------------------#
sub acs_add {
	$temp_chara[7] = $chara[7];
	$temp_chara[8] = $chara[8];
	$temp_chara[9] = $chara[9];
	$temp_chara[10] = $chara[10];
	$temp_chara[11] = $chara[11];
	$temp_chara[12] = $chara[12];

	$chara[7] += $item[8];
	$chara[8] += $item[9];
	$chara[9] += $item[10];
	$chara[10] += $item[11];
	$chara[11] += $item[12];
	$chara[12] += $item[13];

	@temp_item = @item;

	if ($item[7]) {
		require "./acstech/$item[7].pl";
	} else {
		require "./acstech/0.pl";
	}

	if($chara[47]){require "./ptech/$chara[47].pl";}
	else{require "./ptech/0.pl";}
}

#--------------------#
#�@����Ҕ\�͒l�����@#
#--------------------#
sub acs_sub {
	$chara[7] = $temp_chara[7];
	$chara[8] = $temp_chara[8];
	$chara[9] = $temp_chara[9];
	$chara[10] = $temp_chara[10];
	$chara[11] = $temp_chara[11];
	$chara[12] = $temp_chara[12];
	@item = @temp_item;
}

#--------------#
#�@�֐��������@#
#--------------#
sub shokika {
	$dmg1 = 0;
	$dmg4 = 0;
	$sdmg1 = 0;
	$sdmg3 = 0;
	$clit1 = "";
	$clit4 = "";
	$sclit1 = "";
	$sclit3 = "";
	$mem1hit_ritu=0;
	$mem4hit_ritu=50;
	$smem1hit_ritu=0;
	$smem3hit_ritu=50;
	$sake1 = 0;
	$sake4 = 0;
	$ssake1 = 0;
	$ssake3 = 0;
	$com1 = "";
	$com4 = "";
	$scom1 = "";
	$scom3 = "";
	$kawasi1 = "";
	$kawasi3 = "";
	$skawasi1 = "";
	$skawasi4 = "";
	$hpplus1 = 0;
	$hpplus4 = 0;
	$shpplus1 = 0;
	$shpplus3 = 0;
	$kaihuku1 = "";
	$kaihuku4 = "";
	$skaihuku1 = "";
	$skaihuku3 = "";
	$taisyo1=int(rand(2));
	$taisyo2=int(rand(2));
	$staisyo1=int(rand(2));
	$staisyo2=int(rand(2));
	if($smem1hp_flg<=0){$taisyo1=1;$taisyo2=1;}
	if($smem3hp_flg<=0){$taisyo1=0;$taisyo2=0;}
	if($khp_flg<=0){$staisyo1=1;$staisyo2=1;}
	if($mem3hp_flg<=0){$staisyo1=0;$staisyo2=0;}
}

#------------#
#�@HP�̌v�Z�@#
#------------#
sub hp_sum {

	if($khp_flg<1){$dmg1 = 0;}
	if($mem3hp_flg<1){$dmg4 = 0;}

	if($smem1hp_flg<1){$sdmg1 = 0;}
	if($smem3hp_flg<1){$sdmg3 = 0;}

	if($staisyo1==0){
		$khp_flg -= $sdmg1;
	}elsif($staisyo1==1){
		$mem3hp_flg -= $sdmg1;
	}
	if($staisyo2==0){
		$khp_flg -= $sdmg3;
	}elsif($staisyo1==1){
		$mem3hp_flg -= $sdmg3;
	}
	if($taisyo1==0){
		$smem1hp_flg -= $dmg1;
	}elsif($taisyo1==1){
		$smem3hp_flg -= $dmg4;
	}
	if($taisyo2==0){
		$smem1hp_flg -= $dmg1;
	}elsif($taisyo2==1){
		$smem3hp_flg -= $dmg4;
	}

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mem3hp_flg > $chara[43]) {
		$mem3hp_flg = $chara[43];
	}
	if ($smem1hp_flg > $smem1[16]){
		$smem1hp_flg = $smem1[16];
	}
	if ($smem3hp_flg > $smem1[43]) {
		$smem3hp_flg = $smem1[43];
	}
}

#------------#
#�@���s�����@#
#------------#
sub winlose {

	if ($smem1hp_flg<=0 and $smem3hp_flg<=0){ 
		$win = 1; last; #����
	}
	elsif ($khp_flg<1 and $mem3hp_flg<1) {
		$win = 2; last; #����
	}
	else{ $win = 3; } #��������
}

#------------------#
#���      	   #
#------------------#
sub mons_kaihi{
	
	#��𗦌v�Z
	$ci_plus = $item[2] + $item[16];
	$cd_plus = $item[5] + $item[17];
	$mem1ci_plus = $mem1item[2] + $mem1item[16];
	$mem1cd_plus = $mem1item[5] + $mem1item[17];

	$smem1ci_plus = $smem1item[2] + $smem1item[16];
	$smem1cd_plus = $smem1item[5] + $smem1item[17];

	# ������
	$mem1hit_ritu += int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $ci_plus;

	$smem1hit_ritu += int($smem1[9] / 3 + $smem1[11] / 10 + $smem1item[10] / 3)+ 40 + $smem1ci_plus;

	# ���
	$sake1	+= int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $cd_plus - $syamato1;

	$ssake1	+= int($smem1[9] / 10 + $smem1[11] / 20 + $smem1item[10]/10) + $smem1cd_plus - $yamato1;

	if ($sake1 > 90){$sake1 = 90;}

	if ($ssake1 > 90){$ssake1 = 90;}

	if ($staisyo1 ==0){
		if ($sdmg1 < $item[4]*(2+int($chara[10]/10+1))){ $sdmg1=0; }
		else{ $sdmg1 = $sdmg1 - $item[4] * (2+int($chara[10]/10+1)); }
		if (int($sake1 - ($smem1hit_ritu / 3)) > int(rand(100))) {
			$sdmg1 = 0;
			$kawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]�͐g�����킵���I</FONT>";
		}
	}elsif($staisyo1 == 1 and int(rand(100))<20){
		$sdmg1=0;
		$kawasi4= "<FONT SIZE=4 COLOR=\"$red\">$pename�͐g�����킵���I</FONT>";
	}

	if ($taisyo1 ==0){
		if ($dmg1 < $smem1item[4]*(2+int($smem1[10]/10+1))){ $dmg1=0; }
		else{ $dmg1 = $dmg1 - $smem1item[4] * (2+int($smem1[10]/10+1)); }
		if (int($ssake1 - ($mem1hit_ritu / 3)) > int(rand(100))) {
			$dmg1 = 0;
			$skawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$smem1[4]�͐g�����킵���I</FONT>";
		}
	}elsif($taisyo1 == 1 and int(rand(100))<20){
		$dmg1=0;
		$skawasi3= "<FONT SIZE=4 COLOR=\"$red\">$spename�͐g�����킵���I</FONT>";
	}
	if ($staisyo2 ==0){
		if ($sdmg3 < $item[4]*(2+int($chara[10]/10+1))){ $sdmg3=0; }
		else{ $sdmg3 = $sdmg3 - $item[4] * (2+int($chara[10]/10+1)); }
		if (int(rand(100))<20) {
			$sdmg3 = 0;
			$kawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]�͐g�����킵���I</FONT>";
		}
	}elsif($staisyo2 == 1 and int(rand(100))<20){
		$sdmg3=0;
		$kawasi3= "<FONT SIZE=4 COLOR=\"$red\">$pename�͐g�����킵���I</FONT>";
	}

	if ($taisyo2 ==0){
		if ($dmg4 < $smem1item[4]*(2+int($smem1[10]/10+1))){ $dmg4=0; }
		else{ $dmg4 = $dmg4 - $smem1item[4] * (2+int($smem1[10]/10+1)); }
		if (int(rand(100))<20) {
			$dmg4 = 0;
			$skawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$smem1[4]�͐g�����킵���I</FONT>";
		}
	}elsif($taisyo2 == 1 and int(rand(100))<20){
		$dmg4=0;
		$skawasi4= "<FONT SIZE=4 COLOR=\"$red\">$spename�͐g�����킵���I</FONT>";
	}
}

#------------------#
#�@�퓬��      �@#
#------------------#
sub monsbattle_sts {

	$battle_date[$j] = <<"EOM";
	<TABLE BORDER=0 align="center">
	<TR>
	<TD COLSPAN= "3" ALIGN= "center">
	$i�^�[��
	</TD>
	</TR>
EOM
	if ($i == 1) {
		$battle_date[$j] .= <<"EOM";
		<TD>
EOM
		if($khp_flg>=0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$chara[6]]">
EOM
		}
		if($mem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_pet/$egg_img[$chara[45]]">
EOM
		}
		$battle_date[$j] .= <<"EOM";
		</TD><TD></TD><TD></TD><TD>
EOM
		if($smem1hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$smem1[6]]">
EOM
		}
		if($smem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_pet/$egg_img[$smem1[45]]">
EOM
		}
	}
	$battle_date[$j] .= <<"EOM";
	</TD>
	<TR><TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	�Ȃ܂�	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	�E��	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($khp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$chara[4]		</TD>
		<TD class= "b2">	$khp_flg\/$chara[16]	</TD>
		<TD class= "b2">	$chara_syoku[$chara[14]]</TD>
		<TD class= "b2">	$chara[18]		</TD></TR>
EOM
	}
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	if($mem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$pename			</TD>
		<TD class= "b2">	$mem3hp_flg\/$chara[43]	</TD>
		<TD class= "b2">	�y�b�g			</TD>
		<TD class= "b2">	$chara[46]		</TD></TR>
EOM
	}
	$battle_date[$j] .= <<"EOM";
	</TABLE></TD><TD></TD><TD><FONT SIZE=5 COLOR= "#9999DD">VS</FONT></TD>
	<TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	�Ȃ܂�	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	�E��	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($smem1hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$smem1[4]		</TD>
		<TD class= "b2">	$smem1hp_flg\/$smem1[16]</TD>
		<TD class= "b2">	$chara_syoku[$smem1[14]]</TD>
		<TD class= "b2">	$smem1[18]		</TD></TR>
EOM
	}
	if($smem1[138] eq ""){$spename=$smem1[39];}else{$spename=$smem1[138];}
	if($smem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$spename		</TD>
		<TD class= "b2">	$smem3hp_flg\/$smem1[43]</TD>
		<TD class= "b2">	�y�b�g			</TD>
		<TD class= "b2">	$smem1[46]		</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]�B�̍U���I�I</td></tr>
EOM
	if($taisyo1==0){$mname1=$smem1[4];}
	if($taisyo1==1){$mname1=$spename;}
	if($taisyo2==0){$mname4=$smem1[4];}
	if($taisyo2==1){$mname4=$spename;}
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com1 $clit1 $skawasi1 $mname1 �� <font class= "yellow">$dmg1</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku1</font><br>�@</td></tr>
EOM
	}
	if($mem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com4 $skawasi4 $mname4 �� <font class= "yellow">$dmg4</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku4</font><br>�@</td></tr>
EOM
	}
	if($staisyo1==0){$smname1=$chara[4];}
	if($staisyo1==1){$smname1=$pename;}
	if($staisyo2==0){$smname3=$chara[4];}
	if($staisyo2==1){$smname3=$pename;}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">$smem1[4]�B�̍U���I�I</td></tr>
EOM
	if($smem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom1 $kawasi1 $smname1�� <font class= "yellow">$sdmg1</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku1</font><br>�@</td></tr>
EOM
	}
	if($smem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom3 $kawasi3 $smname3 �� <font class= "yellow">$sdmg3</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku3</font><br>�@</td></tr>
EOM
	}
	$battle_date[$j] .= "</table>";
}

#------------------#
#�퓬���ʔ���      #
#------------------#
sub sentoukeka{
	open(IN,"siro.cgi");
	@siro_data = <IN>;
	close(IN);

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}

	if ($win==1) {
		$sihaisya[0]=$chara[0];
		$sihaisya[1]=$chara[4];

		$new_array = '';
		$new_array = join('<>',@sihaisya);
		$new_array =~ s/\n//;
		$new_array .= "<>\n";
		$sihai_data[0] =$new_array;

		open(OUT,">sihaisya.cgi");
		print OUT @sihai_data;
		close(OUT);

 		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɏ������x�z�҂ɂȂ����I</font></b><br>";

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }

		$eg="$chara[4]�l���V���Ȏx�z�҂ƂȂ�܂����I";

		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	} elsif ($win==3) {
		$comment .= "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
		$chara[143]=$mday;
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }

		$eg="�x�z�҂������$chara[4]�l�ɑł������܂����B";

		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}

	$chara[21] ++;
	$chara[25] --;
	$chara[27] = time();
	$chara[28] = $bossd;
}

#------------------#
# �퓬��̂g�o���� #
#------------------#
sub hp_after{
	$chara[15] = $chara[16];
}

#----------------------#
# �퓬��̃t�b�^�[���� #
#----------------------#
sub mons_footer{
	if ($win==1) {
		print "$comment <br>\n";
	} elsif($win==2){
		print "$comment<br>\n";
	} elsif($win==3){
		print "$comment \n";
	}

	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}
