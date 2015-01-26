#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# アイテムライブラリの読み込み
require 'item.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="seigi.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}

if($mode) { &$mode; }

&sakaba;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub sakaba {

	&chara_load;

	&chara_check;

	&item_load;

	&header;
	if($chara[315]==1){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラルのペット</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「天界での修行は順調か？<br>
実はな、俺も最近修行してるのさ。天界でな…。<br>
」
</FONT>
EOM
	}elsif($chara[304]==4){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラルのペット</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「待ってたぜ$chara[4]！！<br>
アンクドラルは重症だ。襲われた時に恐ろしい暗黒魔法をかけられていて、回復もできん。<br>
アンクドラルに襲い掛かった剣士には会ったことがある。悪魔界・王子だ。<br>
あの時・・・<br>
時魔法によって、アンクドラルは王子と共に、突然ここに現れた。<br>
まぁその後は<font size=5><b>俺が</b></font>王子を撃退したんだがな。<br>
ここがどこだか知ってるだろ。この地上では悪魔界と最も遠い場所にあるのさ。<br>
いきなりのフィールドの激変についてこれなかった王子ｖｓ<font size=5><b>元・魔王</b></font>なら、俺の勝ちだ。<br>
$chara[4]との二人がかりなら、王子を倒すことすらできたかもしれない。<br>
・・・とは言っても、二度同じ魔法にかかる悪魔ではない。ヤツは二度とココには来ないだろう。<br>
そこでだ、これから$chara[4]は、天界に行き、奴等を倒す力を得なければならない。<br>
きっと天界では、悪魔界で王子、あるいは悪魔界王をも倒す術を手に入れられるはずだ。<br>
３つのノートがあれば、天界への鍵を作るのは容易い。
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kagi>
<input type=submit class=btn value="天界への鍵を作る">
</form>
」
</FONT>
EOM
	}elsif($chara[304]==5){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラルのペット</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「待ってたぜ$chara[4]！！<br>
アンクドラルに不意打ちを仕掛けたらしいじゃねぇか！ついに俺と一緒に世界征服ってことか？<br>
だが残念だったな！アンクドラルは既に全快しているぜ。<br>
あの時・・・<br>
時魔法によってここへ飛んできたアンクドラルは、すぐさまヒールガでＨＰを全快させたのさ。<br>
何も問題は無いさ。<br>
アンクドラルは全く怒っていないようだったしな。<br>
むしろアンクドラルは、$chara[4]に止められて良かったと考えているようだった。<br>
アンクドラルは…悪魔達の力量を、十二分に評価していたつもりでも、まだ甘く見ていたと言っていた。<br>
今は天界へ行き、更なる修行をしている。<br>
これから$chara[4]も天界へ行き、悪魔達を倒す力を得なければならない。<br>
天界での修行は、悪魔界の最深部に居るとされる、悪魔界王を倒す為に必須だろう。<br>
３つのノートがあれば、天界への鍵を作るのは容易い。
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kagi>
<input type=submit class=btn value="天界への鍵を作る">
</form>
」
</FONT>
EOM
	}elsif($chara[128]==5){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラルのペット</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「まぁ、がんばれよ。」
</FONT>
EOM
	}elsif($chara[128]==4){
		if($item[1]>=9999 or $item[2]>=9999){
		if($chara[24]==1400){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラルのペット</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「$chara[4]か、先日は世話になったな。<br>
アンクドラルから伝言を頼まれている。その言葉を伝えよう。<br>
<font color="yellow">
本当は直接伝えたかったのだが、時が来てしまった。おそらく私は今、悪魔界に居ることだろう。<br>
$chara[4]、君の武器が新たな段階に達しようとしていることを聞いた。それについて伝えておかねばならない。<br>
無の空間で入手した武器、その真骨頂はマテリアを纏うことができるということにある。<br>
マテリアとは、悪魔達の魂のことである。悪魔の魂を宿した武器は、恐ろしい威力を持つことになる。<br>
今、その武器はマテリアを纏う準備が半分完成している状態だ。<br>
もう半分…必要なのは、４つの型を選び、武器を進化させることだ。<br>
４つの型については情報屋で聞いたことだろう。先日、君がなった職業に対応した型に進化することになる。<br>
ここで新たに名前をつけなおし、進化させるのだ。もしも職業が変えたくなった場合、ここでチェンジすることが出来る。<br>
ただし、２つ注意が必要だ。まず、前の職業で習得したアビリティは失ってしまうぞ。<br>
それから、前回よりも武器の波動が強い状態のため、職業を選ぶことは出来ない。４つのうち、ランダムになってしまうぞ。<br>
一度武器を進化させたら、職業チェンジは困難になるだろう。もしかしたら今がラストチャンスかもしれない。<br>
型を変えるのは…特殊なマテリアを入手することができれば出来るかもしれないが…難しいと言っておこう。<br>
武器を進化させた後は、その剣で悪魔を倒し、マテリアを入手することが出来るようになる。<br>
いや、正確にはマテリアの元となる元素、だな。<br>
私もマテリア精製技術の資格は持っているのだが…、まぁ、便利屋で精製して貰うと良いだろう。<br>
マテリアには対応する型がある。まぁその辺のことは、便利屋で聞いてくれ。<br>
</font>」
</FONT>
<hr size=0>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=change>
<input type=submit class=btn value="職業チェンジ！！">
</form>
<br>武器に新たな名前をつけることができます。<br>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=buki2>
<input type="text" name="bname" value="" size=40>
<input type=submit class=btn value="武器を進化させる">
</form>
EOM
		}
		}else{
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「たくましくなったな。後は自分で武器を成長させていくのだ。」
</FONT>
<hr size=0>
EOM
		}
	}elsif($chara[128]==3){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「$chara[4]か・・・。私の修行は順調だが、武器の調子はどうだ？<br>
EOM
if($chara[24]==1400){
	if($item[1]<1000 and $item[2]<1000){
	print <<"EOM";
・・・ダメだな。まだ、悪魔の館の相手には歯が立たないのか？<br>
あそこの相手で苦戦しているようでは悪魔界への進入など不\可\能\だぞ。<br>
よし、私も暇ではないが…１日１度までなら、君の武器の修行を手伝おうではないか。」<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=syugyou>
<input type=hidden name=item value=1>
<input type=submit class=btn value="攻撃力を鍛えてもらう">
</form>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=syugyou>
<input type=hidden name=item value=2>
<input type=submit class=btn value="命中力を鍛えてもらう">
</form>
EOM
	}elsif($item[1]>3000 and $item[2]>3000){
	print <<"EOM";
・・・ほう、とても良い武器になってきているではないか。<br>
その武器をより使いこなしたければ新しいジョブになると良いだろう。<br>
どうだ、梵天になる気はあるか？」<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=54>
<input type=submit class=btn value="梵天になる">
</form>
EOM
	}elsif($item[1]>1000 and $item[2]>1000){
	print <<"EOM";
・・・ほう、性能が中々上がってきているようだな。<br>
その武器をより使いこなしたければ新しいジョブになると良いだろう。<br>
どうだ、阿修羅になる気はあるか？」<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=53>
<input type=submit class=btn value="阿修羅">
</form>
EOM
	}elsif($item[1]>1000 and $item[2]<1000){
	print <<"EOM";
・・・ほう、攻撃力が中々上がってきているようだな。<br>
その武器をより使いこなしたければ新しいジョブになると良いだろう。<br>
どうだ、大黒天になる気はあるか？」<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=51>
<input type=submit class=btn value="大黒天になる">
</form>
EOM
	}elsif($item[1]<1000 and $item[2]>1000){
	print <<"EOM";
・・・ほう、命中力が中々上がってきているようだな。<br>
その武器をより使いこなしたければ新しいジョブになると良いだろう。<br>
どうだ、龍王になる気はあるか？」<br>
<form action="seigi.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=52>
<input type=submit class=btn value="龍王になる">
</form>
EOM
	}
}else{
	print <<"EOM";
ここに持ってきたら、見てやるぞ。」
EOM
}
	print <<"EOM";
</FONT>
<hr size=0>
EOM
	}elsif($chara[128]==2){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「やはり、奴は強敵だったな。おそらく、今の私一人では勝てなかっただろう。<br>
私もまだまだ修行が足りないな…。<br>
これから、私は改めて修行をしなおし、悪魔界に突入するつもりだ。<br>
$chara[4]も、きっとそのつもりだろう。<br>
・・・、この武器を持っていけ。悪魔界で戦うのには、現存する人間界の装備では不\十\分だ。<br>
いかに正義の剣といえども、それは同じこと。<br>
この武器は、『無の空間』という場所で入手した、この世界に誕生したばかりの武器だ。<br>
名前もまだないし、攻撃力も１だが、その可\能\性は無限だ。<br>
悪魔の館でマテリアを入手し、自分専用の最強の武器を作りあげると良いだろう。」
</FONT>
<hr size=0>
<br>武器に名前をつけてください。<br>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=buki>
<input type="text" name="bname" value="" size=40>
<input type=submit class=btn value="受け取る">
</form>
EOM
	}elsif($chara[128]==1 or $chara[0] eq "jupiter"){
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>正義の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
「ようこそ正義の館へ。<br>
第３代大魔王との決戦の舞台へ案内いたしましょう。」
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sandai>
<input type=submit class=btn value="よろしく。">
</form>
EOM
	}else{
	print <<"EOM";
<h1>正義の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>正義の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
「ようこそ正義の館へ。<br>
あなたが、第３代大魔王に勝てるかどうかテストいたしましょう。<br>
私に勝つことが出来たら、第３代大魔王との決戦の舞台へ案内いたしましょう。」
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=sbattle>
<input type=submit class=btn value="挑戦する">
</form>
EOM
	}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub sbattle {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&item_load;

	$khp_flg = $chara[15];

	$mhp_flg = 30000000;

	$i=1;
	$j=0;
	@battle_date=();

	while($i<=$turn) {

		&shokika;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;

	}

	&sentoukeka;
	
	&hp_after;

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
sub shokika {
	if($item[0] eq "正義の剣"){$dmg = int(rand($chara[18]*3000));}
	else{$dmg = 1;}
	if($item[3] eq "正義のマント"){$mdmg = int(rand($chara[16]/4));}
	else{$mdmg=int(rand($chara[16]*2));}
	$com = "";
	$mcom = "正義の使者が襲いかかった！！";
	if($item[0] ne "正義の剣"){
		$mcom.= "<br><font size=\"5\" color=\"yellow\">正義の剣以外で私を傷つけることなどできないよ</font>"
	}
	if($item[3] ne "正義のマント"){
		$mcom.= "<br><font size=\"5\" color=\"yellow\">正義のマントもなしに私の攻撃は防げないよ</font><br>"
	}
}
sub hp_sum {

	if($khp_flg<1){$dmg = 0;}
	if($mhp_flg<1){$mdmg = 0;}

	$khp_flg = $khp_flg - $mdmg;
	$mhp_flg = $mhp_flg - $dmg;

	if ($khp_flg > $chara[16]) {
		$khp_flg = $chara[16];
	}
	if ($mhp_flg > 30000000){
		$mhp_flg = 30000000;
	}
}
sub winlose {
	if ($mhp_flg<=0){ 
		$win = 1; last; #勝ち
	}elsif ($khp_flg<1) {
		$win = 4; last; #負け
	}else{ $win = 2; } #引き分け
}
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
		$battle_date[$j] .= <<"EOM";
		</TD><TD></TD><TD></TD><TD>
EOM
		if($mhp_flg>0){
			$battle_date[$j] .= <<"EOM";
			<IMG SRC="$img_path_t/$chara_img_t[116]">
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
	$battle_date[$j] .= <<"EOM";
	</TABLE></TD><TD></TD><TD><FONT SIZE=5 COLOR= "#9999DD">VS</FONT></TD>
	<TD><TABLE><TR>
	<TD CLASS= "b1" id= "td2">	なまえ	</TD>
	<TD CLASS= "b1" id= "td2">	HP	</TD>
	<TD CLASS= "b1" id= "td2">	職業	</TD>
	<TD CLASS= "b1" id= "td2">	LV	</TD></TR>
EOM
	if($mhp_flg>0){
		$battle_date[$j] .= <<"EOM";
		<TR><TD class= "b2">	正義の使者		</TD>
		<TD class= "b2">	$mhp_flg\/30000000	</TD>
		<TD class= "b2">	モンスター		</TD>
		<TD class= "b2">	120			</TD></TR>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	</TABLE></TD></TR>
	<table align="center">
	<tr><td class="b1" id="td2">$chara[4]の攻撃！！</td></tr>
EOM
	if($khp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$com 正義の使者 に <font class= "yellow">$dmg</font> のダメージを与えた。<br>　</td></tr>
EOM
	}
		$battle_date[$j] .= <<"EOM";
	<tr><td class="b1" id="td2">正義の使者の攻撃！！</td></tr>
EOM
	if($mhp_flg > 0){
		$battle_date[$j] .= <<"EOM";
		<tr><td class="b2"><br>$mcom $chara[4] に <font class= "yellow">$mdmg</font> のダメージを与えた。<br>　</td></tr>
EOM
	}
	$battle_date[$j] .= "</table>";
}
sub sentoukeka{
	if ($win==1) {
		$chara[22] += 1;
 		$comment .= "<b><font size=5>$chara[4]は、戦闘に勝利した！！</font></b><br>";
	} elsif ($win==2) {
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]は、逃げ出した・・・♪</font></b><br>";
	} else {
		$chara[20] = 0;
		$comment .= "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
	}
	if($chara[36]==1){
		if(!$lvup or $chara[38]>3000){
			if($chara[19]>=int($yado_dai*$chara[18])){
				$chara[15] = $chara[16];
				$chara[42] = $chara[43];
				$chara[19] -=int($yado_dai*$chara[18]);
				print "<b><font size=2>$chara[4]は、宿屋に行った。</font></b><br>";
			}else{
	print "<b><font size=2>$chara[4]は、宿屋に行こうとしたがお金が足りなかった。</font></b><br>";
			}
		}
	}
	&chara_regist;
}
sub hp_after{
	$chara[15] = $khp_flg;
	if ($chara[15] > $chara[16]) { $chara[15] = $chara[16]; }
	if ($chara[15] <= 0) { $chara[15] = 1; }
}

#----------------------#
# 戦闘後のフッター処理 #
#----------------------#
sub mons_footer{
	if($win==3){
		print "$comment (涙)<br>\n";
	} elsif($win==1){
		print "$comment <br>\n";
	print <<"EOM";
<B>正義の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
「やりますね！！<br>
あなたなら、第３代大魔王に勝てる可\能\性があります。<br>
付いてきてください。」
</FONT>
<hr size=0>
<br>
<form action="./seigi.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=win>
<input type=submit class=btn value="ついていく">
</form>
EOM
	} elsif($win==2){
		print "$comment <br>\n";
	} else {
		print "$comment (涙)<br>\n";
	}

	print <<"EOM";
<form action="$script">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
}
sub win{

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_acs_num >= $acs_max) {
		&error("アクセサリー倉庫がいっぱいです！$back_form");
	}
	&header;
	if($chara[128]!=1){
		$chara[128]=1;
		$i_no="0047";
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $i_no){last;}
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	print <<"EOM";
<B>正義の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br>
「おや？あなた、<b>正義のアクセサリー</b>をお持ちでないんですね。これをあげましょう。<br>
装備したら、もう一度来てください。」
</FONT>
<hr size=0>
<br>
EOM
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');

	&shopfooter;

	&footer;

	exit;
}

sub sandai {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>決戦の舞台</h1>
<hr size=0>
<FONT SIZE=3>
<B>第３代大魔王</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[54]"><br>
「むっ。貴様は！！生きていたのか！アンクドラル！<br>
何だそのふざけた格好は…。どうやってここへ来た！？」<br><br>
<B>正義の使者　改め　アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[116]"><br><br>
「もはや初代大魔王、第２代大魔王ですら、人間界の強者達の間では一日一匹の雑魚扱い…。<br>
ここまでの道のりに強い者など一匹も居なかったわ。<br>
しかし、貴様だけは油断ならん。悪魔界と何やら契約を結んでいたそうだからな。<br>
そこで…、今回は助っ人を連れてきた。「人間界の強者」だ。<br>
$chara[4]、まだ自己紹介をしていなかったな。<br>
私はアンクドラル。この姿は、正義の館での仮の姿…。<br>
今こそ、真の力を解放し、奴と戦おう。<br>
協力してくれ！」
</FONT>
<hr size=0>
<br>
<form action="./maoubattle.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=maou>
<input type=submit class=btn value="戦う">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

sub buki{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($in{'bname'} eq ""){
		&error("武器に名前をつけてください。$back_form");
	}
	if (length($in{'bname'}) > 20) {
		&error("武器の名前が長すぎます。$back_form");
	}

	open(IN,"$item_file");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($i_no == 1400) { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	$souko_item_num = @souko_item;

	if ($souko_item_num >= $item_max) {
		&error("武器倉庫がいっぱいです！");
	}

	push(@souko_item,"$i_no<>$in{'bname'}<>$i_dmg<>$i_gold<>$ihit<>\n");

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	$chara[128]=3;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>自分専用の武器『$in{'bname'}』を受け取った！</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub change {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("現在の職業をマスターしていません。");}
	if($chara[128]==4){
		$lock_file = "$lockfolder/syoku$in{'id'}.lock";
		&lock($lock_file,'SK');
		&syoku_load;
		$syoku_master[51] = 0;
		$syoku_master[52] = 0;
		$syoku_master[53] = 0;
		$syoku_master[54] = 0;
		&syoku_regist;
		&unlock($lock_file,'SK');
		if($chara[51]==71 or $chara[51]==72 or $chara[51]==73 or $chara[51]==74){$chara[51]=0;$chara[13]+=650;}
		if($chara[52]==71 or $chara[52]==72 or $chara[52]==73 or $chara[52]==74){$chara[52]=0;$chara[13]+=650;}
		if($chara[53]==71 or $chara[53]==72 or $chara[53]==73 or $chara[53]==74){$chara[53]=0;$chara[13]+=650;}
		if($chara[54]==71 or $chara[54]==72 or $chara[54]==73 or $chara[54]==74){$chara[54]=0;$chara[13]+=650;}
		$chara[14]=51+int(rand(4));
		$comment="アンクドラルのペット";
	}else{
		$chara[14]=$in{'item'};
		$comment="アンクドラル";
		$chara[128]=4;
	}

	$chara[33]=1;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が新しい型職になりました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$comment</B><BR>
「うむ…。無事に新たな職になれたようだな。これからもがんばりなさい。
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub syugyou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[147]==$mday){&error("今日はもう修行しましたよ。");}
	else{$chara[147] = $mday;}

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($in{'item'} == 1) {
		$kougeki=int(rand(100));
		$item[1]+=$kougeki;
		$st="武器の攻撃力が$kougekiポイント上昇しました。";
	}elsif($in{'item'} == 2){
		$hit=int(rand(100));
		$item[2]+=$hit;
		$st="武器の命中力が$hitポイント上昇しました。";
	}else{
		&error("エラー。$back_form");
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>無事、修行が完了し、$st</B><BR>
</font>
<br>
<form action="seigi.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub buki2{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	&syoku_load;

	if($syoku_master[51]==100){$msyoku=1;}
	elsif($syoku_master[52]==100){$msyoku=2;}
	elsif($syoku_master[53]==100){$msyoku=3;}
	elsif($syoku_master[54]==100){$msyoku=4;}
	else{&error("必要職業をマスターしていない状況です。$back_form");}

	if ($in{'bname'} eq ""){
		&error("武器に名前をつけてください。$back_form");
	}
	if (length($in{'bname'}) > 20) {
		&error("武器の名前が長すぎます。$back_form");
	}

	$item[0] = $in{'bname'};
	$item[28] = $msyoku;
	$item[29] = 1;
	$item[30] = 1;

	$chara[26] = $host;

	$chara[128]=5;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>新たな自分専用の武器『$in{'bname'}』を受け取った！</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kagi{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$red=0;$blue=0;$yellow=0;$i=1;
	foreach(@souko_item){
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($iname eq "レッドノート"){$red=$i;}
		if($iname eq "ブルーノート"){$blue=$i;}
		if($iname eq "イエローノート"){$yellow=$i;}
		$i++;
	}
	if(!$red){&error("レッドノートが倉庫にありません");}
	elsif(!$blue){&error("ブルーノートが倉庫にありません");}
	elsif(!$yellow){&error("イエローノートが倉庫にありません");}
	else{
		$red-=1;$blue=0;$yellow=0;
		splice(@souko_item,$red,1);
		foreach(@souko_item){
			($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
			if($iname eq "ブルーノート"){splice(@souko_item,$blue,1);}
			$blue++;
		}
		foreach(@souko_item){
			($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
			if($iname eq "イエローノート"){splice(@souko_item,$yellow,1);}
			$yellow++;
		}
		$chara[315]=1;
	}
	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red"><br><br>
<B>天界への鍵を作った！！！</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}
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