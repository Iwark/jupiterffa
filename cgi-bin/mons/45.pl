sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 5000;
		$sake2 -= 5000;
		$sake3 -= 5000;
		$sake4 -= 5000;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�G�O�[�W�F\�\\�[\�h�I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;