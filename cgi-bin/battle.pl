#------------------#
#�@����҂̍U��  �@#
#------------------#
sub tyousensya {
	if($chara[24] != "1356" and $chara[24] != "1358" and $chara[59]==10){ $chara[59] = 0; }
	if($i == 2){
		if ($chara[55]==79 or $chara[56]==79 or $chara[57]==79 or $chara[58]==79){
			$i=21;
		}
	}
	$maho1=0;$maho2=0;$maho3=0;
	if($khp_flg > 0){
		$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
		if ($chara[55]==33 or $chara[56]==33 or $chara[57]==33 or $chara[58]==33){$mahoken=1;}else{$mahoken=0;}
		if ($chara[59] and int(rand(4 - $mahoken * 3))==0) {
			$ccc=1;
			$sp=1;
			$dmg1 = $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
			if($mahoken == 1){$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);}
			require "./spell/$chara[59].pl";
			$spell="spell$chara[59]";
			&$spell;
		}
		if(!$ccc){
			if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}
			if($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="yellow";}else{$g="";}
			$com1 = "$chara[4]�́A<font color=\"$g\">$item[0] $bukilv</font>�ōU���I�I";
			if( ($chara[7] + $item[1]) > ($chara[8] + $item[1]) ){
				$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);
			}else{
				$dmg1 += $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
			}
		}
	#�o�[�T�N
		if ($chara[55]==21 or $chara[56]==21 or $chara[57]==21 or $chara[58]==21){
			$dmg1 += ($chara[15]-$khp_flg);
		}
	#���v��
		if ($chara[55]==78 or $chara[56]==78 or $chara[57]==78 or $chara[58]==78){
			if($i>19){$dmg1 *= 8;}
		}
	#�K�ナ���O
		if ($chara[31]=="0055"){
			if($i<31){$dmg1 = int($dmg1/3);}
		}
	#���̔��
		if ($chara[31]=="0051"){
			$dmg1 = $dmg1*2;
		}
	#�{�X�L���[�A�N�X
		if ($on and $on ==$place and $chara[24]==1323){
			$dmg1 *= 44;
		}
	#�N���E������
		if($chara[69]==1){
			if($chara[65]>=70 or $chara[65]<=30){$dmg1 = int($dmg1 * ($chara[65]-50)/20);}
		}
		if($chara[69]==2){
			if($chara[64]>=70 or $chara[64]<=30){$dmg1 = int($dmg1 * ($chara[64]-50)/20);}
		}
	#�K�E���@�H
		if ($sudedmg==1) {
			$dmg1 = $dmg1 * 777;
		}
	#�E�C���X
		if($chara[24]==1081 and int(rand(4))==0){
			$com1 .= "<font color=\"red\" size=3>$chara[4]�́A��s���N�������I</font>";
			$dmg1-=$dmg1*2;
		}
	#10��
		if($item[1]==5 and $item[0] eq "10����"){
			$dmg1=1000000000;
		}
	}
	#�}�e���A
		if ($chara[24]==1400){
		#�Ή��̃}�e���A
			if ($item[31]==1 or $item[32]==1){
				$dmg1 = int($dmg1*1.2);
			}
			if ($item[31]==101 or $item[32]==101){
				$dmg1 = int($dmg1*1.5);
			}
			if ($item[31]==201 or $item[32]==201){
				$dmg1 = int($dmg1*2);
			}
		#�����̃}�e���A
			if ($item[31]==9 or $item[32]==9){
				$mem1hit_ritu=$mem1hit_ritu*2;
			}
			if ($item[31]==109 or $item[32]==109){
				$mem1hit_ritu=$mem1hit_ritu*3;
			}
			if ($item[31]==209 or $item[32]==209){
				$mem1hit_ritu=$mem1hit_ritu*4;
			}
		#�]���̃}�e���A
			if ($item[33]==10 or $item[34]==10){
				$khp_flg = int($khp_flg/10);
				$dmg1 = int($dmg1*1.5);
			}
			if ($item[33]==110 or $item[34]==110){
				$khp_flg = int($khp_flg/1000);
				$dmg1 = int($dmg1*2);
			}
			if ($item[33]==210 or $item[34]==210){
				$khp_flg = int($khp_flg/10000);
				$dmg1 = int($dmg1*2.5);
			}
			if ($item[33]==310 or $item[34]==310){
				$khp_flg = int($khp_flg/100000);
				$dmg1 = int($dmg1*3);
			}
		#�G�A���̃}�e���A
			if ($item[37]%100==12 or $item[38]%100==12){
				if($item[37]%100==12){ $sakep = 1+int($item[37]/100+1)*0.2; }
				else { $sakep = 1+int($item[38]/100+1)*0.2; }
				$ssake1= int($ssake1 / $sakep);
				$ssake2= int($ssake2 / $sakep);
				$ssake3= int($ssake3 / $sakep);
				$ssake4= int($ssake4 / $sakep);
			}
		}
	for($kou=1;$kou<4;$kou++){
		$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
		$ddd=$kou+1;
		if(${'mem'.$kou.'hp_flg'} > 0){
			$mahoken=0;
			if (${'mem'.$kou}[55]==33 or ${'mem'.$kou}[56]==33 or ${'mem'.$kou}[57]==33 or ${'mem'.$kou}[58]==33){$mahoken=1;}else{$mahoken=0;}
			if (${'mem'.$kou}[59] and int(rand(4 - $mahoken * 3))==0) {
				$ccc=1;
				$sp=$kou+1;
				${'dmg'.$ddd} = ${'mem'.$kou}[8] * 4 + ${'mem'.$kou.'item'}[4] * 4 * int(${'mem'.$kou}[8]/10+1);
				if($mahoken == 1){${'dmg'.$ddd} += ${'mem'.$kou}[7] * 4 + ${'mem'.$kou.'item'}[1] * 4 * int(${'mem'.$kou}[7]/10+1);}
				#PT�����o�[�E�U���͕␳���h��͂ɉ�����UP��
				${'dmg'.$ddd} = ${'dmg'.$ddd} + int(rand(${'mem'.$kou.'item'}[4] * 10));

				require "./spell/${'mem'.$kou}[59].pl";
				$spell2="spell${'mem'.$kou}[59]";
				&$spell2;
			}
			if(!$ccc){
				if(${'mem'.$kou.'item'}[20]){$bukilv="+ ${'mem'.$kou.'item'}[20]";}else{$bukilv="";}
				if(${'mem'.$kou.'item'}[20]==10){$g="red";}elsif(${'mem'.$kou}[24]==1400){$g="yellow";}else{$g="";}
				${'com'.$ddd} = "${'mem'.$kou}[4]�́A<font color=\"$g\">${'mem'.$kou.'item'}[0] $bukilv</font>�ōU���I�I";
				if( (${'mem'.$kou}[7] + ${'mem'.$kou.'item'}[1]) > (${'mem'.$kou}[8] + ${'mem'.$kou.'item'}[1]) ){
					${'dmg'.$ddd} += ${'mem'.$kou}[7] * 4 + ${'mem'.$kou.'item'}[1] * 4 * int(${'mem'.$kou}[7]/10+1);
				}else{
					${'dmg'.$ddd} += ${'mem'.$kou}[8] * 4 + ${'mem'.$kou.'item'}[1] * 4 * int(${'mem'.$kou}[8]/10+1);
				}
			}
		#�o�[�T�N
			if (${'mem'.$kou}[55]==21 or ${'mem'.$kou}[56]==21 or ${'mem'.$kou}[57]==21 or ${'mem'.$kou}[58]==21){
				${'dmg'.$ddd} += (${'mem'.$kou}[15]-${'mem'.$kou.'hp_flg'});
			}
		#���v��
			if (${'mem'.$kou}[55]==78 or ${'mem'.$kou}[56]==78 or ${'mem'.$kou}[57]==78 or ${'mem'.$kou}[58]==78){
				if($i>19){${'dmg'.$ddd} *= 8;}
			}
		#�{�X�L���[�A�N�X
			if ($on and $on ==$place and ${'mem'.$kou}[24]==1323){
				${'dmg'.$ddd} *= 44;
			}
		#�N���E������
			if(${'mem'.$kou}[69]==1){
				if(${'mem'.$kou}[65]>=70 or ${'mem'.$kou}[65]<=30){
					${'dmg'.$ddd} = int(${'dmg'.$ddd} * (${'mem'.$kou}[65]-50)/20);
				}
			}
			if(${'mem'.$kou}[69]==2){
				if(${'mem'.$kou}[64]>=70 or ${'mem'.$kou}[64]<=30){
					${'dmg'.$ddd} = int(${'dmg'.$ddd} * (${'mem'.$kou}[64]-50)/20);
				}
			}
		#�E�C���X
			if(${'mem'.$kou}[24]==1081 and int(rand(4))==0){
				${'com'.$ddd} .= "<font color=\"red\" size=3>${'mem'.$kou}[4]�́A��s���N�������I</font>";
				${'dmg'.$ddd}-=${'dmg'.$ddd}*2;
			}
		#10��
			if(${'mem'.$kou.'item'}[1]==5 and ${'mem'.$kou.'item'}[0] eq "10����"){
				${'dmg'.$ddd}=1000000000;
			}
		}
		#�}�e���A
			if (${'mem'.$kou}[24]==1400){
			#�Ή��̃}�e���A
				if (${'mem'.$kou.'item'}[31]==1 or ${'mem'.$kou.'item'}[32]==1){
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*1.2);
				}
				if (${'mem'.$kou.'item'}[31]==101 or ${'mem'.$kou.'item'}[32]==101){
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*1.5);
				}
				if (${'mem'.$kou.'item'}[31]==201 or ${'mem'.$kou.'item'}[32]==201){
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*2);
				}
			#�����̃}�e���A
				if (${'mem'.$kou.'item'}[31]==9 or ${'mem'.$kou.'item'}[32]==9){
					${'mem'.$kou.'hit_ritu'}=${'mem'.$kou.'hit_ritu'}*2;
				}
				if (${'mem'.$kou.'item'}[31]==109 or ${'mem'.$kou.'item'}[32]==109){
					${'mem'.$kou.'hit_ritu'}=${'mem'.$kou.'hit_ritu'}*3;
				}
				if (${'mem'.$kou.'item'}[31]==209 or ${'mem'.$kou.'item'}[32]==209){
					${'mem'.$kou.'hit_ritu'}=${'mem'.$kou.'hit_ritu'}*4;
				}
			#�]���̃}�e���A
				if (${'mem'.$kou.'item'}[33]==10 or ${'mem'.$kou.'item'}[34]==10){
					${'mem'.$kou.'hp_flg'} = int(${'mem'.$kou.'hp_flg'}/10);
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*1.5);
				}
				if (${'mem'.$kou.'item'}[33]==110 or ${'mem'.$kou.'item'}[34]==110){
					${'mem'.$kou.'hp_flg'} = int(${'mem'.$kou.'hp_flg'}/1000);
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*2);
				}
				if (${'mem'.$kou.'item'}[33]==210 or ${'mem'.$kou.'item'}[34]==210){
					${'mem'.$kou.'hp_flg'} = int(${'mem'.$kou.'hp_flg'}/10000);
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*2.5);
				}
				if (${'mem'.$kou.'item'}[33]==310 or ${'mem'.$kou.'item'}[34]==310){
					${'mem'.$kou.'hp_flg'} = int(${'mem'.$kou.'hp_flg'}/100000);
					${'dmg'.$ddd} = int(${'dmg'.$ddd}*3);
				}
			#�G�A���̃}�e���A
				if (${'mem'.$kou.'item'}[37]%100==12 or ${'mem'.$kou.'item'}[38]%100==12){
					if(${'mem'.$kou.'item'}[37]%100==12){
						$sakep = 1+int(${'mem'.$kou.'item'}[37]/100+1)*0.2;
					}else{  $sakep = 1+int(${'mem'.$kou.'item'}[38]/100+1)*0.2; }
					$ssake1= int($ssake1 / $sakep);
					$ssake2= int($ssake2 / $sakep);
					$ssake3= int($ssake3 / $sakep);
					$ssake4= int($ssake4 / $sakep);
				}
			}
	}
	if($chara[39]){
		# �y�b�g�_���[�W�v�Z
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
		$com4 = "$pename�̍U���I";
	
		$dmg4 = $chara[44];
	}

	#��������E�������
	if ($chara[55]==80 or $chara[56]==80 or $chara[57]==80 or $chara[58]==80){
		$mem1hit_ritu=$mem1hit_ritu*100;
		$smem1hit_ritu=$smem1hit_ritu*100;
	}
	if ($chara[55]==81 or $chara[56]==81 or $chara[57]==81 or $chara[58]==81){
		$sake1=$sake1*10;
		$ssake1=$ssake1*10;
	}

}

#------------------#
#�@����҂̕K�E�Z�@#
#------------------#
sub tyosenwaza {

	$waza_ritu1 = int(rand($chara[11] / 10)) + 10;
	if($waza_ritu1 > 80){$waza_ritu1 = 80;}
	if($chara[31]=="0055" and $i<31 and $waza_ritu1 > 20){$waza_ritu1 -= 20;}
	$waza_ritu2 = int(rand($mem1[11] / 10)) + 10;
	if($waza_ritu2 > 80){$waza_ritu2 = 80;}
	$waza_ritu3 = int(rand($mem2[11] / 10)) + 10;
	if($waza_ritu3 > 80){$waza_ritu3 = 80;}
	$waza_ritu4 = 10;

	if ($waza_ritu1 > int(rand(100))) {
		$com1 .= "<font color=\"$red\" size=5>�N���e�B�J���I�I�u$chara[23]�v</font><br>";
		if($chara[30]==2000 or $chara[30]==3000){$dmg1 = $dmg1 * 4;}
		else{$dmg1 = $dmg1 * 2;}
	}
	if ($waza_ritu2 > int(rand(100))) {
		$com2 .= "<font color=\"$red\" size=5>�N���e�B�J���I�I�u$mem1[23]�v</font><br>";
		if($mem1[30]==2000 or $mem1[30]==3000){$dmg2 = $dmg2 * 4;}
		else{$dmg2 = $dmg2 * 2;}
	}
	if ($waza_ritu3 > int(rand(100))) {
		$com3 .= "<font color=\"$red\" size=5>�N���e�B�J���I�I�u$mem2[23]�v</font><br>";
		if($mem2[30]==2000 or $mem2[30]==3000){$dmg3 = $dmg3 * 4;}
		else{$dmg3 = $dmg3 * 2;}
	}
	if ($waza_ritu4 > int(rand(100))) {
		$com4 .= "<font color=\"$red\" size=5>�N���e�B�J���I�I</font><br>";
		$dmg4 = $dmg4 * 2;
	}

	$k = 0;$ab = 1;$sab=0;
	$ghissatu=999;
	if($chara[55]!=65 and $chara[56]!=65 and $chara[57]!=65 and $chara[58]!=65){
	for($his=51;$his<55;$his++){
		if($his==51 and $chara[31]=="0055" and $i>30 and int(rand(5))==0){
		}elsif($his==51 and $item[3] eq "���~�b�^�["){
			if($limiter!=1 and $khp_flg > 0 and $chara[$his]){
				$hissatu1="hissatu$chara[$his]";
				require "./tech/$chara[$his].pl";
				&$hissatu1;
				$limiter=1;
			}
		}elsif ($k!=1 and $khp_flg > 0 and $chara[$his]) {
			$hissatu1="hissatu$chara[$his]";
			require "./tech/$chara[$his].pl";
			&$hissatu1;
			if($k==1){$ghissatu=$chara[$his];}
		}
	}
	}
	if($chara[24]==1400){
	if($item[31]%100==5 and int($item[31]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($item[32]%100==5 and int($item[32]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($item[33]%100==6 and $i==1 and !$whp_flg){
		$sendmg=int($dmg1/(4-int($item[33]/100)));
		if($akumakai==1){$sendmg=int($sendmg/10000);}
		$smem1hp_flg-=$sendmg;
		$com1.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($item[34]%100==6 and $i==1 and !$whp_flg){
		$sendmg=int($dmg1/(4-int($item[34]/100)));
		if($akumakai==1){$sendmg=int($sendmg/10000);}
		$smem1hp_flg-=$sendmg;
		$com1.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($item[33]%100==2 and $i==1){
		$dmg1=int($dmg1*int($item[33]/100+2));
		$com1.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($item[34]%100==2 and $i==1){
		$dmg1=int($dmg1*int($item[34]/100+2));
		$com1.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($item[37]%100==8 and int($item[37]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($item[38]%100==8 and int($item[38]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($item[37]%100==4 and $i==1){
		$mons_ritu1-=int($item[37]/100+1)*10;
	}
	if($item[38]%100==4 and $i==1){
		$mons_ritu1-=int($item[38]/100+1)*10;
	}
	}
	$k = 0;$ab = 2;
	if($mem1[55]!=65 and $mem1[56]!=65 and $mem1[57]!=65 and $mem1[58]!=65){
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem1hp_flg > 0 and $mem1[$his]) {
			$hissatu2="hissatu$mem1[$his]";
			require "./tech/$mem1[$his].pl";
			&$hissatu2;
		}
	}
	}
	if($mem1[24]==1400){
	if($mem1item[31]%100==5 and int($mem1item[31]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem1item[32]%100==5 and int($mem1item[32]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem1item[33]%100==6 and $i==1){
		$sendmg=int($dmg2/(4-int($mem1item[33]/100)));
		$smem1hp_flg-=$sendmg;
		$com2.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem1item[34]%100==6 and $i==1){
		$sendmg=int($dmg2/(4-int($mem1item[34]/100)));
		$smem1hp_flg-=$sendmg;
		$com2.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem1item[33]%100==2 and $i==1){
		$dmg2=int($dmg2*int($mem1item[33]/100+2));
		$com2.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem1item[34]%100==2 and $i==1){
		$dmg2=int($dmg2*int($mem1item[34]/100+2));
		$com2.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem1item[37]%100==8 and int($mem1item[37]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem1item[38]%100==8 and int($mem1item[38]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem1item[37]%100==4 and $i==1){
		$mons_ritu1-=int($mem1item[37]/100+1)*5;
	}
	if($mem1item[38]%100==4 and $i==1){
		$mons_ritu1-=int($mem1item[38]/100+1)*5;
	}
	}
	$k = 0;$ab = 3;
	if($mem2[55]!=65 and $mem2[56]!=65 and $mem2[57]!=65 and $mem2[58]!=65){
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem2hp_flg > 0 and $mem2[$his]) {
			$hissatu3="hissatu$mem2[$his]";
			require "./tech/$mem2[$his].pl";
			&$hissatu3;
		}
	}
	}
	if($mem2[24]==1400){
	if($mem2item[31]%100==5 and int($mem2item[31]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem2item[32]%100==5 and int($mem2item[32]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem2item[33]%100==6 and $i==1){
		$sendmg=int($dmg3/(4-int($mem2item[33]/100)));
		$smem1hp_flg-=$sendmg;
		$com3.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem2item[34]%100==6 and $i==1){
		$sendmg=int($dmg3/(4-int($mem2item[34]/100)));
		$smem1hp_flg-=$sendmg;
		$com3.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem2item[33]%100==2 and $i==1){
		$dmg3=int($dmg3*int($mem2item[33]/100+2));
		$com3.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem2item[34]%100==2 and $i==1){
		$dmg3=int($dmg3*int($mem2item[34]/100+2));
		$com3.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem2item[37]%100==8 and int($mem2item[37]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem2item[38]%100==8 and int($mem2item[38]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem2item[37]%100==4 and $i==1){
		$mons_ritu1-=int($mem2item[37]/100+1)*5;
	}
	if($mem2item[38]%100==4 and $i==1){
		$mons_ritu1-=int($mem2item[38]/100+1)*5;
	}
	}
	$k = 0;$ab = 4;
	if($mem3[55]!=65 and $mem3[56]!=65 and $mem3[57]!=65 and $mem3[58]!=65){
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem3hp_flg > 0 and $mem3[$his]) {
			$hissatu4="hissatu$mem3[$his]";
			require "./tech/$mem3[$his].pl";
			&$hissatu4;
		}
	}
	}
	if($mem3[24]==1400){
	if($mem3item[31]%100==5 and int($mem3item[31]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem3item[32]%100==5 and int($mem3item[32]/10+10)>int(rand(100))){
		require "./tech/18.pl";
		&hissatu18;
	}
	if($mem3item[33]%100==6 and $i==1){
		$sendmg=int($dmg4/(4-int($mem3item[33]/100)));
		$smem1hp_flg-=$sendmg;
		$com4.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem3item[34]%100==6 and $i==1){
		$sendmg=int($dmg4/(4-int($mem3item[34]/100)));
		$smem1hp_flg-=$sendmg;
		$com4.="<font class=\"red\" size=5>�搧�U���I�I</font><font class=\"yellow\" size=5>$sendmg</font><br>";
	}
	if($mem3item[33]%100==2 and $i==1){
		$dmg4=int($dmg4*int($mem3item[33]/100+2));
		$com4.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem3item[34]%100==2 and $i==1){
		$dmg4=int($dmg4*int($mem3item[34]/100+2));
		$com4.="<font class=\"red\" size=5>�L�[�b�N�I�I</font><br>";
	}
	if($mem3item[37]%100==8 and int($mem3item[37]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem3item[38]%100==8 and int($mem3item[38]/10+10)>int(rand(100))){
		require "./tech/47.pl";
		&hissatu47;
	}
	if($mem3item[37]%100==4 and $i==1){
		$mons_ritu1-=int($mem3item[37]/100+1)*5;
	}
	if($mem3item[38]%100==4 and $i==1){
		$mons_ritu1-=int($mem3item[38]/100+1)*5;
	}
	}
	if ($k!=1) {require "./tech/0.pl";}
	if ($mem3hp_flg>0){&phissatu;}

	if($item[0] eq "�d���A�W�A"){$staisyo1=4;}
	if($mem1item[0] eq "�d���A�W�A"){$staisyo2=4;}
	if($mem2item[0] eq "�d���A�W�A"){$staisyo3=4;}
	if($mem3item[0] eq "�d���A�W�A"){$staisyo4=4;}

	if($hpplus1 > 0){$kaihuku1="$hpplus1�̉񕜁�";}
	if($hpplus2 > 0){$kaihuku2="$hpplus2�̉񕜁�";}
	if($hpplus3 > 0){$kaihuku3="$hpplus3�̉񕜁�";}
	if($hpplus4 > 0){$kaihuku4="$hpplus4�̉񕜁�";}
}
#------------------#
#�@���x���A�b�v  �@#
#------------------#
sub levelup {

	if($in{'mode'} eq "guild_battle"){
		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[66] and $array[2] > $array[3] * 1500000){
				$comment .= "<font class=red size=7>�M���h���x�����オ�����I</font><br>";
				$array[3] += 1;
				$array[2] = 0;
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

	#���Ȃ�20���x�ɂ��邱�Ƃő��i����
	if ($chara[38]>3000 and $chara[38]<3100 and $chara[40] > $chara[41]){$chara[46]=20;}
	elsif ($chara[38]>3000 and $chara[40] > $chara[41]) {
		#�y�b�g���x���A�b�v
		if($chara[46] < 20 or $chara[38] > 3400){
		while($chara[40] > $chara[41] and $chara[46]<1000 and $chara[46] < $chara[18] and ($plvup + $chara[46])<=1000){
			$chara[40] = $chara[40] - $chara[41];
			$plvup += 1;
			if(!$chara[49]){$chara[49]=1;}
			if(!$chara[46]){$chara[46]=1;}
			$chara[41] = $chara[41] + int($chara[41] / $chara[46]) + 100 * int ($chara[49] / 4);
			$chara[46] += 1;
			$chara[43] = $chara[43] + int(rand($chara[46]) * 15);
			$chara[44] = $chara[44] + int(rand($chara[46]) * 5);
			if($chara[31]=="0048"){
				$chara[43] += int(rand($chara[43]/200));
				$chara[44] += int(rand($chara[44]/100));
			}
		}
		}
		if ($plvup != 0){
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	$comment .= "<font class=red size=7>$pename�̃��x����$plvup�オ�����I</font><br>";
			if ($chara[46] > 19 and $chara[38] < 3400) { $chara[46]=20; }
			elsif($chara[46] >1000){$chara[46]=1000;}
			if($chara[46]==1000){
			$tamas=$chara[38]-3200;
	$comment .= "<font class=red size=7>$chara[39]�̍�����ɓ��ꂽ�I</font><br>";
				$chara[$tamas]=1;
			}
			$chara[42] = $chara[43];
		}
	}

	#�y�b�g�i��
	if ($chara[38]>3000 and $chara[46]>=20){
	#�i���撲��
		open(IN,"$pet_sinka");
		@sinka_array = <IN>;
		close(IN);
		foreach(@sinka_array){
		($i_no,$i_noa,$i_nob,$i_noc,$i_nod) = split(/<>/);
		if($chara[38] eq "$i_no") { $shit=1;last;}
		}
		if($shit) {
	#�i����̌�����
		$sinkasaki=0;
		if ($i_noa != 0){$sinkasaki+=1;}
		if ($i_nob != 0){$sinkasaki+=1;}
		if ($i_noc != 0){$sinkasaki+=1;}
		if ($i_nod != 0){$sinkasaki+=1;}
			if ($sinkasaki > 0){
	#�i����̌���
		$sinkano=int(rand($sinkasaki));
		if($sinkano==0){$item_no=$i_noa;}
		if($sinkano==1){$item_no=$i_nob;}
		if($sinkano==2){$item_no=$i_noc;}
		if($sinkano==3){$item_no=$i_nod;}
	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);
	foreach(@item_array){
	($i_no,$pi_name,$i_gold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
	if($item_no eq "$i_no") { $ihit=1;last; }
	}
	if(!$ihit) { &error("����ȃA�C�e���͑��݂��܂���"); }
		if($chara[38] < $i_no){
		$comment .= "<font class=red size=7>�y�b�g��$pi_name�ɐi�������I�I</font><br>";
		$chara[41] = $i_exp;
		}
		if($chara[38] > $i_no){
		$comment .= "<font class=red size=7>�y�b�g��$pi_name�ɑމ������c</font><br>";
		$chara[41] = int($i_exp/2);
		}
		$chara[38] = $i_no;
		$chara[39] = $pi_name;
		$chara[40] = 0;
		$chara[43] = int(rand($chara[42])/10)+$i_hp;
		$chara[42] = $chara[43];
		$chara[44] = int(rand($chara[44])/10)+$i_damage;
		$chara[45] = $i_image;
		$chara[46] = 1;
		$chara[47] = $ps;
		$chara[49] += 1;
			}
		}
	}
	if ($chara[18] < $charamaxlv or $chara[70]>=1) {
		if($chara[70]<1){
			while ($chara[17] >= $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50)) {
				$chara[17] -= $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50);
				$lvup += 1;
				if(!$chara[35]){$chara[35]=0;}
				$chara[35] += 4;
				$chara[18] += 1;
				$hpup = 400;
				$chara[16] = $chara[16] + $hpup;
			}
		}else{
			while ($chara[17] >= $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10) {
				$chara[17] -= $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;
				$lvup += 1;
				if(!$chara[35]){$chara[35]=0;}
				$chara[35] += 4;
				$chara[18] += 1;
				if($chara[18]<100){$hpup = 300;}
				elsif($chara[18]<200){$hpup = 500;}
				elsif($chara[18]<500){$hpup = 800;}
				elsif($chara[18]<1000){$hpup = 1000;}
				elsif($chara[18]<2000){$hpup = 1200;}
				else{$hpup = 1500;}
				$chara[16] = $chara[16] + $hpup;
			}
		}

		if ($lvup != 0){
			$comment .= "<font class=red size=7>���x����$lvup�オ�����I</font><br>";
			$klvbf = $chara[33];
			$chara[33] += $lvup;
			#�W���u�}�X�^�[�̏���
			if ($chara[33] > 99 && $klvbf <=99) {
				$comment .= "<font class=red size=5>$chara_syoku[$chara[14]]���}�X�^�[�����I�I</font><br>";
				$lock_file = "$lockfolder/syoku$in{'id'}.lock";
				&lock($lock_file,'SK');
				&syoku_load;

				$syoku_master[$chara[14]] = 100;

				&syoku_regist;
				&unlock($lock_file,'SK');
			}
			if ($chara[33] > 100) { $chara[33]=100; }

			$chara[15] = $chara[16];
		}
	}
}

#----------------#
# �E�Ə����ݏ��� #
#----------------#
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

#------------------#
#���A�N�Z�T���[����#
#------------------#
sub acs_waza {

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

#----------------------#
#�@�ΐ푊��f�[�^�Ǒց@#
#----------------------#
# �L�����f�[�^��@winner_data�ɑ�����Ă���Ăяo����@winner�ɕϊ����܂�
sub winner_data {

	open(IN,"./item/$winner_data[0].cgi");
	$witem_log = <IN>;
	close(IN);

	@witem = split(/<>/,$witem_log);

	@winner = ($winner_data[0],$winner_data[2],$winner_data[3],$winner_data[4],$winner_data[5],$winner_data[6],$winner_data[7],$winner_data[8],$winner_data[9],$winner_data[10],$winner_data[11],$winner_data[12],$winner_data[13],$winner_data[20],$winner_data[14],$winner_data[15],$winner_data[16],$winner_data[18],$winner_data[21],$winner_data[22],$winner_data[23],$witem[0],$witem[1],$witem[2],$witem[3],$witem[4],$witem[5],$witem[6],$witem[8],$witem[9],$witem[10],$witem[11],$witem[12],$witem[13],$witem[15],$witem[17],$witem[18],$winner_data[30],$winner_data[26],$winner_data[33]);

	$winner[51] = $witem[7];
	$winner[52] = $witem[16];
	$winner[53] = $witem[14];
}
#------------------------#
#�@����������\�̓A�b�v  #
#------------------------#
sub item_u {

$itemmaxlv = 10;
$defmaxlv = 10;

	if($item[20] < $itemmaxlv and $chara[24] and $chara[24]>0 and $chara[24]<4000){
		$item[21] += int(rand($place+1));
	}
	if($item[22] < $defmaxlv and $chara[29] and $chara[29]>0 and $chara[29]<4000){
		$item[23] += int(rand($place+1));
	}

	if ($item[21] >= int(rand(($item[20]+1) * 100) + 20*int($item[20]))) {
		$comment .= "<font class=red size=6>$item[0]���g������ċ����Ȃ����I�I</font><br>";
		if($item[20]==9){
			$item[1] = $item[1] + 6; 
			$item[2] = $item[2] + 2;
			$item[20] += 1;
			$item[21] = 0;
		}else{
			$item[1] = $item[1] + 1; 
			$item[2] =$item[2] + 2;
			$item[20] += 1;
			$item[21] = 0;
		}
	}

	if ($item[23] >= int(rand(($item[22]+1) * 100) + 20*int($item[22]))) {
		$comment .= "<font class=red size=6>$item[3]���g������ċ����Ȃ����I�I</font><br>";
		if($item[22]==9){
			$item[4] = $item[4] + 6; 
			$item[5] =$item[5] + 2;
			$item[22] += 1;
			$item[23] = 0;
		}else{
		$item[4] = $item[4] + 1; 
		$item[5] =$item[5] + 2;
		$item[22] += 1;
		$item[23] = 0;
		}
	}
}
#----------------------------#
#�@�A�C�e���t�@�C���������݁@#
#----------------------------#
sub item_regist {

	$new_item = "";
	foreach(@item){
		$new_item .="$_<>";
	}
	open(OUT,">./item/$chara[0].cgi"); 
	print OUT $new_item; 
	close(OUT);

}
sub egg_lose {
	$chara[38] = 3000;
	$chara[39] = "��ꂽ��";
	$chara[40] = 0;
	$chara[41] = 0;
	$chara[42] = 0;
	$chara[43] = 0;
	$chara[44] = 0;
	$chara[45] = 0;
	$chara[46] = 0;
	$chara[47] = 0;
}
sub egg_egg {
	$comment .= "<b><font size=4 color=red>�G�b�O���E�����I�I</font></b><br>";
	$php_flg = 300;
	$chara[38] = 3003;
	$chara[39] = "�G�b�O";
	$chara[40] = 0;
	$chara[41] = 300000;
	$chara[42] = 300;
	$chara[43] = 300;
	$chara[44] = 0;
	$chara[45] = 2;
	$chara[46] = 1;
	$chara[47] = 0;
}
sub pet_get {
	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($phi_no,$phi_name,$phi_gold,$phi_exp,$phi_hp,$phi_damage,$phi_image,$ps) = split(/<>/);
		if($ssmname1 eq $phi_name) { $hit=1;last; }
	}
	if($hit and $chara[38]<3000 and $chara[70]>=1 and $chara[19] > $phi_gold) {
		if($phi_name eq "�I�[�K" and $i <10){
		}elsif($phi_name eq "�x��2"){
		}elsif($phi_name eq "�V�^�E�C���X2"){
		}elsif($phi_name eq "�V�^�E�C���X3"){
		}elsif($phi_name eq "���~�r��" and $i<6){
		}elsif($phi_name eq "�M�K���g�I�[�N"){
		}elsif($phi_name eq "�����R�c��" and $i>1){
		}elsif($phi_gold <= 300000000 and $phi_gold > 0){
			$comment .= "<b><font size=4 color=red>$phi_name��ߊl�����I�I</font></b><br>";
			$chara[19] = $chara[19] - $phi_gold;
			$chara[38] = $phi_no;
			$chara[39] = $phi_name;
			$chara[40] = 0;
			$chara[41] = $phi_exp;
			$chara[42] = $phi_hp;
			$chara[43] = $phi_hp;
			$chara[44] = $phi_damage;
			$chara[45] = $phi_image;
			$chara[46] = 1;
			$chara[47] = $ps;
		}
	}
}
1;
