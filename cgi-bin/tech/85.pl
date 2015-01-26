sub hissatu85{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(3000))){
					$k=1;
					if(${'mem'.$ab.'hit_ritu'}<0){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 1111); }
					elsif(${'mem'.$ab.'hit_ritu'}<10){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 999); }
					elsif(${'mem'.$ab.'hit_ritu'}<100){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 777); }
					elsif(${'mem'.$ab.'hit_ritu'}<1000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 555); }
					elsif(${'mem'.$ab.'hit_ritu'}<10000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 333); }
					elsif(${'mem'.$ab.'hit_ritu'}<100000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 111); }
					${'mem'.$ab.'hit_ritu'} *= 10;
					${'com'.$ab} .="<font class=\"yellow\" size=6>魔剣！！</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(3000))){
					$k=1;
					if(${'mem'.$ab.'hit_ritu'}<0){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 1111); }
					elsif(${'mem'.$ab.'hit_ritu'}<10){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 999); }
					elsif(${'mem'.$ab.'hit_ritu'}<100){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 777); }
					elsif(${'mem'.$ab.'hit_ritu'}<1000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 555); }
					elsif(${'mem'.$ab.'hit_ritu'}<10000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 333); }
					elsif(${'mem'.$ab.'hit_ritu'}<100000){ ${'dmg'.$ab} = int(${'dmg'.$ab} * 111); }
					${'mem'.$ab.'hit_ritu'} *= 10;
					${'com'.$ab} .="<font class=\"yellow\" size=6>魔剣！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(3000))){
				$k=1;
				if(${'smem'.$sab.'hit_ritu'}<0){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 1111); }
				elsif(${'smem'.$sab.'hit_ritu'}<10){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 999); }
				elsif(${'smem'.$sab.'hit_ritu'}<100){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 777); }
				elsif(${'smem'.$sab.'hit_ritu'}<1000){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 555); }
				elsif(${'smem'.$sab.'hit_ritu'}<10000){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 333); }	
				elsif(${'smem'.$sab.'hit_ritu'}<100000){ ${'sdmg'.$sab} = int(${'dmg'.$ab} * 111); }
				${'smem'.$sab.'hit_ritu'} *= 10;
				${'scom'.$sab} .="<font class=\"yellow\" size=6>魔剣！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;