sub spell6{
	for($spe=1;$spe<5;$spe++){
	if($spe==$sp){
	${'maho'.$sp}=8;
	$sdmg1=int($sdmg1*0.7);$sdmg2=int($sdmg2*0.7);$sdmg3=int($sdmg3*0.7);$sdmg4=int($sdmg4*0.7);
	if($sp==1){
		if($chara[24]==1335){${'dmg'.$sp} = int(${'dmg'.$sp} * 9);}
		if($chara[29]==2309){${'dmg'.$sp} = int(${'dmg'.$sp} * 8);}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣ブリザガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>$chara[4]は黒魔法ブリザガを放った!!</font><br>";
			if ($chara[55]==32 or $chara[56]==32 or $chara[57]==32 or $chara[58]==32){
				${'dmg'.$sp} = ${'dmg'.$sp} * 2;
				${'com'.$sp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
			}
		}
	}else{
		$ri=$sp-1;
		if(${'mem'.$ri}[24]==1335){${'dmg'.$sp} = int(${'dmg'.$sp} * 9);}
		if(${'mem'.$ri}[29]==2309){${'dmg'.$sp} = int(${'dmg'.$sp} * 8);}
		if($mahoken==1){
			${'com'.$sp} .="<font class=\"red\" size=5>魔法剣ブリザガ!!</font><br>";
		}else{
			${'com'.$sp} .="<font class=\"red\" size=5>${'mem'.$ri}[4]は黒魔法ブリザガを放った!!</font><br>";
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
	$dmg1=int($dmg1*0.7);$dmg2=int($dmg2*0.7);$dmg3=int($dmg3*0.7);$dmg4=int($dmg4*0.7);
	if(${'smem'.$ssp}[24]==1335){${'sdmg'.$ssp} = int(${'sdmg'.$ssp} * 9);}
	if(${'smem'.$ssp}[29]==2309){${'sdmg'.$ssp} = int(${'sdmg'.$ssp} * 8);}
	if($mahoken==1){
		${'scom'.$ssp} .="<font class=\"red\" size=5>魔法剣ブリザガ!!</font><br>";
	}else{
		${'scom'.$ssp} .="<font class=\"red\" size=5>${'smem'.$ssp}[4]は黒魔法ブリザガを放った!!</font><br>";
		if (${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32 or ${'smem'.$ssp}[55]==32){
			${'sdmg'.$ssp} = ${'sdmg'.$ssp} * 2;
			${'scom'.$ssp} .="<font class=\"yellow\" size=5>秘技、連続魔法発動!!</font><br>";
		}
	}
	}
	}
}
1;