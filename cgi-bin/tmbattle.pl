#--------------#
#�@�֐��������@#
#--------------#
sub shokika {
	$dmg1 = 0;
	$dmg2 = 0;
	$dmg3 = 0;
	$dmg4 = 0;
	$sdmg1 = $mdmg1 + int(rand($mrand1));
	$sdmg2 = $mdmg2 + int(rand($mrand2));
	$sdmg3 = $mdmg3 + int(rand($mrand3));
	$sdmg4 = $mdmg4 + int(rand($mrand4));
	$clit1 = "";
	$clit2 = "";
	$clit3 = "";
	$clit4 = "";
	$sclit1 = "";
	$sclit2 = "";
	$sclit3 = "";
	$sclit4 = "";
	$mem1hit_ritu=0;
	$mem2hit_ritu=0;
	$mem3hit_ritu=0;
	$mem4hit_ritu=0;
	$smem1hit_ritu=0;
	$smem2hit_ritu=0;
	$smem3hit_ritu=0;
	$smem4hit_ritu=0;
	$sake1 = 0;
	$sake2 = 0;
	$sake3 = 0;
	$sake4 = 0;
	$ssake1 = 0;
	$ssake2 = 0;
	$ssake3 = 0;
	$ssake4 = 0;
	$waza_ritu = 0;
	$awaza_ritu = 0;
	$bwaza_ritu = 0;
	$cwaza_ritu = 0;
	$swaza_ritu = 25;
	$sawaza_ritu = 25;
	$sbwaza_ritu = 25;
	$scwaza_ritu = 25;
	$com1 = "";
	$com2 = "";
	$com3 = "";
	$com4 = "";
	$scom1 = "$ssmname1���P�����������I�I";
	$scom2 = "$ssmname2���P�����������I�I";
	$scom3 = "$ssmname3���P�����������I�I";
	$scom4 = "$ssmname4���P�����������I�I";
	$kawasi1 = "";
	$kawasi2 = "";
	$kawasi3 = "";
	$kawasi4 = "";
	$skawasi1 = "";
	$skawasi2 = "";
	$skawasi3 = "";
	$skawasi4 = "";
	$hpplus1 = 0;
	$hpplus2 = 0;
	$hpplus3 = 0;
	$hpplus4 = 0;
	$shpplus1 = 0;
	$shpplus2 = 0;
	$shpplus3 = 0;
	$shpplus4 = 0;
	$kaihuku1 = "";
	$kaihuku2 = "";
	$kaihuku3 = "";
	$kaihuku4 = "";
	$skaihuku1 = "";
	$skaihuku2 = "";
	$skaihuku3 = "";
	$skaihuku4 = "";
	for($tai=0;$tai<5;$tai++){
		${'taisyo'.$tai} =0;
		${'taisyopt'.$tai} =0;
		${'staisyo'.$tai} =0;
		${'staisyopt'.$tai} =0;
		if($khp_flg<1 and $mem1hp_flg<1){${'taisyopt'.$tai}=1;}
		elsif($mem2hp_flg<1 and $mem3hp_flg<1){${'taisyopt'.$tai}=0;}
		else{${'taisyopt'.$tai}=int(rand(2));}
		if(${'taisyopt'.$tai} == 0){
			if($mem1hp_flg<1){${'taisyo'.$tai} = 0;}
			elsif($khp_flg<1){${'taisyo'.$tai} = 1;}
			else{${'taisyo'.$tai} = int(rand(2));}
		}
		if(${'taisyopt'.$tai} == 1){
			if($mem2hp_flg<1){${'taisyo'.$tai} = 3;}	
			elsif($mem3hp_flg<1){${'taisyo'.$tai} = 2;}
			else{${'taisyo'.$tai} = int(rand(2))+2;}
		}
		if($smem1hp_flg<1 and $smem2hp_flg<0){${'staisyopt'.$tai}=1;}
		elsif($smem3hp_flg<1 and $smem4hp_flg<1){${'staisyopt'.$tai}=0;}
		else{${'staisyopt'.$tai}=int(rand(2));}
		if(${'staisyopt'.$tai} == 0){
			if($smem1hp_flg<1){${'staisyo'.$tai} = 1;}
			elsif($smem2hp_flg<1){${'staisyo'.$tai} = 0;}
			else{${'staisyo'.$tai} = int(rand(2));}
		}
		if(${'staisyopt'.$tai} == 1){
			if($smem3hp_flg<1){${'staisyo'.$tai} = 3;}	
			elsif($smem4hp_flg<1){${'staisyo'.$tai} = 2;}
			else{${'staisyo'.$tai} = int(rand(2))+2;}
		}
	}
}

#------------#
#�@HP�̌v�Z�@#
#------------#
sub hp_sum {
	if($khp_flg<1){$dmg1 = 0;}
	if($mem1hp_flg<1){$dmg2 = 0;}
	if($mem2hp_flg<1){$dmg3 = 0;}
	if($mem3hp_flg<1){$dmg4 = 0;}

	if($smem1hp_flg<1){$sdmg1 = 0;}
	if($smem2hp_flg<1){$sdmg2 = 0;}
	if($smem3hp_flg<1){$sdmg3 = 0;}
	if($smem3hp_flg<1){$sdmg4 = 0;}

	if($khp_flg > 0){$khp_flg += $hpplus1;}
	if($mem1hp_flg > 0){$mem1hp_flg += $hpplus2;}
	if($mem2hp_flg > 0){$mem2hp_flg += $hpplus3;}
	if($mem3hp_flg > 0){$mem3hp_flg += $hpplus4;}

	if($mem1hp_flg > 0){$smem1hp_flg += $shpplus1;}
	if($mem2hp_flg > 0){$smem2hp_flg += $shpplus2;}
	if($mem3hp_flg > 0){$smem3hp_flg += $shpplus3;}
	if($mem4hp_flg > 0){$smem4hp_flg += $shpplus4;}

	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0){
			$khp_flg = $khp_flg - ${'sdmg'.$tai};
		}
		elsif(${'taisyo'.$tai} ==1) {
			$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
		}
		elsif(${'taisyo'.$tai} ==2){
			$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
		}
		elsif(${'taisyo'.$tai} ==3){
			$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
		}
		elsif(${'taisyo'.$tai} ==4){
			$khp_flg = $khp_flg - ${'sdmg'.$tai};
			$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
			$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
			$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
		}

		if (${'staisyo'.$tai}==0){
			$smem1hp_flg = $smem1hp_flg - ${'dmg'.$tai};
		}
		elsif(${'staisyo'.$tai}==1) {
			$smem2hp_flg = $smem2hp_flg - ${'dmg'.$tai};
		}
		elsif(${'staisyo'.$tai}==2){
			$smem3hp_flg = $smem3hp_flg - ${'dmg'.$tai};
		}
		elsif(${'staisyo'.$tai}==3){
			$smem4hp_flg = $smem4hp_flg - ${'dmg'.$tai};
		}
		elsif(${'staisyo'.$tai}==4){
			$smem1hp_flg = $smem1hp_flg - ${'dmg'.$tai};
			$smem2hp_flg = $smem2hp_flg - ${'dmg'.$tai};
			$smem3hp_flg = $smem3hp_flg - ${'dmg'.$tai};
			$smem4hp_flg = $smem4hp_flg - ${'dmg'.$tai};
		}
	}

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mem1hp_flg > $mem1[16]){
		$mem1hp_flg = $mem1[16];
	}
	if ($mem2hp_flg > $mem2[16]) {
		$mem2hp_flg = $mem2[16];
	}
	if ($mem3hp_flg > $mem3[16]) {
		$mem3hp_flg = $mem3[16];
	}
	if ($smem1hp_flg > $smem1hp){
		$smem1hp_flg = $smem1hp;
	}
	if ($smem2hp_flg > $smem2hp){
		$smem2hp_flg = $smem2hp;
	}
	if ($smem3hp_flg > $smem3hp){
		$smem3hp_flg = $smem3hp;
	}
	if ($smem4hp_flg > $chara[43]){
		$smem4hp_flg = $chara[43];
	}
}

#------------#
#�@���s�����@#
#------------#
sub winlose {

	if ($smem1hp_flg<=0 and $smem2hp_flg<=0 and $smem3hp_flg<=0 and $smem4hp_flg<=0){ 
		$win = 1; last; #����
	}
	elsif ($khp_flg<1 and $chara[38]>3000 and $chara[38]<3100 and $php_flg<1 and $mem1hp_flg<1 and $mem2hp_flg<1 and $mem3hp_flg<1) {
		$win = 3; last; #����
	}
	elsif ($khp_flg<1 and $mem1hp_flg<1 and $mem2hp_flg<1 and $mem3hp_flg<1) {
		$win = 4; last; #����
	}
	else{ $win = 2; } #��������
}
#------------------#
#�����N���B�e�B�J��#
#------------------#
sub mons_clt{
	if ($swaza_ritu > int(rand(200))) {
		$scom1 .= "<font color=\"$red\">�N���e�B�J���I�I</font><br>";
		$sdmg1 = $sdmg1 * 2;
	}
	if ($sawaza_ritu > int(rand(200))) {
		$scom2 .= "<font color=\"$red\">�N���e�B�J���I�I</font><br>";
		$sdmg2 = $sdmg2 * 2;
	}
	if ($sbwaza_ritu > int(rand(200))) {
		$scom3 .= "<font color=\"$red\">�N���e�B�J���I�I</font><br>";
		$sdmg3 = $sdmg3 * 2;
	}
	if ($scwaza_ritu > int(rand(200))) {
		$scom4 .= "<font color=\"$red\">�N���e�B�J���I�I</font><br>";
		$sdmg4 = $sdmg4 * 2;
	}
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
	$mem2ci_plus = $mem2item[2] + $mem2item[16];
	$mem2cd_plus = $mem2item[5] + $mem2item[17];
	$mem3ci_plus = $mem3item[2] + $mem3item[16];
	$mem3cd_plus = $mem3item[5] + $mem3item[17];

	$smem1ci_plus = $smem1item[2] + $smem1item[16];
	$smem1cd_plus = $smem1item[5] + $smem1item[17];
	$smem2ci_plus = $smem2item[2] + $smem2item[16];
	$smem2cd_plus = $smem2item[5] + $smem2item[17];
	$smem3ci_plus = $smem3item[2] + $smem3item[16];
	$smem3cd_plus = $smem3item[5] + $smem3item[17];
	$smem4ci_plus = $smem4item[2] + $smem4item[16];
	$smem4cd_plus = $smem4item[5] + $smem4item[17];

	# ������
	$mem1hit_ritu += int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $ci_plus;
	$mem2hit_ritu += int($mem1[9] / 3 + $mem1[11] / 10 + $mem1item[10] / 3)+ 40 + $mem1ci_plus;
	$mem3hit_ritu += int($mem2[9] / 3 + $mem2[11] / 10 + $mem2item[10] / 3)+ 40 + $mem2ci_plus;
	$mem4hit_ritu += int($mem3[9] / 3 + $mem3[11] / 10 + $mem3item[10] / 3)+ 40 + $mem3ci_plus;

	$smem1hit_ritu += int($smem1[9] / 3 + $smem1[11] / 10 + $smem1item[10] / 3)+ 40 + $smem1ci_plus;
	$smem2hit_ritu += int($smem2[9] / 3 + $smem2[11] / 10 + $smem2item[10] / 3)+ 40 + $smem2ci_plus;
	$smem3hit_ritu += int($smem3[9] / 3 + $smem3[11] / 10 + $smem3item[10] / 3)+ 40 + $smem3ci_plus;
	$smem4hit_ritu += int($smem4[9] / 3 + $smem4[11] / 10 + $smem4item[10] / 3)+ 40 + $smem4ci_plus;

	if ($chara[55]==25 or $chara[56]==25 or $chara[57]==25 or $chara[58]==25){$yamato1=10;}
	if ($mem1[55]==25 or $mem1[56]==25 or $mem1[57]==25 or $mem1[58]==25){$yamato2=10;}
	if ($mem2[55]==25 or $mem2[56]==25 or $mem2[57]==25 or $mem2[58]==25){$yamato3=10;}
	if ($mem3[55]==25 or $mem3[56]==25 or $mem3[57]==25 or $mem3[58]==25){$yamato4=10;}
	if ($smem1[55]==25 or $smem1[56]==25 or $smem1[57]==25 or $smem1[58]==25){$syamato1=10;}
	if ($smem2[55]==25 or $smem2[56]==25 or $smem2[57]==25 or $smem2[58]==25){$syamato2=10;}
	if ($smem3[55]==25 or $smem3[56]==25 or $smem3[57]==25 or $smem3[58]==25){$syamato3=10;}
	if ($smem4[55]==25 or $smem4[56]==25 or $smem4[57]==25 or $smem4[58]==25){$syamato4=10;}

	# ���
	$sake1	+= int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $cd_plus - $syamato1;
	$sake2	+= int($mem1[9] / 10 + $mem1[11] / 20 + $mem1item[10]/10) + $mem1cd_plus - $syamato2;
	$sake3	+= int($mem2[9] / 10 + $mem2[11] / 20 + $mem2item[10]/10) + $mem2cd_plus - $syamato3;
	$sake4	+= int($mem3[9] / 10 + $mem3[11] / 20 + $mem3item[10]/10) + $mem3cd_plus - $syamato4;
	$ssake1	+= int($smem1[9] / 10 + $smem1[11] / 20 + $smem1item[10]/10) + $smem1cd_plus - $yamato1;
	$ssake2	+= int($smem2[9] / 10 + $smem2[11] / 20 + $smem2item[10]/10) + $smem2cd_plus - $yamato2;
	$ssake3	+= int($smem3[9] / 10 + $smem3[11] / 20 + $smem3item[10]/10) + $smem3cd_plus - $yamato3;
	$ssake4	+= int($smem4[9] / 10 + $smem4[11] / 20 + $smem4item[10]/10) + $smem4cd_plus - $yamato4;

	if ($sake1 > 90){$sake1 = 90;}
	if ($sake2 > 90){$sake2 = 90;}
	if ($sake3 > 90){$sake3 = 90;}
	if ($sake4 > 90){$sake4 = 90;}
	if ($ssake1 > 90){$ssake1 = 90;}
	if ($ssake2 > 90){$ssake2 = 90;}
	if ($ssake3 > 90){$ssake3 = 90;}
	if ($ssake4 > 90){$ssake4 = 90;}

	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $item[4]*(2+int($chara[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{ ${'sdmg'.$tai} = ${'sdmg'.$tai} - $item[4] * (2+int($chara[10]/10+1)); }
			if (int($sake1 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==1 or ${'taisyo'.$tai} ==4) {
			if (${'sdmg'.$tai} < $mem1item[4]*(2+int($mem1[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem1item[4] * (2+int($mem1[10]/10+1)); }
			if (int($sake2 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem1[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==2 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $mem2item[4]*(2+int($mem2[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem2item[4] * (2+int($mem2[10]/10+1)); }
			if (int($sake3 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem2[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==3 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $mem3item[4]*(2+int($mem3[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem3item[4] * (2+int($mem3[10]/10+1)); }
			if (int($sake4 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem3[4]�͐g�����킵���I</FONT>";
			}
		}

		if (${'staisyo'.$tai}==0 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem1item[4]*(2+int($smem1[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem1item[4] * (2+int($smem1[10]/10+1)); }
			if (int($ssake1 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem1[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'staisyo'.$tai}==1 or ${'staisyo'.$tai}==4) {
			if (${'dmg'.$tai} < $smem2item[4]*(2+int($smem2[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem2item[4] * (2+int($smem2[10]/10+1)); }
			if (int($ssake2 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem2[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'staisyo'.$tai}==2 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem3item[4]*(2+int($smem3[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem3item[4] * (2+int($smem1[10]/10+1)); }
			if (int($ssake3 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem3[4]�͐g�����킵���I</FONT>";
			}
		}
		if(${'staisyo'.$tai}==3 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem4item[4]*(2+int($smem4[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem4item[4] * (2+int($smem4[10]/10+1)); }
			if (int($ssake4 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem4[4]�͐g�����킵���I</FONT>";
			}
		}
	}

	if($chara[55]==34 or $chara[56]==34 or $chara[57]==34 or $chara[58]==34){$sdmg1=int($sdmg1*3/4);}
	if($mem1[55]==34 or $mem1[56]==34 or $mem1[57]==34 or $mem1[58]==34){$sdmg2=int($sdmg2*3/4);}
	if($mem2[55]==34 or $mem2[56]==34 or $mem2[57]==34 or $mem2[58]==34){$sdmg3=int($sdmg3*3/4);}
	if($mem3[55]==34 or $mem3[56]==34 or $mem3[57]==34 or $mem3[58]==34){$sdmg4=int($sdmg4*3/4);}

	if($smem1[55]==34 or $smem1[56]==34 or $smem1[57]==34 or $smem1[58]==34){$dmg1=int($dmg1*3/4);}
	if($smem2[55]==34 or $smem2[56]==34 or $smem2[57]==34 or $smem2[58]==34){$dmg2=int($dmg2*3/4);}
	if($smem3[55]==34 or $smem3[56]==34 or $smem3[57]==34 or $smem3[58]==34){$dmg3=int($dmg3*3/4);}
	if($smem4[55]==34 or $smem4[56]==34 or $smem4[57]==34 or $smem4[58]==34){$dmg4=int($dmg4*3/4);}
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
		if($mem1hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem1[6]]">
EOM
		}
		if($mem2hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem2[6]]">
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
			<IMG SRC="$img_path_t/$chara_img_t[$mimg1]">
EOM
		}
		if($smem2hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg2]">
EOM
		}
		if($smem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg3]">
EOM
		}
		if($smem4hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg4]">
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
	if($mem1hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$mem1[4]		</TD>
		<TD class= "b2">	$mem1hp_flg\/$mem1[16]	</TD>
		<TD class= "b2">	$chara_syoku[$mem1[14]]	</TD>
		<TD class= "b2">	$mem1[18]		</TD></TR>
EOM
	}
	if($mem2hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$mem2[4]		</TD>
		<TD class= "b2">	$mem2hp_flg\/$mem2[16]	</TD>
		<TD class= "b2">	$chara_syoku[$mem2[14]]	</TD>
		<TD class= "b2">	$mem2[18]		</TD></TR>
EOM
	}
	if($mem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$chara[39]		</TD>
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
		<TR><TD class= "b2">	$ssmname1		</TD>
		<TD class= "b2">	$smem1hp_flg\/$smem1hp	</TD>
		<TD class= "b2">	�����X�^�[		</TD>
		<TD class= "b2">	$mlv1			</TD></TR>
EOM
	}
	if($smem2hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$ssmname2		</TD>
		<TD class= "b2">	$smem2hp_flg\/$smem2hp	</TD>
		<TD class= "b2">	�����X�^�[		</TD>
		<TD class= "b2">	$mlv2			</TD></TR>
EOM
	}
	if($smem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$ssmname3		</TD>
		<TD class= "b2">	$smem3hp_flg\/$smem3hp	</TD>
		<TD class= "b2">	�����X�^�[		</TD>
		<TD class= "b2">	$mlv3			</TD></TR>
EOM
	}
	if($smem4hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$ssmname4		</TD>
		<TD class= "b2">	$smem4hp_flg\/$smem4hp	</TD>
		<TD class= "b2">	�����X�^�[		</TD>
		<TD class= "b2">	$mlv4			</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]�B�̍U���I�I</td></tr>
EOM
	for($tai=0;$tai<5;$tai++){
		if(${'staisyo'.$tai}==0){${'mname'.$tai}=$ssmname1;}
		if(${'staisyo'.$tai}==1){${'mname'.$tai}=$ssmname2;}
		if(${'staisyo'.$tai}==2){${'mname'.$tai}=$ssmname3;}
		if(${'staisyo'.$tai}==3){${'mname'.$tai}=$ssmname4;}
		if(${'staisyo'.$tai}==4){${'mname'.$tai}="�G�S��";}
	}
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com1 $clit1 $skawasi1 $mname1 �� <font class= "yellow">$dmg1</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku1</font><br>�@</td></tr>
EOM
	}
	if($mem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com2 $skawasi2 $mname2 �� <font class= "yellow">$dmg2</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku2</font><br>�@</td></tr>
EOM
	}
	if($mem2hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com3 $skawasi3 $mname3 �� <font class= "yellow">$dmg3</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku3</font><br>�@</td></tr>
EOM
	}
	if($mem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com4 $skawasi4 $mname4 �� <font class= "yellow">$dmg4</font> �̃_���[�W��^�����B<font class= "yellow">$kaihuku4</font><br>�@</td></tr>
EOM
	}
	for($tai=0;$tai<5;$tai++){
		if(${'taisyo'.$tai}==0){${'smname'.$tai}=$chara[4];}
		if(${'taisyo'.$tai}==1){${'smname'.$tai}=$mem1[4];}
		if(${'taisyo'.$tai}==2){${'smname'.$tai}=$mem2[4];}
		if(${'taisyo'.$tai}==3){${'smname'.$tai}=$mem3[4];}
		if(${'taisyo'.$tai}==4){${'smname'.$tai}="�G�S��";}
	}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">$smem1[4]�B�̍U���I�I</td></tr>
EOM
	if($smem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom1 $kawasi1 $smname1�� <font class= "yellow">$sdmg1</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku1</font><br>�@</td></tr>
EOM
	}
	if($smem2hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom2 $kawasi2 $smname2�� <font class= "yellow">$sdmg2</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku2</font><br>�@</td></tr>
EOM
	}
	if($smem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom3 $kawasi3 $smname3 �� <font class= "yellow">$sdmg3</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku3</font><br>�@</td></tr>
EOM
	}
	if($smem4hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom4 $kawasi4 $smname4�� <font class= "yellow">$sdmg4</font> �̃_���[�W��^�����B<font class= "yellow">$skaihuku4</font><br>�@</td></tr>
EOM
	}
	$battle_date[$j] .= "</table>";
}
#------------------#
#�퓬���ʔ���      #
#------------------#
sub sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + int(rand($mgold*$chara[20])+1);
		if($chara[24]==1080){$gold=$gold*2;}
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
 		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I</font></b><br>";
		& item_u;
		& item_regist;
	} elsif ($win==2) {
		$mex = int($mex/2);
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$mex = 1;
		$chara[19] = int(($chara[19] / 2));
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
	if($win==3){
		$comment .= "<b><font size=4 color=red>�������Ă��܂����I</font></b><br>";
		$chara[19] = int(($chara[19] / 2));
		&egg_lose;
	}
		if($chara[33]==100){$mex= int($mex * 1.5);}
		if($khp_flg<=0){$mex= int($mex/2);}
		if($chara[0] eq "jupiter"){$mex= $mex * 10;}
		if($chara[0] eq "ikuei6"){$mex= $mex * 10;}
		if($chara[0] eq "jack"){$mex= $mex * 10;}
		if($chara[0] eq "aaaa"){$mex= $mex * 10;}
		if($chara[24]==1078){$mex = $mex * 2;}
		$chara[17] = $chara[17] + $mex;

		if($in{'mode'} eq "guild_battle"){
			open(IN,"allguild.cgi");
			@member_data = <IN>;
			close(IN);
			$i=0;$hit=0;
			foreach(@member_data){
				@array = split(/<>/);
				if($array[0] eq $chara[66]){
					$gg_maxmem=$array[4] * 4;
					$array[2] += $mex;
					$new_array = '';
					$new_array = join('<>',@array);
					$member_data[$i]=$new_array;
					open(OUT,">allguild.cgi");
					print OUT @member_data;
					close(OUT);
					last;
				}
				$i++;
			}
		}

		$imex = $mex*int(rand(10)+1);
		if($win!=3 and $win and $chara[38]>3000 and $in{'mode'} ne "guild_battle"){
			if($chara[24]==1076 and $chara[38]<3100)
				{$chara[40] = $chara[40] + $imex;}
			else{$chara[40] = $chara[40] + $mex;}
		}
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
		$chara[28] = $bossd;

	#�A�C�e���h���b�v
	if($win==1){
		if($chara[70]!=1){$pp=($place/2) + 1;}
		else{$pp=($place/2) + 10;}
		if($on and $on==$place and $name eq "�G�b�O�G���W�F��"){
			if($chara[91] == 1){$item_no = 16;$chara[91]=2;&itemdrop;}
			elsif(int(rand($sdrop)) == 0){$item_no = 16;&itemdrop;}
		}
		elsif($on and $on==$place and int(rand($sdrop)) == 0){$item_no = int(rand(15));&itemdrop;}
		elsif(int(rand($adrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+11);&itemdrop;}
		elsif(int(rand($bdrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+6);&itemdrop;}
		elsif(int(rand($cdrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+1);&itemdrop;}
		if($mname eq "�G�b�O" and int(rand(15))==0 and $chara[18]>60){
			if($chara[38]<3001){&egg_egg;}
		}
		if($chara[70]!=1 and int(rand($turu_drop / $turu_plus))==0){
			$comment.= "<b><font size=4 color=yellow>��͂����E�����I�I</font></b><br>";
			$chara[100]++;
		}
		if($chara[70]==1 and int(rand($turu_drop2 / $turu_plus))==0){
			$comment.= "<b><font size=4 color=yellow>��͂����E�����I�I</font></b><br>";
			$chara[100]++;
		}
		elsif($chara[70]!=1 and int(rand($ougon_drop / $turu_plus))==0){
			$comment.= "<b><font size=5 color=red>�����̂�͂������I�I</font></b><br>";
			$chara[97]++;
		}
		if($i_name){$comment .= "<b><font size=5 color=red>$i_name���E�����I�I</font></b><br>";}

		&quest;
	}
	
}

#------------------#
#�퓬���ʔ���      #
#------------------#
sub legend_sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold +int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
		$chara[28] -= 1;
		if ($chara[28] == 0) {
			$comment = "<b><font color=yellow size=5>$chara[4]�́A���W�F���h�v���C�X���U�������I�I�V�����̍����^�����܂��I�I</font></b><br>";

			$lock_file = "$lockfolder/messa$in{'id'}.lock";
			&lock($lock_file,'MS');
			open(IN,"$chat_file");
			@chat_mes = <IN>;
			close(IN);
			$mes_sum = @chat_mes;
	if($in{'boss_file'}==0){$rp="���킳�̂ق���";}
	if($in{'boss_file'}==1){$rp="�Â̐_�a";}
	if($in{'boss_file'}==2){$rp="�E�҂̓��A";}
	if($in{'boss_file'}==3){$rp="�K�C�A�t�H�[�X";}
			$chmes="$chara[4]�l���V����$rp���U������A�̍����オ��܂����I";
			if($mes_sum > $mes_max) { pop(@chat_mes); }
			unshift(@chat_mes,"<><font color=\"yellow\">���m</font><>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$chmes</font><>$host<><>\n");

			open(OUT,">$chat_file");
			print OUT @chat_mes;
			close(OUT);

			&unlock($lock_file,'MS');

			if ($chara[32] < $in{'boss_file'} + 1) {
				$chara[32] = $in{'boss_file'} + 1;
			}
		} else {
			$comment = "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I�܂��܂���ɒ��킷�邼���I</font></b><br>";
		}
	} elsif ($win==2) {
		$mex = int($mex/2);
		$chara[28] = $bossd;
		$comment = "<b><font size=5>$chara[4]�́A�����o�����E�E�E��</font></b><br>";
	} else {
		$mex = 1;
		$chara[28] = $bossd;
		$chara[19] = int(($chara[19] / 2));
		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";
	}
	if($win==3){
		$comment .= "<b><font size=4 color=red>�������Ă��܂����I</font></b><br>";
		$chara[19] = int(($chara[19] / 2));
		&egg_lose;
	}
		if($chara[33]==100){$mex= $mex * 1.5;}
		if($khp_flg<=0){$mex= int($mex/2);}
		$chara[17] = $chara[17] + $mex;
		$imex = $mex*int(rand(10)+1);
		if($win!=3 and $win and $chara[38]>3000){
			if($chara[24]==1076 and $chara[38]<3100)
				{$chara[40] = $chara[40] + $imex;}
			else{$chara[40] = $chara[40] + $mex;}
		}
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
		if($win==1){&quest;}
}

#------------------#
#�A�C�e���h���b�v  #
#------------------#
sub itemdrop{
	if($qh==2){
		open(IN,"questitem2.cgi");
		@item_array = <IN>;
		close(IN);
	}
	elsif($q_item and $q_name eq $mname){
		open(IN,"questitem.cgi");
		@item_array = <IN>;
		close(IN);
	}
	elsif($on and $on==$place){
		open(IN,"$drop11_file");
		@item_array = <IN>;
		close(IN);
	}
	else{
		if($place==20){$drop_file="drop1_file";}
		elsif($place>=30){$drop_file="drop1_file";}
		else{$drop_file="drop$place\_file";}
		open(IN,"$$drop_file");
		@item_array = <IN>;
		close(IN);
	}
	$hit=0;
	foreach(@item_array){			($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
		if($item_no eq "$ino") { $hit=1;last; }
	}
	if(!$hit) { &error("$drop_file @item_array $mname ����ȃA�C�e���͑��݂��܂��� $q_name $item_no"); }

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
	if($i_no < 1000){
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}
	elsif($i_no < 2000 and $i_no > 1000){
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$i_hissatu<>$i_tokusyu<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}	
	elsif($i_no < 3000 and $i_no > 2000){
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}
	elsif($i_no > 7000 and $i_no<8000){
		$i_no=$i_no-7000;
		$chara[$i_no]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $i_no){last;}
		}
		$i_name=$sname3;
	}
	else{&error("�A�C�e����������܂���I$back_form");}

	&unlock($lock_file,'SI');
}

#------------------#
#�C���F���g	   #
#------------------#
sub ivent{

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	push(@log_item,"3002<>�X�^�[�g�G�b�O<>0<>3000<>30000<>0<>1<>1<>0<>\n");

	open(OUT,">pets/$chara[0].cgi");
	print OUT @log_item;
	close(OUT);

	&unlock($lock_file,'SI');
}

#------------------#
#     �N�G�X�g     #
#------------------#
sub quest{
	open(IN,"inquest.cgi");
	@quest_item = <IN>;
	close(IN);
	for($i=101;$i<130;$i++){
		if($chara[$i]==1){
			$hit=0;
			foreach(@quest_item){											($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
				if($i == $q_no and $q_name eq $ssmname1) {$hit=1;last;}
				elsif($i == $q_no and $q_name eq $ssmname2) {$hit=2;last;}
				elsif($i == $q_no and $q_name eq $ssmname3) {$hit=3;last;}
				elsif($i == $q_no and $q_name eq $ssmname4) {$hit=4;last;}
			}
			if($hit){
				$comment .= "<b><font size=4 color=red>";
				$comment .= "�u$q_name�v��|�������N�G�X�g���N���A�����I<br>";
				if($q_gold){
					$chara[19] += $q_gold;
					$comment .= "��V$q_gold G����肵���I�I<br>";
				}
				if($q_exp){
					$chara[17] += $q_exp;
					$comment .= "��V$q_exp�o���l����肵���I�I<br>";
				}
				if($q_item){
					$item_no=$q_no;&itemdrop;
					$comment .= "��V$i_name����肵���I�I<br>";
					$i_name="";
				}
				if($i==127){
					$lock_file = "$lockfolder/messa$in{'id'}.lock";
					&lock($lock_file,'MS');

					open(IN,"$chat_file");
					@chat_mes = <IN>;
					close(IN);

					$mes_sum = @chat_mes;

					if($mes_sum > $mes_max) { pop(@chat_mes); }

					$eg="$chara[4]�l�������N�G�X�g���e�ŏI�W�I�𓢔����܂���";
	
					unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

					open(OUT,">$chat_file");
					print OUT @chat_mes;
					close(OUT);

					&unlock($lock_file,'MS');
				}

				$comment .= "</font></b>";
				$chara[$i] = 2;
			}
		}
	}
	open(IN,"inquest2.cgi");
	@quest2_item = <IN>;
	close(IN);
	for($i=151;$i<180;$i++){
		if($chara[$i]==1){
			$hit=0;
			foreach(@quest2_item){											($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
				if($i == $q_no and $q_name eq $ssmname1) {$hit=1;last;}
				elsif($i == $q_no and $q_name eq $ssmname2) {$hit=2;last;}
				elsif($i == $q_no and $q_name eq $ssmname3) {$hit=3;last;}
				elsif($i == $q_no and $q_name eq $ssmname4) {$hit=4;last;}
			}
			if($hit){
				$comment .= "<b><font size=4 color=red>";
				$comment .= "�u$q_name�v��|�������N�G�X�g���N���A�����I<br>";
				if($q_gold){
					$chara[19] += $q_gold;
					$comment .= "��V$q_gold G����肵���I�I<br>";
				}
				if($q_exp){
					$chara[17] += $q_exp;
					$comment .= "��V$q_exp�o���l����肵���I�I<br>";
				}
				if($q_item){
					$qh=2;$item_no=$q_no;&itemdrop;
					$comment .= "��V$i_name����肵���I�I<br>";
					$i_name="";
				}
				if($i==178){
					$lock_file = "$lockfolder/messa$in{'id'}.lock";
					&lock($lock_file,'MS');

					open(IN,"$chat_file");
					@chat_mes = <IN>;
					close(IN);

					$mes_sum = @chat_mes;

					if($mes_sum > $mes_max) { pop(@chat_mes); }

					$eg="$chara[4]�l�������N�G�X�g���e�ŏI�W�I�𓢔����܂���";

					unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

					open(OUT,">$chat_file");
					print OUT @chat_mes;
					close(OUT);

					&unlock($lock_file,'MS');
				}

				$comment .= "</font></b>";
				$chara[$i] = 2;
			}
		}
	}
}

#--------------#
# ���ԃ`�F�b�N #
#--------------#
sub time_check{
	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $m_time - $ltime;

	if ($vtime > 0) {
		&error("����$vtime�b�ԓ����܂���B");
	}
}

#----------------------#
# �����X�f�[�^�Ăяo�� #
#----------------------#
sub mons_read{
	$mex=0;$mgold=0;
	if($on and $on==$place){
		foreach(@MONSTER){
($keikatime,$basyo,$mname,$mzoku,$mlv,$mex,$mrand,$msp,$maxhp,$mdmg,$mkahi,$monstac,$mons_ritu,$mgold,$mimg) = split(/<>/);
		if ($mname eq $name) {last;}
		}
	}else{
		for($mon=1;$mon<$kazu;$mon++){
			$s_no = int(rand($r_no));
(${'ssmname'.$mon},${'mzoku'.$mon},${'mlv'.$mon},${'mex'.$mon},${'mrand'.$mon},${'msp'.$mon},${'mdmg'.$mon},${'mkahi'.$mon},${'monstac'.$mon},${'mons_ritu'.$mon},${'mgold'.$mon},${'mimg'.$mon}) = split(/<>/,$MONSTER[$s_no]);
			$mex += int(${'mex'.$mon} * $exp_plus);
			$mgold += ${'mgold'.$mon};
			if (${'monstac'.$mon}) {
				require "./mons/${'monstac'.$mon}.pl";
			} else {
				require "./mons/0.pl";
			}
		}
	}
}
#------------------#
# �퓬��̂g�o���� #
#------------------#
sub hp_after{
	$chara[15] = $khp_flg;
	$chara[42] = $mem3hp_flg;
	if ($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	if ($chara[15] <= 0) { $chara[15] = 1; }
	if ($chara[38]>3000 and $chara[42] > $chara[43]) { $chara[42] = $chara[43]; }
	if ($chara[38]>3000 and $chara[42] <= 0) { $chara[42] = 1; }
	if ($win!=1 and $on ==$place){
		open(IN,"$boss_monster");
		@boss_data = <IN>;
		close(IN);
		$i=0;
		foreach(@boss_data){
($keikatime,$basyo,$mname,$mzoku,$mlv,$mmex,$mrand,$msp,$maxhp,$mdmg,$mkahi,$monstac,$mons_ritu,$mgold,$mimg) = split(/<>/);
			if ($mname eq $name){
			$boss_data[$i]="$keikatime<>$basyo<>$mname<>$mzoku<>$mlv<>$mmex<>$mrand<>$mhp<>$maxhp<>$mdmg<>$mkahi<>$monstac<>$mons_ritu<>$mgold<>$mimg<>";
			open(OUT,">$boss_monster");
			print OUT @boss_data;
			close(OUT);
			last;
			}
		$i++;
		}
	}
	elsif($win==1 and $on and $on ==$place){
		$hit=0;
		foreach(@bosson_data){
			($name,$on) = split(/<>/);
			if($on and $on==$place){$hit=1;last;}
		}
		if(!$hit){&error("�ɂ�[�B�ɂ�[�B");}
		open(IN,"$boss_monster");
		@boss_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@boss_data){
($keikatime,$basyo,$mname,$mzoku,$mlv,$mmex,$mrand,$msp,$maxhp,$mdmg,$mkahi,$monstac,$mons_ritu,$mgold,$mimg) = split(/<>/);
			if ($mname eq $name){
				$boss_data[$i]="$keikatime<>$basyo<>$mname<>$mzoku<>$mlv<>$mmex<>$mrand<>$maxhp<>$maxhp<>$mdmg<>$mkahi<>$monstac<>$mons_ritu<>$mgold<>$mimg<>";
				open(OUT,">$boss_monster");
				print OUT @boss_data;
				close(OUT);
				$hit=1;
				last;
			}
		$i++;
		}
		if(!$hit){&error("�G���[�ł񂪂ȁB");}
		open(IN,"./data/bosson.ini");
		@bosson_data = <IN>;
		close(IN);
		$g=0;
		foreach(@bosson_data){
			($name,$on) = split(/<>/);
			if($on and $name eq $mname){
				$bosson_data[$g]="$name<>0<>";
				open(OUT,">./data/bosson.ini");
				print OUT @bosson_data;
				close(OUT);
				last;
			}
		$g++;
		}
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;
	$year = $year +1900;

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$bosss="$chara[4]�l���{�X�u$name�v�𓢔����܂���";
	
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<>$bosss<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');
	}
}

#----------------------#
# �퓬��̃t�b�^�[���� #
#----------------------#
sub mons_footer{
	if ($win==1 and $chara[38]>3000) {
		if($chara[24]==1076 and $chara[38]<3100){
			print "$comment $imex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
		}else{
			print "$comment $mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
		}
	} elsif($win==3){
		print "$comment $mex�̌o���l����ɓ��ꂽ�B�����������ɂȂ����E�E�E�B(��)<br>\n";
	} elsif($win==1){
		print "$comment $mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n";
	} elsif($win==2){
		print "$comment $mex�̌o���l����ɓ��ꂽ�B<br>\n";
	} else {
		print "$comment $mex�̌o���l����ɓ��ꂽ�B�����������ɂȂ����E�E�E(��)<br>\n";
	}
	if($chara[36]==1){
		if(!$lvup or $chara[38]>3000){
			if($chara[19]>=int($yado_dai*$chara[18])){
				$chara[15] = $chara[16];
				$chara[42] = $chara[43];
				$chara[19] -=int($yado_dai*$chara[18]);
				print "<b><font size=2>$chara[4]�́A�h���ɍs�����B</font></b><br>";
	}else{
	print "<b><font size=2>$chara[4]�́A�h���ɍs�����Ƃ���������������Ȃ������B</font></b><br>";
	}
	}
	}
	&chara_regist;

	if($in{'mode'} eq "monster"){
	print <<"EOM";
<form action= "tmonster.cgi" method= "POST">
<input type= "hidden" name= "mode" value= "monster">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$new_chara">
<input type="hidden" name="tmons_file" value="$in{'tmons_file'}">
<input type= "submit" class= "btn" value= "����ɓ���">
</form>
EOM
}
	if($in{'mode'} eq "guild_battle"){
	print <<"EOM";
<form action= "guild_battle.cgi" method= "POST">
<input type= "hidden" name= "mode" value= "guild_battle">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$new_chara">
<input type="hidden" name="guild_file" value="$in{'guild_file'}">
<input type= "submit" class= "btn" value= "����ɓ���">
</form>
EOM
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
1;