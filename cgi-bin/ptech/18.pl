sub phissatu{
	if (int(rand(100)) < 15) {
			$com4 .="<font class=\"white\" size=5>エンジェルフェニックス!!</font><br>";
			$kaihuku4 .= "ＰＴメンバーが全員蘇り、じわじわと動き出した！！";
		if($khp_flg<0){
			$khp_flg=$chara[16];
		}
		if($mem1[4] and $mem1hp_flg<0){
			$mem1hp_flg=$mem1[16];
		}
		if($mem2[4] and $mem2hp_flg<0){
			$mem2hp_flg=$mem2[16]/2;
		}
	}
}
sub patowaza{}
1;