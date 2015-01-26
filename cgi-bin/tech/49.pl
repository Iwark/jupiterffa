sub hissatu49{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$khp_flg -=int(${'dmg'.$ab}/int(rand(50)+50));
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技ブラッディクロス！</font><br>";
					if($khp_flg>0){${'dmg'.$ab} = int(${'dmg'.$ab} * 8);
					}else{$khp_flg=1;${'com'.$ab} .="<font class=\"red\" size=5>失敗したッ。</font><br>";}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ri.'hp_flg'}-=int(${'dmg'.$ab}/int(rand(50)+50));
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技ブラッディクロス！</font><br>";
					if(${'mem'.$ri.'hp_flg'}>0){${'dmg'.$ab} = int(${'dmg'.$ab} * 8);
					}else{${'mem'.$ri.'hp_flg'}=1;${'com'.$ab} .="<font class=\"red\" size=5>失敗したッ。</font><br>";}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hp_flg'}-=int(${'sdmg'.$sab}/int(rand(50)+50));
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技ブラッディクロス！</font><br>";
				if(${'smem'.$sab.'hp_flg'}>0){${'sdmg'.$sab} = int(${'sdmg'.$sab} * 8);
				}else{${'smem'.$sab.'hp_flg'}=1;${'scom'.$sab} .="<font class=\"red\" size=5>失敗したッ。</font><br>";}
			}
		}
	}
}
sub atowaza{}
1;