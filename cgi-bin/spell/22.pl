sub spell22{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'sake'.$sp} += int(rand(2000));
	if($sp==1){
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>–‚–@Œ•‹óä!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]‚Í”Ep‹óä‚ğ•ú‚Á‚½!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'sake'.$sp} += int(rand(2000));
				${'com'.$sp} .="<font class=\"yellow\" size=5>”é‹ZA˜A‘±–‚–@”­“®!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>–‚–@Œ•‹óä!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]‚Í”Ep‹óä‚ğ•ú‚Á‚½!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				${'sake'.$sp} += int(rand(2000));
				${'com'.$sp} .="<font class=\"yellow\" size=5>”é‹ZA˜A‘±–‚–@”­“®!!</font><br>";
			}
		}
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	${'ssake'.$ssp} += int(rand(2000));
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>–‚–@Œ•‹óä!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]‚Í”Ep‹óä‚ğ•ú‚Á‚½!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'ssake'.$ssp} += int(rand(2000));
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>”é‹ZA˜A‘±–‚–@”­“®!!</font><br>";
		}
	}
	}
	}
}
1;