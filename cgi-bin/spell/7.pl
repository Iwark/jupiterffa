sub spell7{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'mem'.$sp.'hit_ritu'}+=10;
	if($sp==1){
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>���@���T���_�[!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]�͍����@�T���_�[�������!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>���@���T���_�[!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]�͍����@�T���_�[�������!!</font><br>";
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
	${'smem'.$ssp.'hit_ritu'}+=10;
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>���@���T���_�[!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]�͍����@�T���_�[�������!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
		}
	}
	}
	}
}
1;