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
<form action="akuma.cgi" >
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

	&header;

	$test=0;
	if($chara[0] eq "jupiter"){$test=1;}
	$taisei=$chara[135]+1;
	if($taisei>30){$taisei=30;}
	print <<"EOM";
<h1>悪魔の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>悪魔の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
「ガハハハハハ、ようこそ悪魔の館へ！<br>
ここから、<font color="red">土曜日と日曜日のみ</font>１日１回まで悪魔界に突入できるぞガハハハ！<br>
始めに言っておくが、悪魔界は耐性の無い者にはとても耐え切れないフィールドだ。<br>
どんなに屈強でも、同じこと。今のおぬしは<font color="red" size="5">$taisei</font>ターンぐらいなら耐えられるだろうな。<br>
悪魔達の持つアイテムは凄くレアだが、狙うにしても覚悟して挑むことだなガハハハ！<br>
まぁ悪魔界に挑戦する前に、まずは悪魔界をシミュレートした『仮想悪魔界１F～７F』で耐性を付けると良いだろう。<br>
仮想と言っても一応本物の悪魔なんだがなガハハ！落ちこぼれで、マテリア元素はドロップできないぞ！ガハハ！<br>
なお、悪魔界に挑戦できるのは１０秒に１回までで、仮想で１回も倒せないようだと挑戦は認められないな。<br>
EOM
if($chara[146]>0){
	print <<"EOM";
<br><font color="red" size=4>お、悪魔界チケットを$chara[146]枚持ってるのか！そいつがあれば、いつでも挑戦できるぜ～ガハハハハ！</font>
EOM
}
if($wday==2){
	print <<"EOM";
<br><font color="red" size=4>火曜日は気分が良い、チケットが無くても特別に10億Ｇで悪魔界への突入を許可しようガハハハハ！</font>
EOM
}
	print <<"EOM";
」
</FONT>
<hr size=0>
<br>

<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=1>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界１Fに挑戦する">
</form>
EOM
if($chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=2>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界２Fに挑戦する">
</form>
EOM
}
if($chara[135]>=2){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=3>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界３Fに挑戦する">
</form>
EOM
}
if($chara[135]>=3){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=4>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界４Fに挑戦する">
</form>
EOM
}
if($chara[135]>=4){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=5>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界５Fに挑戦する">
</form>
EOM
}
if($chara[135]>=5){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=6>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界６Fに挑戦する">
</form>
EOM
}
if($chara[135]>=6){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=7>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="仮想悪魔界７Fに挑戦する">
</form>
EOM
}
if($chara[304]==1 or $chara[304]==2 or $chara[0] eq "jupiter"){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc>
<input type=submit class=btn value="悪魔界に突入する">
</form>
EOM
}elsif(time()-$chara[314]>=10 and $chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=8>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="悪魔界に突入する">
</form>
EOM
}
if($chara[304]==4 or $chara[304]==5){
if(time()-$chara[314]>=10 and $chara[135]>=1){
	print <<"EOM";
<form action="./akumavs.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=boss_file value=9>
<input type=hidden name=mode value=abattle>
<input type=submit class=btn value="悪魔界の奥へ進む">
</form>
EOM
}
}
if($chara[128]>=5 and $chara[135]>=4 and !$chara[304]){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yuwaku>
<input type=submit class=btn value="悪魔の頼み事">
</form>
EOM
}
if($chara[304]==3){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yuwaku2>
<input type=submit class=btn value="報酬を受け取る">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub yuwaku {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>悪魔の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>悪魔の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
「お、おぬし、中々強いな・・・。実は頼み事があるんだ…。<br>
天界から悪魔界に放たれたアンクドラルという使者が強すぎるんだ…。<br>
ヤツを止めることが出来たら、４種の元素を40個ずつあげようと思うんだが…。」<br><br>
</FONT>
<hr size=0>
<br>
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yes>
<input type=hidden name=yes value=1>
<input type=submit class=btn value="引き受ける">
</form>
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=yes>
<input type=hidden name=yes value=2>
<input type=submit class=btn value="引き受けない">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub yuwaku2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[304] !=3 ){&error("ERROR!");}

		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$isi[29]+=40;
		$isi[30]+=40;
		$isi[31]+=40;
		$isi[32]+=40;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
	$chara[304]=5;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>悪魔の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>悪魔の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
「よくやってくれたな、お礼の元素セットだ！」<br><br>
<font color="red" size=5>火、水、闇、光の元素を40個ずつ手に入れた！</font>
</FONT>
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub yes {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	if($chara[304]>0){&error("既に選択しましたよ。");}

	&get_host;

	$chara[304]=$in{'yes'};

	if($in{'yes'}==1){
		$com="じゃぁ、頼んだぜ！！";
	}else{
		$com="ちっ、貴様にはもう頼まん。";
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>悪魔の館</h1>
<hr size=0>
<FONT SIZE=3>
<B>悪魔の使者</B><BR>
<IMG SRC="$img_path_t/$chara_img_t[239]"><br>
「$com」<br><br>
</FONT>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub anc {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>悪魔界</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「やはり来たか、$chara[4]。<br>
巨大なエネルギーを感じるな・・・悪魔界王はまだ遠いはずだが…。<br>
ここから先は、悪魔界でも極めて危険なフィールドに属すだろう。<br>
正直、この私でも、一歩先には死が待っているかもしれない・・・来るか？<br>
」<br><br>
</FONT>
<hr size=0>
<br>
EOM
if($chara[304]==1){
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc1>
<input type=submit class=btn value="アンクドラルに襲い掛かる">
</form>
EOM
}else{
	print <<"EOM";
<form action="./akuma.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=anc2>
<input type=submit class=btn value="ついていく">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub anc1 {

	&chara_load;

	&chara_check;

	$chara[304]=3;
	&chara_regist;

	&header;

	print <<"EOM";
<h1>悪魔界</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「何をする、$chara[4]！？<br>
<br>
ぐふっ。不覚・・・。」<br><br>
<font color="red" size=5>アンクドラルに致命傷を負わせた！</font>
</FONT>
<br><br><br><br>
そしてアンクドラルは消えた・・・。
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub anc2 {

	&chara_load;

	&chara_check;

	$chara[304]=4;
	&chara_regist;

	&header;

	print <<"EOM";
<h1>悪魔界</h1>
<hr size=0>
<FONT SIZE=3>
<B>アンクドラル</B><BR>
<IMG SRC="$img_path_t/$chara_img[185]"><br>
「ぐふっ。不覚・・・。」<br><br>
<font color="red" size=5>銀髪の剣士が飛んできてアンクドラルに襲いかかった！<br>
アンクドラルは致命傷を負った！</font>
</FONT>
<br><br><br><br>
そしてアンクドラルと銀髪の剣士は消えてしまった・・・。<br>
$chara[4]は仕方なく町に戻ることにした・・・。<br>
<hr size=0>
<br>
EOM

	&shopfooter;

	&footer;

	exit;
}