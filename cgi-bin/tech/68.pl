sub hissatu68{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$khp_flg =int(rand($khp_flg/10));
					if(int(rand(2))==0 and $bossdayo!=1){
						$smem1hp_flg = int(rand($smem1hp_flg));
						$smem2hp_flg = int(rand($smem2hp_flg));
						$smem3hp_flg = int(rand($smem3hp_flg));
						$smem4hp_flg = int(rand($smem4hp_flg));
						${'com'.$ab} .="<font class=\"red\" size=5>…呪術HPカット！</font><br>";
					}else{
						$sdmg1 = int(rand($sdmg1/10));
						$sdmg2 = int(rand($sdmg2/10));
						$sdmg3 = int(rand($sdmg3/10));
						$sdmg4 = int(rand($sdmg4/10));
						${'com'.$ab} .="<font class=\"red\" size=5>…呪術ダメージカット！</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'mem'.$ri.'hp_flg'}=int(rand(${'mem'.$ri.'hp_flg'}/10));
					if(int(rand(2))==0 and $bossdayo!=1){
						$smem1hp_flg = int(rand($smem1hp_flg));
						$smem2hp_flg = int(rand($smem2hp_flg));
						$smem3hp_flg = int(rand($smem3hp_flg));
						$smem4hp_flg = int(rand($smem4hp_flg));
						${'com'.$ab} .="<font class=\"red\" size=5>…呪術HPカット！</font><br>";
					}else{
						$sdmg1 = int(rand($sdmg1/10));
						$sdmg2 = int(rand($sdmg2/10));
						$sdmg3 = int(rand($sdmg3/10));
						$sdmg4 = int(rand($sdmg4/10));
						${'com'.$ab} .="<font class=\"red\" size=5>…呪術ダメージカット！</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'smem'.$sab.'hp_flg'}=int(rand(${'smem'.$sab.'hp_flg'}/10));
				if(int(rand(2))==0){
					$mem1hp_flg = int(rand($mem1hp_flg));
					$mem2hp_flg = int(rand($mem2hp_flg));
					$mem3hp_flg = int(rand($mem3hp_flg));
					$mem4hp_flg = int(rand($mem4hp_flg));
					${'scom'.$sab} .="<font class=\"red\" size=5>…呪術HPカット！</font><br>";
				}else{
					$dmg1 = int(rand($dmg1/10));
					$dmg2 = int(rand($dmg2/10));
					$dmg3 = int(rand($dmg3/10));
					$dmg4 = int(rand($dmg4/10));
					${'scom'.$sab} .="<font class=\"red\" size=5>…呪術ダメージカット！</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;