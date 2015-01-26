#!/usr/local/bin/perl

#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトを使用したいかなる損害に対しても             #
#    作者は一切の責任を負いませんし負えません。                 #
# 2. これに関する質問は掲示板かメールでよろしくです             #
#   余談ですが作者は                                            #
#   http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/       #
#   ↑ここ辺にいます                                            #
#---------------------------------------------------------------#

##############
#変数設定開始#
##############

#▼タイトル等の色
$col_1 = "#000000";

#▼投稿ナンバーと◇の色
$col_2 = "#5588FF";

#▼メッセージと名前の色
$col_3 = "#333333";

#▼時刻の色
$col_4 = "#CCCCCC";

#入力フォームの線の色(IEのみ)
$form_line = "#000000";

#入力フォームの背景色(IEのみ)
$form_col = "#FFFFFF";

#▼文字の大きさ
$fontsize = "13px";

#▼リクエストメソッドの設定
$form = "POST";

#▼埋め込み表示最高メッセージ数
$maxmes = "18";

#▼保存メッセージ数
$maxmes2 = "200";

#▼このファイルのフルパス(http://から)
$pppbbsmini = "http://w2.abcoroti.com/~ffajupiter/cgi-bin/pppbbsmini.cgi";

#▼テンプレートファイルのアドレス(相対パス)
$templ = "./temp.html";

#▼書き出すHTMLログファイル(実際にアクセスするファイル)のパス
#相対パスで指定して下さい
#パーミッション[666]で作成
$mainf = "../index.html";

#▼HTMLログファイルのフルパス(http://から、最後にスラッシュ[/]はいりません)
$htmlog = "http://127.0.0.1/cgi-bin/cgilabo/index.html";

#▼ログファイルのパス(相対パス)
#パーミッション[666]で作成する
$lfile = "./log.cgi";

#テーブル用の画像があるディレクトリのフルパス(http://から、最後にスラッシュ[/]はいりません)
$image_dir = "http://127.0.0.1/cgi-bin/cgilabo/images";

#▼各イメージのパス、番号はreadmeの中で説明している枠の番号です
#画像を入れないところはスペーサー画像で埋めておいて下さい
$table01 = "table1.gif";
$table02 = "space.gif";
$table03 = "table2.gif";
$table04 = "space.gif";
$table05 = "space.gif";
$table06 = "space.gif";
$table07 = "space.gif";
$table08 = "space.gif";
$table09 = "space.gif";
$table10 = "table3.gif";
$table11 = "table4.gif";

#▼テーブルの高さの設定
#○番ってのは付属のreadmeの中で説明している枠の番号です

#１番の高さ
$height1 = "15";
#４番の高さ
$height4 = "0";
#７番の高さ
$height7 = "20";
#１０番の高さ
$height10 = "15";

#１番の幅
$width1 = "15";
#２番の幅
$width2 = "800";
#３番の幅
$width3 = "15";

#▼メッセージの最高半角文字数
$mesmax = "60";

#▼名前の最高半角文字数
$namemax = "10";

#▼メールアドレスの半角最高文字数
$mailmax = "50";

#▼使い方＆過去ログ画面に出るコメント
$howto =<<"EOH";
<!--ココから-->

<CENTER><B>★１行掲示板、注意点★</B></CENTER><br>
・名前とメッセージは必須です<br><br>
・HTMLタグは使用出来ません<br><br>
・文字数制限があります<br>
名前[半角$namemax文字]<br>
メールアドレス[半角$mailmax文字]<br>
メッセージ[半角$mesmax文字]<br><br>
・書き込みが反映されないときはリロードしてみて下さい<br><br>
・人の迷惑になるような発言は削除します<br><br>
・半角カナは文字化けするので使わないで下さい<br><br>

<!--ココまで-->
EOH

#▼HTMLの設定(過去ログ画面とエラー画面)
$bgcolor = "#DDEEFF";
$bground = "";
$textc   = "#000000";
$linkc   = "#333333";
$vlinkc  = "#444444";
$alinkc  = "#555555";

#▼埋め込み掲示版のタイトル
$title = "うめこみ掲示板";

#▼管理人削除パス
$adpass = "pass";

#▼タグを許可するか否か、許可するなら1そうでなければ0
$tagok = "0";

#▼書き込み終了時、エラー時の画面から何秒で自動的に戻るか
$backsec = "5";

###############################################################
#変数設定終了～ココからは知識を持った人が変更しましょう
###############################################################

require 'jcode.pl';

if ($ENV{'REQUEST_METHOD'} eq "POST") {
read(STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
} else {
$query_string = $ENV{'QUERY_STRING'};
}
@a = split(/&/, $query_string);
foreach $a (@a) {
($name, $value) = split(/=/, $a);
&jcode'convert(*value, "euc");
$value =~ tr/+/ /;
$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
&jcode'convert(*value, "sjis");
$in{$name} = $value;
if($name = "delno"){push(@delno,"$value");}
}

$mes   = $in{'mes'};
$name  = $in{'name'};
$url   = $in{'url'};
$mail  = $in{'mail'};
$mode  = $in{'mode'};
$pass  = $in{'pass'};

$mes  =~ s/\x0D\x0A/<BR>/g;
$mes  =~ s/\x0D/<BR>/g;
$mes  =~ s/\x0A/<BR>/g;
$name =~ tr/\x0D\x0A//d;
$mail =~ tr/\x0D\x0A//d;

unless($tagok){
$mes =~ s/</&lt;/g;
$mes =~ s/>/&gt;/g;
$name =~ s/</&lt;/g;
$name =~ s/>/&gt;/g;
}

#############################
if ($mode eq admin){&admin;}
if ($mode eq view){&view;}
if ($mode eq howto){&howto;}
if ($mode eq main){&wlog;}

&htm_main;

@main = ();
open (TEMPL,"$templ");
while(<TEMPL>){
s/<!--bbs-->/$bbs/g;
push (@main,"$_");
}
close(TEMPL);

open(FILE,">$mainf");
print FILE @main;
close(FILE);
if ($mode eq admin){&view;}
if ($mode eq main){&emes('書き込み完了！','書き込みが反映されていないときはリロードしてみて下さい');}
print "Location: $htmlog\n\n";
#############################

##################
#ログ書き込み処理#
##################
sub wlog{
unless($mes){&emes('Erorr!!','メッセージが書き込まれていません');}
unless($name){&emes('Erorr!!','名前が書き込まれていません');}

if ($namemax < length($name)){&emes('Erorr!!',"名前の文字数が制限オーバーです(半角$namemax文字まで)");}
if ($mailmax < length($mail)){&emes('Erorr!!',"メールアドレスの文字数が制限オーバーです(半角$mailmax文字まで)");}
if ($mesmax < length($mes)){&emes('Erorr!!',"メッセージの文字数が制限オーバーです(半角$mesmax文字まで)");}

&gettime;
open (MAIN,"<$lfile");
@main = <MAIN>;
close(MAIN);
$count = shift(@main);
chomp($count);
$count =~ s/\t//;
$count++;

@main2 = ();
push(@main2,"$count<:>$name<:>$mail<:>$mes<:>$date<:>\n");
$maxcount = "1";
foreach(@main){
if($maxcount >= $maxmes2) {last;}
if($_=~/^\t(.+)$/) {next;}
($count2,$name2,$mail2,$mes2,$date2) = split(/<:>/);
push(@main2,"$count2<:>$name2<:>$mail2<:>$mes2<:>$date2<:>\n");
$maxcount++;
}

open(MAIN, ">$lfile");
print MAIN "\t$count\n";
print MAIN @main2;
close(MAIN);
}

##########
#テーブル#
##########
sub htm_main {
$bbs =<<"EOH";

<!--Start pppbbsmini-->
<TABLE BORDER=0 HEIGHT="$heightall" CELLSPACING=0 CELLPADDING=0>
<TR>
<TD HEIGHT="$height1" WIDTH="$width1"><IMG SRC="$image_dir/$table01"></TD>
<TD HEIGHT="$height1" WIDTH="$width2" ALIGN="CENTER" VALIGN="bottom" BGCOLOR="#FFFFFF" background="$image_dir/$table02">
<SPAN STYLE="font-size:13px;color:$col_1">$title</SPAN></TD>
<TD HEIGHT="$height1" WIDTH="$width1"><IMG SRC="$image_dir/$table03"></TD>
</TR>

<TR>
<TD WIDTH="$width1" HEIGHT="$height4" BGCOLOR="#FFFFFF"><IMG SRC="$image_dir/$table04"></TD>
<TD WIDTH="$width2" HEIGHT="$height4" BGCOLOR="#FFFFFF" background="$image_dir/$table05">
<TABLE WIDTH="$width2" BORDER=0 CELLSPACING=0 CELLPADDING=1><tr><td colspan=3><HR size=0></td></tr>
EOH

$name_w = $fontsize * $namemax +5;

open(MAIN, "$lfile");
$i=1;
while (<MAIN>) {
if($_=~/^\t(.+)$/) {next;}
if($i >= $maxmes) {last;}
($count,$name,$mail,$mes,$date) = split(/<:>/);
$bbs .= "<tr><td width=\"$name_w\"><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">$count◇</SPAN>";
if ($mail ne ""){$bbs .= "<A HREF=\"mailto\:$mail\" style\=\"font\-size\:$fontsize\;color\:$col_3;\">$name</A></td>";}
else{$bbs .= "<SPAN style\=\"font\-size\:$fontsize\;color\:$col_3;\">$name</SPAN></td>";}
$bbs .= "<td><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">◇</SPAN><SPAN style\=\"font\-size\:$fontsize\;color\:$col_3;\">$mes</SPAN></td><td><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">◇</SPAN><SPAN STYLE=\"font\-size\:11px\;\ color\:$col_4\;\">$date</SPAN></td></tr>\n";
$i++;
}
close(MAIN);

$bbs .=<<"EOH";
<tr><td colspan=3><HR size=0></td></tr>
</TABLE></TD>
<TD WIDTH="$width3" HEIGHT="$height4" BGCOLOR="#FFFFFF"><IMG SRC="$image_dir/$table06"></TD>
</TR>

<TR>
<TD WIDTH="$width1" HEIGHT="$height7" BGCOLOR="#FFFFFF"><IMG SRC="$image_dir/$table07"></TD>
<FORM METHOD=$form ACTION="$pppbbsmini">
<TD WIDTH="$width2" ROWSPAN=2 BGCOLOR="#FFFFFF" background="$image_dir/$table08">
<TABLE BORDER=0 CELLSPACING=0 CELLPADDING=0><tr>
<TD><SPAN STYLE="font-size:12px;color:$col_1">name
</TD><TD><INPUT TYPE=text NAME=name SIZE=10 MAXLENGTH="$namemax" STYLE="BORDER: 1px solid $form_line; BACKGROUND-COLOR: $form_col;">&nbsp;
</TD><TD><SPAN STYLE="font-size:12px;color:$col_1">mail</SPAN>
</TD><TD><INPUT TYPE=text NAME=mail SIZE=10 MAXLENGTH="$mailmax" STYLE="BORDER: 1px solid $form_line; BACKGROUND-COLOR: $form_col;">&nbsp;
</TD><TD><SPAN STYLE="font-size:12px;color:$col_1">mes</SPAN>
</TD><TD><INPUT TYPE=text NAME=mes SIZE=40 MAXLENGTH="$mesmax" STYLE="BORDER: 1px solid $form_line; BACKGROUND-COLOR: $form_col;">&nbsp;
<INPUT TYPE="hidden" NAME="mode" VALUE="main">
</TD><TD><INPUT TYPE=submit VALUE="OK!" STYLE="BORDER: 1px solid $form_line; BACKGROUND-COLOR: $form_col;">&nbsp;
</TD><TD><A href="$pppbbsmini?mode=view" target="_blank" STYLE="font-size:12px;color:$col_1">使い方</A>
</TD></TR></TABLE>
</TD>
<TD WIDTH="$width3" HEIGHT="$height7" BGCOLOR="#FFFFFF"><IMG SRC="$image_dir/$table09"></TD>
</TR>

<TR>
<TD WIDTH="$width1" HEIGHT="$height10"><IMG SRC="$image_dir/$table10"></TD>
<TD WIDTH="$width3" HEIGHT="$height10"><IMG SRC="$image_dir/$table11"></TD>
</TR>
</FORM>
</TABLE>
<!--End pppbbsmini-->
EOH
}

##############
#現在時刻取得#
##############
sub gettime{
($second,$minute,$hour,$day,$month,$year) = localtime(time);
$year += 1900;
$month += 1;
$date = "$month/$day/$hour\:$minute";
}

################
#メッセージ表示#
################
sub emes {

print << "EOH";
Content-type: text/html; charset=Shift_JIS

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=Shift-JIS">
<META HTTP-EQUIV="Refresh" CONTENT="$backsec; url=$htmlog">
<TITLE>$_[0]</TITLE>
</HEAD>
<BODY BGCOLOR="$bgcolor" BACKGROUND="$bground" TEXT="$textc" LINK="$linkc" VLINK="$vlinkc" ALINK="$alinkc">
<hr size=0 width=300>
<FONT SIZE="6"><center>$_[0]</center></font>
<hr size=0 width=300><br>
<center>$_[1]<br>
<a href="$htmlog">ページに戻る</a><br><br><br><br><br>
<span style="font-size:11px">
<a href="http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/">てきとう君＠うめこみ</a></span></center>
</body></html>
EOH
exit;
}

##############
#過去ログ表示#
##############
sub view {

print << "EOH";
Content-type: text/html; charset=Shift_JIS

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=Shift-JIS">
<TITLE>過去ログ</TITLE>
</HEAD>
<BODY BGCOLOR="$bgcolor" BACKGROUND="$bground" TEXT="$textc" LINK="$linkc" VLINK="$vlinkc" ALINK="$alinkc">
<hr size=0>
<SPAN style="font-size:13px">
<center><table border=0><tr><td align=left>$howto</td></tr></table></center></SPAN>
<FORM ACTION="$pppbbsmini" METHOD="$form">
▼過去の記録【$maxmes2件】
<hr size=1>
EOH
open(MAIN, "$lfile");
while (<MAIN>) {
if($_=~/^\t(.+)$/) {next;}
($count,$name,$mail,$mes,$date) = split(/<:>/);
print"<INPUT TYPE=\"checkbox\" NAME=\"delno\" VALUE=\"$count\"><SPAN STYLE=\"font-size:$fontsize\">$count◇";
if ($mail ne ""){print"<A HREF=\"mailto\:$mail\">$name</A>";}
else{print"$name";}
print"◇$mes◇</SPAN><SPAN STYLE=\"font\-size\:11px\;\">$date</SPAN><HR size=0>\n";
}
close(MAIN);
print<<"EOH";
<a href="$htmlog">ページに戻る</a><br>
<INPUT TYPE="password" NAME="pass" size="10">
<INPUT TYPE="hidden" name="mode" value="admin"><INPUT TYPE="submit" VALUE="admin">
</FORM><br><br><br><br>
<span style="font-size:11px">
<center><a href="http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/">
てきとう君＠うめこみ</a></span></center>
</center></body></html>
EOH
exit;
}
######
#削除#
######
sub admin{
  if($pass ne $adpass){&emes('Erorr!!','パスワードが違います！！');}
  unless($pass){&emes('Erorr!','パスが入力されていません！！');}
  unless($delno[0]){&emes('Erorr!','削除ナンバーが入力されていません！！');}

open (MAIN, "<$lfile");
@main = <MAIN>;
close(MAIN);
@new = ();
  foreach(@main){
    if($_=~/^\t(.+)$/) {
      push(@new,"$_");
      next;}
    ($count,$name,$mail,$mes,$date) = split(/<:>/);
    $hit=0;
    foreach(@delno){
      if("$_" == "$count"){$hit=1;$last;}
    }
    if($hit){next;}
    else{push(@new,"$count<:>$name<:>$mail<:>$mes<:>$date<:>\n");}
  }

open(MAIN, ">$lfile");
print MAIN @new;
close(MAIN);

}
