sub hissatu44{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					${'mem'.$ab.'hit_ritu'}+=30;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E�Z�O�����I�R��q�b�g�I</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					${'mem'.$ab.'hit_ritu'}+=30;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E�Z�O�����I�R��q�b�g�I</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 3);
				${'smem'.$sab.'hit_ritu'}+=30;
				${'scom'.$sab} .="<font class=\"red\" size=5>�K�E�Z�O�����I�R��q�b�g�I</font><br>";
			}
		}
	}
}
sub atowaza{}
1;