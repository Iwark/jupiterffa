sub hissatu58{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * int(rand(7)+2));
					${'mem'.$ab.'hit_ritu'}+=100;
					${'com'.$ab} .="<font class=\"yellow\" size=5>•KE‹ZŒÜŒ‰JIIIUŒ‚‚ª‰J‚Ì‚æ‚¤‚É~‚è’‚®‚ÁI</font>";
					if($item[0] eq "‰JŒ•"){
						${'dmg'.$ab} = int(${'dmg'.$ab} * 2);
						${'com'.$ab} .="<font class=\"yellow\" size=5>‰JII</font>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'dmg'.$ab} = int(${'dmg'.$ab} * int(rand(7)+2));
					${'mem'.$ab.'hit_ritu'}+=100;
					${'com'.$ab} .="<font class=\"yellow\" size=5>•KE‹ZŒÜŒ‰JIIIUŒ‚‚ª‰J‚Ì‚æ‚¤‚É~‚è’‚®‚ÁI</font>";
					if(${'mem'.$ri.'item'}[0] eq "‰JŒ•"){
						${'dmg'.$ab} = int(${'dmg'.$ab} * 2);
						${'com'.$ab} .="<font class=\"yellow\" size=5>‰JII</font>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = int(${'sdmg'.$sab} * int(rand(7)+2));
				${'smem'.$sab.'hit_ritu'}+=100;
				${'scom'.$sab} .="<font class=\"yellow\" size=5>•KE‹ZŒÜŒ‰JIIIUŒ‚‚ª‰J‚Ì‚æ‚¤‚É~‚è’‚®‚ÁI</font>";
				if(${'smem'.$sab.'item'}[0] eq "‰JŒ•"){
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 2);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>‰JII</font>";
				}
			}
		}
	}
}
sub atowaza{}
1;