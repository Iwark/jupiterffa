sub hissatu70{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if(int(rand(5))!=0){
						$dmg1 = -$dmg1;
						$dmg2 = -$dmg2;
						$dmg3 = -$dmg3;
						$dmg4 = -$dmg4;
						$sdmg1 = -$sdmg1;
						$sdmg2 = -$sdmg2;
						$sdmg3 = -$sdmg3;
						$sdmg4 = -$sdmg4;
						${'com'.$ab} .="<font class=\"red\" size=5>…明るい未来を作る！</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(int(rand(5))!=0){
						$dmg1 = -$dmg1;
						$dmg2 = -$dmg2;
						$dmg3 = -$dmg3;
						$dmg4 = -$dmg4;
						$sdmg1 = -$sdmg1;
						$sdmg2 = -$sdmg2;
						$sdmg3 = -$sdmg3;
						$sdmg4 = -$sdmg4;
						${'com'.$ab} .="<font class=\"red\" size=5>…明るい未来を作る！</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				if(int(rand(5))!=0){
					$dmg1 = -$dmg1;
					$dmg2 = -$dmg2;
					$dmg3 = -$dmg3;
					$dmg4 = -$dmg4;
					$sdmg1 = -$sdmg1;
					$sdmg2 = -$sdmg2;
					$sdmg3 = -$sdmg3;
					$sdmg4 = -$sdmg4;
					${'scom'.$sab} .="<font class=\"red\" size=5>…明るい未来を作る！</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;