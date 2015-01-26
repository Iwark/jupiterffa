sub mons_waza{
	if ($i==1) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ようこそ、超魔王ＥＸの城へ…。</font><br>
EOM
	}elsif ($i==2) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>どうした。もっと強く当たってこい！</font><br>
EOM
	}elsif ($i==3) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>そんなものか…？</font><br>
EOM
	}elsif ($i==4) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>…期待はずれだな…出直して来い！</font><br>
EOM
	}else{
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