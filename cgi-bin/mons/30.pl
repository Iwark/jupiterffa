sub mons_waza{
	if($chara[0] eq "jupiter" and $chara[0] eq "aaa"){
		$sdmg1=0;$sdmg2=0;
	}elsif ($i==1) {
		if ($item[1]<0){
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$sdmg1=$sdmg1*1111;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>貴様・・・おかしなものを装備しているようだな・・・。その装備で戦うことは許可しない！！</font><br>
EOM
		}elsif($item[0] eq "闇封じの剣"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣！闇封じの剣…！闇の衣が効果を発揮しない！</font><br>
EOM
		}elsif($item[3] eq "闇の羽衣"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣！闇の羽衣…！闇の衣が効果を発揮しない！</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣を発動した！全ての攻撃は猿猫丸に吸い込まれる！！</font><br>
EOM
		}
	}elsif(int(rand(10))<3) {
		$sdmg1=$sdmg1*1111;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>必死猿猫エンド！！</font><br>
EOM
	}elsif(int(rand(10))<3) {
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>必中猿猫エンド！！</font><br>
EOM
	}elsif(int(rand(5))<3) {
		if($item[0] eq "闇封じの剣"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣猿猫エンド！闇封じの剣…！闇の衣が効果を発揮しない！</font><br>
EOM
		}elsif($item[3] eq "闇の羽衣"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣猿猫エンド！闇の羽衣…！闇の衣が効果を発揮しない！</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>闇の衣猿猫エンド！！</font><br>
EOM
		}
	}elsif($chara[51] or $chara[52] or $chara[53] or $chara[54]){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$sdmg1=$sdmg1*111;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>アビリティ封猿殺猫剣丸！！！</font><br>
EOM
	}
}
sub mons_atowaza{}
1;