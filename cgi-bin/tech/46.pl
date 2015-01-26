sub hissatu46{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(500))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‘ß•ßIII</font><br>";
					if($place==98 or $bossdayo==1){
						${'com'.$ab} .="<font class=\"yellow\" size=5>‘Ï«‚ª‚ ‚é‚Ì‚©ƒbƒbƒbB</font>";
						$bunsi=6+$bossdayo*2;
						$bunbo=$bunsi+1;
						$smem1hp_flg = int($smem1hp_flg * $bunsi / $bunbo);
						$smem2hp_flg = int($smem2hp_flg * $bunsi / $bunbo);
						$smem3hp_flg = int($smem3hp_flg * $bunsi / $bunbo);
						$smem4hp_flg = int($smem4hp_flg * $bunsi / $bunbo);
					}else{
					$smem1hp_flg = int($smem1hp_flg * 3 / 4);
					$smem2hp_flg = int($smem2hp_flg * 3 / 4);
					$smem3hp_flg = int($smem3hp_flg * 3 / 4);
					$smem4hp_flg = int($smem4hp_flg * 3 / 4);
					if($item[0] eq "Œx–_"){
						$smem1hp_flg = int($smem1hp_flg * 5 / 7);
						$smem2hp_flg = int($smem2hp_flg * 5 / 7);
						$smem3hp_flg = int($smem3hp_flg * 5 / 7);
						$smem4hp_flg = int($smem4hp_flg * 5 / 7);
						${'com'.$ab} .="<font class=\"yellow\" size=5>ŒY–±Š‚Ö”ò‚Î‚·I</font>";
					}
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(500))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z‘ß•ßIII</font><br>";
					if($place==98 or $bossdayo==1){
						${'com'.$ab} .="<font class=\"yellow\" size=5>‘Ï«‚ª‚ ‚é‚Ì‚©ƒbƒbƒbB</font>";
						$bunsi=6+$bossdayo*2;
						$bunbo=$bunsi+1;
						$smem1hp_flg = int($smem1hp_flg * $bunsi / $bunbo);
						$smem2hp_flg = int($smem2hp_flg * $bunsi / $bunbo);
						$smem3hp_flg = int($smem3hp_flg * $bunsi / $bunbo);
						$smem4hp_flg = int($smem4hp_flg * $bunsi / $bunbo);
					}else{
					$smem1hp_flg = int($smem1hp_flg * 3 / 4);
					$smem2hp_flg = int($smem2hp_flg * 3 / 4);
					$smem3hp_flg = int($smem3hp_flg * 3 / 4);
					$smem4hp_flg = int($smem4hp_flg * 3 / 4);
					if(${'mem'.$ri.'item'}[0] eq "Œx–_"){
						$smem1hp_flg = int($smem1hp_flg * 5 / 7);
						$smem2hp_flg = int($smem2hp_flg * 5 / 7);
						$smem3hp_flg = int($smem3hp_flg * 5 / 7);
						$smem4hp_flg = int($smem4hp_flg * 5 / 7);
						${'com'.$ab} .="<font class=\"yellow\" size=5>ŒY–±Š‚Ö”ò‚Î‚·I</font>";
					}
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(500))){
				$k=1;
				$mem1hp_flg = int($mem1hp_flg * 3 / 4);
				$mem2hp_flg = int($mem2hp_flg * 3 / 4);
				$mem3hp_flg = int($mem3hp_flg * 3 / 4);
				$mem4hp_flg = int($mem4hp_flg * 3 / 4);
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z‘ß•ßIII</font><br>";
				if(${'smem'.$sab.'item'}[0] eq "Œx–_"){
					$mem1hp_flg = int($mem1hp_flg * 5 / 7);
					$mem2hp_flg = int($mem2hp_flg * 5 / 7);
					$mem3hp_flg = int($mem3hp_flg * 5 / 7);
					$mem4hp_flg = int($mem4hp_flg * 5 / 7);
					${'scom'.$sab} .="<font class=\"yellow\" size=5>ŒY–±Š‚Ö”ò‚Î‚·I</font>";
				}
			}
		}
	}
}
sub atowaza{}
1;