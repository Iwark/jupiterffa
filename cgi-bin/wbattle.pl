#--------------#
#　関数初期化　#
#--------------#
sub shokika {
	$dmg1 = 0;
	$sdmg1 = 0;
	$clit1 = "";
	$clit2 = "";
	$com1 = "";
	$scom1 = "";
	$kawasi1 = "";
	$kawasi2 = "";
	$mem1hit_ritu = int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16];
	$sake1 = int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17];
	$smem1hit_ritu = int($winner[9] / 3 + $winner[11] / 10 + $winner[30] / 3) + 40 + $winner[23] + $winner[52];
	$ssake1 = int($winner[9] / 10 + $winner[11] / 20 + $winner[30]/10) + $winner[26] + $winner[35];
	$kaihuku1 = "";
	$skaihuku1 = "";
	$kclit = 0;
	$wclit = 0;
	$kmclit = 0;
	$wmclit = 0;
	$hpplus1 = 0;
	$shpplus1 = 0;
	$taisyo = 0;
}

#------------#
#　HPの計算　#
#------------#
sub hp_sum {
	$khp_flg = $khp_flg - $sdmg1 + $hpplus1;
	if ($khp_flg > $chara[16]) { $khp_flg = $chara[16]; }
	$whp_flg = $whp_flg - $dmg1 + $shpplus1;
	if ($whp_flg > $winner[16]) { $whp_flg = $winner[16]; }
}

#------------#
#　勝敗条件　#
#------------#
sub winlose {
	if ($whp_flg <= 0 and $khp_flg > 0) { $win = 1; last; }
	elsif ($khp_flg <= 0 and $whp_flg > 0) { $win = 0; last; }
	elsif ($khp_flg <= 0 and $whp_flg <= 0) { $win = 2; last; }
	else { $win = 3; }
}

#------------------#
#　チャンプの攻撃　#
#------------------#
sub winner_atack {
	$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
	if ($winner[60]==33 or $winner[61]==33 or $winner[62]==33 or $winner[63]==33){$mahoken=1;}else{$mahoken=0;}
	if ($winner[64] and int(rand(4 - $mahoken * 3))==0) {
		$ccc=1;
		$ssp=1;
		$sdmg1 = $winner[8] * 4 + $winner[22] * 4 * int($winner[8]/10);
		if($mahoken == 1){$sdmg1 += $winner[7] * 4 + $winner[22] * 4 * int($winner[7]/10+1);}
		require "./spell/$winner[64].pl";
		$spell="spell$winner[64]";
		&$spell;
	}
	if(!$ccc){
		$scom1 = "$winner[3]は、$winner[21]で攻撃！！";
		if( $winner[7] > $winner[8] ){
			$sdmg1 = $winner[7] * 4 + $winner[22] * 4 * int($winner[7]/10);
		}else{
			$sdmg1 = $winner[8] * 4 + $winner[22] * 4 * int($winner[8]/10);
		}
	}
	if ($winner[60]==21 or $winner[61]==21 or $winner[62]==21 or $winner[63]==21){
		$sdmg1 += ($winner[15]-$whp_flg);
	}
	#持久戦
	if ($winner[60]==78 or $winner[61]==78 or $winner[62]==78 or $winner[63]==78){
		if($i>19){$sdmg1 *= 8;}
	}
	#必殺拳法？
	if ($sudedmg==1) {
		$sdmg1 = $sdmg1 * 777;
	}
	if ($winner[60]==80 or $winner[61]==80 or $winner[62]==80 or $winner[63]==80){
		$mem1hit_ritu=$mem1hit_ritu*100;
		$smem1hit_ritu=$smem1hit_ritu*100;
	}
	if ($winner[60]==81 or $winner[61]==81 or $winner[62]==81 or $winner[63]==81){
		$sake1=$sake1*10;
		$ssake1=$ssake1*10;
	}
}

#------------------------#
#チャンプアクセサリー加算#
#------------------------#
sub wacs_add {
	$temp_winner[6] = $winner[6];
	$temp_winner[7] = $winner[7];
	$temp_winner[8] = $winner[8];
	$temp_winner[9] = $winner[9];
	$temp_winner[10] = $winner[10];
	$temp_winner[11] = $winner[11];
	$temp_winner[12] = $winner[12];
	$temp_winner[13] = $winner[13];
	$temp_winner[22] = $winner[22];
	$temp_winner[23] = $winner[23];
	$temp_winner[25] = $winner[25];
	$temp_winner[26] = $winner[26];
	$winner[7] += $winner[28];
	$winner[8] += $winner[29];
	$winner[9] += $winner[30];
	$winner[10] += $winner[31];
	$winner[11] += $winner[32];
	$winner[12] += $winner[33];
	if ($winner[51]) {
		require "./wacstech/$winner[51].pl";
	} else {
		require "./wacstech/0.pl";
	}
}

#------------------#
# チャンプ能力復元 #
#------------------#
sub wacs_sub {
	$winner[7] = $temp_winner[7];
	$winner[8] = $temp_winner[8];
	$winner[9] = $temp_winner[9];
	$winner[10] = $temp_winner[10];
	$winner[11] = $temp_winner[11];
	$winner[12] = $temp_winner[12];
	$winner[22] = $temp_winner[22];
	$winner[23] = $temp_winner[23];
	$winner[25] = $temp_winner[25];
	$winner[26] = $temp_winner[26];
}

#------------------#
#戦闘回避          #
#------------------#
sub battle_kaihi{

	#挑戦者命中率＆回避率


	#相手命中率＆回避率


	$sake1 = 90 - int($smem1hit_ritu - $sake1);
	$ssake1 = 90 - int($mem1hit_ritu - $ssake1);

	if ($sdmg1 < 0) {$sdmg1 = $sdmg1;}
	if ($sdmg1 < $item[4] * (4 + int($chara[10]/10+1))) {$sdmg1 = 1;}
	else {$sdmg1 = $sdmg1 - $item[4] * (4 + int($chara[10]/10+1));}

	if ($dmg1 < 0) {$dmg1 = $dmg1;}
	if ($dmg1 < $winner[25] * (4 + int($winner[10]/10+1))) {$dmg1 = 1;}
	else {$dmg1 = $dmg1 - $winner[25] * (4 + int($winner[10]/10+1));}

	if (int($sake1) > int(rand(100))) {
		$sdmg1 = 0;
		$kawasi1 = "<FONT SIZE=4 class=\"red\">$chara[4]は身をかわした！</FONT><br>";
	}

	if(int($ssake1) > int(rand(100))) {
		$dmg1 = 0;
		$kawasi2 = "<FONT SIZE=4 class=\"red\">$winner[3]は身をかわした！</FONT><br>";
	}

}

#------------------------#
#チャンプアクセサリー効果#
#------------------------#
sub wacs_waza {
	&wacskouka;
}

#------------------#
#　チャンプの必殺技#
#------------------#
sub winwaza {

	# クリティカル率・戦術率算出
	$swaza_ritu1 = int(($winner[11] / 10)) + 10;
	if ($swaza_ritu1 > 80) { $swaza_ritu1 = 80; }
	$swaza_ritu1 +=  int(rand($winner[12] / 4));
	$sab = 1;$ab=0;
	$k=0;
	if ($k!=1 and $winner[56]) {
		$hissatu="hissatu$winner[56]";
		require "./tech/$winner[56].pl";
		&$hissatu;
	}
	if ($k!=1 and $winner[57]) {
		$hissatu="hissatu$winner[57]";
		require "./tech/$winner[57].pl";
		&$hissatu;
	}
	if ($k!=1 and $winner[58]) {
		$hissatu="hissatu$winner[58]";
		require "./tech/$winner[58].pl";
		&$hissatu;
	}
	if ($k!=1 and $winner[59]) {
		$hissatu="hissatu$winner[59]";
		require "./tech/$winner[59].pl";
		&$hissatu;
	} else {require "./tech/0.pl";}
}

#------------------#
#　戦闘状況        #
#------------------#
sub battle_sts {

	$battle_date[$j] = <<"EOM";
	<TABLE BORDER=0 align="center">
	<TR><TD COLSPAN="3" ALIGN="center">$iターン</TD></TR>
EOM
	if($i == 1){
		$battle_date[$j] .= <<"EOM";
		<TD><IMG SRC="$img_path/$chara_img[$chara[6]]"></TD>
		<TD></TD>
		<TD><IMG SRC="$img_path/$chara_img[$winner[5]]"></TD>
EOM
	}
	$battle_date[$j] .= <<"EOM";
	
	<TR><TD><TABLE><TR>
	<TD CLASS="b1" id="td2">
	なまえ
	</TD>
	<TD CLASS="b1" id="td2">
	HP
	</TD>
	<TD CLASS="b1" id="td2">
	職業
	</TD>
	<TD CLASS="b1" id="td2">
	LV
	</TD>
	</TR>
		<TR>
		<TD class="b2">
		$chara[4]
		</TD>
		<TD class="b2">
		$khp_flg\/$chara[16]
		</TD>
		<TD class="b2">
		$chara_syoku[$chara[14]]
		</TD>
		<TD class="b2">
		$chara[18]
		</TD></TR>
	</TABLE></TD><TD><FONT class=red size=5>VS</FONT></TD>
	<TD><TABLE><TR>
	<TD CLASS="b1" id="td2">
	なまえ
	</TD>
	<TD CLASS="b1" id="td2">
	HP
	</TD>
	<TD CLASS="b1" id="td2">
	職業
	</TD>
	<TD CLASS="b1" id="td2">
	LV
	</TD></TR><TR>
	<TD class="b2">
	$winner[3]
	</TD>
	<TD class="b2">
	$whp_flg\/$winner[16]
	</TD>
	<TD class="b2">
	$chara_syoku[$winner[14]]
	</TD>
	<TD class="b2">
	$winner[17]
	</TD></TR></TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]の攻撃！！</td></tr>
		<tr><td class="b2"><br>$com1 $clit1 $kawasi2 $winner[3] に <font class=yellow>$dmg1</font> のダメージを与えた。<font class=yellow>$kaihuku1</FONT><br>　</td></tr>
		<tr><td class="b1" id="td2">$winner[3]の攻撃！！</td></tr>
		<tr><td class="b2"><br>$scom1 $clit2 $kawasi1 $chara[4] に <font class=red>$sdmg1</font> のダメージを与えた。<font class=yellow>$skaihuku1</FONT><br>　</td></tr>
		</table>
		</table>
EOM
}

#------------------#
#戦闘クリィティカル#
#------------------#
sub battle_clt {
	# クリティカル(運÷10＋10)
	$kclt_ritu = int(rand($chara[11] / 10)) + 10;
	$wclt_ritu = int(($winner[11] / 10)) + 10;

	if($kclt_ritu > int(rand(100))) {
		$clit1 = "<font color=$red size=5>クリティカル！！「<b>$chara[23]</b>」</FONT><br>";
		$dmg1 = $dmg1 * 2;
		$dmg1 += $winner[22];
	}

	if($wclt_ritu > int(rand(100))) {
		$clit2 = "<font color=$red size=5>クリティカル！！「<b>$winner[20]</b>」</FONT><br>";
		$sdmg1 = $sdmg1 * 2;
		$sdmg1 += $item[4];
	}
}

#------------------#
#戦闘結果判定      #
#------------------#
sub sentoukeka{
	if ($win == 1) {
		$chara[21] += 1;
		$chara[22] += 1;
		$exp = int($winner[17] * $kiso_exp);
		$winner[50] = int($winner[44] * $chara[17] * $syoukin);
		$comment = "<b><font size=5>$chara[4]は、戦闘に勝利した！！</font></b><br>";
	} elsif($win == 2) {
		$win = 1;
		$chara[21] += 1;
		$exp = int($winner[17] * $kiso_exp);
		$chara[15] = 1;
		$winner[15] = 1;
		$winner[50] = int($winner[44] * $chara[17] * $syoukin);
		$comment = "<b><font size=5>$chara[4]は、$winner[3]と相打ちした！！</font></b><br>";
	} elsif($win == 3) {
		$chara[21] += 1;
		$exp = int($winner[17] * $kiso_exp);
		$gold = 0;
		$winner[50] += int($winner[44] * $chara[17] * $syoukin);
		$comment = "<b><font size=5>$chara[4]は、$winner[3]と勝負が決まらなかった。。。</font></b><br>";
	} else {
		$chara[21] += 1;
		$exp = $winner[17];
		$gold = 0;
		$chara[19] = int(($chara[19] / 2));
		$winner[50] += int($winner[44] * $chara[17] * $syoukin);
		$comment = "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
		$chara[28] = $boss;
	}
		$chara[17] = $chara[17] + $exp;
		$chara[27] = time();
}
1;