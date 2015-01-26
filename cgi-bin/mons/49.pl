sub mons_waza{
	$mem1hit_ritu = 1;
	$mem2hit_ritu = 1;
	$mem3hit_ritu = 1;
	$mem4hit_ritu = 1;
	$comts=1;
	if($smem1hp_flg<1){
		$comts++;
		if($smem2hp_flg<1){
			$comts++;
			if($smem3hp_flg<1){
				$comts++;
			}
		}
	}
	${'scom'.$comts} .= <<"EOM";
	<font class=\"red\" size=5>謎の気配で命中率がグンと下がった！！</font><br>
EOM
	if($staisyo1==4 or $staisyo2==4 or $staisyo3==4 or $staisyo4==4){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
	${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>謎の気配で攻撃を封じられた！</font><br>
EOM
	}
	if($chara[51]==64 or $chara[52]==64 or $chara[53]==64 or $chara[54]==64
	or $mem1[51]==64 or $mem1[52]==64 or $mem1[53]==64 or $mem1[54]==64
	or $mem2[51]==64 or $mem2[52]==64 or $mem2[53]==64 or $mem2[54]==64){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>謎の気配で裁判を封じられた！</font><br>
EOM
	}
	if(int(rand(10))==0){
		$chara[20]=int(rand($chara[20])+1);
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>謎の気配で連勝率が落ちた！</font><br>
EOM
	}
	$hpp=0;
	if($smem1hp_flg<1){$hpp++;}if($smem2hp_flg<2){$hpp++;}if($smem3hp_flg<1){$hpp++;}if($smem4hp_flg<1){$hpp++;}
	if($hpp>2 and int(rand(5))==0){
		$i=28+int(rand(4));
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>謎の気配で時空が飛ばされた！</font><br>
EOM
	}
	if($i>29){
		$khp_flg=0;$mem1hp_flg=0;$mem2hp_flg=0;$mem3hp_flg=0;
		${'scom'.$comts} .= <<"EOM";
		<font class=\"red\" size=5>謎の気配で消滅させられた！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;