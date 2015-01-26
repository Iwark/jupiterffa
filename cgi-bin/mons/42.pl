sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 2000;
		$sake2 -= 2000;
		$sake3 -= 2000;
		$sake4 -= 2000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>‚­‚¢‚¿‚¬‚éII</font><br>
EOM
	}
}
sub mons_atowaza{}
1;