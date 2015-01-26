sub mons_waza{
	$comts=1;
	if($smem1hp_flg<1){
		$comts++;
	}
	${'scom'.$comts} .= <<"EOM";
	<font class=\"red\" size=5>修行に来たのですね…あなたの力を見せてください！</font><br>
EOM
	if($chara[51]==64 or $chara[52]==64 or $chara[53]==64 or $chara[54]==64
	or $mem1[51]==64 or $mem1[52]==64 or $mem1[53]==64 or $mem1[54]==64
	or $mem2[51]==64 or $mem2[52]==64 or $mem2[53]==64 or $mem2[54]==64){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>私達を裁くんですか…？クスクス</font><br>
EOM
	}
	if(int(rand(10))==0){
		$chara[20]=int(rand($chara[20])+1);
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>調子に乗ってはいけませんよ…！</font><br>
EOM
	}
	$hpp=0;
	if($smem1hp_flg<1){$hpp++;}if($smem2hp_flg<2){$hpp++;}
	if($hpp>0 and int(rand(5))==0){
		$i+=int(rand(20));
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>やりますね…！勝負を急ぎましょう！</font><br>
EOM
	}
	if($i>29){
		$khp_flg=0;$mem1hp_flg=0;$mem2hp_flg=0;$mem3hp_flg=0;
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>暗くなってきたので今日はこの程度にしておきましょう。</font><br>
EOM
	}
}
sub mons_atowaza{}
1;