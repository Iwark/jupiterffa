sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 100;
		$sake2 -= 100;
		$sake3 -= 100;
		$sake4 -= 100;
		$sdmg1 += int(rand(100000));
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>おまえは豚インフルエンザだーっ。</font><br>
EOM
	}
}
sub mons_atowaza{}
1;