#!/usr/local/bin/perl

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
<form action="sosiki.cgi" >
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

&item_view;

exit;

#----------------#
#  アイテム表示  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&header;

if($chara[63]>=1){&error("刑務所に入っています。");}

	print <<"EOM";
<h1>謎の組織</h1>
<hr size=0>
EOM
if($chara[65]==100){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう！！英雄$chara[4]じゃねぇか！！<br>
ついに、極悪人になったみたいだな！<br>
その体なら、可\能\だぜ。なりたいんだろ？大魔王に。<br>
俺が、お前を、大魔王にしてやるぜ。<br>
今なっているジョブをマスターして、英雄の証となるものを装備してこいよ。」
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=43>
<input type=submit class=btn value="大魔王になる">
</form>
EOM
}elsif($chara[64]==100){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう！！英雄$chara[4]じゃねぇか！！<br>
ついに、超善人になったみたいだな！<br>
その体なら、可\能\だぜ。なりたいんだろ？大天使に。<br>
俺が、お前を、大天使にしてやるぜ。<br>
今なっているジョブをマスターして、英雄の証となるものを装備してこいよ。」
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=42>
<input type=submit class=btn value="大天使になる">
</form>
EOM
}elsif($chara[65]>=60){
	if($chara[69]==0){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう…$chara[4]か…\噂\は聞いてるぜ…中々　悪　に近づいてるみたいじゃねぇか…<BR><BR>
手を貸してほしければいつでも言いな。<br>
善良ぶってる賞金稼ぎを返り討ちにするために、人を用意してやる…。<br>
それから、ここにある、秘宝「デビルクラウン」を持っていくといい。<br>
金なんかいらねぇぜ。ただし…これを受け取った時点でお前は組織と契約を結んだことになるがな。<br>
ちなみに一応効果を伝えておこう。デビルクラウンを持つ者は、悪に染まるほど強くなる。<br>
組織と契約を結ぶっていうのは、まぁ、お前が今後　仮に善に向かおう時には組織が追手を出すってことだ。<br>
わかるだろ？裏切りは許さん。」
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=item value=1>
<input type=submit class=btn value="受け取る">
</form>
EOM
	}elsif($chara[69]==1 and $chara[86]<2){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう…$chara[4]か…よくきたな…まだまだ　悪　みたいじゃねぇか。<BR><BR>
俺らの手を貸りにきたのか？<br>
善良ぶってる賞金稼ぎを返り討ちにするために、人を用意してやる…。<br>
ただし、今回は金がかかるぜ…なにせ、こっちのモンの人命がかかるからな…。<br>
人、一人につき、$chara[18]000Ｇをいただく。<br>
強さは、お前と同じくらいだ。ただし、３回お前が返り討ちにするのを助けたら１人返してもらうぞ。<br>
ちなみに、同時に雇えるのは２人までだ。
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
<input type=hidden name=item value="1">
<input type=submit class=btn value="１人雇う">
</form>
」
EOM
	}
}elsif($chara[64]>=60){
	if($chara[69]==0){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう…$chara[4]か…\噂\は聞いてるぜ…中々　善　に近づいてるみたいじゃねぇか…<BR><BR>
ふっふ。ここにある、秘宝「エンジェルクラウン」を狙ってきたのか？<br>
どうぞ持っていけ。<br>
金なんかいらねぇぜ。ただし…これを受け取った時点でお前は組織と契約を結んだことになるがな。<br>
ちなみに一応効果を伝えておこう。エンジェルクラウンを持つ者は、善に染まるほど強くなる。<br>
組織と契約を結ぶっていうのは、まぁ、お前が今後　仮に悪に向かおう時には組織が追手を出すってことだ。<br>
わかるだろ？裏切りは許さん。」
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=item value="2">
<input type=submit class=btn value="受け取る">
</form>
EOM
	}
}elsif($chara[64]==50 and $chara[177]==2 and $chara[18]<=2000){
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「よう！！$chara[4]じゃねぇか！！<br>
相変わらず中正というか…。悪にも善にもかたよらねぇな。お前は。<br>
だが・・・お前がそのレベルで討伐クエストを終了した英雄であることは間違いない。<br>
望むなら、裁判官にしてやろう。<br>
今なっているジョブをマスターして、英雄の証となるものを装備してこいよ。」
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=45>
<input type=submit class=btn value="裁判官になる">
</form>
EOM
}else{
	print <<"EOM";

<FONT SIZE=3>
<B>組織の男</B><BR>
「なんだおまえ？$chara[4]？きかねぇ名前だな。もっと有名になってから来るんだな。<BR><BR>
別に悪人であろうと善良であろうと\構\わんぜ。　じゃぁな。
EOM
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub item_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[69]=$in{'item'};

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
		$eg="$chara[4]様が組織と契約を結びました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>組織の男</B><BR>
「そら…持っていけ。
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム売る  #
#----------------#
sub item_sell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19]<$chara[18]*1000){&error("お金が足りません");}
	else{$chara[19]-=$chara[18]*1000;}

	$chara[86]+=1;

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
		$eg="$chara[4]様が悪の組織から人を呼び集めました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>組織の男</B><BR>
「そら…連れて行け。
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム売る  #
#----------------#
sub change {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("現在の職業をマスターしていません。");}
	if($chara[24] ne "1079"){&error("英雄の証となるものを装備してきてください。");}

	$chara[14]=$in{'item'};
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
		$eg="$chara[4]様が英雄職になりました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>組織の男</B><BR>
「そらよ…これからも頑張れ！！
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}