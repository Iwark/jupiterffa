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
<form action="./hatake.cgi" method="post">
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
#  ペット表示　  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	if(!$chara[66]){&error("どこかギルドに入ってね");}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	foreach (@all_hatake) {
		@hatake = split(/<>/);
		if($hatake[0] eq $chara[66]){
			$hit=1;last;
		}
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$ghit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){$ghit=1;last;}
	}

	&header;
if($hit==1){
	print <<"EOM";
	<h1>畑</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>おっさん</B><BR>
	「ギルド所有の畑じゃよーっ<br>
	耕しに来たのかい？大変じゃのーっ<br>
	耕せるのはお一人様一日一回までじゃ。やりすぎはよくないんじゃ。」
	</FONT>
	<br>
	土地ランク　：$hatake[1]<br>
	作物の量　　：$hatake[2]<br>
	闇つきリンゴ：$hatake[3] (限界数3)<br>
	かかし　　　：$hatake[4] (限界数100)<br>
	輝くリンゴ　：$hatake[5] (限界数10)<br>
	<br>
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=tagayasu>
	<input type=submit class=btn value="耕す">
	</form>
EOM
if($hatake[2]>100000 and $ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=sellrank>
	<input type=submit class=btn value="土地ランクを売る">(100ポイント金貨１枚)
	</form>
EOM
}
if($hatake[6]==1){
	if($ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="作物を植える">
	<font color="red">※ギルドマスターのみ植えることができる状態です。</font>
	</form>
EOM
	}else{
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="作物を植える" disabled>
	<font color="red">※ギルドマスター以外は植えるの禁止令発令中</font>
	</form>
EOM
	}
}else{
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ueru>
	<input type=submit class=btn value="作物を植える">
	</form>
EOM
}
if($chara[31] eq "0044"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=ringo>
	<input type=submit class=btn value="闇つきリンゴを植える(※無くなります)">
	</form>
EOM
}
if($chara[31] eq "0045"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kakasi>
	<input type=submit class=btn value="かかしを立てる(※無くなります)">
	</form>
EOM
}
if($chara[31] eq "0046"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=mikan>
	<input type=submit class=btn value="Ａ姫蜜柑に仕事を頼む(※居なくなります)">
	</form>
EOM
}
if($chara[31] eq "0048"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=petring>
	<input type=submit class=btn value="ペットリングを植える(※無くなります)">
	</form>
EOM
}
if($chara[31] eq "0054"){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=chees>
	<input type=submit class=btn value="極上のチーズを植える(※無くなります)">
	</form>
EOM
}
if($ghit==1){
	print <<"EOM";
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kinsi>
	<input type=submit class=btn value="植えるの禁止令発令/解除">
	</form>
EOM
}
}else{
	print <<"EOM";
	<h1>畑</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>おっさん</B><BR>
	「畑を買いに来たのか～？買うのはギルドマスターが来いよ～。ちなみに100万Ｇでいいぞ。」
	</FONT>
	<br>
	<br>
	<form action="./hatake.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kau>
	<input type=submit class=btn value="買う">
	</form>
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
sub kau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($chara[66] and $gg_leader eq $chara[4]){$hit=1;last;}
	}

	if($hit!=1){&error("ギルドリーダーではありません");}
	if($chara[19] < 1000000){&error("お金が足りません。");}
	else{$chara[19] -= 1000000;}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$hit=0;

	unshift(@all_hatake,"$chara[66]<>1<>0<>\n");

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

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
		$eg="$chara[66]ギルドが畑を購入しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
	<br>
	<font size=5>畑を買いました</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム買う  #
#----------------#
sub tagayasu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("転生回数10回未満は畑仕事できません");}
	if($chara[92]==$mday){&error("今日はもう畑仕事をしましたよ。");}
	else{$chara[92] = $mday;}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("畑が見つかりません");}

	$tp=int(rand(4));
	if($chara[31] eq "0029"){$tp+=int(rand(8));}
	if($array[3]>0){$tp+=int($array[3]+1);}
	if($array[5]>0){$tp+=int($array[5]+1);}
	$array[1]+=$tp;
	$array[2]-=int(rand(2));
	if($array[2]<0){$array[2]=0;}
	$kaneget=$array[2]*10000;
	$chara[19]+=$kaneget;

	$new_array = '';
	$new_array = join('<>',@array);

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>
	畑を耕します。
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	ザクッ<br>
	<font size=5 color="red">
	$tp　ポイント、土地ランクが上がり、$kaneget Ｇ入手しました。
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  アイテム買う  #
#----------------#
sub ueru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("転生回数10回未満は畑仕事できません");}
	if($chara[92]==$mday){&error("今日はもう畑仕事をしましたよ。");}
	else{$chara[92] = $mday;}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$ghit=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){$ghit=1;last;}
	}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("畑が見つかりません");}
	elsif($array[6]==1 and $ghit!=1){&error("植えるの禁止令が発令されています！");}
	$up=int(rand($array[1]));
	if($chara[31] eq "0029"){$up+=int(rand($array[1]));}
	if($array[3]>0){$up+=int(rand($array[3]*25));}
	if($array[5]>0){$up+=int(rand($array[5]*20));}
	if($array[2]+$up>100000){$up=100000-$array[2];}
	$array[2]+=$up;
	$array[1]-=int(rand($array[1]/2));
	if($array[1]<0){$array[1]=0;}
	$kaneget=$array[2]*10000;
	$chara[19]+=$kaneget;

	$new_array = '';
	$new_array = join('<>',@array);
	$new_chara .= '<>';

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>作物植えます。</font>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	グサッ<br>
	<font size=5 color="red">作物を$up個植え、$kaneget Ｇ入手しました。</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub ringo {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0044"){&error("闇つきリンゴがありません");}
	if(!$hit){&error("畑が見つかりません");}
	if($array[3]>2){&error("これ以上闇つきリンゴは植えられません");}
	$array[3]+=1;
	$array[2]-=int(rand($array[2]/2));
	if($array[2]<0){$array[2]=0;}

	#$new_array = '';
	#$new_array = join('<>',@array);
	#$new_array =~ s/\n//;
	#$new_array .= "<>\n";

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>闇つきリンゴを植えます。</font>
	<br><br><br><br><br><br><br>
	グサッ<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">闇つきリンゴを植えた。周りの作物が腐った。</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kakasi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0045"){&error("かかしがありません");}
	if(!$hit){&error("畑が見つかりません");}
	if($array[2]>10000){&error("作物が多すぎてかかしを立てるスペースがありません。");}
	if($array[4]>99){&error("かかしが多すぎて気味が悪い。このくらいにしておこう。");}
	$array[4]+=1;
	$array[2]+=int(rand($array[2]/2));

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>かかしを立てます。</font>
	<br><br><br><br><br><br><br>
	グサグサグサッ<br>ピコーン。
	<br><br><br><br><br><br><br>
	<font size=5 color="red">かかしを立てた。周りの作物が急激に育った。</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub mikan {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0046"){&error("Ａ姫蜜柑がいません");}
	if(!$hit){&error("畑が見つかりません");}
	if($array[3]<1){&error("Ａ姫蜜柑のする仕事がありません");}
	if($array[5]>9){&error("輝くリンゴが多すぎるようです");}
	$array[3]-=1;
	$array[5]+=1;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>Ａ姫蜜柑は、闇つきリンゴを見つけた！</font>
	<br><br><br><br><br><br><br>
	ぴかぴかぴかぴか<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">Ａ姫蜜柑は仕事を終え、闇つきリンゴが輝くリンゴに変化した！！</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub petring {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0048"){&error("ペットリングがありません");}
	if(!$hit){&error("畑が見つかりません");}

	$up=int(rand(10000));
	if($array[2]>50000){$up=int($up/2);}
	if($array[2]>100000){$up=int($up/4);}
	$array[2]+=$up;
	$kaneget=$array[2]*100000;
	$chara[19]+=$kaneget;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>ただの指輪じゃないんだゾ、超レアなペットリングなんだゾ。</font>
	<br><br><br><br><br><br><br>
	土にかえって栄養金銀ざくざく！！！<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">作物もどんどん！$up個も増え、$kaneget Ｇ入手しました。</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub chees {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if($chara[31] ne "0054"){&error("極上のチーズがありません");}
	if(!$hit){&error("畑が見つかりません");}

	$up=int(rand(20000));
	if($array[2]>50000){$up=int($up/2);}
	if($array[2]>100000){$up=int($up/4);}
	if($array[2]>150000){$up=int($up/8);}
	if($array[2]>200000){$up=int($up/20);}
	$array[2]+=$up;
	$kaneget=$array[2]*100000;
	$chara[19]+=$kaneget;

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);
	
	&acs_lose;
	$chara[31]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<br>
	<font size=4>天界の力を得ることが出来るとは、羨ましい畑ダナ！！！</font>
	<br><br><br><br><br><br><br>
	極上チーズで栄養金銀ざくざく！！！<br>
	<br><br><br><br><br><br><br>
	<font size=5 color="red">作物もどんどんどんどんどどんどん！$up個も増え、$kaneget Ｇ入手しました。</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub kinsi {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("畑が見つかりません");}

	if($array[6]==0){$array[6]=1;}
	else{$array[6]=0;}

	if($array[0]){$all_hatake[$i]="$array[0]<>$array[1]<>$array[2]<>$array[3]<>$array[4]<>$array[5]<>$array[6]<>\n";}

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<font size=5 color="red">
	植えるの禁止令を発令/解除しました！
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub sellrank {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[70]<1 and $chara[37]<10){&error("転生回数10回未満は畑仕事できません");}

	open(IN,"allhatake.cgi");
	@all_hatake = <IN>;
	close(IN);
	$i=0;
	foreach(@all_hatake){
		@array = split(/<>/);
		if($chara[66] eq $array[0]){$hit=1;last;}
		$i++;
	}
	if(!$hit){&error("畑が見つかりません");}
	if($array[2]<100000){&error("生産物が足りません");}
	if($array[1]<100){&error("土地ランクが足りません");}
	else{
		$array[1]-=100;
		$chara[136] += 1;
	}
	$new_array = '';
	$new_array = join('<>',@array);

	$all_hatake[$i]=$new_array;

	open(OUT,">allhatake.cgi");
	print OUT @all_hatake;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	<font size=5 color="red">
	土地ランクを１００ポイント売り、金貨を１枚入手しました。
</font>
EOM

	&shopfooter;

	&footer;

	exit;
}