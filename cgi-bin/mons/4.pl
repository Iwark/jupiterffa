sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 30;
		$sake2 -= 30;
		$sake3 -= 30;
		$sake4 -= 30;
		$sdmg1 = int($sdmg1 / 2) ;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>暗黒魔法ダーク!!</font><br>
EOM
	}
}
sub mons_atowaza{}
1;