sub hissatu67{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					if(int(rand(20))==0){
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���񂾂ӂ�I�I�I�E�E�E���A�����B</font><br>";
					}else{
					$sinda=1;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���񂾂ӂ�I�I�I�ۂ��[�B</font><br>";
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					if(int(rand(20))==0){
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���񂾂ӂ�I�I�I�E�E�E���A�����B</font><br>";
					}else{
					$sinda=$ab;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���񂾂ӂ�I�I�I�ۂ��[�B</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$sinda=$sab+4;
				${'scom'.$sab} .="<font class=\"red\" size=5>�K�E���񂾂ӂ�I�I�I�E�E�E���A�����B</font><br>";
			}
		}
	}
}
sub atowaza{}
1;