sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 9999;
		$sake2 -= 9999;
		$sake3 -= 9999;
		$sake4 -= 9999;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>悪魔に魂を売ったのさ…ほんの少しなっ！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;