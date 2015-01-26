sub hissatu72{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300)) and !$whp_flg){
					$k=1;
					if(int(rand(100)) >= int($smem1hp_flg/$smem1hp*100)){
						${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*1000));
						${'com'.$ab} .="<font class=\"red\" size=5>飛龍！！！</font><br>";
						$dmgplus = 200 + int(rand(800));
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}else{
						${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*10));
						${'com'.$ab} .="<font class=\"red\" size=5>飛…！！！(汗)</font><br>";
						$dmgplus = 2 + int(rand(8));
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(int(rand(100)) >= int($smem1hp_flg/$smem1hp*100)){
						${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*1000));
						${'com'.$ab} .="<font class=\"red\" size=5>飛龍！！！</font><br>";
						$dmgplus = 200 + int(rand(800));
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}else{
						${'mem'.$ab.'hit_ritu'}+=int(rand(${'mem'.$ab.'hit_ritu'}*10));
						${'com'.$ab} .="<font class=\"red\" size=5>飛…！！！(汗)</font><br>";
						$dmgplus = 2 + int(rand(8));
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300)) and !$whp_flg){
				$k=1;
				if(int(rand(100)) >= int($mem1hp_flg/$mem1hp*100)){
					${'smem'.$sab.'hit_ritu'}+=int(rand(${'smem'.$sab.'hit_ritu'}*1000));
					${'scom'.$sab} .="<font class=\"red\" size=5>飛龍！！！</font><br>";
					$dmgplus = 200 + int(rand(800));
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
				}else{
					${'smem'.$sab.'hit_ritu'}+=int(rand(${'smem'.$sab.'hit_ritu'}*10));
					${'scom'.$sab} .="<font class=\"red\" size=5>飛…！！！(汗)</font><br>";
					$dmgplus = 2 + int(rand(8));
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
				}
			}
		}
	}
}
sub atowaza{}
1;