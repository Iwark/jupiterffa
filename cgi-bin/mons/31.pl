sub mons_waza{
	if(int(rand(10))<3) {
		if($chara[0] ne "jupiter"){
		$sdmg1=$sdmg1*int(rand(100)+10);
		}
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ŸÓg—ó‰ÎI</font><br>
EOM
	}
}
sub mons_atowaza{}
1;