sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 100;
		$sake2 -= 100;
		$sake3 -= 100;
		$sake4 -= 100;
		$sdmg1 += int($sdmg1 / 10) ;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>ギガフレイム！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;