sub phissatu{
	if (int(rand(100)) < 25) {
		$zzz=int(rand(3));
		if($zzz==0 and $khp_flg<0){
			$sosei=1;
			$khp_flg=1;
			$dmg4 = 0;
			$com4 .="<font class=\"white\" size=5>ゴーチルライブ!!</font><br>";
			$kaihuku4 .= "$chara[4]が蘇った！";
		}
		if($zzz==1 and $mem1[4] and $mem1hp_flg<0){
			$sosei=3;
			$mem1hp_flg=1;
			$dmg4 = 0;
			$com4 .="<font class=\"white\" size=5>ゴーチルライブ!!</font><br>";
			$kaihuku4 .= "$mem1[4]が蘇った！";
		}
		if($zzz==2 and $mem2[4] and $mem2hp_flg<0){
			$sosei=4;
			$mem2hp_flg=1;
			$dmg4 = 0;
			$com4 .="<font class=\"white\" size=5>ゴーチルライブ!!</font><br>";
			$kaihuku4 .= "$mem2[4]が蘇った！";
		}
	}
}
sub patowaza{}
1;