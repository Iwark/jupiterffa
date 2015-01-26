sub phissatu{
	if (int(rand(100)) < 10) {
		$mem4hit_ritu=25;
		$ppp=int(rand($chara[46]/10)+1);
		if($chara[46]<20){$ppp+=100;}
		$dmg4 = $dmg4 * $ppp;
		$com4 .="<font class=\"white\" size=5>\‘å\–\\‚êII</font><br>";
	}
}
sub patowaza{}
1;