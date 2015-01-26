#------------------#
#　挑戦者の攻撃  　#
#------------------#
sub tyousensya {

	if($khp_flg > 0){
		$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
		if ($chara[55]==33 or $chara[56]==33 or $chara[57]==33 or $chara[58]==33){$mahoken=1;}else{$mahoken=0;}
		if ($chara[59] and int(rand(4 - $mahoken * 3))==0) {
			$ccc=1;
			$sp=1;
			$dmg1 = $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
			if($mahoken == 1){$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);}
			require "./spell/$chara[59].pl";
			$spell="spell$chara[59]";
			&$spell;
		}
		if(!$ccc){
			if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}
			if($item[20]==10){$g="red";}else{$g="";}
			$com1 = "$chara[4]は、<font color=\"$g\">$item[0] $bukilv</font>で攻撃！！";
			if( ($chara[7] + $item[1]) > ($chara[8] + $item[1]) ){
				$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);
			}else{
				$dmg1 += $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
			}
		}
		if ($chara[55]==21 or $chara[56]==21 or $chara[57]==21 or $chara[58]==21){
			$dmg1 += ($chara[15]-$khp_flg);
		}
	}
	for($kou=1;$kou<4;$kou++){
		$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
		$ddd=$kou+1;
		if(${'mem'.$kou.'hp_flg'} > 0){
			$mahoken=0;
			if (${'mem'.$kou}[55]==33 or ${'mem'.$kou}[56]==33 or ${'mem'.$kou}[57]==33 or ${'mem'.$kou}[58]==33){$mahoken=1;}else{$mahoken=0;}
			if (${'mem'.$kou}[59] and int(rand(4 - $mahoken * 3))==0) {
				$ccc=1;
				$sp=$kou+1;
				${'dmg'.$ddd} = ${'mem'.$kou}[8] * 4 + ${'mem'.$kou.'item'}[4] * 4 * int(${'mem'.$kou}[8]/10+1);
				if($mahoken == 1){${'dmg'.$ddd} += ${'mem'.$kou}[7] * 4 + ${'mem'.$kou.'item'}[4] * 4 * int(${'mem'.$kou}[7]/10+1);}
				require "./spell/${'mem'.$kou}[59].pl";
				$spell2="spell${'mem'.$kou}[59]";
				&$spell2;
			}
			if(!$ccc){
				if(${'mem'.$kou.'item'}[20]){$bukilv="+ ${'mem'.$kou.'item'}[20]";}else{$bukilv="";}
				if(${'mem'.$kou.'item'}[20]==10){$g="red";}else{$g="";}
				${'com'.$ddd} = "${'mem'.$kou}[4]は、<font color=\"$g\">${'mem'.$kou.'item'}[0] $bukilv</font>で攻撃！！";
				if( (${'mem'.$kou}[7] + ${'mem'.$kou.'item'}[1]) > (${'mem'.$kou}[8] + ${'mem'.$kou.'item'}[1]) ){
					${'dmg'.$ddd} += ${'mem'.$kou}[7] * 4 + ${'mem'.$kou.'item'}[1] * 4 * int(${'mem'.$kou}[7]/10+1);
				}else{
					${'dmg'.$ddd} += ${'mem'.$kou}[8] * 4 + ${'mem'.$kou.'item'}[1] * 4 * int(${'mem'.$kou}[8]/10+1);
				}
			}
			if (${'mem'.$kou}[55]==21 or ${'mem'.$kou}[56]==21 or ${'mem'.$kou}[57]==21 or ${'mem'.$kou}[58]==21){
				${'dmg'.$ddd} += (${'mem'.$kou}[15]-${'mem'.$kou.'hp_flg'});
			}
		}
	}
	if($chara[39]){
		# ペットダメージ計算
		$com4 = "$chara[39]の攻撃！";
	
		$dmg4 += $chara[44];
	}

}

#------------------#
#　挑戦者の必殺技　#
#------------------#
sub tyosenwaza {

	$waza_ritu1 = int(rand($chara[11] / 10)) + 10;
	if($waza_ritu1 > 80){$waza_ritu1 = 80;}
	$waza_ritu2 = int(rand($mem1[11] / 10)) + 10;
	if($waza_ritu2 > 80){$waza_ritu2 = 80;}
	$waza_ritu3 = int(rand($mem2[11] / 10)) + 10;
	if($waza_ritu3 > 80){$waza_ritu3 = 80;}
	$waza_ritu4 = 10;

	if ($waza_ritu1 > int(rand(100))) {
		$com1 .= "<font color=\"$red\" size=5>クリティカル！！「$chara[23]」</font><br>";
		$dmg1 = $dmg1 * 2;
	}
	if ($waza_ritu2 > int(rand(100))) {
		$com2 .= "<font color=\"$red\" size=5>クリティカル！！「$mem1[23]」</font><br>";
		$dmg2 = $dmg2 * 2;
	}
	if ($waza_ritu3 > int(rand(100))) {
		$com3 .= "<font color=\"$red\" size=5>クリティカル！！「$mem2[23]」</font><br>";
		$dmg3 = $dmg3 * 2;
	}
	if ($waza_ritu4 > int(rand(100))) {
		$com4 .= "<font color=\"$red\" size=5>クリティカル！！</font><br>";
		$dmg4 = $dmg4 * 2;
	}

	$k = 0;$ab = 1;$sab=0;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $khp_flg > 0 and $chara[$his]) {
			$hissatu1="hissatu$chara[$his]";
			require "./tech/$chara[$his].pl";
			&$hissatu1;
		}
	}
	$k = 0;$ab = 2;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem1hp_flg > 0 and $mem1[$his]) {
			$hissatu2="hissatu$mem1[$his]";
			require "./tech/$mem1[$his].pl";
			&$hissatu2;
		}
	}
	$k = 0;$ab = 3;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem2hp_flg > 0 and $mem2[$his]) {
			$hissatu3="hissatu$mem2[$his]";
			require "./tech/$mem2[$his].pl";
			&$hissatu3;
		}
	}
	$k = 0;$ab = 4;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $mem3hp_flg > 0 and $mem3[$his]) {
			$hissatu4="hissatu$mem3[$his]";
			require "./tech/$mem3[$his].pl";
			&$hissatu4;
		}
	}
	if ($k!=1) {require "./tech/0.pl";}
	if ($php_flg>0){&phissatu;}

}
#------------------#
#　レベルアップ  　#
#------------------#
sub levelup {

	if($in{'mode'} eq "guild_battle"){
		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[66] and $array[2] > $array[3] * 3000000){
				$comment .= "<font class=red size=7>ギルドレベルが上がった！</font><br>";
				$array[3] += 1;
				$array[2] = 0;
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
			$i++;
		}
	}

	#卵なら20レベにすることで即進化へ
	if ($chara[38]>3000 and $chara[38]<3100 and $chara[40] > $chara[41]){$chara[46]=20;}
	elsif ($chara[38]>3000 and $chara[40] > $chara[41]) {
		#ペットレベルアップ
		while($chara[40] > $chara[41]){
			$chara[40] = $chara[40] - $chara[41];
			$plvup += 1;
			if(!$chara[49]){$chara[49]=1;}
			if(!$chara[46]){$chara[46]=1;}
			$chara[41] = $chara[41] + int($chara[41] / $chara[46]) + 100 * int ($chara[49] / 4);
			$chara[46] += 1;
			$chara[43] = $chara[43] + int(rand($chara[46]) * 15);
			$chara[44] = $chara[44] + int(rand($chara[46]) * 5);
		}
		if ($plvup != 0){
	$comment .= "<font class=red size=7>$chara[39]のレベルが$plvup上がった！</font><br>";
			if ($chara[46] > 19) { $chara[46]=20; }
			$chara[42] = $chara[43];
		}
	}

	#ペット進化
	if ($chara[38]>3000 and $chara[46]>=20){
	#進化先調べ
		open(IN,"$pet_sinka");
		@sinka_array = <IN>;
		close(IN);
		foreach(@sinka_array){
		($i_no,$i_noa,$i_nob,$i_noc,$i_nod) = split(/<>/);
		if($chara[38] eq "$i_no") { $shit=1;last;}
		}
		if($shit) {
	#進化先の個数調べ
		$sinkasaki=0;
		if ($i_noa != 0){$sinkasaki+=1;}
		if ($i_nob != 0){$sinkasaki+=1;}
		if ($i_noc != 0){$sinkasaki+=1;}
		if ($i_nod != 0){$sinkasaki+=1;}
			if ($sinkasaki > 0){
	#進化先の決定
		$sinkano=int(rand($sinkasaki));
		if($sinkano==0){$item_no=$i_noa;}
		if($sinkano==1){$item_no=$i_nob;}
		if($sinkano==2){$item_no=$i_noc;}
		if($sinkano==3){$item_no=$i_nod;}
	open(IN,"$pet_file");
	@item_array = <IN>;
	close(IN);
	foreach(@item_array){
	($i_no,$i_name,$i_gold,$i_exp,$i_hp,$i_damage,$i_image,$ps) = split(/<>/);
	if($item_no eq "$i_no") { $ihit=1;last; }
	}
	if(!$ihit) { &error("そんなアイテムは存在しません"); }
		if($chara[38] < $i_no){
		$comment .= "<font class=red size=7>ペットが$i_nameに進化した！！</font><br>";
		$chara[41] = $i_exp;
		}
		if($chara[38] > $i_no){
		$comment .= "<font class=red size=7>ペットが$i_nameに退化した…</font><br>";
		$chara[41] = int($i_exp/2);
		}
		$chara[38] = $i_no;
		$chara[39] = $i_name;
		$chara[40] = 0;
		$chara[43] = int(rand($chara[42])/10)+$i_hp;
		$chara[42] = $chara[43];
		$chara[44] = int(rand($chara[44])/10)+$i_damage;
		$chara[45] = $i_image;
		$chara[46] = 1;
		$chara[47] = $ps;
		$chara[49] += 1;
			}
		}
	}
	if ($chara[18] < $charamaxlv or $chara[70]==1) {
		if($chara[70]!=1){
			while ($chara[17] >= $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50)) {
				$chara[17] -= $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50);
				$lvup += 1;
				if(!$chara[35]){$chara[35]=0;}
				$chara[35] += 4;
				$chara[18] += 1;
				$hpup = int( rand($chara[18] * 5));
				$chara[16] = $chara[16] + $hpup;
			}
		}else{
			while ($chara[17] >= $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10) {
				$chara[17] -= $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;
				$lvup += 1;
				if(!$chara[35]){$chara[35]=0;}
				$chara[35] += 4;
				$chara[18] += 1;
				$hpup = int( rand($chara[18] * 3));
				$chara[16] = $chara[16] + $hpup;
			}
		}

		if ($lvup != 0){
			$comment .= "<font class=red size=7>レベルが$lvup上がった！</font><br>";
			$klvbf = $chara[33];
			$chara[33] += $lvup;
			#ジョブマスターの処理
			if ($chara[33] > 99 && $klvbf <=99) {
				$comment .= "<font class=red size=5>$chara_syoku[$chara[14]]をマスターした！！</font><br>";
				$lock_file = "$lockfolder/syoku$in{'id'}.lock";
				&lock($lock_file,'SK');
				&syoku_load;

				$syoku_master[$chara[14]] = 100;

				&syoku_regist;
				&unlock($lock_file,'SK');
			}
			if ($chara[33] > 100) { $chara[33]=100; }

			$chara[15] = $chara[16];
		}
	}
}

#----------------#
# 職業書込み処理 #
#----------------#
sub syoku_regist {

	$new_syoku = '';

	for ($s=0;$s<=$chara[14];$s++) {
		if (!$syoku_master[$s]){
			$syoku_master[$s] = 0;
		}
	}

	$new_syoku = join('<>',@syoku_master);

	$new_syoku .= "<>";

	open(OUT,">./syoku/$in{'id'}.cgi");
	print OUT $new_syoku;
	close(OUT);

}

#------------------#
#挑アクセサリー効果#
#------------------#
sub acs_waza {

	&acskouka;

}

#----------------------#
#挑戦者アクセサリー加算#
#----------------------#
sub acs_add {
	$temp_chara[7] = $chara[7];
	$temp_chara[8] = $chara[8];
	$temp_chara[9] = $chara[9];
	$temp_chara[10] = $chara[10];
	$temp_chara[11] = $chara[11];
	$temp_chara[12] = $chara[12];

	$chara[7] += $item[8];
	$chara[8] += $item[9];
	$chara[9] += $item[10];
	$chara[10] += $item[11];
	$chara[11] += $item[12];
	$chara[12] += $item[13];

	@temp_item = @item;

	if ($item[7]) {
		require "./acstech/$item[7].pl";
	} else {
		require "./acstech/0.pl";
	}

	if($chara[47]){require "./ptech/$chara[47].pl";}
	else{require "./ptech/0.pl";}
}

#--------------------#
#　挑戦者能力値復元　#
#--------------------#
sub acs_sub {
	$chara[7] = $temp_chara[7];
	$chara[8] = $temp_chara[8];
	$chara[9] = $temp_chara[9];
	$chara[10] = $temp_chara[10];
	$chara[11] = $temp_chara[11];
	$chara[12] = $temp_chara[12];
	@item = @temp_item;
}

#----------------------#
#　対戦相手データ読替　#
#----------------------#
# キャラデータを@winner_dataに代入してから呼び出すと@winnerに変換します
sub winner_data {

	open(IN,"./item/$winner_data[0].cgi");
	$witem_log = <IN>;
	close(IN);

	@witem = split(/<>/,$witem_log);

	@winner = ($winner_data[0],$winner_data[2],$winner_data[3],$winner_data[4],$winner_data[5],$winner_data[6],$winner_data[7],$winner_data[8],$winner_data[9],$winner_data[10],$winner_data[11],$winner_data[12],$winner_data[13],$winner_data[20],$winner_data[14],$winner_data[15],$winner_data[16],$winner_data[18],$winner_data[21],$winner_data[22],$winner_data[23],$witem[0],$witem[1],$witem[2],$witem[3],$witem[4],$witem[5],$witem[6],$witem[8],$witem[9],$witem[10],$witem[11],$witem[12],$witem[13],$witem[15],$witem[17],$witem[18],$winner_data[30],$winner_data[26],$winner_data[33]);

	$winner[51] = $witem[7];
	$winner[52] = $witem[16];
	$winner[53] = $witem[14];
}
#------------------------#
#　勝利時武器能力アップ  #
#------------------------#
sub item_u {

$itemmaxlv = 10;
$defmaxlv = 10;

	if($item[20] < $itemmaxlv and $chara[24] and $chara[24]>0 and $chara[24]<4000){
		$item[21] += int(rand($place+1));
	}
	if($item[22] < $defmaxlv and $chara[29] and $chara[29]>0 and $chara[29]<4000){
		$item[23] += int(rand($place+1));
	}

	if ($item[21] >= int(rand(($item[20]+1) * 100) + 20*int($item[20]))) {
		$comment .= "<font class=red size=6>$item[0]が使い慣れて強くなった！！</font><br>";
		if($item[20]==9){
			$item[1] = $item[1] + 6; 
			$item[2] = $item[2] + 2;
			$item[20] += 1;
			$item[21] = 0;
		}else{
			$item[1] = $item[1] + 1; 
			$item[2] =$item[2] + 2;
			$item[20] += 1;
			$item[21] = 0;
		}
	}

	if ($item[23] >= int(rand(($item[22]+1) * 100) + 20*int($item[22]))) {
		$comment .= "<font class=red size=6>$item[3]が使い慣れて強くなった！！</font><br>";
		if($item[22]==9){
			$item[4] = $item[4] + 6; 
			$item[5] =$item[5] + 2;
			$item[22] += 1;
			$item[23] = 0;
		}else{
		$item[4] = $item[4] + 1; 
		$item[5] =$item[5] + 2;
		$item[22] += 1;
		$item[23] = 0;
		}
	}
}
#----------------------------#
#　アイテムファイル書き込み　#
#----------------------------#
sub item_regist {

	$new_item = "";
	foreach(@item){
		$new_item .="$_<>";
	}
	open(OUT,">./item/$chara[0].cgi"); 
	print OUT $new_item; 
	close(OUT);

}
sub egg_lose {
	$chara[38] = 3000;
	$chara[39] = "壊れた卵";
	$chara[40] = 0;
	$chara[41] = 0;
	$chara[42] = 0;
	$chara[43] = 0;
	$chara[44] = 0;
	$chara[45] = 0;
	$chara[46] = 0;
	$chara[47] = 0;
}
sub egg_egg {
	$comment .= "<b><font size=4 color=red>エッグを拾った！！</font></b><br>";
	$php_flg = 300;
	$chara[38] = 3003;
	$chara[39] = "エッグ";
	$chara[40] = 0;
	$chara[41] = 300000;
	$chara[42] = 300;
	$chara[43] = 300;
	$chara[44] = 0;
	$chara[45] = 2;
	$chara[46] = 1;
	$chara[47] = 0;
}
1;
