sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$rnd=int(rand(4));
		$scom1 .= "<font class=\"red\" size=5>�K�E�Z�ٔ��I�I</font><br>";
		$sake1 -= 100000;
		$sake2 -= 100000;
		$sake3 -= 100000;
		$sake4 -= 100000;
		if($rnd==0){
			$scom1 .= "<font class=\"red\" size=5>���߁I�I�I</font><br>";
			$sdmg1 = int($sdmg1/10000000);
		}
		if($rnd==1 or $rnd==2){
			$scom1 .="<font class=\"red\" size=5>�L�߁I�I�I</font>";
			$sdmg1 = int($sdmg1 * int(rand(7)+2));
		}
		if($rnd==3){
			$scom1 .="<font class=\"red\" size=5>���Y�I�I�I</font>";
			$taisyo1 = 1;
			if($khp_flg>0){$khp_flg=int(rand(1))+1;}
			if($mem1hp_flg>0){$mem1hp_flg=int(rand(2));}
			if($mem2hp_flg>0){$mem2hp_flg=int(rand(2));}
			if($mem3hp_flg>0){$mem3hp_flg=int(rand(2));}
			if(int(rand(3))==0){
				$siki=int(rand($smem1hp_flg/10));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>����!!HP��$siki�񕜂�����</font>";
			}elsif(int(rand(5))==0){
				$siki=int(rand($smem1hp_flg));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>����!!HP��$siki�񕜂�����</font>";
			}elsif(int(rand(8))==0){
				$siki=int(rand($smem1hp/10));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>���!!HP��$siki�񕜂�����</font>";
			}
		}
		if ($i>25){
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$scom1 .="<font class=\"red\" size=5>�厀�Y�I�I�I<font size=4>�b�t�c��������Ǝv�������c�H��</font>";
		}
	}
}
sub mons_atowaza{}
1;