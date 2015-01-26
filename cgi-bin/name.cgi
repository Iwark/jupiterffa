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
<form action="name.cgi" method="post">
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
<h1>名前変更所</h1>
<hr size=0>
<FONT SIZE=3>
<B>名前変更所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
名前変更がしたいのか・・・？注意点だ。<br>
①名前変更は２週間に１度のみ。変更料金は100万Gだ。<br>
②他キャラの名前や、ゲーム内キャラクターに酷似した名前は絶対につけないでください。<br>
③その他、不正や、嫌がらせと思われるような名前にした場合、何らかの対処が取られます。」
</FONT>
<br>現在の所持金：$chara[19] Ｇ
<hr size=0>
	<form action="./name.cgi" method="post">
	<input type=hidden name=id value=$in{'id'}>
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=jyoho_buy>
新しい名前　：<input type="text" name="new_name" value="" size=40><br>
	<input type=submit class=btn value="変更する">
	</form>
	：：：：変更履歴：：：：
	<table>
	<tr><th>旧名前</th><th>新名前</th><th>変更日</th></tr>
EOM
	open(IN,"allname.cgi");
	@member_data = <IN>;
	close(IN);

	foreach(@member_data){
		($old_name,$new_name,$henko_day) = split(/<>/);
		print <<"EOM";
		<tr><th>$old_name</th><th>$new_name</th><th>$henko_day</th></tr>
EOM
	}
	print "</table>";
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

$koutime=time();

	if ($in{'new_name'} eq ""){ &error("変更したい名前を入力してください。$back_form"); }
	elsif ($name_ban) {
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[4] eq $in{'new_name'}) {
				close(IN);
				&error("同一名のキャラクターがいます。$back_form");
			}
		}
	}
	elsif(int($koutime/1209600)>$chara[96]-1){&error("前回名前を変更してから2週間経っていません$back_form");}
	$ps_gold = 1000000;

	if($chara[19] < $ps_gold) { &error("お金が足りません$back_form"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[1] eq $chara[4]){
			$array[1]=$in{'new_name'};
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[1] eq $chara[4]){
			$array[1]=$in{'new_name'};
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	$old_name=$chara[4];
	$chara[4]=$in{'new_name'};
	$chara[94]=int($koutime/1209600);
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

	$boa="<font color=\"yellow\">$old_name様が、$in{'new_name'}様に、名前変更をなさいました！</font>";

	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<>$boa<>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	open(IN,"allname.cgi");
	@member_data = <IN>;
	close(IN);

	push(@member_data,"$old_name<>$in{'new_name'}<>$year年$mon月$mday日(火)$hour時$min分<>\n");

	open(OUT,">allname.cgi");
	print OUT @member_data;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>名前変更所のマスター</B><BR>
「名前の変更が完了したぞ。
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
