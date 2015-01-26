#---------------------------------------------------------------#
#　ChatSystem ver2.10 ライブラリ
#　Edit by Lost
#　http://kirbys.oo.lv/
#---------------------------------------------------------------#

# チャット設定の読み込み
require 'chat_conf.cgi';

#------------------#
#　チャット表示　　#
#------------------#
sub chat_post {

	$size_list="";
	$list=0;
	foreach (@size_num) {
		$size_list.="<option value = \"$_\">$size_list[$list]";
		$list++;
	}

	$color_list="";
	$list=0;
	foreach (@color_num) {
		$color_list.="<option value = \"$_\" style=\"color:$_\">$color_list[$list]";
		$list++;
	}
		$room_list="";
		$list="";
	foreach(@chat_room){

		$room_list.="<option value = \"$_\">$room_list[$list]";		
		$list++;
	}
	$mes_s=0;
	#if($chara[$color_chara] ne ""){ $mes_c = $chara[$color_chara]; }
	#if($chara[$size_chara] ne ""){ $mes_s = $chara[$size_chara]; }
	$style_v = "";
	#if($chara[$style_chara] ne ""){ $style_v = $chara[$style_chara]; }

print <<"EOM";
<SCRIPT type="text/javascript">
<!--
function autoclear() {
self.document.send.cmes.value = "";
self.document.send.cmes.focus();
}
// -->
</SCRIPT>
<TABLE align="center"width="100%">
<TR><TD id="td1" align="center" class="b2">チャット</TD></TR>
<form action="menu.cgi" method="post" target="chat_load" name="send" ONSUBMIT="setTimeout(&quot;autoclear()&quot;,10)">
<TR><td id="td2" class="b2" align=right colspan="2">
<input type="hidden" name="mode" value="chat_mes">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="style" value="$style_v">
<input type="text" name="cmes" size=100 value="">
<input type=submit class=btn value=" 発言/更新 ">
</TD></TR>
<TR><td id="td2" class="b2" align=right>
<select name=font_size size=1>
<optgroup label="文字サイズ">
<option value="$mes_s">標準
$size_list
</select>
<select name=font_color size=1>
<optgroup label="文字色">
<option value="$mes_c" style="color:$mes_c">標準
$color_list
</select>
<input type="checkbox" name="font_bold" value="強調">強調
<input type="checkbox" name="font_ital" value="斜体">斜体
<input type="checkbox" name="font_line" value="取消">取り消し線
<select name=room size=1>
<optgroup label="部屋">
<option value="">雑談
$room_list
</select>
<input type="reset" class=btn value="クリア">
</TD></form>
</TR>
<TR><td id="td2" class="b2" colspan="2">
<iframe src="menu.cgi" width="100%" height="200" scrolling="yes" frameborder="0" name="chat_load"></iframe>
</TD></TR>
</TABLE>
EOM
}
1;