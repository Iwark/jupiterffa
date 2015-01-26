sub hissatu30{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(400))){
					$k=1;
					if(int(rand(4))==0){$sdmg1=0;}
					if(int(rand(4))==0){$sdmg2=0;}
					if(int(rand(4))==0){$sdmg3=0;}
					if(int(rand(4))==0){$sdmg4=0;}
					${'dmg'.$ab} = int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z˜f‚í‚·IUŒ‚‚ğ•Ô‚µ‚½I</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>‰ïS‚ÌˆêŒ‚II</font><br>";
					}
					if($chara[31] eq "0043"){
						if(int(rand(3))==0){$sdmg1=0;}
						if(int(rand(3))==0){$sdmg2=0;}
						if(int(rand(3))==0){$sdmg3=0;}
						if(int(rand(3))==0){$sdmg4=0;}
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>–À˜fŒ‹ŠE”­“®II</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(400))){
					$k=1;
					if(int(rand(4))==0){$sdmg1=0;}
					if(int(rand(4))==0){$sdmg2=0;}
					if(int(rand(4))==0){$sdmg3=0;}
					if(int(rand(4))==0){$sdmg4=0;}
					${'dmg'.$ab} = int(($sdmg1+$sdmg2+$sdmg3+$sdmg4) / 4);
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z˜f‚í‚·IUŒ‚‚ğ•Ô‚µ‚½I</font><br>";
					if(${'mem'.$ri}[31] eq "0043"){
						if(int(rand(3))==0){$sdmg1=0;}
						if(int(rand(3))==0){$sdmg2=0;}
						if(int(rand(3))==0){$sdmg3=0;}
						if(int(rand(3))==0){$sdmg4=0;}
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>–À˜fŒ‹ŠE”­“®II</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(400))){
				$k=1;
				if(int(rand(4))==0){$dmg1=0;}
				if(int(rand(4))==0){$dmg2=0;}
				if(int(rand(4))==0){$dmg3=0;}
				if(int(rand(4))==0){$dmg4=0;}
				${'sdmg'.$sab} = int(($dmg1+$dmg2+$dmg3+$dmg4) / 4);
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z˜f‚í‚·IUŒ‚‚ğ•Ô‚µ‚½I</font><br>";
				if(${'smem'.$sab}[31] eq "0043"){
					if(int(rand(3))==0){$dmg1=0;}
					if(int(rand(3))==0){$dmg2=0;}
					if(int(rand(3))==0){$dmg3=0;}
					if(int(rand(3))==0){$dmg4=0;}
					${'sdmg'.$sab} = ${'sdmg'.$sab} * int(rand(10));
					${'scom'.$sab} .="<font class=\"red\" size=5>–À˜fŒ‹ŠE”­“®II</font><br>";
				}
			}
		}
	}
}
sub atowaza{
}
1;