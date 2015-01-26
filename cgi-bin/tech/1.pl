sub hissatu1{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 1.5);
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‹¥a‚èIII</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>‰ïS‚ÌˆêŒ‚II</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 1.5);
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‹¥a‚èIII</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 1.5);
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z‹¥a‚èIII</font><br>";
			}
		}
	}
}
sub atowaza{}
1;