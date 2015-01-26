sub hissatu29{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$rrr=int(rand(2));
					if($rrr==0){
						$hpplus1 = ${'dmg'.$ab};
						$hpplus2 = ${'dmg'.$ab};
						$hpplus3 = ${'dmg'.$ab};
						$hpplus4 = ${'dmg'.$ab};
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤!‚g‚o‰ñ•œ!</font><br>";
					}else{
						${'dmg'.$ab} += $chara[11] * int(rand(200));
						${'mem'.$ab.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤I‚Ç‚è‚áI</font><br>";
					}
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>‰ïS‚ÌˆêŒ‚II</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$rrr=int(rand(2));
					if($rrr==0){
						$hpplus1 = ${'dmg'.$ab};
						$hpplus2 = ${'dmg'.$ab};
						$hpplus3 = ${'dmg'.$ab};
						$hpplus4 = ${'dmg'.$ab};
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤!‚g‚o‰ñ•œ!</font><br>";
					}else{
						${'dmg'.$ab} += ${'mem'.$ri}[11] * int(rand(200));
						${'mem'.$ri.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤I‚Ç‚è‚áI</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$rrr=int(rand(2));
				if($rrr==0){
					$shpplus1 = ${'sdmg'.$sab};
					$shpplus2 = ${'sdmg'.$sab};
					$shpplus3 = ${'sdmg'.$sab};
					$shpplus4 = ${'sdmg'.$sab};
					${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤!‚g‚o‰ñ•œ!</font><br>";
				}else{
					${'sdmg'.$sab} += ${'smem'.$sab}[11] * int(rand(200));
					${'smem'.$sab.'hit_ritu'}+=99;
					${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z‰Ì‚¤I‚Ç‚è‚áI</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;