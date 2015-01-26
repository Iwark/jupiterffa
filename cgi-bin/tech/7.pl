sub hissatu7{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技盗む！！！</font><br>";
					$k=1;
					$dmg1 = 0;
					$drop_plus += 1;
					$ahit=0;
					if($place==0){$pp=1;}
					elsif($place==1){$pp=2;}
					elsif($place==2){$pp=3;}
					elsif($place==3){$pp=4;}
					elsif($place==4){$pp=5;}
					elsif($place==5){$pp=6;}
					elsif($place==6){$pp=7;}
					elsif($place==7){$pp=8;}
					elsif($place==8){$pp=9;}
					elsif($place==9){$pp=10;}
					else{$ahit=1;}
					if($ahit!=1){
						if($on and $on==$place and $name eq "エッグエンジェル"){
						if($chara[91] == 1){$item_no = 16;$chara[91]=2;&itemdrop;}
						elsif(int(rand($sdrop*4)) == 0){$item_no = 16;&itemdrop;}
						}
			elsif($on and $on==$place and int(rand($sdrop*4)) == 0){$item_no = int(rand(15));&itemdrop;}
			elsif(int(rand($adrop/$drop_plus*$pp))==0){$item_no = int(rand(5)+11);&itemdrop;}
			elsif(int(rand($bdrop/$drop_plus*$pp))==0){$item_no = int(rand(5)+6);&itemdrop;}
			elsif(int(rand($cdrop/$drop_plus*$pp))==0){$item_no = int(rand(5)+1);&itemdrop;}
						if($ssmname1 eq "エッグ" and int(rand(15))==0 and $chara[18]>60){
							if($chara[38]<3001){
					$com1 .= "<b><font size=4 color=red>エッグを盗んだ！！</font></b><br>";
							$php_flg = 300;
							$chara[38] = 3003;
							$chara[39] = "エッグ";
							$chara[40] = 0;
							$chara[41] = 300000;
							$chara[42] = 300;
							$chara[43] = 300;
							$chara[44] = 0;
							$chara[45] = 2;
							$chara[46] = 1;
							$chara[47] = 0;
							}
						}
					}
				if($i_name){$com1 .="<font class=\"yellow\" size=5>$i_nameを盗んだ！！<br>";}
				$i_name="";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = 0;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技盗む！！！</font><br>";
					${'com'.$ab} .="<font class=\"red\" size=5>何か盗めた…のか？</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = 0;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技盗む！！！</font><br>";
				${'com'.$ab} .="<font class=\"red\" size=5>何か盗めた…のか？</font><br>";
			}
		}
	}
}
sub atowaza{}
1;