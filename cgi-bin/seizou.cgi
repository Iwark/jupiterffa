#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

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

if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="seizou.cgi" >
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

	if($chara[63]>=1){&error("入所中です！！");}

	&header;

	print <<"EOM";
<h1>製造所</h1>
<hr size=0>
<FONT SIZE=3>
<B>製造所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここでは製造ができるぜ・・・<br>
製造に使用するアイテムは攻城戦かなんかで用意しとくんだな。<br>
それか・・・まぁ、闇の組織から買ってもいいだろう…。<br>
製造成功確率はおよそ75％ってとこか。まぁ死力は尽くすが。<br>
また、合成石の換金と、特殊合成石による製造アイテムの製造ができるぞ。<br>
合成石は１つ10万Ｇ、特殊合成石による製造品の製造成功率は７５％だ。<br>
さらにさらに、最近壊れた装備のリサイクルも始めたんだ。成長所で壊れたら、持ってこい。<br>
製造アイテムを作ってやるぜ？ただし、パワー値が低いと確率も低い上に良い製造アイテムはできないぞ。」
</FONT>
<br>現在の所持金：$chara[19] Ｇ<br>
合成石の所持：$chara[99] 個<br>
壊れた装備の累計パワー：$chara[85]<br>
<br>
EOM
if($chara[99]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kankin">
<input type=submit class=btn value="合成石換金">
</form>
EOM
}
if($chara[98]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tokusyu">
<input type=submit class=btn value="特殊合成石製造">
</form>
EOM
}
if($chara[85]){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="recycle">
<input type=submit class=btn value="壊れた装備のリサイクル">
</form>
EOM
}
if($chara[136]>=10){
	print <<"EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="kinka">
<input type=submit class=btn value="金貨１０枚を割る">
</form>
EOM
}
if($chara[18]>=100){
	print <<"EOM";
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="kaisya" value="1">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<input type=submit class=btn value="闇の組織から高額で購入">
</td>
</form>
EOM
}
	print <<"EOM";
<table width = "100%">
<tr>
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="seizou">
<td width = "50%" align = "center" valign = "top">
製造使用品Ｎｏ１
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>所持数</th></tr>
EOM
	for ($i=71;$i<=82;$i++) {
		if($chara[$i]){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($syoukyu,$sno,$sname) = split(/<>/);
				if($sno eq $i){last;}
			}
			print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no1 value="$sno">
</td>
<td class=b1 nowrap>$sname</td>
<td align=right class=b1>$chara[$i]</td>
</tr>
EOM
		}
	}
		print << "EOM";
</table>
</td>
<td width = "50%" align = "center" valign = "top">
製造使用品Ｎｏ２
<table width = "98%">
<tr><th></th><th nowrap>なまえ</th><th nowrap>所持数</th></tr>
EOM
	for ($i=71;$i<=82;$i++) {
		if($chara[$i]){
			open(IN,"seisan.cgi");
			@seisan_data = <IN>;
			close(IN);
			foreach(@seisan_data){
				($syoukyu2,$sno2,$sname2) = split(/<>/);
				if($sno2 eq $i){last;}
			}
			print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no2 value="$sno2">
</td>
<td class=b1 nowrap>$sname2</td>
<td align=right class=b1>$chara[$i]</td>
</tr>
EOM
		}
	}
		print << "EOM";
</table>
</td>
<table>
<br><br>
<input type=submit class=btn value="製造する">
</table>
</form>
</table>
EOM
if($chara[70]>=1 and $chara[18]>=100){
		print << "EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tsusinsell">
<table width="98%">
<tr><td class=b1 align=\"center\">自分：</td>
EOM
$hit=0;
for ($iti=71;$iti<=82;$iti++) {
	if($chara[$iti]){
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($itiyoukyu,$itino,$itiname) = split(/<>/);
			if($itino eq $iti){$hit=1;last;}
		}
		print "<td class=b1 align=\"center\"><input type=radio name=jibun value=\"$itino\"></td>";
		print "<td class=b1 align=\"center\">$itiname</td>";
	}
}
	print "</tr><tr><td class=b1 align=\"center\">相手：</td>";
foreach(@seisan_data){
	($itiyoukyu,$ititno,$ititname) = split(/<>/);
	if($itino eq $iti){$hit=1;last;}
	print "<td class=b1 align=\"center\"><input type=radio name=aite value=\"$ititno\"></td>";
	print "<td class=b1 align=\"center\">$ititname</td>";
}
	print "</tr></table>";
if($hit){print "<p><input type=submit class=btn value=\"共同製造準備\"></form>";}
		print << "EOM";
<form action="seizou.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="tsusinbuy">
<table width="40%">
<tr><th></th><th>名前</th><th>アイテム</th><th>対象</th><th>経過日数</th></tr>
EOM
	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	$tx=0;
	foreach(@seizou_tsusin){
		($tsusinid,$tsusinname,$tsusinitem,$tsusinitemname,$tsusintaisyo,$tsusintaisyoname,$tsusintime) = split(/<>/);
		$tsusintime=int(($koktime-$tsusintime)/86400);
		if($tsusintime > 7){splice(@seizou_tsusin,$tx,1);}
			print << "EOM";
			<tr>
			<td class=b1 align="center">
EOM
			if($chara[0] ne $tsusinid){ print "<input type=radio name=tsusin value=\"$tx\">"; }
			print << "EOM";
			</td>
			<td class=b1 align="center">$tsusinname</td>
			<td class=b1 align="center">$tsusinitemname</td>
			<td align="center" class=b1>$tsusintaisyoname</td>
			<td align="center" class=b1>$tsusintime</td>
			</tr>
EOM
		$tx++;
	}
	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);
		print << "EOM";
</table><p>
<input type=submit class=btn value="共同製造">
</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	　　製造  	   #
#--------------------------#
sub seizou {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$item_no1=$in{'item_no1'};
	$item_no2=$in{'item_no2'};
	if($item_no1 eq $item_no2 and $chara[$item_no1] < 2){&error("製造アイテムの数が足りません。$back_form");}
	elsif($chara[$item_no1] <1 or $chara[$item_no2] < 1){&error("製造アイテムの数が足りません。$back_form");}

	open(IN,"seizoudata.cgi");
	@seizou_data = <IN>;
	close(IN);

	$hit=0;
	foreach(@seizou_data){
		($bango1,$bango2,$ssno) = split(/<>/);
		if($bango1 eq $item_no1 and $bango2 eq $item_no2){$hit=1;last;}
		elsif($bango2 eq $item_no1 and $bango1 eq $item_no2){$hit=1;last;}
	}
	if(!$hit or !$ssno){&error("製造先が見つかりません。$back_form");}
if(int(rand(4))<3){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_item_num = @souko_item;
	$souko_def_num = @souko_def;
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("武器倉庫がいっぱいです！$back_form");
	}
	if ($souko_def_num >= $def_max) {
		&error("防具倉庫がいっぱいです！$back_form");
	}
	if ($souko_acs_num >= $acs_max) {
		&error("アクセサリー倉庫がいっぱいです！$back_form");
	}
	if($ssno < 1000){
		open(IN,"$acs_file");
		@log_acs = <IN>;
		close(IN);

		$hit=0;
		foreach(@log_acs){
			($i_no,$i_name,$i_gold,$i_tokusyu,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$ihit,$i_kai,$i_hissatu,$i_setumei) = split(/<>/);
		if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("アクセが見つかりません。$back_form");}
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno < 2000 and $ssno > 1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("武器が見つかりません。$back_form");}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$seizouname=$i_name;
	}	
	elsif($ssno < 3000 and $ssno > 2000){
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($i_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("防具が見つかりません。$back_form");}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno > 7000 and $ssno<8000){
		$ssno=$ssno-7000;
		$chara[$ssno]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$seizouname=$sname3;
	}
	else{&error("アイテムが見つかりません！$back_form");}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が$seizounameの製造に成功しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

}else{$hh=1;$chara[85]+=1000;}

	$chara[$item_no1]-=1;
	$chara[$item_no2]-=1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($hh==0){
	print <<"EOM";
<FONT SIZE=3>
<B>製造に成功し、$seizounameを製造しました。</B><BR>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>製造に失敗しました。泣</B><BR>
<hr size=0>
EOM
}
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	合成石換金  	   #
#--------------------------#
sub kankin {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[99]){&error("合成石がありません。$back_form");}

	$chara[99]-=1;

	$chara[19]+=100000;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>合成石を換金し、10万Ｇ入手しました。</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	特殊合成石  	   #
#--------------------------#
sub tokusyu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[98]){&error("特殊合成石がありません。$back_form");}

	$chara[98]-=1;
	$rand=int(rand(100));$dhit=0;
	if($rand < 25){		$mes="製造に失敗しました（泣）";$dhit=1
	}elsif($rand < 75){	$mes="闇石を製造しました。";$chara[71]+=1;$seizouname="闇石";
	}elsif($rand < 85){	$mes="白い光を製造しました。";$chara[72]+=1;$seizouname="白い光";
	}elsif($rand < 90){	$mes="王石を製造しました。";$chara[73]+=1;$seizouname="王石";
	}elsif($rand < 94){	$mes="空豆を製造しました。";$chara[74]+=1;$seizouname="空豆";
	}elsif($rand < 97){	$mes="ダークマターを製造しました。";$chara[75]+=1;$seizouname="ダークマター";
	}elsif($rand < 99){	$mes="セブンスターを製造しました。";$chara[76]+=1;$seizouname="セブンスター";
	}else{			$mes="閃光石を製造しました。";$chara[77]+=1;$seizouname="閃光石";
	}
	if($dhit==0){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が特殊合成石から$seizounameの製造に成功しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	リサイクル  	   #
#--------------------------#
sub recycle {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$chara[85]){&error("壊れた装備がありません。$back_form");}

	$rand=int(rand($chara[85]));
	$chara[85]=0;$dhit=0;
	if($rand < 25){		$mes="製造に失敗しました（泣）";$dhit=1;
	}elsif($rand < 250){	$mes="闇石を製造しました。";$chara[71]+=1;$seizouname="闇石";
	}elsif($rand < 2500){	$mes="白い光を製造しました。";$chara[72]+=1;$seizouname="白い光";
	}elsif($rand < 4500){	$mes="王石を製造しました。";$chara[73]+=1;$seizouname="王石";
	}elsif($rand < 8000){	$mes="空豆を製造しました。";$chara[74]+=1;$seizouname="空豆";
	}elsif($rand < 15000){	$mes="ダークマターを製造しました。";$chara[75]+=1;$seizouname="ダークマター";
	}elsif($rand < 20000){	$mes="セブンスターを製造しました。";$chara[76]+=1;$seizouname="セブンスター";
	}elsif($rand < 30000){	$mes="閃光石を製造しました。";$chara[77]+=1;$seizouname="閃光石";
	}else{			$mes="復活の石を製造しました。";$chara[78]+=1;$seizouname="復活の石";
	}
	if($rand > 7500000){	$mes.="\n無属性魔法ギガブレイクを取得した。";$chara[59]=51;}
	if($dhit==0){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様がリサイクルにて$seizounameの製造に成功しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
	}
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	通信売却  	   #
#--------------------------#
sub tsusinsell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	if(!$in{'jibun'}){&error("自分の方を選択してください。$back_form");}
	if(!$in{'aite'}){&error("相手の方を選択してください。$back_form");}
	if($chara[$in{'jibun'}] < 1){&error("製造アイテムの数が足りません。$back_form");}

	open(IN,"seisan.cgi");
	@seisan_data = <IN>;
	close(IN);
	foreach(@seisan_data){
		($ssyoukyu,$ssno,$ssname) = split(/<>/);
		if($in{'jibun'}==$ssno){$jibun=$ssname;}
		if($in{'aite'}==$ssno){$aite=$ssname;}
	}

	push(@seizou_tsusin,"$chara[0]<>$chara[4]<>$in{'jibun'}<>$jibun<>$in{'aite'}<>$aite<>$koktime<>\n");

	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);

	$chara[$in{'jibun'}]-=1;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>共同製造を開始する準備を終了しました。後は同じ志を持つ者を待つのみ…。</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}
#--------------------------#
#  	通信購入  	   #
#--------------------------#
sub tsusinbuy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"allseizou.cgi");
	@seizou_tsusin = <IN>;
	close(IN);
	$tx=0;$hit=0;
	foreach(@seizou_tsusin){
		($tsusinid,$tsusinname,$tsusinitem,$tsusinitemname,$tsusintaisyo,$tsusintaisyoname) = split(/<>/);
		if($in{'tsusin'} == $tx){$hit=1;last;}
		$tx++;
	}
	if(!$hit){&error("選択していません。$back_form");}
	$item_no1=$tsusinitem;
	$item_no2=$tsusintaisyo;
	if($chara[$item_no2] < 1){&error("製造アイテムの数が足りません。$back_form");}

	splice(@seizou_tsusin,$tx,1);

	open(OUT,">allseizou.cgi");
	print OUT @seizou_tsusin;
	close(OUT);

	open(IN,"seizoudata.cgi");
	@seizou_data = <IN>;
	close(IN);

	$hit=0;
	foreach(@seizou_data){
		($bango1,$bango2,$ssno) = split(/<>/);
		if($bango1 eq $item_no1 and $bango2 eq $item_no2){$hit=1;last;}
		elsif($bango2 eq $item_no1 and $bango1 eq $item_no2){$hit=1;last;}
	}
	if(!$hit or !$ssno){&error("製造先が見つかりません。$back_form");}
if(int(rand(4))<2){
	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	$lock_file = "$lockfolder/sitem$tsusinid.lock";
	&lock($lock_file,'ST');

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$souko_item_num = @souko_item;
	$souko_def_num = @souko_def;
	$souko_acs_num = @souko_acs;

	open(IN,"$souko_folder/item/$tsusinid.cgi");
	@souko_item2 = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$tsusinid.cgi");
	@souko_def2 = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$tsusinid.cgi");
	@souko_acs2 = <IN>;
	close(IN);

	$souko_item_num2 = @souko_item2;
	$souko_def_num2 = @souko_def2;
	$souko_acs_num2 = @souko_acs2;

	if ($souko_item_num >= $item_max or $souko_item_num2 >= $item_max) {
		&error("自分か相手の武器倉庫がいっぱいです！$back_form");
	}
	if ($souko_def_num >= $def_max or $souko_def_num2 >= $def_max) {
		&error("自分か相手の防具倉庫がいっぱいです！$back_form");
	}
	if ($souko_acs_num >= $acs_max or $souko_acs_num2 >= $acs_max) {
		&error("自分か相手のアクセサリー倉庫がいっぱいです！$back_form");
	}
	if($ssno < 1000){
		open(IN,"$acs_file");
		@log_acs = <IN>;
		close(IN);

		$hit=0;
		foreach(@log_acs){
			($i_no,$i_name,$i_gold,$i_tokusyu,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$ihit,$i_kai,$i_hissatu,$i_setumei) = split(/<>/);
		if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("アクセが見つかりません。$back_form");}
		push(@souko_acs,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		push(@souko_acs2,"$i_no<>$i_name<>$i_gold<>$i_tokusyu<>$i_str<>$i_int<>$i_dex<>$i_vit<>$i_luk<>$i_ego<>$ihit<>$i_kai<>$i_hissatu<>$i_setumei<>\n");
		open(OUT,">$souko_folder/acs/$tsusinid.cgi");
		print OUT @souko_acs2;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno < 2000 and $ssno > 1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_item){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("武器が見つかりません。$back_form");}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		push(@souko_item2,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<><><>\n");
		open(OUT,">$souko_folder/item/$tsusinid.cgi");
		print OUT @souko_item2;
		close(OUT);
		$seizouname=$i_name;
	}	
	elsif($ssno < 3000 and $ssno > 2000){
		open(IN,"$def_file");
		@log_def = <IN>;
		close(IN);
		$hit=0;
		foreach(@log_def){
			($i_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ssno eq "$i_no"){ $hit=1;last; }
		}
		if(!$hit){&error("防具が見つかりません。$back_form");}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		push(@souko_def2,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$tsusinid.cgi");
		print OUT @souko_def2;
		close(OUT);
		$seizouname=$i_name;
	}
	elsif($ssno > 7000 and $ssno<8000){
		$ssno=$ssno-7000;
		$chara[$ssno]+=1;
			$lock_file = "$lockfolder/$tsusinid.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$tsusinid.cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$tsusinid.lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);
			$mem1[$ssno]+=1;
			$new_chara = '';

			$new_chara = join('<>',@mem1);

			$new_chara .= '<>';

			open(OUT,">./charalog/$tsusinid.cgi");
			print OUT $new_chara;
			close(OUT);
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$seizouname=$sname3;
	}
	else{&error("アイテムが見つかりません！$back_form");}

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が$tsusinname様と共同で$seizounameの製造に成功しました。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

}else{
		$hh=1;
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		$eg="$chara[4]様が$tsusinname様と共同で$seizounameの製造に挑戦しましたが失敗しました…。";
		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
}

	$chara[$item_no2]-=1;

	&unlock($lock_file,'ST');
	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
if($hh==0){
	print <<"EOM";
<FONT SIZE=3>
<B>製造に成功し、$tsusinname様と共同で$seizounameを製造しました。</B><BR>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B>製造に失敗しました。泣</B><BR>
<hr size=0>
EOM
}
	&shopfooter;

	&footer;

	exit;
}
sub ps_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;
if($in{'ok'}==1){
	$ps_gold = $chara[18]*10000;
	if($in{'kaisya'}!=1){&error("エラーでんがな。");}
	if($chara[19] < $ps_gold) { &error("お金が足りません"); }
	else { $chara[19] = $chara[19] - $ps_gold; }

	$chara[26] = $host;
if(int(rand(2))!=1){
	$ps_no=71+int(rand(12));
	if($ps_no>71){
	$ps_no=71+int(rand(12));
	if($ps_no>72){
	$ps_no=71+int(rand(12));
	if($ps_no>73){
	$ps_no=71+int(rand(12));
	if($ps_no>74){
	$ps_no=71+int(rand(12));
	if($ps_no>75){
	$ps_no=71+int(rand(12));
	if($ps_no>76){
	$ps_no=71+int(rand(12));
	if($ps_no>77){
	$ps_no=71+int(rand(12));
	if($ps_no>78){
	$ps_no=71+int(rand(12));
	if($ps_no>79){
	$ps_no=71+int(rand(12));
	if($ps_no>80){
	$ps_no=71+int(rand(12));
	if($ps_no>81){
	$ps_no=71+int(rand(12));
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	}
	if($chara[70]>1 and $ps_no<80){$ps_no+=int(rand(4));}
	$chara[$ps_no] += 1;
}else{
	$bossyu=$chara[34]+$chara[19];
	$chara[93]=$bossyu;
	$chara[34]=0;
	$chara[19]=0;
	$chara[84]=1;
	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=2;
	$chara[65]+=2;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}

	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>違法会社だったようだ!!!!知ってたけど!!!!<br>
$chara[4]は逮捕され、全ての所持金を没収された！！！！悪人に二歩近づきました。気をつけてね。</B><BR>
</font>
<hr size=0>
EOM
	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]様が逮捕されました。没収金額：$bossyuＧ。";

	unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(IN,"allsyoukinkubi.cgi");
	@all_syoukinkubi = <IN>;
	close(IN);
	$hit=0;
	foreach (@all_syoukinkubi) {
		@syou = split(/<>/);
		if($syou[1] eq $chara[0]){
			$hit=1;last;
		}
	}

	if($chara[65]>=80 and $hit!=1){
		$syoukingaku=$chara[18]*10000;
		$eg="$chara[4]様は悪に染まりすぎ、賞金首(賞金：$syoukingaku G)となりました。";

		unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(IN,"allsyoukinkubi.cgi");
		@all_syoukinkubi = <IN>;
		close(IN);

		unshift(@all_syoukinkubi,"1<>$chara[0]<>$chara[4]<>$syoukingaku<>\n");

		open(OUT,">allsyoukinkubi.cgi");
		print OUT @all_syoukinkubi;
		close(OUT);
	}

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&shopfooter;

	&footer;

	exit;

}
	&chara_regist;
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>何か製造品を手に入れた。</B><BR>
</font>
<hr size=0>
EOM
}else{
	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>本当に買いますか？</B><BR>
</font>
<hr size=0>
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="kaisya" value="1">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=ps_buy>
<input type=hidden name=ok value=1>
<input type=submit class=btn value="闇の組織から高額で購入">
</td>
</form>
EOM
}

	&shopfooter;

	&footer;

	exit;
}
sub kinka {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[136]<10){&error("金貨が足りません");}
	else{
		$chara[136]-=10;
		$chara[85]+=2000000;
	}

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	print <<"EOM";
<FONT SIZE=3>
<B>ばいばい、金貨。</B><BR>
<hr size=0>
EOM
	&shopfooter;

	&footer;

	exit;
}