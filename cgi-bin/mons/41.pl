sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 1000;
		$sake2 -= 1000;
		$sake3 -= 1000;
		$sake4 -= 1000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>右ストレート！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;