sub hissatu59{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$khp_flg =int($khp_flg/2);
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技グランドクロス！</font><br>";
					${'staisyo'.$ab} =4;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 6);
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ri.'hp_flg'}=int(${'mem'.$ri.'hp_flg'}/2);
					${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/2);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技グランドクロス！</font><br>";
					${'staisyo'.$ab} =4;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 6);
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hp_flg'}=int(${'smem'.$sab.'hp_flg'}/2);
				${'smem'.$sab.'hit_ritu'}=int(${'smem'.$sab.'hit_ritu'}/2);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技グランドクロス！</font><br>";
				${'taisyo'.$sab} =4;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 6);
			}
		}
	}
}
sub atowaza{}
1;