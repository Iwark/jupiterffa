sub hissatu39{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 6);
					${'mem'.$ab.'hit_ritu'}-=80;
					${'com'.$ab} .="<font class=\"yellow\" size=5>•KE‹Z‘S’eŠJ•úIII</font>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 6);
					${'mem'.$ab.'hit_ritu'}-=80;
					${'com'.$ab} .="<font class=\"yellow\" size=5>•KE‹Z‘S’eŠJ•úIII</font>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 6);
				${'smem'.$sab.'hit_ritu'}-=80;
				${'scom'.$sab} .="<font class=\"yellow\" size=5>•KE‹Z‘S’eŠJ•úIII</font>";
			}
		}
	}
}
sub atowaza{}
1;