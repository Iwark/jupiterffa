#!/usr/local/bin/perl

require 'jcode.pl';
require 'regist.pl';
require 'data/ffadventure.ini';

$midi = $title_midi;
$backgif = $backgif;

if ($mente) {
  &error("ƒo[ƒWƒ‡ƒ“ƒAƒbƒv’†‚Å‚·B‚QA‚R‚O•b‚Ù‚Ç‚¨‘Ò‚¿‰º‚³‚¢Bm(_ _)m");
}

if($link_flg){
  &link_chack;
}

&decode;

foreach (@shut_host) {
  $_ =~ s/\*/\.\*/g;
  if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
    &error("ƒAƒNƒZƒX‚Å‚«‚Ü‚¹‚ñII");
  }
}

&html_top;

sub html_top {

$non = int(rand(4));
if ($non == 3) {
  &read_winner4;
  $sity = "ƒhƒ‰ƒSƒ“ƒ[ƒ‹ƒh";
}
elsif ($non == 2) {
  &read_winner3;
  $sity = "ƒŒƒbƒhƒ[ƒ‹ƒh";
} elsif ($non == 1) {
  &read_winner2;
  $sity = "ƒCƒGƒ[ƒ[ƒ‹ƒh";
} elsif ($non == 0) {
  &read_winner;
  $sity = "ƒWƒ…ƒsƒ^ƒ[ƒ‹ƒh";
}

  &get_cookie;

  if($winner[18]) {
    $ritu = int(($winner[19] / $winner[18]) * 100);
  }
  else {
    $ritu = 0;
  }

  if($winner[4]) {
    $esex = "’j";
  } else {
    $esex = "—";
  }

  $divpm = int($charamaxpm / 100);
  $wci_plus = $winner[23] + $winner[52];
  $wcd_plus = $winner[26] + $winner[35];
  $hit_ritu = int($winner[9] / 3 + $winner[11] / 10 + $winner[30] / 3) + 40;
  $kaihi_ritu = int($winner[9] / 10 + $winner[11] / 20 + $winner[30]/10);
  $waza_ritu = int(($winner[11] / 10)) + 10;
  if($waza_ritu > 90){$waza_ritu = 90;}

  $winner[23] += $a_hitup;
  $winner[26] += $a_kaihiup;

  $date = time();

  &header;

  print <<"EOM";
<table border=0>
<tr>
<td valign="top">
<table border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">‘O‰ñ‚Ì‘±‚«</font></td></tr>
<tr><td class=b1>I D</td>
<form action="$loginscript" method="POST">
<input type="hidden" name="mode" value="log_in">
<td><input type="text" size="10" name="id" value="$c_id"></td>
<td class=b1>ƒpƒXƒ[ƒh</td>
<td><input type="password" size="10" name="pass" value="$c_pass"></td>
<td><input type="submit" class="btn" value="ƒƒOƒCƒ“"></td>
</form>
</tr>
</table>
</td><td>
EOM
  open(IN,"./charalog/test.cgi");
  @testdata = <IN>;
  close(IN);
if ($testdata[27] + 600 < $date) {
  print <<"EOM";
<table border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">ƒeƒXƒgƒvƒŒƒC</font></td></tr>
<tr>
<form action="$loginscript" method="POST">
<td>
<input type="hidden" name="mode" value="log_in">
<input type=hidden name="id" value=test>
<input type=hidden name="pass" value=test>
<input type="submit" class="btn" value="ƒeƒXƒgƒvƒŒƒC"></td>
</form>
</tr></table>
EOM
} else {
print "Œ»ÝŽg—p’†‚Å‚·<br>‚¨‘Ò‚¿‰º‚³‚¢";
}
  print <<"EOM";
</td><td>
<table border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">V‹KƒLƒƒƒ‰ì¬</font></td></tr>
<tr>
<FORM ACTION="$chara_make" METHOD="POST">
<INPUT TYPE="hidden" NAME="mode" VALUE="chara_make">
<td><input type="submit" class="btn" value="V‹KƒLƒƒƒ‰ƒNƒ^ì¬"></td>
</form>
</tr></table>
</td></tr></table>
<table border=0 width='90%'>
<tr><td align="center" talign="center" class="b1">
<MARQUEE>$telop_message</MARQUEE></td>
</tr></table>
EOM

  # –`Œ¯ŽÒ”•\Ž¦
  open(GUEST,"$guestfile");
  @member=<GUEST>;
  close(GUEST);

  $num = 0;
  $blist = '';
  foreach (@member) {
    ($ntimer,$nname,$nid) = split(/<>/);
    if($date - $ntimer < $sanka_time){
      $blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\">$nname</a><font size=1 color=#ffff00>š</font>";
      $num++;
    }
  }


  print "<font size=2 color=#aaaaff>Œ»Ý‚Ì–`Œ¯ŽÒ(<B>$numl</B>)F</font>\n";

  if ($blist) {
    print $blist;
  }
  else {
    print '’N‚à‚¢‚Ü‚¹‚ñ';
  }

  print <<"EOM";
<br>Œ»Ý‚Ì˜AŸ‹L˜^‚ÍA$winner[47]‚³‚ñ‚Ìu<A HREF=\"$winner[49]\" TARGET=\"_blank\"><FONT SIZE=\"3\" COLOR=\"#6666BB\">$winner[48]</FONT></A>vA$winner[45]˜AŸ‚Å‚·BV‹L˜^‚ðo‚µ‚½ƒTƒCƒg–¼‚Ì‰¡‚É‚ÍA<IMG SRC="$mark">ƒ}[ƒN‚ª‚Â‚«‚Ü‚·B
<table border=0 width='100%'>
<tr>
<td width="500" valign="top">
  <table border=1 width="100%">
  <tr>
  <td id="td1" colspan=5 align="center" class="b2">y$sityzƒ`ƒƒƒ“ƒv<font class="white">$winner[44]˜AŸ’†</font><br><font class = "yellow">(<a href=$scripta?mode=chara_sts&id=$winner[40]>$winner[41]</a><font class = "yellow">‚ÉŸ—˜II\[ƒTƒCƒg\]</font><A HREF=\"$winner[43]" TARGET="_blank">$winner[42]</A> )</font></td>
  </tr>
  <tr>
  <td id="td2" align="center" class="b1">ƒz[ƒ€ƒy[ƒW</td>
  <td colspan="4"><a href="$winner[2]"><b>$winner[1]</b></a>
EOM
  if($winner[49] eq $winner[2]) {
    print "<IMG SRC=\"$mark\" border=0>\n";
  }

  $kyouyuu="";
  $index=0;
  foreach (@site_url) {
    $kyouyuu.="<a href=\"$_\">$site_title[$index]</a>/";
    $index++;
    }
  if($winner[54]){$bukilv="+ $winner[54]";}
  if($winner[55]){$bogulv="+ $winner[55]";}
  print <<"EOM";
</td></tr><tr>
<td align="center" rowspan="11" valign=bottom><img src="$img_path/$chara_img[$winner[5]]"><font color=$white>$winner[18]</font>í<font color=$white>$winner[19]</font>Ÿ’†<br>Ÿ—¦F$ritu\%<br>
<table width="100%" border=1>
<tr><td id="td2" class="b2">•Ší</td><td align="center" class="b2">$winner[21] $bukilv</td></tr>
<tr><td id="td2" class="b2">–h‹ï</td><td align="center" class="b2">$winner[24] $bogulv</td></tr>
<tr><td id="td2" class="b2">ü‚è</td><td align="center" class="b2">$winner[27]</td></tr>
<tr><td id="td2" class="b2">–½’†—¦</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu + $winner[23] %</b></td></tr>
<tr><td id="td2" class="b2">‰ñ”ð—¦</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$kaihi_ritu + $winner[26] %</b></td></tr>
<tr><td id="td2" class="b2">•KŽE—¦</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $winner[35]%</b></td><td></td></tr>
</table></td><tr>
<td id="td2" align="center" class="b1">‚È‚Ü‚¦</td><td class="b2"><b>$winner[3]</b></td>
<td id="td2" align="center" class="b1">«•Ê</td><td class="b2"><b>$esex</b></td></tr>
<tr><td id="td2" align="center" class="b1">ƒWƒ‡ƒu</td><td class="b2"><b>$chara_syoku[$winner[14]]</b></td>
<td id="td2" align="center" class="b1">ƒWƒ‡ƒuLV</td><td class="b2"><b>$winner[39]</b></td></tr>
<tr><td id="td2" align="center" class="b1">ƒŒƒxƒ‹</td><td class="b2"><b>$winner[17]</b></td>
<td id="td2" align="left" class="b1">-</td><td class="b2">-</td></tr>
<tr><td id="td2" align="left" class="b1">HP</td><td class="b2"><b>$winner[15]\/$winner[16]</b></td>
<td id="td2" align="left" class="b1">Ü‹à</td><td class="b2"><b>$winner[50]</b></td></tr>
<tr><td id="td2" align="left" class="b1">STR</td><td class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$winner[7] + $winner[28]</b></td>
<td id="td2" align="left" class="b1">INT</td><td class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$winner[8] + $winner[29]</b></td></tr>
<tr><td id="td2" align="left" class="b1">DEX</td><td class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$winner[9] + $winner[30]</b></td>
<td id="td2" align="left" class="b1">VIT</td><td class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$winner[10] + $winner[31]</b></td> </tr>
<tr><td id="td2" align="left" class="b1">LUK</td><td class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$winner[11] + $winner[32]</b></td>
<td id="td2" align="left" class="b1">EGO</td><td class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$winner[12] + $winner[33]</b></td></tr>
</table>
</td>
<td valign="top">
<td valign="top" align="left">

<table width=340 border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">ƒ^ƒCƒ€ƒCƒxƒ“ƒg</font></td></tr>
<tr>
<td align=center>
EOM
($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
$mon = $mon+1;
  if ($hour >= 19 and $hour < 21){
    print '<font color=yellow>19Žž`21ŽžŒø‰ÊF‚Â‚é‚Í‚µƒhƒƒbƒv—¦+20%</font><br>';
  }
  if ($hour >= 21 and $hour < 23){
    print '<font color=yellow>21Žž`23ŽžŒø‰ÊFŽæ“¾ŒoŒ±’l+100%</font><br>';
    print '<font color=yellow>21Žž`23ŽžŒø‰ÊFƒhƒƒbƒv—¦+100%</font><br>';
  }
  if ($wday == 0){
    print '<font color=yellow>“ú—jŒø‰ÊFŽæ“¾ŒoŒ±’l+20“</font><br>';
  }
  if ($wday == 1){
    print '<font color=yellow>ŒŽ—jŒø‰ÊFŽæ“¾ŒoŒ±’l+20“</font><br>';
  }
  if ($wday == 3 and $hour >= 18 and $hour < 19){
    print '<font color=yellow>…—j“ú18Žž`19ŽžŒø‰ÊFƒhƒƒbƒv—¦+100%</font><br>';
  }
  if ($wday == 5){
    print '<font color=yellow>‹à—jŒø‰ÊFh‚Ì‘ã‹à‚ª0‚Æ‚È‚é</font><br>';
  } 
  if ($wday == 6){
    print '<font color=yellow>“y—jŒø‰ÊFƒhƒƒbƒv—¦‚Q”{II</font><br>';
  }
  if ($mday == 15 and $mon == 3){
    #ƒCƒxƒ“ƒgI
    print '<font color=yellow>“Á•ÊƒCƒxƒ“ƒgŠJÃ’†I</font><br>';
  }
  print <<"EOM";
</td>
</tr></table>

[<B><FONT COLOR=$yellow>$main_title ‚Ì—V‚Ñ•û</FONT></B>]
<OL>
<LI>‚Ü‚¸AuV‹KƒLƒƒƒ‰ƒNƒ^[“o˜^vƒ{ƒ^ƒ“‚ð‰Ÿ‚µ‚ÄAƒLƒƒƒ‰ƒNƒ^[‚ðì¬‚µ‚Ü‚·B
<LI>ƒLƒƒƒ‰ƒNƒ^[‚Ìì¬‚ªŠ®—¹‚µ‚½‚çA‚±‚Ìƒy[ƒW‚Ì¶ã‚É‚ ‚é‚Æ‚±‚ë‚©‚çƒƒOƒCƒ“‚µ‚ÄA‚ ‚È‚½ê—p‚ÌƒXƒe[ƒ^ƒX‰æ–Ê‚É“ü‚è‚Ü‚·B
<LI>‚»‚±‚Å‚ ‚È‚½‚Ìs“®‚ð‘I‘ð‚·‚é‚±‚Æ‚ª‚Å‚«‚Ü‚·B
<LI>ˆê“xƒLƒƒƒ‰ƒNƒ^[‚ðì¬‚µ‚½‚çA‰Eã‚Ì‚Æ‚±‚ë‚©‚çƒƒOƒCƒ“‚µ‚Ä—V‚Ñ‚Ü‚·BV‹K‚ÉƒLƒƒƒ‰ƒNƒ^[‚ðì‚ê‚é‚Ì‚ÍAˆêl‚Éˆê‚Â‚ÌƒLƒƒƒ‰ƒNƒ^[‚Ì‚Ý‚Å‚·B
<LI>‚±‚ê‚ÍAHPƒoƒgƒ‰[‚Å‚Í‚È‚­AƒLƒƒƒ‰ƒoƒgƒ‰[‚Å‚·BƒLƒƒƒ‰ƒNƒ^[‚ðˆç‚Ä‚Ä‚¢‚­ƒQ[ƒ€‚Å‚·B
<LI>”\\—Í‚ðU‚è•ª‚¯‚é‚±‚Æ‚ª‚Å‚«ƒLƒƒƒ‰ƒNƒ^[‚Ì”\\—Í‚ð‚²Ž©•ª‚ÅŒˆ‚ß‚é‚±‚Æ‚ª‚Å‚«‚Ü‚·B(‚±‚±‚ÅŒˆ‚ß‚½”\\—Í‚Í‚²‚­‚Ü‚ê‚É‚µ‚©ã¸‚µ‚È‚¢‚Ì‚ÅATd‚É)
<LI><b>$limit“ú</b>ˆÈã“¬‚í‚È‚¯‚ê‚ÎAƒLƒƒƒ‰ƒNƒ^[‚Ìƒf[ƒ^‚ªíœ‚³‚ê‚Ü‚·B
<LI>ˆê“xí“¬‚·‚é‚Æ<b>$b_time</b>•bŒo‰ß‚µ‚È‚¢‚ÆÄ‚Ñí“¬‚Å‚«‚Ü‚¹‚ñB
</OL>
</td>
</tr>
</table>
<hr size=0>
<!--
<font color=$white>‹¤—LÝ’uŽÒ/<a href="$homepage" TARGET="_top">$home_title</a> / $kyouyuu<br>
<font color=$white>ƒƒjƒ…[/</font><a href="$scripta?mode=ranking">“o˜^ŽÒˆê——</a> / <a href="$ranking">\”\\—Í•Êƒ‰ƒ“ƒLƒ“ƒO‚Ö</a> / <a href="$syoku_html" target="_blank">ŠeE‹Æ‚É•K—v‚È“Á«’l</a> /<a href="$img_all_list" target="_blank">$vote_gazou</a> /<a href="$bbs">$bbs_title</a> /<a href="$helptext" target="_blank">$helptext_url</a><br>
<font color=$white>’¬‚ÌŠO‚ê/</font><a href="$sbbs">$sbbs_title</a> / <a href="$vote">$vote_title</a> /<br>
-->
<table border=0 width="100%">
‚e‚e‚`Ý’uƒ‰ƒ“ƒLƒ“ƒO‚É“o˜^’†‚Å‚·B“Š•[‚ÍƒNƒŠƒbƒN¨<A href="http://www.seijyuu.com/game/link/in.cgi?kind=ffa&id=kohe&mode=top" target="_blank">–³—¿ƒQ[ƒ€Ý’uƒTƒCƒgƒ‰ƒ“ƒLƒ“ƒOyFF ADVENTURE z</A>
<TR><TD class="b1" bgcolor="#000000" align="center"><B>˜A—Ž–€</B></font></TD></TR>
<TR><TD class="b2">$kanri_message</TD></TR></table>

<form action="$scriptk" method="POST">
<table><td><input type="password" size="10" name="pass"></td>
<td><input type="submit" class="btn" value="ŠÇ—ŽÒ"></td>
</tr></table></form>
EOM

  &footer;

  exit;
}

sub get_cookie {
  @pairs = split(/;/, $ENV{'HTTP_COOKIE'});
  foreach (@pairs) {
    local($key,$val) = split(/=/);
    $key =~ s/\s//g;
    $GET{$key} = $val;
  }
  @pairs = split(/,/, $GET{$ffcookie});
  foreach (@pairs) {
    local($key,$val) = split(/<>/);
    $COOK{$key} = $val;
  }
  $c_id  = $COOK{'id'};
  $c_pass = $COOK{'pass'};
}

sub link_chack {
  $geturl = $ENV{'HTTP_REFERER'};
  $guid ="<H1>ŒÄ‚Ño‚µŒ³‚ª³‚µ‚­‚ ‚è‚Ü‚¹‚ñII</H1>";
  if ($top_url) {
    $guid.="<a href=\"$top_url\">$top_url</a>‚©‚ç“ü‚è‚È‚¨‚µ‚Ä‚­‚¾‚³‚¢B";
  }
  else{
    $guid.="<font color=$yellow size=4>‹¤—LƒTƒCƒgˆê——</font>";
    $index=0;
    foreach (@site_url) {
      $guid.="<a href=\"$_\">$site_title[$index]</a>/";
      $index++;
    }
  }
  if($geturl eq ""){
    &header;
    print "<center><hr width=400><h3>ERROR !</h3>\n";
    print "<font color=$red><B>$guid</B></font>\n";
    print "<hr width=400></center>\n";
    print "</body></html>\n";
    exit;
  } 
}
