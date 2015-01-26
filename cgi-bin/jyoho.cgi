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
<form action="jyoho.cgi" method="post">
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
<h1>情報屋</h1>
<hr size=0>
<FONT SIZE=3>
<B>情報屋のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
今日も沢山、情報仕入れてるぜーっ。<br>
一回に聞ける情報はわずかだが、何回も聞いてくれれば違う情報をあげられることもあるぞ。<br>
さらに、最近、俺のレベルが上がってな。キャラ情報を調べられるようになったぞ。<br>
名前を教えてくれれば対象がログインしてなくてもステータスを教えてやろう。」<br>
</FONT>
EOM
if($chara[70]>=1){
	print <<"EOM";
<form action="jyouhou2.cgi" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="情報屋２へ">
</form>
EOM
}
	print <<"EOM";
<br>現在の所持金：$chara[19] Ｇ
<hr size=0>
	<form action="./jyoho.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=jyoho_buy>
	<table>
	<tr>
	<th></th><th>No.</th><th>情報の種類</th><th>値段</th><th>情報の数</th></tr>
	<th>
EOM
	if ($chara[19] >= 20000) {print "<input type=radio name=ps_no value=1>";}
	else{print "×";}
	print <<"EOM";
	</th><th>001</th><th>ドラゴンエッグについて</th><th>20000G</th><th>4コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 10000) {print "<input type=radio name=ps_no value=2>";}
	else{print "×";}
	print <<"EOM";
	</th><th>002</th><th>エッグソ\ードについて</th><th>10000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 15000) {print "<input type=radio name=ps_no value=3>";}
	else{print "×";}
	print <<"EOM";
	</th><th>003</th><th>卵やペットについて</th><th>15000G</th><th>3コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=4>";}
	else{print "×";}
	print <<"EOM";
	</th><th>004</th><th>転職やステ振りについて</th><th>30000G</th><th>2コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=5>";}
	else{print "×";}
	print <<"EOM";
	</th><th>005</th><th>武器について</th><th>30000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 30000) {print "<input type=radio name=ps_no value=6>";}
	else{print "×";}
	print <<"EOM";
	</th><th>006</th><th>新世界について</th><th>30000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 5000) {print "<input type=radio name=ps_no value=7>";}
	else{print "×";}
	print <<"EOM";
	</th><th>007</th><th>つるはし</th><th>5000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 50000) {print "<input type=radio name=ps_no value=8>";}
	else{print "×";}
	print <<"EOM";
	</th><th>008</th><th>誰も知らない存在</th><th>50000G</th><th>6コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 500000) {print "<input type=radio name=ps_no value=9>";}
	else{print "×";}
	print <<"EOM";
	</th><th>009</th><th>裏話</th><th>500000G</th><th>3コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 1000000) {print "<input type=radio name=ps_no value=10>";}
	else{print "×";}
	print <<"EOM";
	</th><th>010</th><th>攻城戦小技</th><th>1000000G</th><th>3コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=11>";}
	else{print "×";}
	print <<"EOM";
	</th><th>011</th><th>ヤマタノオロチ</th><th>100000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000) {print "<input type=radio name=ps_no value=12>";}
	else{print "×";}
	print <<"EOM";
	</th><th>012</th><th>製造会社</th><th>100000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 150000) {print "<input type=radio name=ps_no value=13>";}
	else{print "×";}
	print <<"EOM";
	</th><th>013</th><th>金の亡者</th><th>150000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 8000000) {print "<input type=radio name=ps_no value=14>";}
	else{print "×";}
	print <<"EOM";
	</th><th>014</th><th>リミッター</th><th>8000000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=15>";}
	else{print "×";}
	print <<"EOM";
	</th><th>015</th><th>ドリームコンボ</th><th>100000000G</th><th>4コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 300000000) {print "<input type=radio name=ps_no value=16>";}
	else{print "×";}
	print <<"EOM";
	</th><th>016</th><th>オリジナル武器</th><th>300000000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 500000000) {print "<input type=radio name=ps_no value=17>";}
	else{print "×";}
	print <<"EOM";
	</th><th>017</th><th>魔薬</th><th>500000000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=18>";}
	else{print "×";}
	print <<"EOM";
	</th><th>018</th><th>悪魔のノートと夢世界</th><th>100000000G</th><th>8コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 800000000) {print "<input type=radio name=ps_no value=19>";}
	else{print "×";}
	print <<"EOM";
	</th><th>019</th><th>魂繋がり</th><th>800000000G</th><th>1コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 1000000000) {print "<input type=radio name=ps_no value=20>";}
	else{print "×";}
	print <<"EOM";
	</th><th>020</th><th>無属性魔法</th><th>1000000000G</th><th>2コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=21>";}
	else{print "×";}
	print <<"EOM";
	</th><th>021</th><th>黒魔法</th><th>100000000G</th><th>6コ</th></tr>
	<th>
EOM
	if ($chara[19] >= 100000000) {print "<input type=radio name=ps_no value=22>";}
	else{print "×";}
	print <<"EOM";
	</th><th>022</th><th>チャイナ？</th><th>100000000G</th><th>1コ</th></tr>
	</table>
	<br><br>
	<input type=submit class=btn value="情報を買う">
	</form>
EOM
	print <<"EOM";
	<form action="./jyoho.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type="text" name="taisyo" size=20><br>
	<input type=hidden name=mode value=mem_sts>
	<input type=submit class=btn value="キャラ情報を調べる">
	</form>
EOM
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

	if ($in{'ps_no'}==""){ &error("欲しい情報を選んでください$back_form"); }
	if ($in{'ps_no'}==1){$ps_gold = 20000;}
	if ($in{'ps_no'}==2){$ps_gold = 10000;}
	if ($in{'ps_no'}==3){$ps_gold = 15000;}
	if ($in{'ps_no'}==4){$ps_gold = 30000;}
	if ($in{'ps_no'}==5){$ps_gold = 30000;}
	if ($in{'ps_no'}==6){$ps_gold = 30000;}
	if ($in{'ps_no'}==7){$ps_gold = 5000;}
	if ($in{'ps_no'}==8){$ps_gold = 50000;}
	if ($in{'ps_no'}==9){$ps_gold = 500000;}
	if ($in{'ps_no'}==10){$ps_gold = 1000000;}
	if ($in{'ps_no'}==11){$ps_gold = 100000;}
	if ($in{'ps_no'}==12){$ps_gold = 100000;}
	if ($in{'ps_no'}==13){$ps_gold = 150000;}
	if ($in{'ps_no'}==14){$ps_gold = 8000000;}
	if ($in{'ps_no'}==15){$ps_gold = 100000000;}
	if ($in{'ps_no'}==16){$ps_gold = 300000000;}
	if ($in{'ps_no'}==17){$ps_gold = 500000000;}
	if ($in{'ps_no'}==18){$ps_gold = 100000000;}
	if ($in{'ps_no'}==19){$ps_gold = 800000000;}
	if ($in{'ps_no'}==20){$ps_gold = 1000000000;}
	if ($in{'ps_no'}==21){$ps_gold = 100000000;}
	if ($in{'ps_no'}==22){$ps_gold = 100000000;}
	if($chara[19] < $ps_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	if($in{'ps_no'}==1){
	$ran=int(rand(4));
	if($ran==0){
$jyouhou="「ドラゴンエッグ」という非常に貴重な卵がこの世にはあるらしい。<br>
なんでもその中からは種族最強の竜族が生まれるらしいぞ。<br>
入手方法なんだがな、卵やペットを持たずに平原を歩き回ることがポイントらしい。";
}
	if($ran==1){
$jyouhou="ドラゴンはよ、エッグから生まれるらしい。<br>
メモっとけよ。";
}
	if($ran==2){
$jyouhou="ドラゴンエッグを手に入れる方法？<br>
配合だよ、配合";
}
	if($ran==3){
$jyouhou="エッグを手に入れるためには、レベル60以上である必要がある。<br>
メモっとけよ。";
}
	}
	if($in{'ps_no'}==2){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="伝説の剣「エッグソ\ード」、この剣なら卵に入る経験値が最大10倍になるというぜ。<br>
ただし入手は難しい。あるボスを倒すか…あるいは製造か…あるいは…。<br>
まぁ、言っておくがこいつを見つけるのは素人にゃ無理だからな。<br>
無理して探さなくても、時間をかけて卵を育てるといいだろう。";
}

	}
	if($in{'ps_no'}==3){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="壊れた卵はよ、引き取ってもらうと金がかかるだろ？ただし、<br>
新しい卵を買っちまえば金がかからないんだよな。知ってたか？";
}
	if($ran==1){
$jyouhou="どんな卵も育て続けたら何か起こるぞ。<br>
それも、世界が変わるような…そんなことがよ…";
}
	if($ran==2){
$jyouhou="ペットには、最終形態がある。例えばイエローエッグはパンダマンだな。<br>
必要経験値が100万になってたら最終形態だな。";
}
	}
	if($in{'ps_no'}==4){
	$ran=int(rand(2));
	if($ran==0){
$jyouhou="どんな職業が強いかって･･･？<br>
まずは、魔法剣士が重要な職業だろうな。何しろ魔法剣は強い！";
}
	if($ran==1){
$jyouhou="ステータスポイント、ちゃんと振っているか？<br>
技が発動しないなら、ＥＧＯが足りない。<br>
攻撃が当たらないなら、ＤＥＸが足りない。<br>
攻撃は当たるし、技も発動するならば、攻撃力を上げる為にＩＮＴを振ると良いだろう。<br>
それでもポイントに余裕があるなら、ＬＵＫでクリティカル率を上げたり、ＳＴＲでさらに攻撃力を上げよう。<br>
ＶＩＴでは、ＨＰや防御力が上がるが、どちらかというと攻撃力の方が重要だろうな。";
}
	}
	if($in{'ps_no'}==5){
$jyouhou="武器にはランクというものがある…ここでいくつか教えてあげよう。<br>
No.1アイアンソ\ードからNo.10モーニングスターが店で売ってるアイテム武器だな？これらに加えて、<br>
No.11微笑みの杖、12クロスボウ、13プリズムロッド、14ルーンブレイド、15フランベルジュ<br>
ここまでがランク１の武器だ…Noが上がるほど強いと考えていい。そして・・・<br>
No.16妖精のロッド、No.17フレイムタン、No.20アイスブランド、No.25虎鉄など、No.16～No.30の武器はランク２だ・・・<br>
ランク３は菊一文字やフェアリーテール、サイコダガーなど、ランク４はグングニル、村雨、破壊の剣って感じだ。<br>
ランク５になるとメテオ・ブレイカー、オメガブラスターなどと、さらに強い装備となるわけだが・・・<br>
ちなみにエッグソ\ードなどはランク６だが、ランク６は特殊、ということで、強い、とは違うな。<br>
ついでに一つ情報だ。武器を合成する時は、ランクの合計が高くなるように合成しろよ。わかったか？<br>
また情報を入手することもあるだろうから、ちょくちょく寄ってくれ。";
	}
	if($in{'ps_no'}==6){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="新世界か…ズバリ、聞きたいのは鍵のありかだろう。<br>
ところで、ペットはたびたび退化をして飼主を困らせたりするな。<br>
そんなペットがちゃんと成長できると、恩返しをしてくれるという。恩返しとは？<br>
ペットのペットしか知らない世界への「鍵」と表\現していいものだな。<br>
ああ、完全に成長が止まった時、それが、ペットの恩返しの時期だ…。<br>
お金を惜しまず育てると良いだろう。";
}
	}
	if($in{'ps_no'}==7){
$jyouhou="つるはしなら、戦ってればモンスターが落とすよ。";
	}
	if($in{'ps_no'}==8){
	$ran=int(rand(6));
	if($ran==0){
$jyouhou="誰も知らない存在についての情報だね。<br>
アンクドラルさんが提供してくれた情報だ。<br>
壊れてしまった卵から、新たな生が発生する、ということだそうだ。";
}
	if($ran==1){
$jyouhou="誰も知らない存在についての情報だね。今回はNo１だ。<br>
ペットのＨＰやレベル、そして攻撃力、これらは金次第で少しは何とかできるのは知ってるか？<br>
金の力っていうのは恐ろしいもんだ。何が起きるかわからん。";
}
	if($ran==2){
$jyouhou="誰も知らない存在についての情報だね。今回はNo２だ。<br>
「それ」は、「ゴーチル」と名づけられた。アンクドラルさんのセンスにビックリだ。<br>
アンクドラルさんの元ですくすく育ち、やがて、並の冒険者を遥かに越える力を身につけた。<br>
「ゴーチル」がなぜ、神に近い存在といえるのか、このときはまだわかっていなかった。";
}
	if($ran==3){
$jyouhou="誰も知らない存在についての情報だね。今回はNo３だ。<br>
ところで、進化しても「ゴーチル」なのは、アンクドラルさんがその名前をすっかり気に入ったからだ。<br>
だから、いまだに、進化前と、後とで区別する方法がないんだ・・・<br>
果たして、ゴーチルには「ゴッドバード」や「ドラゴンロード」のように、最終形態が存在するのか<br>
私には、アンクドラルさん達を見守ることしかできなかった。。。";
}
	if($ran==4){
$jyouhou="誰も知らない存在についての情報だね。今回はNo４だ。<br>
やがて、ゴーチルに変\化が出た。もはや、その存\在は、言い\表\せない。<br>
彼は、戦う鬼の様な存\在でありながら、優しい心を持つ存\在だった。<br>
彼は進\化の過\程でどんどんと技を変\化させた。<br>
そして・・・、ついに、彼は、人間を蘇\生することをも、可\能にしたのだ･･･。";
}
	if($ran==5){
$jyouhou="誰も知らない存在についての情報だね。今回はNo５だ。<br>
神の国と呼ばれるアルバンダルに、ある伝説がある。<br>
神は、死より生まれて、生を与える存在。<br>
神は、慈悲深いわけではなく、気まぐれで、何かをすることの方が珍しい<br>
神は、誰にも殺すことができない。<br>
そう、この伝説で\表\される「神」に、ゴーチルは、似ていると思わんか？";
}
	}
	if($in{'ps_no'}==9){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="壊れた卵、普通に引き取ってもらおうとすると3万Ｇかかるだろ？<br>
実は、他の卵を買えば、無料で引き取って貰えるぜ。";
}
	if($ran==1){
$jyouhou="なに？最近レベルが上がりにくい？そりゃ、上級者の悩みだな。<br>
そんなときは、レジェンドプレイスで称号を上げてみな。いいことあるかもよ？";
}
	if($ran==2){
$jyouhou="なに？レッドワールドの鍵がどうしても入手できない？<br>
実は火鉄も最終形態じゃないのに鍵を持ってるって話だ。<br>
こいつはかなりの裏話だが、あまりの鍵の出なささに苦情が殺到したらしいんだ。";
}
	}
	if($in{'ps_no'}==10){
	$ran=int(rand(3));
	if($ran==0){
$jyouhou="ブリザガ…あれは中々の技だ…その効果は相手が複数いる時に最も発揮できるな。<br>
なにせ全員のダメージを一気に落としてくれるからな…。";
}
	if($ran==1){
$jyouhou="まさか攻城戦に行くって時に金ＵＰだの盗むだのつけてないだろうな？<br>
対人から金やアイテムを盗むのは犯罪だ。できないぞ？ｗ";
}
	if($ran==2){
$jyouhou="一撃必殺。瀕死のときに発動するやつだな。攻城戦では発動しやすいかもな。<br>
回避と防御力が重要になりそうだな。";
}
	}
	if($in{'ps_no'}==11){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="ヤマタノオロチがどこにいるかって？<br>
次元の狭間さ。超一流の冒険者のみが行くことを許されるのさ。<br>
アンクドラルさん？もちろん日常的に行ってるぜ。ただ、あそこの敵はエグイのさ。<br>
戦略的なモンスターばかりでな、まずPTで行こうがギルドで行こうが引き離されて結局戦う時は一人になる。<br>
さらに、モンスターの強力な一撃で装備がぶっ壊れちまうこともあるっていうんだからな…。<br>
素手で行けば問題ない･･･そういえば格闘家にあったな…素手用アビリティ・・・。";
}
	}
	if($in{'ps_no'}==12){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="限界突破後、狭間で稀に、会社が出るだろ？<br>
あそこは怪しい会社だよなー。なにせ、入手難度Ａクラスの「製造品」が手に入るんだからな…。<br>
だが、怪しいからな。あまりついていかない方がいい。<br>
関係ないんだが「闇卵」知ってるか？どっかの施設で強力な冒険者のみに渡してる卵らしいが。<br>
闇卵は、もしも壊れてしまっても100万Ｇで元に戻せるらしい。<br>
ただ、その場所は、金持ちにしか見つからないらしいぜ。金を沢山持って怪しい場所を当たってみな。";
}
	}
	if($in{'ps_no'}==13){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="狭間に金の亡者っていうボスモンスターが出現するよな。<br>
あいつらは厄介だ。ある条件さえ整っていれば、１ターンとかからずに瞬殺できるそうだが…。<br>
普通に戦おうとすると厄介だ。まず、必須アイテムだが、時計だな。<br>
時計の、秒数に注意して戦うと、ヤツの弱点がわかってくる。<br>
一度ヤツに攻撃がクリーンヒットしたら、同じアビリティで60秒後、再戦だ。<br>
運が良ければ、たとえ弱くても倒せるはずさ。";
}
	}
	if($in{'ps_no'}==14){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="今回の情\報は「リミッター」。<br>
「リミッター」というのは装\備の名\前だな。防\具だ。<br>
「材\料」は「屋\敷」にある。「屋\敷」について知らない奴には入\手はまだ早いだろう。<br>
いいか？「屋\敷」で「三\角\帽\子」か「普\通の盾」、「凄\重の鎧」を拾ったら、拾った場所をメモしておくんだ。<br>
そして、その中の「三\角\帽\子」。こいつが今\回の情\報の鍵になる。<br>
こいつを成\長させて、なんとか「五\角\帽\子」にする。さらに成\長すると、「リミッター」になるのだ。<br>
その効\果は凄まじい。何でも、特\殊なモンスターの捕\獲には必\須だとか…。<br>
問題は、「三\角\帽\子」をどうやって「リミッター」に成\長させるかだが…これは色々試してみる他あるまい…。";
}
	}
	if($in{'ps_no'}==15){
	$ran=int(rand(4));
	if($ran==0){
$jyouhou="夢屋というジョブを知っているか？<br>
俺も最近、アンクドラルさんに聞いたんだが、不思議な動アビリティを持っているジョブだという。<br>
この動アビリティの発動条件はこうだ。１つ目の動アビリティに「ドリームコンボ」をセットし、<br>
２つ目に「サイクロン」、３つ目に「マイティガード」をセットする。<br>
他にも発動条件があるようだ。「マイティサイクロン」は、特定の状況において絶大な効果を発揮するぞ。";
}
	if($ran==1){
$jyouhou="夢屋というジョブを知っているか？<br>
俺も最近、アンクドラルさんに聞いたんだが、不思議な動アビリティを持っているジョブだという。<br>
この動アビリティの発動条件はこうだ。１つ目の動アビリティに「ドリームコンボ」をセットし、<br>
２つ目に「時空を飛ぶ」、３つ目に「地獄へ飛ばす」をセットする。<br>
他にも発動条件があるようだ。「時空地獄へ飛ばす」は、今までの常識を覆す破壊力を持つが、使いづらい場合もあるな。<br>
おそらく、「闇の衣」や「鉄壁のお守り」を装備して使うのがいいだろう。";
}
	if($ran==2){
$jyouhou="夢屋というジョブを知っているか？<br>
俺も最近、アンクドラルさんに聞いたんだが、不思議な動アビリティを持っているジョブだという。<br>
この動アビリティの発動条件はこうだ。１つ目の動アビリティに「ドリームコンボ」をセットし、<br>
２つ目に「必殺拳法」、３つ目に「惑わす」をセットする。<br>
他にも発動条件があるようだ。「酔拳」は、今までの常識を覆す破壊力を持つが、使いづらい場合もあるな。<br>
おそらく、「妖刀アジア」を装備して使うのがいいだろう。";
}
	if($ran==3){
$jyouhou="夢屋というジョブを知っているか？<br>
俺も最近、アンクドラルさんに聞いたんだが、不思議な動アビリティを持っているジョブだという。<br>
この動アビリティの発動条件はこうだ。１つ目の動アビリティに「ドリームコンボ」をセットし、<br>
２つ目に「聖なる審判」、３つ目に「ドラゴンブレス」をセットする。<br>
他にも発動条件があるようだ。「聖なるブレス」は、大回復・全体攻撃の非常に有用なコンボだな。<br>
ともかく強い武器を装備して使うのがいいだろう。";
}
	}
	if($in{'ps_no'}==16){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="オリジナル武器についてか。<br>
こいつは『無の空間』で入手できる装備だな。全く属性がなく、全く人為が加えられていないが故に無限の可\能\性を持つ。<br>
さて、もしもこの武器を入手することができたならば、その取り扱いには十\分気をつけるべきだ。<br>
持ち主の育て方によって、４種の方向へ進化する可\能\性がある。簡単に説明しよう…。<br>
<br>
①まずは、物理型の武器だ。単純に攻撃力が高い。<br>
最も扱いやすいし、４種の型の中では育てるのも簡単な方だろう。<br>
この型に育てるためには、攻撃力を上げる類の魔薬を使用すればよい。<br>
<br>
②つぎに、必殺型の武器だ。単純な攻撃力こそ高くはないものの、必殺技を発動するのが特徴だ。<br>
扱いにくいが、必殺技を発動した時の威力は、想像を絶するだろう。<br>
この型に育てるためには、命中率を上げる類の魔薬を使用すればよい。<br>
<br>
③つぎは、能\力\型の武器だ。攻撃力は高くないが、多くの能\力を持たせることが可\能だ。<br>
昇竜剣や妖刀の能\力を１つの武器で持てるとしたら…と言えば、その価値、わかるか？<br>
この型に育てるためには、攻撃力と、命中率を上げる類の魔薬を、均等に使用していけばよい。<br>
<br>
④最後に、特殊型の武器だな。こいつは、どうも、わからないことだらけだ。<br>
存在は確認されているが…。もし特殊型の武器について情報を入手できれば是非教えてくれ。<br>
<br>
オリジナル武器が進化した後、その装備でもって悪魔界の敵を倒すことで、それぞれの型にあったマテリアが入手できるようになる。<br>
「物理型マテリア」「必殺型マテリア」「能\力型マテリア」「特殊型マテリア」だな。<br>
そのマテリアを装備することで、武器は格段に強くなるぞ…！<br>
…とまぁ、俺の知っている情報は、そんなところだな。<br>
また来てくれっ。";
}
	}
	if($in{'ps_no'}==17){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="魔薬について知りたいのか…？　どこでその話を聞いた。<br>
あれは、少し危険すぎるアイテムだ。入手するのも容易じゃぁない。<br>
なにしろ、悪魔界の悪魔と戦わなければならないんだからな。<br>
悪魔界への道はいくつか存在するが…たとえば、悪魔の館…そこから、悪魔界の悪魔に挑戦することが可\能\だ…。<br>
悪魔界の悪魔との戦いに勝てれば、レアな装備や、魔薬が入手できる可\能\性があるというわけだ。<br>
ちなみに、魔薬は、そのままでは人間界において使用することができない。<br>
人間界用に調整する必要があるんだ。<br>
この町にはそんな技術を持った奴は居なかったんだが、最近<font color=\"red\" size=3>ドリームワールド</font>から便利屋が来たな。<br>
ふざけた名前の店だが、ドリームワールドは最も技術の進んでいるワールド。調整する技術を持っている…らしいぞ。<br>
どんな魔薬があるか説明しよう。<br>
まずは、オリジナル武器の性\能\を上げる魔薬。<br>
攻撃力を上げるスタートッカA<br>
命中率を上げるスタートッカH<br>
両方を上げるスタートッカS<br>
次に、ペットの能\力\値を上げる魔薬。<br>
攻撃力を上げるシェドンレックA<br>
HPを上げるシェドンレックV<br>
レベルを上げるシェドンレックP<br>
さらに、ペットの魂を取り出すシェドンレックQ<br>
などがある。<br>
悪魔界への耐性が強くなれば、より強いアイテムが発見できるかもしれないな。";
}
	}
	if($in{'ps_no'}==18){
	$ran=int(rand(8));
	if($ran==0){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
さらに、あの３冊のノートは限界突破をしていたという。<br>
つまり、マテリアが装備されていた可能性が高いということ。何か強い特殊な\能\力\を秘めているやもしれんな。<br>
まぁ、さすがに武器として\成\長\する\能\力\は失われているだろうがな。<br>
誰が作った装備なのか。気にならないかね？";
}
	if($ran==1){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
いつのことなのだろうか…。まだ、現在確認されている３つの世界が存在しなかった頃に違いない…。<br>
平行しない世界…垂直する世界…ドリームワールドで作られた装備だろう。<br>
ドリームワールドの鍵を持っているのはスティーブン兄弟で間違いない。いや、そのほかに居るはずもない。<br>
それは知っている…。彼らから何とかドリームワールドの鍵を借りることができないものか…。";
}
	if($ran==2){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
スティーブン兄弟がそう言っているのを聞いたことがあるのだ。<br>
彼らは、３冊のノートを求めている。<br>
その３冊のノートさえあれば、オリジナル・トーマスを軽く倒すことが出来る、とか意味不明なことを言っていた。<br>
そう、その３冊があれば…強力な…力を身につけることができるようだな。";
}
	if($ran==3){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
３冊のノートを入手するのは、想像を絶するほど困難なことだろう。まず、悪魔界に突入せねばならない。<br>
悪魔は強い。どうしてもオリジナル武器の強化が不可欠だ。<br>
ただし、オリジナル武器の強化には、テクニックがあるのだ…。アンクドラル直伝の…。<br>
関連するのは意外にもペットだということだな。特に、珍しい、例のペット…。いつか話したはずだ。";
}
	if($ran==4){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
無の空間か…。<br>
あそこで入手した武器、強化するのは並の努力じゃ済まないが…。<br>
ある条件さえ、そろえれば、強化が楽になる。<br>
<font color=\"red\">マテリアが、何であるか</font>、その根本を知っていれば、気づくだろう。<br>";
}
	if($ran==5){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
無の空間で入手した装備っていうのは、持ち主しか受け付けない。<br>
が、この３冊のノートは既に、持ち主が居ないし、相当な年月が経っているからな…話は別だ。<br>
そう、<font color=\"red\">ノートは時間を知っている</font>んだ。";
}
	if($ran==6){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
太古の昔から受け継がれる存在…。<br>
話は変わるが…。黄色・赤・龍、ご存知、現在確認される３つの世界だ。<br>
いつからある世界なんだろうな？<br>
そして、何が生みだしたものなんだろうな？<br>
<font color=\"red\">どの世界にも属さない存在</font>っていうのがあるって、知ってるか？";
}
	if($ran==7){
$jyouhou="悪魔界に存在すると言われる悪魔のノート３冊…。<br>
あれは、太古の昔に無の空間から作られた武器だったそうだ…。<br>
当時の使い手は、トーマスという名だったそうだ。信憑性のない情報ですまないがな…。<br>
トーマスと言えば、もともとこの世界の存在じゃないんだろう？<br>
破壊を意味する神の名前だ。<br>
<font color=\"red\">破壊</font>か…。異世界には、破壊の神殿があるというが…ま、関係ないな。";
}
	}
	if($in{'ps_no'}==19){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="無の空間というのは。この世界のどこを探してもないのだよ。<br>
歴史は変わらない。次元を超えるという悪魔や天使なら別だが…。<br>
魂は、無に帰す。ペットの魂も、今の冒険者たちはペットを進化させるアイテム程度にしか思ってないが…<br>
やはり、無属性に帰すべきもの。<br>
そういうわけで、魂の使い道に困ったら、無に帰させてあげると良いだろう。<br>
普通のペットはこの世界に属してしまっているが…無と関係を持つものが１匹、居たはずだ。<br>
そのときは、もうひとつの無属性、すなわち君のオリジナル武器を持っていることが条件だぞ。";
}
	}
	if($in{'ps_no'}==20){
	$ran=int(rand(4));
	if($ran<3){
$jyouhou="無属性魔法…その名もギガブレイク。<br>
その使い手は、世界でも有数だ。<br>
この魔法は、全てを壊す魔法。その威力は時魔法メテオと同等、あるいはそれ以上であると言う。<br>
この魔法は、誰でも使える。ただし、壊すことが得意であるならば。<br>
この魔法は、使い方次第で更に強力になる\可\能\性\を秘めている。<br>
ただし、金貨を破壊しようなんて、大それたことを考えるんじゃないぞ。";
}
	if($ran==3){
$jyouhou="無属性魔法の修得か。<br>
これは大変面倒だろう。最低1000万…いや2000万は欲しいか…。<br>
物に宿るパワーを集めるのは、容易ではないからな。<br>
ところで、この魔法には１つの長所と、１つの特殊な使い方がある。<br>
この特殊な使い方をすると、たまに非常に高い攻撃力を発揮する。<br>
静アビリティが関係しているということだが…特別な戦いで特に有効だ。<br>";
}
	}
	if($in{'ps_no'}==21){
	$ran=int(rand(6));
	if($ran==0){
$jyouhou="黒魔法ファイガは、攻撃力を上げる黒魔法だぞ。<br>
赤色のノートやマントを装備することで、更に攻撃力の上昇をすることができるぞ。<br>
なに、今さらそんな情報要らないって！？　まぁそう言うなよ…。";
}
	if($ran==1){
$jyouhou="黒魔法ブリザガは、敵の攻撃力を下げる黒魔法だぞ。<br>
青色のノートやマントを装備することで、自身の攻撃力を上昇させることもできるぞ。<br>
なに、今さらそんな情報要らないって！？　まぁそう言うなよ…。";
}
	if($ran==2){
$jyouhou="黒魔法サンダガは、命中力を上げる黒魔法だぞ。<br>
黄色のノートやマントを装備することで、自身の攻撃力を上昇させることもできるぞ。<br>
なに、今さらそんな情報要らないって！？　まぁそう言うなよ…。";
}
	if($ran==3){
$jyouhou="黒魔法エアロガは、敵の回避を下げる黒魔法だぞ。<br>
なに、そんな黒魔法、店には売ってないって！？<br>
その通り。この魔法は発動、そして制御が非常に困難なんだ。<br>
その為に、発動を助ける装備、制御を助ける装備があるが…<br>
最低でも発動を助ける装備を持っていないといけないからな、店で売っても誰も買わないのさ。";
}
	if($ran==4){
$jyouhou="黒魔法エアロガの発動に必要な装備とは。<br>
こいつは、スカイスピアと、スカイアクスを合成させれば完成だ。<br>
必要な合成石が多いからな、金がかかるんだがな。";
}
	if($ran==5){
$jyouhou="黒魔法エアロガの制御に必要な装備とは。<br>
こいつは、まぁ、入手困難だ。<br>
冒険を続けていれば、いつかわかるだろう…。";
}
	}
	if($in{'ps_no'}==22){
	$ran=int(rand(1));
	if($ran==0){
$jyouhou="チャイナという新世界を見たという人間が居るんだ。<br>
まぁそんなこと他では聞いたことないし、どうせガセネタだろうと思うんだがね、興味深いかい？<br>
情報によると、その地に居る人たちは皆、それぞれの持つペットを愛していたそうだよ。<br>
愛し、ペットの心を理解した結果、怪しい奥義を編み出した人たちも居るらしい…。何の奥義だか知らんが…。<br>
なんでも、それらの奥義を修得する為には、とんでもないＡＰが必要だとか。<br>
ＡＰを上げる方法はそう多くは無いが…例えば、ＡＰを上げることが目的なら100回転生を利用すると良いかもな…。";
}
	}
	if(int(rand(100))==0 and $chara[135]>2){
$jyouhou.="<font size=5 color=\"red\"><b><br><br>そうそう！たった今思い出した！<br>
今回の情報とは関係ないんだが、耳よりの情報があるんだ！<br>
\噂\の\時空戦士についてなんだがよ。<br>
１０００億の費用でもって正義の剣を成長させるのが鍵らしいぜ！<br>
もし失敗して壊れちまったらショックだよなぁ…！<br>
そうそう、この情報はアンタだから教えたんだぜ？<br>
他の人にとっては意味をなさないことだからな！！</b></font>";
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
sub mem_sts {

	&chara_load;

	&chara_check;

	open(IN,"alldata.cgi");
	@member_data = <IN>;
	close(IN);
	$i=1;$hit=0;
	foreach(@member_data){
		@mem = split(/<>/);
		if($mem[4] eq $in{'taisyo'}){$hit=1;last;}
		$i++;
	}
	if($hit!=1){&error("そんなキャラ見つかりません");}
	open(IN,"./item/$mem[0].cgi");
	$mitem_log = <IN>;
	close(IN);
	@mitem = split(/<>/,$mitem_log);

	if ($mem[5]) { $esex = "男"; } else { $esex = "女"; }
	if($mem[70]!=1){$next_ex = $mem[18] * ($lv_up + $mem[37] * 150 - $mem[32] * 50);}
	else{$next_ex = $mem[18] * ($lv_up * 10 - $mem[32] * 50) * 10;}

	# 基本値算出
	$divpm = int($memmaxpm / 100);
$hit_ritu = int($mem[9] / 3 + $mem[11] / 10 + $mitem[10] / 3) + 40 + $mitem[2] + $mitem[16];
$sake = int($mem[9] / 10 + $mem[11] / 20 + $mitem[10]/10) + $mitem[5] + $mitem[17];
$waza_ritu = int(($mem[11] / 10)) + 10 + $a_wazaup;
if($waza_ritu > 90){$waza_ritu = 90;}
$hissatu_ritu = $waza_ritu + int($mem[12]/4);

	if($mitem[20]){$bukilv="+ $mitem[20]";}
	if($mitem[22]){$bogulv="+ $mitem[22]";}
	if($mem[64]==0 and $mem[65]==0){$mem[64]=50;$mem[65]=50;}

	if($mem[0] eq "jupiter"){
		$mitem[0] = "????";
		$mitem[1] = "????";
		$mitem[3] = "????";
		$mitem[4] = "????";
		$mitem[6] = "????";
		$hit_ritu = "????";
		$sake = "????";
	}

	&header;

	print <<"EOM";
<table align="center"><TR><TD><font size=5>$mem[4]さんのステータス画面</font></TD><TD>
</TD></table>
<hr size=0>
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">キャラクターデータ</td></tr>
<td rowspan="7" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$mem[6]]">
<tr><td id="td2" class="b2">武器</td><td align="right" class="b2">$mitem[0] $bukilv</td>
<td id="td2" class="b1">攻撃力</td><td align="right" class="b2">$mitem[1]</td></tr>
<tr><td id="td2" class="b2">防具</td><td align="right" class="b2">$mitem[3] $bogulv</td>
<td id="td2" class="b1">防御力</td><td align="right" class="b2">$mitem[4]</td></tr>
<tr><td id="td2" class="b2">アクセサリー</td><td align="right" class="b2">$mitem[6]</td>
<td id="td2" class="b1">連戦中連勝率</td><td align="right" class="b2">$mem[20]</td></tr>
<tr>
<td id="td2" class="b2">現在の世界</td><td align="center" class="b2">
EOM
if($mem[140]==2){print "イエローワールド</td>";}
elsif($mem[140]==3){print "レッドワールド</td>";}
elsif($mem[140]==4){print "ドラゴンワールド</td>";}
elsif($mem[140]==5){print "天界</td>";}
else{print "ジュピタワールド</td>";}
print "<td id=\"td2\" class=\"b2\">鍵</td><td align=\"center\" class=\"b2\">";
if($mem[131]){print "イエローワールド<br>";}
if($mem[132]){print "レッドワールド<br>";}
if($mem[133]){print "ドラゴンワールド<br>";}
if($mem[315]){print "天界<br>";}
	print <<"EOM";
</td></table>
<td valign=top width='50%'>
<table width="100%"><tr>
<tr><td id="td1" colspan="5" class="b2" align="center">ペットデータ</td></tr>
<td rowspan="7" align="center" valign=bottom class="b2"><img src="$img_path_pet/$egg_img[$mem[45]]">
<tr><td id="td2" class="b2">種</td><td align="center" class="b2">$mem[39]</td>
<td id="td2" class="b2">名前</td><td align="center" class="b2">$mem[138]</td>
</tr>
<tr>
<td id="td2" class="b2">HP</td><td align="center" class="b2">$mem[42]\/$mem[43]</td>
<td id="td2" class="b2">攻撃力</td><td align="center" class="b2">$mem[44]</td>
</tr>
<tr>
<td id="td2" class="b2">ペットレベル</td><td align="center" class="b2">$mem[46]</td>
<td id="td2" class="b2">ペット経験値</td><td align="center" class="b2">$mem[40]\/$mem[41]</td>
</tr>
</td>
</tr></table></td>

<table width='50%'>
<tr><td id="td1" colspan="5" class="b2" align="center">ステータス</td></tr>
<tr>
<td class="b1" id="td2">なまえ</td><td class="b2">$mem[4]</td>
<td class="b1" id="td2">性別</td><td class="b2">$esex</td></tr>
<tr><td class="b1" id="td2">善良度</td><td class="b2">$mem[64]</td>
<td id="td2" class="b1">悪人度</td><td class="b2"><b>$mem[65]</b></td></tr>
<tr><td class="b1" id="td2">ジョブ</td><td class="b2">$mem_syoku[$mem[14]]</td>
<td id="td2" class="b1">ジョブLV</td><td class="b2"><b>$mem[33]</b></td></tr>
<tr><td class="b1" id="td2">レベル</td><td class="b2">$mem[18]</td>
<td class="b1" id="td2">経験値</td><td class="b2">$mem[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$mem[15]\/$mem[16]</td>
<td class="b1" id="td2">お金</td><td class="b2">$mem[19]</td></tr>
<tr><td class="b1" id="td2">STR</td><td align="left" class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$mem[7] + $mitem[8]</b></td>
<td class="b1" id="td2">INT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$mem[8] + $mitem[9]</b></td></tr>
<tr><td class="b1" id="td2">DEX</td><td align="left" class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$mem[9] + $mitem[10]</b></td>
<td class="b1" id="td2">VIT</td><td align="left" class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$mem[10] + $mitem[11]</b></td></tr>
<tr><td class="b1" id="td2">LUK</td><td align="left" class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$mem[11] + $mitem[12]</b></td>
<td class="b1" id="td2">EGO</td><td align="left" class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$mem[12] + $mitem[13]</b></td></tr>
<tr><td id="td2" class="b2">命中率</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu</b></td>
<td id="td2" class="b2">回避率</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$sake</b></td></tr>
<tr>
<td id="td2" class="b2">会心率</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $mitem[17]%</b></td>
<td id="td2" class="b2">必殺率</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhissatu height=$bh><br><b>$hissatu_ritu + $mitem[17]%</b></td></tr>
<tr>
<td id="td2" class="b2">称号</td><td align="left" class="b2"><font color="$yellow">$shogo[$mem[32]]</font></td>
<td id="td2" class="b2">ギルド</td><td align="left" class="b2">$mem[66]</td>
</tr>
<tr>
<td id="td2" class="b2">転生回数</td><td align="left" class="b2">$mem[37]</td>
<td id="td2" class="b2">レベル順位</td><td align="left" class="b2">$i位</td>
</tr>
</table>
</table>
<hr size=0>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}