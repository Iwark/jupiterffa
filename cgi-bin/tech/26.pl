sub hissatu26{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} += int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
					${'com'.$ab} .="<font class=\"red\" size=5>‘å˜a°‚ªày—ôIII</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>‰ïS‚ÌˆêŒ‚II</font><br>";
					}
					if($item[3] eq "‘å˜a•"){
						${'dmg'.$ab} += int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
						${'com'.$ab} .="<font class=\"red\" size=5>‘å˜a°ày—ôII</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} += int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
					${'com'.$ab} .="<font class=\"red\" size=5>‘å˜a°‚ªày—ôIII</font><br>";
					if(${'mem'.$ri.'item'}[3] eq "‘å˜a•"){
						${'dmg'.$ab} += int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
						${'com'.$ab} .="<font class=\"red\" size=5>‘å˜a°ày—ôII</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} += int(($dmg1+$dmg2+$dmg3+$dmg4) / 4);
				${'scom'.$sab} .="<font class=\"red\" size=5>‘å˜a°‚ªày—ôIII</font><br>";
				if(${'smem'.$sab.'item'}[3] eq "‘å˜a•"){
					${'sdmg'.$sab} += int(($dmg1+$dmg2+$dmg3+$dmg4) / 4);
					${'scom'.$sab} .="<font class=\"red\" size=5>‘å˜a°ày—ôII</font><br>";
				}
			}
		}
	}
}
sub atowaza{
}
1;