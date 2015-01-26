sub spell12{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	if($mahoken==1){$rand=4;}else{$rand=1;}
	if(int(rand($rand))==0){
		$hpplus1 = int(${'dmg'.$sp}/50);
		$hpplus2 = int(${'dmg'.$sp}/50);
		$hpplus3 = int(${'dmg'.$sp}/50);
		$hpplus4 = int(${'dmg'.$sp}/50);
		${'dmg'.$sp} = 0;
		if($sp==1){
			${'com'.$sp} .="<font class=\"white\" size=5>$chara[4]は白魔法ヒールラを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				$hpplus1 = $hpplus1 * 2;
				$hpplus2 = $hpplus2 * 2;
				$hpplus3 = $hpplus3 * 2;
				$hpplus4 = $hpplus4 * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}else{
			$ri=$sp-1;
			${'com'.$sp} .="<font class=\"white\" size=5>${'mem'.$ri}[4]は白魔法ヒールラを放った!!</font><br>";
			if (${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32 or ${'mem'.$ri}[55]==32){
				$hpplus1 = $hpplus1 * 2;
				$hpplus2 = $hpplus2 * 2;
				$hpplus3 = $hpplus3 * 2;
				$hpplus4 = $hpplus4 * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
		${'kaihuku'.$sp} ="<font class=\"white\" size=5>メンバーのHPが$hpplus1回復した!!</font><br>";
	}
	}
	}
	for($spe=1;$spe<5;$spe++){
	if($spe==$ssp){
	if($mahoken==1){$rand=4;}else{$rand=1;}
	if(int(rand($rand))==0){
		$shpplus1 = int(${'sdmg'.$ssp}/50);
		$shpplus2 = int(${'sdmg'.$ssp}/50);
		$shpplus3 = int(${'sdmg'.$ssp}/50);
		$shpplus4 = int(${'sdmg'.$ssp}/50);
		${'sdmg'.$ssp} = 0;
		${'scom'.$ssp} .="<font class=\"white\" size=5>${'smem'.$ssp}[4]は白魔法ヒールラを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			$shpplus1 = $shpplus1 * 2;
			$shpplus2 = $shpplus2 * 2;
			$shpplus3 = $shpplus3 * 2;
			$shpplus4 = $shpplus4 * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
		${'skaihuku'.$ssp} ="<font class=\"white\" size=5>メンバーのHPが$shpplus1回復した!!</font><br>";
	}
	}
	}
}
1;