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

require 'item.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

require 'mbattle.pl';

require 'battle.pl';

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
<form action="kunren.cgi" >
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

	&header;

	print <<"EOM";
<h1>訓練所</h1>
<hr size=0>
<FONT SIZE=3>
<B>訓練所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここでは、たるんだ貴様の根性を叩きなおしてやるぜっ。<br>
ここで戦ったが最後、貴様の体力は回復不\能\なまでにダメージを負うだろうがなっ。<br>
ま、その代わり得るものは多いだろうが…。<br>
ここで受けたダメージは特殊な回復法が必要だ。<br>
とりあえず回復第一条件はギルドに加入することだな。」
</FONT>
EOM

if($chara[150]>0 and $chara[0] ne "jupiter"){print "前回の訓練のダメージが回復していません。";}
else{
print <<"EOM";
<form action="./kunren.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=kunren>
<input type=submit class=btn value="訓練に挑む">
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
sub kunren {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	if($chara[150]>0 and $chara[0] ne "jupiter"){&error("前回の訓練のダメージが回復していません。");}
	if($chara[70]<1){&error("限界突破者専用施設です。");}

	$chara[150]=10;

	&item_load;

	&acs_add;

	if($chara[18]<150){$kunren_monster="kunren_monster1";}
	elsif($chara[18]<200){$kunren_monster="kunren_monster2";}
	elsif($chara[18]<250){$kunren_monster="kunren_monster3";}
	else{$kunren_monster="kunren_monster4";}

	open(IN,"$$kunren_monster");
	@MONSTER = <IN>;
	close(IN);

	$r_no = @MONSTER;

	$kazu=5;

	&mons_read;

	$khp_flg = $chara[15];

	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem2hp_flg = int(rand($mrand2)) + $msp2;
	$smem3hp_flg = int(rand($mrand3)) + $msp3;
	$smem4hp_flg = int(rand($mrand4)) + $msp4;
	$smem1hp = $smem1hp_flg;
	$smem2hp = $smem2hp_flg;
	$smem3hp = $smem3hp_flg;
	$smem4hp = $smem4hp_flg;
	
	if($chara[24]==9999 or $chara[24]==0){$sudedmg=1;}

	$i=1;
	$j=0;@battle_date=();
	$place = 29;
	foreach(1..$turn) {
		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	&hp_after;

	if ($win==1) {
 		$comment .= "<b><font size=5>$chara[4]は、戦闘に勝利した！！</font></b><br>";
		&quest;
	} elsif ($win==2) {
		$comment .= "<b><font size=5>$chara[4]は、逃げ出した・・・♪</font></b><br>";
	} else {
		$comment .= "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
	}

	&acs_sub;

	if($win==1){
		$jup=int(rand(4));
		$comment.= <<"EOM";
		<FONT SIZE=4 color="red">
		<B>ジョブレベルが$jup上がりました。</B><BR>
		<hr size=0>
EOM
		$klvbf=$chara[33];
		$chara[33] += $jup;
		#ジョブマスターの処理
		if ($chara[33] > 99 && $klvbf <=99) {
			$comment .= "<font class=red size=5>$chara_syoku[$chara[14]]をマスターした！！</font><br>";
			$lock_file = "$lockfolder/syoku$in{'id'}.lock";
			&lock($lock_file,'SK');
			&syoku_load;

			$syoku_master[$chara[14]] = 100;

			&syoku_regist;
			&unlock($lock_file,'SK');
		}
		if ($chara[33] > 100) { $chara[33]=100; }

		$chara[15] = $chara[16];
	}
		
	if(int(rand(5))<2){
		$comment.= <<"EOM";
		<FONT SIZE=4 color="red">
		<B>精一杯訓練して皆から見直された。善人度が１上がった。</B><BR>
		<hr size=0>
EOM
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$chara[64]+=1;
		$chara[65]-=1;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[64]>100){$chara[64]=100;}
		if($chara[65]<0){$chara[65]=0;}
	}

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>訓練所</B></FONT>
<BR>

<B><CENTER><FONT SIZE= "6">バトル！</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	print "$comment<br>\n";
	print <<"EOM";
<form action="$script" >
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="ステータス画面へ">
</form>
EOM
	&footer;

	exit;
}