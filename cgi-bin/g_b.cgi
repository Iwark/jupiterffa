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
<form action="g_b.cgi" method="post">
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

	open(IN,"siro.cgi");
	@siro_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>攻城戦受付所</h1>
<hr size=0>
<FONT SIZE=3>
<B>マスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
攻城戦は一時間にに一戦まで、だ。<br>
城を支配すれば、アイテムを生産することができる。<br>
他のギルドが戦ってから５分経っていない城では戦えないぞ。<br>
自分のレベルが城の制限レベルより低くないと戦えないぞ。」
</FONT>
<hr size=0>
EOM
if($chara[67]==$mday + $hour){print "前回攻城戦に参加してから１時間経っていません。";}
if($chara[66]){
	print <<"EOM";
<form action="./koujyou.cgi" method="post">
<table border=1>
現在の城支配ギルド
<th colspan="2">城</th><th>制限レベル</th><th>ギルド名</th><th>支配者</th><th>戦闘間隔</th><th>生産品</th><th>生産度</th></tr><tr>
EOM
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$koutime=time();$koubut="";$hit=0;
	foreach(@siro_data){
		($siro_name,$siro_seigen,$gg_name,$sihaisya,$sihaisyaid,$kankaku,$seisanhin,$seisando,$maxseisando) = split(/<>/);
		$kankaku = 5 - int(($koutime - $kankaku)/60);
		if($kankaku<0){$kankaku=0;}
		if($siro_name and $siro_name ne "象徴戦"){
			print "<tr>";
			if($gg_name ne $chara[66] and $kankaku==0 and $chara[67]!=$mday + $hour and $siro_seigen >= $chara[18]){
				print "<td><input type=radio name=siro_name value=$siro_name></td>";
			}
			else{
				print "<td>　</td>";
			}
			print <<"EOM";
			<td align=center>$siro_name</td>
			<td align=center>$siro_seigen</td>
			<td align=center>$gg_name</td>
			<td align=center>$sihaisya</td>
			<td align=center>残り$kankaku分</td>
			<td align=center>$seisanhin</td>
			<td align=center>$seisando\/$maxseisando</td>
EOM
		}
	}
	print <<"EOM";
</tr>
</table>
<p>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=koujyou>
<input type=submit class=btn value="攻城戦に挑む">
</form>
<p>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="./g_b.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=syoutyou>
<td><input type=submit class=btn value="象徴戦メンバーセレクト"></td>
</form>
<form action="./koujyou.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=syoutyou>
<input type=hidden name=siro_name value="象徴戦">
<td><input type=submit class=btn value="象徴戦"></td>
</form>
EOM
}
open(IN,"seisanmati.cgi");
@seisanmati_data = <IN>;
close(IN);
$hit=0;
foreach(@seisanmati_data){
	($seisansya,$seisanmatihin) = split(/<>/);
	if($seisansya eq $chara[4]){$hit++;}
}
if($hit){
	print <<"EOM";
受け取れる生産品が$hit個あります。
<form action="./g_b.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<td><input type=submit class=btn value="受け取る"></td>
</form>
EOM
}
}else{
	print "ギルドに所属していません。";
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub uketoru {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"seisanmati.cgi");
	@seisanmati_data = <IN>;
	close(IN);
	$hit=0;$se_i=0;
	foreach(@seisanmati_data){
		($sid,$sname) = split(/<>/);
		if($chara[4] eq $sid){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($ssyoukyu,$ssno,$ssname) = split(/<>/);
				if($sname eq $ssname){$chara[$ssno]+=1;$hit=1;$seisanmati_data[$se_i]="";}
			}
		}
		$se_i++;
	}
	if(!$hit){&error("受け取れる生産物がありません。$back_form");}

	open(OUT,">seisanmati.cgi");
	print OUT @seisanmati_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「生産品を受け取ったぞ<br>
」</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub syoutyou {

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	open(IN,"datalog/guest.dat");
	@guest_data = <IN>;
	close(IN);
	$hit=0;$i=0;$ct="";
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){$hit=1;last;}
		$i++;
	}
	if($hit!=1 or $array[1] ne $chara[4]){
		&error("エラー発生。ギルドに所属していないか、ギルマスではありません。");
	}else{
	
		&header;

		print <<"EOM";
<form action="g_b.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="select">
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>名前</th><th>レベル</th></tr>
EOM
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
		$battle_mem_num = @battle_mem;
		$ht=0;
		for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$battle_mem[$bgb].cgi");
			$mem_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&unlock($lock_file,'DR');
			@mem = split(/<>/,$mem_data);
			if($mem[70]<1){$sou=$mem[18]+$mem[37]*100;}
			else{$sou=$mem[18];}
			$guhit=0;
			foreach(@guest_data){
				@guests = split(/<>/);
				if($mem[4] eq $guests[1]){$guhit=1;last;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				$ht=1;
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
		print <<"EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>名前</th><th>レベル</th></tr>
<tr><td><input type="radio" name="mem1" value=$chara[4]></td>
EOM
if($chara[70]<1){$sou=$chara[18]+$chara[37]*100;}
else{$sou=$chara[18];}
if($chara[70]<1){
	print "<td>$chara[4]</td><td>$sou</td></tr>";
}else{
	print "<td><font color=\"yellow\">$chara[4]</font></td><td>$sou</td></tr>";
}
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
		$battle_mem_num = @battle_mem;
		for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$battle_mem[$bgb].cgi");
			$mem_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&unlock($lock_file,'DR');
			@mem = split(/<>/,$mem_data);
			if($mem[70]<1){$sou=$mem[18]+$mem[37]*100;}
			else{$sou=$mem[18];}
			$guhit=0;
			foreach(@guest_data){
				if($mem[4] eq $_){$guhit=1;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
		print <<"EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
<table border=1>
<tr><th></th><th>名前</th><th>レベル</th></tr>
<tr><td><input type="radio" name="mem1" value=$chara[4]></td>
EOM
if($chara[70]<1){$sou=$chara[18]+$chara[37]*100;}
else{$sou=$chara[18];}
if($chara[70]<1){
	print "<td>$chara[4]</td><td>$sou</td></tr>";
}else{
	print "<td><font color=\"yellow\">$chara[4]</font></td><td>$sou</td></tr>";
}
		@pre = split(/<>/,$member_data[$i],8);
		@battle_mem = split(/<>/,$pre[7]);
		$battle_mem_num = @battle_mem;
		for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$battle_mem[$bgb].cgi");
			$mem_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
			&unlock($lock_file,'DR');
			@mem = split(/<>/,$mem_data);
			if($mem[70]<1){$sou=$mem[18]+$mem[37]*100;}
			else{$sou=$mem[18];}
			$guhit=0;
			foreach(@guest_data){
				if($mem[4] eq $_){$guhit=1;}
			}
			if($mem[4] and $mem[66] eq $array[0] and $guhit==1){
				print "<tr><td><input type=\"radio\" name=\"mem1\" value=$mem[4]></td>";
				if($mem[70]<1){
					print "<td>$mem[4]</td><td>$sou</td></tr>";
				}else{
					print "<td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td></tr>";
				}
			}
		}
	}
	print <<"EOM";
</table>
</td>
</tr>
</table>
EOM
if($ht!=1){
	print "現在ログインしているギルドメンバーが居ません";
}else{
	print <<"EOM";
<input type=submit class=btn value="セレクト">
EOM
}
	print <<"EOM";
</form>
<form action="g_b.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="戻る">
</form>
EOM

	&footer;

	exit;
}