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
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。     	#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    直接メールによる質問は一切お受けいたしておりません。   	#
#---------------------------------------------------------------#
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
<form action="jyouhou2.cgi" method="post">
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

&jyoho;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub jyoho {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>情報屋ver2</h1>
<hr size=0>
<FONT SIZE=3>
<B>情報屋のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここでは完全なJupiterFFAの攻略情報が聞けるぞ。ただし、会員専用だ。<br>
会員証を持って来い。入手法？それは、秘密だ。<br>
ネタバレが嫌な奴は、決してくるんじゃないぞ。<br>
ここで聞いた内容を、チャットや他のサイトなどに、絶対に漏らしてはいけないぞ。<br>
料金や内容は、会員証のレベルに応じて変わるぞ。」
</FONT>
<br>現在の所持金：$chara[19] Ｇ
<hr size=0>
EOM
	if ($chara[30] == 1000){print"裏技①がセットされています。";}
	if ($chara[30] == 2000){print"裏技②がセットされています。";}
	if ($chara[30] == 3000){print"裏技①と②がセットされています。";}
	if ($chara[31] == "0015") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="G級情報を見る(1000G) : 4個">
		</form><br>
EOM
	}elsif ($chara[31] == "0013") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="F級情報を見る(10000G) : 2個">
		</form><br>
EOM
	}elsif ($chara[31] == "0016") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="E級情報を見る(30000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0017") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="D級情報を見る(50000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0018") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="C級情報を見る(100000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0019") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="B級情報を見る(300000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0020") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="A級情報を見る(500000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0021") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="S級情報を見る(1000000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0022") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=jyoho_buy>
		<input type=submit class=btn value="SS級情報を見る(10000000G) : 1個">
		</form><br>
EOM
	}elsif ($chara[31] == "0030" or $chara[0] eq "jupiter") {
		print <<"EOM";
		<form action="./jyouhou2.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=pass>
		<input type=submit class=btn value="パスコードを使用する。">
		</form><br>
EOM
	}else{
		print <<"EOM";
		会員証がありません
EOM
	}
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=sc>
	<input type=submit class=btn value="スカウター ver2">
	</form>
EOM
if($chara[90]>999){
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=rg>
	<input type=submit class=btn value="レジスト">(レジスト値：$chara[89])
	</form>
EOM
}
if($chara[18]>2000){
	print <<"EOM";
	<form action="./jyouhou2.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=anjou>
	<input type=submit class=btn value="？？？">
	</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub jyoho_buy {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$aplace0="平原モンテヴィーヌ";$aplace1="洞窟ラヴォス";$aplace2="底なしの泥沼";
	$aplace3="闇山脈チャランラッツ";$aplace4="ダーク・エリア";$aplace5="神の塔エルヴァーヌ";
	$aplace6="スペシャルエリート";$aplace7="死者ゆく場所";$aplace8="イエローワールド";
	$aplace9="レッドワールド";$aplace10="ドラゴンワールド";$aplace11="ドラゴンヘブン";
	$aplace12="超魔王の城";$aplace13="天界への洞穴";$aplace14="天界の部屋";

	if ($chara[31] == "0015"){
		if($chara[19] < 1000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 1000; }
		$jyouhou="情報その１：戦闘力が1000の倍数の時、経験値が２倍になる。ただし装備必須。<br>";
		$jyouhou.="情報その２：製造品を成長させるとレアアイテムになることが多い。<br>";
		$jyouhou.="情報その３：壊れた装備の累計パワーは最低１００、できれば５００は欲しいな。<br>";
		$jyouhou.="情報その４：戦闘力が一回一致したら経験値を倍のままにさせる方法があるらしいな。<br>";
	}
	if ($chara[31] == "0013"){
		if($chara[19] < 10000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 10000; }
		$jyouhou = <<"EOM";
		情報その１：＜成長を必ず成功させる方法＞<br>
		①まず、お金になるアイテムを集めます。(倉庫の中に。)<br>
		②次元の狭間へ行き、警官に逮捕されます。<br>
		③そのままどこへも行かずに、倉庫へ行き、要らないアイテムを売ります。<br>
		④成長させます。必ず成功っっっ。お疲れ様でした。<br>
		あらかじめ成長費用分の売値を持つアイテムと、製造会社へ行く費用が必要になります。<br>
		商人になっていると少しやりやすいと思います。<br><br>
		情報その２：＜Ｅ級会員証の簡単入手法＞<br>
		①レッドワールドへ行きます。<br>
		②銀行から100万Ｇ引き出します。<br>
		③装飾品店でＧ級会員証を購入します。<br>
		④倉庫を確認します。終わり。<br>
EOM
	}
	if ($chara[31] == "0016"){
		if($chara[19] < 30000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 30000; }
		$jyouhou = <<"EOM";
		情報その１：＜製造レシピＮｏ１＞<br>
		闇の石＋闇の石→ダークナイフ（ランク２武器）<br>
		闇の石＋白い光→カオスソ\ード（ランク３武器）<br>
		白い光＋白い光→光の剣（ランク３武器）<br><br>

		情報その２：＜製造レシピＮｏ２の一部＞<br>
		○○＋白い光→竜骨盾（ランク５防具）<br>
		○○＋王者の証→Ｓ級会員証<br>
		○○＋ダークマター→剛剣（ランク４武器）<br>
EOM
	}
	if ($chara[31] == "0017"){
		if($chara[19] < 50000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 50000; }
		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
		$jyouhou = <<"EOM";
		<table>
		<tr><th>名前</th><th>出現場所</th><th>戦闘力</th></tr><tr>
EOM
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			if($abasyo==5 or $abasyo==6){$jyouhou.="<th>$aname</th><th>${'aplace'.$abasyo}</th><th>$power</th></tr>";}
		}
		$jyouhou.="</table>";
	}
	if ($chara[31] == "0018"){
		if($chara[19] < 100000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 100000; }
		$jyouhou = <<"EOM";
屋敷で儲ける方法か…。闇雲に進んだら必ず儲からないようにできているからな…。<br>
一方向に行き続ければ報酬が貰えるという、甘い罠に引っかかる初心者が本当に多い。<br>
いいか。屋敷で儲けたければ、まず、全ての方角、同じぐらいだけ進むんだ。<br>
そうだな、４ずつぐらい進むといいだろう。そのあと、欲しいもののある方向へ進むといい。<br>
これで、今日から君も儲けられるだろう。誰かに理由を聞かれても、決してしゃべるんじゃないぞっ<br>
Ｃ級？大した情報無かったよ。作らないほうがいいよ。とでも言っておくんだｗ
EOM
	}
	if ($chara[31] == "0019"){
		if($chara[19] < 300000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 300000; }
		$jyouhou = <<"EOM";
ペットが捕獲できることは知ってるよな？<br>
怪しくない方の武器屋で売ってるアイテムのうち、高成長させると、特殊な武器に成長するものがある。<br>
そいつを持って、ペットは持たずに、捕獲できる敵を倒すと、条件を満たしていれば捕獲することができるんだ。<br>
そして、捕獲したペットは、自分のレベルまで、レベルが上がる。お前が1000レベルを超えているなら、限界は1000レベルだ。<br>
ペットは1000レベルになると、魂をくれる。魂の用途はペットによって違うが、魂をペットに使うと、進化したりするな。<br>
例えば、新型ウイルスに新型ウイルスの魂を使うと新型ウイルス2に進化する。<br>
オーガにタヌキマンの魂を使うと、ギガントオークに進化する、というようにだな。<br>
ただし、ギガントオークは序盤で仲間にするべきペットではないな。<br>
あいつは極端に成長が遅いから、”学習装置”でも手に入れた後、他のペットと並行してレベルを上げたほうがいいだろう…。<br>
ん？学習装置？そいつについての情報はまた今度だな。ガッハッハｗ<br>
まぁともかく、なにしろ奴は成長が遅い。あいつより数倍強い”屋敷荒し”でさえ、あんなに遅くないぜ…<br>
ん？屋敷荒し？そいつについての情報はまた今度だな。ガッハッハｗ<br>
で、結論として、俺のお勧めだがな。まずはタヌキマンを育てておくのがいいだろう。<br>
成長度合は普通。パワーも成長の早さの割りに結構強い。あとでギガントオークを作ろうとした時に魂が必要だしな。<br>
次の段階はヘルハウンドだな。あいつも強いし、後に必要だぞ。ただし、捕獲の際には所持金に気をつけるんだぞ。<br>
しかしまぁ、ペットに強さを求めないなら、気に入ったペットを育てるといいぞ。<br>
周りの育てていないペットを育てていたら、意外な奴に進化…なんてこともあるだろうしな。<br>
頑張れ$chara[4]。お前がナンバーワンだ！(<br>
EOM
	}
	if ($chara[31] == "0020"){
		if($chara[19] < 500000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 500000; }
		$jyouhou="情報その１：1000回戦闘力を測定するとレジストモードが出現する。";
	}
	if ($chara[31] == "0021"){
		if($chara[19] < 1000000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 1000000; }
		$jyouhou="情報その１：クリティカルコメントを「時雨Ｆ燕流!!」にするとクリダメ4倍?(対モンスターのみ)";
	}
	if ($chara[31] == "0022"){
		if($chara[19] < 10000000) { &error("お金が足りません$back_form"); }
		else { $chara[19] = $chara[19] - 10000000; }
		$jyouhou="情報その１：画像Ｎｏを４６４９に設定することで取得経験値量+100％";
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>情報屋のマスター</B><BR>
「毎度あり～！では、教えよう！<br>
$jyouhou
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub sc {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&item_load;

	$sentou=$chara[8] * 4 + $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10 + $chara[8]/10 + 1);
	$sentou+=int($chara[16]/2) + $item[4] * (4 + int($chara[10]/10+1));
	$sentou+=(int(($chara[11] / 10)) + 10 + int($chara[12]/4))*10;
	$sentou+=(int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16])*10;
	$sentou+=(int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17])*10;
	if($item[0] eq "素手" or $item[3] eq "普段着"){$sentou+=int(rand(10));}
	$chara[90]+=1;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
#		$jyouhou = <<"EOM";
#		<table>
#		<tr><th>名前</th><th>出現場所</th><th>戦闘力</th></tr><tr>
#EOM
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			${'asentou'.$abasyo}+=$power;
			${'akazu'.$abasyo}+=1;
#			$jyouhou.="<th>$aname</th><th>${'aplace'.$abasyo}</th><th>$power</th></tr>";
		}
#		$jyouhou.="</table>";

	$aplace0="平原モンテヴィーヌ";$aplace1="洞窟ラヴォス";$aplace2="底なしの泥沼";
	$aplace3="闇山脈チャランラッツ";$aplace4="ダーク・エリア";$aplace5="神の塔エルヴァーヌ";
	$aplace6="スペシャルエリート";$aplace7="死者ゆく場所";$aplace8="イエローワールド";
	$aplace9="レッドワールド";$aplace10="ドラゴンワールド";$aplace11="ドラゴンヘブン";
	$aplace12="超魔王の城";$aplace13="天界への洞穴";$aplace14="天界の部屋";
	$bsentou=0;$csentou=0;$dsentou=0;$esentou=0;$bbasyo="";$cbasyo="";$dbasyo="";$ebasyo="";
	for($as=0;$as<15;$as++){
		if(${'akazu'.$as}){${'asentou'.$as}=int(${'asentou'.$as}/${'akazu'.$as});}
		if(${'asentou'.$as}<$sentou){
			if($bsentou<${'asentou'.$as}){
				$bsentou=${'asentou'.$as};$bbasyo=${'aplace'.$as};
				if($ebasyo){
					$csentou=$esentou;
					$cbasyo=$ebasyo;
				}
				$esentou=${'asentou'.$as};
				$ebasyo=${'aplace'.$as};
			}
		}else{
			if(!$dsentou or $dsentou>${'asentou'.$as}){
				$dsentou=${'asentou'.$as};
				$dbasyo=${'aplace'.$as};
			}
		}
	}
	$jyouhou.="あなたの戦闘力は<font color=\"yellow\">$bbasyo</font>のモンスター級です。<br>";
	$jyouhou.="敵数や仲間の強さを考慮して自信が無ければ<font color=\"yellow\">$cbasyo</font>、<br>";
	$jyouhou.="自信があるならば<font color=\"yellow\">$dbasyo</font>に挑むと良いでしょう。<br>";

if($chara[0] eq "jupiter"){
		open(IN,"data/allmonster.ini");
		@MONSTER = <IN>;
		close(IN);
		foreach(@MONSTER){
	($abasyo,$aname,$azoku,$alv,$amex,$arand,$asp,$admg,$akahi,$amonstac,$amons_ritu,$agold,$aimg) = split(/<>/);
			$power=($arand+$admg)*2+int($asp/10)+$akahi*10;
			$alv=int($power/100)+1;
	$gggg.="$abasyo<>$aname<>$azoku<>$alv<>$amex<>$arand<>$asp<>$admg<>$akahi<>$amonstac<>$amons_ritu<>$agold<>$aimg<><br>";
		}
}
	&header;

	print <<"EOM";
<h1>あなたの戦闘力は、$sentouです。</h1><br>
<h2>$jyouhou</h2>
$gggg
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub rg {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&item_load;

	$sentou=$chara[8] * 4 + $chara[7] * 4 + $item[1] * 4 * int($chara[7]/10 + $chara[8]/10 + 1);
	$sentou+=int($chara[16]/2) + $item[4] * (4 + int($chara[10]/10+1));
	$sentou+=(int(($chara[11] / 10)) + 10 + int($chara[12]/4))*10;
	$sentou+=(int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16])*10;
	$sentou+=(int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17])*10;
	$chara[89]=$sentou;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>あなたの現在の戦闘力$sentouを、レジストしました。</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  パスコード　  #
#----------------#
sub pass {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[31] == "0030" or $chara[0] eq "jupiter"){
	$hokaku = <<"EOM";
	<form action="jyouhou2.cgi" method="post">
	<input type=hidden name=id value="$chara[0]">
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=hokaku>
	<input type=submit class=btn value="捕獲可\能\ペット">
	</form>
EOM
	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;
	$jyouhou="<table><tr><th>Ｎｏ．</th><th>質問者</th><th>内容</th><th>返答者</th><th>答え</th></tr>";
	foreach(@member_data){
		($no,$q_name,$q_com,$a_name,$a_com) = split(/<>/);
		if($no>$i-60){
			$jyouhou.="	<tr>
			<th>$no</th>
			<th><font size=2.9>$q_name</font></th><th><font size=2.9>「$q_com」</font></th>
			<th><font size=2.9>$a_name</font></th><th><font size=2.9>「$a_com」</font></th>
			</tr>";
		}
	}
	$jyouhou.="</table>";
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=toukou>
質問内容　：<input type="text" name="com" value="" size=40><br>
<br>　　
<input type=submit class=btn value="質問する">
</form>

EOM
if($chara[0] eq "jupiter"){
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kaitou>
No.:<input type="text" name="no" value="" size=10><br>
回答内容　：<input type="text" name="com" value="" size=40><br>
<br>　　
<input type=submit class=btn value="回答する">
</form>
EOM
}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>†ジュピタ†の何でも相談室！(別名　裏掲示板)</B><BR><br>
「ここで聞くと、(†ジュピタ†の気が向いたら)何でも答えてくれるみたいだよ！<br>
あんまり沢山聞いたりすると、†ジュピタ†は返信してくれないよ！<br>
あと、半年後に返答が来たりしても(来なかったとしても)怒らないように！<br>
とりあえず、表\示されるのは最新の60件。ログ検索はいつかできるようにするかも…<br><br>
捕獲可\能\ペットについては、→$hokaku
$jyouhou
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub toukou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($chara[31] != "0030" and $chara[0] ne "jupiter"){&error("パスコードもってこいバカモン$back_form");}
	else{
		if ($in{'com'} eq "") {
			&error("内容を入力しないで何を聞く？$back_form");
		}
	}

	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;$i+=1;

	push(@member_data,"$i<>$chara[4]<>$in{'com'}<><><>\n");

	open(OUT,">passcode.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>質問を投稿しました。</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kaitou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if ($chara[31] != "0030" and $chara[0] ne "jupiter"){&error("パスコードもってこいバカモン$back_form");}
	else{
		if ($in{'com'} eq "") {
			&error("内容を入力しないで何を聞く？$back_form");
		}
		if ($in{'no'} eq "") {
			&error("ナンバーを入力せい。$back_form");
		}
	}

	open(IN,"passcode.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		($no,$q_name,$q_com,$a_name,$a_com) = split(/<>/);
		if($in{'no'} == $no){
			$member_data[$i]="$no<>$q_name<>$q_com<>$chara[4]<>$in{'com'}<>\n";
			last;
		}
		$i++;
	}

	open(OUT,">passcode.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>質問に回答しました。</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub hokaku {
	
	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if ($chara[31] == "0030" or $chara[0] and "jupiter"){
	open(IN,"hokakukanou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=@member_data;$no=0;
	$jyouhou="<table><tr><th>ペット名</th><th>捕獲場所</th><th>捕獲方法</th><th>備考</th><th>ペット名</th><th>捕獲場所</th><th>捕獲方法</th><th>備考</th></tr>";
	foreach(@member_data){
		($name,$basyo,$houhou,$bikou) = split(/<>/);
		if($no>$i-100){
			if($no % 2 == 0){$jyouhou.="<tr>";}
			$jyouhou.="	<th><font size=2.9>$name</font></th><th><font size=2.9>$basyo</font></th>
					<th><font size=2.9>$houhou</font></th><th><font size=2.9>$bikou</font></th>";
			if($no % 2 == 1){$jyouhou.="</tr>";}
		}
		$no++;
	}
	$jyouhou.="</table>";
if($chara[0] eq "jupiter"){
		$jyouhou .= <<"EOM";
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ptoukou>
ペット名:<input type="text" name="name" value="" size=40><br>
捕獲場所　：<input type="text" name="basyo" value="" size=40><br>
捕獲方法　：<input type="text" name="houhou" value="" size=40><br>
捕獲備考　：<input type="text" name="bikou" value="" size=40><br>
<br>　　
<input type=submit class=btn value="投稿する">
</form>
EOM
}
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3><br><br>
<B>†ジュピタ†の何でも相談室！(別名　裏掲示板)</B><BR><br>
「ここでは、捕獲ペットについて、書くぞ。自力で見つけたい人は見るんじゃないぞ。<br>
とりあえず、表\示されるのは最新の100件。ログ検索はいつかできるようにするかも…<br><br>
$jyouhou
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub ptoukou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"hokakukanou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		($name,$basyo,$houhou,$bikou) = split(/<>/);
		if($name eq $in{'name'}){
			$hit=1;
			if($in{'basyo'}){$basyo=$in{'basyo'};}
			if($in{'houhou'}){$houhou=$in{'houhou'};}
			if($in{'bikou'}){$bikou=$in{'bikou'};}
			$member_data[$i]="$in{'name'}<>$basyo<>$houhou<>$bikou<>\n";
		}
		$i++;
	}
	if($hit != 1){
		push(@member_data,"$in{'name'}<>$in{'basyo'}<>$in{'houhou'}<>$in{'bikou'}<>\n");
	}

	open(OUT,">hokakukanou.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>ペットについて投稿しました。</B><BR>
</font>
<br>
<form action="jyouhou2.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=hidden name=mode value=pass>
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub anjou {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');	
	&chara_load;

	&chara_check;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	open(IN,"data/angou.ini");
	$angou = <IN>;
	close(IN);

	$i=0;
	while ($angou =~ /([\x00-\x7f]|..)/g) {
		$angou1[$i]="$1";
		$i++;
	}

	$i=0;
	foreach(@angou1){
		if("$_" eq "あ"){$angou1[$i]="a";}if("$_" eq "い"){$angou1[$i]="b";}
		if("$_" eq "う"){$angou1[$i]="c";}if("$_" eq "え"){$angou1[$i]="d";}
		if("$_" eq "お"){$angou1[$i]="e";}if("$_" eq "か"){$angou1[$i]="f";}
		if("$_" eq "き"){$angou1[$i]="g";}if("$_" eq "く"){$angou1[$i]="h";}
		if("$_" eq "け"){$angou1[$i]="i";}if("$_" eq "こ"){$angou1[$i]="j";}
		if("$_" eq "さ"){$angou1[$i]="k";}if("$_" eq "し"){$angou1[$i]="l";}
		if("$_" eq "す"){$angou1[$i]="m";}if("$_" eq "せ"){$angou1[$i]="n";}
		if("$_" eq "そ"){$angou1[$i]="o";}if("$_" eq "た"){$angou1[$i]="p";}
		if("$_" eq "ち"){$angou1[$i]="q";}if("$_" eq "つ"){$angou1[$i]="r";}
		if("$_" eq "て"){$angou1[$i]="s";}if("$_" eq "と"){$angou1[$i]="t";}
		if("$_" eq "な"){$angou1[$i]="u";}if("$_" eq "に"){$angou1[$i]="v";}
		if("$_" eq "ぬ"){$angou1[$i]="w";}if("$_" eq "ね"){$angou1[$i]="x";}
		if("$_" eq "の"){$angou1[$i]="y";}if("$_" eq "は"){$angou1[$i]="z";}
		if("$_" eq "ひ"){$angou1[$i]="A";}if("$_" eq "ふ"){$angou1[$i]="B";}
		if("$_" eq "へ"){$angou1[$i]="C";}if("$_" eq "ほ"){$angou1[$i]="D";}
		if("$_" eq "ま"){$angou1[$i]="E";}if("$_" eq "み"){$angou1[$i]="F";}
		if("$_" eq "む"){$angou1[$i]="G";}if("$_" eq "め"){$angou1[$i]="H";}
		if("$_" eq "も"){$angou1[$i]="I";}if("$_" eq "や"){$angou1[$i]="J";}
		if("$_" eq "ゆ"){$angou1[$i]="K";}if("$_" eq "よ"){$angou1[$i]="L";}
		if("$_" eq "ら"){$angou1[$i]="M";}if("$_" eq "り"){$angou1[$i]="N";}
		if("$_" eq "る"){$angou1[$i]="O";}if("$_" eq "れ"){$angou1[$i]="P";}
		if("$_" eq "ろ"){$angou1[$i]="Q";}if("$_" eq "わ"){$angou1[$i]="R";}
		if("$_" eq "を"){$angou1[$i]="S";}if("$_" eq "ん"){$angou1[$i]="T";}
		$i++;
	}
	open(OUT,">data/angou1.ini");
	print OUT @angou1;
	close(OUT);

	&header;

	print <<"EOM";
<h1>@angou1</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}