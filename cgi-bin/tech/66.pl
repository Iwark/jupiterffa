sub hissatu66{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if($chara[52]==43 and $chara[53]==47){
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技マイティサイクロン！！</font>";
						${'staisyo'.$ab}=4;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					}
					if($chara[52]==36 and $chara[53]==61){
						$khp_flg =int($khp_flg/10);
						${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/10);
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技時空地獄へ飛ばす！！</font>";
						if($i>2){$i=int(rand(29)+1);}
						if(int(rand(4))<3){${'staisyo'.$ab}=4;}
						elsif($smem1hp_flg>0){${'staisyo'.$ab}=0;}
						elsif($smem2hp_flg>0){${'staisyo'.$ab}=1;}
						elsif($smem3hp_flg>0){${'staisyo'.$ab}=2;}
						elsif($smem4hp_flg>0){${'staisyo'.$ab}=3;}
						else{${'staisyo'.$ab}=4;}
						$dmgplus = int($chara[18]/400);
						if($dmgplus > 20){$dmgplus = 20;}
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}
					if($chara[52]==6 and $chara[53]==30){
						${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/100);
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技酔拳！！</font>";
						if(int(rand(4))<3){
							${'dmg'.$ab} = int(${'dmg'.$ab} * 99);
						}else{	${'dmg'.$ab} = -int(${'dmg'.$ab} * 99);}
					}
					if($chara[52]==48 and $chara[53]==20){
						${'hpplus'.$ab} = int(${'dmg'.$ab}/int(rand(1000)+1));
						${'staisyo'.$ab} =4;
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技聖なるブレス！！</font>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(${'mem'.$ri}[52]==43 and ${'mem'.$ri}[53]==47){
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技マイティサイクロン！！</font>";
						${'staisyo'.$ab}=4;
						${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					}
					if(${'mem'.$ri}[52]==36 and ${'mem'.$ri}[53]==61){
						${'mem'.$ri.'hp_flg'}=int(${'mem'.$ri.'hp_flg'}/10);
						${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/10);
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技時空地獄へ飛ばす！！</font>";
						if($i>2){$i=int(rand(29)+1);}
						if(int(rand(4))<3){${'staisyo'.$ab}=4;}
						elsif($smem1hp_flg>0){${'staisyo'.$ab}=0;}
						elsif($smem2hp_flg>0){${'staisyo'.$ab}=1;}
						elsif($smem3hp_flg>0){${'staisyo'.$ab}=2;}
						elsif($smem4hp_flg>0){${'staisyo'.$ab}=3;}
						else{${'staisyo'.$ab}=4;}
						$dmgplus = int(${'mem'.$ri}[18]/400);
						if($dmgplus > 20){$dmgplus = 20;}
						${'dmg'.$ab} = int(${'dmg'.$ab} * $dmgplus);
					}
					if(${'mem'.$ri}[52]==6 and ${'mem'.$ri}[53]==30){
						${'mem'.$ab.'hit_ritu'}=int(${'mem'.$ab.'hit_ritu'}/100);
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技酔拳！！</font>";
						if(int(rand(4))<3){
							${'dmg'.$ab} = int(${'dmg'.$ab} * 99);
						}else{	${'dmg'.$ab} = -int(${'dmg'.$ab} * 99);}
					}
					if(${'mem'.$ri}[52]==48 and ${'mem'.$ri}[53]==20){
						${'hpplus'.$ab} = int(${'dmg'.$ab}/int(rand(1000)+1));
						${'staisyo'.$ab} =4;
						${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技聖なるブレス！！</font>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				if(${'smem'.$sab}[52]==43 and ${'smem'.$sab}[53]==47){
					${'scom'.$sab} .="<font class=\"yellow\" size=5>必殺技マイティサイクロン！！</font>";
					${'taisyo'.$sab}=4;
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 4);
				}
				if(${'smem'.$sab}[52]==36 and ${'smem'.$sab}[53]==61){
					${'smem'.$sab.'hp_flg'}=int(${'smem'.$sab.'hp_flg'}/10);
					${'smem'.$sab.'hit_ritu'}=int(${'smem'.$sab.'hit_ritu'}/10);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>必殺技時空地獄へ飛ばす！！</font>";
					if($i>2){$i=int(rand(29)+1);}
					if(int(rand(4))<3){${'taisyo'.$sab}=4;}
					elsif($mem1hp_flg>0){${'taisyo'.$sab}=0;}
					elsif($mem2hp_flg>0){${'taisyo'.$sab}=1;}
					elsif($mem3hp_flg>0){${'taisyo'.$sab}=2;}
					elsif($mem4hp_flg>0){${'taisyo'.$sab}=3;}
					else{${'taisyo'.$sab}=4;}
					$dmgplus = int(${'smem'.$sab}[18]/400);
					if($dmgplus > 20){$dmgplus = 20;}
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * $dmgplus);
				}
				if(${'smem'.$sab}[52]==6 and ${'smem'.$sab}[53]==30){
					${'smem'.$sab.'hit_ritu'}=int(${'smem'.$sab.'hit_ritu'}/100);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>必殺技酔拳！！</font>";
					if(int(rand(4))<3){
						${'sdmg'.$sab} = int(${'sdmg'.$sab} * 99);
					}else{	${'sdmg'.$sab} = -int(${'sdmg'.$sab} * 99);}
				}
				if(${'smem'.$sab}[52]==48 and ${'smem'.$sab}[53]==20){
					${'shpplus'.$sab} = int(${'sdmg'.$sab}/int(rand(1000)+1));
					${'taisyo'.$sab} =4;
					${'scom'.$sab} .="<font class=\"yellow\" size=5>必殺技聖なるブレス！！</font>";
				}
			}
		}
	}
}
sub atowaza{}
1;