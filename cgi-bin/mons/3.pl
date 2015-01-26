sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 30;
		$sake2 -= 30;
		$sake3 -= 30;
		$sake4 -= 30;
		$sdmg1 += int($sdmg1 / int(rand(2)+1)) + int(rand($sdmg1));
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>ƒMƒKƒ“ƒgƒI[ƒN‚Í˜r‚ğŒƒ‚µ‚­U‚Á‚½!!</font><br>
EOM
	}
	elsif ($i>10){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>‚³‚ç‚Î‚¾I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;