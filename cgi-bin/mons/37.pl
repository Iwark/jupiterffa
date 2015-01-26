sub mons_waza{
	if($swit!=1){
		$hint=int($sec*3/5)+1;
		$swit=1;
	}
	if($chara[51]==64 or $chara[52]==64 or $chara[53]==64 or $chara[54]==64
	or $mem1[51]==64 or $mem1[52]==64 or $mem1[53]==64 or $mem1[54]==64
	or $mem2[51]==64 or $mem2[52]==64 or $mem2[53]==64 or $mem2[54]==64){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*1111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>何にも悪いことしてないのに裁判にかけるなんてひどいじょ！</font><br>
EOM
		$shpplus1 = int($sdmg1*1111);
		$smem1hp_flg = $smem1hp_flg + 3000000000000000000 - 1;
	}elsif($chara[51]==46 or $chara[52]==46 or $chara[53]==46 or $chara[54]==46
	or $mem1[51]==46 or $mem1[52]==46 or $mem1[53]==46 or $mem1[54]==46
	or $mem2[51]==46 or $mem2[52]==46 or $mem2[53]==46 or $mem2[54]==46){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*1111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>何にも悪いことしてないのに逮捕するなんてひどいじょ！</font><br>
EOM
		$shpplus1 = int($sdmg1*1111);
		$smem1hp_flg = $smem1hp_flg + 3000000000000000000 - 1;
	}elsif($chara[51]==$hint){
		if($smem1hp_flg<104444444){
		$dmg1=int(rand(84444444));$dmg2=int(rand(84444444));$dmg3=int(rand(84444444));$dmg4=int(rand(84444444));
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*111111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>くひゃぁ！まずいじょ！攻撃するなじょ！だいぼ～ぎょ！！</font><br>
EOM
		}else{
		$dmg1=int(rand(84444444));$dmg2=int(rand(84444444));$dmg3=int(rand(84444444));$dmg4=int(rand(84444444));
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*11111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>くひゃぁ！昔なつかしい技を使うなじょ！</font><br>
EOM
		}
	}elsif(int(rand(30))==0){
	$scom1 .= <<"EOM";
	<font class=\"red\" size=5>もう$hour時$min分$sec秒か…寝る時間だじょ。ばいばい。</font><br>
EOM
	$mgold=0;
	$smem1hp_flg=1;
	}else{
	$dmg1=100000;$dmg2=100000;$dmg3=100000;$dmg4=100000;
	$sake1 -= 9999;$sake2 -= 9999;
	$sake3 -= 9999;$sake4 -= 9999;
	$taisyo1 = 4;
	$scom1 .= <<"EOM";
	<font class=\"red\" size=5>たまには愛用ＣＤの$hint番の曲でも聴きたいじょ～♪</font><br>
EOM
	}
	if($i>25){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
	$taisyo1 = 4;
	$scom1 .= <<"EOM";
	<font class=\"red\" size=5>さらばだじょ～♪</font><br>
EOM
	}
}
sub mons_atowaza{}
1;