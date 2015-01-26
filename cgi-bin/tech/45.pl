sub hissatu45{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$mem1hit_ritu*=3;$mem2hit_ritu*=3;$mem3hit_ritu*=3;$mem4hit_ritu*=3;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹ZwŠöI</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$mem1hit_ritu*=3;$mem2hit_ritu*=3;$mem3hit_ritu*=3;$mem4hit_ritu*=3;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹ZwŠöI</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$smem1hit_ritu*=3;$smem2hit_ritu*=3;$smem3hit_ritu*=3;$smem4hit_ritu*=3;
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹ZwŠöI</font><br>";
			}
		}
	}
}
sub atowaza{}
1;