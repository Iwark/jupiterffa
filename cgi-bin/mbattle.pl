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
	$mem1hit_ritu = int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16];
	$mem2hit_ritu = int($mem1[9] / 3 + $mem1[11] / 10 + $mem1item[10] / 3)+ 40 + $mem1item[2] + $mem1item[16];
	$mem3hit_ritu = int($mem2[9] / 3 + $mem2[11] / 10 + $mem2item[10] / 3)+ 40 + $mem2item[2] + $mem2item[16];
	$mem4hit_ritu=50;
	$smem1hit_ritu=100;
	$smem2hit_ritu=100;
	$smem3hit_ritu=100;
	$smem4hit_ritu=100;
	$sake1	= int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17];
	$sake2	= int($mem1[9] / 10 + $mem1[11] / 20 + $mem1item[10]/10) + $mem1item[5] + $mem1item[17];
	$sake3	= int($mem2[9] / 10 + $mem2[11] / 20 + $mem2item[10]/10) + $mem2item[5] + $mem2item[17];
	$sake4 = 10;
	$ssake1 = $mkahi1;
	$ssake2 = $mkahi2;
	$ssake3 = $mkahi3;
	$ssake4 = $mkahi4;
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
	$sinda=0;
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
		if($smem1hp_flg<1 and $smem2hp_flg<1){${'staisyopt'.$tai}=1;}
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

	if ($chara[55]==42 or $chara[56]==42 or $chara[57]==42 or $chara[58]==42){$ande1=1;}
	if ($mem1[55]==42 or $mem1[56]==42 or $mem1[57]==42 or $mem1[58]==42){$ande2=1;}
	if ($mem2[55]==42 or $mem2[56]==42 or $mem2[57]==42 or $mem2[58]==42){$ande3=1;}
	if ($ande1==1 and $khp_flg<1){$andea1+=1;}
	if ($ande2==1 and $mem1hp_flg<1){$andea2+=1;}
	if ($ande3==1 and $mem2hp_flg<1){$andea3+=1;}
	if ($andea1==3){$andea1=0;$khp_flg=$chara[16];}
	if ($andea2==3){$andea2=0;$mem1hp_flg=$mem1[16];}
	if ($andea3==3){$andea3=0;$mem2hp_flg=$mem2[16];}

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

	if($smem1hp_flg > 0){$smem1hp_flg += $shpplus1;}
	if($smem2hp_flg > 0){$smem2hp_flg += $shpplus2;}
	if($smem3hp_flg > 0){$smem3hp_flg += $shpplus3;}
	if($smem4hp_flg > 0){$smem4hp_flg += $shpplus4;}

	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0){
			if($chara[31]=="0028" and $i==1){
			}elsif($chara[31]=="0041" and $i<=2){
			}elsif($chara[31]=="0042" and int(rand(5))==0){
			}elsif($chara[31]=="0049" or $miti==1){
				$miti=1;
				&acs_lose;
			}elsif($sinda==1){
			}else{
			$khp_flg = $khp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==1) {
			if($mem1[31]=="0028" and $i==1){
			}elsif($mem1[31]=="0041" and $i<=2){
			}elsif($mem1[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==2){
			}else{
			$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==2){
			if($mem2[31]=="0028" and $i==1){
			}elsif($mem2[31]=="0041" and $i<=2){
			}elsif($mem2[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==3){
			}else{
			$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==3){
			if($mem3[31]=="0028" and $i==1){
			}elsif($mem3[31]=="0041" and $i<=2){
			}elsif($mem3[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==4){
			}else{
			$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==4){
			if($chara[31]=="0028" and $i==1){
			}elsif($chara[31]=="0041" and $i<=2){
			}elsif($chara[31]=="0042" and int(rand(5))==0){
			}elsif($chara[31]=="0049" or $miti==1){
				$miti=1;
				&acs_lose;
			}elsif($sinda==1){
			}else{
			$khp_flg = $khp_flg - ${'sdmg'.$tai};
			}
			if($mem1[31]=="0028" and $i==1){
			}elsif($mem1[31]=="0041" and $i<=2){
			}elsif($mem1[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==2){
			}else{
			$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
			}
			if($mem2[31]=="0028" and $i==1){
			}elsif($mem2[31]=="0041" and $i<=2){
			}elsif($mem2[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==3){
			}else{
			$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
			}
			if($mem3[31]=="0028" and $i==1){
			}elsif($mem3[31]=="0041" and $i<=2){
			}elsif($mem3[31]=="0042" and int(rand(5))==0){
			}elsif($sinda==4){
			}else{
			$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
			}
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
	if ($mem3hp_flg > $chara[43]) {
		$mem3hp_flg = $chara[43];
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
	if ($smem4hp_flg > $smem4hp){
		$smem4hp_flg = $smem4hp;
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

	# ���@�ϐ�
	if($place==17){
		for($tai=1;$tai<4;$tai++){
			$mtai=${'staisyo'.$tai}+1;
			if(${'mzoku'.$mtai}==8 and ${'maho'.$tai}==1){
				${'com'.$tai}.="<font color=red size=4>��_�����I</font>";
				${'dmg'.$tai}=${'dmg'.$tai}*2;
				${'ssake'.$mtai}=int(${'ssake'.$mtai}/2);
			}elsif(${'mzoku'.$mtai}>0 and ${'maho'.$tai}==${'mzoku'.$mtai}+1){
				${'com'.$tai}.="<font color=red size=4>��_�����I</font>";
				${'dmg'.$tai}=${'dmg'.$tai}*2;
				${'ssake'.$mtai}=int(${'ssake'.$mtai}/2);
			}elsif(${'maho'.$tai}==8 and ${'mzoku'.$mtai}==1){
				${'com'.$tai}.="<font color=blue size=4>�ϐ������I</font>";
				${'dmg'.$tai}=int(${'dmg'.$tai}/2);
				${'ssake'.$mtai}=int(${'ssake'.$mtai}*2);
			}elsif(${'maho'.$tai}>0 and ${'mzoku'.$mtai} == ${'maho'.$tai}+1){
				${'com'.$tai}.="<font color=blue size=4>�ϐ������I</font>";
				${'dmg'.$tai}=int(${'dmg'.$tai}/2);
				${'ssake'.$mtai}=int(${'ssake'.$mtai}*2);
			}
		}
	}

	# ������
	if ($chara[55]==25 or $chara[56]==25 or $chara[57]==25 or $chara[58]==25){$mem1hit_ritu = int($mem1hit_ritu * 1.5);}
	if ($mem1[55]==25 or $mem1[56]==25 or $mem1[57]==25 or $mem1[58]==25){$mem2hit_ritu = int($mem2hit_ritu * 1.5);}
	if ($mem2[55]==25 or $mem2[56]==25 or $mem2[57]==25 or $mem2[58]==25){$mem3hit_ritu = int($mem3hit_ritu * 1.5);}

	# ���
	if ($chara[55]==55 or $chara[56]==55 or $chara[57]==55 or $chara[58]==55){$sake1=0;}
	if ($mem1[55]==55 or $mem1[56]==55 or $mem1[57]==55 or $mem1[58]==55){$sake2=0;}
	if ($mem2[55]==55 or $mem2[56]==55 or $mem2[57]==55 or $mem2[58]==55){$sake3=0;}

	$sake1 = int($sake1/500);
	$sake2 = int($sake2/500);
	$sake3 = int($sake3/500);
	$sake4 = int($sake4/500);
	if ($sake1 > 90){$sake1 = 91;}
	if ($sake2 > 90){$sake2 = 91;}
	if ($sake3 > 90){$sake3 = 91;}
	if ($sake4 > 90){$sake4 = 91;}
	if($chara[55]==34 or $chara[56]==34 or $chara[57]==34 or $chara[58]==34){
		$sdmg1=int($sdmg1*3/4);
		$sdmg2=int($sdmg2*3/4);
		$sdmg3=int($sdmg3*3/4);
		$sdmg4=int($sdmg4*3/4);
	}elsif($mem1[55]==34 or $mem1[56]==34 or $mem1[57]==34 or $mem1[58]==34){
		$sdmg1=int($sdmg1*3/4);
		$sdmg2=int($sdmg2*3/4);
		$sdmg3=int($sdmg3*3/4);
		$sdmg4=int($sdmg4*3/4);
	}elsif($mem2[55]==34 or $mem2[56]==34 or $mem2[57]==34 or $mem2[58]==34){
		$sdmg1=int($sdmg1*3/4);
		$sdmg2=int($sdmg2*3/4);
		$sdmg3=int($sdmg3*3/4);
		$sdmg4=int($sdmg4*3/4);
	}

	#�V�[���h�̃}�e���A
	if($chara[24]==1400){
		if ($item[35]%100==11 or $item[36]%100==11){
			if($item[35]%100==11){ $gp = 1+int($item[35]/100+1)*0.1; }
			else { $gp = 1+int($item[36]/100+1)*0.1; }
			$sdmg1=int($sdmg1/$gp);
			$sdmg2=int($sdmg2/$gp);
			$sdmg3=int($sdmg3/$gp);
			$sdmg4=int($sdmg4/$gp);
		}
	}

	$si1=1; $si2=1; $si3=1;
	if ($chara[31]=="0051"){ $si1 = 2; }
	if ($mem1[31]=="0051"){ $si2 = 2; }
	if ($mem2[31]=="0051"){ $si3 = 2; }

	if ($chara[31]=="0056" or $mem1[31]=="0056" or $mem2[31]=="0056"){
		if($mem1[31]=="0056"){
			$com2 .= "<FONT SIZE=4 COLOR=\"Lime\">���̌��ʁI</FONT>";
		}elsif($mem2[31]=="0056"){
			$com3 .= "<FONT SIZE=4 COLOR=\"Lime\">���̌��ʁI</FONT>";
		}else{
			$com1 .= "<FONT SIZE=4 COLOR=\"Lime\">���̌��ʁI</FONT>";
		}
		$ssake1 = int($ssake1/10);
		$ssake2 = int($ssake2/10);
		$ssake3 = int($ssake3/10);
		$ssake4 = int($ssake4/10);
	}
	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $si1*$item[4]*(2+int($chara[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{ ${'sdmg'.$tai} = ${'sdmg'.$tai} - $si1*$item[4] * (2+int($chara[10]/10+1)); }
			if (int($sake1 - (${'smem'.$tai.'hit_ritu'} / 100)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} .= "<FONT SIZE=4 COLOR=\"$red\">$chara[4]�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'taisyo'.$tai} ==1 or ${'taisyo'.$tai} ==4) {
			if (${'sdmg'.$tai} < $si2*$mem1item[4]*(2+int($mem1[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$si2*$mem1item[4] * (2+int($mem1[10]/10+1)); }
			if (int($sake2 - (${'smem'.$tai.'hit_ritu'} / 100)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} .= "<FONT SIZE=4 COLOR=\"$red\">$mem1[4]�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'taisyo'.$tai} ==2 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $si3*$mem2item[4]*(2+int($mem2[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$si3*$mem2item[4] * (2+int($mem2[10]/10+1)); }
			if (int($sake3 - (${'smem'.$tai.'hit_ritu'} / 100)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} .= "<FONT SIZE=4 COLOR=\"$red\">$mem2[4]�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'taisyo'.$tai} ==3 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $chara[49] * (2+int($chara[49]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$chara[49] * (2+int($chara[49]/10+1)); }
			if (int($sake4 - (${'smem'.$tai.'hit_ritu'} / 100)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} .= "<FONT SIZE=4 COLOR=\"$red\">$chara[39]�͐g�����킵���I</FONT>";
			}
		}

		if (${'staisyo'.$tai}==0 or ${'staisyo'.$tai}==4){
			if($ssake1 - ${'mem'.$tai.'hit_ritu'}>90){$hitok=90;}else{$hitok=$ssake1 - ${'mem'.$tai.'hit_ritu'};}
			if($tai==4){
				if($mem4hit_ritu < int(rand(100))){
					${'dmg'.$tai} = 0;
					${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname1�͐g�����킵���I</FONT>";
				}
			}
			elsif ($hitok > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname1�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'staisyo'.$tai}==1 or ${'staisyo'.$tai}==4) {
			if($ssake2 - ${'mem'.$tai.'hit_ritu'}>90){$hitok=90;}else{$hitok=$ssake2 - ${'mem'.$tai.'hit_ritu'};}
			if($tai==4){
				if($mem4hit_ritu < int(rand(100))){
					${'dmg'.$tai} = 0;
					${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname2�͐g�����킵���I</FONT>";
				}
			}
			elsif ($hitok > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname2�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'staisyo'.$tai}==2 or ${'staisyo'.$tai}==4){
			if($ssake3 - ${'mem'.$tai.'hit_ritu'}>90){$hitok=90;}else{$hitok=$ssake3 - ${'mem'.$tai.'hit_ritu'};}
			if($tai==4){
				if($mem4hit_ritu < int(rand(100))){
					${'dmg'.$tai} = 0;
					${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname3�͐g�����킵���I</FONT>";
				}
			}
			elsif ($hitok > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname3�͐g�����킵���I</FONT>";
			}
		}
		elsif(${'staisyo'.$tai}==3 or ${'staisyo'.$tai}==4){
			if($ssake4 - ${'mem'.$tai.'hit_ritu'}>90){$hitok=90;}else{$hitok=$ssake4 - ${'mem'.$tai.'hit_ritu'};}
			if($tai==4){
				if($mem4hit_ritu < int(rand(100))){
					${'dmg'.$tai} = 0;
					${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname4�͐g�����킵���I</FONT>";
				}
			}
			elsif ($hitok > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$ssmname4�͐g�����킵���I</FONT>";
			}
		}
	}

	if($shpplus1 > 0){$skaihuku1="$shpplus1�̉񕜁�";}
	if($shpplus2 > 0){$skaihuku2="$shpplus2�̉񕜁�";}
	if($shpplus3 > 0){$skaihuku3="$shpplus3�̉񕜁�";}
	if($shpplus4 > 0){$skaihuku4="$shpplus4�̉񕜁�";}

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
	if ($i == 1 or $ssmname1 eq "OMEGA") {
		$battle_date[$j] .= <<"EOM";
		<TD>
EOM
		if($khp_flg>=0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$chara[6]]">
EOM
		}
		if($mem1hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem1[6]]">
EOM
		}
		if($mem2hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem2[6]]">
EOM
		}
		if($mem3hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_pet/$egg_img[$chara[45]]">
EOM
		}
		$battle_date[$j] .= <<"EOM";
		</TD><TD></TD><TD></TD><TD>
EOM
		if($smem1hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg1]">
EOM
		}elsif($smem1hp_flg>0 and $ssmname1 eq "OMEGA"){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg1]">
EOM
		}
		if($smem2hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg2]">
EOM
		}
		if($smem3hp_flg>0 and $chara[50]!=1){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[$mimg3]">
EOM
		}
		if($smem4hp_flg>0 and $chara[50]!=1){
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
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
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
		if(${'taisyo'.$tai}==3){${'smname'.$tai}=$pename;}
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
	if ($chara[55]==62 or $chara[56]==62 or $chara[57]==62 or $chara[58]==62)
		{$ygold = $i * int(rand(30000));}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + $ygold + int(rand($mgold*$chara[20])+1);
		if($chara[24]==1080){$gold=$gold*2;}
($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
$mon = $mon+1;
		if ($mon==12 and $mday==24){$gold=$gold*3;}
		if($item[3] eq "�N���X�}�X�E�A�[�}�["){$gold=int($gold*1.5);}
		if($item[3] eq "�N���X�}�X�E�V�[���h"){$gold=int($gold/2);}
		if($chara[31]=="0050"){$gold=$gold*2;}
		if($chara[0] eq "jupiter"){$gold=$gold*2;}
		if(!$goldplus){$goldplus=1;}
		$gold = int($gold * $goldplus);
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
		$mex = int($mex/4);
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
	$sentou=$chara[8] * 4 + $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10 + $chara[8]/10 + 1);
	$sentou+=int($chara[16]/2) + $item[4] * (4 + int($chara[10]/10+1));
	$sentou+=(int(($chara[11] / 10)) + 10 + int($chara[12]/4))*10;
	$sentou+=(int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16])*10;
	$sentou+=(int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17])*10;
	if($item[0] eq "�f��" or $item[3] eq "���i��"){$sentou+=int(rand(10));}
		if(!$chara[89]){$chara[89]=1;}
		if($sentou%1000==0 or $chara[89]%1000==0){$mex= int($mex * 2);}
		if($chara[33]==100){$mex= int($mex * 1.5);}
		if($khp_flg<=0){$mex= int($mex/2);}
		if($item[3] eq "�N���X�}�X�E�V�[���h"){$mex=int($mex*1.5);}
		if($item[3] eq "�N���X�}�X�E�A�[�}�["){$mex=int($mex/2);}
		if($chara[24]==1078 or $chara[24]==1083 or $chara[24]==1345){$mex = $mex * 2;}
		if($chara[24]==1331){$mex = $mex * int(rand(2)+2);}
		if($chara[31]=="0014"){$mex = $mex * 1.5;}
		if($chara[31]=="0025"){$mex = $mex * 1.8;}
		if($chara[31]=="0027" or $chara[31]=="0055"){$mex = $mex * 2;}
		if($chara[18]<100){$mex = $mex * 2;}
		if($chara[30]==1000 or $chara[30]==3000){$mex = $mex * 2;}
		#�����̃}�e���A
		if($chara[24]==1400){
			if($item[35]%100==7){$mex = $mex + int($mex * int($item[35]/100 + 1) / 5);}
			if($item[36]%100==7){$mex = $mex + int($mex * int($item[36]/100 + 1) / 5);}
		}

		if($chara[63]==1){$mex=0;}

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
		$kmex = $mex*int(rand(8)+13);
		if($chara[0] eq "jupiter"){$kmex *= 10;}
		if($win!=3 and $win and $chara[38]>3000 and $in{'mode'} ne "guild_battle"){
			if($chara[24]==1076 and $chara[38]<3100)
				{$chara[40] = $chara[40] + $imex;}
			if($chara[24]==1133)
				{$chara[40] = $chara[40] + $kmex;}
			else{$chara[40] = $chara[40] + $mex;}
		}
		if($chara[31]=="0031"){
			open(IN,"pets/$chara[0].cgi");
			@log_item = <IN>;
			close(IN);
			$c=0;
			foreach (@log_item) {
		($i_no,$pi_name,$i_exp,$i_maxexp,$i_hp,$i_damage,$i_image,$i_lv,$i_ps,$i_namae) = split(/<>/);
				if($i_no){
					$i_exp+=$mex;
$log_item[$c]="$i_no<>$pi_name<>$i_exp<>$i_maxexp<>$i_hp<>$i_damage<>$i_image<>$i_lv<>$i_ps<>$i_namae<>\n";
				}
			$c++;
			}
			open(OUT,">pets/$chara[0].cgi");
			print OUT @log_item;
			close(OUT);
		}
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
		$chara[28] = $bossd;

	#�A�C�e���h���b�v
	if($win==1){
		if($chara[70]<1){$pp=($place/2) + 1;}
		else{$pp=($place/2) + 10;}
		if($on and $on==$place and $name eq "�G�b�O�G���W�F��"){
			if($chara[91] == 1){$item_no = 16;$chara[91]=2;&itemdrop;}
			elsif(int(rand($sdrop)) == 0){$item_no = 16;&itemdrop;}
		}
		elsif($place==31){
			if(int(rand(3000)) == 0){$item_no = int(rand(4)+1);&itemdrop;}
			elsif(int(rand(1500)) == 0){$item_no = int(rand(3)+1);&itemdrop;}
		}
		elsif($place==17){
			if(int(rand(3000)) == 0){$item_no = int(rand(2)+4);&itemdrop;}
			elsif(int(rand(750)) == 0){$item_no = int(rand(3)+1);&itemdrop;}
		}
		elsif($ssmname1 eq "�V�^�E�C���X"){
			if(int(rand(3000)) == 0){
				$lock_file = "$lockfolder/sitem$in{'id'}.lock";
				&lock($lock_file,'SI');

				open(IN,"$souko_folder/item/$chara[0].cgi");
				@souko_item = <IN>;
				close(IN);

				$souko_item_num = @souko_item;

				if ($souko_item_num >= $item_max) {
					&error("����q�ɂ������ς��ł��I$back_form");
				}
				push(@souko_item,"1081<>�^�~�t��<>200<>10<>0<>10<>0<>\n");
				open(OUT,">$souko_folder/item/$chara[0].cgi");
				print OUT @souko_item;
				close(OUT);
				$i_name="�^�~�t�� + 10";
			}
		}
		elsif($on and $on==$place and int(rand($sdrop)) == 0){$item_no = int(rand(15));&itemdrop;}
		elsif(int(rand($adrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+11);&itemdrop;}
		elsif(int(rand($bdrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+6);&itemdrop;}
		elsif(int(rand($cdrop*$pp/$drop_plus))==0){$item_no = int(rand(5)+1);&itemdrop;}
		if($ssmname1 eq "�G�b�O" and int(rand(15))==0 and $chara[18]>60){
			if($chara[38]<3001){&egg_egg;}
		}
		
		if($chara[18]>$mlv1 and $chara[24] == 1131){
			&pet_get;
		}
		if(int(($mon*$mday)%7)<4){$turu_plus+=0.8;}
		if($chara[70]<1 and int(rand($turu_drop / $turu_plus))==0){
			$comment.= "<b><font size=4 color=yellow>��͂����E�����I�I</font></b><br>";
			$chara[100]++;
		}
		if($chara[70]>=1 and int(rand($turu_drop2 / $turu_plus))==0){
			if(int(rand($chara[18]/3000))==0){
				$comment.= "<b><font size=4 color=yellow>��͂����E�����I�I</font></b><br>";
				$chara[100]++;
			}
		}
		elsif($chara[70]<1 and int(rand($ougon_drop / $turu_plus))==0){
			$comment.= "<b><font size=5 color=red>�����̂�͂������I�I</font></b><br>";
			$chara[97]++;
		}
		if($i_name){$comment .= "<b><font size=5 color=red>$i_name���E�����I�I</font></b><br>";}

		&quest;
	}
	if ($chara[55]==75 or $chara[56]==75 or $chara[57]==75 or $chara[58]==75){
		if($chara[55]==76 or $chara[56]==76 or $chara[57]==76 or $chara[58]==76){
			if($chara[55]==77 or $chara[56]==77 or $chara[57]==77 or $chara[58]==77){
				$getcoin=int(rand(45)+1);
				$chara[148]+=$getcoin;
				$comment .= "<b><font size=5 color=red>�R�C����$getcoin�����肵���I�I</font></b><br>";
			}elsif($win!=2){
				$getcoin=int(rand(18)+1);
				$chara[148]+=$getcoin;
				$comment .= "<b><font size=5 color=red>�R�C����$getcoin�����肵���I�I</font></b><br>";
			}
		}elsif($win!=1 and $win!=2){
			$getcoin=int(rand(10)+1);
			$chara[148]+=$getcoin;
			$comment .= "<b><font size=5 color=red>�R�C����$getcoin�����肵���I�I</font></b><br>";
		}
	}
}

#------------------#
#�퓬���ʔ���      #
#------------------#
sub legend_sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($chara[55]==62 or $chara[56]==62 or $chara[57]==62 or $chara[58]==62)
		{$ygold = $i * int(rand(30000));}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + $ygold + int(rand($mgold)+1);
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
			if ($chara[32] < $in{'boss_file'} + 1) {
				$chara[32] = $in{'boss_file'} + 1;
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
			}
		} else {
			$comment = "<b><font size=5>$chara[4]�́A�퓬�ɏ��������I�I�܂��܂���ɒ��킷�邼���I</font></b><br>";
		}
	} elsif ($win==2) {
		$mex = int($mex/4);
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

		if($chara[18]>$mlv1 and $chara[24] == 1131){
			&pet_get;
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
#�퓬���ʔ���      #
#------------------#
sub akuma_sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($chara[55]==62 or $chara[56]==62 or $chara[57]==62 or $chara[58]==62)
		{$ygold = $i * int(rand($mgold/10));}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + $ygold + int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
		$chara[134] = $mday;
		if($chara[135]>7){$chara[135]=7;}
		if($chara[135]<$in{'boss_file'} and $in{'boss_file'}!=8 and $in{'boss_file'}!=9){$chara[135] = $in{'boss_file'};}
		$comment .= "<b><font color=yellow size=5>$chara[4]�́A�����̊ق̍U���ɐ��������I</font></b><br>";

		if($in{'boss_file'}==8){
			if(int(rand(200))==0){
				$item_no=1;
				&itemdrop;
			}elsif(int(rand(800))==0){
				$item_no=2;
				&itemdrop;
			}elsif(int(rand(2000))==0){
				$item_no=3;
				&itemdrop;
			}
		}elsif($in{'boss_file'}==9){
			if(int(rand(800))==0){
				$item_no=1;
				&itemdrop;
			}elsif(int(rand(1600))==0){
				$item_no=2;
				&itemdrop;
			}elsif(int(rand(4000))==0){
				$item_no=3;
				&itemdrop;
			}
		}elsif(int(rand(2))==0){
			if(int(rand(3))==0){$item_no=1;}
			elsif(int(rand(2))==0){$item_no=2;}
			elsif(int(rand(3))==0){$item_no=3;}
			elsif(int(rand(2))==0){$item_no=4;}	
			elsif(int(rand(3))==0){$item_no=5;}
			elsif(int(rand(2))==0){$item_no=6;}
			else{$item_no=7;}
			&itemdrop;
		}elsif(int(rand(10))<8){
			$chara[146]+=1;
			$i_name="�����E�`�P�b�g";
		}

		if($test!=1 and $i_name){
			$lock_file = "$lockfolder/messa$in{'id'}.lock";
			&lock($lock_file,'MS');
			open(IN,"$chat_file");
			@chat_mes = <IN>;
			close(IN);
			$mes_sum = @chat_mes;
			if($in{'boss_file'}==8 or $in{'boss_file'}==9){
				$chmes="$chara[4]�l�������E�̈����̓����ɐ������A�Ȃ��$i_name����肵�܂����I";
			}else{
				$chmes="$chara[4]�l�������̊�$in{'boss_file'}F�̈����̓����ɐ������A$i_name����肵�܂����I";
			}
			if($mes_sum > $mes_max) { pop(@chat_mes); }
			unshift(@chat_mes,"<><font color=\"yellow\">���m</font><>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$chmes</font><>$host<><>\n");

			open(OUT,">$chat_file");
			print OUT @chat_mes;
			close(OUT);
			&unlock($lock_file,'MS');
		}

		open(IN,"akuma_log.cgi");
		@akuma_log = <IN>;
		close(IN);

		$aku_sum = @akuma_log;
		if($i_name){$akumes="$chara[4]�l�������̊�$in{'boss_file'}F�̃{�X�̓����ɐ������A$i_name����肵�܂����I";}
		else{$akumes="$chara[4]�l�������̊�$in{'boss_file'}F�̃{�X�̓����ɐ������܂����I";}
		if($aku_sum > 100) { pop(@akuma_log); }
		unshift(@akuma_log,"$year�N$mon��$mday��(��)$hour��$min��$akumes\n");

		open(OUT,">akuma_log.cgi");
		print OUT @akuma_log;
		close(OUT);

		if($i_name){$comment .= "<b><font size=5 color=red>$i_name���E�����I�I</font></b><br>";}
		if($in{'boss_file'}==9 and int(rand(30))==0){
			$comment.= "<b><font size=4 color=yellow>�v���`�i��͂����E�����I�I</font></b><br>";
			$chara[310]++;
		}
	} else {
		$mex = 1;
		$chara[28] = $bossd;
		#$chara[19] = int(($chara[19] / 2));
		$comment = "<b><font size=5>$chara[4]�́A�퓬�ɕ������E�E�E�B</font></b><br>";

		open(IN,"akuma_log2.cgi");
		@akuma_log2 = <IN>;
		close(IN);

		$aku_sum2 = @akuma_log2;
		$akumes2="$chara[4]�l�������̊�$in{'boss_file'}F�̃{�X�̓����Ɏ��s���܂����I";
		if($aku_sum2 > 100) { pop(@akuma_log2); }
		unshift(@akuma_log2,"$year�N$mon��$mday��(��)$hour��$min��$akumes2\n");

		open(OUT,">akuma_log2.cgi");
		print OUT @akuma_log2;
		close(OUT);

	}

		if($khp_flg<=0){$mex= int($mex/10);}
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
}
#------------------#
#�A�C�e���h���b�v  #
#------------------#
sub itemdrop{
	if($aku==1 or $akumakai==1){
		open(IN,"data/akumadrop$in{'boss_file'}.ini");
		@item_array = <IN>;
		close(IN);
	}elsif($qh==3){
		open(IN,"questitem3.cgi");
		@item_array = <IN>;
		close(IN);
	}elsif($qh==2){
		open(IN,"questitem2.cgi");
		@item_array = <IN>;
		close(IN);
	}elsif($qh==1){
		open(IN,"questitem.cgi");
		@item_array = <IN>;
		close(IN);
	}elsif($on and $on==$place){
		open(IN,"$drop11_file");
		@item_array = <IN>;
		close(IN);
	}else{
		if($place==20){$drop_file="drop1_file";}
		elsif($place==31){$drop_file="drop31_file";}
		elsif($place>=30){$drop_file="drop1_file";}
		else{$drop_file="drop$place\_file";}
		if(!$$drop_file){$drop_file="drop12_file";}
		open(IN,"$$drop_file");
		@item_array = <IN>;
		close(IN);
	}
	$hit=0;
	foreach(@item_array){
		($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
		if($item_no eq "$ino") { $hit=1;last; }
	}
	if(!$hit) { &error("$drop_file @item_array $mname ����ȃA�C�e���͑��݂��܂��� $q_name $item_no"); }

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if($i_no < 1000){
		open(IN,"$souko_folder/acs/$chara[0].cgi");
		@souko_acs = <IN>;
		close(IN);
		$souko_acs_num = @souko_acs;
		if ($souko_acs_num >= $acs_max) {
			&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}elsif($i_no < 2000 and $i_no > 1000){
		open(IN,"$souko_folder/item/$chara[0].cgi");
		@souko_item = <IN>;
		close(IN);
		$souko_item_num = @souko_item;
		if ($souko_item_num >= $item_max) {
			&error("����q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$i_hissatu<>$i_tokusyu<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($i_no < 3000 and $i_no > 2000){
		open(IN,"$souko_folder/def/$chara[0].cgi");
		@souko_def = <IN>;
		close(IN);
		$souko_def_num = @souko_def;
		if ($souko_def_num >= $def_max) {
			&error("�h��q�ɂ������ς��ł��I$back_form");
		}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}elsif($i_no < 4000 and $i_no > 3000){
		open(IN,"pets/$chara[0].cgi");
		@log_item = <IN>;
		close(IN);
		$log_item_num = @log_item;
		if ($log_item_num >= $acs_max) {
			&error("�q�ꂪ�����ς��ł��I$back_form");
		}
		push(@log_item,"$i_no<>$i_name<>0<>$i_dmg<>$i_def<>$ihit<>$i_kai<>1<>$i_str<>\n");
		open(OUT,">pets/$chara[0].cgi");
		print OUT @log_item;
		close(OUT);
	}elsif($i_no > 3999 and $i_no<5000){
		$i_no=$i_no-4000;
		open(IN,"./mayaku/$chara[0].cgi");
		$mayaku_list = <IN>;
		close(IN);
		@mayaku = split(/<>/,$mayaku_list);
		$mayaku[$i_no]+=1;
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
		open(IN,"mayaku.cgi");
		@mayaku_data = <IN>;
		close(IN);
		foreach(@mayaku_data){
			($mayano,$mayaname,$mayakind) = split(/<>/);
			if($mayano == $i_no){last;}
		}
		$i_name=$mayaname;
	}elsif($i_no > 7000 and $i_no<8000){
		$i_no=$i_no-7000;
		$chara[$i_no]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 == $i_no){last;}
		}
		$i_name=$sname3;
	}else{&error("�A�C�e����������܂���I$back_form");}

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
					$qh=1;$item_no=$q_no;&itemdrop;
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
	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$eg</span>";

	unshift(@CLOG,"kokuti<>���m<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);
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
			foreach(@quest2_item){														($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
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
					if($q_item eq "�����X�^�[�̍�"){
						open(IN,"$pet_file");
						@item_array = <IN>;
						close(IN);
						$hit=0;$gxu=0;
						while($hit!=1 and $gxu<10){
							$pmons=int(rand(100)+3401);
							foreach(@item_array){
			($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
							if($phi_no == $pmons) { $hit=1;last; }
							}
							$gxu++;
						}
						if(!$hit){$comment .= "���̓���Ɏ��s�����c(��)<br>";}
						else{
							$comment .= "$phi_name�̍�����肵���I�I<br>";
							$pmons-=3200;
							$chara[$pmons]+=1;
						}
					}else{
						$qh=2;$item_no=$q_no;&itemdrop;
						$comment .= "��V$i_name����肵���I�I<br>";
						$i_name="";
					}
				}
				if($i==177){
					$lock_file = "$lockfolder/messa$in{'id'}.lock";
					&lock($lock_file,'MS');

					open(IN,"$chat_file");
					@chat_mes = <IN>;
					close(IN);

					$mes_sum = @chat_mes;

					if($mes_sum > $mes_max) { pop(@chat_mes); }

					$eg="$chara[4]�l�������N�G�X�g���e�ŏI�W�I�𓢔����܂���";

	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$eg</span>";

	unshift(@CLOG,"kokuti<>���m<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);


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
	open(IN,"inquest3.cgi");
	@quest3_item = <IN>;
	close(IN);
	for($i=196;$i<200;$i++){
		if($chara[$i]==1){
			$hit=0;
			foreach(@quest3_item){														($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
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
					$qh=3;$item_no=$q_no;&itemdrop;
					$comment .= "��V$i_name����肵���I�I<br>";
					$i_name="";
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
	if($item[0] eq "���̌�"){$item[1]-=int(rand($chara[18]/20));if($item[1]<0){$item[1]=0;}&item_regist;}
	if($item[0] eq "����Ƃ炷�؂����"){$item[1]-=10;if($item[1]<-800){$item[1]=-800;}&item_regist;}
	if($item[3] eq "���؂���邤��Ƃ�"){$item[4]-=10;if($item[4]<-800){$item[4]=-800;}&item_regist;}
	if($item[0] eq "�܂���ĂԂꂢ���["){$item[1]=0;&item_regist;}
	if($item[0] eq "10����"){$item[1]-=5;if($item[1]<-1000){$item[1]=-1000;}&item_regist;}
	if($siren!=1){$mex=0;$mgold=0;}
	if($chara[141]>0 and $mode ne "boss" and $place!=98){
		$chara[142]++;
		if($place!=17){
			open(IN,"data/otte.ini");
			@MONSTER = <IN>;
			close(IN);
		}else{
			open(IN,"data/otte2.ini");
			@MONSTER = <IN>;
			close(IN);
		}
		$r_no = @MONSTER;
		$kazu=5;
	}
	if($chara[142]>49){$chara[141]-=1; $chara[142]=0;}
	if($on and $on==$place){
		if($kazu==2){
		for($mon=1;$mon<$kazu;$mon++){
			foreach(@MONSTER){
(${'keikatime'.$mon},${'basyo'.$mon},${'ssmname'.$mon},${'mzoku'.$mon},${'mlv'.$mon},${'mex'.$mon},${'mrand'.$mon},${'msp'.$mon},${'maxhp'.$mon},${'mdmg'.$mon},${'mkahi'.$mon},${'monstac'.$mon},${'mons_ritu'.$mon},${'mgold'.$mon},${'mimg'.$mon}) = split(/<>/);
			if (${'ssmname'.$mon} eq $name) {last;}
			}
			$mex += int(${'mex'.$mon} * $exp_plus);
			$mgold += ${'mgold'.$mon};
			if (${'monstac'.$mon}) {
				require "./mons/${'monstac'.$mon}.pl";
			} else {
				require "./mons/0.pl";
			}
		}
		}else{
			$mon=1;
			foreach(@MONSTER){
(${'keikatime'.$mon},${'basyo'.$mon},${'ssmname'.$mon},${'mzoku'.$mon},${'mlv'.$mon},${'mex'.$mon},${'mrand'.$mon},${'msp'.$mon},${'maxhp'.$mon},${'mdmg'.$mon},${'mkahi'.$mon},${'monstac'.$mon},${'mons_ritu'.$mon},${'mgold'.$mon},${'mimg'.$mon}) = split(/<>/);
			$mex += int(${'mex'.$mon} * $exp_plus);
			$mgold += ${'mgold'.$mon};
			if (${'monstac'.$mon}) {
				require "./mons/${'monstac'.$mon}.pl";
			} else {
				require "./mons/0.pl";
			}
			$mon++;
			}
		}
	}else{
		for($mon=1;$mon<$kazu;$mon++){
			if($place==29){
				if($chara[93]<5000000){$s_no = 0;}
				elsif($chara[93]<20000000){$s_no = 1;}
				elsif($chara[93]<30000000){$s_no = 2;}
				elsif($chara[93]<40000000){$s_no = 3;}
				elsif($chara[93]<50000000){$s_no = 4;}
				else{$s_no = 5;}
				if($chara[84]==1){
					$chara[84]=0;
					$syakuhou=1;
				}
			}elsif($chara[84]==1){
				&error("�ߕ߂���Ă��܂��B�x�@���֍s���Ă��������B");
			}elsif($aku==1){$s_no = $r_no;
			}elsif($le!=1){$s_no = int(rand($r_no));}
			else{$s_no = $r_no-1;}
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
	if ($win!=1 and $on and $on ==$place){
		open(IN,"$boss_monster");
		@boss_data = <IN>;
		close(IN);
		$i=0;
		foreach(@boss_data){
			@array = split(/<>/);
			if ($array[2] eq $name){
				$array[7]=$smem1hp_flg;
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array .= "<>\n";
				$boss_data[$i]=$new_array;
				open(OUT,">$boss_monster");
				print OUT @boss_data;
				close(OUT);
				last;
			}
			$i++;
		}
	}elsif($win==1 and $on and $on ==$place){
		$hit=0;
		open(IN,"$boss_monster");
		@boss_data = <IN>;
		close(IN);
		$i=0;
		foreach(@boss_data){
			@array = split(/<>/);
			if ($array[2] eq $name){
				$array[7]=$array[8];
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array .= "<>\n";
				$boss_data[$i]=$new_array;
				open(OUT,">$boss_monster");
				print OUT @boss_data;
				close(OUT);
				last;
			}
		$i++;
		}
		open(IN,"./data/bosson.ini");
		@bosson_data = <IN>;
		close(IN);
		$g=0;
		foreach(@bosson_data){
			($name,$on) = split(/<>/);
			if($on and $name eq $ssmname1){
				$bosson_data[$g]="$name<>0<>\n";
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

	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$bosss</span>";

	unshift(@CLOG,"kokuti<>���m<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);


	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<>$bosss<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]+=1;
	$chara[65]-=1;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]>100){$chara[64]=100;}
	if($chara[65]<0){$chara[65]=0;}

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
		if(int($yado_dai*$chara[18])>100000 and int(rand(100))==0){
			$chara[305]+=1;
			print "<b><font size=2>���y�Y�ɏh���݂���ɓ��ꂽ�I���݂̏������F$chara[305]��</font></b><br>";
		}
	}else{
			print "<b><font size=2>$chara[4]�́A�h���ɍs�����Ƃ���������������Ȃ������B</font></b><br>";
			}
		}
	}
	&chara_regist;

	if($in{'mode'} eq "monster" and $place!=29){
	print <<"EOM";
<form action= "monster.cgi">
<input type= "hidden" name= "mode" value= "monster">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$new_chara">
<input type="hidden" name="mons_file" value="$in{'mons_file'}">
<input type= "submit" class= "btn" value= "����ɓ���">
</form>
EOM
}
	if($in{'mode'} eq "guild_battle"){
	print <<"EOM";
<form action= "guild_battle.cgi">
<input type= "hidden" name= "mode" value= "guild_battle">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$new_chara">
<input type="hidden" name="guild_file" value="$in{'guild_file'}">
<input type= "submit" class= "btn" value= "����ɓ���">
</form>
EOM
}
	print <<"EOM";
<form action="$script">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}
1;