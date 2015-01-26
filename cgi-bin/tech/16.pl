sub hissatu16{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					$rrr=int(rand(3));
					${'dmg'.$ab} += $chara[7] * int(rand(150));
					${'dmg'.$ab} += $chara[8] * int(rand(150));
					if($rrr==0){
						$sdmg1=0;$sdmg2=0;$sdmg3=0;$sdmg4=0;
						${'com'.$ab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!“G‚à!!</font><br>";
					}else{
						${'com'.$ab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!‚ ‚êc</font><br>";
					}
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>‰ïS‚ÌˆêŒ‚II</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					$rrr=int(rand(3));
					${'dmg'.$ab} += ${'mem'.$ri}[7] * int(rand(150));
					${'dmg'.$ab} += ${'mem'.$ri}[8] * int(rand(150));
					if($rrr==0){
						$sdmg1=0;$sdmg2=0;$sdmg3=0;$sdmg4=0;
						${'com'.$ab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!“G‚à!!</font><br>";
					}else{
						${'com'.$ab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!‚ ‚êc</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				$rrr=int(rand(3));
				${'sdmg'.$sab} += ${'smem'.$sab}[7] * int(rand(150));
				${'sdmg'.$sab} += ${'smem'.$sab}[8] * int(rand(150));
				if($rrr==0){
					$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
					${'scom'.$sab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!“G‚à!!</font><br>";
				}else{
					${'scom'.$sab} .="<font class=\"red\" size=5>ˆê‚É—x‚é!!‚ ‚êc</font><br>";
				}
			}
		}
	}
}
sub atowaza{}
1;