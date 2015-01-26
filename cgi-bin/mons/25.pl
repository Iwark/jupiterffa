sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
		$sake1 -= 100;
		$sake2 -= 100;
		$sake3 -= 100;
		$sake4 -= 100;
		$sdmg1 += int(rand(100000));
		$taisyo1 = 4;
	if($smem1hp_flg<5000000){$shpplusu1 = int($sdmg1 /2);}
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>‚±‚ê‚É‚±‚è‚½‚ç“ñ“x‚Æˆ«‚³‚ð‚µ‚È‚¢‚±‚Æ‚¾‚È‚Á</font><br>
EOM
	}
}
sub mons_atowaza{}
1;