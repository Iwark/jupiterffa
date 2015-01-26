sub hissatu22{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
				if($khp_flg < 100 and $mem1hp_flg < 100 and $mem2hp_flg < 100 and $mem3hp_flg < 100){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 44);
					${'mem'.$ab.'hit_ritu'}+=999;
					${'com'.$ab} .="<font class=\"red\" size=5>一撃必殺どりゃぁ！</font><br>";
					if($chara[70]>=1 and int(rand(1000))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>会心の一撃！！</font><br>";
					}
				}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
				if($khp_flg < 100 and $mem1hp_flg < 100 and $mem2hp_flg < 100 and $mem3hp_flg < 100){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 44);
					${'mem'.$ab.'hit_ritu'}+=999;
					${'com'.$ab} .="<font class=\"red\" size=5>一撃必殺どりゃぁ！</font><br>";
				}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				if($smem1hp_flg<100 and $smem2hp_flg<100 and $smem3hp_flg<100 and $smem4hp_flg<100){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 44);
				${'smem'.$sab.'hit_ritu'}+=999;
				${'scom'.$sab} .="<font class=\"red\" size=5>一撃必殺どりゃぁ！</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;