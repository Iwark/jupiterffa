sub hissatu63{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					if($wanacount==4){
					${'com'.$ab} .="<font class=\"red\" size=5>‰®•~ã©”­“®I</font><br>";
					${'mem'.$ab.'hit_ritu'}=100000000;
					if($item[0] eq "‰®•~Œ•" and $item[3] eq "‰®•~ŠZ"){
						${'dmg'.$ab} = ${'dmg'.$ab} * 9999;
					}else{
						${'dmg'.$ab} = ${'dmg'.$ab} * 99;
					}
					$wanacount=0;
					}elsif($wanacount>0){
					$wncount=4-$wanacount;
					${'com'.$ab} .="<font class=\"red\" size=5>$wncount c</font><br>";
					$wanacount++;
					}else{
					$wanacount=1;
					$wncount=4-$wanacount;
					${'com'.$ab} .="<font class=\"red\" size=5>‰®•~ã©‚ğİ’u‚µ‚½I$wncount c</font><br>";
					$wanacount++;
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					if($wanacount==4){
					${'com'.$ab} .="<font class=\"red\" size=5>‰®•~ã©”­“®I</font><br>";
					${'mem'.$ab.'hit_ritu'}=100000000;
					if(${'mem'.$ri.'item'}[0] eq "‰®•~Œ•" and ${'mem'.$ri.'item'}[3] eq "‰®•~ŠZ"){
						${'dmg'.$ab} = ${'dmg'.$ab} * 9999;
					}else{
						${'dmg'.$ab} = ${'dmg'.$ab} * 99;
					}
					$wanacount=0;
					}elsif($wanacount>0){
					$wncount=4-$wanacount;
					${'com'.$ab} .="<font class=\"red\" size=5>$wncount c</font><br>";
					$wanacount++;
					}else{
					$wanacount=1;
					$wncount=4-$wanacount;
					${'com'.$ab} .="<font class=\"red\" size=5>‰®•~ã©‚ğİ’u‚µ‚½I$wncount c</font><br>";
					$wanacount++;
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				if($swanacount==4){
					${'scom'.$sab} .="<font class=\"red\" size=5>‰®•~ã©”­“®I</font><br>";
					${'smem'.$sab.'hit_ritu'}=100000000;
					if(${'smem'.$sab.'item'}[0] eq "‰®•~Œ•" and ${'smem'.$sab.'item'}[3] eq "‰®•~ŠZ"){
						${'sdmg'.$sab} = ${'sdmg'.$sab} * 9999;
					}else{
						${'sdmg'.$sab} = ${'sdmg'.$sab} * 99;
					}
					$swanacount=0;
				}elsif($swanacount>0){
					$swncount=4-$swanacount;
					${'scom'.$sab} .="<font class=\"red\" size=5>$swncount c</font><br>";
					$swanacount++;
				}else{
					$swanacount=1;
					$swncount=4-$swanacount;
					${'scom'.$sab} .="<font class=\"red\" size=5>‰®•~ã©‚ğİ’u‚µ‚½I$swncount c</font><br>";
					$swanacount++;
				}
			}
		}
	}
}
sub atowaza{}
1;