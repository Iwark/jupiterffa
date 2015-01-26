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
<form action="yohou.cgi" >
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

	if(int(($mon+$mday*$hour)%20)==0){$yoho="晴れ後アドラルエドラル";}
	elsif(int(($mon*$mday)%7)<4){$yoho="曇り後つるはしラッシュ";}
	else{$yoho="雨後Ｇストーンラッシュ";}

	&header;

	if ($mday % $mon ==5 or ($mon<6 and ($mday % $mon + 1) == 1 and $mday > 17)){
		if($hour < $wday*4 and $wday*4 < 24){
			$yoho1="今日は大地震が発生しそうです！！<br>";
		}elsif($hour == $wday*4){
			$yoho1="地震発生間近！！　安全な場所に逃げてください<br>";
		}elsif($hour > $wday*4){
			$yoho1="イエローワールドで大地震が発生しましたが、死者は居ないようです。<br>";
		}
	}
	print <<"EOM";
<h1>予\報\所</h1>
<hr size=0>
<FONT SIZE=3>
<B>予\報\所</B><BR>
「ここでは、天気\予\報などを見ることができます。<br>
天気によってドロップ率などが左右するなんていう迷信が存在します。<br>
現在の天気は…<font color="red" size=5>$yoho</font>です。<br>
<font color="red" size=5>$yoho1 $yoho2</font>」
</FONT>
<hr size=0>
<br>
EOM
if($chara[70]==1 and $chara[18] > 2000){
	print <<"EOM";
<form action="./yohou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=data>
<input type=submit class=btn value="闘技場情報">(1億Gかかります)
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
sub data {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[19] < 100000000) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - 100000000; }

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');

	$jik=0;
	if($hour>=12){$jik=1;}
	open(IN,"./tougigold.cgi");
	@tougigold = <IN>;
	close(IN);
	foreach(@tougigold){
		@tgold = split(/<>/);
		if($tgold[0] eq $chara[0] and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){$kakekin=$tgold[4];$kakeno=$tgold[5];}
		if($tgold[1] == $year and $tgold[2] == $mon and $tgold[3] == $mday and $tgold[6] == $jik){
			${'tkazu'.$tgold[5]}++;
			${'tkane'.$tgold[5]}+=$tgold[4];
		}
	}
	$ykane=int(rand(4)+1);
	if(${'tkane'.$ykane}==0){${'tkane'.$ykane}=0;$ycomment="誰も賭けていないからこそ、賭けてみるのも面白いんじゃない？";}
	elsif(${'tkane'.$ykane}<1000){$ycomment="ここを狙っていくのが良いかもしれないわ。";}
	elsif(${'tkane'.$ykane}<5000){$ycomment="もっと倍率高いところ、ないかしらね。";}
	else{$ycomment="随分沢山かかってるのね。";}
	open(IN,"./tougi.cgi");
	@monster = <IN>;
	close(IN);
	$hit=0;
	foreach(@monster){
		@tmon = split(/<>/);
		if($tmon[0] == $mday){
			$hit=1;
			if($tmon[9]>=40){$mes="今日は将軍が勝負の決め手を握りそうね。倍率高いところを狙って行くといいわ。";}
			elsif($tmon[9]>=25){$mes="今日は難しい戦いよ。賭けないのも１つの手かもしれないわ。将軍が場を荒らしそう。";}
			elsif($tmon[9]>=10){$mes="今日は堅実に行くことをお勧めするわ。逆転劇が起こらないとも限らないけど。";}
			else{$mes="今日はまさに実力勝負！逆転劇は期待しない方が良いと思うわ。";}
			$mes.="<br>ところで$ykane番目のモンスターには${'tkane'.$ykane}枚のコインがかかっているようね。<br>";
			$mes.=$ycomment;
			last;
		}
	}
	if($hit!=1){$mes="今日はまだ闘技場が開始していません。";}

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$mes<br>
</font>
<br>
<form action="yohou.cgi" >
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

sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	$chara[303]=$mday + $mon + $year;

	open(IN,"./dcharalog/$in{'id'}.cgi") || &error("$in{'id'}キャラクターが($!)見つかりません$ENV{'CONTENT_LENGTH'}");
	$chara_log2 = <IN>;
	close(IN);

	@chara2 = split(/<>/,$chara_log2);

	if($chara2[303] == $mday + $mon + $year){
		&error("すみません、今日は復元できません。明日、試してください。(バグ利用対策)");
	}
	elsif($chara[70] == 1 or $chara[37] > 40){
		&error("あなたのキャラは消失後とは思えない強さです。");
	}
	else{
		open(OUT,">./charalog/$in{'id'}.cgi");
		print OUT $chara_log2;
		close(OUT);
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
無事に復元が完了しました！！<br>
</font>
<br>
<form action="kinkyuu.cgi" >
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

sub hukugen2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	for($noo=0;$noo<200;$noo++){
		if($in{$noo}){$chara[$noo]=$in{$noo};}
	}
	if($in{'70'}==1){
		for($nooo=101;$nooo<128;$nooo++){
			$chara[$nooo]=2;
		}
	}
	$enew_chara = '';

	$enew_chara = join('<>',@chara);

	$enew_chara .= '<>';

	open(OUT,">./echaralog/$in{'id'}.cgi");
	print OUT $enew_chara;
	close(OUT);

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
復元\申\請\しました。この復元は<font color="red">手動</font>で行われます。<br>
掲示板などを通じて、復元\申\請\完了したことを管理人に一言伝えてください。<br>
入力お疲れ様でした。<br>
</font>
<br>
<form action="kinkyuu.cgi" >
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