sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$rnd=int(rand(4));
		$scom1 .= "<font class=\"red\" size=5>必殺技裁判！！</font><br>";
		$sake1 -= 100000;
		$sake2 -= 100000;
		$sake3 -= 100000;
		$sake4 -= 100000;
		if($rnd==0){
			$scom1 .= "<font class=\"red\" size=5>無罪！！！</font><br>";
			$sdmg1 = int($sdmg1/10000000);
		}
		if($rnd==1 or $rnd==2){
			$scom1 .="<font class=\"red\" size=5>有罪！！！</font>";
			$sdmg1 = int($sdmg1 * int(rand(7)+2));
		}
		if($rnd==3){
			$scom1 .="<font class=\"red\" size=5>死刑！！！</font>";
			$taisyo1 = 1;
			if($khp_flg>0){$khp_flg=int(rand(1))+1;}
			if($mem1hp_flg>0){$mem1hp_flg=int(rand(2));}
			if($mem2hp_flg>0){$mem2hp_flg=int(rand(2));}
			if($mem3hp_flg>0){$mem3hp_flg=int(rand(2));}
			if(int(rand(3))==0){
				$siki=int(rand($smem1hp_flg/10));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>少回復!!HPが$siki回復した♪</font>";
			}elsif(int(rand(5))==0){
				$siki=int(rand($smem1hp_flg));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>中回復!!HPが$siki回復した♪</font>";
			}elsif(int(rand(8))==0){
				$siki=int(rand($smem1hp/10));
				$smem1hp_flg+=$siki;
				$scom1 .="<font class=\"yellow\" size=2>大回復!!HPが$siki回復した♪</font>";
			}
		}
		if ($i>25){
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$scom1 .="<font class=\"red\" size=5>大死刑！！！<font size=4>ッフ…逃げられると思ったか…？ｗ</font>";
		}
	}
}
sub mons_atowaza{}
1;