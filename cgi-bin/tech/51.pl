sub hissatu51{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					${'dmg'.$ab} = 0;
					if($sdmg1){$sdmg1-=int(rand(10000));}
					if($sdmg2){$sdmg2-=int(rand(10000));}
					if($sdmg3){$sdmg3-=int(rand(10000));}
					if($sdmg4){$sdmg4-=int(rand(10000));}
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技フライ返し！！！</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					${'dmg'.$ab} = 0;
					if($sdmg1){$sdmg1-=int(rand(10000));}
					if($sdmg2){$sdmg2-=int(rand(10000));}
					if($sdmg3){$sdmg3-=int(rand(10000));}
					if($sdmg4){$sdmg4-=int(rand(10000));}
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技フライ返し！！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				${'sdmg'.$sab} = 0;
					if($dmg1){$dmg1-=int(rand(10000));}
					if($dmg2){$dmg2-=int(rand(10000));}
					if($dmg3){$dmg3-=int(rand(10000));}
					if($dmg4){$dmg4-=int(rand(10000));}
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技フライ返し！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;