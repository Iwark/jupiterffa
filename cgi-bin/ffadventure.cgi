#!/usr/local/bin/perl

#------------------------------------------------------#
#　本スクリプトの著作権は下記の4人にあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
#  FF ADVENTURE(いく改)
#　remodeling by いく
#　http://www.eriicu.com
#　icu@kcc.zaq.ne.jp
#------------------------------------------------------#
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

#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した	#
#    いかなる損害に対して作者は一切の責任を負いません。		#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。	#
#    直接メールによる質問は一切お受けいたしておりません。	#
# 3. 設置したら皆さんに楽しんでもらう為にも、Webリングへぜひ参加#
#    してくださいm(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi　		#
#---------------------------------------------------------------#

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# レジストライブラリの読み込み
require 'sankasya.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

require 'chat.pl';

# このファイル用設定
$backgif = $sts_back;
$midi = $sts_midi;
#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

#--------------#
#　メイン処理　#
#--------------#
if ($mente) {
	&error("バージョンアップ中です。２、３０秒ほどお待ち下さい。m(_ _)m"); 
}
&decode;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("アクセスできません！！");
	}
}

&log_in;

#----------------#
#  ログイン画面  #
#----------------#
sub log_in {

	if (!( -e "./charalog/$in{'id'}.cgi")) {
		if ( -e "./autobackup/charalog/$in{'id'}.cgi" ) {
		}else{
			&error('IDが正しくありません！');
		}
	}

	&chara_load;

	&chara_check;

	&item_load;

	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	$chara[144]=time();
	&chara_regist;
	&chara_load;

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;
	$xtime = $vtime + 1;
	$ztime = $vtime + 1;
	$mtime = $m_time - $ltime + 1;

	if($chara[28] < $boss) {
		$chara[28] = 0;
	}

	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);
	$gnnt="<option value=\"\">ささやき\n";
	foreach(@guest){
		($gtt,$gnn,$gii) = split(/<>/);
		if($gii ne "jupiter"){ $gnnt.="<option value=\"$gnn\">$gnnさんへ\n"; }
	}
	if($chara[5]) { $esex = "男"; } else { $esex = "女"; }
	if($chara[70]!=1){$next_ex = $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50);}
	else{$next_ex = $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;}
        if(!$chara[32]){$chara[32] = 0;}

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}

	$syou = @shogo[$chara[32]];

        #宿代計算
        $yado_daix=int($yado_dai*$chara[18]);

	&header;

	&guest_list;

	&guest_view;

	if($chara[140]==2){$sity = "イエローワールド";&read_winner2;}
	elsif($chara[140]==3){$sity = "レッドワールド";&read_winner3;}
	elsif($chara[140]==4){$sity = "ドラゴンワールド";&read_winner4;}
	elsif($chara[140]==5){$sity = "天界";&read_winner5;}
	else{$sity = "ジュピタワールド";&read_winner;}

       print <<"EOM";
	<hr size=0>
	<font class=white>メニュー/</font><a href="$scripta?mode=ranking">登録者一覧</a> /
	<a href="$helptext" target="_blank">$helptext_url</a> /
	<a href="./cbbs/cbbs.cgi" target="_blank">掲示板</a>
	<br>
	<!--
	<a href="$ranking">能\力別ランキングへ</a> /
	<a href="$syoku_html" target="_blank">各職業に必要な特性値</a> /
	<a href="$img_all_list" target="_blank">$vote_gazou</a> /
	<a href="$bbs" target="_blank">$bbs_title</a> /
	<font class=white>町の外れ/</font>
	<a href="$sbbs" target="_blank">$sbbs_title</a> / 
	<a href="$vote" target="_blank">$vote_title</a> /
	-->
<br>
<table align="center"width="100%">
EOM
if($chara[50]==1){
	print <<"EOM";
<TR><td rowspan="2"  align="center" class="b2" width=70 height=60>
EOM
}else{
	print <<"EOM";
<TR><td rowspan="2"  align="center" class="b2" width=70 height=60><img src="$img_path/$chara_img[$winner[5]]">
EOM
}
	print <<"EOM";
<TD id="td1" align="center" colspan=2 class="b2">【$sity】チャンプ<a href="$scripta?mode=chara_sts&id=$winner[0]"><B>$winner[3]</B></a>さん($winner[44]連勝中)</TD></TR>
	<TR><td id="td2"align="center" class="b2">現在のHP</td><TD class="b2"align="center"><B>$winner[15]\/$winner[16]</B></TD></TR></table>
<hr size=0>
<font size=5 color="yellow">$sity</font><br>
<font size=4 color="red"><b>新規さんは掲示板で情報を取得しよう！聞く前に調べよう！</b></font>
EOM
	print <<"EOM";
<table border=0 width='30%'>
<tr><td align="center" talign="center" class="b1">
<MARQUEE><font color=yellow>$ttemes</font></MARQUEE></td>
</tr></table>

<hr width=400>
<script>
function aaa(fm){ 
fm.mes.value="";
fm.mes.focus(); 
return false; 
}
</script>
<FORM action="menu.cgi" target="chat" onSubmit="setTimeout(function(){return aaa(this)},10)">
<table border=0 align="center" width='100%'><tr>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="name" value="$chara[4]">
<input type="hidden" name="level" value="$chara[18]">
<input type="hidden" name="chattime" value="1">
<input type="hidden" name="chan" value="$chara[96]">
<input type="hidden" name="chan2" value="$chara[180]">
常連チャンネル使用：①<INPUT TYPE="radio" NAME="tch2" VALUE="$chara[96]">ON
<INPUT TYPE="radio" NAME="tch2" VALUE="" checked>OFF
　②<INPUT TYPE="radio" NAME="tch3" VALUE="$chara[180]">ON
<INPUT TYPE="radio" NAME="tch3" VALUE="" checked>OFF
　<select name="sasayaki">$gnnt</select>
<td align="left"><input type="submit" class=btn value="発言＆更新">
<INPUT type="text" value="" name="mes" size="100" maxlength="60">　　
<INPUT type="text" value="" name="tch" size="3" maxlength="3">ch</td>
</tr>
<tr></FORM>
<td align="left" class="b2">
<iframe src="menu.cgi" width="100%" height="200" frameborder="0" name="chat" allowtransparency="true" scrolling="yes"></iframe>
</td></tr></table>

EOM
#	&chat_post;

if ($ztime > 0) {
       print <<"EOM";
<table><tr>
<FORM NAME="form1">
<td>
戦闘開始可能\まで残り<INPUT TYPE="text" NAME="clock" SIZE="3">秒です。(自動で更新されます。)
</td>
</FORM>
</tr></table>
EOM
}
if($item[20]==10 and $chara[24]==1400){$g="yellow";}elsif($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="pink";}else{$g="";}
if($item[22]==10){$w="red";}else{$w="";}
$bukikoka = "攻撃力 $item[1]<br>命中率 $item[2]<br>効果 $item[24]";
$bogukoka = "防御力 $item[4]<br>回避率 $item[5]<br>効果 $item[25]";
$acskoka = "効果 $item[19]";
$waza_ritu = int(($chara[11] / 10)) + 10 + $a_wazaup;
if($waza_ritu > 90){$waza_ritu = 90;}
$hissatu_ritu = $waza_ritu + int($chara[12]/4);
$hit_ritu = int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16];
$sake = int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17];
if($item[20]){$bukilv="+ $item[20]";}
if($item[22]){$bogulv="+ $item[22]";}
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
       print <<"EOM";
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">キャラクターデータ</td></tr>
EOM
if($chara[50] == 1){
       print <<"EOM";
<td rowspan="6" align="center" valign=bottom class="b2">
EOM
}else{
       print <<"EOM";
<td rowspan="6" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$chara[6]]">
EOM
}
$rensyo = int($chara[20]*100000)/100000;
       print <<"EOM";
<tr><td id="td2" class="b2">武器</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
<td id="td2" class="b2">ペット</td><td align="center" class="b2">$pename</td></tr>
<tr><td id="td2" class="b2">防具</td><td align="right" class="b2">
<A onmouseover="up('$bogukoka')"; onMouseout="kes()"><font color="$w">$item[3] $bogulv</font></A></td>
<td id="td2" class="b2">HP</td><td align="center" class="b2">$chara[42]\/$chara[43]</td></tr>
<tr><td id="td2" class="b2">アクセサリー</td><td align="right" class="b2">
<A onmouseover="up('$acskoka')"; onMouseout="kes()">$item[6]</A></td>
<td id="td2" class="b2">ペットレベル</td><td align="center" class="b2">$chara[46]</td></tr>
<tr><td id="td2" class="b2">称号</td><td align="center" class="b2"><font color=yellow>$syou</font></td>
<td id="td2" class="b2">ペット経験値</td><td align="center" class="b2">$chara[40]\/$chara[41]</td></tr>
</table>

<table width='100%'>
<tr><td id="td1" colspan="5" class="b2" align="center">ステータス</td></tr>
<tr><td class="b1" id="td2">善良度</td><td class="b2">$chara[64]</td>
<td id="td2" align="center" class="b1">悪人度</td><td class="b2"><b>$chara[65]</b></td></tr>
<tr><td class="b1" id="td2">ジョブ</td><td class="b2">$chara_syoku[$chara[14]]</td>
<td id="td2" align="center" class="b1">ジョブLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">レベル</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">経験値</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">お金</td><td class="b2">$chara[19]\/$gold_max</td></tr>
<tr><td class="b1" id="td2">命中力</td><td class="b2">$hit_ritu</td>
<td class="b1" id="td2">回避力</td><td class="b2">$sake</td></tr>
<tr><td class="b1" id="td2">会心率</td><td class="b2">$waza_ritu %</td>
<td class="b1" id="td2">必殺率</td><td class="b2">$hissatu_ritu %</td></tr>
<tr><td class="b1" id="td2">パーティ</td><td class="b2">$chara[61]</td>
<td class="b1" id="td2">ギルド</td><td class="b2">$chara[66]</td></tr>
<tr><td class="b1" id="td2">連戦中連勝率</td><td class="b2">$rensyo</td>
<td class="b1" id="td2">転生回数</td><td class="b2">$chara[37]</td>
</tr>
<tr><td colspan="4">
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">能\力\値</td></td></tr>
</table>
<table width="100%">
<tr><td class="b1" id="td2">STR</td>
<td align="left" class="b2"><b>$chara[7] + $item[8]</b></td>
<td class="b1" id="td2">INT</td>
<td align="left" class="b2"><b>$chara[8] + $item[9]</b></td></tr>
<tr><td class="b1" id="td2">DEX</td>
<td align="left" class="b2"><b>$chara[9] + $item[10]</b></td>
<td class="b1" id="td2">VIT</td>
<td align="left" class="b2"><b>$chara[10] + $item[11]</b></td></tr>
<tr><td class="b1" id="td2">LUK</td>
<td align="left" class="b2"><b>$chara[11] + $item[12]</b></td>
<td class="b1" id="td2">EGO</td>
<td align="left" class="b2"><b>$chara[12] + $item[13]</b></td></tr>
</table></td></tr>
<tr>
<td class="b1" id="td2">チャンピオンを目指す</td>
EOM
$gold = int($winner[50] / 10000);
if($chara[140]==2){print "<form action=\"$scriptb2\" name=\"champ_battle\">";}
elsif($chara[140]==3){print "<form action=\"$scriptb3\" name=\"champ_battle\">";}
elsif($chara[140]==4){print "<form action=\"$scriptb4\" name=\"champ_battle\">";}
elsif($chara[140]==5){print "<form action=\"$scriptb5\" name=\"champ_battle\">";}
else{print "<form action=\"$scriptb\" name=\"champ_battle\">";}
	print <<"EOM";
<td colspan="3" align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
EOM
	if ($winner[0] eq $chara[0]) {
		print "現在チャンプなので闘えません\n";
	} elsif ($winner[40] eq $chara[0] and $chanp_milit == 1) {
		print "チャンプと戦った直後なので疲れて闘えません\n";
	}elsif($ltime > $b_time) {
		print "<input type=\"submit\" class=btn value=\"チャンプに挑戦\">\n";
	}else{        print "<input type=submit class=btn value=\"チャンプに挑戦\" name=\"battle_start\" disabled>\n";    }
	print <<"EOM";
<br>※賞金：$gold G
</td></form>
</tr>
EOM
if($chara[0] eq "jupiter" or $chara[18] > 10000){
	print <<"EOM";
<tr><td class="b1" id="td2">チャット欄を攻撃する</td>
<form action="kougeki.cgi" >
<td colspan="3" align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="攻撃！！" disabled>
<br>※管理人、もしくはレベル10000以上の人のみ。
</td></form></tr>
EOM
}
	print <<"EOM";
</table>
</td>
EOM

# ここから右半分のテーブル
	print <<"EOM";
<td valign="top">
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">街の施設</td></tr>
<tr>
<td bgcolor="#cbfffe" align="center">【旅の宿】(<b>$yado_daix</b>G)</td>
<td bgcolor="#cbfffe" align="center">【商店街】</td>
<td bgcolor="#cbfffe" align="center">【アイテム倉庫】</td>
<td bgcolor="#cbfffe" align="center">【銀行】</td>
</tr>
<tr>
<form action="$scripty" >
<td align="center" class="b2">
<input type=hidden name=mode value="yado">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="体力を回復"></td>
</form>
<form action="shops.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="商店街"></td>
</form>
<form action="$script_souko" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="アイテム倉庫"></td>
</form>
<form action="$script_bank" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="銀行"></td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【ステータスの変更】</td>
<td bgcolor="#cbfffe" align="center">【ステ振り所】</td>
<td bgcolor="#cbfffe" align="center">【転職の神殿】</td>
<td bgcolor="#cbfffe" align="center">【アビリティ】</td>
</tr><tr>
<td align="center" class="b2">
<form action="$scriptst" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステータスの変更">
</td>
</form>
<form action="shop_ability.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステ振り所">
</td>
</form>
<form action="syokuchange.cgi" >
<td align="center" class="b2">
<input type=hidden name=mode value=tensyoku>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="転職の神殿">
</td>
</form>
<form action="abilitychange.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="アビリティ">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【ペット】</td>
<td bgcolor="#cbfffe" align="center">【牧場】</td>
<td bgcolor="#cbfffe" align="center">【フリマ】</td>
<td bgcolor="#cbfffe" align="center">【酒場】</td>
</tr>
<tr>
<form action="petsts.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="ペット">
</td>
</form>
<form action="bokujyo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="牧場">
</td>
</form>
<form action="market.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="フリマ">
</td>
</form>
<form action="sakaba.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="酒場">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【クエスト】</td>
<td bgcolor="#cbfffe" align="center">【鍛冶屋】</td>
<td bgcolor="#cbfffe" align="center">【製造所】</td>
<td bgcolor="#cbfffe" align="center">【新世界】</td>
</tr><tr>
<form action="quest.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="クエスト">
</td>
</form>
<form action="kaji.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="鍛冶屋">
</td>
</form>
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="製造所">
</td>
</form>
<form action="anotherworld.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="新世界">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【緊急所】</td>
<td bgcolor="#cbfffe" align="center">【予\報\所】</td>
<td bgcolor="#cbfffe" align="center">【鉱山】</td>
<td bgcolor="#cbfffe" align="center">【情報屋】</td>
</tr><tr>
<form action="kinkyuu.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="緊急所">
</td>
</form>
<form action="yohou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="予\報\所">
</td>
</form>
<form action="kouzan.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="鉱山">
</td>
</form>
<form action="jyoho.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="情報屋">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【ギルド】</td>
<td bgcolor="#cbfffe" align="center">【攻城戦】</td>
<td bgcolor="#cbfffe" align="center">【畑】</td>
<td bgcolor="#cbfffe" align="center">【支配者施設】</td>
</tr><tr>
<form action="guild.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ギルド">
</td>
</form>
<form action="g_b.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="攻城戦">
</td>
</form>
<form action="hatake.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="畑">
</td>
</form>
<form action="sihai.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="支配者施設">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【謎の組織】</td>
<td bgcolor="#cbfffe" align="center">【賞金首】</td>
<td bgcolor="#cbfffe" align="center">【刑務所】</td>
<td bgcolor="#cbfffe" align="center">【ランキング】</td>
</tr>
<tr>
<form action="sosiki.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="謎の組織">
</td>
</form>
<form action="syoukin.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="賞金首">
</td>
</form>
<form action="keimusyo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="刑務所">
</td>
</form>
<form action="seirank.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ランキング">
</td>
</form>
</tr>
EOM
if($chara[70] < 1){
	print <<"EOM";
<tr>
<td bgcolor="#cbfffe" align="center">【合成所】</td>
<td bgcolor="#cbfffe" align="center">【配合所】</td>
<td bgcolor="#cbfffe" align="center">【限界突破】</td>
<td bgcolor="#cbfffe" align="center"></td>
</tr>
<tr>
<form action="gosei.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="合成所">
</td>
</form>
<form action="haigo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="配合所">
</td>
</form>
<form action="genkai.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="限界突破">
</td>
</form>
<td align="center" class="b2">
</td>
</tr>
EOM
}else{
	print <<"EOM";
<tr>
<td bgcolor="#cbfffe" align="center">【成長所】</td>
<td bgcolor="#cbfffe" align="center">【工房】</td>
<td bgcolor="#cbfffe" align="center">【加工所】</td>
<td bgcolor="#cbfffe" align="center">【依頼所】</td>
</tr>
<tr>
<form action="seityo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="成長所">
</td>
</form>
<form action="koubou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="工房">
</td>
</form>
<form action="kako.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="加工所">
</td>
</form>
<form action="ippatu.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="依頼所">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【名前変更所】</td>
<td bgcolor="#cbfffe" align="center">【アイコン所】</td>
<td bgcolor="#cbfffe" align="center">【屋敷】</td>
<td bgcolor="#cbfffe" align="center">【闇空間】</td>
</tr>
<tr>
<form action="name.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="名前変更所">
</td>
</form>
<form action="icon.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="アイコン所">
</td>
</form>
<form action="yashiki.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="屋敷">
</td>
</form>
<form action="yami.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="闇空間">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">【訓練所】</td>
<td bgcolor="#cbfffe" align="center">【正義の館】</td>
<td bgcolor="#cbfffe" align="center">【悪魔の館】</td>
<td bgcolor="#cbfffe" align="center">【便利屋】</td>
</tr>
<tr>
<form action="kunren.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="訓練所">
</td>
</form>
<form action="seigi.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="正義の館">
</td>
</form>
<form action="akuma.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="悪魔の館">
</td>
</form>
<form action="benri.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="便利屋">
</td>
</form>
</tr>
EOM
}
	print <<"EOM";
</table>
<table width="100%">
<tr><td id="td1" colspan="2" class="b2" align="center">冒険に出かける</td></tr>
<tr>
<td class="b1" id="td2">周辺の探索</td>
<form action="$scriptm"  name="monster_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=monster>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
if(!$chara[21]) {print "一度チャンピオンと戦って下さい\n";
} else { 
	if($chara[140]==2){
		$opt = "<option value=\"monster8\">イエローワールド";
	} elsif($chara[140]==3){
		$opt = "<option value=\"monster9\">レッドワールド";
	} elsif($chara[140]==4){
		$opt = "<option value=\"monster10\">ドラゴンワールド";
		$opt .= "<option value=\"monster12\">ドラゴンヘブン";
	} elsif($chara[140]==5){
		$opt = "<option value=\"monster17\">天界";
	} else {
		$opt = <<"EOM";
		<option value="monster0">平原モンテヴィーヌ
		<option value="monster1">洞窟ラヴォス
		<option value="monster2">底なしの泥沼
		<option value="monster3">闇山脈チャランラッツ
		<option value="monster4">ダーク・エリア
		<option value="monster5">神の塔エルヴァーヌ
		<option value="monster6">スペシャルエリート
		<option value="monster7">死者ゆく場所
EOM
	}
	if ($chara[140]!=5 and $chara[70] >= 1) {
		$opt .= "<option value=\"monster15\">ガッカリ村\n";
		$opt .= "<option value=\"monster16\">終わりの町\n";
		$opt .= "<option value=\"monster30\">猿猫村\n";
		$opt .= "<option value=\"monster31\">猿猫町地下\n";
		$opt .= "<option value=\"monster14\">サンタの基地\n";
		#$opt .= "<option value=\"monster18\">テスト中\n";
	}
	if ($chara[93]>0) {
		$opt .= "<option value=\"monster29\">警察署\n";
	}
	if ($chara[140]!=5 and $chara[163] >= 1) {
		$opt .= "<option value=\"monster28\">†裏ジュピタ†の本拠地\n";
	}
	if ($chara[127] == 1 or $chara[176] == 1) {
		$opt .= "<option value=\"monster27\">超魔王の城\n";
	}
	if ($ltime >= $m_time or !$chara[21]) {
		print <<"EOM";
		<select name="mons_file">$opt</select>
		<input type=submit class=btn value="モンスターと闘う">
EOM
	}else{
		print <<"EOM";
		<select name="mons_file" disabled>$opt</select>
		<input type=submit class=btn value="モンスターと戦う" name="battle_start" disabled>
EOM
	}
	print <<"EOM";
	</td>
	</form>
</tr>
<tr><td colspan=2>※修行の旅にいけます。</td></tr>
EOM
}
if($chara[27]%5 == 0){
	print <<"EOM";
<tr>
<td class="b1" id="td2">突然の出現</td>
<form action=\"$scriptm\" method=\"post\" name="gennei_battle">
<td align=\"center\" class=\"b2\">
<input type=hidden name=mode value=genei>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "１度モンスターと戦って下さい\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"幻影の城へ\">\n";
	} else {
		print qq|<input type=submit class=btn value="幻影の城へ" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>※財宝が眠ると言われる「幻影の城」にいけます。</td></tr>
EOM
}
	print <<"EOM";
<tr>
<td class="b1" id="td2">レジェンドプレイス</td>
<form action="$script_legend"  name="legend_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=boss>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21] || $chara[28] != $bossd) {
		print "１度モンスターと戦って下さい\n";
	} else {
		my $opt = qq|<option value="0">うわさのほこら\n|;
		if ($chara[32] > 0) {
			$opt .= "<option value=\"1\">古の神殿\n";
		}
		if ($chara[32] > 1) {
			$opt .= "<option value=\"2\">勇者の洞窟\n";
		}
		if ($chara[32] > 2) {
			$opt .= "<option value=\"3\">ガイアフォース\n";
		}
		if ($chara[193]==1){
			$opt .= "<option value=\"4\">アンクドラルフォース\n";
		}
		if ($ltime >= $m_time or !$chara[21]) {
			print <<"EOM";
			<select name="boss_file">$opt</select>
			<input type=submit class=btn value="伝説に挑む">
EOM
		} else {
			print <<"EOM";
			<select name="boss_file" disabled>$opt</select>
			<input type=submit class=btn value="伝説に挑む" name="battle_start" disabled>
EOM
		}
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>※でんせつの場所へ訪れることができます。</td></tr>
EOM
	print <<"EOM";
<tr>
<td class="b1" id="td2">ギルドダンジョン</td>
<form action="guild_battle.cgi"  name="guild_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=guild_battle>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	$opt = <<"EOM";
		<option value="guild0">天界への洞穴
		<option value="guild1">天界の部屋
EOM
	if($chara[70]>=1 and $chara[18]>1000){
	$opt .= <<"EOM";
		<option value="guild2">高天原
EOM
	}
	if(!$chara[66]){
		print "ギルドに加入していません。<br>\n";
	} elsif ($chara[70]==1 and $chara[18]<70){
		print "レベルが足りません。<br>\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		print <<"EOM";
		<select name="guild_file">$opt</select>
		<input type=submit class=btn value="ギルドダンジョンへ">
EOM
    } else {
		print <<"EOM";
		<select name="guild_file" disabled>$opt</select>
		<input type=submit class=btn value="ギルドダンジョンへ" name="battle_start" disabled>
EOM
    }

	print <<"EOM";
</td></form></tr>
<tr><td colspan=2>※ギルド加入者のみ挑戦できる、世にも恐ろしいダンジョンです。</td></tr>
EOM
	print <<"EOM";
<tr>
<td class="b1" id="td2">異世界</td>
<form action="$scriptm"  name="isekai_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=isekiai>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if ($chara[18] < $isekai_lvl) {
		print "レベルが$isekai_lvlを超えるまで行けません。<br>\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"異世界へ行く\"><br>\n";
	} else {
		print qq|<input type=submit class=btn value="異世界へ行く" name="battle_start" disabled>\n|;
	}

	print <<"EOM";
</td></form></tr>
<tr><td colspan=2>※神々の領域と言われるこの世界に足をふみいれて、無事に帰ったものは誰一人いない・・・</td></tr>
EOM
open(IN,"sihaisya.cgi");
@sihai_data = <IN>;
close(IN);
foreach (@sihai_data) {
	@sihaisya = split(/<>/);
	if($sihaisya[0]){last;}
}
$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);
if($point <= 10000){
	print <<"EOM";
<tr>
<td class="b1" id="td2">支配者ダンジョン</td>
<form action=\"$scriptm\" method=\"post\" name="sihai_battle">
<td align=\"center\" class=\"b2\">
<input type=hidden name=mode value=sihaid>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "１度モンスターと戦って下さい\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"支配者ダンジョン\">\n";
	} else {
		print qq|<input type=submit class=btn value="支配者ダンジョン" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>※入場料：$sihaisya[2] G</td></tr>
EOM
}
if($chara[27]%2 == 0 and $chara[70] >= 1){
	print <<"EOM";
<tr><td class="b1" id="td2">突然の出現</td>
<form action="$scriptm"  name="ijigen_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=ijigen>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "１度モンスターと戦って下さい\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"次元の狭間へ\"><br>\n";
	} else {
		print qq|<input type=submit class=btn value="次元の狭間へ" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr><tr><td colspan=2>※この世で最も危険な場所です。覚悟なしにはいかないでください。</td></tr>
EOM
}
	print <<"EOM";
</table></td></tr>
</table>
EOM

	&footer;

	exit;
}
