sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 999999;
		$sake2 -= 999999;
		$sake3 -= 999999;
		$sake4 -= 999999;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�N���̋������ؖ������ł���I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;