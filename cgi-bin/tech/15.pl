sub hissatu15{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$rrr=int(rand(2));
					if($rrr==0){
						${'dmg'.$ab} += $chara[7] * int(rand(150));
						${'mem'.$ab.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIISTR!!</font><br>";
					}else{
						${'dmg'.$ab} += $chara[8] * int(rand(150));
						${'mem'.$ab.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIIINT!!</font><br>";
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
						${'dmg'.$ab} += ${'mem'.$ri}[7] * int(rand(150));
						${'mem'.$ab.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIISTR!!</font><br>";
					}else{
						${'dmg'.$ab} += ${'mem'.$ri}[8] * int(rand(150));
						${'mem'.$ab.'hit_ritu'}+=99;
						${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIIINT!!</font><br>";
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
					${'sdmg'.$sab} += ${'smem'.$sab}[7] * int(rand(150));
					${'smem'.$sab.'hit_ritu'}+=99;
					${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIISTR!!</font><br>";
				}else{
					${'sdmg'.$sab} += ${'smem'.$sab}[8] * int(rand(150));
					${'smem'.$sab.'hit_ritu'}+=99;
					${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z—x‚éIIINT!!</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;