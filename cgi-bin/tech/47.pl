sub hissatu47{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if(int(rand(3))==0){$sdmg1=0;}
					if(int(rand(3))==0){$sdmg2=0;}
					if(int(rand(3))==0){$sdmg3=0;}
					if(int(rand(3))==0){$sdmg4=0;}
					$taisyo1=$ab-1;$taisyo2=$ab-1;$taisyo3=$ab-1;$taisyo4=$ab-1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺マイティガード！！！</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(int(rand(3))==0){$sdmg1=0;}
					if(int(rand(3))==0){$sdmg2=0;}
					if(int(rand(3))==0){$sdmg3=0;}
					if(int(rand(3))==0){$sdmg4=0;}
					$taisyo1=$ab-1;$taisyo2=$ab-1;$taisyo3=$ab-1;$taisyo4=$ab-1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺マイティガード！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				if(int(rand(3))==0){$dmg1=0;}
				if(int(rand(3))==0){$dmg2=0;}
				if(int(rand(3))==0){$dmg3=0;}
				if(int(rand(3))==0){$dmg4=0;}
				$staisyo1=$sab-1;$staisyo2=$sab-1;$staisyo3=$sab-1;$staisyo4=$sab-1;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺マイティガード！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;