#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

#------------------------------------------------------#
#　本スクリプトの著作権は下記の3人にあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
#　FF ADVENTURE 改i v2.1
#　programed by jun-k
#　http://www5b.biglobe.ne.jp/~jun-kei/
#　jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#　FF ADVENTURE v0.21
#　programed by CUMRO
#　http://cgi.members.interq.or.jp/sun/cumro/mm/
#　cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(改) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(いく改)
#　remodeling by いく
#　http://www.eriicu.com
#　icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した	#
#    いかなる損害に対して作者は一切の責任を負いません。		#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。	#
#    直接メールによる質問は一切お受けいたしておりません。	#
# 3. 設置したら皆さんに楽しんでもらう為にも、Webリングへぜひ参加#
#    してくださいm(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

if ($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

# このファイル用設定
$temp_back = "$mode\_back";
$temp_midi = "$mode\_midi";
$backgif = $$temp_back;
$midi = $$temp_midi;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");
	}
}

&$mode;

exit;

#----------------------#
#  モンスターとの戦闘  #
#----------------------#
sub koujyou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&item_load;

	&acs_add;
	$place=50;
	#メンバー調整
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){$hit=1;last;}
		$i++;
	}
	if($hit){
		$g=0;
		foreach(@array){
			if(!$_ and $g>6){splice(@array,$g,1);}
			$g++;
		}
		$memmem=@array;
		$array[4]=$memmem - 8;
		$new_array = '';
		$new_array = join('<>',@array);
		$member_data[$i]=$new_array;
		open(OUT,">allguild.cgi");
		print OUT @member_data;
		close(OUT);
	}


	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$koutime=time();$koubut="";$hit=0;

	open(IN,"siro.cgi");
	@siro_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@siro_data){
		($siro_name,$siro_seigen,$gg_name,$sihaisya,$sihaisyaid,$kankaku) = split(/<>/);
		if($in{'siro_name'} eq $siro_name){$hit=1;last;}
	}
	if($hit!=1){&error("城が見つかりません");}
	if($siro_seigen < $chara[18]){&error("レベルが高すぎます。");}
	$kankaku = 5 - int(($koutime - $kankaku)/60);
	if($kankaku>0){&error("この城は戦われたばかりです。");}

	#自分のメンバー決定
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($g_name,$gg_leader,$gg_exp,$gg_lv) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $chara[66]){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bgb=0;$bgb<$battle_mem_num;$bgb++){
				if($battle_mem[$bgb] eq $chara[0]){$ht=1;last;}
			}
			if(!$ht){$chara[66]="";}
			$battle_i=0;
			for($bab=0;$bab<10;$bab++){
				$battle_rand = int(rand($battle_mem_num));
				if($battle_mem[$battle_rand] ne $chara[0]){
					if($battle_i==0){
						$gmem1=$battle_mem[$battle_rand];
						$lock_file = "$lockfolder/$gmem1.lock";
						&lock($lock_file,'DR');
						open(IN,"./charalog/$gmem1.cgi");
						$member1_data = <IN>;
						close(IN);
						$lock_file = "$lockfolder/$gmem1.lock";
						&unlock($lock_file,'DR');
						@mem1 = split(/<>/,$member1_data);
						if($mem1[18]<=$siro_seigen){
							$bab=0;
							$battle_i++;
						}else{
							$member1_data="";
							@mem1=();
							$gmem1="";
						}
					}
					if($battle_i==1 and $gmem1 ne $battle_mem[$battle_rand]){
						$gmem2=$battle_mem[$battle_rand];
						$lock_file = "$lockfolder/$gmem2.lock";
						&lock($lock_file,'ER');
						open(IN,"charalog/$gmem2.cgi");
						$member2_data = <IN>;
						close(IN);
						$lock_file = "$lockfolder/$gmem2.lock";
						&unlock($lock_file,'ER');
						@mem2 = split(/<>/,$member2_data);
						if($mem2[18]<=$siro_seigen){
							$bab=0;
							$battle_i++;
						}else{
							$member2_data="";
							@mem2=();
							$gmem2="";
						}
					}
					if($battle_i==2 and $gmem1 ne $battle_mem[$battle_rand] and $gmem2 ne $battle_mem[$battle_rand]){
						$gmem3=$battle_mem[$battle_rand];
						$lock_file = "$lockfolder/$gmem3.lock";
						&lock($lock_file,'ER');
						open(IN,"charalog/$gmem3.cgi");
						$member3_data = <IN>;
						close(IN);
						$lock_file = "$lockfolder/$gmem3.lock";
						&unlock($lock_file,'ER');
						@mem3 = split(/<>/,$member3_data);
						if($mem3[18]<=$siro_seigen){
							$bab=0;
							$battle_i++;
						}else{
							$member3_data="";
							@mem3=();
							$gmem3="";
						}
					}
				}
			}
			$hit=1;last;
		}
	}
	if(!$hit or !$chara[66]){&error("ギルドに所属していません。");}

	if($battle_i){
		$member=1;
		if($gmem1){
			open(IN,"./item/$gmem1.cgi");
			$mem1item_log = <IN>;
			close(IN);
			@mem1item = split(/<>/,$mem1item_log);
			$member+=1;
		}
		if($gmem2){
			open(IN,"./item/$gmem2.cgi");
			$mem2item_log = <IN>;
			close(IN);
			@mem2item = split(/<>/,$mem2item_log);
			$member+=1;
		}
		if($gmem3){
			open(IN,"./item/$gmem3.cgi");
			$mem3item_log = <IN>;
			close(IN);
			@mem3item = split(/<>/,$mem3item_log);
			$member+=1;
		}
	}

	#相手のメンバー決定
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
		if($g_name eq $gg_name){
			$battle_mem_num = @battle_mem;
			$ht=0;
			$battle_i=0;
			for($bab=0;$bab<10;$bab++){
				$battle_rand = int(rand($battle_mem_num));
				if($battle_i==0){
					$sgmem1=$sihaisyaid;
					$lock_file = "$lockfolder/$sgmem1.lock";
					&lock($lock_file,'DR');
					open(IN,"./charalog/$sgmem1.cgi");
					$smember1_data = <IN>;
					close(IN);
					$lock_file = "$lockfolder/$sgmem1.lock";
					&unlock($lock_file,'DR');
					@smem1 = split(/<>/,$smember1_data);
					if($smem1[18]<=$siro_seigen){
						$bab=0;
						$battle_i++;
					}else{
						$smember1_data="";
						@smem1=();
						$sgmem1="";
					}
				}
				if($battle_i==1 and $sgmem1 ne $battle_mem[$battle_rand]){
					$sgmem2=$battle_mem[$battle_rand];
					$lock_file = "$lockfolder/$sgmem2.lock";
					&lock($lock_file,'ER');
					open(IN,"charalog/$sgmem2.cgi");
					$smember2_data = <IN>;
					close(IN);
					$lock_file = "$lockfolder/$sgmem2.lock";
					&unlock($lock_file,'ER');
					@smem2 = split(/<>/,$smember2_data);
					if($smem2[18]<=$siro_seigen){
						$bab=0;
						$battle_i++;
					}else{
						$smember2_data="";
						@smem2=();
						$sgmem2="";
					}
				}
				if($battle_i==2 and $sgmem1 ne $battle_mem[$battle_rand] and $sgmem2 ne $battle_mem[$battle_rand]){
					$sgmem3=$battle_mem[$battle_rand];
					$lock_file = "$lockfolder/$sgmem3.lock";
					&lock($lock_file,'ER');
					open(IN,"charalog/$sgmem3.cgi");
					$smember3_data = <IN>;
					close(IN);
					$lock_file = "$lockfolder/$sgmem3.lock";
					&unlock($lock_file,'ER');
					@smem3 = split(/<>/,$smember3_data);
					if($smem3[18]<=$siro_seigen){
						$bab=0;
						$battle_i++;
					}else{
						$smember3_data="";
						@smem3=();
						$sgmem3="";
					}
				}
				if($battle_i==3 and $sgmem1 ne $battle_mem[$battle_rand] and $sgmem2 ne $battle_mem[$battle_rand] and $sgmem3 ne $battle_mem[$battle_rand]){
					$sgmem4=$battle_mem[$battle_rand];
					$lock_file = "$lockfolder/$sgmem4.lock";
					&lock($lock_file,'ER');
					open(IN,"charalog/$sgmem4.cgi");
					$smember4_data = <IN>;
					close(IN);
					$lock_file = "$lockfolder/$sgmem4.lock";
					&unlock($lock_file,'ER');
					@smem4 = split(/<>/,$smember4_data);
					if($smem4[18]<=$siro_seigen){
						$bab=0;
						$battle_i++;
					}else{
						$smember4_data="";
						@smem4=();
						$sgmem4="";
					}
				}
			}
		}
	}

	if($battle_i){
		$member2=0;
		if($sgmem1){
			open(IN,"./item/$sgmem1.cgi");
			$smem1item_log = <IN>;
			close(IN);
			@smem1item = split(/<>/,$smem1item_log);
			$member2+=1;
		}
		if($sgmem2){
			open(IN,"./item/$sgmem2.cgi");
			$smem2item_log = <IN>;
			close(IN);
			@smem2item = split(/<>/,$smem2item_log);
			$member2+=1;
		}
		if($sgmem3){
			open(IN,"./item/$sgmem3.cgi");
			$smem3item_log = <IN>;
			close(IN);
			@smem3item = split(/<>/,$smem3item_log);
			$member2+=1;
		}
		if($sgmem4){
			open(IN,"./item/$sgmem4.cgi");
			$smem4item_log = <IN>;
			close(IN);
			@smem4item = split(/<>/,$smem4item_log);
			$member2+=1;
		}
	}

	$khp_flg = $chara[15];
	if($member>1){$mem1hp_flg = $mem1[15];}
	if($member>2){$mem2hp_flg = $mem2[15];}
	if($member>3){$mem3hp_flg = $mem3[15];}

	if($member2>0){$smem1hp_flg = $smem1[15];}
	if($member2>1){$smem2hp_flg = $smem2[15];}
	if($member2>2){$smem3hp_flg = $smem3[15];}
	if($member2>3){$smem4hp_flg = $smem4[15];}

	$i=1;
	$j=0;

	@battle_date=();

	$turn=$turn3;

	while($i<=$turn) {
		
		&shokika;

		&tyousensya;

		&tyosenwaza;

		&acs_waza;

		&mons_kaihi;

		$dmg1=int($dmg1/50);$dmg2=int($dmg2/50);$dmg3=int($dmg3/50);$dmg4=int($dmg4/50);
		$sdmg1=int($sdmg1/50);$sdmg2=int($sdmg2/50);$sdmg3=int($sdmg3/50);$sdmg4=int($sdmg4/50);

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;
	
	&acs_sub;

	&hp_after;

	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$chara[67]=$mday + $hour;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B><br>バトル！</B></FONT>
EOM
	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

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
	for($kou=1;$kou<5;$kou++){
		$ccc=0;$sp=0;$ssp=0;$mahoken=0;$k=0;
		if(${'smem'.$kou.'hp_flg'} > 0){
			$mahoken=0;
			if (${'smem'.$kou}[55]==33 or ${'smem'.$kou}[56]==33 or ${'smem'.$kou}[57]==33 or ${'smem'.$kou}[58]==33){$mahoken=1;}else{$mahoken=0;}
			if (${'smem'.$kou}[59] and int(rand(4 - $mahoken * 3))==0) {
				$ccc=1;
				$ssp=$kou;
				${'sdmg'.$kou} = ${'smem'.$kou}[8] * 4 + ${'smem'.$kou.'item'}[4] * 4 * int(${'smem'.$kou}[8]/10+1);
				if($mahoken == 1){${'sdmg'.$kou} += ${'smem'.$kou}[7] * 4 + ${'smem'.$kou.'item'}[4] * 4 * int(${'smem'.$kou}[7]/10+1);}
				require "./spell/${'smem'.$kou}[59].pl";
				$sspell="spell${'smem'.$kou}[59]";
				&$sspell;
			}
			if(!$ccc){
				if(${'smem'.$kou.'item'}[20]){$bukilv="+ ${'smem'.$kou.'item'}[20]";}else{$bukilv="";}
				if(${'smem'.$kou.'item'}[20]==10){$g="red";}else{$g="";}
				${'scom'.$kou} = "${'smem'.$kou}[4]は、<font color=\"$g\">${'smem'.$kou.'item'}[0] $bukilv</font>で攻撃！！";
				if( (${'smem'.$kou}[7] + ${'smem'.$kou.'item'}[1]) > (${'smem'.$kou}[8] + ${'smem'.$kou.'item'}[1]) ){
					${'sdmg'.$kou} += ${'smem'.$kou}[7] * 4 + ${'smem'.$kou.'item'}[1] * 4 * int(${'smem'.$kou}[7]/10+1);
				}else{
					${'sdmg'.$kou} += ${'smem'.$kou}[8] * 4 + ${'smem'.$kou.'item'}[1] * 4 * int(${'smem'.$kou}[8]/10+1);
				}
			}
			if (${'smem'.$kou}[55]==21 or ${'smem'.$kou}[56]==21 or ${'smem'.$kou}[57]==21 or ${'smem'.$kou}[58]==21){
				${'sdmg'.$kou} += (${'smem'.$kou}[15]-${'smem'.$kou.'hp_flg'});
			}
		}
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
	$waza_ritu4 = int(rand($mem3[11] / 10)) + 10;
	if($waza_ritu4 > 80){$waza_ritu4 = 80;}

	$swaza_ritu1 = int(rand($smem1[11] / 10)) + 10;
	if($swaza_ritu1 > 80){$swaza_ritu1 = 80;}
	$swaza_ritu2 = int(rand($smem2[11] / 10)) + 10;
	if($swaza_ritu2 > 80){$swaza_ritu2 = 80;}
	$swaza_ritu3 = int(rand($smem3[11] / 10)) + 10;
	if($swaza_ritu3 > 80){$swaza_ritu3 = 80;}
	$swaza_ritu4 = int(rand($smem4[11] / 10)) + 10;
	if($swaza_ritu4 > 80){$swaza_ritu4 = 80;}

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
		$com4 .= "<font color=\"$red\" size=5>クリティカル！！「$mem3[23]」</font><br>";
		$dmg4 = $dmg4 * 2;
	}

	if ($swaza_ritu1 > int(rand(100))) {
		$scom1 .= "<font color=\"$red\" size=5>クリティカル！！「$smem1[23]」</font><br>";
		$sdmg1 = $sdmg1 * 2;
	}
	if ($swaza_ritu2 > int(rand(100))) {
		$scom2 .= "<font color=\"$red\" size=5>クリティカル！！「$smem2[23]」</font><br>";
		$sdmg2 = $sdmg2 * 2;
	}
	if ($swaza_ritu3 > int(rand(100))) {
		$scom3 .= "<font color=\"$red\" size=5>クリティカル！！「$smem3[23]」</font><br>";
		$sdmg3 = $sdmg3 * 2;
	}
	if ($swaza_ritu4 > int(rand(100))) {
		$scom4 .= "<font color=\"$red\" size=5>クリティカル！！「$smem4[23]」</font><br>";
		$sdmg4 = $sdmg4 * 2;
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

	$k = 0;$sab = 1;$ab=0;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $smem1hp_flg > 0 and $smem1[$his]) {
			$shissatu1="hissatu$smem1[$his]";
			require "./tech/$smem1[$his].pl";
			&$shissatu1;
		}
	}
	$k = 0;$sab = 2;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $smem2hp_flg > 0 and $smem2[$his]) {
			$shissatu2="hissatu$smem2[$his]";
			require "./tech/$smem2[$his].pl";
			&$shissatu2;
		}
	}
	$k = 0;$sab = 3;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $smem3hp_flg > 0 and $smem3[$his]) {
			$shissatu3="hissatu$smem3[$his]";
			require "./tech/$smem3[$his].pl";
			&$shissatu3;
		}
	}
	$k = 0;$sab = 4;
	for($his=51;$his<55;$his++){
		if ($k!=1 and $smem4hp_flg > 0 and $smem4[$his]) {
			$shissatu4="hissatu$smem4[$his]";
			require "./tech/$smem4[$his].pl";
			&$shissatu4;
		}
	}
	if($hpplus1 > 0){$kaihuku1="$hpplus1の回復♪";}
	if($hpplus2 > 0){$kaihuku2="$hpplus2の回復♪";}
	if($hpplus3 > 0){$kaihuku3="$hpplus3の回復♪";}
	if($hpplus4 > 0){$kaihuku4="$hpplus4の回復♪";}
	if($shpplus1 > 0){$skaihuku1="$shpplus1の回復♪";}
	if($shpplus2 > 0){$skaihuku2="$shpplus2の回復♪";}
	if($shpplus3 > 0){$skaihuku3="$shpplus3の回復♪";}
	if($shpplus4 > 0){$skaihuku4="$shpplus4の回復♪";}

	if($item[0] eq "妖刀アジア"){$staisyo1=4;}
	if($mem1item[0] eq "妖刀アジア"){$staisyo2=4;}
	if($mem2item[0] eq "妖刀アジア"){$staisyo3=4;}
	if($mem3item[0] eq "妖刀アジア"){$staisyo4=4;}
	if($smem1item[0] eq "妖刀アジア"){$taisyo1=4;}
	if($smem2item[0] eq "妖刀アジア"){$taisyo2=4;}
	if($smem3item[0] eq "妖刀アジア"){$taisyo3=4;}
	if($smem4item[0] eq "妖刀アジア"){$taisyo4=4;}

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

#--------------#
#　関数初期化　#
#--------------#
sub shokika {
	$dmg1 = 0;
	$dmg2 = 0;
	$dmg3 = 0;
	$dmg4 = 0;
	$sdmg1 = 0;
	$sdmg2 = 0;
	$sdmg3 = 0;
	$sdmg4 = 0;
	$clit1 = "";
	$clit2 = "";
	$clit3 = "";
	$clit4 = "";
	$sclit1 = "";
	$sclit2 = "";
	$sclit3 = "";
	$sclit4 = "";
	$mem1hit_ritu=0;
	$mem2hit_ritu=0;
	$mem3hit_ritu=0;
	$mem4hit_ritu=0;
	$smem1hit_ritu=0;
	$smem2hit_ritu=0;
	$smem3hit_ritu=0;
	$smem4hit_ritu=0;
	$sake1 = 0;
	$sake2 = 0;
	$sake3 = 0;
	$sake4 = 0;
	$ssake1 = 0;
	$ssake2 = 0;
	$ssake3 = 0;
	$ssake4 = 0;
	$waza_ritu = 0;
	$awaza_ritu = 0;
	$bwaza_ritu = 0;
	$cwaza_ritu = 0;
	$swaza_ritu = 0;
	$sawaza_ritu = 0;
	$sbwaza_ritu = 0;
	$scwaza_ritu = 0;
	$com1 = "";
	$com2 = "";
	$com3 = "";
	$com4 = "";
	$scom1 = "";
	$scom2 = "";
	$scom3 = "";
	$scom4 = "";
	$kawasi1 = "";
	$kawasi2 = "";
	$kawasi3 = "";
	$kawasi4 = "";
	$skawasi1 = "";
	$skawasi2 = "";
	$skawasi3 = "";
	$skawasi4 = "";
	$hpplus1 = 0;
	$hpplus2 = 0;
	$hpplus3 = 0;
	$hpplus4 = 0;
	$shpplus1 = 0;
	$shpplus2 = 0;
	$shpplus3 = 0;
	$shpplus4 = 0;
	$kaihuku1 = "";
	$kaihuku2 = "";
	$kaihuku3 = "";
	$kaihuku4 = "";
	$skaihuku1 = "";
	$skaihuku2 = "";
	$skaihuku3 = "";
	$skaihuku4 = "";
	$sinda=0;
	for($tai=0;$tai<5;$tai++){
		${'taisyo'.$tai} =0;
		${'taisyopt'.$tai} =0;
		${'staisyo'.$tai} =0;
		${'staisyopt'.$tai} =0;
		if($khp_flg<1 and $mem1hp_flg<1){${'taisyopt'.$tai}=1;}
		elsif($mem2hp_flg<1 and $mem3hp_flg<1){${'taisyopt'.$tai}=0;}
		else{${'taisyopt'.$tai}=int(rand(2));}
		if(${'taisyopt'.$tai} == 0){
			if($mem1hp_flg<1){${'taisyo'.$tai} = 0;}
			elsif($khp_flg<1){${'taisyo'.$tai} = 1;}
			else{${'taisyo'.$tai} = int(rand(2));}
		}
		if(${'taisyopt'.$tai} == 1){
			if($mem2hp_flg<1){${'taisyo'.$tai} = 3;}	
			elsif($mem3hp_flg<1){${'taisyo'.$tai} = 2;}
			else{${'taisyo'.$tai} = int(rand(2))+2;}
		}
		if($smem1hp_flg<1 and $smem2hp_flg<0){${'staisyopt'.$tai}=1;}
		elsif($smem3hp_flg<1 and $smem4hp_flg<1){${'staisyopt'.$tai}=0;}
		else{${'staisyopt'.$tai}=int(rand(2));}
		if(${'staisyopt'.$tai} == 0){
			if($smem1hp_flg<1){${'staisyo'.$tai} = 1;}
			elsif($smem2hp_flg<1){${'staisyo'.$tai} = 0;}
			else{${'staisyo'.$tai} = int(rand(2));}
		}
		if(${'staisyopt'.$tai} == 1){
			if($smem3hp_flg<1){${'staisyo'.$tai} = 3;}	
			elsif($smem4hp_flg<1){${'staisyo'.$tai} = 2;}
			else{${'staisyo'.$tai} = int(rand(2))+2;}
		}
	}
}

#------------#
#　HPの計算　#
#------------#
sub hp_sum {

	if ($chara[55]==42 or $chara[56]==42 or $chara[57]==42 or $chara[58]==42){$ande1=1;}
	if ($mem1[55]==42 or $mem1[56]==42 or $mem1[57]==42 or $mem1[58]==42){$ande2=1;}
	if ($mem2[55]==42 or $mem2[56]==42 or $mem2[57]==42 or $mem2[58]==42){$ande3=1;}
	if ($mem3[55]==42 or $mem3[56]==42 or $mem3[57]==42 or $mem3[58]==42){$ande4=1;}
	if ($ande1==1 and $khp_flg<1){$andea1+=1;}
	if ($ande2==1 and $mem1hp_flg<1){$andea2+=1;}
	if ($ande3==1 and $mem2hp_flg<1){$andea3+=1;}
	if ($ande4==1 and $mem3hp_flg<1){$andea4+=1;}
	if ($andea1==3){$andea1=0;$khp_flg=$chara[16];}
	if ($andea2==3){$andea2=0;$mem1hp_flg=$mem1[16];}
	if ($andea3==3){$andea3=0;$mem2hp_flg=$mem2[16];}
	if ($andea4==3){$andea4=0;$mem3hp_flg=$mem3[16];}

	if($khp_flg<1){$dmg1 = 0;}
	if($mem1hp_flg<1){$dmg2 = 0;}
	if($mem2hp_flg<1){$dmg3 = 0;}
	if($mem3hp_flg<1){$dmg4 = 0;}

	if ($smem1[55]==42 or $smem1[56]==42 or $smem1[57]==42 or $smem1[58]==42){$sande1=1;}
	if ($smem2[55]==42 or $smem2[56]==42 or $smem2[57]==42 or $smem2[58]==42){$sande2=1;}
	if ($smem3[55]==42 or $smem3[56]==42 or $smem3[57]==42 or $smem3[58]==42){$sande3=1;}
	if ($smem4[55]==42 or $smem4[56]==42 or $smem4[57]==42 or $smem4[58]==42){$sande4=1;}
	if ($sande1==1 and $smem1hp_flg<1){$sandea1+=1;}
	if ($sande2==1 and $smem2hp_flg<1){$sandea2+=1;}
	if ($sande3==1 and $smem3hp_flg<1){$sandea3+=1;}
	if ($sande4==1 and $smem4hp_flg<1){$sandea4+=1;}
	if ($sandea1==3){$sandea1=0;$smem1hp_flg=$smem1[16];}
	if ($sandea2==3){$sandea2=0;$smem2hp_flg=$smem2[16];}
	if ($sandea3==3){$sandea3=0;$smem3hp_flg=$smem3[16];}
	if ($sandea4==3){$sandea4=0;$smem4hp_flg=$smem4[16];}

	if($smem1hp_flg<1){$sdmg1 = 0;}
	if($smem2hp_flg<1){$sdmg2 = 0;}
	if($smem3hp_flg<1){$sdmg3 = 0;}
	if($smem3hp_flg<1){$sdmg4 = 0;}

	if($khp_flg > 0){$khp_flg += $hpplus1;}
	if($mem1hp_flg > 0){$mem1hp_flg += $hpplus2;}
	if($mem2hp_flg > 0){$mem2hp_flg += $hpplus3;}
	if($mem3hp_flg > 0){$mem3hp_flg += $hpplus4;}

	if($mem1hp_flg > 0){$smem1hp_flg += $shpplus1;}
	if($mem2hp_flg > 0){$smem2hp_flg += $shpplus2;}
	if($mem3hp_flg > 0){$smem3hp_flg += $shpplus3;}
	if($mem4hp_flg > 0){$smem4hp_flg += $shpplus4;}

	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0){
			if($sinda!=1){
				$khp_flg = $khp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==1) {
			if($sinda!=2){
				$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==2){
			if($sinda!=3){
				$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==3){
			if($sinda!=4){
				$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
			}
		}
		elsif(${'taisyo'.$tai} ==4){
			if($sinda!=1){
				$khp_flg = $khp_flg - ${'sdmg'.$tai};
			}
			if($sinda!=2){
				$mem1hp_flg = $mem1hp_flg - ${'sdmg'.$tai};
			}
			if($sinda!=3){
				$mem2hp_flg = $mem2hp_flg - ${'sdmg'.$tai};
			}
			if($sinda!=4){
				$mem3hp_flg = $mem3hp_flg - ${'sdmg'.$tai};
			}
		}

		if (${'staisyo'.$tai}==0){
			if($sinda!=5 or int(rand(10))<2){
				$smem1hp_flg = $smem1hp_flg - ${'dmg'.$tai};
			}
		}
		elsif(${'staisyo'.$tai}==1) {
			if($sinda!=6 or int(rand(10))<2){
				$smem2hp_flg = $smem2hp_flg - ${'dmg'.$tai};
			}
		}
		elsif(${'staisyo'.$tai}==2){
			if($sinda!=7 or int(rand(10))<2){
				$smem3hp_flg = $smem3hp_flg - ${'dmg'.$tai};
			}
		}
		elsif(${'staisyo'.$tai}==3){
			if($sinda!=8 or int(rand(10))<2){
				$smem4hp_flg = $smem4hp_flg - ${'dmg'.$tai};
			}
		}
		elsif(${'staisyo'.$tai}==4){
			if($sinda!=5 or int(rand(10))<2){
				$smem1hp_flg = $smem1hp_flg - ${'dmg'.$tai};
			}
			if($sinda!=6 or int(rand(10))<2){
				$smem2hp_flg = $smem2hp_flg - ${'dmg'.$tai};
			}
			if($sinda!=7 or int(rand(10))<2){
				$smem3hp_flg = $smem3hp_flg - ${'dmg'.$tai};
			}
			if($sinda!=8 or int(rand(10))<2){
				$smem4hp_flg = $smem4hp_flg - ${'dmg'.$tai};
			}
		}
	}

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mem1hp_flg > $mem1[16]){
		$mem1hp_flg = $mem1[16];
	}
	if ($mem2hp_flg > $mem2[16]) {
		$mem2hp_flg = $mem2[16];
	}
	if ($mem3hp_flg > $mem3[16]) {
		$mem3hp_flg = $mem3[16];
	}
	if ($smem1hp_flg > $smem1[16]){
		$smem1hp_flg = $smem1[16];
	}
	if ($smem2hp_flg > $smem2[16]){
		$smem2hp_flg = $smem2[16];
	}
	if ($smem3hp_flg > $smem3[16]){
		$smem3hp_flg = $smem3[16];
	}
	if ($smem4hp_flg > $smem4[16]){
		$smem4hp_flg = $smem4[16];
	}
}

#------------#
#　勝敗条件　#
#------------#
sub winlose {

	if ($smem1hp_flg<=0 and $smem2hp_flg<=0 and $smem3hp_flg<=0 and $smem4hp_flg<=0){ 
		$win = 1; last; #勝ち
	}
	elsif ($khp_flg<1 and $mem1hp_flg<1 and $mem2hp_flg<1 and $mem3hp_flg<1) {
		$win = 2; last; #負け
	}
	else{ $win = 3; } #引き分け
}

#------------------#
#回避      	   #
#------------------#
sub mons_kaihi{
	
	#回避率計算
	$ci_plus = $item[2] + $item[16];
	$cd_plus = $item[5] + $item[17];
	$mem1ci_plus = $mem1item[2] + $mem1item[16];
	$mem1cd_plus = $mem1item[5] + $mem1item[17];
	$mem2ci_plus = $mem2item[2] + $mem2item[16];
	$mem2cd_plus = $mem2item[5] + $mem2item[17];
	$mem3ci_plus = $mem3item[2] + $mem3item[16];
	$mem3cd_plus = $mem3item[5] + $mem3item[17];

	$smem1ci_plus = $smem1item[2] + $smem1item[16];
	$smem1cd_plus = $smem1item[5] + $smem1item[17];
	$smem2ci_plus = $smem2item[2] + $smem2item[16];
	$smem2cd_plus = $smem2item[5] + $smem2item[17];
	$smem3ci_plus = $smem3item[2] + $smem3item[16];
	$smem3cd_plus = $smem3item[5] + $smem3item[17];
	$smem4ci_plus = $smem4item[2] + $smem4item[16];
	$smem4cd_plus = $smem4item[5] + $smem4item[17];

	# 命中率
	$mem1hit_ritu += int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $ci_plus;
	$mem2hit_ritu += int($mem1[9] / 3 + $mem1[11] / 10 + $mem1item[10] / 3)+ 40 + $mem1ci_plus;
	$mem3hit_ritu += int($mem2[9] / 3 + $mem2[11] / 10 + $mem2item[10] / 3)+ 40 + $mem2ci_plus;
	$mem4hit_ritu += int($mem3[9] / 3 + $mem3[11] / 10 + $mem3item[10] / 3)+ 40 + $mem3ci_plus;

	$smem1hit_ritu += int($smem1[9] / 3 + $smem1[11] / 10 + $smem1item[10] / 3)+ 40 + $smem1ci_plus;
	$smem2hit_ritu += int($smem2[9] / 3 + $smem2[11] / 10 + $smem2item[10] / 3)+ 40 + $smem2ci_plus;
	$smem3hit_ritu += int($smem3[9] / 3 + $smem3[11] / 10 + $smem3item[10] / 3)+ 40 + $smem3ci_plus;
	$smem4hit_ritu += int($smem4[9] / 3 + $smem4[11] / 10 + $smem4item[10] / 3)+ 40 + $smem4ci_plus;

	if ($chara[55]==25 or $chara[56]==25 or $chara[57]==25 or $chara[58]==25){$yamato1=10;}
	if ($mem1[55]==25 or $mem1[56]==25 or $mem1[57]==25 or $mem1[58]==25){$yamato2=10;}
	if ($mem2[55]==25 or $mem2[56]==25 or $mem2[57]==25 or $mem2[58]==25){$yamato3=10;}
	if ($mem3[55]==25 or $mem3[56]==25 or $mem3[57]==25 or $mem3[58]==25){$yamato4=10;}
	if ($smem1[55]==25 or $smem1[56]==25 or $smem1[57]==25 or $smem1[58]==25){$syamato1=10;}
	if ($smem2[55]==25 or $smem2[56]==25 or $smem2[57]==25 or $smem2[58]==25){$syamato2=10;}
	if ($smem3[55]==25 or $smem3[56]==25 or $smem3[57]==25 or $smem3[58]==25){$syamato3=10;}
	if ($smem4[55]==25 or $smem4[56]==25 or $smem4[57]==25 or $smem4[58]==25){$syamato4=10;}

	# 回避率
	$sake1	+= int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $cd_plus - $syamato1;
	$sake2	+= int($mem1[9] / 10 + $mem1[11] / 20 + $mem1item[10]/10) + $mem1cd_plus - $syamato2;
	$sake3	+= int($mem2[9] / 10 + $mem2[11] / 20 + $mem2item[10]/10) + $mem2cd_plus - $syamato3;
	$sake4	+= int($mem3[9] / 10 + $mem3[11] / 20 + $mem3item[10]/10) + $mem3cd_plus - $syamato4;
	$ssake1	+= int($smem1[9] / 10 + $smem1[11] / 20 + $smem1item[10]/10) + $smem1cd_plus - $yamato1;
	$ssake2	+= int($smem2[9] / 10 + $smem2[11] / 20 + $smem2item[10]/10) + $smem2cd_plus - $yamato2;
	$ssake3	+= int($smem3[9] / 10 + $smem3[11] / 20 + $smem3item[10]/10) + $smem3cd_plus - $yamato3;
	$ssake4	+= int($smem4[9] / 10 + $smem4[11] / 20 + $smem4item[10]/10) + $smem4cd_plus - $yamato4;

	if ($sake1 > 90){$sake1 = 90;}
	if ($sake2 > 90){$sake2 = 90;}
	if ($sake3 > 90){$sake3 = 90;}
	if ($sake4 > 90){$sake4 = 90;}
	if ($ssake1 > 90){$ssake1 = 90;}
	if ($ssake2 > 90){$ssake2 = 90;}
	if ($ssake3 > 90){$ssake3 = 90;}
	if ($ssake4 > 90){$ssake4 = 90;}

	if ($chara[55]==55 or $chara[56]==55 or $chara[57]==55 or $chara[58]==55){$yuuki1=1;}
	if ($mem1[55]==55 or $mem1[56]==55 or $mem1[57]==55 or $mem1[58]==55){$yuuki2=1;}
	if ($mem2[55]==55 or $mem2[56]==55 or $mem2[57]==55 or $mem2[58]==55){$yuuki3=1;}
	if ($mem3[55]==55 or $mem3[56]==55 or $mem3[57]==55 or $mem3[58]==55){$yuuki4=1;}
	if ($smem1[55]==55 or $smem1[56]==55 or $smem1[57]==55 or $smem1[58]==55){$syuuki1=1;}
	if ($smem2[55]==55 or $smem2[56]==55 or $smem2[57]==55 or $smem2[58]==55){$syuuki2=1;}
	if ($smem3[55]==55 or $smem3[56]==55 or $smem3[57]==55 or $smem3[58]==55){$syuuki3=1;}
	if ($smem4[55]==55 or $smem4[56]==55 or $smem4[57]==55 or $smem4[58]==55){$syuuki4=1;}

	for($tai=0;$tai<5;$tai++){
		if (${'taisyo'.$tai} ==0 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $item[4]*(2+int($chara[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{ ${'sdmg'.$tai} = ${'sdmg'.$tai} - $item[4] * (2+int($chara[10]/10+1)); }
			if ($yuuki1!=1 and int($sake1 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]は身をかわした！</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==1 or ${'taisyo'.$tai} ==4) {
			if (${'sdmg'.$tai} < $mem1item[4]*(2+int($mem1[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem1item[4] * (2+int($mem1[10]/10+1)); }
			if ($yuuki2!=1 and int($sake2 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem1[4]は身をかわした！</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==2 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $mem2item[4]*(2+int($mem2[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem2item[4] * (2+int($mem2[10]/10+1)); }
			if ($yuuki3!=1 and int($sake3 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem2[4]は身をかわした！</FONT>";
			}
		}
		if(${'taisyo'.$tai} ==3 or ${'taisyo'.$tai} ==4){
			if (${'sdmg'.$tai} < $mem3item[4]*(2+int($mem3[10]/10+1))){ ${'sdmg'.$tai}=0; }
			else{${'sdmg'.$tai} = ${'sdmg'.$tai}-$mem3item[4] * (2+int($mem3[10]/10+1)); }
			if ($yuuki4!=1 and int($sake4 - (${'smem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'sdmg'.$tai} = 0;
				${'kawasi'.$tai} = "<FONT SIZE=4 COLOR=\"$red\">$mem3[4]は身をかわした！</FONT>";
			}
		}

		if (${'staisyo'.$tai}==0 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem1item[4]*(2+int($smem1[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem1item[4] * (2+int($smem1[10]/10+1)); }
			if ($syuuki1!=1 and int($ssake1 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem1[4]は身をかわした！</FONT>";
			}
		}
		if(${'staisyo'.$tai}==1 or ${'staisyo'.$tai}==4) {
			if (${'dmg'.$tai} < $smem2item[4]*(2+int($smem2[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem2item[4] * (2+int($smem2[10]/10+1)); }
			if ($syuuki2!=1 and int($ssake2 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem2[4]は身をかわした！</FONT>";
			}
		}
		if(${'staisyo'.$tai}==2 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem3item[4]*(2+int($smem3[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem3item[4] * (2+int($smem1[10]/10+1)); }
			if ($syuuki3!=1 and int($ssake3 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem3[4]は身をかわした！</FONT>";
			}
		}
		if(${'staisyo'.$tai}==3 or ${'staisyo'.$tai}==4){
			if (${'dmg'.$tai} < $smem4item[4]*(2+int($smem4[10]/10+1))){ ${'dmg'.$tai}=0; }
			else{${'dmg'.$tai} = ${'dmg'.$tai}-$smem4item[4] * (2+int($smem4[10]/10+1)); }
			if ($syuuki4!=1 and int($ssake4 - (${'mem'.$tai.'hit_ritu'} / 3)) > int(rand(100))) {
				${'dmg'.$tai} = 0;
				${'skawasi'.$tai} ="<FONT SIZE=4 COLOR=\"$red\">$smem4[4]は身をかわした！</FONT>";
			}
		}
	}

	if($chara[55]==34 or $chara[56]==34 or $chara[57]==34 or $chara[58]==34){$sdmg1=int($sdmg1*3/4);}
	if($mem1[55]==34 or $mem1[56]==34 or $mem1[57]==34 or $mem1[58]==34){$sdmg2=int($sdmg2*3/4);}
	if($mem2[55]==34 or $mem2[56]==34 or $mem2[57]==34 or $mem2[58]==34){$sdmg3=int($sdmg3*3/4);}
	if($mem3[55]==34 or $mem3[56]==34 or $mem3[57]==34 or $mem3[58]==34){$sdmg4=int($sdmg4*3/4);}

	if($smem1[55]==34 or $smem1[56]==34 or $smem1[57]==34 or $smem1[58]==34){$dmg1=int($dmg1*3/4);}
	if($smem2[55]==34 or $smem2[56]==34 or $smem2[57]==34 or $smem2[58]==34){$dmg2=int($dmg2*3/4);}
	if($smem3[55]==34 or $smem3[56]==34 or $smem3[57]==34 or $smem3[58]==34){$dmg3=int($dmg3*3/4);}
	if($smem4[55]==34 or $smem4[56]==34 or $smem4[57]==34 or $smem4[58]==34){$dmg4=int($dmg4*3/4);}
}

#------------------#
#　戦闘状況      　#
#------------------#
sub monsbattle_sts {

	$battle_date[$j] = <<"EOM";
	<TABLE BORDER=0 align="center">
	<TR>
	<TD COLSPAN= "3" ALIGN= "center">
	$iターン
	</TD>
	</TR>
EOM
	if ($i == 1) {
		$battle_date[$j] .= <<"EOM";
		<TD>
EOM
		if($khp_flg>=0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$chara[6]]">
EOM
		}
		if($mem1hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem1[6]]">
EOM
		}
		if($mem2hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem2[6]]">
EOM
		}
		if($mem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$mem3[6]]">
EOM
		}
		$battle_date[$j] .= <<"EOM";
		</TD><TD></TD><TD></TD><TD>
EOM
		if($smem1hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$smem1[6]]">
EOM
		}
		if($smem2hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$smem2[6]]">
EOM
		}
		if($smem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$smem3[6]]">
EOM
		}
		if($smem4hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path/$chara_img[$smem4[6]]">
EOM
		}
	}
	$battle_date[$j] .= <<"EOM";
	</TD>
	<TR><TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	なまえ	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	職業	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($khp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$chara[4]		</TD>
		<TD class= "b2">	$khp_flg\/$chara[16]	</TD>
		<TD class= "b2">	$chara_syoku[$chara[14]]</TD>
		<TD class= "b2">	$chara[18]		</TD></TR>
EOM
	}
	if($mem1hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$mem1[4]		</TD>
		<TD class= "b2">	$mem1hp_flg\/$mem1[16]	</TD>
		<TD class= "b2">	$chara_syoku[$mem1[14]]	</TD>
		<TD class= "b2">	$mem1[18]		</TD></TR>
EOM
	}
	if($mem2hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$mem2[4]		</TD>
		<TD class= "b2">	$mem2hp_flg\/$mem2[16]	</TD>
		<TD class= "b2">	$chara_syoku[$mem2[14]]	</TD>
		<TD class= "b2">	$mem2[18]		</TD></TR>
EOM
	}
	if($mem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$mem3[4]		</TD>
		<TD class= "b2">	$mem3hp_flg\/$mem3[16]	</TD>
		<TD class= "b2">	$chara_syoku[$mem3[14]]	</TD>
		<TD class= "b2">	$mem3[18]		</TD></TR>
EOM
	}
	$battle_date[$j] .= <<"EOM";
	</TABLE></TD><TD></TD><TD><FONT SIZE=5 COLOR= "#9999DD">VS</FONT></TD>
	<TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	なまえ	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	職業	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($smem1hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$smem1[4]		</TD>
		<TD class= "b2">	$smem1hp_flg\/$smem1[16]</TD>
		<TD class= "b2">	$chara_syoku[$smem1[14]]</TD>
		<TD class= "b2">	$smem1[18]		</TD></TR>
EOM
	}
	if($smem2hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$smem2[4]		</TD>
		<TD class= "b2">	$smem2hp_flg\/$smem2[16]</TD>
		<TD class= "b2">	$chara_syoku[$smem2[14]]</TD>
		<TD class= "b2">	$smem2[18]		</TD></TR>
EOM
	}
	if($smem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$smem3[4]		</TD>
		<TD class= "b2">	$smem3hp_flg\/$smem3[16]</TD>
		<TD class= "b2">	$chara_syoku[$smem3[14]]</TD>
		<TD class= "b2">	$smem3[18]		</TD></TR>
EOM
	}
	if($smem4hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$smem4[4]		</TD>
		<TD class= "b2">	$smem4hp_flg\/$smem4[16]</TD>
		<TD class= "b2">	$chara_syoku[$smem4[14]]</TD>
		<TD class= "b2">	$smem4[18]		</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]達の攻撃！！</td></tr>
EOM
	for($tai=0;$tai<5;$tai++){
		if(${'staisyo'.$tai}==0){${'mname'.$tai}=$smem1[4];}
		if(${'staisyo'.$tai}==1){${'mname'.$tai}=$smem2[4];}
		if(${'staisyo'.$tai}==2){${'mname'.$tai}=$smem3[4];}
		if(${'staisyo'.$tai}==3){${'mname'.$tai}=$smem4[4];}
		if(${'staisyo'.$tai}==4){${'mname'.$tai}="敵全員";}
	}
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com1 $clit1 $skawasi1 $mname1 に <font class= "yellow">$dmg1</font> のダメージを与えた。<font class= "yellow">$kaihuku1</font><br>　</td></tr>
EOM
	}
	if($mem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com2 $skawasi2 $mname2 に <font class= "yellow">$dmg2</font> のダメージを与えた。<font class= "yellow">$kaihuku2</font><br>　</td></tr>
EOM
	}
	if($mem2hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com3 $skawasi3 $mname3 に <font class= "yellow">$dmg3</font> のダメージを与えた。<font class= "yellow">$kaihuku3</font><br>　</td></tr>
EOM
	}
	if($mem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com4 $skawasi4 $mname4 に <font class= "yellow">$dmg4</font> のダメージを与えた。<font class= "yellow">$kaihuku4</font><br>　</td></tr>
EOM
	}
	for($tai=0;$tai<5;$tai++){
		if(${'taisyo'.$tai}==0){${'smname'.$tai}=$chara[4];}
		if(${'taisyo'.$tai}==1){${'smname'.$tai}=$mem1[4];}
		if(${'taisyo'.$tai}==2){${'smname'.$tai}=$mem2[4];}
		if(${'taisyo'.$tai}==3){${'smname'.$tai}=$mem3[4];}
		if(${'taisyo'.$tai}==4){${'smname'.$tai}="敵全員";}
	}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">$smem1[4]達の攻撃！！</td></tr>
EOM
	if($smem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom1 $kawasi1 $smname1に <font class= "yellow">$sdmg1</font> のダメージを与えた。<font class= "yellow">$skaihuku1</font><br>　</td></tr>
EOM
	}
	if($smem2hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom2 $kawasi2 $smname2に <font class= "yellow">$sdmg2</font> のダメージを与えた。<font class= "yellow">$skaihuku2</font><br>　</td></tr>
EOM
	}
	if($smem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom3 $kawasi3 $smname3 に <font class= "yellow">$sdmg3</font> のダメージを与えた。<font class= "yellow">$skaihuku3</font><br>　</td></tr>
EOM
	}
	if($smem4hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom4 $kawasi4 $smname4に <font class= "yellow">$sdmg4</font> のダメージを与えた。<font class= "yellow">$skaihuku4</font><br>　</td></tr>
EOM
	}
	$battle_date[$j] .= "</table>";
}

#------------------#
#戦闘結果判定      #
#------------------#
sub sentoukeka{
	open(IN,"siro.cgi");
	@siro_data = <IN>;
	close(IN);
	$siro_i=0;$sirotime=time();
	foreach(@siro_data){
		($siro_name,$siro_seigen,$gg_name,$sihaisya,$sihaisyaid,$kankaku,$seisanhin,$seisando,$maxseisando) = split(/<>/);
		if($siro_name eq $in{'siro_name'}){last;}
		$siro_i++;
	}
	if ($win==1) {
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		$seisanhit=0;
		foreach(@seisan_data){
			($syoukyu,$sno,$sname) = split(/<>/);
			if($syoukyu * 10 <= $gg_lv){$seisanhit++;}
		}
		$sei_ran=int(rand($seisanhit));
		($syoukyu,$sno,$stname) = split(/<>/,$seisan_data[$sei_ran]);
		if($siro_name eq "無敵生産城"){$stname="無敵";}
		$chara[22] += 1;
 		$comment .= "<b><font size=5>$chara[4]は、戦闘に勝利した！！$stnameの生産を開始した。</font></b><br>";
		$siro_data[$siro_i] = "$siro_name<>$siro_seigen<>$chara[66]<>$chara[4]<>$chara[0]<>$sirotime<>$stname<>0<>$maxseisando<>\n";
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が攻城戦で勝利し、$siro_nameを制覇し、$stnameの生産を始めました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');


	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$eg</span>";

	unshift(@CLOG,"kokuti<>告知<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);


		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[66]){
				$gg_maxmem=$array[3] + 4;
				$array[2] += 100000;
				if($array[2] > $array[3] * 1500000){
					$comment .= "<font class=red size=7>ギルドレベルが上がった！</font><br>";
					$array[3] += 1;
					$array[2] = 0;
				}
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
	} elsif ($win==3) {
		$comment .= "<b><font size=5>$chara[4]は、逃げ出した・・・♪</font></b><br>";
		$siro_data[$siro_i] = "$siro_name<>$siro_seigen<>$gg_name<>$sihaisya<>$sihaisyaid<>$sirotime<>$seisanhin<>$seisando<>$maxseisando<>\n";
		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[66]){
				$gg_maxmem=$array[3] + 4;
				$array[2] += 25000;
				if($array[2] > $array[3] * 1500000){
					$comment .= "<font class=red size=7>ギルドレベルが上がった！</font><br>";
					$array[3] += 1;
					$array[2] = 0;
				}
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
	} else {
		$comment .= "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
		if($seisando!=$maxseisando){
			$seisando+=1;
			if($seisando==$maxseisando){
				open(IN,"seisanmati.cgi");
				@seisanmati_data = <IN>;
				close(IN);
				push(@seisanmati_data,"$sihaisya<>$seisanhin<>\n");
				open(OUT,">seisanmati.cgi");
				print OUT @seisanmati_data;
				close(OUT);
				$ssss=1;
				$seisando=0;
			}
		}
		$siro_data[$siro_i] = "$siro_name<>$siro_seigen<>$gg_name<>$sihaisya<>$sihaisyaid<>$sirotime<>$seisanhin<>$seisando<>$maxseisando<>\n";
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		if($ssss==1){
$eg="$sihaisya様($gg_name)の支配する$siro_nameが防衛され、$seisanhinの生産が完了しました。";
		}else{
$eg="$sihaisya様($gg_name)の支配する$siro_nameが防衛されました。$seisanhin生産度$seisando / $maxseisando";
		}
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');


	$text_color = "#66FF99";
	$text_size = 13;

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	$log_chat = "chat_log.cgi";

	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > 100) { pop(@CLOG); }

	&unlock($lock_file,'CA');
	$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$eg</span>";

	unshift(@CLOG,"kokuti<>告知<>$comment<>$get_day<>\"$hour:$min\"<><>9999<>\n");

	$log_chat = "chat_log.cgi";

	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);


		open(IN,"allguild.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[66]){
				$gg_maxmem=$array[4] + 4;
				$array[2] += 10000;
				if($array[2] > $array[3] * 3000000){
					$comment .= "<font class=red size=7>ギルドレベルが上がった！</font><br>";
					$array[3] += 1;
					$array[2] = 0;
				}
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
	open(OUT,">siro.cgi");
	print OUT @siro_data;
	close(OUT);

	$chara[21] ++;
	$chara[25] --;
	$chara[27] = time();
	$chara[28] = $bossd;
}

#------------------#
# 戦闘後のＨＰ処理 #
#------------------#
sub hp_after{
	$chara[15] = $chara[16];
}

#----------------------#
# 戦闘後のフッター処理 #
#----------------------#
sub mons_footer{
	if ($win==1) {
		print "$comment 城を制覇した。<br>\n";
	} elsif($win==2){
		print "$comment 防衛側にやられた。<br>\n";
	} elsif($win==3){
		print "$comment ギリギリ足りなかった。\n";
	}

	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
}
