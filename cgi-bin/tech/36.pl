sub hissatu36{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					$i=int(rand(29)+1);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技時空を飛ぶ！！</font><br>";
					if($chara[70]>=1 and int(rand(2))==0){
						${'dmg'.$ab} = ${'dmg'.$ab} * int(rand(10));
						${'com'.$ab} .="<font class=\"red\" size=5>会心の一撃！！</font><br>";
					}
					if($chara[29] == 0 and $chara[24] == 1339){
						&item_lose;
						$chara[29]=2244;
						$item[3]="時空カブト";
						$item[4]=0;
						$item[5]=0;
						$item[22]=0;
						$item[23]=0;
						$si_koka="正義のマントはどこだぁ";
						$item[25]=$si_koka;
						&item_regist;
					}
					if($chara[29] == 2246 and $chara[33] == 100){
						&def_lose;
						$chara[14]=59;
						$chara[33]=1;
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が時空戦士に覚醒しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(水)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
						&item_regist;
					}
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					$i=int(rand(29)+1);
					${'com'.$ab} .="<font class=\"red\" size=5>必殺技時空を飛ぶ！！</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				$i=int(rand(29)+1);
				${'scom'.$sab} .="<font class=\"red\" size=5>必殺技時空を飛ぶ！！</font><br>";
			}
		}
	}
}
sub atowaza{}
1;