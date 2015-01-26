sub mons_waza{
	if ($i==1) {
		if ($item[1]<0){
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>無への追放！！</font><br>
EOM
		}elsif(int(rand(10))<5)
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>無への追放！！</font><br>
EOM
		}elsif($item[0] eq "闇封じの剣"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣！む…それは、闇封じの剣…！闇の衣が効果を発揮しない！</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣を発動した！全ての攻撃を闇に吸い込む！・・・この一撃を受けて立っていられないものに、この町で戦う資格はない！！</font><br>
EOM
		}
	}elsif(int(rand(10))<7) {
		$sdmg1=$sdmg1*1111;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ジュピタワールドエンド！！</font><br>
EOM
	}elsif(int(rand(10))<7) {
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>無への追放！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;