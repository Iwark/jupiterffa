sub phissatu{
	if (int(rand(100)) < 20) {
		$com4 .="<font class=\"red\" size=5>˜r‚ğŒƒ‚µ‚­U‚Á‚½!!</font><br>";
		$dmg4 += int($dmg4 / int(rand(2)+1)) + int(rand($dmg4));
		$staisyo4 = 4 ;
		$ssake1 -= 30;
		$ssake2 -= 30;
		$ssake3 -= 30;
		$ssake4 -= 30;
	}
}
sub patowaza{}
1;