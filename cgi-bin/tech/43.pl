sub hissatu43{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$khp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem1hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem2hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem3hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					${'staisyo'.$ab}=4;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技サイクロン！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$khp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem1hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem2hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					$mem3hp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					${'staisyo'.$ab}=4;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技サイクロン！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$smem1hp_flg -=int(${'sdmg'.$sab}/int(rand(50)+50));
				$smem2hp_flg -=int(${'sdmg'.$sab}/int(rand(50)+50));
				$smem3hp_flg -=int(${'sdmg'.$sab}/int(rand(50)+50));
				$smem4hp_flg -=int(${'sdmg'.$sab}/int(rand(50)+50));
				${'taisyo'.$sab}=4;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技サイクロン！</font><br>";
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 5);
			}
		}
	}
}
sub atowaza{}
1;