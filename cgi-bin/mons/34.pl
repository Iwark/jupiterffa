sub mons_waza{
	if(int(rand(10))<3) {
		$shpplusu1 = int($sdmg1 /2);
		$shpplusu2 = int($sdmg2 /2);
		$shpplusu3 = int($sdmg3 /2);
		$shpplusu4 = int($sdmg4 /2);
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>–½‹~–‚•I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;