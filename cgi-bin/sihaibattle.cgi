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
sub sihai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[143]==$mday){
		&error("今日はもう戦えません。");
	}

	&item_load;

	&acs_add;
	$place=51;

	#相手のメンバー決定
	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}
	$lock_file = "$lockfolder/$sihaisya[0].lock";
	&lock($lock_file,'DR');
	open(IN,"./charalog/$sihaisya[0].cgi");
	$smember1_data = <IN>;
	close(IN);
	$lock_file = "$lockfolder/$sihaisya[0].lock";
	&unlock($lock_file,'DR');
	@smem1 = split(/<>/,$smember1_data);
	open(IN,"./item/$sihaisya[0].cgi");
	$smem1item_log = <IN>;
	close(IN);
	@smem1item = split(/<>/,$smem1item_log);

	$khp_flg = $chara[15];
	if($chara[42]){
		$mem3hp_flg = $chara[42];
	}
	$smem1hp_flg = $smem1[15];
	if($smem1[42]){
		$smem3hp_flg = $smem1[42];
	}

	$i=1;
	$j=0;

	@battle_date=();

	$turn=$turn3;

	while($i<=$turn) {
		
		&shokika;

		&tyousensya;

		&acs_waza;

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
		if($item[20]){$bukilv="+ $item[20]";}else{$bukilv="";}
		if($item[20]==10){$g="red";}else{$g="";}
		$com1 = "$chara[4]は、<font color=\"$g\">$item[0] $bukilv</font>で攻撃！！";
		if( ($chara[7] + $item[1]) > ($chara[8] + $item[1]) ){
			$dmg1 += $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10+1);
		}else{
			$dmg1 += $chara[8] * 4 + $item[1] * 4 * int($chara[8]/10+1);
		}
	}
	if($smem1hp_flg > 0){
		if($smem1item[20]){$bukilv="+ $smem1item[20]";}else{$bukilv="";}
		if($smem1item[20]==10){$g="red";}else{$g="";}
		$scom1 = "$smem1[4]は、<font color=\"$g\">$smem1item[0] $bukilv</font>で攻撃！！";
		if( ($smem1[7] + $smem1item[1]) > ($smem1[8] + $smem1item[1]) ){
			$sdmg1 += $smem1[7] * 4 + $smem1item[1] * 4 * int($smem1[7]/10+1);
		}else{
			$sdmg1 += $smem1[8] * 4 + $smem1item[1] * 4 * int($smem1[8]/10+1);
		}
	}
	if($chara[39]){
		# ペットダメージ計算
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
		$com4 = "$penameの攻撃！";
	
		$dmg4 = $chara[44];
	}
	if($smem1[39]){
		# ペットダメージ計算
	if($smem1[138] eq ""){$spename=$smem1[39];}else{$spename=$smem1[138];}
		$scom3 = "$spenameの攻撃！";
	
		$sdmg3 = $smem1[44];
	}
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
	$dmg4 = 0;
	$sdmg1 = 0;
	$sdmg3 = 0;
	$clit1 = "";
	$clit4 = "";
	$sclit1 = "";
	$sclit3 = "";
	$mem1hit_ritu=0;
	$mem4hit_ritu=50;
	$smem1hit_ritu=0;
	$smem3hit_ritu=50;
	$sake1 = 0;
	$sake4 = 0;
	$ssake1 = 0;
	$ssake3 = 0;
	$com1 = "";
	$com4 = "";
	$scom1 = "";
	$scom3 = "";
	$kawasi1 = "";
	$kawasi3 = "";
	$skawasi1 = "";
	$skawasi4 = "";
	$hpplus1 = 0;
	$hpplus4 = 0;
	$shpplus1 = 0;
	$shpplus3 = 0;
	$kaihuku1 = "";
	$kaihuku4 = "";
	$skaihuku1 = "";
	$skaihuku3 = "";
	$taisyo1=int(rand(2));
	$taisyo2=int(rand(2));
	$staisyo1=int(rand(2));
	$staisyo2=int(rand(2));
	if($smem1hp_flg<=0){$taisyo1=1;$taisyo2=1;}
	if($smem3hp_flg<=0){$taisyo1=0;$taisyo2=0;}
	if($khp_flg<=0){$staisyo1=1;$staisyo2=1;}
	if($mem3hp_flg<=0){$staisyo1=0;$staisyo2=0;}
}

#------------#
#　HPの計算　#
#------------#
sub hp_sum {

	if($khp_flg<1){$dmg1 = 0;}
	if($mem3hp_flg<1){$dmg4 = 0;}

	if($smem1hp_flg<1){$sdmg1 = 0;}
	if($smem3hp_flg<1){$sdmg3 = 0;}

	if($staisyo1==0){
		$khp_flg -= $sdmg1;
	}elsif($staisyo1==1){
		$mem3hp_flg -= $sdmg1;
	}
	if($staisyo2==0){
		$khp_flg -= $sdmg3;
	}elsif($staisyo1==1){
		$mem3hp_flg -= $sdmg3;
	}
	if($taisyo1==0){
		$smem1hp_flg -= $dmg1;
	}elsif($taisyo1==1){
		$smem3hp_flg -= $dmg4;
	}
	if($taisyo2==0){
		$smem1hp_flg -= $dmg1;
	}elsif($taisyo2==1){
		$smem3hp_flg -= $dmg4;
	}

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mem3hp_flg > $chara[43]) {
		$mem3hp_flg = $chara[43];
	}
	if ($smem1hp_flg > $smem1[16]){
		$smem1hp_flg = $smem1[16];
	}
	if ($smem3hp_flg > $smem1[43]) {
		$smem3hp_flg = $smem1[43];
	}
}

#------------#
#　勝敗条件　#
#------------#
sub winlose {

	if ($smem1hp_flg<=0 and $smem3hp_flg<=0){ 
		$win = 1; last; #勝ち
	}
	elsif ($khp_flg<1 and $mem3hp_flg<1) {
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

	$smem1ci_plus = $smem1item[2] + $smem1item[16];
	$smem1cd_plus = $smem1item[5] + $smem1item[17];

	# 命中率
	$mem1hit_ritu += int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $ci_plus;

	$smem1hit_ritu += int($smem1[9] / 3 + $smem1[11] / 10 + $smem1item[10] / 3)+ 40 + $smem1ci_plus;

	# 回避率
	$sake1	+= int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $cd_plus - $syamato1;

	$ssake1	+= int($smem1[9] / 10 + $smem1[11] / 20 + $smem1item[10]/10) + $smem1cd_plus - $yamato1;

	if ($sake1 > 90){$sake1 = 90;}

	if ($ssake1 > 90){$ssake1 = 90;}

	if ($staisyo1 ==0){
		if ($sdmg1 < $item[4]*(2+int($chara[10]/10+1))){ $sdmg1=0; }
		else{ $sdmg1 = $sdmg1 - $item[4] * (2+int($chara[10]/10+1)); }
		if (int($sake1 - ($smem1hit_ritu / 3)) > int(rand(100))) {
			$sdmg1 = 0;
			$kawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]は身をかわした！</FONT>";
		}
	}elsif($staisyo1 == 1 and int(rand(100))<20){
		$sdmg1=0;
		$kawasi4= "<FONT SIZE=4 COLOR=\"$red\">$penameは身をかわした！</FONT>";
	}

	if ($taisyo1 ==0){
		if ($dmg1 < $smem1item[4]*(2+int($smem1[10]/10+1))){ $dmg1=0; }
		else{ $dmg1 = $dmg1 - $smem1item[4] * (2+int($smem1[10]/10+1)); }
		if (int($ssake1 - ($mem1hit_ritu / 3)) > int(rand(100))) {
			$dmg1 = 0;
			$skawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$smem1[4]は身をかわした！</FONT>";
		}
	}elsif($taisyo1 == 1 and int(rand(100))<20){
		$dmg1=0;
		$skawasi3= "<FONT SIZE=4 COLOR=\"$red\">$spenameは身をかわした！</FONT>";
	}
	if ($staisyo2 ==0){
		if ($sdmg3 < $item[4]*(2+int($chara[10]/10+1))){ $sdmg3=0; }
		else{ $sdmg3 = $sdmg3 - $item[4] * (2+int($chara[10]/10+1)); }
		if (int(rand(100))<20) {
			$sdmg3 = 0;
			$kawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$chara[4]は身をかわした！</FONT>";
		}
	}elsif($staisyo2 == 1 and int(rand(100))<20){
		$sdmg3=0;
		$kawasi3= "<FONT SIZE=4 COLOR=\"$red\">$penameは身をかわした！</FONT>";
	}

	if ($taisyo2 ==0){
		if ($dmg4 < $smem1item[4]*(2+int($smem1[10]/10+1))){ $dmg4=0; }
		else{ $dmg4 = $dmg4 - $smem1item[4] * (2+int($smem1[10]/10+1)); }
		if (int(rand(100))<20) {
			$dmg4 = 0;
			$skawasi1 = "<FONT SIZE=4 COLOR=\"$red\">$smem1[4]は身をかわした！</FONT>";
		}
	}elsif($taisyo2 == 1 and int(rand(100))<20){
		$dmg4=0;
		$skawasi4= "<FONT SIZE=4 COLOR=\"$red\">$spenameは身をかわした！</FONT>";
	}
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
		if($mem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_pet/$egg_img[$chara[45]]">
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
		if($smem3hp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_pet/$egg_img[$smem1[45]]">
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
	if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
	if($mem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$pename			</TD>
		<TD class= "b2">	$mem3hp_flg\/$chara[43]	</TD>
		<TD class= "b2">	ペット			</TD>
		<TD class= "b2">	$chara[46]		</TD></TR>
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
	if($smem1[138] eq ""){$spename=$smem1[39];}else{$spename=$smem1[138];}
	if($smem3hp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	$spename		</TD>
		<TD class= "b2">	$smem3hp_flg\/$smem1[43]</TD>
		<TD class= "b2">	ペット			</TD>
		<TD class= "b2">	$smem1[46]		</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]達の攻撃！！</td></tr>
EOM
	if($taisyo1==0){$mname1=$smem1[4];}
	if($taisyo1==1){$mname1=$spename;}
	if($taisyo2==0){$mname4=$smem1[4];}
	if($taisyo2==1){$mname4=$spename;}
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com1 $clit1 $skawasi1 $mname1 に <font class= "yellow">$dmg1</font> のダメージを与えた。<font class= "yellow">$kaihuku1</font><br>　</td></tr>
EOM
	}
	if($mem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com4 $skawasi4 $mname4 に <font class= "yellow">$dmg4</font> のダメージを与えた。<font class= "yellow">$kaihuku4</font><br>　</td></tr>
EOM
	}
	if($staisyo1==0){$smname1=$chara[4];}
	if($staisyo1==1){$smname1=$pename;}
	if($staisyo2==0){$smname3=$chara[4];}
	if($staisyo2==1){$smname3=$pename;}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">$smem1[4]達の攻撃！！</td></tr>
EOM
	if($smem1hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom1 $kawasi1 $smname1に <font class= "yellow">$sdmg1</font> のダメージを与えた。<font class= "yellow">$skaihuku1</font><br>　</td></tr>
EOM
	}
	if($smem3hp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$scom3 $kawasi3 $smname3 に <font class= "yellow">$sdmg3</font> のダメージを与えた。<font class= "yellow">$skaihuku3</font><br>　</td></tr>
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

	open(IN,"sihaisya.cgi");
	@sihai_data = <IN>;
	close(IN);
	foreach (@sihai_data) {
		@sihaisya = split(/<>/);
		if($sihaisya[0]){last;}
	}

	if ($win==1) {
		$sihaisya[0]=$chara[0];
		$sihaisya[1]=$chara[4];

		$new_array = '';
		$new_array = join('<>',@sihaisya);
		$new_array =~ s/\n//;
		$new_array .= "<>\n";
		$sihai_data[0] =$new_array;

		open(OUT,">sihaisya.cgi");
		print OUT @sihai_data;
		close(OUT);

 		$comment .= "<b><font size=5>$chara[4]は、戦闘に勝利し支配者になった！</font></b><br>";

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }

		$eg="$chara[4]様が新たな支配者となりました！";

		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	} elsif ($win==3) {
		$comment .= "<b><font size=5>$chara[4]は、逃げ出した・・・♪</font></b><br>";
	} else {
		$comment .= "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
		$chara[143]=$mday;
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }

		$eg="支配者が挑戦者$chara[4]様に打ち勝ちました。";

		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}

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
		print "$comment <br>\n";
	} elsif($win==2){
		print "$comment<br>\n";
	} elsif($win==3){
		print "$comment \n";
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
