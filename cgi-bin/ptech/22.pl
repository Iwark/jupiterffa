sub phissatu{
	if (int(rand(100)) < 50) {
		$com4 .="<font class=\"yellow\" size=5>エッグ\ソ\ー\ド！！</font><br>";
		$dmg4 += int($dmg4 / int(rand(2)+1)) + int(rand($dmg4*10));
		$staisyo4 = 4 ;
		$mem4hit_ritu=80;
	}
}
sub patowaza{}
1;