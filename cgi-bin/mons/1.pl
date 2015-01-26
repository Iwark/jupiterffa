sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sdmg1 += int($sdmg1 / int(rand(2)+1)) + int(rand($sdmg1));
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>生半可な覚悟でこの私と戦いに来たのか！？エッグ\ソ\ー\ド!!</font><br>
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