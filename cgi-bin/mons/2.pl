sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 999999;
		$sake2 -= 999999;
		$sake3 -= 999999;
		$sake4 -= 999999;
		$sdmg1 += $sdmg1 * int(rand(10)+1) + int(rand($sdmg1));
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>ギギ…消えれ…シャド\ー\ウェーブ!!</font><br>
EOM
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