sub hissatu57{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$zrd=int(rand(2)+1);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技リザレクション！！</font><br>";
					if($zrd==1){if($mem1[4] and $mem1hp_flg<1){
						$mem1hp_flg=$mem1[16];
						${'com'.$ab} .="<font class=\"red\" size=5>$mem1[4]が蘇る！</font><br>";
					}}
					if($zrd==2){if($mem2[4] and $mem2hp_flg<1){
						$mem2hp_flg=$mem2[16];
						${'com'.$ab} .="<font class=\"red\" size=5>$mem2[4]が蘇る！</font><br>";
					}}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$zrd=int(rand(3));
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技リザレクション！！</font><br>";
					if($zrd==0){if($chara[4] and $khp_flg<1){
						$khp_flg=$chara[16];
						${'com'.$ab}.="<font class=\"red\" size=5>$chara[4]が蘇る！</font><br>";
					}}
					if($zrd==1){if($mem1[4] and $mem1hp_flg<1){
						$mem1hp_flg=$mem1[16];
						${'com'.$ab} .="<font class=\"red\" size=5>$mem1[4]が蘇る！</font><br>";
					}}
					if($zrd==2){if($mem2[4] and $mem2hp_flg<1){
						$mem2hp_flg=$mem2[16];
						${'com'.$ab} .="<font class=\"red\" size=5>$mem2[4]が蘇る！</font><br>";
					}}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$zrd=int(rand(4));
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技リザレクション！！</font><br>";
				if($zrd==0){if($smem1[4] and $smem1hp_flg<1){
					$smem1hp_flg=$smem1[16];
					${'com'.$ab} .="<font class=\"red\" size=5>$smem1[4]が蘇る！</font><br>";
				}}
				if($zrd==1){if($smem2[4] and $smem1hp_flg<1){
					$smem2hp_flg=$smem2[16];
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem2[4]が蘇る！</font><br>";
				}}
				if($zrd==2){if($smem3[4] and $smem2hp_flg<1){
					$smem3hp_flg=$smem3[16];
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem3[4]が蘇る！</font><br>";
				}}
				if($zrd==3){if($smem4[4] and $smem2hp_flg<1){
					$smem4hp_flg=$smem4[16];
					${'scom'.$sab} .="<font class=\"red\" size=5>$smem4[4]が蘇る！</font><br>";
				}}
			}
		}
	}
}
sub atowaza{}
1;