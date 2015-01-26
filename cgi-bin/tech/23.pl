sub hissatu23{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					${'dmg'.$ab} = 0;
					$sdmg1=int($sdmg1/4);$sdmg2=int($sdmg2/4);
					$sdmg3=int($sdmg3/4);$sdmg4=int($sdmg4/4);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技説得！！！</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>会心の一撃！！</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					${'dmg'.$ab} = 0;
					$sdmg1=int($sdmg1/4);$sdmg2=int($sdmg2/4);
					$sdmg3=int($sdmg3/4);$sdmg4=int($sdmg4/4);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技説得！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				${'sdmg'.$sab} = 0;
				$dmg1=int($dmg1/4);$dmg2=int($dmg2/4);
				$dmg3=int($dmg3/4);$dmg4=int($dmg4/4);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技説得！！！</font><br>";
			}
		}
	}
}
sub atowaza{
}
1;