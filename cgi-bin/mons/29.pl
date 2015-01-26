sub mons_waza{
	if ($i==1) {
		if($chara[14]!=44){
		$scom1 .= <<"EOM";
			<font class=\"red\" size=5>我が恐れるは、屋敷守のみ！お主では話にならんな！！</font><br>
EOM
		}else{
		$scom1 .= <<"EOM";
			<font class=\"red\" size=5>お・・・お主、屋敷守か！！カンベンしてくれ！！</font><br>
EOM
		}
	}elsif ($i==2) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>おいおい…。</font><br>
EOM
	}elsif ($i==3) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>なんだよ…。</font><br>
EOM
	}elsif ($i==4) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ふ…そろそろ帰るか…。</font><br>
EOM
	}elsif($i==5 or $i>20){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>さらばだ！</font><br>
EOM
	}elsif($item[0] eq "げっちゅう" and $chara[196]==2 and $chara[52]==63){
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>私に仲間になれとな…見たところ中々の手練れ…それも面白そうだな…。</font><br>
EOM
		$smem1hp_flg = int($smem1hp_flg / 100);
	}
}
sub mons_atowaza{}
1;