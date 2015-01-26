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

# 戦闘ライブラリの読み込み
require 'battle.pl';
# モンスター戦用ライブラリ
require 'mbattle.pl';

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

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");
	}
}

&boss;

exit;
#----------------------------#
#  レジェンドプレイスでの戦闘#
#----------------------------#
sub boss {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$test=0;
	$hit=0;
	if($chara[146]>0){$hit=1;}
	if ($test!=1 and $chara[134] == $mday) {
		if($hit==1){$hit=2;}
		else{
			if($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==8){
			}elsif($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==9){
			}else{
				&error("今日は既に挑戦しました。");
			}
		}
	}

	if ($test!=1 and $wday != 0 and $wday != 6 and $hit!=2) {
		if($hit==1){$hit=2;}
		else{
			if($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==8){
				$chara[19]-=1000000000;
			}elsif($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==9){
				$chara[19]-=1000000000;
			}else{
				&error("今日は既に挑戦しました。");
			}
		}
	}

	if ($hit==2){$chara[146]-=1;}

	if (!$in{'boss_file'}){
		&error("直リンク禁止！");
	}
	$chara[314]=time();

	&get_host;

	&item_load;

	&acs_add;

	$kazu=2;

	if($in{'boss_file'}==8 or $in{'boss_file'}==9){
		open(IN,"data/akumakai.ini");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		$akumakai = 1;
	}else{
		open(IN,"data/akuma.ini");
		@MONSTER = <IN>;
		close(IN);
		$r_no = $in{'boss_file'} - 1;
		$aku=1;
	}

	$place = 98;

	&mons_read;

	$khp_flg = $chara[15];

	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	if($in{'boss_file'}!=8 and $in{'boss_file'}!=9){
		$smem1hp = $smem1hp_flg * ($chara[135]+1);
	}elsif($in{'boss_file'}==9){
		$smem1hp = $smem1hp_flg + int(rand($smem1hp_flg));
	}else{
		$smem1hp = $smem1hp_flg;
	}
	$smem1hp_flg = $smem1hp;
	if(!$smem1hp or $smem1hp<1){&error("モンスターが見つかりません。再挑戦してください。");}

	$mem3hp_flg = $chara[42];

	$i=1;
	$j=0;@battle_date=();

	@gakusyuu=();
	open(OUT,">akuma/$chara[0].cgi");
	print OUT @gakusyuu;
	close(OUT);

	while($i<=$chara[135]+1) {

		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;
		&mons_atowaza;

		open(IN,"akuma/$chara[0].cgi");
		@gakusyuu = <IN>;
		close(IN);
		$ghit=0;
		foreach(@gakusyuu){
			if($ghissatu==$_ and $ghissatu<999){
				if($in{'boss_file'}==8 or $in{'boss_file'}==9){
		if($chara[24]==1400 and $item[37]%100==4 and int($item[37]/100+1)*10>int(rand(100))){
				$ghit=1;
				last;
		}elsif($chara[24]==1400 and $item[38]%100==4 and int($item[38]/100+1)*10>int(rand(100))){
				$ghit=1;
				last;
		}else{
				$scom1 .= "<font class=\"yellow\" size=5>マ\た\ソ\の\ワ\ざ\カ\…\ば\カ\め\！\！</font><br>";
				$dmg1=int($dmg1*int(rand(100)+1)/100);
				$ssake1 = $ssake1*(int(rand(100)+1));
				$ghit=1;
				last;
		}
				}
			}
		}
		if($ghit!=1){
			push(@gakusyuu,"$ghissatu\n");
			open(OUT,">akuma/$chara[0].cgi");
			print OUT @gakusyuu;
			close(OUT);
		}
		if($in{'boss_file'}==8 or $in{'boss_file'}==9){
			$dmg1=int($dmg1/10000);
			$dmg4=int($dmg4/8500);
			$mem1hit_ritu = int($mem1hit_ritu/80);
			$sake1=int($sake1/10000);
		}

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	$kmori_w = $chara[28];

	if($chara[70]>0 and $win==1){
		$gishi=0;
		if($in{'boss_file'}==8 and $chara[24]==1400){
			if(int(rand(100))<40){
				$gishi=int(rand(4)+30);
			}
		}elsif($in{'boss_file'}==9 and $chara[24]==1400){
			if(int(rand(100))<60){
				$gishi=int(rand(4)+30);
			}
		}elsif($in{'boss_file'}>4){
			if($item[0] eq "ツルハシ" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "山のツルハシ" and int(rand(2))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(1))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>3){
			if($item[0] eq "ツルハシ" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "山のツルハシ" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(2))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>2){
			if($item[0] eq "ツルハシ" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "山のツルハシ" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>1){
			if($item[0] eq "ツルハシ" and int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "山のツルハシ" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(7))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}else{
			if($item[0] eq "ツルハシ" and int(rand(7))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "山のツルハシ" and int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "黄金のツルハシ" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(8))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
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
	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest4_item = split(/<>/,$questdata);
	$hit=0;
	if($quest4_item[1]>0 and $ssmname1 eq "スノム") {$hit=29;}
	if($quest4_item[2]>0 and $ssmname1 eq "スノム") {$hit=30;}
	if($quest4_item[3]>0 and $ssmname1 eq "スノミ") {$hit=31;}
	if($quest4_item[4]>0 and $ssmname1 eq "スノミ") {$hit=32;}
	if($hit>0){
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
			if($so == $hit) {last;}
			$so++;
		}
		@isi[$hit]+=1;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$hit=$hit-28;
		$quest4_item[$hit]=0;
		$new_data = '';
		$new_data = join('<>',@quest4_item);
		$new_data .= '<>';
		open(OUT,">./quest/$chara[0].cgi");
		print OUT $new_data;
		close(OUT);
		$comment .= "<b><font size=4 color=red>";
		$comment .= "「$ssmname1」を倒しクエストをクリアした！<br>";
		$comment .= "報酬$sozainameを入手した！！<br>";
	}
	}

	&akuma_sentoukeka;

	&acs_sub;

	&hp_after;

	&levelup;

	$chara[134]=$mday;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>悪魔の館</B></FONT><br>

<B><CENTER><FONT SIZE= "6">バトル！</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&bossfooter;

	&footer;

	exit;
}

#--------------------------------#
#  レジェンドプレイス用フッター  #
#--------------------------------#
sub bossfooter {
	if ($win<3) { print "$comment$chara[4]は、$mexの経験値を手に入れた。<b>$gold</b>G手に入れた。<br>\n"; }
	else { print "$comment$chara[4]は、$mexの経験値を手に入れた。お金が半分になった・・・(涙)<br>\n"; }

	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
}