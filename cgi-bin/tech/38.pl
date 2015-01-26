sub hissatu38{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技召喚！！！</font><br>";
					if($chara[18]<100){
					${'com'.$ab} .="<font class=\"red\" size=5>イフリートの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 2);
					}elsif($chara[18]<300){
					${'com'.$ab} .="<font class=\"red\" size=5>ラムウの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					}elsif($chara[18]<500){
					${'com'.$ab} .="<font class=\"red\" size=5>シヴァの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					}else{
					${'com'.$ab} .="<font class=\"red\" size=5>ジュピタの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技召喚！！！</font><br>";
					if(${'mem'.$ri}<100){
					${'com'.$ab} .="<font class=\"red\" size=5>イフリートの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 2);
					}elsif(${'mem'.$ri}<300){
					${'com'.$ab} .="<font class=\"red\" size=5>ラムウの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 3);
					}elsif(${'mem'.$ri}<500){
					${'com'.$ab} .="<font class=\"red\" size=5>シヴァの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 4);
					}else{
					${'com'.$ab} .="<font class=\"red\" size=5>ジュピタの力を借りた！</font><br>";
					${'dmg'.$ab} = int(${'dmg'.$ab} * 5);
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技召喚！！！</font><br>";
					if(${'smem'.$sab}<100){
					${'scom'.$sab} .="<font class=\"red\" size=5>イフリートの力を借りた！</font><br>";
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 2);
					}elsif(${'smem'.$sab}<300){
					${'scom'.$sab} .="<font class=\"red\" size=5>ラムウの力を借りた！</font><br>";
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 3);
					}elsif(${'smem'.$sab}<500){
					${'scom'.$sab} .="<font class=\"red\" size=5>シヴァの力を借りた！</font><br>";
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 4);
					}else{
					${'scom'.$sab} .="<font class=\"red\" size=5>ジュピタの力を借りた！</font><br>";
					${'sdmg'.$sab} = int(${'sdmg'.$sab} * 5);
					}
			}
		}
	}
}
sub atowaza{}
1;