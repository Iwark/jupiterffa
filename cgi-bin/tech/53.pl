sub hissatu53{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if($mem3hp_flg>0){$dmg4 = $dmg4*30;}
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技ペットパワー！！！</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技ペットパワー！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技ペットパワー！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;