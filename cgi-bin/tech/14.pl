sub hissatu14{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>���₵�p���`�I�I�I</font><br>";
					if (int(rand(10))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * 10;
						${'com'.$ab} .="<font class=\"yellow\" size=5>���ɂ̂P�O�A�������I�I<br>";
					if($chara[70]>=1 and int(rand(10))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>��S�̈ꌂ�I�I</font><br>";
					}
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>���₵�p���`�I�I�I</font><br>";
					if (int(rand(10))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * 10;
						${'com'.$ab} .="<font class=\"yellow\" size=5>���ɂ̂P�O�A�������I�I<br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'scom'.$sab} .="<font class=\"red\" size=5>���₵�p���`�I�I�I</font><br>";
				if (int(rand(10))==0){
					${'sdmg'.$sab} = ${'sdmg'.$sab} * 10;
					${'scom'.$sab} .="<font class=\"yellow\" size=5>���ɂ̂P�O�A�������I�I<br>";
				}
			}
		}
	}
}
sub atowaza{}
1;