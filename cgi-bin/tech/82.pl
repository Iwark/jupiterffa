sub hissatu82{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
		if($i >= 3 and $smem1hp_flg<1000000){
	${'com'.$ab} .="<font class=\"purple\" size=8><b>献上せよ！</b></font><br>";
	$k=1;
	$i_no=0;
	if(int(rand(2000))==1){
		$rjizo=int(rand(10));
		if($rjizo < 3){
			$i_no=int(rand(81)+1001);
			${'com'.$ab} .="<font class=\"red\" size=4>要らんものをよこしおって！</font><br>";
		}elsif($rjizo < 6){
			$i_no=int(rand(10)+1091);
			${'com'.$ab} .="<font class=\"red\" size=4>今さらこんな情報いらんわい！</font><br>";
		}elsif($rjizo < 8){
			$i_no=int(rand(17)+1101);
			if($i_no == 1114 or $i_no == 1116){$i_no=1113;}
			${'com'.$ab} .="<font class=\"red\" size=4>こんなもの地力で作れるわい！</font><br>";
		}elsif($rjizo < 9){
			$i_no=int(rand(11)+1121);
			if($i_no == 1122 or $i_no == 1123 or $i_no == 1124){$i_no=1125;}
			${'com'.$ab} .="<font class=\"red\" size=4>おかしなものをくれおって！</font><br>";
		}elsif($rjizo < 10){
			$i_no=1083;
			${'com'.$ab} .="<font class=\"red\" size=4>どうせなら昇龍烈剣をよこせ！</font><br>";
		}
	}elsif(int(rand(20000))==2){
		$rjizo=int(rand(4));
		if($rjizo < 2){
			$i_no=1133;
			${'com'.$ab} .="<font class=\"yellow\" size=5>これでペットを育てるとするか！</font><br>";
		}elsif($rjizo < 3){
			$i_no=1119;
			${'com'.$ab} .="<font class=\"yellow\" size=6>うむ。中々良いものじゃな！</font><br>";
		}elsif($rjizo < 4){
			$i_no=1170;
			${'com'.$ab} .="<font class=\"yellow\" size=6>うむ。中々良いものじゃな！</font><br>";
		}
	}elsif(int(rand(100000))==3){
		$rjizo=int(rand(8));
		if($rjizo < 3){
			$i_no=1345;
			${'com'.$ab} .="<font class=\"yellow\" size=7>素晴らしい！本物の龍剣か！</font><br>";
		}elsif($rjizo < 5){
			$i_no=1341;
			${'com'.$ab} .="<font class=\"yellow\" size=7>これは素晴らしいぞ！よいよい！</font><br>";
		}elsif($rjizo < 7){
			$i_no=1323;
			${'com'.$ab} .="<font class=\"yellow\" size=7>死神が持つとされる幻の斧か…！</font><br>";
		}elsif($rjizo < 6){
			$i_no=1347;
			${'com'.$ab} .="<font class=\"yellow\" size=8>これこそ我が持つべき品！</font><br>";
		}
	}else{
		${'com'.$ab} .="<font class=\"red\" size=4>何も献上しないというのか！こら！</font><br>";
	}
		if($i_no>1000){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("武具倉庫がいっぱいです！$back_form");
			}
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			${'com'.$ab} .="<font color=\"Lime\" size=6><b>$i_nameを手に入れた！！</b></font><br>";
			$i_name="";
		}
		$dmg1 = 0;
		}
				}

			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					if($i == 1){
				${'com'.$ab} .="<font class=\"purple\" size=8><b>献上せよ！</b></font><br>";
				$k=1;
				${'dmg'.$ab} = 0;
				${'com'.$ab} .="<font class=\"red\" size=5>お地蔵様ですよっと！！！</font><br>";
					}
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'sdmg'.$sab} = 0;
				${'scom'.$sab} .="<font class=\"red\" size=5>お地蔵様ですよっと！！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;