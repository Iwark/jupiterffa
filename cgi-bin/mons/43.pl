sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 3000;
		$sake2 -= 3000;
		$sake3 -= 3000;
		$sake4 -= 3000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�R�c�W���U���I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;