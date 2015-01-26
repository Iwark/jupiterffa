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
<form action="koubou.cgi" >
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

&haigo;

&error;

exit;

#----------#
#  配合所  #
#----------#
sub haigo {

	&chara_load;

	&chara_check;

	&item_load;

	if($chara[70]<1){&error("エラー");}

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	if($item[20]){$bukilv="+ $item[20]";}
	if($item[22]){$bogulv="+ $item[22]";}
	if(!$chara[98]){$chara[98]=0;}
	if(!$chara[99]){$chara[99]=0;}
	&header;

	print <<"EOM";
<h1>工房</h1>
<hr size=0>
<FONT SIZE=3>
<B>工房のおじさん</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここが何の場所か知っているか・・・<br>
知らずに利用するのは得とは言えんな。<br>
ここでは、特殊な装備を作ることが可\能\だ。」
</FONT>
<br>現在の所持金：$chara[19] Ｇ
<br>合成石の所持：$chara[99] 個
<br><hr>現在の装備<br>
<table>
<tr>
<td id="td2" class="b2">武器</td><td align="right" class="b2">$item[0] $bukilv</td>
<td id="td2" class="b2">攻撃力</td><td align="right" class="b2">$item[1]</td>
</tr>
<tr>
<td id="td2" class="b2">防具</td><td align="right" class="b2">$item[3] $bogulv</td>
<td id="td2" class="b2">防御力</td><td align="right" class="b2">$item[4]</td>
</tr>
</table>
<table width = "100%">
<tr>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="item_soubi">
<td width = "25%" align = "center" valign = "top">
本体（武器）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>価格</th></tr>
EOM
	$i = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
EOM
if($ino==1400){
		print << "EOM";
×
EOM
}else{
		print << "EOM";
<input type=radio name=item_no1 value="$i">
EOM
}
		print << "EOM";
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
対象（武器）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>攻撃力</th><th nowrap>価格</th></tr>
EOM
	$g = 0;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibuki="+ $ilv";}else{$ibuki="";}
		print << "EOM";
<tr>
<td class=b1 align="center">
EOM
if($ino==1400){
		print << "EOM";
×
EOM
}else{
		print << "EOM";
<input type=radio name=item_no2 value="$g">
EOM
}
		print << "EOM";
</td>
<td class=b1 nowrap>$iname $ibuki</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$g++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
本体（防具）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>価格</th></tr>
EOM
	$d = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defd=$d+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$defd">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$d++;
	}
		print << "EOM";
</table>
</td>
<td width = "25%" align = "center" valign = "top">
対象（防具）
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>防御力</th><th nowrap>価格</th></tr>
EOM
	$e = 0;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
		if($ilv){$ibogu="+ $ilv";}else{$ibogu="";}
		$defe = $e+100;
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$defe">
</td>
<td class=b1 nowrap>$iname $ibogu</td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$e++;
	}
		print << "EOM";
</table>
</td>
<table>
<br><br>
<input type=submit class=btn value="合成する">
</table>
</form>
</table>
<table>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=submit class=btn value="合成石を買うぜっ(1億Ｇ)">
</form>
</table>
<table>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=1>
<input type=submit class=btn value="６個セットのお買い得パックを買う(5億Ｇ)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=2>
<input type=submit class=btn value="30個セットのお買い得パックを買う(24億Ｇ)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=3>
<input type=submit class=btn value="100個セットのお買い得パックを買う(75億Ｇ)">
</form>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="gouseiseki">
<input type=hidden name=tokutoku value=4>
<input type=submit class=btn value="300個セットのお買い得パックを買う(200億Ｇ)">
</form>
</table>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub item_soubi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	$chara[26] = $host;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	if($in{'item_no1'} > 99){
		$item_no1 = $in{'item_no1'} - 100;
		$souko_def[$item_no1] =~ s/\n//g;
		$souko_def[$item_no1] =~ s/\r//g;
		($ino1,$iname1,$idmg1,$igold1,$ihit1,$ilv1,$iexp1) = split(/<>/,$souko_def[$item_no1]);
	}else{
		$item_no1 = $in{'item_no1'};
		$souko_item[$item_no1] =~ s/\n//g;
		$souko_item[$item_no1] =~ s/\r//g;
		($ino1,$iname1,$idmg1,$igold1,$ihit1,$ilv1,$iexp1) = split(/<>/,$souko_item[$item_no1]);
	}
	if($in{'item_no2'} > 99){
		$item_no2 = $in{'item_no2'} - 100;
		$souko_def[$item_no2] =~ s/\n//g;
		$souko_def[$item_no2] =~ s/\r//g;
		($ino2,$iname2,$idmg2,$igold2,$ihit2,$ilv2,$iexp2) = split(/<>/,$souko_def[$item_no2]);
	}else{
		$item_no2 = $in{'item_no2'};
		$souko_item[$item_no2] =~ s/\n//g;
		$souko_item[$item_no2] =~ s/\r//g;
		($ino2,$iname2,$idmg2,$igold2,$ihit2,$ilv2,$iexp2) = split(/<>/,$souko_item[$item_no2]);
	}
	if($item_no1 == $item_no2){&error("同じアイテムです。");}
	if($iname1 eq "エ\ッ\グ\ソ\ー\ド" and $iname2 eq "ス\ピ\ス\ソ\ー\ド"){
		$mes = "おお、素晴らしい組み合わせだっ。これは良い物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は３個だ。挑戦するかいっ？";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1173;
		}else{
			$it_no = 1174;
		}
	}elsif($iname1 eq "マシンガン" and $iname2 eq "キラーボウ"){
		$mes = "おー。これはこれは。良い組みあわせだね。<br>";
		$mes.= "必要な合成石は4個だ。挑戦するかいっ？";
		$gouseiseki=4;
		if(int(rand(3))==0){
			$it_no = 1176;
		}else{
			$it_no = 1177;
		}
	}elsif($iname1 eq "タミフル" and $iname2 eq "キングナイフ"){
		$mes = "まぁまぁの組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は3個だ。挑戦するかいっ？";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1179;
		}else{
			$it_no = 1180;
		}
	}elsif($iname1 eq "スピア" and $iname2 eq "剛剣"){
		$mes = "まぁまぁの組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は3個だ。挑戦するかいっ？";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 1182;
		}else{
			$it_no = 1183;
		}
	}elsif($iname1 eq "昇竜烈剣" and $iname2 eq "昇竜剣"){
		$mes = "なんというか、レベルが上がりそうな組み合わせだな。<br>";
		$mes.= "必要な合成石は4個だ。挑戦するかいっ？";
		$gouseiseki=4;
		if(int(rand(3))==0){
			$it_no = 1185;
		}else{
			$it_no = 1186;
		}
	}elsif($iname1 eq "モーゼの杖" and $iname2 eq "エルフィンボウ"){
		$mes = "まぁまぁの組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は5個だ。挑戦するかいっ？";
		$gouseiseki=5;
		if(int(rand(3))==0){
			$it_no = 1188;
		}else{
			$it_no = 1189;
		}
	}elsif($iname1 eq "悪霊剣" and $iname2 eq "小竜剣"){
		$mes = "ひぇー。おそろしい武器ができそうだ。<br>";
		$mes.= "必要な合成石は15個だ。挑戦するかいっ？";
		$gouseiseki=15;
		if(int(rand(3))==0){
			$it_no = 1191;
		}else{
			$it_no = 1192;
		}
	}elsif($iname1 eq "時雨剣" and $iname2 eq "最強剣"){
		$mes = "おいおい、もったいねぇな。こんな強い剣を！？<br>";
		$mes.= "必要な合成石は20個だ。挑戦するかいっ？";
		$gouseiseki=20;
		if(int(rand(3))==0){
			$it_no = 1194;
		}else{
			$it_no = 1195;
		}
	}elsif($iname1 eq "論刀" and $iname2 eq "幻の剣"){
		$mes = "予測のつかない組み合わせだな。良い物ができるといいなっ<br>";
		$mes.= "必要な合成石は10個だ。挑戦するかいっ？";
		$gouseiseki=10;
		if(int(rand(3))==0){
			$it_no = 1170;
		}else{
			$it_no = 1170;
		}
	}elsif($iname1 eq "帝王双烈剣" and $iname2 eq "成仏鎌"){
		$mes = "これ以上の組み合わせなどこの世に存在しない。<br>";
		$mes.= "必要な合成石は50個だ。挑戦するかいっ？";
		$gouseiseki=50;
		if(int(rand(3))==0){
			$it_no = 1197;
		}else{
			$it_no = 1198;
		}
	}elsif($iname1 eq "普通の盾" and $iname2 eq "ミネルバビスチェ"){
		$mes = "まぁまぁの組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は3個だ。挑戦するかいっ？";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 2152;
		}else{
			$it_no = 2153;
		}
	}elsif($iname1 eq "闇封じの剣" and $iname2 eq "闇の羽衣"){
		$mes = "良いセンスしてるな。<br>";
		$mes.= "必要な合成石は5個だ。挑戦するかいっ？";
		$gouseiseki=5;
		if(int(rand(3))==0){
			$it_no = 2155;
		}else{
			$it_no = 2156;
		}
	}elsif($iname1 eq "竜骨剣" and $iname2 eq "竜骨盾"){
		$mes = "良いセンスしてるな。<br>";
		$mes.= "必要な合成石は6個だ。挑戦するかいっ？";
		$gouseiseki=6;
		if(int(rand(3))==0){
			$it_no = 2158;
		}else{
			$it_no = 2159;
		}
	}elsif($iname1 eq "武人の鎧" and $iname2 eq "黒装束"){
		$mes = "まぁまぁの組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は3個だ。挑戦するかいっ？";
		$gouseiseki=3;
		if(int(rand(3))==0){
			$it_no = 2161;
		}else{
			$it_no = 2162;
		}
	}elsif($iname1 eq "源氏の鎧" and $iname2 eq "銀の胸当て"){
		$mes = "どーだか。あんまよさそうじゃないぜ<br>";
		$mes.= "必要な合成石は2個だ。挑戦するかいっ？";
		$gouseiseki=2;
		if(int(rand(3))==0){
			$it_no = 2164;
		}else{
			$it_no = 2165;
		}
	}elsif($iname1 eq "英雄怒服" and $iname2 eq "黒帯3000"){
		$mes = "良い組み合わせだな。良物ができるとみるぜっ<br>";
		$mes.= "必要な合成石は7個だ。挑戦するかいっ？";
		$gouseiseki=7;
		if(int(rand(3))==0){
			$it_no = 2167;
		}else{
			$it_no = 2168;
		}
	}elsif($iname1 eq "ヒーロースーツ" and $iname2 eq "ライダースーツ"){
		$mes = "なんて良い組み合わせだ！期待しなっ<br>";
		$mes.= "必要な合成石は10個だ。挑戦するかいっ？";
		$gouseiseki=10;
		if(int(rand(3))==0){
			$it_no = 2170;
		}else{
			$it_no = 2171;
		}
	}elsif($iname1 eq "屋敷剣" and $iname2 eq "屋敷鎧"){
		$mes = "ふむ。吉と出るか凶と出るか…<br>";
		$mes.= "必要な合成石は8個だ。挑戦するかいっ？";
		$gouseiseki=8;
		if(int(rand(3))==0){
			$it_no = 2173;
		}else{
			$it_no = 2174;
		}
	}elsif($iname1 eq "スーパースーツ" and $iname2 eq "大屋敷鎧"){
		$mes = "おいおい。度胸あるな。成功すれば天国だが。<br>";
		$mes.= "必要な合成石は25個だ。挑戦するかいっ？";
		$gouseiseki=25;
		if(int(rand(3))==0){
			$it_no = 2176;
		}else{
			$it_no = 2177;
		}
	}elsif($iname1 eq "キュウリ" and $iname2 eq "封魔の鎧"){
		$mes = "これ以上の組み合わせは無いぞっ。神にでもなるつもりか？<br>";
		$mes.= "必要な合成石は50個だ。挑戦するかいっ？";
		$gouseiseki=50;
		if(int(rand(3))==0){
			$it_no = 2179;
		}else{
			$it_no = 2180;
		}
	}elsif($iname1 eq "アルテマスーツ" and $iname2 eq "小物鎌"){
		$mes = "ｆｍ・・・合成のベースは弱いが・・・面白いな。というか見たこと無い組み合わせだな。<br>";
		$mes.= "結果が知りたい。特別に合成石1個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2228;
		}else{
			$it_no = 2229;
		}
	}elsif($iname1 eq "降竜服" and $iname2 eq "強い槍"){
		$mes = "ｆｍ・・・合成のベースは弱いが・・・面白いな。というか見たこと無い組み合わせだな。<br>";
		$mes.= "結果が知りたい。特別に合成石1個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2231;
		}else{
			$it_no = 2232;
		}
	}elsif($iname1 eq "情報その１０" and $iname2 eq "10億剣"){
		$mes = "ｆｍ・・・合成のベースは弱いが・・・面白いな。というか見たこと無い組み合わせだな。<br>";
		$mes.= "結果が知りたい。特別に合成石1個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 2234;
		}else{
			$it_no = 2235;
		}
	}elsif($iname1 eq "デスペナルティ" and $iname2 eq "天罰の杖"){
		$mes = "ｆｍ・・・合成のベースは弱いが・・・面白いな。というか見たこと無い組み合わせだな。<br>";
		$mes.= "結果が知りたい。特別に合成石1個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 1228;
		}else{
			$it_no = 1229;
		}
	}elsif($iname1 eq "ルール砲" and $iname2 eq "リミッター"){
		$mes = "ｆｍ・・・合成のベースは弱いが・・・面白いな。というか見たこと無い組み合わせだな。<br>";
		$mes.= "結果が知りたい。特別に合成石1個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1;
		if(int(rand(3))==0){
			$it_no = 1231;
		}else{
			$it_no = 1232;
		}
	}elsif($iname1 eq "モーゼルフィン" and $iname2 eq "霧弓"){
		$mes = "うむ。良い感じの組み合わせだな。<br>";
		$mes.= "合成石20個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=20;
		if(int(rand(3))==0){
			$it_no = 1234;
		}else{
			$it_no = 1235;
		}
	}elsif($iname1 eq "時空神剣" and $iname2 eq "時空真剣"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1237;
		}else{
			$it_no = 1238;
		}
	}elsif($iname1 eq "正義の棍棒"){
		$mes = "あっはっは。失敗しちまったようだな！<br>";
		$mes.= "合成石100個でもう一度挑戦してやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1237;
		}else{
			$it_no = 1238;
		}
	}elsif($iname1 eq "げっちゅう" and $iname2 eq "ペットニウム"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1242;
		}else{
			$it_no = 1243;
		}
	}elsif($iname1 eq "時空神鎧" and $iname2 eq "時空真服"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 2237;
		}else{
			$it_no = 2238;
		}
	}elsif($iname1 eq "正義の金槌" and $iname2 eq "正義の鉄拳"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1240;
		}else{
			$it_no = 1240;
		}
	}elsif($iname1 eq "正義の盾" and $iname2 eq "正義の冠"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 2240;
		}else{
			$it_no = 2240;
		}
	}elsif($iname1 eq "ウデフラ刀" and $iname2 eq "ジャバーナ刀"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		if(int(rand(3))==0){
			$it_no = 1170;
		}else{
			$it_no = 1170;
		}
	}elsif($iname1 eq "ツデアックス" and $iname2 eq "シャドーナイフ"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石150個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=150;
		if(int(rand(3))==0){
			$it_no = 1194;
		}else{
			$it_no = 1194;
		}
	}elsif($iname1 eq "エグジェソ\ード" and $iname2 eq "オメジャスタッフ"){
		$mes = "つるはしができそうだな<br>";
		$mes.= "合成石200個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=200;
		if(int(rand(3))==0){
			$it_no = 1341;
		}else{
			$it_no = 1341;
		}
	}elsif($iname1 eq "時空カブト" and $iname2 eq "正義のマント"){
		$mes = "別次元の装備が生まれそうだな<br>";
		$mes.= "合成石100個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=100;
		$it_no = 2246;
	}elsif($iname1 eq "スカイスピア" and $iname2 eq "スカイアクス"){
		$mes = "この気配…エアロガか…。懐かしいな…。<br>";
		$mes.= "合成石1500個でやってやるぞ。挑戦するかいっ？";
		$gouseiseki=1500;
		$it_no = 1356;
	}elsif($iname1 eq $iname2){
		$gouseiseki=1;
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
			if($iname1 eq $si_name){$hit=1;last;}
		}
		if($hit!=1){
			foreach(@log_def){
				($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
				if($iname1 eq $si_name){$hit=2;last;}
			}	
		}
		if($hit==1 and $si_no > 1172){
			$mes = "特殊同名合成か・・・。特殊同名合成は実行できない可能性が高い。<br>";
			$mes.= "試してやってもいいが…。成功したら合成石1個を貰おう。挑戦するかいっ？";
			$it_no = $si_no - 1;
		}elsif($hit==2 and $si_no > 2151){
			$mes = "特殊同名合成か・・・。特殊同名合成は実行できない可\能\性が高い。<br>";
			$mes.= "試してやってもいいが…。成功したら合成石1個を貰おう。挑戦するかいっ？";
			$it_no = $si_no - 1;
		}else{
			$mes = "<font color=\"red\" size=5>$iname1と$iname2の組み合わせはダメだ。";
			$mes.= "今すぐやめなさい。<br></font>必要な合成石は１個だ。挑戦するかいっ？";
			if($in{'item_no1'} > 99){
				if(int(rand(2))==0){
					$it_no = 2001 + int(rand(75));
				}else{
					$it_no = 2091 + int(rand(10));
				}
			}else{
				if(int(rand(2))==0){
					$it_no = 1001 + int(rand(75));
				}else{
					$it_no = 1091 + int(rand(10));
				}
			}
		}
	}else{
		$mes = "<font color=\"red\" size=5>$iname1と$iname2の組み合わせはダメだ。今すぐやめなさい<br>";
		$mes.= "</font>必要な合成石は１個だ。挑戦するかいっ？";
		$gouseiseki=1;
		if($in{'item_no1'} > 99){
			if(int(rand(2))==0){
				$it_no = 2001 + int(rand(75));
			}else{
				$it_no = 2091 + int(rand(10));
			}
		}else{
			if(int(rand(2))==0){
				$it_no = 1001 + int(rand(75));
			}else{
				$it_no = 1091 + int(rand(10));
			}
		}
	}

if (!$in{'kakunin'}){
	&unlock($lock_file,'SI');
	&header;
	print << "EOM";
<center>
<h3>工房のおっさん「$mes」</h3>
<form action="koubou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=item_no1 value="$in{'item_no1'}">
<input type=hidden name=item_no2 value="$in{'item_no2'}">
<input type=hidden name=kakunin value="1">
<input type=hidden name=mode value="item_soubi">
<input type=submit class=btn value="挑戦する">
</form>
</center>
EOM
	$new_chara = $chara_log;
	&shopfooter;
	&footer;
	exit;
}
	open(IN,"$def_file");
	@log_def = <IN>;
	close(IN);

	open(IN,"$item_file");
	@log_item = <IN>;
	close(IN);

	if($chara[99]<$gouseiseki){&error("合成石が$gouseiseki個必要です$back_form");}
	else{$chara[99]-=$gouseiseki;}

	$hit=0;
	foreach(@log_item){
		($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
		if($it_no == $si_no){$hit=1;last;}
	}
	if($hit!=1){
	foreach(@log_def){
		($si_no,$si_name,$si_dmg,$si_gold,$si_hit) = split(/<>/);
		if($it_no == $si_no){$hit=2;last;}
	}
	}
	if($hit!=1 and $hit!=2){&error("その組み合わせは特殊な為、合成できません。");}

	if($in{'item_no1'} > 99){
		if($hit==1){
			$souko_def[$item_no1] = ();
			$souko_item[$item_no2] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}elsif($in{'item_no2'} > 99){
			$souko_def[$item_no2] = ();
			$souko_def[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}else{
			$souko_item[$item_no2] = ();
			$souko_def[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}
	}elsif($in{'item_no2'} > 99){
		if($hit==1){
			$souko_def[$item_no2] = ();
			$souko_item[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}else{
			$souko_item[$item_no1] = ();
			$souko_def[$item_no2] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
		}
	}else{
		$souko_item[$item_no2] = ();
		$souko_item[$item_no1] = "$si_no<>$si_name<>$si_dmg<>$si_gold<>$si_hit<>0<>0<>\n";
	}

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	&unlock($lock_file,'SI');

	&item_regist;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$si_nameができました</B><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub gouseiseki {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'tokutoku'}==1){
		if($chara[19]<500000000){&error("お金が足りません$back_form");}
		else{$chara[19]-=500000000;}
		$chara[99]+=6;	
	}elsif($in{'tokutoku'}==2){
		if($chara[19]<2400000000){&error("お金が足りません$back_form");}
		else{$chara[19]-=2400000000;}
		$chara[99]+=30;	
	}elsif($in{'tokutoku'}==3){
		if($chara[19]<7500000000){&error("お金が足りません$back_form");}
		else{$chara[19]-=7500000000;}
		$chara[99]+=100;	
	}elsif($in{'tokutoku'}==4){
		if($chara[19]<20000000000){&error("お金が足りません$back_form");}
		else{$chara[19]-=20000000000;}
		$chara[99]+=300;	
	}else{
		if($chara[19]<100000000){&error("お金が足りません$back_form");}
		else{$chara[19]-=100000000;}
		$chara[99]+=1;
	}

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>合成石を買いました</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}