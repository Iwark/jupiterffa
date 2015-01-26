sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 300;
		$sdmg1 = $sdmg1*10;
		$scom1 .= "<font class=\"red\" size=5>死への誘い！！！</font><br>";
	}
	elsif ($i>10){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>さらばだ！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;