sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 999999;
		$sake2 -= 999999;
		$sake3 -= 999999;
		$sake4 -= 999999;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>年寄りの強さを証明する一打を放つ！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;