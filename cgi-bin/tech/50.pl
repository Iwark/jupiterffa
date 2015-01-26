sub hissatu50{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(600))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技号令！</font><br>";
					if($mem1[4] and $mem1hp_flg<0){
						$mem1hp_flg=1;
						${'com'.$ab} .="<font class=\"red\" size=5>$mem1[4]が帰ってきた！</font><br>";
					}
					if($mem2[4] and $mem2hp_flg<0){
						$mem2hp_flg=1;
						${'com'.$ab} .="<font class=\"red\" size=5>$mem2[4]が帰ってきた！</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(600))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技号令！</font><br>";
					if($chara[4] and $khp_flg<0){
						$khp_flg=1;
						${'com'.$ab}.="<font class=\"red\" size=5>$chara[4]が帰ってきた！</font><br>";
					}
					if($mem1[4] and $mem1hp_flg<0){
						$mem1hp_flg=1;
						${'com'.$ab} .="<font class=\"red\" size=5>$mem1[4]が帰ってきた！</font><br>";
					}
					if($mem2[4] and $mem2hp_flg<0){
						$mem2hp_flg=1;
						${'com'.$ab} .="<font class=\"red\" size=5>$mem2[4]が帰ってきた！</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(600))){
				$k=1;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技号令！</font><br>";
				if($smem1[4] and $smem1hp_flg<0){
					$smem1hp_flg=1;
					${'com'.$ab} .="<font class=\"red\" size=5>$smem1[4]が帰ってきた！</font><br>";
				}
				if($smem2[4] and $smem1hp_flg<0){
					$smem2hp_flg=1;
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem2[4]が帰ってきた！</font><br>";
				}
				if($smem3[4] and $smem2hp_flg<0){
					$smem3hp_flg=1;
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem3[4]が帰ってきた！</font><br>";
				}
				if($smem4[4] and $smem2hp_flg<0){
					$smem4hp_flg=1;
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem4[4]が帰ってきた！</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;