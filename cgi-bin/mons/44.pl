sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 4000;
		$sake2 -= 4000;
		$sake3 -= 4000;
		$sake4 -= 4000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�s�ӑł��I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;