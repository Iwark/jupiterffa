sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 5000;
		$sake2 -= 5000;
		$sake3 -= 5000;
		$sake4 -= 5000;
		$taisyo1 = 4;
		$shpplus1 = int($sdmg1 /2);
		$skaihuku1 = "$ssmname1のＨＰが$shpplus1回復した！";
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>オメジャレーザー！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;