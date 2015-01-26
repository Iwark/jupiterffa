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
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した	#
#    いかなる損害に対して作者は一切の責任を負いません。		#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。	#
#    直接メールによる質問は一切お受けいたしておりません。	#
# 3. 設置したら皆さんに楽しんでもらう為にも、Webリングへぜひ参加#
#    してくださいm(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

require 'sankasya.pl';

# 戦闘ライブラリの読み込み
require 'battle.pl';
# モンスター戦用ライブラリ
require 'mbattle.pl';
require 'item.pl';
# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

if ($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

# このファイル用設定
$temp_back = "$mode\_back";
$temp_midi = "$mode\_midi";
$backgif = $$temp_back;
$midi = $$temp_midi;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");
	}
}
if($mode == 1){&monster;}
else{&$mode;}

exit;

#----------------------#
#  モンスターとの戦闘  #
#----------------------#
sub maou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	&get_host;

	&item_load;

	&acs_add;

	$place=98;
	
	open(IN,"data/maou.ini");
	@MONSTER = <IN>;
	close(IN);
	$r_no = @MONSTER;
	$kazu=2;

	&mons_read;

	open(IN,"./ancd.cgi");
	$member1_data = <IN>;
	close(IN);
	@mem1 = split(/<>/,$member1_data);
	$member=2;
	open(IN,"./ancditem.cgi");
	$mem1item_log = <IN>;
	close(IN);
	@mem1item = split(/<>/,$mem1item_log);

	$khp_flg = $chara[15];
	$mem1hp_flg = $mem1[15];
	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	$smem1hp = $smem1hp_flg;

	$m_sp = int(rand(11));

	$i=1;
	$j=0;
	@battle_date=();

	while($i<=$turn) {

		&shokika;

		&tyousensya;
		
		&tyosenwaza;
		&mons_waza;

		&acs_waza;
		&mons_atowaza;
		
		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;

	}

	&seigi_sentoukeka;
	
	&acs_sub;

	&hp_after;

	&levelup;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><br><B>バトル！</B></FONT>
EOM
	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&mons_footer;

	&footer;

	exit;
}

sub seigi_sentoukeka{
	if ($chara[55]==11 or $chara[56]==11 or $chara[57]==11 or $chara[58]==11)
		{$lgold = int($mgold/2);}
	if ($chara[55]==62 or $chara[56]==62 or $chara[57]==62 or $chara[58]==62)
		{$ygold = $i * int(rand($mgold/10));}
	if ($win==1) {
		$chara[22] += 1;
		$gold = $mgold + $lgold + $ygold + int(rand($mgold)+1);
		$chara[19] += $gold;
		if ($chara[19] > $gold_max) {
			$chara[19] = $gold_max;
		}
		elsif ($chara[19] < 0) {
			$chara[19] = 0;
		}
		$chara[128] = 2;
		$comment = "<b><font color=yellow size=5>$chara[4]はアンクドラルと共に第３代大魔王をやっつけた！</font></b><br>";

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		$chmes="$chara[4]様が第３代大魔王を討伐しました！";
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		unshift(@chat_mes,"<><font color=\"yellow\">告知</font><>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$chmes</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	} else {
		$mex = 1;
		$chara[28] = $bossd;
		$chara[19] = int(($chara[19] / 2));
		$comment = "<b><font size=5>$chara[4]は、戦闘に負けた・・・。</font></b><br>";
	}
		if($khp_flg<=0){$mex= int($mex/10);}
		$chara[17] = $chara[17] + $mex;
		$imex = $mex*int(rand(10)+1);
		$chara[21] ++;
		$chara[25] --;
		$chara[27] = time();
}