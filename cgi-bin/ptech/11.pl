sub phissatu{
	if ($khp_flg>0 and int(rand(100)) < 25) {
		$hpplus1 += $dmg4 + int(rand($chara[46]*5));
		$hpplus2 += $dmg4 + int(rand($chara[46]*5));
		$hpplus3 += $dmg4 + int(rand($chara[46]*5));
		$hpplus4 += $dmg4 + int(rand($chara[46]*5));
		$dmg4 = 0;
		$com4 .="<font class=\"white\" size=5>ゴーチルヒーリング!!</font><br>";
		$kaihuku4 .= "メンバー のＨＰが $hpplus1 回復した！♪";
	}
}
sub patowaza{}
1;