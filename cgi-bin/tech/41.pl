sub hissatu41{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技調合！！！</font><br>";
					if($chara[19]>1000000000){
						${'com'.$ab} .="<font class=\"red\" size=5>10億Gドープ!!</font><br>";
						$chara[19]-=1000000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 98);
					}elsif($chara[19]>100000000){
						${'com'.$ab} .="<font class=\"red\" size=5>1億Gドープ!!</font><br>";
						$chara[19]-=100000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 30);
					}elsif($chara[19]>10000000){
						${'com'.$ab} .="<font class=\"red\" size=5>1000万Gドープ!!</font><br>";
						$chara[19]-=10000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 10);
					}elsif($chara[19]>1000000){
						${'com'.$ab} .="<font class=\"red\" size=5>100万Gドープ!!</font><br>";
						$chara[19]-=1000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
					}elsif($chara[19]>100000){
						${'com'.$ab} .="<font class=\"red\" size=5>10万Gドープ!!</font><br>";
						$chara[19]-=100000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 1.5);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技調合！！！</font><br>";
					if(${'mem'.$ri}[19]>10000000){
						${'com'.$ab} .="<font class=\"red\" size=5>1000万Gドープ!!</font><br>";
						${'mem'.$ri}[19]-=10000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 10);
					}elsif(${'mem'.$ri}[19]>1000000){
						${'com'.$ab} .="<font class=\"red\" size=5>100万Gドープ!!</font><br>";
						${'mem'.$ri}[19]-=1000000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
					}elsif(${'mem'.$ri}[19]>100000){
						${'com'.$ab} .="<font class=\"red\" size=5>10万Gドープ!!</font><br>";
						${'mem'.$ri}[19]-=100000;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 1.5);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技調合！！！</font><br>";
				if(${'smem'.$sab}[19]>10000000){
					${'scom'.$sab} .="<font class=\"red\" size=5>1000万Gドープ!!</font><br>";
					${'smem'.$sab}[19]-=10000000;
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 10);
				}elsif(${'smem'.$sab}[19]>1000000){
					${'scom'.$sab} .="<font class=\"red\" size=5>100万Gドープ!!</font><br>";
					${'smem'.$sab}[19]-=1000000;
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 5);
				}elsif(${'smem'.$sab}[19]>100000){
					${'scom'.$sab} .="<font class=\"red\" size=5>10万Gドープ!!</font><br>";
					${'smem'.$sab}[19]-=100000;
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 3);
				}
			}
		}
	}
}
sub atowaza{}
1;