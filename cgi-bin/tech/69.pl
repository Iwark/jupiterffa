sub hissatu69{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$mem1hp_flg = 0;
					$mem2hp_flg = 0;
					$mem3hp_flg = 0;
					$smem2hp_flg = 0;
					$smem3hp_flg = 0;
					$smem4hp_flg = 0;
					${'com'.$ab} .="<font class=\"red\" size=5>決闘だ！！！！</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$khp_flg=0;
					if($ab!=2){$mem1hp_flg = 0;}
					if($ab!=3){$mem2hp_flg = 0;}
					if($ab!=4){$mem3hp_flg = 0;}
					$smem2hp_flg = 0;
					$smem3hp_flg = 0;
					$smem4hp_flg = 0;
					${'com'.$ab} .="<font class=\"red\" size=5>決闘だ！！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$mem1hp_flg = 0;
				$mem2hp_flg = 0;
				$mem3hp_flg = 0;
				$smem2hp_flg = 0;
				$smem3hp_flg = 0;	
				$smem4hp_flg = 0;
				${'scom'.$sab} .="<font class=\"red\" size=5>決闘だ！！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;