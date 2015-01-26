sub mons_waza{
	if(int(rand(10))<3) {
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>•KŒ‚‹¥nI</font><br>
EOM
	}
}
sub mons_atowaza{}
1;