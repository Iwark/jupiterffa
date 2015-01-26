sub spell9{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'maho'.$sp}=3;
	${'mem'.$sp.'hit_ritu'}=int(${'mem'.$sp.'hit_ritu'}*3.3);
	if($sp==1){
		if($chara[24]==1337){${'dmg'.$sp} = int(${'dmg'.$sp} * 12);}
		if($chara[29]==2311){${'dmg'.$sp} = int(${'dmg'.$sp} * 8);}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣サンダガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]は黒魔法サンダガを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if(${'mem'.$ri}[24]==1337){${'dmg'.$sp} = int(${'dmg'.$sp} * 12);}
		if(${'mem'.$ri}[29]==2311){${'dmg'.$sp} = int(${'dmg'.$sp} * 8);}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣サンダガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]は黒魔法サンダガを放った!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	${'smem'.$ssp.'hit_ritu'}=int(${'smem'.$ssp.'hit_ritu'}*3.3);
	if(${'smem'.$ssp}[24]==1337){${'sdmg'.$ssp} = int(${'sdmg'.$ssp} * 12);}
	if(${'smem'.$ssp}[29]==2311){${'sdmg'.$ssp} = int(${'sdmg'.$ssp} * 8);}
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>魔法剣サンダガ!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]は黒魔法サンダガを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
	}
	}
	}
}
1;