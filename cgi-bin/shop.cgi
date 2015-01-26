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
<form action="$script" method="post">
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

&error;

exit;

#--------#
#  宿屋  #
#--------#
sub yado {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

        #宿代計算
        $yado_daix=int($yado_dai*$chara[18]);
	$com="";
	if($yado_daix>100000 and int(rand(100))==0 and $chara[15] != $chara[16]){
		$chara[305]+=1;
		$com="お土産に宿屋餅を手に入れた！";
	}
($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
$mon = $mon+1;
$year = $year +1900;
	if($mon==1 and $mday==1 and $year != $chara[306]){
		$chara[306]=$year;
		if($chara[18]<=10000){
			$okane=$year * int($chara[18]/10+10) * 10000;
			$chara[19]+=$okane;
			$com="あけましておめでとうイベント！お年玉に$okaneＧ手に入れた！";
		}else{
			$chara[305]+=$year;
			$com="あけましておめでとうイベント！お土産に宿屋餅を$year個手に入れた！";
		}
	}
		
	$chara[15] = $chara[16];
	$chara[42] = $chara[43];
	$chara[19] -= $yado_daix;
	$chara[28] = $boss;
	$chara[17]=int($chara[17]);
	$chara[40]=int($chara[40]);

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;
	$xtime = $vtime + 1;
	$ztime = $vtime + 1;
	if($ztime < 10){$chara[139]=0;}
	if ($chara[19] < 0) { &error("お金が足りません！$back_form"); }

	&chara_regist;
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/cmp.lock";
	&lock($lock_file,'BT');

	if($chara[140]==2){&read_winner2;$wt="winner2_file";}
	elsif($chara[140]==3){&read_winner3;$wt="winner3_file";}
	elsif($chara[140]==4){&read_winner4;$wt="winner4_file";}
	elsif($chara[140]==5){&read_winner5;$wt="winner5_file";}
	else{&read_winner;$wt="winner_file";}

	if ($winner[0] eq $chara[0]) {
		$winner[15] = $winner[16];
		$new_winner = '';
		foreach(@winner){
			$new_winner .="$_<>";
		}
		open(OUT,">$winner$$wt");
		print OUT $new_winner;
		close(OUT);
	}

	&unlock($lock_file,'BT');

	&header;

	print <<"EOM";
<h1>宿屋</h1>
<hr size=0>
<FONT SIZE=3>
$yado_daixＧを使用し、体力を全回復しました！<br>
$com</FONT>
EOM
if($chara[305]>100 and int(rand(30))==0){
	print <<"EOM";
<FONT SIZE=3>
帰り道、なんと、お腹を空かせた悪魔が一匹倒れているのを見つけました。<br>
宿屋餅を100個あげれば元素を１つくれそうです。<br>
現在、宿屋餅を$chara[305]個所持しています。<br>
宿屋餅100個と何かの元素を交換してもらいますか？</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti>
<input type=submit class=btn value="交換してもらう">
</form>
EOM
}elsif($chara[305]>30 and int(rand(10))==0){
	print <<"EOM";
<FONT SIZE=3>
帰り道、なんと、お腹を空かせた天使が一匹倒れているのを見つけました。<br>
宿屋餅を30個あげれば元気を出してくれそうです。<br>
現在、宿屋餅を$chara[305]個所持しています。<br>
宿屋餅30個をあげますか？</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti2>
<input type=submit class=btn value="あげる">
</form>
EOM
}elsif($chara[305]>20 and int(rand(10))==0){
	print <<"EOM";
<FONT SIZE=3>
帰り道、なんと、いつもは見ないお地蔵様を発見しました。<br>
宿屋餅を20個ぐらい欲しそうな顔をしています。<br>
現在、宿屋餅を$chara[305]個所持しています。<br>
宿屋餅20個をあげますか？</FONT>
<form action="./shop.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=moti3>
<input type=submit class=btn value="あげる">
</form>
EOM
}elsif($chara[305]>0){
	print <<"EOM";
<FONT SIZE=3>
現在、宿屋餅を$chara[305]個所持しています。<br>
凄く手間暇かかっているお餅で、高価な宿でしか貰えません。<br>
いつか、このお餅を探し求めるお爺さんが現れて、レアなアイテムと交換してくれるだなんて、<br>
そんな妄想を抱いてはいけません。。</FONT>
EOM
}
	&shopfooter;

	&footer;

	exit;
}

#--------#
#  宿屋  #
#--------#
sub moti {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 100) { &error("お餅が足りません！$back_form"); }
	else {
		$chara[305] -= 100;
		$chara[308] += 1;
		$gishi=int(rand(4)+29);
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
		$com = "<font class=\"red\" size=5>$sozainameを手に入れたッ！！</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>宿屋</h1>
<hr size=0>
<FONT SIZE=3>
悪魔に宿屋餅を100個あげた！<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub moti2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 30) { &error("お餅が足りません！$back_form"); }
	else {
		$chara[305] -= 30;
		$chara[307] += 1;
		$gishi=int(rand(21)+12);
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
		$com = "<font class=\"red\" size=5>天使はお礼に$sozainameをくれたッ！！</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>宿屋</h1>
<hr size=0>
<FONT SIZE=3>
天使に宿屋餅を30個あげた！<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub moti3 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

     
	if ($chara[305] < 20) { &error("お餅が足りません！$back_form"); }
	else {
		$chara[305] -= 20;
		$chara[309] += 1;
		$gishi=23;
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
		$jizo = int(rand(3)+1);
		@isi[$gishi]+=$jizo;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$com = "<font class=\"red\" size=5>お地蔵様はお礼に$sozainameを$jizo個くれたッ！！</font><br>";
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>宿屋</h1>
<hr size=0>
<FONT SIZE=3>
お地蔵様に宿屋餅を20個あげた！<br>
$com</FONT>
EOM
	&shopfooter;

	&footer;

	exit;
}