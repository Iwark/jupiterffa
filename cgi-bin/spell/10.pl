sub spell10{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'maho'.$sp}=7;
	$ssake1= int($ssake1 / 3); $ssake2= int($ssake2 / 3); $ssake3= int($ssake3 / 3); $ssake4= int($ssake4 / 3);
	${'dmg'.$sp} = ${'dmg'.$sp} * 4;
	if($sp==1){
		if($chara[24]==1358){
	${'dmg'.$sp} = ${'dmg'.$sp} * 4;
	$ssake1= int($ssake1 / 5); $ssake2= int($ssake2 / 5); $ssake3= int($ssake3 / 5); $ssake4= int($ssake4 / 5);
		}
		if($chara[29]==2314){
	${'dmg'.$sp} = ${'dmg'.$sp} * 12;
	$ssake1= int($ssake1 / 5); $ssake2= int($ssake2 / 5); $ssake3= int($ssake3 / 5); $ssake4= int($ssake4 / 5);
		}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣エアロガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]は黒魔法エアロガを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if(${'mem'.$ri}[24]==1358){
	${'dmg'.$sp} = ${'dmg'.$sp} * 4;
	$ssake1= int($ssake1 / 5); $ssake2= int($ssake2 / 5); $ssake3= int($ssake3 / 5); $ssake4= int($ssake4 / 5);
		}
		if(${'mem'.$ri}[29]==2314){
	${'dmg'.$sp} = ${'dmg'.$sp} * 12;
	$ssake1= int($ssake1 / 5); $ssake2= int($ssake2 / 5); $ssake3= int($ssake3 / 5); $ssake4= int($ssake4 / 5);
		}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣エアロガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]は黒魔法エアロガを放った!!</font><br>";
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
	${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 4;
	$sake1= int($sake1 / 3); $sake2= int($sake2 / 3); $sake3= int($sake3 / 3); $sake4= int($sake4 / 3);
	if(${'smem'.$ssp}[24]==1358){
		${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 4;
		$sake1= int($sake1 / 5); $sake2= int($sake2 / 5); $sake3= int($sake3 / 5); $sake4= int($sake4 / 5);
	}
	if(${'smem'.$ssp}[29]==2314){
		${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 12;
		$sake1= int($sake1 / 5); $sake2= int($sake2 / 5); $sake3= int($sake3 / 5); $sake4= int($sake4 / 5);
	}
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>魔法剣エアロガ!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]は黒魔法エアロガを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
	}
	}
	}
}
1;