sub hissatu61{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$khp_flg =int($khp_flg/3);
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>…地獄へ飛んでいけ！</font><br>";
					${'staisyo'.$ab} =4;
					$dmgplus = int($chara[18]/400);
					if($dmgplus > 10){$dmgplus = 10;}
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ri.'hp_flg'}=int(${'mem'.$ri.'hp_flg'}/3);
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>…地獄へ飛んでいけ！</font><br>";
					${'staisyo'.$ab} =4;
					$dmgplus = int(${'mem'.$ri}[18]/400);
					if($dmgplus > 10){$dmgplus = 10;}
					${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hp_flg'}=int(${'smem'.$sab.'hp_flg'}/3);
				${'smem'.$sab.'hit_ritu'}=int(${'smem'.$sab.'hit_ritu'}/2);
				${'scom'.$sab} .="<font class=\"red\" size=5>…地獄へ飛んでいけ！</font><br>";
				${'taisyo'.$sab} =4;
				$dmgplus = int(${'smem'.$sab}[18]/400);
				if($dmgplus > 10){$dmgplus = 10;}
				if($dmgplus < 1){$dmgplus = 1;}
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
			}
		}
	}
}
sub atowaza{}
1;