sub hissatu18{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					${'mem'.$ab.'hit_ritu'}-=50;
					${'com'.$ab} .="<font class=\"yellow\" size=5>�K�E�Z�݂��ꂤ���႟���I�I�I</font><br>������I<br>������I<br>������I<br>������I<br>";
					if($chara[70]>=1 and int(rand(20))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>��S�̈ꌂ�I�I</font><br>";
					}
					if($item[0] eq "����|��"){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(5)+4);
						${'com'.$ab} .="<font class=\"yellow\" size=5>�Ƃǂ߂��I�I</font>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					${'mem'.$ab.'hit_ritu'}-=50;
					${'com'.$ab} .="<font class=\"yellow\" size=5>�K�E�Z�݂��ꂤ���႟���I�I�I</font><br>������I<br>������I<br>������I<br>������I<br>";
					if(${'mem'.$ri.'item'}[0] eq "����|��"){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(3)+3);
						${'com'.$ab} .="<font class=\"yellow\" size=5>�Ƃǂ߂��I�I</font>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * 4);
				${'smem'.$sab.'hit_ritu'}-=50;
				${'scom'.$sab} .="<font class=\"yellow\" size=5>�K�E�Z�݂��ꂤ���႟���I�I�I</font><br>������I<br>������I<br>������I<br>������I<br>";
				if(${'smem'.$sab.'item'}[0] eq "����|��"){
					${'sdmg'.$sab} = ${'sdmg'.$sab} * int(rand(3)+3);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>�Ƃǂ߂��I�I</font>";
				}
			}
		}
	}
}
sub atowaza{}
1;