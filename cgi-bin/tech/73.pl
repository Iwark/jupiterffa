sub hissatu73{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*500));
					$sake1 += 5000;
					$sake2 += 5000;
					$sake3 += 5000;
					$sake4 += 5000;
					${'com'.$ab} .="<font class=\"red\" size=5>鬼圧！！！</font><br>";
					$dmgplus = 10 + int(rand(40)) + $oni*10;
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					$oni+=1;
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*1000));
					$sake1 += 5000;
					$sake2 += 5000;
					$sake3 += 5000;
					$sake4 += 5000;
					${'com'.$ab} .="<font class=\"red\" size=5>鬼圧！！！</font><br>";
					$dmgplus = 10 + int(rand(40)) + $oni*10;
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					$oni+=1;
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hit_ritu'}+=int(rand(${'smem'.$sab.'hit_ritu'}*1000));
				$ssake1 += 5000;
				$ssake2 += 5000;
				$ssake3 += 5000;
				$ssake4 += 5000;
				${'scom'.$sab} .="<font class=\"red\" size=5>鬼圧！！！</font><br>";
				$dmgplus = 10 + int(rand(40)) + $oni*10;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
				$oni+=1;
			}
		}
	}
}
sub atowaza{}
1;