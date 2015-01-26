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
<form action="ippatu.cgi" method="post">
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

	print <<"EOM";
<h1>一発逆転ショップ</h1>
<hr size=0>
<FONT SIZE=3>
<B>ショップの店員の孫の友達</B><BR>
「ん？、君、ここを見つけたのか。やるじゃない。<br>
一発逆転ショップへようこそ。ここでは、君が何かを買うのでなく、僕が君の勇気を買うよ。<br>
もし、<br>
君が僕の言うことを成功させることができたら、<br>
君の望む物をあげようと思うよ。<br>
しかし、もしもできなかったその時は、<br>
タイヘンなことになるからなっ！！！！！！！！！！！！！<br>
挑戦したいレベルを選択しな。高ければ高いほど難しいし、報酬も大きいよ。」
</FONT>
<hr size=0>
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
EOM
if($chara[191]!=1 and $chara[191]!=2){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="1">スーパーイージー<br>
EOM
}
if($chara[192]!=1 and $chara[192]!=2){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="2">イージー<br>
EOM
}
if($chara[193]!=1 and $chara[193]!=2 and $chara[64] > 90){
	print <<"EOM";
<INPUT TYPE="radio" NAME="cylv" VALUE="3">善人モード<br>
EOM
}
	print <<"EOM";
<br>　　
<input type=submit class=btn value="挑戦する">
</form>
EOM
if($chara[191]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=191>
<br>　　
<input type=submit class=btn value="スーパーイージークリア報酬を受け取る">
</form>
EOM
}
if($chara[192]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=192>
<br>　　
<input type=submit class=btn value="イージークリア報酬を受け取る">
</form>
EOM
}
if($chara[193]==2){
	print <<"EOM";
<form action="ippatu.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=hosh>
<input type=hidden name=cqu value=193>
<br>　　
<input type=submit class=btn value="善人モードクリア報酬を受け取る">
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
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$cylv=$in{'cylv'};

	if($cylv == 1){
		$chara[191]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よし、君にやってもらうことを教えよう。<br>
		それは、、、怪しい武器屋の店主を倒すこと！<br>
		もしも、倒すことに成功したら、またここへ戻ってくるといい。
		」</font>
		<hr size=0>
EOM
	}elsif($cylv == 2){
		$chara[192]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よし、君にやってもらうことを教えよう。<br>
		それは、、、怪しい武器屋の店主から武器を盗むこと！<br>
		あいつには恨みがあるからな・・・ｗ<br>
		もしも、倒すことに成功したら、またここへ戻ってくるといい。
		」</font>
		<hr size=0>
EOM
	}elsif($cylv == 3){
		$chara[193]=1;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「あえて、君のすべきことは教えないよ。<br>
		周りの人と相談してやってみなっ！<br>
		ヒントは、ア○○○ラ○。<br>
		よーし行ってこい！失敗したら処刑だぞっ！」</font>
		<hr size=0>
EOM
	}elsif($cylv == 4){
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よーし行ってこい！失敗したら処刑だぞっ！」</font>
		<hr size=0>
EOM
	}elsif($cylv == 5){
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よーし行ってこい！失敗したら処刑だぞっ！」</font>
		<hr size=0>
EOM
	}else{
		&error("レベルを設定していません。$back_form");
	}

	&shopfooter;

	&footer;

	exit;
}
sub hosh {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$cqu=$in{'cqu'};

	if($cqu == 191){
		$chara[191]=0;
		if(int(rand(100))<80){
			$hoos=10000000;
		}elsif(int(rand(100))<99){
			$hoos=30000000;
		}else{
			$hoos=50000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よくやったな！それ、報酬として、$hoosＧやろう。
		」</font>
		<hr size=0>
EOM
	}elsif($cqu == 192){
		$chara[192]=0;
		if(int(rand(100))<80){
			$hoos=30000000;
		}elsif(int(rand(100))<99){
			$hoos=50000000;
		}else{
			$hoos=80000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よくやったな！それ、報酬として、$hoosＧやろう。
		」</font>
		<hr size=0>
EOM
	}elsif($cqu == 193){
		$chara[193]=0;
		if(int(rand(100))<80){
			$hoos=70000000;
		}elsif(int(rand(100))<99){
			$hoos=100000000;
		}else{
			$hoos=130000000;
		}
		$chara[34]+=$hoos;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よくやったな！それ、報酬として、$hoosＧやろう。
		」</font>
		<hr size=0>
EOM
	}elsif($cqu == 194){
		$chara[194]=0;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よーし行ってこい！失敗したら処刑だぞっ！」</font>
		<hr size=0>
EOM
	}elsif($cqu == 195){
		$chara[195]=0;
		&chara_regist;

		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
	
		&header;

		print <<"EOM";
		<FONT SIZE=3>
		<B>ショップの店員の孫の友達</B><BR>
		「よーし行ってこい！失敗したら処刑だぞっ！」</font>
		<hr size=0>
EOM
	}else{
		&error("レベルを設定していません。$back_form");
	}

	&shopfooter;

	&footer;

	exit;
}