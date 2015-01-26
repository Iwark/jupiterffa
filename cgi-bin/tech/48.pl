sub hissatu48{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'hpplus'.$ab} = int(${'dmg'.$ab}/50);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技聖なる審判！！！</font><br>";
					if($item[0] eq "聖剣サラダ"){
						${'hpplus'.$ab} = int(${'dmg'.$ab}/2);
						${'com'.$ab} .="<font class=\"yellow\" size=5>サラダ！！</font>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'hpplus'.$ab} = int(${'dmg'.$ab}/50);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技聖なる審判！！！</font><br>";
					if(${'mem'.$ri.'item'}[0] eq "聖剣サラダ"){
						${'hpplus'.$ab} = int(${'dmg'.$ab}/2);
						${'com'.$ab} .="<font class=\"yellow\" size=5>サラダ！！</font>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'shpplus'.$sab} = int(${'sdmg'.$sab}/50);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技聖なる審判！！！</font><br>";
				if(${'smem'.$sab.'item'}[0] eq "聖剣サラダ"){
					${'shpplus'.$sab} = int(${'sdmg'.$sab}/2);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>サラダ！！</font>";
				}
			}
		}
	}
}
sub atowaza{}
1;