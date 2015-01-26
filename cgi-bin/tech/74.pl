sub hissatu74{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if($place==50 or $on == $place or $place==98 or $bossdayo==1){
					${'com'.$ab} .="<font class=\"red\" size=5>試練カモーン！！…ギャッ!!</font><br>";
					}elsif( int(rand(100)) < 80 ){
					$siren=1;
					&mons_read;
					$siren=0;
					$mem1hp_flg = 0;
					$mem2hp_flg = 0;
					$mem3hp_flg = 0;
					$smem1hp_flg = int(rand($mrand1)) + $msp1*($sirenp+1);
					$smem2hp_flg = int(rand($mrand2)) + $msp2*($sirenp+1);
					$smem3hp_flg = int(rand($mrand3)) + $msp3*($sirenp+1);
					$smem4hp_flg = int(rand($mrand4)) + $msp4*($sirenp+1);
					$smem1hp = $smem1hp_flg;
					$smem2hp = $smem2hp_flg;
					$smem3hp = $smem3hp_flg;
					$smem4hp = $smem4hp_flg;
					${'com'.$ab} .="<font class=\"red\" size=5>試練カモーン！！</font><br>";
					$sirenp++;
					}else{
					${'com'.$ab} .="<font class=\"red\" size=5>試練カモーン！！…ギャッ!!</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>試練カモーン！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'com'.$ab} .="<font class=\"red\" size=5>試練カモーン！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;