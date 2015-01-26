sub hissatu54{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					${'sake'.$ab} +=40;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹ZŠïPIII</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					${'sake'.$ab} +=40;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹ZŠïPIII</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 3);
				${'ssake'.$sab} +=40;
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹ZŠïPIII</font><br>";
			}
		}
	}
}
sub atowaza{}
1;