sub phissatu{
	if (int(rand(100)) < 10) {
			$com4 .="<font class=\"white\" size=5>ゴーチルフェニックス!!</font><br>";
			$kaihuku4 .= "ＰＴメンバーが全員蘇り、じわじわと動き出した！！";
		if($khp_flg<0){
			$khp_flg=int($chara[16]/4);
		}
		if($mem1[4] and $mem1hp_flg<0){
			$mem1hp_flg=int($mem1[16]/4);
		}
		if($mem2[4] and $mem2hp_flg<0){
			$mem2hp_flg=int($mem2[16]/4);
		}
	}
}
sub patowaza{}
1;