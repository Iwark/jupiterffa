sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 100;
		$sake3 -= 100;
		$sake4 -= 100;
		$sake8 -= 100;
		$sdmg1 = int($sdmg1 * 4 / 3) ;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>ƒMƒ‹ƒ_ƒ“‚ğ‚È‚ß‚é‚ñ‚¶‚á‚È‚Ÿ‚Ÿ‚¢I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;