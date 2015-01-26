sub hissatu52{
	for($abi=1;$abi<5;$abi++){
		if($abi==$ab){
			if($ab==1){
				if($waza_ritu1 + int(rand($chara[12]/4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z’é‰¤†—ßI</font><br>";
	if($chara[66] and $mem1hp_flg < 1){
		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$hit=0;
		foreach(@member_data){
			s/\n//i;
			s/\r//i;
			($g_name,$gg_leader) = split(/<>/);
			@pre = split(/<>/,$_,8);
			@battle_mem = split(/<>/,$pre[7]);
			if($g_name eq $chara[66]){
				$battle_mem_num = @battle_mem;
				$ht=0;
				for($bgb=0;$bgb<$battle_mem_num;$bgb++){
					if($battle_mem[$bgb] eq $chara[0]){$ht=1;last;}
				}
				if(!$ht){$chara[66]="";}
				for($bab=0;$bab<10;$bab++){
					$battle_rand = int(rand($battle_mem_num));
					if($battle_mem[$battle_rand] ne $chara[0]){
						if($battle_mem[0] ne $chara[0]){
							$gmem1=$battle_mem[$battle_rand];$bab=0;$battle_i++;
							$lock_file = "$lockfolder/$gmem1.lock";
							&lock($lock_file,'DR');
							open(IN,"./charalog/$gmem1.cgi");
							$member1_data = <IN>;
							close(IN);
							$lock_file = "$lockfolder/$gmem1.lock";
							&unlock($lock_file,'DR');
							@mem1 = split(/<>/,$member1_data);
							open(IN,"./item/$gmem1.cgi");
							$mem1item_log = <IN>;
							close(IN);
							@mem1item = split(/<>/,$mem1item_log);
					${'com'.$ab} .="<font class=\"red\" size=5>$mem1[4]‚ª‚â‚Á‚Ä‚«‚½‚ÁI</font><br>";
					$mem1hp_flg=$mem1[15];
						}
					}
				}
			}
		}
	}
					${'com'.$ab} .="<font class=\"red\" size=5>’N‚à‚â‚Á‚Ä‚±‚È‚©‚Á‚½c</font><br>";
				}
			}else{
				$ri=$ab-1;
				if(${'waza_ritu'.$ab} + int(rand(${'mem'.$ri}[12] / 4)) > int(rand(300))){
					$k=1;
					${'com'.$ab} .="<font class=\"red\" size=5>•KE‹Z’é‰¤†—ßI</font><br>";
				}
			}
		}
	}
	for($abi=1;$abi<5;$abi++){
		if($abi==$sab){
			if(${'swaza_ritu'.$sab} + int(rand(${'smem'.$sab}[12] / 4)) > int(rand(300))){
				$k=1;
				${'scom'.$sab} .="<font class=\"red\" size=5>•KE‹Z’é‰¤†—ßI</font><br>";
			}
		}
	}
}
sub atowaza{}
1;