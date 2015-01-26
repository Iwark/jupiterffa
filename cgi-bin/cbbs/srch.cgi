#!/usr/local/bin/perl

require './jcode.pl';

#------------------------------------------
$ver="Child Search v8.92";# (ツリー式掲示板)
#------------------------------------------
# Copyright(C) りゅういち
# E-Mail:ryu@cj-c.com
# W W W :http://www.cj-c.com/
#------------------------------------------

#---[設定ファイル]-------------------------

# 同じようにいくつでも増やせます。
# [ ]内の数字を使いCGIにアクセスするとその設定ファイルで動作します。
# $set[12] の設定ファイルを使う場合: http://www.---.com/cgi-bin/srch.cgi?no=12
$set[0]="./set.cgi";
$set[1]="./set1.cgi";
$set[2]="./set2.cgi";
$set[3]="./set3.cgi";
$set[4]="./set4.cgi";

# ---[設定ここまで]--------------------------------------------------------------------------------------------------
&d_code_;
if($no eq ""){$no=0;}
if($set[$no]){unless(-e $set[$no]){&er_('設定ファイルが無いです!');}else{$SetUpFile="$set[$no]"; require"$SetUpFile";}}
else{&er_('設定ファイルがCGIに設定されてません!');}
# ---[フォームスタイルシート設定等]----------------------------------------------------------------------------------
$ag=$ENV{'HTTP_USER_AGENT'};
if($fss && $ag =~ /IE|Netscape6/){
	$fm=" onmouseover=\"this.style.$on\" onmouseout=\"this.style.$off\"";
	$ff=" onFocus=\"this.style.$on\" onBlur=\"this.style.$off\"";
	$fsi="$fst";
}
if($logs){unless(($logs eq "$log" || $logs=~ /^[\d]+\.txt$/ || $logs eq "all")){&er_("そのファイルは閲覧できません!");}}
$nf="<input type=hidden name=no value=$no>\n";
$SL="$klog_d\/1.txt";
# ---[簡易パスワード制限関連]----------------------------------------------------------------------------------------
if($s_ret){$P=$FORM{"P"}; $pf="<input type=hidden name=P value=$P>\n"; $pp="&P=$P";}else{$pf=""; $pp="";}
if($s_ret && $P eq ""){&er_("<a href=\"$cgi_f?no=$no\">認証</a>してください!");}
if($P ne "R"){if($s_ret && $P ne "$s_pas"){&er_("パスワードが違います!");}}
if($s_ret==2 && $P eq "R"){&er_("パスワードが違います!");}
# ---[サブルーチンの読み込み/表示確定]-------------------------------------------------------------------------------
if($mode eq "log"){&log_;}
if($mode eq "del"){&del_;}
if($mode eq "dl"){&dl_;}
&srch_;
exit;
#--------------------------------------------------------------------------------------------------------------------
# [フォームコード]
# -> フォーム入力内容を解釈する(d_code_)
#
sub d_code_ {
if($ENV{'REQUEST_METHOD'} eq "POST"){read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});}else{$buffer=$ENV{'QUERY_STRING'};}
@pairs = split(/&/,$buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;

	&jcode'convert(*value,'sjis');
	$value =~ s/&/&amp\;/g;
	$value =~ s/</\&lt\;/g;
	$value =~ s/>/\&gt\;/g;
	$value =~ s/\"/\&quot\;/g;
	$value =~ s/<>/\&lt\;\&gt\;/g;
	$value =~ s/<!--(.|\n)*-->//g;

	$FORM{$name} = $value;
	if ($name eq 'del') { push(@d_,$value); }
}
$word= $FORM{'word'};
$andor=$FORM{'andor'};
$mode= $FORM{'mode'};
$logs =$FORM{'logs'};
$no   =$FORM{'no'};
}
#--------------------------------------------------------------------------------------------------------------------
# [ヘッダ表示]
# -> HTMLヘッダを出力する(hed_)
#
sub hed_ {
print "Content-type: text/html; charset=Shift_JIS\n\n";
print <<"_HTML_";
<html><head>
<META HTTP-EQUIV="Content-type" CONTENT=\"text/html; charset=Shift_JIS"></head>
$STYLE
$fsi
<!--$ver-->
<title>$title [$_[0]]</title>
_HTML_
print"<body text=$text link=$link vlink=$vlink bgcolor=$bg";
if($back ne ""){print" background=\"$back\">\n";}elsif($back eq ""){print">\n";}
print <<"_HTML_";
<!--ヘッダ広告タグ挿入位置▽-->

<!--△ここまで-->
<center>
_HTML_
if($t_img){print"<img src=\"$t_img\" width=$twid height=$thei>\n";}
else{print"<span style=\"font-size:$tsize;color:$tcolor;font-family:$tface;\">$title</span>\n";}
$BG=" bgcolor=$t_back";
if($mode eq "log"){$T1="$BG";}else{$T2="$BG";}
if($klog_s){$klog_link="<td$T1><a href=\"$srch?mode=log&no=$no$pp\">過去ログ</a></td>\n";}
if($M_Rank){$rank_link="<td><a href=\"$cgi_f?mode=ran&no=$no$pp\">発言ランク</a></td>\n";}
if($topok){$New_link="<td><a href=\"$cgi_f?mode=new&no=$no$pp\">新規作成</a></td>\n";}
if($TrON){$TrL="<td><a href=\"$cgi_f?H=T&no=$no$pp$Wf\">ツリー表\示</a></td>\n";}
if($TpON){$TpL="<td><a href=\"$cgi_f?H=F&no=$no$pp$Wf\">トピック表\示</a></td>\n";}
if($ThON){$ThL="<td><a href=\"$cgi_f?mode=alk&no=$no$pp$Wf\">スレッド表\示</a></td>\n";}
if($i_mode){$FiL="<td><a href=\"$cgi_f?mode=f_a&no=$no$pp\">ファイル一覧</a></td>\n";}
$HEDF= <<"_HTML_";
<p><table border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$ttb><tr align=center bgcolor="$k_back">
<td><a href="$backurl">HOME</a></td>
<td><a href="$cgi_f?mode=man&no=$no$pp">HELP</a></td>
$New_link<td><a href="$cgi_f?mode=n_w&no=$no$pp">新着記事</a></td>
$TrL$ThL$TpL$rank_link$FiL<td$T2><a href="$srch?no=$no$pp">検索</a></td>
$klog_link
</td></tr></table></p>
_HTML_
print"$HEDF</center>";
}
#--------------------------------------------------------------------------------------------------------------------
# [フッタ表示]
# -> HTMLフッタを出力する(foot_)
#
sub foot_ {
print <<"_HTML_";
<center>$HEDF
<!--著作権表\示 削除不可-->
- <a href="http://www.cj-c.com/" target=$TGT>Child Tree</a> -<br>
<!--フッタ広告タグ挿入位置▽-->

<!--△ここまで-->
</center>
</body></html>
_HTML_
exit;
}
#--------------------------------------------------------------------------------------------------------------------
# [検索機能&表示]
# -> 検索フォームの表示と、検索結果の表示をおこなう(srch_)
#
sub srch_ {
if($FORM{"PAGE"}){$klog_h=$FORM{"PAGE"};}else{$klog_h=$klog_h[0];}
if($logs && $logs=~ /txt$/){
	$logn=$logs; $C="";
	$logn=~ s/\.//g; $logn=~ s/txt//; $logn=~ s/\///g;
	$nowlog="<hr width=90\%><h3>過去ログ$logn を検索</h3>";
}elsif($logs && $logs eq "$log"){$nowlog="<hr width=90\%><h3>現在のログを検索</h3>";
}elsif($logs && $logs eq "all"){$nowlog="<hr width=90\%><h3>全過去ログを検索</h3>";}
if($FORM{"ALL"}){$nowlog="<hr width=90\%><h3>No.$word の関連記事表\示</h3>"; $KNS=" checked";}
&hed_("Search:$word");
if($klog_s){$klog_msg="(*過去ログは表\示されません)<br>・過去ログから探す場合は検索範囲から過去ログを選択。";}
if($andor eq "or"){$OC=" selected";}else{$OC="";}
print <<"_STOP_";
<center><table width=90\%><tr><th bgcolor=$ttb>ログ内検索</th></tr></table>
<table><tr><td>
・キーワードを複数指定する場合は 半角スペース で区切ってください。<br>
・検索条件は、(AND)=[A かつ B] (OR)=[A または B] となっています。<br>
・[返信]をクリックすると返信ページへ移動します。
$klog_msg
</td></tr></table>
<hr width=90%>
<form action="$srch" method=$Met>$nf$pf<table><tr>
<td bgcolor=$ttb>キーワード</td><td>/ <input type=text name=word size=20 value="$word"$ff></td>
<td bgcolor=$ttb>検索条件</td>
<td>/ <select name=andor><option value=and>(AND)<option value=or$OC>(OR)</select></td></tr>
<tr><td bgcolor=$ttb>検索範囲</td><td>/ <select name=logs><option value="$log">(現在のログ)
_STOP_
if($klog_s && -e $SL){
	if($klog_a){
		$C=""; if($logs eq "all"){$C=" selected";}
		print"<option value=all$C>(全過去ログ)";
	}
	open(NO,"$klog_c");
	$n = <NO>;
	close(NO);
	$br=0;
	for ($i=0;$i<$n;$i++) {
		$l=$i+1; $C="";
		if($l==$logn){$C=" selected";}
		print "<option value=\"$l\.txt\"$C>(過去ログ$l)\n"; 
		$br++;
	}
}
if($FORM{"KYO"}){$CB=" checked";}
if($FORM{"bigmin"}){$CB2=" checked"; $BM=0;}else{$BM=1;}
print <<"_SS_";
</select></td>
<td bgcolor=$ttb>強調表\示</td><td>/ <input type=checkbox name=KYO value=1$CB$fm>ON
<small>(自動リンクOFF)</small></td></tr>
<tr><td bgcolor=$ttb>結果表\示件数</td><td>/ <select name=PAGE>
_SS_
foreach $KH (@klog_h){$S=""; if($klog_h==$KH){$S=" selected";} print"<option value=$KH$S>$KH件\n";}
print <<"_SS_";
</select></td>
<td bgcolor=$ttb>記事No検索</td><td>/ <input type=checkbox name=ALL value=1$KNS$fm>ON</td></tr>
<tr><td colspan=2><input type=checkbox name=bigmin value=1$CB2$fm>大文字と小文字を区別する</td>
<td colspan=2 align=right>
<input type=submit value=" 検 索 "$fm>
<input type=reset value="リセット"$fm>
</td></tr></table></form>$nowlog</center>
_SS_
if($word ne "") {
	$word =~ s/　/ /g;
	$word =~ s/\t/ /g;
	@key_ws= split(/ /,$word);
	if($logs eq "all"){
		$Stert=0; if($FORM{'N'}){($N,$S)=split(/\,/,$FORM{'N'}); $Stert=$N;} $End=$n-1;
		if($klog_a==0){&er_("全過去ログ検索は使用不可");}}
	else{$Stert=0; $End=0;}
	@new=(); $Next=0;
	foreach ($Stert..$End) {
		if($logs eq "all"){$I=$_+1; $IT="$I\.txt"; $Log="$klog_d\/$IT";}
		elsif($logs eq $log){$Log=$log;}
		else{$Log="$klog_d\/$logn\.txt";}
		open(DB,$Log) || &er_("Can't open $Log");
		while ($Line=<DB>) {
			$hit = 0;
			if($FORM{"ALL"}){
				($nam,$date,$name,$email,$d_may,$comment,
					$url,$font,$ico,$type,$del,$ip) = split(/<>/,$Line);
				if($word==$nam || $word==$type){$hit=1;}
			}else{
				foreach $key_w (@key_ws){
					if($key_w =~ /[\x80-\xff]/){$jflag = 1;}else{$jflag = 0;}
					$key_w=~ s/^&$/&amp\;/g;
					$key_w=~ s/^<$/\&lt\;/g;
					$key_w=~ s/^>$/\&gt\;/g;
					$key_w=~ s/^\"$/\&quot\;/g;
					if ($jflag) {
						if(index($Line, $key_w) >= 0){$hit=1;}else{$hit=0;}
					} else {
						if($BM){if($Line =~ /$key_w/i){$hit=1;}else{$hit=0;}}
						else{if($Line =~ /$key_w/){$hit=1;}else{$hit=0;}}
					}
					if($hit){if($andor eq "or"){last;}}else{if($andor eq "and"){$hit=0; last;}}
				}
			}
			if($hit){push(@new,"$IT<>$Line");}
			if($#new+1 >= 200 && $logs eq "all"){$Next=$I+1;}
		}
		close(DB);
		if($Next){last;}
	}
}
$count=@new;
if($logs eq "$log"){@new=reverse(@new);}
if($count > 0){
	$word=~ s/([^0-9A-Za-z_])/"%".unpack("H2",$1)/ge;
	$word=~ tr/ /+/;
	$total=@new;
	$page_=int(($total-1)/$klog_h);
	if($FORM{'page'} eq ""){$page=0;}else{$page=$FORM{'page'};}

	$end_data=@new-1;
	$page_end=$page+($klog_h-1);
	if($page_end >= $end_data){$page_end=$end_data;}
	$Pg=$page+1; $Pg2=$page_end+1;
	print"<ul><b>ヒット / $count件</b> ($Pg-$Pg2 を表\示)";
	if($Next || $N){
		$NLog="<br>ヒット件数が多いので";
		if($N){$N++; $NLog.="過去ログ$N";}else{$NLog.="過去ログ1";}
		$NLog.="～$I までの検索結果 / <b>";
		$NLog.="<a href=\"$srch?mode=srch&logs=$logs&no=$no$pp&word=$word&andor=$andor&KYO=$FORM{'KYO'}&PAGE=$klog_h&N=$I,$Stert\">";
		$NLog.="過去ログ$Nextからさらに検索→</a></b>\n";
	}
	print"$NLog</ul><center>\n";
	$nl=$page_end + 1;
	$bl=$page - $klog_h;
	if($bl >= 0){
		$Bl ="<a href=\"$srch?mode=srch&logs=$logs&page=$bl&no=$no$pp&word=$word&andor=$andor&KYO=$FORM{'KYO'}&PAGE=$klog_h\">";
		$Ble="</a>";
	}
	if($page_end ne $end_data){
		$Nl ="<a href=\"$srch?mode=srch&logs=$logs&page=$nl&no=$no$pp&word=$word&andor=$andor&KYO=$FORM{'KYO'}&PAGE=$klog_h\">";
		$Nle="</a>";
	}
	$Plink="$Bl\&lt\;\&lt\;$Ble\n";
	$a=0;
	for($i=0;$i<=$page_;$i++){
		$af=$page/$klog_h;
		if($i != 0){$Plink.="| ";}
		if($i eq $af){$Plink.="<b>$i</b>\n";}
		else{
			$Plink.="<a href=\"$srch?mode=srch&logs=$logs&page=$a&no=$no$pp";
			$Plink.="&word=$word&andor=$andor&KYO=$FORM{'KYO'}&PAGE=$klog_h\">$i</a>\n";
		}
		$a+=$klog_h;
	}
	$Plink.="$Nl\&gt\;\&gt\;$Nle\n";
	print <<"_KT_";
$Plink
<form action="$srch" method=$Met><input type=hidden name=mode value="del">
<input type=hidden name=logs value="$logs">$nf$pf
_KT_
	foreach ($page .. $page_end) {
		($IT,$nam,$date,$name,$email,$d_may,$comment,$url,
			$sp,$e,$type,$del,$ip,$tim,$Se) = split(/<>/,$new[$_]);
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		if($date eq ""){next;}
		$Pr="";
		if($ico){
			if($Ent==0 && $fimg){$fimg=$no_ent;}
			if(-s "$i_dir/$ico"){$Size= -s "$i_dir/$ico";}else{$Size=0;}
			$KB=int($Size/1024); if($KB==0){$KB=1;}
			if($Size){
				if($Size && $fimg ne $no_ent){$Alt=" alt=\"$ico/$KB\KB\"";}else{$Alt="";}
				if($fimg eq $no_ent){$A=0;}
				elsif($fimg eq "img"){
					$Pr.="<a href=\"$i_Url/$ico\" target=_blank><img src='$i_Url/$i_ico' border=0$Alt>";
					$A=1;
				}else{$Pr.="<a href=\"$i_Url/$ico\" target=_blank>";$A=1;}
				if($img_h eq "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" border=0$Alt>";}
				elsif($img_h ne "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" height=$img_h width=$img_w border=0$Alt>";}
				$AEND="";
				if($A){$AEND="$ico</a>/";}
				$Pr="<center>$Pr"."<br>$AEND<small>$KB\KB</small></center>\n";
			}
		}
		if($font eq ""){$font=$text;}
		if($hr eq ""){$hr=$ttb;}
		if($type > 0){$t_com="記事No.$type のレス\n"; $KK="$type";}else{$t_com="親記事\n"; $KK="$nam";}
		if($d_may eq ""){$d_may="No Title";}
		if($email && $Se < 2){$name ="$name <a href=mailto:$email>$AMark</a>";}
		if($url){
			if($URLIM){
				if($UI_Wi){$UIWH=" width=$UI_Wi height=$UI_He>";}
				$i_or_t="<img src=\"$URLIM\"$UIWH>";
			}else{$i_or_t="http://$url";}
			$url="<a href=\"http://$url\" target=$TGT>$i_or_t</a>";
		}
		if($Icon && $comment=~/<br>\(携帯\)$/){$ICO="$Ico_k";}
		if($ICO ne ""){
			if($IconHei){$WH=" height=$IconHei width=$IconWid";}
			$ICO="<img src=\"$IconDir\/$ICO\"$WH>";
		}
		if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
		if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
		if($yobi){$yobi="<font color=$IDCol>[ID:$yobi]</font>";}
		if($Txt || $Sel ||($Txt && $Sel)){
			if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}
			elsif($TS_Pr==1){$comment="$Txt<br>$Sel<br><br>"."$comment";}
			elsif($TS_Pr==2){$comment.="<br><br>$Txt<br>$Sel";}
		}
		if($comment=~ /^<pre>/){$comment=~ s/<br>/\n/g;}
		$comment="<!--C-->$comment";
		if($IT ne "" && $logs eq "all"){
			$IT=~s/^\n//; $IT=~s/\.txt$//; $PLL="過去ログ$ITより /"; $IT="&KLOG=$IT";
		}else{$IT="";}
		if($FORM{"KYO"}){
			if($comment=~/<\/pre>/){$comment=~ s/(>|\n)((&gt;|＞|>)[^\n]*)/$1<font color=$res_f>$2<\/font>/g;}
			else{$comment=~ s/>((&gt;|＞|>)[^<]*)/><font color=$res_f>$1<\/font>/g;}
			&jcode'convert(*comment,'euc');
			foreach $KEY (@key_ws){
				&jcode'convert(*KEY,'euc');
				$comment=~ s/$KEY/<b STYLE="background-color:$Kyo_f\;">$KEY<\/b>/g;
				if($BM){$comment=~ s/($KEY)/<b STYLE="background-color:$Kyo_f\;">$1<\/b>/ig;}
				else{$comment=~ s/$KEY/<b STYLE="background-color:$Kyo_f\;">$KEY<\/b>/g;}
			}
			&jcode'convert(*comment,'sjis');
		}else{&auto_($comment);}
		if($e){$e=" END /";}
		if($logs eq $log){
			if($TOPH==0){$MD="mode=res&namber="; if($type){$MD.="$type";}else{$MD.="$nam";}}
			elsif($TOPH==1){$MD="mode=one&namber=$nam&type=$type&space=$sp";}
			elsif($TOPH==2){$MD="mode=al2&namber="; if($type){$MD.="$type";}else{$MD.="$nam";}}
			$L=" <a href=\"$cgi_f?$MD&no=$no$pp\">返信ページ</a> /";
		}
		print <<"_HITCOM_";
<table width=90\% bgcolor=$k_back border=1 bordercolor="$hr"><tr><td>
<table width=100% border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$hr>
<tr><td width=1\% nowrap><font color="$kijino"><b>■$nam</b></font></td><td bgcolor="$hr">
<font color=$t_font>　<b>$d_may</b></font></td></tr></table>
□投稿者/ $name -<small>($date) $yobi<br>$url</small>
<ul><table><tr><td align=center>$ICO</td><td><font color="$font">$comment</fonr></td></table></ul>
$Pr<div align=right>$t_com /$e$L$PLL
<a href="$cgi_f?mode=al2&namber=$KK&no=$no$pp$IT" target="_blank">関連記事表\示</a><br>
削除チェック/<input type=checkbox name=del value=$nam$fm></div></td></tr></table><br>
_HITCOM_
	}
	print "<b>\n";
	if($Bl){print"$Bl＜前の$klog_h件$Ble\n";}
	if($Nl){if($Bl){print"| ";} print"$Nl次の$klog_h件＞$Nle\n";}
	print <<"_KF_";
</b><br><br>$Plink<br>
$NLog</center>
<hr width=90\%>
<div align=right>パスワード/<input type=password name=pas size=4$ff>
<input type=submit value="管理者削除用"$fm></form></div>
_KF_
}elsif($count == 0 && $word){print"<center>該当する記事はありませんでした。</center>";}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [過去ログリンク表示]
# -> 過去ログを表示するリンク表示(log_)
#

sub log_ {
&hed_("Past Log");
if($logs){
	$logn=$logs;
	$logn=~ s/\.//; $logn=~ s/txt//; $logn=~ s/\///;
	$nowlog="<h3>過去ログ$logn を表\示</h3>";
}
if($FORM{"KLOG_H"}){$klog_h[0]=$FORM{"KLOG_H"};}
print <<"_LTOP_";
<center><table width="85\%"><tr><th bgcolor=$ttb>過去ログ表\示</th></tr>
<tr><td><ul>
<li>過去ログの検索は <a href="$srch?no=$no$pp">検索</a> より行えます。
<li>過去ログの表\示はトピック表\示となります。
</ul></td></tr>
</table><table><tr><th>表\示ログ</th><td>
_LTOP_
if(-e $SL){
	open(NO,"$klog_c");
	$n = <NO>;
	close(NO);
	$br=0;
	for ($i=1;$i<=$n;$i++) {
		print"<a href=\"$cgi_f?KLOG=$i&no=$no$pp\" target=\"_blank\">過去ログ$i</a>\n";
		$br++; if($br==5){print"<br>";$br=0;}
	}
}else{print"現在表\示できる過去ログはありません。\n";}
print"</td></tr></table><hr width=\"85\%\">";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [過去ログ削除]
# -> 過去ログ内のいらない記事を削除(del_)
#
sub del_ {
if($FORM{'pas'} ne "$pass"){ &er_("パスワードが違います!"); }
if($logs eq $log){&er_("現在ログは<a href='$cgi_f?no=$no$pp'>$cgi_f</a>管理モードより削除下さい。");}
$logs="$klog_d/$logs";
open(DB,"$logs") || &er_("Can't open $logs");
@mens = <DB>;
close(DB);
@CAS = ();
foreach $mens (@mens) {
	$castam=0;
	$mens =~ s/\n//g;
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$e,$type,$del,$ip) = split(/<>/,$mens);
	foreach $word (@d_) {if($word eq "$nam"){$mens=""; $castam=1;}}
	if($mens eq ""){ $n=""; }else{ $n="\n"; }
	push (@CAS,"$mens$n");
}
open (DB,">$logs");
print DB @CAS;
close(DB);
&log_;
}
#--------------------------------------------------------------------------------------------------------------------
# [URLをリンク等]
# -> コメント内、リンク・文字色など処理(auto_)
#
sub auto_ {
if($_[0]=~/<\/pre>/){$_[0]=~ s/(>|\n)((&gt;|＞|>)[^\n]*)/$1<font color=$res_f>$2<\/font>/g;}
else{$_[0]=~ s/>((&gt;|＞|>)[^<]*)/><font color=$res_f>$1<\/font>/g;}
$_[0]=~ s/([^=^\"]|^)((http|ftp|https)\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+)/$1<a href=$2 target=$TGT>$2<\/a>/g;
$_[0]=~ s/([^\w^\.^\~^\-^\/^\?^\&^\+^\=^\:^\%^\;^\#^\,^\|]+)(No|NO|no|No.|NO.|no.|&gt;&gt;|＞＞|>>)([0-9\,\-]+)/$1<a href=\"$srch?mode=srch&ALL=1&word=$3&logs=all&no=$no$pp\" target=$TGT>$2$3<\/a>/g;
}
#--------------------------------------------------------------------------------------------------------------------
# [エラー表示]
# -> エラーの内容を表示する(er_)
#
sub er_ {
&hed_("Error");
print "<center>ERROR - $_[0]</center><br>\n";
&foot_;
}
