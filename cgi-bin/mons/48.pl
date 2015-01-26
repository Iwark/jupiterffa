sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 100000;
		$sake2 -= 100000;
		$sake3 -= 100000;
		$sake4 -= 100000;
		$shpplus1 = int(rand($smem1hp_flg));
		$skaihuku1 = "$ssmname1のＨＰが$shpplus1回復した！";
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>シャニガミドレイン！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;