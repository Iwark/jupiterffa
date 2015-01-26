sub hissatu64{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if(!$smem1[0]){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(480))){
					$k=1;
					$rnd=int(rand(5));
					${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技裁判！！！！</font>";
					if($rnd<3){
					${'com'.$ab} .="<font class=\"yellow\" size=5>無罪！！！</font>";
					${'dmg'.$ab} = 0;
					}
					if($rnd==3){
					${'com'.$ab} .="<font class=\"yellow\" size=5>有罪！！！</font>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * int(rand(7)+2));
					}
					if($rnd==4){
					${'com'.$ab} .="<font class=\"yellow\" size=5>死刑！！！</font>";
					if($place==98 or $bossdayo==1){
						${'com'.$ab} .="<font class=\"yellow\" size=5>耐性があるのかッッッ。</font>";
						$bunsi=5;
						$bunbo=$bunsi+1;
						$smem1hp_flg = int($smem1hp_flg * $bunsi / $bunbo);
						$smem2hp_flg = int($smem2hp_flg * $bunsi / $bunbo);
						$smem3hp_flg = int($smem3hp_flg * $bunsi / $bunbo);
						$smem4hp_flg = int($smem4hp_flg * $bunsi / $bunbo);
						${'dmg'.$ab} = 0;
					}else{
						$smem1hp_flg=int(rand(1))+1;
						$smem2hp_flg=int(rand(2));
						$smem3hp_flg=int(rand(2));
						$smem4hp_flg=int(rand(2));
						${'dmg'.$ab} = 0;
					}
					}					
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(480))){
					$k=1;
					$rnd=int(rand(5));
					${'com'.$ab} .="<font class=\"yellow\" size=5>必殺技裁判！！！！</font>";
					if($rnd<3){
					${'com'.$ab} .="<font class=\"yellow\" size=5>無罪！！！</font>";
					${'dmg'.$ab} = 0;
					}
					if($rnd==3){
					${'com'.$ab} .="<font class=\"yellow\" size=5>有罪！！！</font>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * int(rand(7)+2));
					}
					if($rnd==4){
					${'com'.$ab} .="<font class=\"yellow\" size=5>死刑！！！</font>";
					if($place==98 or $bossdayo==1){
						${'com'.$ab} .="<font class=\"yellow\" size=5>耐性があるのかッッッ</font>";
						$bunsi=5;
						$bunbo=$bunsi+1;
						$smem1hp_flg = int($smem1hp_flg * $bunsi / $bunbo);
						$smem2hp_flg = int($smem2hp_flg * $bunsi / $bunbo);
						$smem3hp_flg = int($smem3hp_flg * $bunsi / $bunbo);
						$smem4hp_flg = int($smem4hp_flg * $bunsi / $bunbo);
						${'dmg'.$ab} = 0;
					}else{
						$smem1hp_flg=int(rand(1))+1;
						$smem2hp_flg=int(rand(2));
						$smem3hp_flg=int(rand(2));
						$smem4hp_flg=int(rand(2));
						${'dmg'.$ab} = 0;
					}
					}
				}
			}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if(!$mem1[0]){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(480))){
				$k=1;
				$rnd=int(rand(5));
				${'scom'.$sab} .="<font class=\"yellow\" size=5>必殺技裁判！！！！</font>";
				if($rnd<3){
					${'scom'.$sab} .="<font class=\"yellow\" size=5>無罪！！！</font>";
					${'sdmg'.$sab} = 0;
				}
				if($rnd==3){
					${'scom'.$sab} .="<font class=\"yellow\" size=5>有罪！！！</font>";
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * int(rand(7)+2));
				}
				if($rnd==4){
					${'scom'.$sab} .="<font class=\"yellow\" size=5>死刑！！！</font>";
					$mem1hp_flg=int(rand(1))+1;
					$mem2hp_flg=int(rand(2));
					$mem3hp_flg=int(rand(2));
					$mem4hp_flg=int(rand(2));
					${'sdmg'.$sab} = 0;
				}
			}
		}
		}
	}
}
sub atowaza{}
1;