sub hissatu83{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(8000))){
					if(int(rand(10))<8){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*102));
					${'dmg'.$ab} = int(${'dmg'.$ab} * 102);
					${'com'.$ab} .="<font class=\"yellow\" size=6>‰œ‹`‚P‚O‚P•C‚í‚ñ‚¿‚á‚ñIII</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(8000))){
					if(int(rand(10))<8){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*102));
					${'dmg'.$ab} = int(${'dmg'.$ab} * 102);
					${'com'.$ab} .="<font class=\"yellow\" size=6>‰œ‹`‚P‚O‚P•C‚í‚ñ‚¿‚á‚ñIII</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(8000))){
				if(int(rand(10))<8){
				$k=1;
				${'smem'.$sab.'hit_ritu'}+=int(rand(${'smem'.$sab.'hit_ritu'}*102));
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 102);
				${'scom'.$sab} .="<font class=\"yellow\" size=6>‰œ‹`‚P‚O‚P•C‚í‚ñ‚¿‚á‚ñIII</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;