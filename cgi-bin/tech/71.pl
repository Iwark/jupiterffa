sub hissatu71{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*100));
					$sake1 += 1000;
					$sake2 += 1000;
					$sake3 += 1000;
					$sake4 += 1000;
					${'com'.$ab} .="<font class=\"red\" size=5>吹雪！！！</font><br>";
					$dmgplus = 20 + int(rand(80));
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*100));
					$sake1 += 1000;
					$sake2 += 1000;
					$sake3 += 1000;
					$sake4 += 1000;
					${'com'.$ab} .="<font class=\"red\" size=5>吹雪！！！</font><br>";
					$dmgplus = 20 + int(rand(80));
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hit_ritu'}+=int(rand(${'smem'.$sab.'hit_ritu'}*100));
				$ssake1 += 1000;
				$ssake2 += 1000;
				$ssake3 += 1000;
				$ssake4 += 1000;
				${'scom'.$sab} .="<font class=\"red\" size=5>吹雪！！！</font><br>";
				$dmgplus = 20 + int(rand(80));
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
			}
		}
	}
}
sub atowaza{}
1;