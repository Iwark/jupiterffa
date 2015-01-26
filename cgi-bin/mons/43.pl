sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 3000;
		$sake2 -= 3000;
		$sake3 -= 3000;
		$sake4 -= 3000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>ŒR’cW’†UŒ‚II</font><br>
EOM
	}
}
sub mons_atowaza{}
1;