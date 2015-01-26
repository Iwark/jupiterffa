sub hissatu60{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>エンジェルキッスッ！</font><br>";
					$dmgplus = $chara[18] / 200;
					if($dmgplus > 20){$dmgplus=20;}
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>エンジェルキッスッ！</font><br>";
					$dmgplus = ${'mem'.$ri}[18] / 200;
					if($dmgplus > 20){$dmgplus=20;}
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hit_ritu'}=int(${'smem'.$sab.'hit_ritu'}/2);
				${'scom'.$sab} .="<font class=\"red\" size=5>エンジェルキッスッ！</font><br>";
				$dmgplus = ${'smem'.$sab}[18] / 200;
				if($dmgplus > 20){$dmgplus=20;}
				if($dmgplus < 1 ){$dmgplus=1;}
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
			}
		}
	}
}
sub atowaza{}
1;