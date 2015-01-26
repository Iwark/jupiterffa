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
<form action="stdefshop.cgi" >
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

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	&item_load;

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>怪しい防具屋</h1>
<hr size=0>

<FONT SIZE=3>
<B>怪しい防具屋のマスター</B><BR>
「ぉぅいらっしゃい！この大陸の中じゃ、うちの商品が一級の強さだよ！<BR>
　あ、なんだい、<B>$chara[4]</B>じゃないか。元気にしてたかい？<br>
<font color="red" size=5>金がないのに商品を手に取ったら泥棒とみなすぜ</font>
<BR>
　まあ、ゆっくり見ていってくれ。
<BR><BR>そうそう！最近装備品の下取りはやめたんだ。」
</FONT>
<br><hr>現在の所持金：$chara[19] Ｇ<br>
<form action="stdefshop.cgi" >
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		print "<input type=radio name=item_no value=\"$ino\">";
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="防具を手に取る">
</form>
EOM

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

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	if($in{'kane'}>0){$chara[19]-=$in{'kane'};}
	elsif($chara[19] < $i_gold) { $bgg=1; }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;
if($bgg!=1){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("武器倉庫がいっぱいです！$back_form");
	}

	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>1000000<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>怪しい武器屋のマスター</B><BR>
「毎度あり～！<br>
買った武器はあんたの武器倉庫に送っておいたよ！
」</font>
<hr size=0>
EOM
	&shopfooter;

	&footer;
}else{

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい武器屋のマスター</B><BR>
「貴様・・・金もないのに防具を手に取るとは良い度胸だな<br>
そこを一歩でも動いたら、地獄よりも恐ろしい恐怖を体験することになるぞ。
」</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="防具を元に戻す">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=nigeru>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="防具を持って逃亡する。">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tatakau>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="店主と戦う">
</form>
EOM
if($chara[64]==100){
	print <<"EOM";
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=negiri>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="値切り交渉する">
</form>
EOM
}
print "<hr size=0>";
}
	exit;
}
#----------------#
#  アイテム盗む  #
#----------------#
sub nigeru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;
if(int(rand(10))==1){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("武器倉庫がいっぱいです！$back_form");
	}
	
	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい防具屋のマスター</B><BR>
「待てゴラァァァァ<br>
・・・・・・っち、逃がしたか。<br>
覚えてろよ・・・。
」</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様が怪しい者に追われているようです。";

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
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	$chara[13]-=1;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい防具屋のマスター</B><BR>
「逃げられると思ってたのか？貴様・・・言ったよな。<br>
そこを一歩でも動いたら、地獄よりも恐ろしい恐怖を体験することになる、と。<br>
後悔しても遅いぜ・・・。お前には恐ろしい呪いがかかったのだ。
」</font>
$back_form
<hr size=0>
EOM
}

	exit;
}
#----------------#
#  アイテム盗む  #
#----------------#
sub tatakau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$chara[26] = $host;
	if($chara[18]>5000){$byouyy=int(19701+rand(400));}
	else{$byouyy=int(10000+rand($chara[18]+12500));}
if($byouyy>20000){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("防具倉庫がいっぱいです！$back_form");
	}
	
	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>怪しい防具屋のマスター</B><BR>
「ぐ・・・今日は調子が悪いぜ。<br><br>
覚えてろよ・・・。
」</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様が怪しい防具屋の店主をやっつけたようです。";

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
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[13]-=2;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	$byouyy-=10000;
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy秒で瞬殺された。</B><BR><BR>
<B>怪しい防具屋のマスター</B><BR>
「ザコが。その程度の腕でうちへくるんじゃねぇ。帰りな。AP下げといてやったよｗ
」</font>
$back_form
<hr size=0>
EOM
}

	exit;
}
sub negiri {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("ここには入れない感じだ・・・");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("そんなアイテムは存在しません"); }

	$ok=1;
	if($i_gold > 100000000){$kane=int($i_gold / 100);}else{$kane=int($i_gold/2);}
	if($kane > $chara[19]){$ok=0;}

	$chara[26] = $host;

	&header;
if($ok==1){
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい防具屋のマスター</B><BR>
「ｆｍ・・・確かに君は、人の良さそうな人間だ・・・。<br>
気にいったぜ！それ、あんたの買える値段に値下げしてやる。<br>
どうだ、$kaneＧで買わないか？」</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=kane value=$kane>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="買う">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="買わない">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>怪しい防具屋のマスター</B><BR>
「ｆｍ・・・確かに君は、人の良さそうな人間だ・・・。<br>
だが、いくらなんでも君の所持金は低すぎるな。その値段では売れないよ。<br>
$kaneＧぐらいは用意してくれ。」</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="防具を元に戻す">
</form>
<hr size=0>
EOM
}
	exit;
}