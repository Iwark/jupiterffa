sub hissatu56{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if(int(rand(4))==0){
					${'dmg'.$ab} = int(${'dmg'.$ab} * 99);
					${'mem'.$ab.'hit_ritu'}+=999;
					${'com'.$ab} .="<font class=\"red\" size=5>ˆÃEI</font><br>";
					}else{
					${'com'.$ab} .="<font class=\"red\" size=5>ˆÃEI¸”s‚©‚ÁI‚®‚Ó‚Á</font><br>";
					$khp_flg =0;
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(int(rand(4))==0){
					${'dmg'.$ab} = int(${'dmg'.$ab} * 99);
					${'mem'.$ab.'hit_ritu'}+=999;
					${'com'.$ab} .="<font class=\"red\" size=5>ˆÃEI</font><br>";
					}else{
					${'com'.$ab} .="<font class=\"red\" size=5>ˆÃEI¸”s‚©‚ÁI‚®‚Ó‚Á</font><br>";
					${'mem'.$ri.'hp_flg'}=0;
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				if(int(rand(4))==0){
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 99);
				${'smem'.$sab.'hit_ritu'}+=999;
				${'scom'.$sab} .="<font class=\"red\" size=5>ˆÃEI‚­‚ç‚¦‚ÁI</font><br>";
				}else{
				${'scom'.$sab} .="<font class=\"red\" size=5>ˆÃEI¸”s‚©‚ÁI‚®‚Ó‚Á</font><br>";
				${'smem'.$sab.'hp_flg'}=0;
				}
			}
		}
	}
}
sub atowaza{}
1;