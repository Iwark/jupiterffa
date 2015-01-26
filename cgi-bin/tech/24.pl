sub hissatu24{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					$sdmg1=int($sdmg1/2);$sdmg2=int($sdmg2/2);
					$sdmg3=int($sdmg3/2);$sdmg4=int($sdmg4/2);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技説法！！！</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>会心の一撃！！</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					$sdmg1=int($sdmg1/2);$sdmg2=int($sdmg2/2);
					$sdmg3=int($sdmg3/2);$sdmg4=int($sdmg4/2);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技説法！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				$dmg1=int($dmg1/2);$dmg2=int($dmg2/2);
				$dmg3=int($dmg3/2);$dmg4=int($dmg4/2);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技説法！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;