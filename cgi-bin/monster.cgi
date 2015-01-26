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

require 'sankasya.pl';

# 戦闘ライブラリの読み込み
require 'battle.pl';
# モンスター戦用ライブラリ
require 'mbattle.pl';
require 'item.pl';
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
if($mode == 1){&monster;}
else{&$mode;}

exit;

#----------------------#
#  モンスターとの戦闘  #
#----------------------#
sub monster {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&guest_list;
	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	if (!$chara[25]) {
		&error("一度キャラクターと闘ってください");
	}
	if($chara[63]>=1){&error("入所中です！！");}
	if(!$chara[144]){$chara[144]=time();}
	$koutime=time();
	$kankaku = $chara[144] - $koutime + 600;
	if($kankaku<int(rand(100+$chara[70]*100))){&error("クールタイム。一度ステータス画面に戻りましょう。");}

	$chara[139]++;
	if(int(rand(300))==0){$chara[139]=451;}
	if($chara[139] > 450){
		&error("一度チャンプと闘ってください");
	}
	if($chara[18] > 500 and int(rand(500))==0){
		&error("最近頑張ってるでしょ？");
	}
	$ntime = time();
	$b_time = $m_time;
	$ztime = $ntime - $chara[27];
	$ztime = $b_time - $ztime;

	if ($ztime > 0) { &mons_error; }

	&time_check;

	&item_load;

	&acs_add;

	if ($in{'mons_file'} eq "monster0"){$place = 0;}
	elsif ($in{'mons_file'} eq "monster1"){$place = 1;}
	elsif ($in{'mons_file'} eq "monster2"){$place = 2;}
	elsif ($in{'mons_file'} eq "monster3"){$place = 3;}
	elsif ($in{'mons_file'} eq "monster4"){$place = 4;}
	elsif ($in{'mons_file'} eq "monster5"){$place = 5;}
	elsif ($in{'mons_file'} eq "monster6"){$place = 6;}
	elsif ($in{'mons_file'} eq "monster7"){$place = 7;}
	elsif ($in{'mons_file'} eq "monster8"){$place = 8;}
	elsif ($in{'mons_file'} eq "monster9"){$place = 9;}
	elsif ($in{'mons_file'} eq "monster10"){$place = 10;}
	elsif ($in{'mons_file'} eq "monster11"){$place = 11;}
	elsif ($in{'mons_file'} eq "monster12"){$place = 12;}
	elsif ($in{'mons_file'} eq "monster13"){$place = 13;}
	elsif ($in{'mons_file'} eq "monster14"){$place = 14;}
	elsif ($in{'mons_file'} eq "monster15"){$place = 15;}
	elsif ($in{'mons_file'} eq "monster16"){$place = 16;}
	elsif ($in{'mons_file'} eq "monster17"){$place = 17;}
	elsif ($in{'mons_file'} eq "monster18"){$place = 18;}
	elsif ($in{'mons_file'} eq "monster27"){$place = 27;}
	elsif ($in{'mons_file'} eq "monster28"){$place = 28;}
	elsif ($in{'mons_file'} eq "monster29"){$place = 29;}
	elsif ($in{'mons_file'} eq "monster30"){$place = 30;}
	elsif ($in{'mons_file'} eq "monster31"){$place = 31;}
	else{$place=99;}
	open(IN,"senyou.cgi");
	@member_data = <IN>;
	close(IN);
	foreach (@member_data) {
		($cid,$cno) = split(/<>/);
		if ($cno == $chara[6] and $cid ne $chara[0]) {
			&error("アイコンを変えてください。$back_form");
		}
	}

	#ボスがいるかチェック

	open(IN,"./data/bosson.ini");
	@bosson_data = <IN>;
	close(IN);
	foreach(@bosson_data){
		($name,$on) = split(/<>/);
		if($on){
			if($on==$place){
				#ボスキャラ
				open(IN,"$boss_monster");
				@MONSTER = <IN>;
				close(IN);
				$kazu=2;
				$bossdayo=1;
				last;
			}	
		}
	}
	if($on and $on==$place){
	}else{
		if($chara[70]<1){$monster_file = "$in{'mons_file'}\_monster";}
		else{$monster_file = "$in{'mons_file'}\_2monster";}
		open(IN,"$$monster_file");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		if($place==0){$kazu=2;}
		elsif($place==1){$kazu=3;}
		elsif($place==2){$kazu=3;}
		elsif($place==3){$kazu=3;}
		elsif($place==4){$kazu=4;}
		elsif($place==5){$kazu=4;}
		elsif($place==6){$kazu=5;}
		elsif($place==7){$kazu=5;}
		elsif($place==14){$kazu=5;}
		elsif($place==15){$kazu=3;}
		elsif($place==16){$kazu=2;}
		elsif($place==17){$kazu=3;}
		elsif($place==18){$kazu=5;}
		elsif($place==29){$kazu=5;}
		elsif($place==30){$kazu=4;}
		elsif($place==31){$kazu=3;}
		else{$kazu=2;}
	}
	$ymrnd=600-int($chara[18]/79);
	if(int(($mon+$mday*$hour)%20)==0){$ymrnd=int($ymrnd/2);}
	if($place!=17 and $ymrnd<100){$ymrnd=100;}
	if($place==17 and $ymrnd<70){$ymrnd=70;}
	if($chara[70]>0 and int(rand($ymrnd))==0){
		open(IN,"data/yami.ini");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		$r_no = int(rand($r_no)+1);
		$kazu=2;
	}
	&mons_read;

	#自分のメンバー決定
	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data){
		($pp_name,$pp_leader,$pp_lv,$pp_mem,$pp_com,$pp_mem1,$pp_mem2,$pp_mem3) = split(/<>/);
		if($pp_name eq $chara[61]){$hit=1;last;}
	}
	if($hit){
		if($pp_mem1 ne ""){
			$lock_file = "$lockfolder/$pp_mem1.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pp_mem1.cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pp_mem1.lock";
			&unlock($lock_file,'DR');
			@pmem1 = split(/<>/,$member1_data);
		}
		if($pp_mem2 ne ""){
			$lock_file = "$lockfolder/$pp_mem2.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pp_mem2.cgi");
			$member2_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pp_mem2.lock";
			&unlock($lock_file,'DR');
			@pmem2 = split(/<>/,$member2_data);
		}
		if($pp_mem3 ne ""){
			$lock_file = "$lockfolder/$pp_mem3.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pp_mem3.cgi");
			$member3_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pp_mem3.lock";
			&unlock($lock_file,'DR');
			@pmem3 = split(/<>/,$member3_data);
		}
		$tlv=0;$tts=0;
		if($chara[70]<1){$tlv=1;}elsif($chara[70]<2){$tlv=2;}else{$tlv=3;}
		if($pmem1[70]<1){$pmem1lv=$pmem1[18]+$pmem1[37]*100;}
		elsif($pmem1[70]<2){$pmem1lv=$pmem1[18];}
		else{$tts=1;}
		if($pmem2[70]<1){$pmem2lv=$pmem2[18]+$pmem2[37]*100;}
		elsif($pmem2[70]<2){$pmem2lv=$pmem2[18];}
		else{$tts=2;}
		if($pmem3[70]<1){$pmem3lv=$pmem3[18]+$pmem3[37]*100;}
		elsif($pmem3[70]<2){$pmem3lv=$pmem3[18];}
		else{$tts=3;}
		$hhit=0;$member=1;
		if($tlv==3 or $tts>0){
			if($chara[0] eq $pmem1[0]){
				if($pmem2lv > $pmem1lv - 20000 and $pmem2lv < $pmem1lv + 20000){
					@mem1 = @pmem2;$mem1hp_flg=$mem1[15];$member++;
				}
				if($pmem3lv > $pmem1lv - 20000 and $pmem3lv < $pmem1lv + 20000){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem2[0]){
				if($pmem2lv > $pmem1lv - 20000 and $pmem2lv < $pmem1lv + 20000){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem3lv > $pmem1lv - 20000 and $pmem3lv < $pmem1lv + 20000){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem3[0]){
				if($pmem3lv > $pmem1lv - 20000 and $pmem3lv < $pmem1lv + 20000){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem2lv > $pmem1lv - 20000 and $pmem2lv < $pmem1lv + 20000){
					@mem2 = @pmem2;$mem2hp_flg=$mem2[15];$member++;
				}
			}
		}
		elsif($tlv==1){
			if($chara[0] eq $pmem1[0]){
				if($pmem2lv > $pmem1lv - 300 and $pmem2lv < $pmem1lv + 300){
					@mem1 = @pmem2;$mem1hp_flg=$mem1[15];$member++;
				}
				if($pmem3lv > $pmem1lv - 300 and $pmem3lv < $pmem1lv + 300){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem2[0]){
				if($pmem2lv > $pmem1lv - 300 and $pmem2lv < $pmem1lv + 300){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem3lv > $pmem1lv - 300 and $pmem3lv < $pmem1lv + 300){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem3[0]){
				if($pmem3lv > $pmem1lv - 300 and $pmem3lv < $pmem1lv + 300){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem2lv > $pmem1lv - 300 and $pmem2lv < $pmem1lv + 300){
					@mem2 = @pmem2;$mem2hp_flg=$mem2[15];$member++;
				}
			}
		}
		elsif($tlv==2){
			$ptlim=int($chara[18]/1000)*50+100;
			if($chara[0] eq $pmem1[0]){
				if($pmem2lv > $pmem1lv - $ptlim and $pmem2lv < $pmem1lv + $ptlim){
					@mem1 = @pmem2;$mem1hp_flg=$mem1[15];$member++;
				}elsif($pmem2[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem1 = @pmem2;$mem1hp_flg=$mem1[15];$member++;
				}
				if($pmem3lv > $pmem1lv - $ptlim and $pmem3lv < $pmem1lv + $ptlim){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}elsif($pmem3[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem2[0]){
				if($pmem2lv > $pmem1lv - $ptlim and $pmem2lv < $pmem1lv + $ptlim){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}elsif($pmem1[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem3lv > $pmem1lv - $ptlim and $pmem3lv < $pmem1lv + $ptlim){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}elsif($pmem3[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem2 = @pmem3;$mem2hp_flg=$mem2[15];$member++;
				}
			}
			elsif($chara[0] eq $pmem3[0]){
				if($pmem3lv > $pmem1lv - $ptlim and $pmem3lv < $pmem1lv + $ptlim){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}elsif($pmem1[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem1 = @pmem1;$mem1hp_flg=$mem1[15];$member++;$hhit=1;
				}
				if($hhit==1 and $pmem2lv > $pmem1lv - $ptlim and $pmem2lv < $pmem1lv + $ptlim){
					@mem2 = @pmem2;$mem2hp_flg=$mem2[15];$member++;
				}elsif($pmem2[0] eq "jupiter" or $chara[0] eq "jupiter"){
					@mem2 = @pmem2;$mem2hp_flg=$mem2[15];$member++;
				}
			}
		}
		if($member>1){
			open(IN,"./item/$mem1[0].cgi");
			$mem1item_log = <IN>;
			close(IN);
			@mem1item = split(/<>/,$mem1item_log);
		}
		if($member>2){
			open(IN,"./item/$mem2[0].cgi");
			$mem2item_log = <IN>;
			close(IN);
			@mem2item = split(/<>/,$mem2item_log);
		}
	}

	$khp_flg = $chara[15];

	if($chara[42]){
		$mem3hp_flg = $chara[42];
	}
	if($on and $on==$place){
		$smem1hp_flg = $msp1;
		$smem2hp_flg = $msp2;
		$smem3hp_flg = $msp3;
		$smem4hp_flg = $msp4;
		$smem1hp = $maxhp1;
		$smem2hp = $maxhp2;
		$smem3hp = $maxhp3;
		$smem4hp = $maxhp4;
	}else{
		$smem1hp_flg = int(rand($mrand1)) + $msp1;
		$smem2hp_flg = int(rand($mrand2)) + $msp2;
		$smem3hp_flg = int(rand($mrand3)) + $msp3;
		$smem4hp_flg = int(rand($mrand4)) + $msp4;
		$smem1hp = $smem1hp_flg;
		$smem2hp = $smem2hp_flg;
		$smem3hp = $smem3hp_flg;
		$smem4hp = $smem4hp_flg;
	}

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	$sai=0;
	@battle_date=();
	if($chara[20]<1 or $chara[20]>10){$chara[20] = 1;}
	else{$chara[20]= $chara[20]+ $chara[20]/10;}

	if($member==2){$turn=$turn2;}
	if($member==3){$turn=$turn3;}
$ticket=0;
	while($i<=$turn and $sai<200) {

		&shokika;

		&tyousensya;
		
		&tyosenwaza;
		&mons_waza;

		&acs_waza;
		&mons_atowaza;
		
		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
		$sai++;

	}
	if ($in{'mons_file'} eq "monster29" and $win==1){
		$keikin=int($chara[93]/2);
		if($keikin>0){
			$comment .= "<b><font size=5 color=red>警官から$keikinG手に入れたっ！</font></b><br>";
			$chara[19]+=$keikin;$chara[93]=0;
		}
	}elsif($in{'mons_file'} eq "monster29"){
		$keikin=int($chara[93]/10);
		if($keikin>0){
			$comment .= "<b><font size=5 color=red>情けとして警官から$keikinG手に入れた。</font></b><br>";
			$chara[19]+=$keikin;$chara[93]=0;
		}
	}
	if($ticket>0){
		$chara[189]+=1;
			$comment .= <<"EOM";
			<font class=\"red\" size=5>闇空間チケットを手に入れたッ！！</font><br>
EOM
	}
	if($ticket2>0){
		$chara[146]+=1;
			$comment .= <<"EOM";
			<font class=\"red\" size=5>悪魔界チケットを手に入れたッ！！</font><br>
EOM
	}
	if ($chara[24]==1400){
		if ($item[35]==3 or $item[36]==3){
			$bukinamae=$item[0];
			$item[0]="ツルハシ";
		}
		if ($item[35]==103 or $item[36]==103){
			$bukinamae=$item[0];
			$item[0]="山のツルハシ";
		}
		if ($item[35]==203 or $item[36]==203){
			$bukinamae=$item[0];
			$item[0]="黄金のツルハシ";
		}
	}
	if($chara[70]>0 and $win==1){
		$gishi=0;
		if($place==14){
			if($ssmname1 eq "スノム" or $ssmname1 eq "スノミ" or $ssmname2 eq "スノム" or $ssmname2 eq "スノミ" or $ssmname3 eq "スノム" or $ssmname3 eq "スノミ" or $ssmname4 eq "スノム" or $ssmname4 eq "スノミ"){
				if(int(rand(250))==0){
					$gishi=int(rand(4)+30);
				}
			}
		}
		if($chara[140]==2 and $jisin==1){
			if($item[0] eq "ツルハシ" and int(rand(1))==0){$gishi=int(rand(1)+24);}
			elsif($item[0] eq "山のツルハシ" and int(rand(1))==0){$gishi=int(rand(1)+24);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(1))==0){$gishi=int(rand(1)+24);}
			elsif(int(rand(1))==0){$gishi=int(rand(1)+24);}
		}
		if($item[0] eq "黄金のツルハシ"){
		if(int(($mon*$mday)%7)>3){$gston=500;}
		if($chara[24]==1400){$gston=-1000;}
			if(int(rand(1000-$gston))==0){$gishi=int(rand(1)+27);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(250))==0){
				$gishi=int(rand(1)+27);
			}}
		}
		if($chara[37] >= 100){
			if(int(rand(1000))==0){$gishi=int(rand(1)+28);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(250))==0){
				$gishi=int(rand(1)+28);
			}}
		}
		if($bossdayo==1){
			if($item[0] eq "ツルハシ" and int(rand(12))==0){$gishi=int(rand(1)+25);}
			elsif($item[0] eq "山のツルハシ" and int(rand(8))==0){$gishi=int(rand(1)+25);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(4))==0){$gishi=int(rand(1)+25);}
			elsif(int(rand(20))==0){$gishi=int(rand(1)+25);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(250))==0){
				$gishi=int(rand(1)+27);
			}}
		}elsif($place == 0){
			if($item[0] eq "ツルハシ" and int(rand(12))==0){$gishi=int(rand(2)+1);}
			elsif($item[0] eq "山のツルハシ" and int(rand(8))==0){$gishi=int(rand(2)+1);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(4))==0){$gishi=int(rand(2)+1);}
			elsif(int(rand(20))==0){$gishi=int(rand(2)+1);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(2))==0){
				$gishi=int(rand(2)+1);
			}}
		}elsif($place == 1){
			if($item[0] eq "ツルハシ" and int(rand(24))==0){$gishi=int(rand(2)+2);}
			elsif($item[0] eq "山のツルハシ" and int(rand(16))==0){$gishi=int(rand(2)+2);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(8))==0){$gishi=int(rand(2)+2);}
			elsif(int(rand(40))==0){$gishi=int(rand(2)+2);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(4))==0){
				$gishi=int(rand(2)+2);
			}}
		}elsif($place == 2){
			if($item[0] eq "ツルハシ" and int(rand(36))==0){$gishi=int(rand(2)+3);}
			elsif($item[0] eq "山のツルハシ" and int(rand(24))==0){$gishi=int(rand(2)+3);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(12))==0){$gishi=int(rand(2)+3);}
			elsif(int(rand(60))==0){$gishi=int(rand(2)+3);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(6))==0){
				$gishi=int(rand(2)+3);
			}}
		}elsif($place == 3){
			if($item[0] eq "ツルハシ" and int(rand(48))==0){$gishi=int(rand(2)+4);}
			elsif($item[0] eq "山のツルハシ" and int(rand(32))==0){$gishi=int(rand(2)+4);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(16))==0){$gishi=int(rand(2)+4);}
			elsif(int(rand(80))==0){$gishi=int(rand(2)+4);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(8))==0){
				$gishi=int(rand(2)+4);
			}}
		}elsif($place == 4){
			if($item[0] eq "ツルハシ" and int(rand(60))==0){$gishi=int(rand(2)+5);}
			elsif($item[0] eq "山のツルハシ" and int(rand(40))==0){$gishi=int(rand(2)+5);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(20))==0){$gishi=int(rand(2)+5);}
			elsif(int(rand(100))==0){$gishi=int(rand(2)+5);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(10))==0){
				$gishi=int(rand(2)+5);
			}}
		}elsif($place == 5){
			if($item[0] eq "ツルハシ" and int(rand(72))==0){$gishi=int(rand(2)+6);}
			elsif($item[0] eq "山のツルハシ" and int(rand(48))==0){$gishi=int(rand(2)+6);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(24))==0){$gishi=int(rand(2)+6);}
			elsif(int(rand(120))==0){$gishi=int(rand(2)+6);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(12))==0){
				$gishi=int(rand(2)+6);
			}}
		}elsif($place == 6){
			if($item[0] eq "ツルハシ" and int(rand(84))==0){$gishi=int(rand(2)+7);}
			elsif($item[0] eq "山のツルハシ" and int(rand(56))==0){$gishi=int(rand(2)+7);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(28))==0){$gishi=int(rand(2)+7);}
			elsif(int(rand(140))==0){$gishi=int(rand(2)+7);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(14))==0){
				$gishi=int(rand(2)+7);
			}}
		}elsif($place == 7){
			if($item[0] eq "ツルハシ" and int(rand(96))==0){$gishi=int(rand(1)+8);}
			elsif($item[0] eq "山のツルハシ" and int(rand(64))==0){$gishi=int(rand(1)+8);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(32))==0){$gishi=int(rand(1)+8);}
			elsif(int(rand(160))==0){$gishi=int(rand(1)+8);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(16))==0){
				$gishi=int(rand(1)+8);
			}}
		}elsif($place == 14 and $santa==1){
			if($item[0] eq "ツルハシ" and int(rand(30))==0){$gishi=int(rand(1)+23);}
			elsif($item[0] eq "山のツルハシ" and int(rand(20))==0){$gishi=int(rand(1)+23);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(10))==0){$gishi=int(rand(1)+23);}
			elsif(int(rand(50))==0){$gishi=int(rand(1)+23);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(5))==0){
				$gishi=int(rand(1)+23);
			}}
		}elsif($place == 15){
			if($item[0] eq "ツルハシ" and int(rand(120))==0){$gishi=int(rand(1)+9);}
			elsif($item[0] eq "山のツルハシ" and int(rand(80))==0){$gishi=int(rand(1)+9);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(40))==0){$gishi=int(rand(1)+9);}
			elsif(int(rand(200))==0){$gishi=int(rand(1)+9);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(20))==0){
				$gishi=int(rand(1)+9);
			}}
		}elsif($place == 16){
			if($item[0] eq "ツルハシ" and int(rand(132))==0){$gishi=int(rand(1)+10);}
			elsif($item[0] eq "山のツルハシ" and int(rand(88))==0){$gishi=int(rand(1)+10);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(44))==0){$gishi=int(rand(1)+10);}
			elsif(int(rand(220))==0){$gishi=int(rand(1)+10);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(22))==0){
				$gishi=int(rand(1)+10);
			}}
		}elsif($place == 17){
			if($item[0] eq "ツルハシ" and int(rand(132))==0){$gishi=int(rand(1)+34);}
			elsif($item[0] eq "山のツルハシ" and int(rand(88))==0){$gishi=int(rand(1)+34);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(44))==0){$gishi=int(rand(1)+34);}
			elsif(int(rand(220))==0){$gishi=int(rand(1)+34);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(22))==0){
				$gishi=int(rand(1)+34);
			}}
		}elsif($place == 30 or $place == 31){
			if($item[0] eq "ツルハシ" and int(rand(102))==0){$gishi=int(rand(1)+11);}
			elsif($item[0] eq "山のツルハシ" and int(rand(68))==0){$gishi=int(rand(1)+11);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(34))==0){$gishi=int(rand(1)+11);}
			elsif(int(rand(170))==0){$gishi=int(rand(1)+11);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){if(int(rand(17))==0){
				$gishi=int(rand(1)+11);
			}}
		}
		if($gishi>0){
			$gishi-=1;
			open(IN,"./kako/$chara[0].cgi");
			$isi_list = <IN>;
			close(IN);
			@isi = split(/<>/,$isi_list);
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			$so=0;
			foreach(@sozai_data){
				($sozainame) = split(/<>/);
				if($so == $gishi) {last;}
				$so++;
			}
			@isi[$gishi]+=1;
			$new_isi = '';
			$new_isi = join('<>',@isi);
			$new_isi .= '<>';
			open(OUT,">./kako/$chara[0].cgi");
			print OUT $new_isi;
			close(OUT);
			$comment .= <<"EOM";
			<font class=\"red\" size=5>$sozainameを手に入れたッ！！</font><br>
EOM
		}
	}

	if ($chara[24]==1400){
		if ($item[35]%100==3 or $item[36]%100==3){
			$item[0]=$bukinamae;
		}
	}

	&sentoukeka;
	
	&acs_sub;

	&hp_after;

	&levelup;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><br><B>バトル！</B></FONT>
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

#----------------------#
#  幻影の城の戦闘      #
#----------------------#
sub genei {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("一度キャラクターと闘ってください");
	}
	$chara[139]++;
	if(int(rand(300))==0){$chara[139]=251;}
	if($chara[139] > 250){
		&error("一度チャンプと闘ってください");
	}
	&time_check;

	if ($chara[27]%5 != 0) {
		&error("もう消えてしまって行けませんでした");
	}

	&item_load;

	&acs_add;

	if($chara[70]!=1){
		if ($chara[18] < $genei_low) {$monster_file=$monster0_monster;}
		elsif ($chara[18] < $genei_normal) {$monster_file=$monster1_monster;}
		elsif ($chara[18] < $genei_mid) {$monster_file=$monster2_monster;}
		elsif ($chara[18] < $genei_high) {$monster_file=$monster3_monster;}
		elsif ($chara[18] < $genei_dark) {$monster_file=$monster4_monster;}
		else {$monster_file=$monster5_monster;}
		$kazu=2;
	}else{
		if ($chara[18] < $genei_low * 10) {$monster_file=$monster0_2monster;}
		elsif ($chara[18] < $genei_normal * 10) {$monster_file=$monster1_2monster;}
		elsif ($chara[18] < $genei_mid * 10) {$monster_file=$monster2_2monster;}
		elsif ($chara[18] < $genei_high * 10) {$monster_file=$monster3_2monster;}
		elsif ($chara[18] < $genei_dark * 10) {$monster_file=$monster4_2monster;}
		elsif ($chara[18] < $genei_dark * 10) {$monster_file=$monster4_2monster;}
		elsif ($chara[18] < 1000) {$monster_file=$monster5_2monster;}
		elsif ($chara[18] < 2000) {$monster_file=$monster6_2monster;}
		elsif ($chara[18] < 3000) {$monster_file=$monster7_2monster;}
		elsif ($chara[18] < 5000) {$monster_file=$monster15_2monster;}
		elsif ($chara[18] < 10000) {$monster_file=$monster16_2monster;}
		elsif ($chara[18] < 20000) {$monster_file=$monster30_2monster;}
		else {$monster_file=$monster31_2monster;}
		$kazu=5;
	}

	$place = 20;

	open(IN,"$monster_file");
	@MONSTER = <IN>;
	close(IN);
	$r_no = @MONSTER;

	$on=0;
	&mons_read;

	$khp_flg = $chara[15];
	$mem3hp_flg = $chara[42];
	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem1hp = $smem1hp_flg;

	$i=1;
	$j=0;@battle_date=();

	foreach(1..$turn) {

		&shokika;

		$dmg2 += $item[4];

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	if ($win == 1) {
		if (int(rand(3)) == 0) {
			$otakara = int(rand(20)+1) * int($mgold);
			$chara[19] += $otakara;
			$comment .= "<b><font size=5 color=red>財宝($otakaraＧ)を発見した！！！！</font></b><br>";
		} else {
			$comment .= "<b><font size=5>辺りに財宝は見つからなかった・・・。</font></b><br>";
		}
	}

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>幻影の城</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">バトル！</FONT></CENTER>
<BR>
<BR>
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

#----------------------#
#  異世界での戦闘      #
#----------------------#
sub isekiai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if (!$chara[25]) {
		&error("一度キャラクターと闘ってください");
	}
	$chara[139]++;
	if(int(rand(100))==0){$chara[139]=251;}
	if($chara[139] > 250){
		&error("一度チャンプと闘ってください");
	}
	&time_check;

	&item_load;

	&acs_add;

	open(IN,"$isekai_monster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$kazu=5;

	&mons_read;

	$khp_flg = $chara[15];
	$mem3hp_flg = $chara[42];
	if($on and $on==$place){
		$smem1hp_flg = $msp1;
		$smem2hp_flg = $msp2;
		$smem3hp_flg = $msp3;
		$smem4hp_flg = $msp4;
		$smem1hp = $maxhp1;
		$smem2hp = $maxhp2;
		$smem3hp = $maxhp3;
		$smem4hp = $maxhp4;
	}else{
		$smem1hp_flg = int(rand($mrand1)) + $msp1;
		$smem2hp_flg = int(rand($mrand2)) + $msp2;
		$smem3hp_flg = int(rand($mrand3)) + $msp3;
		$smem4hp_flg = int(rand($mrand4)) + $msp4;
		$smem1hp = $smem1hp_flg;
		$smem2hp = $smem2hp_flg;
		$smem3hp = $smem3hp_flg;
		$smem4hp = $smem4hp_flg;
	}

	$i=1;
	$j=0;@battle_date=();
	$place = 21;
	foreach(1..$turn) {
		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&hp_after;

	&sentoukeka;

	&acs_sub;

	&levelup;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>異世界</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">バトル！</FONT></CENTER>
<BR>
<BR>
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

#----------------#
#  待ち時間表示  #
#----------------#
sub mons_error {

	foreach (keys %lock_flg) {
		if ($lock_flg{$_}) {
			if ($lockkey == 3) {
				foreach (@flock) {
					($flock_pre,$flock_file) = split(/,/);
					if ($flock_file eq $_) {
						last;
					}
				}
			}
			&unlock($_,$flock_pre);
		}
	}

	&header;

	&time_view;

	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);
	$gnnt="<option value=\"\">ささやき\n";
	foreach(@guest){
		($gtt,$gnn,$gii) = split(/<>/);
		$gnnt.="<option value=\"$gnn\">$gnnさんへ\n";
	}

       print <<"EOM";
<center><hr width=400>
<font color=red><B>まだ戦闘できません！</B></font><br>
<FORM NAME= "form1">
あと<INPUT TYPE= "text" NAME= "clock" SIZE= "3">秒待って下さい
</FORM>

<form action= "monster.cgi" method= "POST">
<input type= "hidden" name= "mode" value= "monster">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type="hidden" name="mons_file" value="$in{'mons_file'}">
<input type= "submit" class= "btn" value= "さらに闘う">
</form>
<form action= "$script" method= "POST">
<input type= "hidden" name= "mode" value= "log_in">
<input type= "hidden" name= "id" value= "$chara[0]">
<input type= "hidden" name= "mydata" value= "$in{'mydata'}">
<input type= "submit" class= "btn" value= "ステータス画面へ">
</form>
</center>
<hr width=400>
<script>
function aaa(fm){ 
fm.mes.value="";
fm.mes.focus(); 
return false; 
}
</script>

<FORM action="menu.cgi" method="POST" target="chat" onSubmit="setTimeout(function(){return aaa(this)},10)">
<table border=0 align="center" width='100%'><tr>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="name" value="$chara[4]">
<input type="hidden" name="level" value="$chara[18]">
<input type="hidden" name="chattime" value="1">
<input type="hidden" name="chan" value="$chara[96]">
<input type="hidden" name="chan2" value="$chara[180]">
常連チャンネル使用：①<INPUT TYPE="radio" NAME="tch2" VALUE="$chara[96]">ON
<INPUT TYPE="radio" NAME="tch2" VALUE="" checked>OFF
　②<INPUT TYPE="radio" NAME="tch3" VALUE="$chara[180]">ON
<INPUT TYPE="radio" NAME="tch3" VALUE="" checked>OFF
　<select name="sasayaki">$gnnt</select>
<td align="left"><input type="submit" class=btn value="発言＆更新">
<INPUT type="text" value="" name="mes" size="100" maxlength="60">　　
<INPUT type="text" value="" name="tch" size="3" maxlength="3">ch</td>
</tr>
<tr></FORM>
<td align="left" class="b2">
<iframe src="menu.cgi" width="100%" height="240" frameborder="0" name="chat" allowtransparency="true" scrolling="yes"></iframe>
</td></tr></table>
EOM

	&footer;

	exit;

}

#----------------------#
#  幻影の城の戦闘      #
#----------------------#
sub ijigen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[63]>=1){&error("入所中です！！");}

	&get_host;

	if (!$chara[25]) {
		&error("一度キャラクターと闘ってください");
	}
	$chara[139]++;
	if(int(rand(300))==0){$chara[139]=251;}
	if($chara[139] > 250){
		&error("一度チャンプと闘ってください");
	}
	&time_check;

	if ($chara[27]%2 != 0) {
		&error("もう消えてしまって行けませんでした");
	}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&acs_add;

	$place = 13;

	open(IN,"./data/bosson.ini");
	@bosson_data = <IN>;
	close(IN);
	foreach(@bosson_data){
		($name,$on) = split(/<>/);
		if($on){
			if($on==$place){
				#ボスキャラ
				open(IN,"$boss_monster");
				@MONSTER = <IN>;
				close(IN);
				$kazu=2;
				last;
			}	
		}
	}
	if($on and $on==$place){
	}else{
		if($chara[70]<1){&error("限界突破前だぞっ！不正禁止っ！");}
		else{$monster_file=$monster13_monster;}
		open(IN,"$monster_file");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		$kazu=2;
	}

	&mons_read;

	$khp_flg = $chara[15];
	$mem3hp_flg = $chara[42];
	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem1hp = $smem1hp_flg;

	$i=1;
	$j=0;@battle_date=();

	foreach(1..$turn) {

		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&sentoukeka;

	if($win != 1 and $win != 2){
		$rad=int(rand(8));
		if($rad==0 and $chara[24]!=1400){
			$chara[190]=$chara[24];
			if($item[1]>504){$chara[85]+=25000;}
			elsif($item[1]>203){$chara[85]+=5000;}
			elsif($item[1]>152){$chara[85]+=500;}
			elsif($item[1]>93){$chara[85]+=150;}
			elsif($item[1]>43){$chara[85]+=30;}
			else{$chara[85]+=0;}
			&item_lose;
			$chara[24]=0;
			$comment .= "<b><font size=5 color=red>武器が壊れてしまった！！</font></b><br>";
		}elsif($rad==1){
			$chara[190]=$chara[29];
			if($item[4]>704){$chara[85]+=25000;}
			elsif($item[4]>404){$chara[85]+=5000;}
			elsif($item[4]>199){$chara[85]+=500;}
			elsif($item[4]>103){$chara[85]+=150;}
			elsif($item[4]>52){$chara[85]+=30;}
			else{$chara[85]+=0;}
			&def_lose;
			$chara[29]=0;
			$comment .= "<b><font size=5 color=red>防具が壊れてしまった！！</font></b><br>";
		}elsif($rad==2){
			$chara[190]=$chara[31];
			&acs_lose;
			$chara[31]=0;
			$comment .= "<b><font size=5 color=red>アクセサリーが壊れてしまった！！</font></b><br>";
		}
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&acs_sub;

	&levelup;

	&hp_after;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>次元の狭間</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">バトル！</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}
	
	&mons_footer;

	if($win == 1 and int(rand(2))==0){
	$ps_gold = $chara[18]*10000;
if($chara[70]<2){
	print <<"EOM";
<font color="red" siza=3>製造会社が現れたっ。<br>
「今ならたったの$ps_gold\Gで製造品を売りますぜ。」<br>
EOM
}else{
	print <<"EOM";
<font color="red" siza=3>＜封印＞製造会社が現れたっ。<br>
「封印の旅人さんですか。$ps_gold\Gで良質の製造品を売りますぜ。」<br>
EOM
}
	print <<"EOM";
</font>
<form action="monster.cgi" method="post">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="kaisya" value="1">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=ps_buy>
<input type=submit class=btn value="行く">
</td>
</form>
EOM
	}

	&footer;

	exit;
}
sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$ps_gold = $chara[18]*10000;
	if($in{'kaisya'}!=1){&error("エラーでんがな。");}
	if($chara[19] < $ps_gold) { &error("お金が足りません"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;
if(int(rand(3))!=1){
	$ps_no=71+int(rand(12));
	if($ps_no>71){
	$ps_no=71+int(rand(12));
	if($ps_no>72){
	$ps_no=71+int(rand(12));
	if($ps_no>73){
	$ps_no=71+int(rand(12));
	if($ps_no>74){
	$ps_no=71+int(rand(12));
	if($ps_no>75){
	$ps_no=71+int(rand(12));
	if($ps_no>76){
	$ps_no=71+int(rand(12));
	if($ps_no>77){
	$ps_no=71+int(rand(12));
	if($ps_no>78){
	$ps_no=71+int(rand(12));
	if($ps_no>79){
	$ps_no=71+int(rand(12));
	if($ps_no>80){
	$ps_no=71+int(rand(12));
	if($ps_no>81){
	$ps_no=71+int(rand(12));
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	if($chara[70]>1 and $ps_no<80){$ps_no+=int(rand(4));}
	$chara[$ps_no] += 1;
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }
	if($chara[70]<2){
	$eg="$chara[4]様が製造会社で何か製造品を買ったようです。最近、狭間では警察の動きが活発です。";
	}else{
	$eg="$chara[4]様が＜封印＞製造会社で何か製造品を買ったようです。最近、狭間では警察の動きが活発です。";
	}
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
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');
}else{
	$bossyu=$chara[34]+$chara[19];
	$chara[93]=$bossyu;
	$chara[34]=0;
	$chara[19]=0;
	$chara[84]=1;
	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=1;
	$chara[65]+=1;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>違法会社だったようだ!!!!<br>
$chara[4]は逮捕され、全ての所持金を没収された！！！！悪人に一歩近づきました。気をつけてね。</B><BR>
</font>
<hr size=0>
EOM
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様が逮捕されました。没収金額：$bossyuＧ。";
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
	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]様は悪に染まりすぎ、賞金首(賞金：$syoukingaku G)となりました。";
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
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);

		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");

		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;

	exit;

}
	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>何か製造品を手に入れた。</B><BR>
</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub sihaid {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&guest_list;

	if (!$chara[25]) {
		&error("一度キャラクターと闘ってください");
	}
	$chara[139]++;
	if(int(rand(300))==0){$chara[139]=251;}
	if($chara[139] > 250){
		&error("一度チャンプと闘ってください");
	}
	if($chara[18] > 500 and int(rand(250))==0){
		&error("最近頑張ってるでしょ？");
	}

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);
	if($point > 10000){&error("ダンジョン設定のポイント超過です。支配者に伝えてください。");}
	if($chara[19] < $sihaisya[2] and $chara[0] ne $sihaisya[0]){
		&error("入場料として支払うお金が足りません。");
	}elsif($chara[0] ne $sihaisya[0]){
		$chara[19] -= $sihaisya[2];
		$sihaisya[15] += $sihaisya[2];
		$new_array = '';
		$new_array = join('<>',@sihaisya);
		$new_array =~ s/\n//;
		$new_array .= "<>\n";
		$sihai_data[0] =$new_array;

		open(OUT,">sihaisya.cgi");
		print OUT @sihai_data;
		close(OUT);
	}
	$ntime = time();
	$b_time = $m_time;
	$ztime = $ntime - $chara[27];
	$ztime = $b_time - $ztime;

	if ($ztime > 0) { &mons_error; }

	&time_check;

	&item_load;

	&acs_add;

	$place=45;

	$exp_plus += $sihaisya[12] - 1;
	$goldplus = $sihaisya[13];
	open(IN,"data/sihai.ini");
	@mon = <IN>;
	close(IN);
	$ket=0;
	foreach (@mon) {
		@mons = split(/<>/);
		if($mons[0] eq $sihaisya[3]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[4]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[5]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[6]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[7]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[8]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[9]){$MONSTER[$ket] = $_;$ket++;}
		elsif($mons[0] eq $sihaisya[10]){$MONSTER[$ket] = $_;$ket++;}
	}

	$r_no = @MONSTER;

	$kazu=$sihaisya[11]+1;

	&mons_read;

	$khp_flg = $chara[15];

	if($chara[42]){
		$mem3hp_flg = $chara[42];
	}

	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem2hp_flg = int(rand($mrand2)) + $msp2;
	$smem3hp_flg = int(rand($mrand3)) + $msp3;
	$smem4hp_flg = int(rand($mrand4)) + $msp4;
	$smem1hp = $smem1hp_flg;
	$smem2hp = $smem2hp_flg;
	$smem3hp = $smem3hp_flg;
	$smem4hp = $smem4hp_flg;

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();
	if($chara[20]<1 or $chara[20]>10){$chara[20] = 1;}
	else{$chara[20]= $chara[20]+ $chara[20]/10;}

	while($i<=$turn) {

		&shokika;

		&tyousensya;
		
		#&tyosenwaza;
		&mons_waza;

		&acs_waza;
		&mons_atowaza;
		
		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;

	}

	&sentoukeka;
	
	&acs_sub;

	&hp_after;

	&levelup;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><br><B>バトル！</B></FONT>
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