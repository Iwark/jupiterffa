sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 5000;
		$sake2 -= 5000;
		$sake3 -= 5000;
		$sake4 -= 5000;
		$taisyo1 = 4;
		$shpplus1 = int($sdmg1 /2);
		$skaihuku1 = "$ssmname1�̂g�o��$shpplus1�񕜂����I";
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�I���W�����[�U�[�I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;