sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 300;
		$sake2 -= 300;
		$sake3 -= 300;
		$sake4 -= 300;
		$shpplusu1 = int($sdmg1 /2);
		$skaihuku1 = "$ssmname1�̂g�o��$shpplus1�񕜂����I";
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�I���K���[�U�[�I</font><br>
EOM
	}
	elsif ($i>10){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>����΂��I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;