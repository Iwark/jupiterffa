sub spell31{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'hpplus'.$sp} = int(${'dmg'.$sp}/50);
	if($sp==1){
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣ドレイン!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]は赤魔法ドレインを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'hpplus'.$sp} = ${'hpplus'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣ドレイン!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]は赤魔法ドレインを放った!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				${'hpplus'.$sp} = ${'hpplus'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}
	${'kaihuku'.$sp} ="<font class=\"white\" size=5>HPが${'hpplus'.$sp}回復した!!</font><br>";
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	${'shpplus'.$ssp} = int(${'sdmg'.$ssp}/50);
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>魔法剣ドレイン!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]は赤魔法ドレインを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'shpplus'.$ssp} = ${'shpplus'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
	}
	${'skaihuku'.$ssp} ="<font class=\"white\" size=5>HPが${'shpplus'.$ssp}回復した!!</font><br>";
	}
	}
}
1;