sub spell41{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'sake'.$sp} += 20;
	if($sp==1){
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣スロウ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]は時魔法スロウを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'sake'.$sp} += 20;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣スロウ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]は時魔法スロウを放った!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				${'sake'.$sp} += 20;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	${'ssake'.$ssp} += 20;
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>魔法剣スロウ!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]は時魔法スロウを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'ssake'.$ssp} += 20;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
	}
	}
	}
}
1;