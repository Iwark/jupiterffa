sub spell5{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	$sdmg1=int($sdmg1*0.8);$sdmg2=int($sdmg2*0.8);$sdmg3=int($sdmg3*0.8);$sdmg4=int($sdmg4*0.8);
	if($sp==1){
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>���@���u���U��!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]�͍����@�u���U���������!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>���@���u���U��!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]�͍����@�u���U���������!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
			}
		}
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	$dmg1=int($dmg1*0.8);$dmg2=int($dmg2*0.8);$dmg3=int($dmg3*0.8);$dmg4=int($dmg4*0.8);
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>���@���u���U��!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]�͍����@�u���U���������!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
		}
	}
	}
	}
}
1;