sub spell11{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	if($mahoken==1){$rand=4;}else{$rand=1;}
	if(int(rand($rand))==0){
		${'hpplus'.$sp} = int(${'dmg'.$sp}/50);
		${'dmg'.$sp} = 0;
		if($sp==1){
			${'com'.$sp} .="<font class=\"white\" size=5>$chara[4]�͔����@�q�[���������!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'hpplus'.$sp} = ${'hpplus'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
			}
		}else{
			$ri=$sp-1;
			${'com'.$sp} .="<font class=\"white\" size=5>${'mem'.$ri}[4]�͔����@�q�[���������!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[56]==32 or ${'mem'.$ri}[57]==32 or ${'mem'.$ri}[58]==32){
				${'hpplus'.$sp} = ${'hpplus'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
			}
		}
	${'kaihuku'.$sp} ="<font class=\"white\" size=5>HP��${'hpplus'.$sp}�񕜂���!!</font><br>";
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	${'shpplus'.$ssp} = int(${'sdmg'.$ssp}/50);
	${'sdmg'.$ssp} = 0;
	if($mahoken==1){$rand=4;}else{$rand=1;}
	if(int(rand($rand))==0){
		${'scom'.$ssp} .="<font class=\"white\" size=5>${'smem'.$ssp}[4]�͔����@�q�[���������!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[56]==32 or ${'smem'.$ssp}[57]==32 or ${'smem'.$ssp}[58]==32){
			${'shpplus'.$ssp} = ${'shpplus'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>��Z�A�A�����@����!!</font><br>";
		}
	}
	${'skaihuku'.$ssp} ="<font class=\"white\" size=5>HP��${'shpplus'.$ssp}�񕜂���!!</font><br>";
	}
	}
}
1;