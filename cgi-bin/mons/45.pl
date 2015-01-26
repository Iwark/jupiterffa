sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 5000;
		$sake2 -= 5000;
		$sake3 -= 5000;
		$sake4 -= 5000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>エグージェ\ソ\ー\ド！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;