sub hissatu6{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					if($item[0] eq "����Ƃ炷�؂����" or $item[0] eq "�܂���ĂԂꂢ���[" or $item[0] eq "�ŕ����̌�" or $item[0] eq "10����"){
						$item[1]=0;
						&item_regist;
						${'com'.$ab} .="<font class=\"red\" size=5>$item[0]����ꂽ�I�I�I</font><br>";
					}elsif ($chara[24]==9999 or $chara[24]==0) {
					$k=1;
					${'dmg'.$ab} = ${'dmg'.$ab}*99;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���@�I�I�I</font><br>";
					if($chara[70]>=1 and int(rand(20))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>��S�̈ꌂ�I�I</font><br>";
					}
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					if(${'mem'.$ri.'item'}[0] eq "����Ƃ炷�؂����" or ${'mem'.$ri.'item'}[0] eq "�܂���ĂԂꂢ���[" or ${'mem'.$ri.'item'}[0] eq "�ŕ����̌�" or ${'mem'.$ri.'item'}[0] eq "10����"){
					}elsif (${'mem'.$ri}[24]==9999 or ${'mem'.$ri}[24]==0) {
					$k=1;
					${'dmg'.$ab} = ${'dmg'.$ab}*99;
					${'com'.$ab} .="<font class=\"red\" size=5>�K�E���@�I�I�I</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				if(${'smem'.$sab.'item'}[0] eq "����Ƃ炷�؂����" or ${'smem'.$sab.'item'}[0] eq "�܂���ĂԂꂢ���[" or ${'smem'.$sab.'item'}[0] eq "�ŕ����̌�" or ${'smem'.$sab.'item'}[0] eq "10����"){
				}elsif (${'smem'.$sab}[24]==9999 or ${'smem'.$sab}[24]==0) {
					$k=1;
					${'sdmg'.$sab} = ${'sdmg'.$sab}*99;
					${'scom'.$sab} .="<font class=\"red\" size=5>�K�E���@�I�I�I</font><br>";
				}
			}
		}
	}
}
sub atowaza{
}
1;