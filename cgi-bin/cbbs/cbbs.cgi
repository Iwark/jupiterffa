#!/usr/local/bin/perl

require './jcode.pl';

#------------------------------------------
$ver = "Child Tree v8.94";# (ツリー式掲示板)
#------------------------------------------
# Copyright(C) りゅういち
# E-Mail:ryu@cj-c.com
# W W W :http://www.cj-c.com/
#------------------------------------------

#---[設定ファイル]-------------------------

# 同じようにいくつでも増やせます。
# [ ]内の数字を使いCGIにアクセスするとその設定ファイルで動作します。
# $set[12] の設定ファイルを使う場合: http://www.---.com/cgi-bin/cbbs.cgi?no=12
$set[0]="./set.cgi";
$set[1]="./set1.cgi";
$set[2]="./set2.cgi";
$set[3]="./set3.cgi";
$set[4]="./set4.cgi";

# 禁止文字列 タグ使用の場合は禁止タグも入力OK 同じようにいくつでも指定可能
@NW=('死ね');

# 排除IP/禁止文字列設定ファイル
$IpFile="IpAcDeny.cgi";
$NWFile="WordDeny.cgi";

# ---[設定ここまで]--------------------------------------------------------------------------------------------------
#
# ファイルアップ機能はとほほさんのWWWUPLを参考にしています。
# -> http://tohoho.wakusei.ne.jp/
#
# ---[排除IP/禁止文字列読み込み]-------------------------------------------------------------------------------------
if(-e $NWFile){
	open(DE,"$NWFile");
	while(<DE>){push(@NW,$_);}
	close(DE);
}
if(-e $IpFile){
	open(DE,"$IpFile");
	while(<DE>){push(@ips,$_);}
	close(DE);
}
if(@ips){
	$match=0;
	foreach (@ips) {$_=~ s/\n//; if($ENV{'REMOTE_ADDR'}=~ /$_/){$match=1; last;}}
	if($match){&er_("あなたには閲覧権限がありません!");}
}
# ---[設定ファイル読み込み]------------------------------------------------------------------------------------------
$res_r=1;
&d_code_;
if($no eq ""){$no=0;}
if($set[$no]){unless(-e $set[$no]){&er_('設定ファイルが無いです!');}else{$SetUpFile="$set[$no]"; require"$SetUpFile";}}
else{&er_('設定ファイルがCGIに設定されてません!');}
$nf="<input type=hidden name=no value=$no>\n";
# ---[フォームスタイルシート設定]------------------------------------------------------------------------------------
$ag=$ENV{'HTTP_USER_AGENT'};
if($fss && $ag =~ /IE|Netscape6/){
	$fm=" onmouseover=\"this.style.$on\" onmouseout=\"this.style.$off\"";
	$ff=" onFocus=\"this.style.$on\" onBlur=\"this.style.$off\"";
	$fsi="$fst";
}
# ---[簡易パスワード制限関連]----------------------------------------------------------------------------------------
if($s_ret){if($FORM{"P"} eq ""){
	&get_("P");} $P=$FORM{"P"};
	$pf="<input type=hidden name=P value=$P>\n";
	$pp="&P=$P";
}else{$pf=""; $pp="";}
if($FORM{'KLOG'}){
	$KLOG=$FORM{'KLOG'}; $TrON=0; $TpON=1; $ThON=0; $TOPH=2;
	unless($KLOG=~ /^[\d]+/){&er_("そのファイルは閲覧できません!");}
	$log="$klog_d\/$KLOG\.txt";
	$pp.="&KLOG=$KLOG";
	$pf.="<input type=hidden name=KLOG value=$KLOG>\n";
}
if($s_ret && $P eq "" && ($mode eq "alk"||$mode eq "")){&pas_;}
if($s_ret==2 && $P eq "R"){&er_("パスワードが違います!");}
if($s_ret && $P ne "R"){if($P ne "$s_pas"){&er_("パスワードが違います!");}else{&set_("P");}}
# ---[サブルーチンの読み込み/表示確定]-------------------------------------------------------------------------------
if($mode eq "all_v"){&a_;} if($mode eq "ffs"){&freeform_;}
if($mode eq "bma"){&bma_;} if($mode eq "Den"){&Den_;}
if($mode eq "ent"){&ent_;} if($mode eq "man"){&man_;}
if($mode eq "n_w"){&n_w_;} if($mode eq "wri"){&wri_;}
if($mode eq "del"){&del_;} if($mode eq "s_d"){&s_d_;}
if($mode eq "nam"){&hen_;} if($mode eq "h_w"){&h_w_;}
if($mode eq "new"){&new_;} if($mode eq "all"){&all_;}
if($mode eq "al2"){&all2;} if($mode eq "res"){&res_;}
if($mode eq "key"){&key_;} if($mode eq "one"){&one_;}
if($mode eq "ran"){&ran_;} if($mode eq "f_a"){&f_a_;}
if($mode eq "img"){&img_;} if($mode eq "red"){&read;}
if($mode eq "cmin"){&set_("M");} if($mode eq "cookdel"){&cookdel;}
unless(-e $log){if($KLOG eq ""){&l_m($log);}}
unless(-e $c_f){if($cou){&l_m($c_f);}}
unless(-e $RLOG){if($M_Rank){&l_m($RLOG);}}
if($W){$Wf="&W=$W";} if($H){$Hf="&H=$H";}
if($W eq "W"){$Res_T=0;}elsif($W eq "T"){$Res_T=1;}elsif($W eq "R"){$Res_T=2;}
if($mode eq "alk"){&alk_;}
if($H eq "F"){&html2_;}elsif($H eq "T"){&html_;}elsif($H eq "N"){&alk_;}
if($TOPH==1){&html_;}elsif($TOPH==2){&html2_;}else{&alk_;}
exit;
#--------------------------------------------------------------------------------------------------------------------
# [記事デザイン] 
# -> 記事を統一デザインで表示(design)
#
sub design {
local($namber,$date,$name,$email,$d_may,$comment,$url,$space,$end,$type,$delkey,$ip,$tim,$ico,
	$Ent,$fimg,$mini,$icon,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,$htype,$hanyo)=@_; @_=();
$HTML="";
if($font eq ""){$font=$text;}
if($hr eq ""){$hr=$ttb;}
if($d_may eq ""){$d_may="NO TITLE";}
if($Icon && $comment=~/<br>\(携帯\)$/){$icon="$Ico_k";}
if($icon ne ""){
	if($IconHei){$WH=" height=$IconHei width=$IconWid";}
	$icon="<img src=\"$IconDir\/$icon\"$WH>";
}
if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
if($yobi){$yobi="<font color=$IDCol>[ID:$yobi]</font>";}
if($end){$end="$end_ok";}
if($email && $Se < 2){$email="<a href=\"mailto:$SPAM$email\">$AMark</a>";}else{$email="";}
if($url){
	if($URLIM){
		if($UI_Wi){$UIWH=" width=\"$UI_Wi\" height=\"$UI_He\"";}
		$i_or_t="<img src=\"$URLIM\" border=0$UIWH>";
	}else{$i_or_t="http://$url";}
	$url="<a href=\"http://$url\" target=$TGT>$i_or_t</a>";
}
if($comment=~ /<\/pre>$/){$comment=~ s/<br>/\n/g;}
if($Txt || $Sel ||($Txt && $Sel)){
	if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}
	elsif($TS_Pr==1){$comment="$Txt<br>$Sel<br><br>"."$comment";}
	elsif($TS_Pr==2){$comment.="<br><br>$Txt<br>$Sel";}
}
if($FORM{"pass"} && $FORM{"pass"} eq $pass){$Ent=1; $url="";}
if($mas_c==2 && $Ent==0){$comment="コメント表\示:未許可";}
$comment="<!--C-->$comment"; &auto_($comment);
if($o_mail){$Smsg="[メール受信/";if($Se==2 || $Se==1){$Smsg.="ON]\n";}else{$Smsg.="OFF]\n";}}
if($ico && $i_mode){$Pr=""; &size(); $Pr="<tr><td align=center>$Pr</td></tr>\n"; $SIZE+=$Size;}else{$Pr="";}
$agsg=""; $UeSt=""; $Pre="";
if($ResNo==0){$ResNo="親";}
if($htype eq "T"){
	$ResNo="$ResNo階層"; $Border=1; $Twidth=90;
	if($Res_i){$IN="<b><a href=\"$cgi_f?mo=1&mode=one&namber=$namber&type=$type&space=$space&no=$no$pp#F\">記事引用</a></b>";}
}elsif($htype eq "T2"){
	$ResNo="$ResNo階層"; $Border=1; $Twidth=90;
	$IN="<b><a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">返信</a></b>";
	if($Res_i){$IN.="/<b><a href=\"$cgi_f?mo=1&mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">引用返信</a></b>\n";}
	$VNo=$namber; $OTL="";
	if($type > 0){$UeSt.="$b_ "; $OTL=" <a href=#$ty>親 $type </a> /";}else{$UeSt.="親記事　/ ";}
	if($n_){$UeSt.="$n_ </a>\n";}else{$UeSt.="返信無し\n";}
	$OTL.=" <a href=#>□ Tree</a>\n";
	$IN="[$OTL]\n".$IN;
	$HTML.="<br>";
}elsif($htype eq "F"){
	$VNo++;	$ResNo="inTopicNo.$ResNo"; $Border=0; $Twidth=90;
	$IN="<a href=\"$cgi_f?mode=al2&mo=$nam&namber=$FORM{'namber'}&space=$sp&rev=$rev&page=$fp&no=$no$pp#F\"><b>引用返信</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=al2&mo=$nam&namber=$FORM{'namber'}&space=$space&rev=$rev&page=$fp&In=1&no=$no$pp#F\"><b>返信</b></a>";}
	if($VNo==1){$sg=$VNo+1; $agsg="\&nbsp\;\&nbsp\;<a href=\"#$sg\">▼</a><a href=\"#1\">■</a>";}
	elsif($VNo >= $topic){$ag=$VNo-1; $agsg="<a href=\"#$ag\">▲</a>　<a href=\"#1\">■</a>";}
	else{$ag=$VNo-1; $sg=$VNo+1; $agsg="<a href=\"#$ag\">▲<a href=\"#$sg\">▼<a href=\"#1\">■</a>";}
}elsif($htype eq "N"){
	$ResNo=""; $Border=1; $Twidth=90;
	if($TOPH==0){$MD="mode=res&namber="; if($type){$MD.="$type";}else{$MD.="$namber";}}
	elsif($TOPH==1){$MD="mode=one&namber=$namber&type=$type&space=$space";}
	elsif($TOPH==2){$MD="mode=al2&namber="; if($type){$MD.="$type";}else{$MD.="$namber";} $MD.="&space=$space";}
	$IN="<b><a href=\"$cgi_f?$MD&no=$no$pp#F\">返信</a></b>";
	if($Res_i){$IN.="/<b><a href=\"$cgi_f?$MD&mo=$namber&no=$no$pp#F\">引用返信</a></b>\n";}
	$HTML.="<br>";
}elsif($htype eq "P"){
	$ResNo=""; $Border=1; $Twidth=90;
	if($hanyo eq "randam"){$icon="アイコン<br>ランダム";}
	$Smsg.="<!--"; $Pre="--";
}elsif($htype eq "TR"){
	if($ResNo eq "親"){$ResNo="親記事"; $Twidth=100;}else{$ResNo="ResNo.$ResNo"; $Twidth=90;}
	$Border=0; $Smsg.="<!--"; $Pre="--";
	$IN="<a href=\"$cgi_f?mode=res&namber=$nam&type=$type&space=$space&mo=$namber&page=$PNO&no=$no$pp#F\"><b>引用返信</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=res&namber=$nam&type=$type&space=$space&mo=$namber&page=$PNO&In=1&no=$no$pp#F\"><b>返信</b></a>";}
}elsif($htype eq "TRES"){
	$Border=0; $Twidth=90; $VNo++;
	if($ResNo eq "親"){$ResNo="親記事";}else{$ResNo="ResNo.$ResNo";}
	if($VNo==1){$sg=$VNo+1; $agsg="\&nbsp\;\&nbsp\;<a href=\"#$sg\">▼</a><a href=\"#1\">■</a>";}
	elsif($VNo >= $topic){$ag=$VNo-1; $agsg="<a href=\"#$ag\">▲</a>　<a href=\"#1\">■</a>";}
	else{$ag=$VNo-1; $sg=$VNo+1; $agsg="<a href=\"#$ag\">▲<a href=\"#$sg\">▼<a href=\"#1\">■</a>";}
	$IN="<a href=\"$cgi_f?mode=res&mo=$nam&namber=$FORM{'namber'}&space=$sp&page=$page&no=$no$pp#F\"><b>引用返信</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=res&mo=$nam&namber=$FORM{'namber'}&space=$sp&page=$page&In=1&no=$no$pp#F\"><b>返信</b></a>"}
}
$HTML.=<<"_HTML_";
<a name="$VNo"></a>
<table width=$Twidth\% bgcolor=$k_back border=$Border bordercolor=$hr cellspacing=0><tr><td>$UeSt
<table border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$hr>
<tr><td width=1\% nowrap><b><font color="$kijino">■$namber</font></b> / $ResNo)</td>
<td bgcolor=$hr>　<b><font color=$t_font>$d_may</font></b>
</td></tr></table><div align=right>$agsg</div>
□投稿者/ $name $email <small>$R-($date) $yobi<br>$url</small>
<ul><table><tr><td align=center>$icon</td><td><font color="$font">$comment<br></td></tr></table></ul>
<div align=right>$end</div></td></tr>
$Pr<tr><form action="$cgi_f" method=$met>
<td align=right>$IN
$Smsg
<input type=hidden name=del value=$namber>$nf$pf
削除キー/<input type=password name=delkey size=8$ff>
<select name=mode>
<option value=nam>編集
<option value=key>削除
</select>
<input type=submit value="送 信"$fm$Pre></td></form></tr></table>
_HTML_
}
#--------------------------------------------------------------------------------------------------------------------
# [パスワード認証]
# -> 入室時のパスワード認証(pas_)
#
sub pas_ {
&hed_("Pass Input");
print <<_PAS_;
<center><table width=90\%>
<tr bgcolor=$ttb><th>パスワード認証</th></tr>
<tr><th>*書きこむにはパスワードが必要です!<form action=$cgi_f method=$met>
<input type=password size=8 name=P$ff>$nf
<input type=submit value=" 認証 "$fm>
</form></th></tr></table>
_PAS_
if($s_ret==1){
	print"記事の閲覧はできます(リードオンリー)\n";
	print" <a href=\"$cgi_f?P=R&no=$no\"><b>記事を閲覧する</b></a>\n";
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [トピック一覧表示]
# -> トピックを一覧表示(html2_)
#
sub html2_ {
@NEW=(); @RES=(); %R=(); %RES=(); $RS=0;
if($FORM{'page'}){$page=$FORM{'page'};}else{$page=0;}
open(LOG,"$log") || &er_("Can't open $log");
while (<LOG>) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
	if($type){
		if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim); $RS++;
		if($R{$type}){$R{$type}++;}else{$R{$type}=1;}
		if(($OyaCount > $page+($tab_m*$tpmax) || $page > $OyaCount+1) && $Res_T==0 && $tim=~/[\d]+/){next;}
		if($date){$RES{$type}.="$tim<>$_";}
	}else{
		if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
		if($Res_T==2){$tim=$R{$namber}; $tim=sprintf("%05d",$tim);}
		push(@NEW,"$tim<>$_"); $OyaCount=@NEW;
	}
	$TIM=$tim;
}
close(LOG);
if($Res_T){@NEW=sort(@NEW); @NEW=reverse(@NEW);}
$total=@NEW; $NS=$total+$RS; @lines=();
$PAGE=$page/($tpmax*2);
&hed_("All Topic / Page: $PAGE");
$Pg=$page+1; $Pg2=$page+$tpmax*$tab_m;
if($Pg2 >= $total){$Pg2=$total;}
print <<"_HTML_";
<center><table cellspacing=0 cellpadding=0><tr><td>
$com_top
</td></tr><tr><td>
■ $new_t時間以内に作成されたトピックは $new_i で表\示されます。<br>
■ $new_t時間以内に更新されたトピックは $up_i_ で表\示されます。<br>
■ トピックタイトルをクリックするとそのトピックの内容と返信を表\示します。
</td></tr></table>$Henko<hr width="95\%">
_HTML_
if($i_mode){&minf_("F");}

$end_data=@NEW-1;
$page_end=$page+($tpmax*$tab_m-1);
if($page_end >= $end_data){$page_end=$end_data;}
$page_=int(($total-1)/($tpmax*$tab_m));
$view =$tpmax*$tab_m;
$nl = $page_end + 1;
$bl = $page - $view;
if($bl >= 0){$Bl="<a href=\"$cgi_f?H=F&page=$bl&no=$no$pp$Wf\">"; $Ble="</a>";}else{$Bl=""; $Ble="";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?H=F&page=$nl&no=$no$pp$Wf\">"; $Nle="</a>";}else{$Nl=""; $Nle="";}

print"</center><ul>[ 全$totalトピック($Pg-$Pg2 表\示) ]　\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/($tpmax*$tab_m);
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?page=$a&H=F&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$tpmax*$tab_m;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=F&W=W&no=$no$pp\">更新順</a>"; $OJ2="投稿順"; $OJ3="<a href=\"$cgi_f?H=F&W=R&no=$no$pp\">レス数</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=F&W=W&no=$no$pp\">更新順</a>"; $OJ2="<a href=\"$cgi_f?H=F&W=T&no=$no$pp\">投稿順</a>"; $OJ3="レス数";}
else{$OJ1="更新順"; $OJ2="<a href=\"$cgi_f?H=F&W=T&no=$no$pp\">投稿順</a>"; $OJ3="<a href=\"$cgi_f?H=F&W=R&no=$no$pp\">レス数</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ] ←ソ\ート方法変更 </ul><center>";
$k=0; $q=0;
if($k){$p=$tab_m-$i; $page+=$tpmax*$p; last;}
if($topok){$TP="<th>トピック作成者</th>";}
if($he_tp==0){$SK="<th>最終発言者</th>";}
if($end_f){$EE="<th>END</th>";}
$TableChange=0;
foreach ($page .. $page_end) {
	($T,$namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	if($TableChange==0){
		print"<br><table width=95\% border=1 cellspacing=0 bordercolor=\"$ttb\"><tr bgcolor=$t_back>\n";
		if($SEL_F){print"<th>$SEL_T</th>";}
		if($TXT_F){print"<th>$TXT_T</th>";}
		print"<th>トピックタイトル</th><th>記事数</th>$TP$SK<th>最終更新</th>$EE</tr>\n";
	}
	$TableChange++;
	if($i_mode){
		$File=0; $Size=0;
		if($ico){$File++; $Size+=-s "$i_dir/$ico";}
	}
	if(($time_k-$tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
	if($yobi){$yobi="<br><small><font color=\"$IDCol\">[ID:$yobi]</font></small>";}
	if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
	if($d_may eq ""){$d_may="No Title";}
	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2)); $d_may="$d_may..";}
	$reok="<br>"; $date=substr($date,5,16);
	$ksu=1; $BeTime=0;
	@RES= split(/\n/,$RES{$namber}); @RES=sort(@RES);
	foreach $lines(@RES) {
		($T,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
			$rsp,$re,$rtype,$del,$ip,$rtim,$rSe) = split(/<>/,$lines);
		if($namber eq "$rtype"){
			($Ip,$ico,$Ent,$fimg,$rTXT,$rSEL,$R)=split(/:/,$ip);
			($rtxt,$rsel,$rid)=split(/\|\|/,$rSEL);
			if($SEL_R==0){$sel="$rsel";} if($TXT_R==0){$txt=$rtxt;}
			if($rid){$rid="<br><small><font color=\"$IDCol\">[ID:$rid]</font></small>";}
			if($i_mode){if($ico){$File++; $Size+=-s "$i_dir/$ico";}}
			$ksu++;
			if($BeTime < $rtim || $tim !~/[\d]+/){
				if($rmail && $rSe < 2){$rn="$rname <a href=\"mailto:$SPAM$rmail\">$AMark</a>";}
				else{$rn="$rname";}
				$rdd=substr($rd,5,16);
				if($re){$reok="$end_ok";}else{$reok="<br>";}
				if(($time_k-$rtim)>$new_t*3600){$news="$hed_i";}else{$news="$up_i_";}
				$BeTime=$rtim;
			}
			if($R{$namber}==($ksu-1)){last;}
		}
	}
	if($rdd eq ""){$rdd="$date";}
	if($rn eq "") {$rn="$name$yobi";}
	if($topok){$TP2="<td>$name$yobi</td>";}
	if($he_tp==0){$SK2="<td>$rn$rid</td>";}
	if($Size){$KB=int($Size/1024); if($KB==0){$KB=1;}}
	$FL="<br><small>└<font color=$kijino>#$namber</font>　[作成:$date]";
	if($File && $Size){$FL.="　[File:$File -$KB\KB]";}
	if($topic < $ksu){
		$a=0; $PG_=int(($ksu-1)/$topic); $RP="";
		for($j=0;$j<=$PG_;$j++){
			$RP.="<a href=\"$cgi_f?mode=al2&namber=$namber&page=$a&rev=$tp_hi&no=$no$pp$Wf\">$j</a>\n";
			$a+=$topic;
		}
		if($FL){$FL.="　[ $RP]";}else{$FL="<br>　<small>[ $RP]";}
	}
	$FL.="</small>";
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
		$news.="<img src=\"$IconDir\/$mICO\" border=0$WHm>";
	}
	if($TXT_F){if($txt){$Txt="<td>$txt</td>";}else{$Txt="<td>/</td>";}}
	if($SEL_F){if($sel){$Sel="<td>$sel</td>";}else{$Sel="<td>/</td>";}}
	$ksu=$R{$namber}+1;
	print"<tr bgcolor=\"$k_back\" align=center>$Sel$Txt<td align=left>";
	print"<a href=\"$cgi_f?mode=al2&namber=$namber&rev=$r&no=$no$pp\">$news <b>$d_may</b></a>$FL</td>";
	print"<th>$ksu</th>$TP2$SK2<td><small>$rdd</small></td>";
	if($end_f){print"<td>$reok</td>";}
	print"</tr>\n";
	$rdd=""; $rn=""; $rid="";
	if($tpmax <= $TableChange || $_ >= $total-1){print"</table><br><hr width=\"95\%\">\n"; $TableChange=0;}
}
print"</center>";
&allfooter("トピック$view");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [コメント引用]
# -> トピック/スレッド表示の際の引用処理(comin_)
#
sub comin_{
if($sp==0){$re=1;}elsif($sp>0){$re=$sp/15+1;}
if($d_may eq ""){$d_may="NO TITLE";}
if($d_may=~ /^Re\[/){
	$resuji=index("$d_may" , "\:");
	$d_may=~ s/\:\ //;
	$d_may=substr($d_may,$resuji);
}
$ti="Re[$re]: $d_may"; $space=$sp;
if($FORM{'In'} eq ""){
	$com="■No$namに返信($naさんの記事)<br>$co";
	$com=~ s/<br>/\r&gt; /g;
	$com=~ s/&gt; &gt; /&gt;&gt;/g;
}
$FORM{"type"}=$ty; $type=$ty; $namber=$nam;
}
#--------------------------------------------------------------------------------------------------------------------
# [トピック内容表示]
# -> トピック内容を表示(all2)
#
sub all2 {
if($FORM{'rev'} ne ""){$rev=$FORM{'rev'};}else{$rev=$tp_hi;}
if($space eq ""){$space=0;}
$SP=$space+15;
@TOP=(); $k=0; $Dk=0; $On=0; $En=0; $O2=0; $TitleHed="";
open(DB,"$log");
while (<DB>) {
	($nam,$da,$na,$mail,$d_may,$co,$ur,
		$sp,$end,$ty,$de,$ip,$time)=split(/<>/,$_);
	if(($ty==0 && $FORM{"namber"} eq "$nam")||($ty != 0 && $FORM{"namber"} eq $ty)){
		if($rev){
			($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
			if($ico && -s "$i_dir/$ico"){$SIZE+= -s "$i_dir/$ico";}else{$SIZE+=0;}
		}
		if($space < $sp && $On==0 && $O2==0){$N_NUM=$nam; $On=1;}
		if($space eq $sp && $O2==0 && $mo ne $nam){$On=0; $N_NUM="";}
		if($time){
			$time=sprintf("%011d",$time);
			push(@TOP,"$time<>$_"); if($end){$En=1;}
		}else{$Dk++;}
		$namb=$nam; $k++; $TitleHed=$d_may;
		if($mo){if($mo eq $nam){$On=1; $O2=1; &comin_;}}else{if($k==1){$On=1; $O2=1; &comin_;}}
	}else{if($k && $KLOG eq ""){last;}}
}
close(DB);
@TOP=sort(@TOP);
if($rev){@TOP=reverse(@TOP);}
$fhy ="<a name=F><table width=\"90\%\" align=center>\n";
$fhy.="<tr><th bgcolor=$ttb>このトピックに書きこむ</th></tr></table></a></center>\n";
$total=@TOP;
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$PAGE=$page/$topic;
&hed_("One Topic All View / $TitleHed / Page: $PAGE","1");
print"<center>";
if($rev == 0){
	print"<b>[ <a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&rev=1&no=$no$pp\">";
	print"最新記事及び返信フォームをトピックトップへ</a> ]</b><br><br>\n";
}elsif($rev){
	print"<b>[ <a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&rev=0&no=$no$pp\">親記事をトピックトップへ</a> ]</b><br><br>\n";
}
if($rev){
	print"$fhy";
	if($r_max && ($total-1) >= $r_max){
		print"<center><br><h3>レス数の限度を超えたのでレスできません。</h3>(レス数限度:$r_max 現在のレス数:$#TOP)\n";
		print" → <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[トピックの新規作成]</a></b></center>";
	}else{&forms_("F");}
	print"<center>\n";
}
$page_=int(($total-1)/$topic);
$end_data=@TOP-1;
$page_end=$page+($topic-1);
if($page_end >= $end_data){$page_end=$end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end+1; 
$bl=$page-$topic;
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$nl&rev=$rev&no=$no$pp\">"; $Nle="</a>";}
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$bl&rev=$rev&no=$no$pp\">"; $Ble="</a>";}
print"</center><ul>[ トピック内全$total記事($Pg-$Pg2 表\示) ]　\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$topic;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$a&rev=$rev&no=$no$pp\">$i</a>\n";}
	$a+=$topic;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
print"$Plink<br>";
if($Dk){print"($Dk件の削除記事を非表\示)<br>";}
print"</ul><center>\n";
$i=0; $ToNo=$page; $SIZE=0;
foreach ($page .. $page_end) {
	($T,$nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$TOP[$_]);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	$ToNo++;
	if($rev){$fp=0;}else{$fp=$topic*$page_;}
	&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
		$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ToNo,"F","");
	print"$HTML\n";
}
if($TrON){$TrLink="<a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&no=$no$pp\">$all_i このトピックをツリーで一括表\示</a>";}
print"</center><ul>$TrLink</ul>\n";
print"<center><hr width=\"90\%\"><b>\n";
if($Bl){print"$Bl＜前の$topic件$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl次の$topic件＞$Nle\n";}
print"</b><br><br>トピック内ページ移動 / $Plink";
$Ta=$total-1;
if($r_max && $Ta > $r_max){
	print"<br><br><h3>レス数の限度を超えたのでレスできません。</h3>(レス数限度:$r_max 現在のレス数:$Ta)";
	print" → <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[トピックの新規作成]</a></b></center>";
}else{
	if($En && $end_e){print"<center><h3>$end_ok / 返信不可</h3></center>";}
	else{
		if($total <= ($page+$topic) && $rev==0){
			print"<br><br>$fhy</center>";
			&forms_("F");
		}elsif($total >= ($page+$topic) && $rev==0){
			$page=$i-1; $a-=$topic;
			print"<br><br><b>[<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$a&no=$no$pp#F\">このトピックに返信</a>]</b>";
		}
	}
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [フォーム]
# -> フォームを表示する(forms_)
#
sub forms_ {
if($s_ret && $P ne "$s_pas"){print"<center><h3>書き込み不可</h3></center>\n";}
elsif($KLOG){print"<center><h3>過去ログには書き込み不可</h3></center>";}
else{
	if($FORM{'PV'}){
		$N_NUM=$FORM{"N"}; $nams=$type; $namber=$kiji; $sp=$space;
		if($FORM{'pub'}){$c_pub=1;} if($FORM{'end'}){$PVC=" checked";}
		if($FORM{'send'}){$PVE=" selected";}
	}else{
		&get_;
		if($FORM{'type'} eq ""){$sp=0;}elsif($FORM{'type'}==0){$sp=15;}elsif($FORM{'type'} > 0){$sp=$space+15;}
		if($namber eq ""){$namber=0;}
		if($FORM{'type'} > 0){$nams=$type;}elsif($FORM{'type'}==0){$nams=$namber;}
		$T=" checked";
	}
	if($o_mail){
		if($c_pub){$Pch=" selected";}
		$Mbox= <<_MAIL_;
<tr><td colspan=2>
└&gt; 関連するレス記事をメールで受信しますか?<select name=send>
<option value=0>NO
<option value=1$PVE>YES
</select> /
アドレス<select name=pub>
<option value=0>非公開
<option value=1$Pch>公開
</select></td></tr>
_MAIL_
	}
	if($he_tp){
		$TPH="<h3>トピックを作成した時の削除キーでのみ返信ができます。</h3>";
		$KEY="/トピック追加には削除キーが必須です!\n";
	}
	if(($com =~ /<pre>/)&&($com =~ /<\/pre>/)){$com=~ s/<pre>//g;$com=~ s/<\/pre>//g;}
	if($tag){$com=~ s/</&lt;/g; $com=~ s/>/&gt;/g;}
	if($mas_c==2 && $Ent==0){$com="コメント表示:未許可";}
	if($Res_i && $mo eq "" && $FORM{'PV'} eq ""){$com="";}
	if($i_mode && ($ResUp || ($ResUp==0 && $sp==0))){
		$FORM_E=" enctype=\"multipart/form-data\"";
		$FI="<tr><td bgcolor=$ttb>File</td><td>/<input type=file name=ups size=60$ff><br>アップ可能\拡張子=&gt;\n";
		foreach (0..$#exn) {
			if($exi[$I] eq "img"){$EX="<b>$exn[$_]</b>";}else{$EX="$exn[$_]";}
			$FI.="/$EX"; $I++;
		}
		$FI.=<<"_M_";
<br>
1) 太字の拡張子は画像として認識されます。<br>
2) 画像は初期状態で縮小サイズ$H2×$W2ピクセル以下で表\示されます。<br>
3) 同名ファイルがある、またはファイル名が不適切な場合、<br>
　　ファイル名が自動変更されます。<br>
4) アップ可能\ファイルサイズは1回<B>$max_fs\KB</B>(1KB=1024Bytes)までです。<br>
5) ファイルアップ時はプレビューは利用できません。<br>
_M_
		if($ResUp && $sp){
			$SIZE=int($SIZE/1024);
			$Rest=$max_or-$SIZE;
			$FI.="6) スレッド内の合計ファイルサイズ:[$SIZE/$max_or\KB] <b>残り:[$Rest\KB]</b>\n";
		}
	}else{$FORM_E=""; $FORM_I="";}
	if($NMAX){$NML=" maxlength=$NMAX";}
	if($TMAX){$YML=" maxlength=$TMAX";}
	if($CMAX){$CML="/半角$CMAX文字以内";}
	if($UID){$uidv=" [ID:$pUID]<!--←<a href=\"$cgi_f?mode=cookdel\" target=\"_blank\">このIDを破棄</a>-->";}
	if($tag){$tagmsg="可能\です。";}else{$tagmsg="できません。";}
	if($FORM{"PV"} eq ""){print"<form action=\"$cgi_f\" method=\"$met\"$FORM_E>";}
	print <<"_FORM_";
<ul><ul><li>入力内容にタグは利用$tagmsg</ul>$atcom<br><input type=hidden name=N value=$N_NUM>
<input type=hidden name=mode value=wri><input type=hidden name=type value=$nams>
<input type=hidden name=kiji value=$namber><input type=hidden name=space value=$sp>
$nf$pf$Hi$TPH<table border=0>
<tr><td bgcolor=$ttb>Name</td><td>/
<input type=text name="name" value="$c_name" size=25$ff$NML>$uidv</td></tr>
<tr><td bgcolor=$ttb>E-Mail</td><td>/
<input type=text name="email" value="$c_email" size=40$ff></td></tr>
$Mbox<tr><td bgcolor=$ttb>Title</td><td>/
<input type=text name="d_may" size=40 value="$ti"$ff$TML></td></tr>
<tr><td bgcolor=$ttb>URL</td><td>/
<input type=text name="url" value="ttp://$c_url" size=70$ff></td></tr>
<tr><td colspan=2 bgcolor=$ttb>Comment/
通常モード-&gt;<input type=radio name=pre value=0$T>　
図表\モード-&gt;<input type=radio name=pre value=1$Z>
(適当に改行して下さい$CML)<br>
<textarea name="comment" rows=12 cols=75 wrap=$wrap$ff>$com</textarea></td></tr>
$FI
_FORM_
	if(@fonts){
		print "<tr><td bgcolor=$ttb>文字色</td><td>/\n";
		foreach (0 .. $#fonts) {
			if($c_font eq ""){$c_font="$fonts[0]";}
			print"<input type=radio name=font value=\"";
			if($c_font eq "$fonts[$_]"){print"$fonts[$_]\" checked><font color=$fonts[$_]>■</font>\n";}
			else{print"$fonts[$_]\"><font color=$fonts[$_]>■</font>\n";}
		}
		print"</td></tr>";
	}
	if(@hr){
		print"<tr><td bgcolor=$ttb>枠線色</td><td>/\n";
		foreach (0 .. $#hr) {
			if($c_hr eq ""){$c_hr="$hr[0]";}
			print "<input type=radio name=hr value=\"";
			if($c_hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=$hr[$_]>■</font>\n";}
			else{print"$hr[$_]\"><font color=$hr[$_]>■</font>\n";}
		}
		print"</td></tr>";
	}
	if($Icon){
		print"<tr><td bgcolor=$ttb>Icon</td><td>/ <select name=Icon>\n";
		foreach(0 .. $#ico1) {
			if($c_ico eq $ico1[$_]){print"<option value=\"$_\" selected>$ico2[$_]\n";}
			else{print"<option value=\"$_\">$ico2[$_]\n";}
		}
		print"</select> <small>(画像を選択/";
		print"<a href='$cgi_f?mode=img&no=$no$pp' target=_blank>サンプル一覧</a>)</small></td></tr>\n";
	}
	if(($SEL_F && $SEL_R==0) || ($SEL_F && $SEL_R && $sp==0)){
		print"<tr><td bgcolor=$ttb>$SEL_T</td><td>/ <select name=sel>\n";
		foreach(0 .. $#SEL) {
			if($c_sel eq "$SEL[$_]"){print"<option value=\"$SEL[$_]\" selected>$SEL[$_]\n";}
			else{print"<option value=\"$SEL[$_]\">$SEL[$_]\n";}
		}
		print"</select></td></tr>\n";
	}
	if(($TXT_F && $TXT_R==0) || ($TXT_F && $TXT_R && $sp==0)){
		print"<tr><td bgcolor=$ttb>$TXT_T</td><td>/\n";
		print"<input type=text name=txt value=\"$c_txt\" maxlength=$TXT_Mx size=$TXT_Mx></td></tr>\n";
	}
	if($space ne "" && $end_f==1){
		if($end_c){$end_form="<tr><td colspan=2>$end_ok になったらその旨も書いてください。</td></tr>";}
		else{$end_form="<tr><td colspan=2>$end_ok BOX/<input type=checkbox name=end value=\"1\"$PVC>$end_m</td></tr>";}
	}
	if($AgSg && $sp > 0){
		$AgSgIn ="記事ソ\ート/<select name=\"AgSg\">";
		if($FORM{"AgSg"} eq "0"){$SgS=" selected";}
		$AgSgIn.="<option value=1>上げる(age)<option value=0$SgS>下げる(sage)</select>\n";
	}else{$AgSgIn="<input type=hidden name=AgSg value=1>\n";}
	if($_[0]){print"<input type=hidden name=H value=$_[0]>";}
print<<"_FORM_";
<tr><td bgcolor=$ttb>削除キー</td><td>/
<input type=password name=delkey value="$c_key" size=8$ff>
<small>(半角8文字以内$KEY)</small>
</td></tr>
$end_form
<tr><td colspan=2 align=right>$AgSgIn　
プレビュー/<input type=checkbox name=PV value=1>　
<input type=submit value=" 送 信 "$fm>
<input type=reset value="リセット"$fm></td></tr></table></form></ul><hr width=\"95\%\">
_FORM_
	}
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー記事表示]
# -> ツリーの記事を表示する(one_)
#
sub one_ {
@TREE=();
open(LOG,"$log") || &er_("Can't open $log");
while ($Line = <LOG>) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim) = split(/<>/,$Line);
	if(($type==0 && ($nam eq $namber || $ty eq $namber))||($type && ($nam eq $type || $ty eq $type))){
		if($ty){
			if($Keisen){
				$SPS=$sp/15; $Lg=0; $Tg=0; $S="";
				if($SP){
					if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
					elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
				}else{$Lg=1;}
				if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
				$SP=$sp/15;
				if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
				if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
				elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
			}else{$Line="<>$Line";}
			if($date){unshift(@TREE,$Line);}
		}else{unshift(@TREE,"<>$Line"); $SP=0; @L=(); if($tim=~/[\d]+/){last;}}
	}
}
close(LOG);
$rs=0; $i=0; $ON=0; $Tree=""; $SP=0; $F=0;
foreach $lines (@TREE) {
	($Sen,$nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$lines);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	if($namber eq "$nam" && $namber ne $ty) {
		if($d_may eq ""){$d_may="NO TITLE";}
		&hed_("One Message View / $d_may","1");
		$com="■No$namberに返信($nameさんの記事)<br>$comment";
		$com=~ s/<br>/\r&gt; /g; $com=~ s/&gt; &gt; /&gt;&gt;/g;
		if($sp==0){$re=1;}elsif($sp>0){$re=$sp/15+1;}
		if($d_may=~ /^Re\[/){
			$resuji=index("$d_may" , "\:");
			$d_may=~ s/\:\ //;
			$d_may=substr($d_may,$resuji);
		}
		$ti="Re[$re]: $d_may";
		if($i==0){$i=1;}
		print"<center>";
		$ResNo=$sp/15;
		&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
			$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"T");
		print"$HTML\n";
		print"<br><table width=95\% cellspacing=0 cellpadding=0>\n";
		print"<tr align=center><td bgcolor=$ttb><b>前の記事</b><small>(元になった記事)</small></td>\n";
		print"<td bgcolor=$ttb><b>次の記事</b><small>(この記事の返信)</small></td></tr>\n";
	}
	if($end){$end="$end_ok"; $En=1;}
	if($d_may eq ""){$d_may="No Title";}
	$date=substr($date,2,19);
	if(($time_k-$tim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
	if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
	if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
	if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
		$news.="<img src=\"$IconDir\/$mICO\" border=0$WHm>";
	}
	if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2)); $d_may="$d_may..";}
	if($email && $Se < 2){$name="$name <a href=\"mailto:$email\">$AMark</a>";}
	if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr"; $SIZE+=$Size;}else{$Pr="";}
	$psp=$space+15;$nsp=$space-15;
	if(($namber eq "$ty" || $type eq "$nam" || $type eq "$ty") && $ON==0){
		if($rs && $sp <= $space && $type){$ON=1;}
		if($sp eq $nsp && $nam < $namber && $i != 1){
			$b_="<a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">←$d_may</a>\n/$name <small>$yobi</small>$Pr";
		}elsif($type == 0){$b_="親記事";}
		if($sp eq $psp && $nam > $namber && $i == 1){
			$n_.="<a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">→$d_may</a>\n/$name <small>$yobi</small>$Pr<br>";
			$N_NUM=$nam;
		}
		if($i==1){$rs=1;}
	}
	$im=""; $im2=""; $im3="";
	if($sp > $SP && $F){$N_NUM=$nam;}
	if($sp eq $SP && $F){$F=0;}
	if($N_NUM eq $nam && $F==0){$F=1; $SP=$sp;}
	if($nam eq $namber){$im="<b STYLE=\"background-color:$t_back\">"; $im2="</b>"; $im3=" <b>←Now</b>";}
	if($Keisen){$Tree.="$Sen";}
	else{
		$Tree.="<font color=$k_back>";
		$spz=$sp/15*$zure;
		$Tree.="." x $spz;
		$Tree.="</font>";
	}
	$Tree.="$im<a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">$news $d_may</a>\n";
	$Tree.="/ $name <small>($date) $yobi<font color=\"$kijino\">#$nam</font></small>$im2 $end$Pr$im3</td></tr><tr><td colspan=2 nowrap>\n";
}
print"<tr><td valign=top width=50\%>$b_</td><td width=50\%>\n";
if($n_){print"$n_\n";}else{print"返信無し<br>\n";}
print"　</td></tr><th colspan=2 bgcolor=\"$ttb\">上記関連ツリー</th></tr><tr><td colspan=2><br>$Tree\n";
$total=@TREE-1;
if($type>0){$a_="$type";}elsif($type==0){$a_="$namber";}
if($TpON){$TpLink=" / <a href=\"$cgi_f?mode=al2&namber=$a_&rev=$r&no=$no$pp\">上記ツリーをトピック表\示</a>\n";}
print"<br><a href=\"$cgi_f?mode=all&namber=$a_&type=0&space=0&no=$no$pp\">$all_i 上記ツリーを一括表\示</a>$TpLink\n";
print"<br>　</td></tr><tr><th colspan=2 bgcolor=\"$ttb\"><a name=F>上記の記事へ返信</a></th></tr></table></center>\n";
if($r_max && $total >= $r_max){
	print"<center><h3>レス数の限度を超えたのでレスできません。</h3>(レス数限度:$r_max 現在のレス数:$total)\n";
	print" → <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[ツリーの新規作成]</a></b></center>\n";
}else{if($En && $end_e){print"<center><h3>$end_ok / 返信不可</h3></center>";}else{&forms_("T");}}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー表示]
# -> ツリーの一覧を表示する(html_)
#
sub html_ {
@NEW=(); @RES=(); @SEN=(); $SP=0; %RES=(); %R=();
if($FORM{'page'}){$page=$FORM{'page'};}else{$page=0;}
open(LOG,"$log") || &er_("Can't open $log");
while ($Line = <LOG>) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim) = split(/<>/,$Line);
	if($type){
		$RS++;
		if($R{$type}){$R{$type}++;}else{$R{$type}=1;}
		if(($OyaCount > $page+$a_max || $page > $OyaCount+1) && $Res_T==0 && $tim=~/[\d]+/){next;}
		if($date){
			if($Keisen){
				$SPS=$space/15; $Lg=0; $Tg=0; $S="";
				if($SP){
					if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
					elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
				}else{$Lg=1;}
				if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
				$SP=$space/15;
				if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
				if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
				elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
			}else{$Line="<>$Line";}
			$RES{$type}="$Line".$RES{$type};
		}
	}else{
		if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
		if($Res_T==2){$tim=$R{$namber}; $tim=sprintf("%05d",$tim);}
		push(@NEW,"$tim<>$Line"); $SP=0; @L=(); $OyaCount=@NEW;
	}
	$TIM=$tim;
}
close(LOG);
if($Res_T){@NEW=sort(@NEW); @NEW=reverse(@NEW);}
@lines=(); $total=@NEW; $NS=$total+$RS;
$PAGE=$FORM{"page"}/$a_max;
&hed_("All Tree / Page: $PAGE");

$page_=int(($total-1)/$a_max);
$end_data=@NEW-1;
$page_end=$page + ($a_max - 1);
if($page_end >= $end_data){$page_end=$end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end + 1;
$bl=$page - $a_max;
if($bl >= 0){$Bl="<a href=\"$cgi_f?page=$bl&H=T&no=$no$pp$Wf\">"; $Ble="</a>";}else{$Bl=""; $Ble="";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?page=$nl&H=T&no=$no$pp$Wf\">";$Nle="</a>";}else{$Nl=""; $Nle="";}
print <<"_HTML_";
<center><table cellspacing=0 cellpadding=0><tr><td>
$com_top
</td></tr><tr><td>
■ $new_t時間以内の記事は $new_i で表\示されます。<br>
■ $all_i をクリックするとそのツリーを一括で表\示します。
</td></tr></table>$Henko<hr width=\"95\%\">
_HTML_
if($i_mode){&minf_("T");}

print"</center><ul>[ 全$totalツリー($Pg-$Pg2 表\示) ]　\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$a_max;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?page=$a&H=T&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$a_max;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=T&W=W&no=$no$pp\">更新順</a>"; $OJ2="投稿順"; $OJ3="<a href=\"$cgi_f?H=T&W=R&no=$no$pp\">レス数</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=T&W=W&no=$no$pp\">更新順</a>"; $OJ2="<a href=\"$cgi_f?H=T&W=T&no=$no$pp\">投稿順</a>"; $OJ3="レス数";}
else{$OJ1="更新順"; $OJ2="<a href=\"$cgi_f?H=T&W=T&no=$no$pp\">投稿順</a>"; $OJ3="<a href=\"$cgi_f?H=T&W=R&no=$no$pp\">レス数</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ] ←ソ\ート方法変更 </ul><center>";
foreach ($page .. $page_end) {
	($T,$namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
	if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
	if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
		$news.="<img src=\"$IconDir\/$mICO\" border=0$WHm>";
	}
	if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
	if($d_may eq ""){$d_may="No Title";}
	if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
	if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
	if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
	if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may.."; }
	$date=substr($date,2,19);
	print <<"_HTML_";
<table width=95% bgcolor=$bg cellspacing=0 cellpadding=0 border=0>
<tr><td bgcolor=$obg width=1\% nowrap>
<a href="$cgi_f?mode=all&namber=$namber&type=$type&space=$space&no=$no$pp">$all_i</a></td>
<td bgcolor=$obg><a href="$cgi_f?mode=one&namber=$namber&type=$type&space=$space&no=$no$pp">$news $d_may</a>
/ $name <small>($date) $yobi<font color=$kijino>#$namber</font></small>$Pr
_HTML_
	$res=0;
	@RES= split(/\n/,$RES{$namber});
	foreach $lines(@RES) {
		($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
			$rsp,$re,$rtype,$del,$ip,$rtim,$M) = split(/<>/,$lines);
		if($re ne ""){$re="$end_ok";}
		if($namber eq "$rtype"){
			if(($time_k-$rtim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
			if($rmail && $M < 2){$rname="$rname <a href=\"mailto:$SPAM$rmail\">$AMark</a>";}
			$rd=substr($rd,2,19);
			($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
			($rICON,$ICO,$font,$hr)=split(/\|/,$TXT);
			($txt,$sel,$yobi)=split(/\|\|/,$SEL);
			if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(携帯\)$/)){
				if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
				if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
				elsif($Icon && $rcom=~/<br>\(携帯\)$/){$mrICO="$Ico_km";}
				$news.="<img src=\"$IconDir\/$mrICO\" border=0$WHm>";
			}
			if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
			if($rdm eq ""){$rdm="No Title"; }
			if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
			if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
			if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
			if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$rdm="$Txt$Sel/"."$rdm";}}
			if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2)); $rdm="$rdm..";}
			print "</td></tr><tr><td></td><td nowrap>\n";
			if($Keisen){print"$Sen";}
			else{
				print "<font color=$bg>";
				$rspz=$rsp/15*$zure;
				print "." x $rspz;
				print "</font>";
			}
			print"<a href=\"$cgi_f?mode=one&namber=$rnam&type=$rtype&space=$rsp&no=$no$pp\">$news $rdm</a>\n";
			print"/ $rname <small>($rd) $yobi<font color=\"$kijino\">#$rnam</font></small> $re$Pr\n";
			$res++;
			if($R{$namber}==$res){last;}
		}
	}
	print "</td></tr></table><br>";
}
print"<br></center><hr width=\"95\%\">\n";
&allfooter("ツリー$a_max");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ツリー一括表示]
# -> ツリーの関連記事を表示する(all_)
#
sub all_ {
@TREE=();
open(DB,"$log");
while ($Line = <DB>) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim) = split(/<>/,$Line);
	if(($type==0 && ($nam eq $namber || $ty eq $namber))||($type && ($nam eq $type || $ty eq $type))){
		if($ty){
			if($Keisen){
				$SPS=$sp/15; $Lg=0; $Tg=0; $S="";
				if($SP){
					if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
					elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
				}else{$Lg=1;}
				if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
				$SP=$sp/15;
				if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
				if($Lg){$Line="<tt>$S$K_L</tt><>$Line";}
				elsif($Tg){$Line="<tt>$S$K_T</tt><>$Line";}
			}else{$Line="<>$Line";}
			if($date){unshift(@TREE,$Line);}
		}else{unshift(@TREE,"<>$Line"); $SP=0; @L=(); if($tim=~/[\d]+/){last;}}
	}
}
close(DB);
&hed_("One Tree All Message");
print<<"_ALLTOP_";
<center><table width=90\% cellspacing=0 cellpadding=0><tr>
<th bgcolor=$ttb>ツリー一括表\示</th></tr>$IcCom
<tr><td><br>
_ALLTOP_
$ALLTREE="";
foreach $line (@TREE) {
	($Sen,$nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$line);
	if($end ne ""){$end="$end_ok";}
	if(($ty == 0 && $namber eq "$nam")||($ty != 0 && $namber eq $ty)){
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		$n_="";
		$rs=0;$i=0;
		foreach $Line (@TREE) {
			($S,$n,$d,$na,$e,$dm,$c,$u,$s,$e,$t) = split(/<>/,$Line);
			if($nam eq $n){$i=1;}
			if(($t==0 && $namber eq "$n")||($t != 0 && $namber eq $t)){
				if($rs && $sp eq "$s"){last;}
				$psp=$sp+15;$nsp=$sp-15;
				if($s eq $nsp && $nam > $n && $i != 1){$b_="<a href=\#$n>▲[ $n ]</a> / ";}
				if($s eq $psp && $nam < $n && $i == 1){$n_.="<a href=\#$n>▼[ $n ]</a>\n";}
			}
		if($i==1){$rs=1;}
		}
		$ResNo=$sp/15;
		&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
			$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"T2");
		$ALLTREE.="$HTML";
		if($email && $Se < 2){$name="$name <a href=\"mailto:$email\">$AMark</a>";}
		if(($time_k-$tim)>$new_t*3600){$news = "$hed_i";}else{$news="$new_i";}
		if($d_may eq ""){$d_may = "No Title";}
		$date=substr($date,2,19);
		if($Keisen){print"$Sen";}
		else{
			print "<font color=$k_back>";
			$spz=$sp/15*$zure;
			print "." x $spz;
			print "</font>";
		}
		if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
		if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
		if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
		if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
		if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
		if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(携帯\)$/)){
			if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
			if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
			elsif($Icon && $comment=~/<br>\(携帯\)$/){$mICO="$Ico_km";}
			$news.="<img src=\"$IconDir\/$mICO\" border=0$WHm>";
		}
		if($i_mode && $ico){$Pr=""; &size(1); $Pr=" "."$Pr"; $CookOn="";}else{$Pr="";}
		print"<a href=#$nam>$news $d_may</a>\n";
		print"/$name <small>($date) $yobi<font color=\"$kijino\">#$nam</font></small> $end$Pr</td></tr><tr><td nowrap>\n";
	}
}
print"</td></tr></table><br>\n";
print"$ALLTREE<br><br></center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [新着記事表示]
# -> 新着記事を表示する(n_w_)
#
sub n_w_ {
@NEW=();
open(DB,"$log");
while (<DB>) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$_);
	if(($time_k - $tim) <= $new_t*3600){push(@NEW,"$tim<>$_<>");}
}
close(DB);

&hed_("New Message");
$total=@NEW;
$page_=int(($#NEW)/$new_s);
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$end_data=@NEW-1;
$page_end=$page + ($new_s - 1);
if($page_end >= $end_data) { $page_end = $end_data; }
$Pg=$page+1; $Pg2=$page_end+1;
$nl = $page_end + 1;
$bl = $page - $new_s;
if($bl >= 0){$Bl="<a href=\"$cgi_f?page=$bl&mode=n_w&no=$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?page=$nl&mode=n_w&no=$no$pp\">"; $Nle="</a>";}
print <<"_FTOP_";
<center><table width=90\%><tr><th bgcolor=$ttb>$new_t時間以内に投稿された新着記事</th></tr></table><br></center>
<ul>[ 新着記事全$total件($Pg-$Pg2 を表\示) ]　
_FTOP_
$Plink="$Bl\&lt\;\&lt\;$Ble\n";$a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$new_s;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=n_w&page=$a&no=$no$pp\">$i</a>\n";}
	$a+=$new_s;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
if($FORM{"s"} ne ""){$new_su=$FORM{"s"};}
if($new_su){$SL1="新着順"; $SL2="<a href=\"$cgi_f?mode=n_w&s=0&no=$no$pp\">古い順</a>";}
else{$SL1="<a href=\"$cgi_f?mode=n_w&s=1&no=$no$pp\">新着順</a>"; $SL2="古い順";}
print"$Plink<br>[ $SL1 / $SL2 ] ←ソ\ート方法変更</ul><center>";
if(@NEW){
	@NEW=sort @NEW;
	if($new_su){@NEW=reverse(@NEW);}
	foreach ($page..$page_end) {
		($Tim,$nam,$date,$name,$email,$d_may,$comment,$url,
			$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
			$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"N");
		print"$HTML\n";
	}
	print"</center><br><ul><b>\n";
	if($Bl){print"$Bl＜前の$new_s件$Ble\n";}
	if($Nl){if($Bl){print"| ";} print"$Nl次の$new_s件＞$Nle\n";}
	print"</b><ul>( ページ移動 / $Plink )</ul></ul><br>\n";
}else{print"<br>新着記事はありません。<br><br>\n";}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [新規投稿]
# -> 新規投稿のフォームを表示する(new_)
#
sub new_ {
if($topok==0 && $FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}
&hed_("Write New Message","1");
print"<center><table width=90\%><tr><th bgcolor=$ttb>";
if($TrON){$T01="ツリー　";} if($TpON){$T02="トピック　";} if($ThON){$T03="スレッド　";}
print"$T01$T02$T03の新規作成</th></tr></table></center>\n";
&forms_;
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ログ書きこみ処理]
# -> ログに記事を書き込む(wri_)
#
sub wri_ {
if($s_ret && $P ne "$s_pas"){&er_("パスワードが違います!");}
if($KLOG){&er_("過去ログには書き込みできません!");}
&check_;
if($FORM{"PV"} && $FLAG==0){
	&hed_("Preview","1");
	$c_name=$name; $c_email=$email; $ti=$d_may; $c_txt=$txt; $c_sel=$sel;
	$c_ico=$CICO; $c_hr=$hr; $c_font=$font; $c_key=$delkey;
	$com=$comment; $com=~ s/<br>/\n/g;
	if(($com=~ /^<pre>/)&&($com=~ /<\/pre>$/)){$Z=" checked";}else{$T=" checked";}
	$c_url=$url;
	if($i_mode && ($ResUp || ($ResUp==0 && $sp==0))){$FORM_E=" enctype=\"multipart/form-data\"";}
	else{$FORM_E="";}
	if($tag){
		$comment=~ s/\&lt\;/</g;
		$comment=~ s/\&gt\;/>/g;
		$comment=~ s/\&quot\;/\"/g;
		$comment=~ s/<>/\&lt\;\&gt\;/g;
	}
	&design("",$date,$name,$email,$d_may,$comment,$url,$space,$end,$type,$delkey,$ip,$tim,"",
		"","","",$ICO,$font,$hr,$txt,$sel,$yobi,$send,"","P",$CICO);
	if($AgSg){if($FORM{"AgSg"}){$HTML.="記事ソ\ート:上げる(age)";}else{$HTML.="記事ソ\ート:下げる(sage)";}}
	print<<"_PV_";
<center><table width=95\%><tr><th bgcolor=$ttb>プレビュー</th></tr></table><br>
$HTML
<form action="$cgi_f" method="$met"$FORM_E>
<input type=submit value="送信 O K"$fm> / <b>[<a href="#F">書き直す</a>]</b>
<br><br><a name="F">
<table width=90\%><tr><th bgcolor=$ttb>▽ 書き直す ▽</th></tr></table></a></center>
_PV_
	&forms_($H);
	&foot_;
}
if($FORM{'URL'}){
	($KURL,$Ag) = split(/::/,$FORM{'URL'});
	$comment.="<br><br>(携帯)";
}
if($UID){
	if($Ag){$pUID=$Ag;}else{&get_("I");}
	if($pUID eq "n"){&er_("ブラウザのcookie機能\がOFFでは投稿不可。対応ブラウザにするか、ONにしてください!");}
}
&set_; &cry_;
if($pUID){&set_("I","$pUID");}
if($tag){
	$comment=~ s/\&lt\;/</g;
	$comment=~ s/\&gt\;/>/g;
	$comment=~ s/\&quot\;/\"/g;
	$comment=~ s/<>/\&lt\;\&gt\;/g;
}
if($locks){&lock_("$lockf");}
if($M_Rank){&rank;}
open(LOG,"$log") || &er_("Can't open $log");
@lines = <LOG>;
close(LOG);
$NOWTIME=time; &time_($NOWTIME);
if($bup){&backup_;}
($knum,$kd,$kname,$kem,$ksub,$kcom)=split(/<>/,$lines[0]);
$namber=$knum+1;
if($kd eq "" && $kcom eq ""){shift(@lines);}
if($mas_c){$E=0;}else{$E=1;}
$oya=0; @new=(); $SeMail=""; $WR=0; $R=~ s/:/：/g; $SIZE=0;
$txt=~ s/\:/：/g; $sel=~ s/\:/：/g; $txt=~ s/\|\|/｜｜/g; $sel=~ s/\|\|/｜｜/g; 
if($file){$SIZE+=-s "$i_dir/$file";}
if($o_mail){if($send && $FORM{'pub'}==0){$send=2;}elsif($send==0 && $FORM{'pub'}==0){$send=3;}}
$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$space<>$end<>$type<>$epasswd<>";
$new_.="$Ip:$file:$E:$TL:$ICON\|$ICO\|$font\|$hr\|:$txt\|\|$sel\|\|$pUID\|\|:$R:<>$time_k<>$send<>\n";
if ($res_r==1 && $type != 0) {
	@r_date=();
	foreach (0 .. $#lines) {
		$resres=0;
		($nam,$d,$na,$mail,$d_m,$com,$u,$s,$e,$ty,$de,$ip,$tim,$sml) = split(/<>/,$lines[$_]);
		$sml=~ s/\n/0/;
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		if($name eq $na && $comment eq $com){&er_("同じ内容は送信不可!","1");}
		if($FORM{'N'} eq $nam){	push(@r_data,$new_); $oya=1; $resres=1;}
		if($ty == 0 && $nam eq "$type"){
			if($i_mode && $ico){$SIZE+=-s "$i_dir/$ico";}
			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
			$new_line="$lines[$_]";
			if($he_tp){&cryma_($de); if($ok eq "n"){&er_("トピック制作者しか返信できません!","1");}}
			if(($nam eq "$kiji" && $oya==0) && $FORM{'N'} eq ""){push(@r_data,$new_); $oya=1;}
			$resres=1;
			if($FORM{"AgSg"}==0){push(@new,@r_data); push(@new,$new_line);}
		}elsif($ty eq "$type"){
			if($i_mode && $ico){$SIZE+=-s "$i_dir/$ico";}
			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
			if(($nam eq "$kiji" && $oya==0)||($ty eq "$kiji" && $oya==0 && $space > 15) && $FORM{'N'} eq ""){
				push(@r_data,$new_); $oya=1;
			}
			push(@r_data,$lines[$_]);
			if($he_tp){&cryma_($de); if($ok eq "n"){&er_("トピック制作者しか返信できません!","1");}}
			$resres=1;
		}
		if($resres == 0){push(@new,$lines[$_]);}
	}
	if($FORM{"AgSg"}){unshift(@new,$new_line); unshift(@new,@r_data);}
}else{
	$h=0; $ON=0; @KLOG=();
	foreach (0 .. $#lines) {
		($nam,$d,$na,$mail,$d_m,$com,$u,$s,$e,$ty,$de,$ip,$tim,$sml)=split(/<>/,$lines[$_]);
		($IP,$i,$E)=split(/:/,$ip);
		if($name eq $na && $comment eq $com){ &er_("同じ内容は送信不可!","1"); }
		$sml =~ s/\n/0/;
		if($ty==0){$h++;}
		if($FORM{'N'} eq $nam){push(@new,$new_); $oya=1;}
		if($nam eq "$kiji" && $FORM{'N'} eq ""){
			if($i_mode && $i){$SIZE+=-s "$i_dir/$i";}
			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
			push(@new,$new_);
			$oya=1;
		}
		if($ON){
			if($i && -e "$i_dir/$i" && $LogDel){unlink("$i_dir/$i");}
			if($klog_s){unshift(@KLOG,$lines[$_]);}else{if($i_mode==0){last;}}
		}else{push(@new,$lines[$_]);}
		if($h >= $max-1){$ON=1;}
	}
}
if($SIZE && $max_or < int($SIZE/1024)){&er_("限度ファイルサイズを超えたので、ファイルアップできません!","1");}
if($type==0 || $oya==0){unshift(@new,$new_);}
elsif($oya){unshift(@new,"$namber<><><><><><><><><>$namber<><><><><>\n");}

open(LOG,">$log") || &er_("Can't write $log","1");
print LOG @new;
close(LOG);
if($i_mode){&get_("M"); &set_("M");}
if($klog_s && @KLOG){&log_;}
if(-e $lockf){rmdir($lockf);}
if($t_mail || $o_mail){&mail_;}
if($KURL){&ktai("書き込み","$KURL");}
if($H eq "F" && $tpend && $type){$FORM{"namber"}=$type; $space=0; &all2;}
}
#--------------------------------------------------------------------------------------------------------------------
# [記事一括削除]
# -> 記事フォーマットをおこなう(s_d_)
#
sub s_d_ {
if($s_ret && $P ne "$s_pas"){&er_("パスワードが違います!");}
if($FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}

open(DB,">$log");
print DB "";
close(DB);
$msg="<h3>フォーマット完了</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [説明書]
# -> 簡易ヘルプを表示する(man_)
#
sub man_ {
&hed_("Help");
if($TrON){$Tr=" ツリー ";}else{$Tr="";}
if($TpON){$Tp=" トピック ";}else{$Tp="";}
if($ThON){$Th=" スレッド ";}else{$Th="";}
print <<"_HTML_";
<center><table width=95\%><tr><th bgcolor="$ttb">$title マニュアル</th></tr>
<tr><td bgcolor="$k_back">
□ 基本事項/使用方法<ul>
<li><b>電子掲示板(BBS)について</b>
<ul><u>電子掲示板(BBS)とは、インターネット上で不特定多数に公開されている公の発言の場です。</u><ul>
<li>無責任な発言や、他人の悪口・個人情報などは、書き込んではいけません。
<li>そのような記述があった場合、管理者権限により予\告なく削除され、然るべき処置がとられます。</ul></ul><br>
<li><b>このBBSの記事表\示形態について</b>
<ul><u>このBBSは$Tr$Tp$Th表\示型のBBSです。</u><ul>
_HTML_
if($Tr){
	print"<li>[ツリー] ...記事を木の枝分かれのように表\示します。話の流れが分かり易いのが特徴です。<br>\n";
	print"閲覧/返信したい記事タイトルをクリックします。$all_i をクリックするとツリーを一括表\示します。<br>\n";
}
if($Tp){
	print"<li>[トピック] ...記事を話題ごとに表\示します。ひとつの話題の多くの記事をスムーズに読む事ができます。<br>\n";
	print"閲覧/返信したいトピック(話題)タイトルをクリックします。\n";
}
if($Th){
	print"<li>[スレッド] ...最初から記事内容を表\示します。一度に多くの話題に目を通すことができます。<br>\n";
	print"初期表\示で$alk_su件のスレッド(話題)とそれぞれの最新$alk_rm件の返信記事を閲覧できます。";
}
print <<"_HTML_";
</ul></ul><br>
<li><b>記事の投稿方法について</b><ul>
<li><u>新しい話題を投稿するには...</u><br>上部/下部メニューにある [新規作成] をクリックして、必要な情報を入力してください。
<li><u>既に投稿されている記事に、返信記事を投稿するには...</u><br>返信したい記事を表\示し [返信] をクリックして、
必要な情報を入力してください。</ul><br>
<li><b>その他のメニューについて</b><ul>
<li>[新着記事] をクリックすると$new_t時間内に投稿された記事を抽出して閲覧できます。
<li>[検索] をクリックするとログ内の記事をキーワードをから検索できます。
_HTML_
if($M_Rank){print"<li>[発言ランク] をクリックすると名前を元に集計された投稿回数のランキングを表\示します。\n";}
if($i_mode){print"<li>[ファイル一覧] をクリックすると投稿記事に添付されたファイルのみを閲覧できます。\n";}
if($klog_s){print"<li>[過去ログ] をクリックすると過去の話題を閲覧できます。過去ログの検索は [検索] から行ないます。\n";}
print <<"_HTML_";
</ul><br><li><b>このBBSの機能\について</b><ul>
<li>話題を$max件まで保持し、それら話題内の記事には返信ができます。<br>
話題が$max件を超えた場合、更新日時が古い話題から
_HTML_
if($klog_s){print" [過去ログ] へ保存されます。返信はできません。\n";}else{print"削除されます。\n";}
if($r_max){print"<br>また、各話題毎の返信限度数は、$r_max件です。それ以上は返信できません。";}
if($end_f && $end_c==0){print"<li>話題が $end_ok になった時、$end_ok BOX をチェックして投稿してください。\n";}
elsif($end_c && $end_f){print"<li>話題が $end_ok になった時、その旨をお知らせ下さい。管理者がチェックします。\n";}
if($UID){
	print"<li>投稿者には個別のIDが発行されます(ランダムな半角英数8文字)。他人に成りすますことを防ぎます。<br>\n";
	print"この場合、ブラウザのcookieが ON でなければ投稿できません(ブラウザの初期設定ではONになっています)。\n";
}
if($SPAM){
	print"<li>メールアドレス自動収集ソ\フト対策のため、メールリンクに $SPAM という文字列を付加して表\示しています。<br>\n";
	print"メールを送る際は $SPAM という文字列を削除してください。\n";
}
if($i_mode){
	print"<li>ローカル(自分のPC内)にある$max_fs\KB以内のファイルをアップロードすることができます。<br>\n";
	print"詳しくは投稿の際の説明を参照してください。\n";
}
print <<"_HTML_";
<li>$new_i\...$new_t時間内に投稿された話題/記事 $up_i_\...$new_t時間内に更新された話題 $hed_i\...左記以外の話題/記事
<li>cookieに対応しています。このBBSに関するcookieを削除することもできます。
→[<a href=\"$cgi_f?mode=cookdel\" target="_blank">cookieの削除</a>]<br>
cookie...ブラウザが入力内容を保存しておく機能\です。別のサイトで利用されることは通常ありません。
<li>記事投稿の際 削除キー(任意のパスワード) を入力することによって、自分の投稿記事の編集/削除ができます。
</ul></ul><hr>
□ 書き込む際の注意
$atcom
</td></tr></table></center>
_HTML_
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ヘッダ表示]
# -> HTMLヘッダの生成(hed_)
#
sub hed_ {
print"Content-type: text/html; charset=Shift_JIS\n";
if($UID && $_[1]==1){
	&get_("I");
	if($pUID eq "n"){
		$pUID="";
		@UID = ('a'..'z','A'..'Z','0'..'9');
		srand;
		$pUID.="$UID[int(rand(62))]"; $pUID.="$UID[int(rand(62))]";
		$pUID.="$UID[int(rand(62))]"; $pUID.="$UID[int(rand(62))]";
		$pUID.="$UID[int(rand(62))]"; $pUID.="$UID[int(rand(62))]";
		$pUID.="$UID[int(rand(62))]"; $pUID.="$UID[int(rand(62))]";
		&set_("I","$pUID");
	}
	if($pUID eq "n"){$pUID="未発行";}
}
print"\n";
print <<"_HTML_";
<html>
<head>
<meta http-equiv="Content-type" content=\"text/html; charset=Shift_JIS">
$STYLE
$fsi
<!--$ver-->
<title>$title [$_[0]]</title>
</head>
_HTML_
print"<body text=$text link=$link vlink=$vlink bgcolor=$bg";
if($back ne ""){print" background=\"$back\">\n";}elsif($back eq ""){ print ">\n";}
print <<"_HTML_";
<!--ヘッダ広告タグ挿入位置▽-->

<!--△ここまで-->
<center>
_HTML_
if($t_img){print"<img src=\"$t_img\" width=$twid height=$thei>\n";}
else{print"<span style=\"font-size:$tsize;color:$tcolor;font-family:$tface;\">$title</span>\n";}
$BG=" bgcolor=$t_back";
if($mode eq "man"){$T1="$BG";}elsif($mode eq "n_w"){$T2="$BG";}elsif($mode eq "one"){$T5="$BG";}
elsif($mode eq "new"){$T3="$BG";}elsif($mode eq "alk"){$T4="$BG";}elsif($mode eq "all"){$T5="$BG";}
elsif($mode eq "al2"){$T7="$BG";}elsif($mode eq "ran"){$T6="$BG";}elsif($mode eq "res"){$T4="$BG";}
elsif($mode eq "f_a"){$T8="$BG";}elsif($mode eq "" || $mode eq "wri"){
	if($H){if($H eq "T"){$T5="$BG";}elsif($H eq "F"){$T7="$BG";}elsif($H eq "N"){$T4="$BG";}}
	else{if($TOPH==1){$T5="$BG";}elsif($TOPH==2){$T7="$BG";}else{$T4="$BG";}}
}
if($klog_s){$klog_link="<td><a href=\"$srch?mode=log&no=$no$pp\">過去ログ</a></td>\n";}
if($M_Rank){$rank_link="<td$T6><a href=\"$cgi_f?mode=ran&no=$no$pp\">発言ランク</a></td>\n";}
if($topok){$New_link="<td$T3><a href=\"$cgi_f?mode=new&no=$no$pp\">新規作成</a></td>\n";}
if($TrON){$TrL="<td$T5><a href=\"$cgi_f?H=T&no=$no$pp$Wf\">ツリー表\示</a></td>\n";}
if($TpON){$TpL="<td$T7><a href=\"$cgi_f?H=F&no=$no$pp$Wf\">トピック表\示</a></td>\n";}
if($ThON){$ThL="<td$T4><a href=\"$cgi_f?mode=alk&no=$no$pp$Wf\">スレッド表\示</a></td>\n";}
if($i_mode){$FiL="<td$T8><a href=\"$cgi_f?mode=f_a&no=$no$pp\">ファイル一覧</a></td>\n";}
$HEDF= <<"_HTML_";
<p><table border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$ttb><tr align=center bgcolor="$k_back">
<td><a href="$backurl">HOME</a></td>
<td$T1><a href="$cgi_f?mode=man&no=$no$pp">HELP</a></td>
$New_link<td$T2><a href="$cgi_f?mode=n_w&no=$no$pp">新着記事</a></td>
$TrL$ThL$TpL$rank_link$FiL<td><a href="$srch?no=$no$pp">検索</a></td>
$klog_link
</td></tr></table></p>
_HTML_
if($KLOG){print"<br>(現在 過去ログ$KLOG を表\示中)";}
print"$HEDF";
if($cou){&con_;} print"</center>";
}
#--------------------------------------------------------------------------------------------------------------------
# [フッタ表示]
# -> HTMLフッタの生成(foot_)
#
sub foot_ {
print"<div align=right><form action=\"$cgi_f\" method=$met>$nf$pf\n";
if($i_mode || $mas_c){print"Mode/<select name=mode><option value=del>通常管理<option value=ent>表\示許可</select>　\n";}
else{print"<input type=hidden name=mode value=del>\n";}
print <<"_HTML_";
Pass/<input type=password name=pass size=6$ff><input type=submit value=\"管理用\"$fm></form></div><br>
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
# [フォームデコード]
# -> フォーム入力内容を解釈(d_code_)
#
sub d_code_ {
$file="";
if($ENV{'CONTENT_LENGTH'} && $ENV{'CONTENT_TYPE'} =~ /^multipart\/form-data/){
	$buf=""; $read_data="";
	$remain=$ENV{'CONTENT_LENGTH'};
	binmode(STDIN);
	while($remain){
		$remain-=($read_length=sysread(STDIN, $buf, $remain));
		exit if $read_length == 0; # 接続が途中で切れた
		$read_data.=$buf;
	}
	$pos1=0; $pos2=0; $pos3=0; $UP=0;
	$delimiter="";
	while (1) {
		$pos2=index($read_data,"\r\n\r\n",$pos1)+4;
		@headers=split("\r\n",substr($read_data,$pos1,$pos2-$pos1));
		$filename=""; $name="";
		foreach(@headers){
			if($delimiter eq ""){$delimiter=$_;}
			elsif(/^Content-Disposition: ([^;]*); name="([^;]*)"; filename="([^;]*)"/i){
				if($3){
					$filename=$3;
					if($filename =~ /([^\\\/]+$)/){$filename=$1;}
				}
			}elsif(/^Content-Disposition: ([^;]*); name="([^;]*)"/i){$name= $2;}
		}
		$pos3=index($read_data,"\r\n$delimiter",$pos2);
		$size=$pos3-$pos2;
		if($filename){$UP=1; $file=$filename; $Read=$read_data; $Fsize=$size; $Pos2=$pos2;}
		elsif($name){
			$FORM{$name}=substr($read_data,$pos2,$size);
			$value=$FORM{$name};
			&jcode'convert(*value,'sjis');
			if(@NW){
				foreach(0..$#NW){
					$NW[$_]=~ s/\n//;
					if(index($value,$NW[$_]) >= 0){
						$NW[$_]=~ s/</\&lt\;/g; $NW[$_]=~ s/>/\&gt\;/g;
						&er_("「$NW[$_]」は使用できません!");
					}
				}
			}
			$value =~ s/&/&amp\;/g;
			$value =~ s/</\&lt\;/g;
			$value =~ s/>/\&gt\;/g;
			$value =~ s/\"/\&quot\;/g;
			$value =~ s/<>/\&lt\;\&gt\;/g;
			$value =~ s/<!--(.|\n)*-->//g;
			$FORM{$name}=$value;
		}
		$pos1=$pos3+length("\r\n$delimiter");
		if(substr($read_data, $pos1, 4) eq "--\r\n"){last;}
		else{$pos1+=2; if($max_count++ > 30){last;} next;}
	}
}else{
	if ($ENV{'REQUEST_METHOD'} eq "POST") {read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});}
	else { $buffer = $ENV{'QUERY_STRING'}; }
	@pairs = split(/&/,$buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		&jcode'convert(*value,'sjis');
		if(@NW && $name ne "del"){
			foreach(0..$#NW){
				$NW[$_]=~ s/\n//;
				if(index($value,$NW[$_]) >= 0){
					$NW[$_]=~ s/</\&lt\;/g; $NW[$_]=~ s/>/\&gt\;/g;
					&er_("「$NW[$_]」は使用できません!");
				}
			}
		}
		$value =~ s/&/&amp\;/g;
		$value =~ s/</\&lt\;/g;
		$value =~ s/>/\&gt\;/g;
		$value =~ s/\"/\&quot\;/g;
		$value =~ s/<>/\&lt\;\&gt\;/g;
		$value =~ s/<!--(.|\n)*-->//g;
		$FORM{$name} = $value;
		if($name eq 'del'){push(@d_,$value);}
		if($name eq 'ENT'){push(@E_,$value);}
		if($name eq 'IMD'){push(@I_,$value);}
	}
}
$d_may= $FORM{'d_may'};
$name = $FORM{'name'};
$comment=$FORM{'comment'}; $comment=~ s/\r\n|\r|\n/<br>/g;
$email =$FORM{'email'};
$url  = $FORM{'url'}; $url=~ s/^http\:\/\///;
$mode = $FORM{'mode'};
$end  = $FORM{'end'};
$space= $FORM{'space'};
$kiji = $FORM{'kiji'};
$namber=$FORM{'namber'};
$type = $FORM{'type'};
$delkey=$FORM{"delkey"};
$mo    =$FORM{"mo"};
$send = $FORM{"send"};
$no    =$FORM{"no"};
$W     =$FORM{"W"};
$H     =$FORM{"H"};
$txt   =$FORM{"txt"}; $sel=$FORM{"sel"};
$ICON  =$FORM{"Icon"}; $hr=$FORM{"hr"}; $font=$FORM{"font"};
&time_;
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie発行]
# -> cookieを発行する(set_)
#
sub set_ {
if($_[0] eq "I"){$kday=1826;}else{$kday=30;}
($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$ydayg,$isdstg) = gmtime(time + $kday*24*60*60);
$yearg += 1900;
if($secg  < 10){$secg ="0$secg"; }
if($ming  < 10){$ming ="0$ming"; }
if($hourg < 10){$hourg="0$hourg";}
if($mdayg < 10){$mdayg="0$mdayg";}
$month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
$date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
if($SEL_C){$Csel=",sel:$sel";}else{$Csel="";}
if($TXT_C){$Ctxt=",txt:$txt";}else{$Ctxt="";}
$cook="name\:$name\,email\:$email\,url\:$url\,delkey\:$delkey\,pub\:$FORM{'pub'}\,ico\:$CICO\,font\:$font\,hr\:$hr$Csel$Ctxt";
if($_[0] eq "P"){print"Set-Cookie: $s_pas=$s_pas; expires=$date_gmt\n";}
elsif($_[0] eq "M"){print"Set-Cookie: Cmin=$FORM{'min'}; expires=$date_gmt\n";}
elsif($_[0] eq "I"){print"Set-Cookie: UID=$_[1]; expires=$date_gmt\n";}
else{print "Set-Cookie: CBBS=$cook; expires=$date_gmt\n";}
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie取得]
# -> cookieを取得する(get_)
#
sub get_ { 
$cookies = $ENV{'HTTP_COOKIE'};
@pairs = split(/;/,$cookies);
foreach $pair (@pairs) {
	($NAME, $value) = split(/=/, $pair);
	$NAME =~ s/ //g;
	$DUMMY{$NAME} = $value;
}
if($_[0] eq "P"){if($DUMMY{"$s_pas"}){$FORM{"P"}=$DUMMY{"$s_pas"};}}
elsif($_[0] eq "M"){if($DUMMY{'Cmin'}){$FORM{"min"}=$DUMMY{'Cmin'};}else{$FORM{"min"}=0;}}
elsif($_[0] eq "I"){if($DUMMY{'UID'}){$pUID=$DUMMY{'UID'};}else{$pUID="n";}}
else{
	@pairs = split(/,/,$DUMMY{'CBBS'});
	foreach $pair (@pairs) {
		($name, $value)= split(/:/, $pair);
		$COOKIE{$name} = $value;
	}
	$c_name=$COOKIE{'name'};$c_email=$COOKIE{'email'};
	$c_url =$COOKIE{'url'}; $c_key  =$COOKIE{'delkey'};
	$c_pub =$COOKIE{'pub'}; $c_ico  =$COOKIE{'ico'};
	$c_font=$COOKIE{'font'};$c_hr   =$COOKIE{'hr'};
	if($SEL_C){$c_sel=$COOKIE{'sel'};}
	if($TXT_C){$c_txt=$COOKIE{'txt'};}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [時間設定]
# -> 時間を設定する(time_)
#
sub time_ {
$ENV{'TZ'} = "JST-9";
if($_[0]){$time_k=$_[0];}else{$time_k=time;}
($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime($time_k);
$year=$year+1900;
$mon++;
if($mon  < 10){$mon ="0$mon"; }
if($mday < 10){$mday="0$mday";}
if($hour < 10){$hour="0$hour";}
if($min  < 10){$min ="0$min"; }
if($sec  < 10){$sec ="0$sec"; }
$week=('Sun','Mon','Tue','Wed','Thu','Fri','Sat') [$wday];
$date="$year\/$mon\/$mday\($week\) $hour\:$min\:$sec";
}
#--------------------------------------------------------------------------------------------------------------------
# [管理用ページ]
# -> 管理モードを表示する(del_)
#
sub del_ {
if($FORM{'pass'} ne "$pass"){ &er_("パスワードが違います!"); }
&hed_("Editor");
@NEW=(); $RES=(); $FSize=0; $RS=0; @lines=(); %R=();
open(DB,"$log");
while ($Line=<DB>) {
	if($FORM{"mode2"} eq "Backup"){push(@lines,$Line);}
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$delk,$ip,$tim) = split(/<>/,$Line);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	if($i_mode && $ico){$FSize+= -s "$i_dir/$ico";}
	if($type){
		if($Keisen){
			$SPS=$space/15; $Lg=0; $Tg=0; $S="";
			if($SP){
				if($SP > $SPS){if($L[$SPS]){$Tg=1; $L[$SP]="";}else{$Lg=1; $L[$SP]="";}}
				elsif($SP==$SPS && $L[$SPS]){$Tg=1;}elsif($SP < $SPS){$Lg=1;}
			}else{$Lg=1;}
			if($SPS > 1){foreach(2..$SPS){$_--; if($L[$_]){$S.="$K_I";}else{$S.="$K_SP";}}}
			$SP=$space/15;
			if($SP==1){@L=(); $L[$SP]=1;}else{$L[$SP]=1;}
			if($Lg){$Line="<tt>$S$K_L</tt><>".$Line;}
			elsif($Tg){$Line="<tt>$S$K_T</tt><>".$Line;}
		}else{$Line="0<>$Line";}
		if($date){$R{$type}="$Line".$R{$type}; $RS++;}
	}else{push(@NEW,$Line); $SP=0; @L=();}
}
close(DB);
if($FORM{"mode2"} eq "Backup"){&backup_; $msg="<h3>バックアップ完了</h3>"; @lines=();}
elsif($FORM{"mode2"} =~/\d/){
	open(NO,">$c_f") || &er_("Can't write $c_f","1");
	print NO $FORM{"mode2"};
	close(NO);
	$msg="<h3>カウンタ値編集完了</h3>";
}elsif($FORM{"mode2"} eq "LockOff"){
	$msg="<h3>ロック解除完了</h3>";
	if(-e $lockf){rmdir($lockf); $msg.="($lockf解除)";}else{$msg.="($lockf無し)";}
	if(-e $cloc){rmdir($cloc);   $msg.="($cloc解除)"; }else{$msg.="($cloc無し)";}
}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$a_max);
if(-s $log){$l_size=int((-s $log)/1024);}else{$l_size=0;}
if($topok==0){$NewMsg="<li><a href=\"$cgi_f?mode=new&no=$no&pass=$FORM{'pass'}$pp\">管理用新規作成</a>\n";}
if($i_mode || $mas_c){
	if($FSize){$FSize=int($FSize/1024); $FileSize="<br>アップファイル合計サイズ：$FSize\KB";}else{$FSize=0;}
	$FP ="<form action=\"$cgi_f\" method=$met target=_blank>\n";
	$FP.="<b>[画像/記事表\示許可]</b><br><input type=hidden name=mode value=ent>$nf$pf\n";
	$FP.="<input type=hidden name=pass value=$FORM{'pass'}><input type=submit value=\"表\示許可システム\"></form>\n";
}
if($bup){$BUL="/バックアップ";}
print <<"_HTML_";
<center><table width=90\%>
<tr><td align=right colspan=2><a href="http://www.cj-c.com/help/cbbs.html" target="_blank">管理モードヘルプ</a></td></tr>
<tr><th bgcolor="$ttb" colspan=2>管理モード</th><tr><td>
現在のログのサイズ：$l_size\KB　記事数：$NS(親/$total レス/$RS)$FileSize<ul>
<li>記事を編集したい場合、その記事のタイトルをクリック。
<li>削除したい記事にチェックを入れ「削除」ボタンを押して下さい。
<li>記事Noの横のIPアドレスをクリックすると排除IPモードへ情報を送ります。
<li>ツリー削除をするとツリーが跡形も無く消えます。
<li>記事削除は、その記事に対するレスがない場合は完全削除になります。<br>
その記事に対するレスがある場合は完全に削除されず削除記事になります。
<li>削除記事は「記事完全削除」をチェックすると完全に消せます。
<li><a href=#FMT>ロック解除/ログ初期化/フリーフォーム修復/ログコンバート$BUL</a>
$NewMsg
</ul></td><td>
<form action="$cgi_f" method=$met target="_blank">$nf$pf
<input type=hidden name=mode value="Den"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[排除IP/禁止文字追加]</b><br>
<input type=submit value="排除設定追加"></form>
$FP
_HTML_
if($cou){
	open(NO,"$c_f") || &er_("Can't open $c_f");
	$cnt = <NO>;
	close(NO);
	print <<"_BUP_";
<form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value="del"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[カウンタ値編集]</b><br>
カウント数/<input type=text name=mode2 value=$cnt size=7><input type=submit value="編集"></form>
_BUP_
}
print <<"_HTML_";
</td></table>$msg</center>
<form action=\"$cgi_f\" method=$met>$nf$pf
<input type=hidden name=mode value="key"><input type=hidden name=mo value="1">
<input type=hidden name=pass value="$FORM{'pass'}"><input type=hidden name=page value="$FORM{"page"}">
<hr width="95\%"><ul>
_HTML_
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$end_data=@NEW - 1;
$page_end=$page + ($a_max - 1);
if($page_end >= $end_data){$page_end=$end_data;}
$nl=$page_end + 1;
$bl=$page - $a_max;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=del&page=$bl&pass=$FORM{'pass'}&no=$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=del&page=$nl&pass=$FORM{'pass'}&no=$no$pp\">"; $Nle="</a>";}
$Plink="ページ移動 / $Bl\&lt;\&lt\;$Ble\n";
$a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$a_max;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?page=$a&mode=del&pass=$FORM{'pass'}&no=$no$pp\">$i</a>\n";}
	$a+=$a_max;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
print"$Plink</ul>\n";
foreach ($page .. $page_end) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$delkey,$Ip) = split(/<>/,$NEW[$_]);
	($ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$Ip);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	if($ico){$ico=" [File:<a href='$i_Url\/$ico' target=_blank>$ico</a>]";}
	if($email ne ""){$name = "<a href=\"mailto:$email\">$name</a>";}
	if($d_may eq ""){$d_may= "No Title";}
	if($yobi){$yobi=" <font color=\"$IDCol\">[ID:$yobi]</font>";}
	if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
	$date=substr($date,2,19);
	print <<"_HTML_";
<ul><input type=radio name="kiji" value="$namber">ツリー削除<br><input type=checkbox name="del" value="$namber">
<a href="$cgi_f?mode=nam&pass=$FORM{'pass'}&kiji=$namber&mo=1&no=$no$pp">$d_may</a>
/ $name <small>($date)$yobi <font color=$kijino>#$namber</font>
[<a href="$cgi_f?mode=Den&pass=$FORM{"pass"}&mo=$ip" target="_blank">$ip</a>]$ico</small><br>
_HTML_
	@RES=split(/\n/,$R{$namber});
	foreach $lines(@RES) {
		($Sen,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
			$rsp,$re,$rtype,$rde,$rIp,$tim,$Se) = split(/<>/,$lines);
		($rip,$ico,$Ent,$fimg,$TXT,$rSEL,$R)=split(/:/,$rIp);
		($txt,$sel,$ryobi)=split(/\|\|/,$rSEL);
		if ($namber eq "$rtype"){
			if($rmail){$rname="<a href=\"mailto:$rmail\">$rname</a>";}
			if($rd_may eq ""){$rd_may="No Title";}
			if(length($rdm)>$t_max){$rdm=substr($rdm,0,($t_max-2));$rdm="$rdm..";}
			$rd=substr($rd,2,19); if($re){$re="$end_ok";}
			if($ico){$ico=" [File:<a href='$i_Url\/$ico' target=_blank>$ico</a>]";}
			if($ryobi){$ryobi=" <font color=\"$IDCol\">[ID:$ryobi]</font>";}
			if($Keisen){print"$Sen";}
			else{
				print "<font color=$bg>";
				$rspz=$rsp/15*$zure;
				print "." x $rspz;
				print "</font>";
			}
			print <<"_HTML_";
<input type=checkbox name="del" value="$rnam">
<a href="$cgi_f?mode=nam&pass=$FORM{'pass'}&kiji=$rnam&mo=1&no=$no$pp">$rdm</a>
/ $rname <small>($rd)$ryobi <font color=$kijino>#$rnam</font>
[<a href="$cgi_f?mode=Den&pass=$FORM{"pass"}&mo=$rip" target="_blank">$rip</a>]$ico</small> $re<br>
_HTML_
		}
	}
	print"</ul><hr width=\"90\%\">";
}
print <<"_DEL_";
<center><input type=checkbox name=kiji value=A>記事完全削除<br>
<input type=submit value=" 削 除 ">
<input type=reset value="リセット"></form>
<b>
_DEL_
if($Bl){print"$Bl＜前の$a_max件$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl次の$a_max件＞$Nle\n";}
print <<"_HTML_";
</b><br><br>$Plink
<SCRIPT language="JavaScript">
<!--
function Link(url) {
	if(confirm("本当に実行してもOKですか?\\n(実行すると内容は元に戻せません!)")){location.href=url;}
	else{location.href="#FMT";}
}
//-->
</SCRIPT>
<a name=FMT><hr width="95\%"></a>
*JavaScript を ONにしてください*
<table border=1 bordercolor=$ttb width=90\%>
<tr><td colspan=2><form action="$cgi_f" method="$met"><b>[ロックファイルの解除(削除)]</b><ul>
<input type=button value="ロック解除" onClick="Link('$cgi_f?mode=del&pass=$FORM{"pass"}&mode2=LockOff&no=$no$pp')">
<li>ロックファイルがどうしても削除されない場合に試してください。問題が無い場合はあまり使わないで下さい<ul>
_HTML_
if(-e $lockf){print"<li>メインログ($lockf):ロック中\n";}
if(-e $cloc){print"<li>カウンタログ($cloc):ロック中\n";}
print<<"_HTML_";
</ul><li>ロック中のログがあっても、ユーザが操作中の場合があります。しばらく様子を見て実行してください。
</ul></form></td></tr>
<tr valign="top"><td>
<form action="$cgi_f" method=$met>
<b>[ログフォーマット(初期化)]</b>
<ul><input type=button value="フォーマット" onClick="Link('$cgi_f?mode=s_d&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>ファイルアップ機能\がONの場合、表\示許可モードでファイルをすべて削除し行なってください!
</ul></form>
</td><td>
<form action="$cgi_f" method=$met>
<b>[フリーフォーム修復]</b>
<ul><input type=button value="修復処理" onClick="Link('$cgi_f?mode=ffs&mo=1&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>文字コード上の不具合修正します。文字化けが起きた場合は編集で修正してください。<br>
<li>念のためバックアップを取っておくことをお勧めします(v7.0未満からフリーフォームを使用\している場合)
</ul></form>
</td></tr><tr valign="top"><td>
<form action="$cgi_f" method=$met>
<b>[ログコンバート]</b>
<ul><input type=button value="I-BOARD" onClick="Link('$cgi_f?mode=ffs&mo=I-BOARD&pass=$FORM{"pass"}&no=$no$pp')"> /
<input type=button value="UPP-BOARD" onClick="Link('$cgi_f?mode=ffs&mo=UPP-BOARD&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>I-BOARDシリーズ もしくは UPP-BOARD のログを ChildTree 用にコンバートします。<br>
<li>コンバートすると元に戻すのは大変なので注意! ボタンを間違えないで!<br>
<li>記事はすべて新着記事扱いとなります。<br>
<li>コンバート対象ログ:[$log]<br>
</ul></form>
</td><td>
_HTML_
if($bup){
	if(-e $bup_f){
		$bl=(-M $bup_f); $bh=sprintf("%.1f",24*$bl); $bl=sprintf("%.2f",$bl); $bs=int((-s $bup_f)/1024);
		$bc="あり($bs\KB / $bl日(約$bh時間)前)"; $Nb=$bup-$bl; $Nh=sprintf("%.1f",$Nb*24);
	}else{$bc="無し";}
	print <<"_BUP_";
<form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value="del"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[バックアップ]</b>
<ul><input type=button value="ログを修復" onClick="Link('$cgi_f?mode=bma&pass=$FORM{"pass"}&no=$no$pp')">
/ <input type=submit value="Backup" name=mode2><br>
<li>[Backup]ボタンをクリックすると現在のログをバックアップします。
<li>バックアップ機\能\を使用している人のみ修復可能\です。<br>
<li>バックアップ$bc
<li>次のバックアップは $Nb日(約$Nh時間)後
</ul></form>
_BUP_
}
print"</td></tr></table></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [記事編集]
# -> 記事編集のフォームを出力(hen_)
#
sub hen_ {
if($KLOG){&er_("過去ログは編集不可");}
if($mo eq ""){
	if($FORM{'del'} eq ""){ &er_("登録No が未入力!"); }
	if($delkey eq ""){ &er_("削除キー が未入力!"); }
	$kiji=$FORM{'del'};
}elsif($mo==1){if($FORM{'pass'} ne "$pass"){ &er_("パスワードが違います!"); }}
open(DB,"$log");
while ($line=<DB>) {
	($namber,$d,$name,$email,$d_may,$comment,$url,
		$s,$end,$t,$de,$i,$ti,$sml) = split(/<>/,$line);
	if($d eq ""){next;}
	if($kiji eq "$namber"){
		if($mo eq ""){
			if($de eq "") { &er_("この記事は削除キーがありません!"); }
			&cryma_($de);
			if($delkey eq "$pass"){$ok="m";}
			if($ok eq "n"){ &er_("パスワードが違います!"); }
			$hen_l="$cgi_f?no=$no$pp"; $Lcom="";
		}else{$hen_l="$cgi_f?mode=del&pass=$FORM{'pass'}&no=$no$pp"; $Lcom="管理モードに";}
		if($s && $end_f && ($end_c==0||$FORM{'pass'} eq $pass) && $t){
			if($end){$C=" checked";}
			$end_form=<<"_ENDBOX_";
$end_ok BOX
<input type=checkbox name=end value="1"$C>
$end_m
_ENDBOX_
		}
		if($FORM{'pass'} eq ""){$FORM{'pass'}=$delkey;}
		&hed_("Message Edit");
		$comment =~ s/<br>/\n/g;
		if(($comment =~ /^<pre>/)&&($comment =~ /<\/pre>$/)){
			$Z=" checked";$comment=~ s/<pre>//g;$comment=~ s/<\/pre>//g;
		}else{$T=" checked";}
		if($o_mail){
			if($sml==1 || $sml==2){$Y=" selected";}
			if($sml < 2){$Pch=" selected";}
			$Mbox= <<_MAIL_;
<tr><td colspan=2>
└&gt; 関連するレス記事をメールで受信しますか?<select name=send>
<option value=0>NO
<option value=1$Y>YES
</select> /
アドレス<select name=pub>
<option value=0>非公開
<option value=1$Pch>公開
</select></td></tr>
_MAIL_
		}
		if($tag){$comment=~ s/</\&lt\;/g; $comment=~ s/>/\&gt\;/g;}
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$i);
		print <<"_HTML_";
<center><table width=90\%><tr bgcolor=$ttb><th>記事No[$namber] の編集</th></tr></table>
$msg</center>
<ul><form action="$cgi_f" method="$met">$nf$pf
□<a href="$hen_l"> $Lcom戻る</a><br><br>
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value=h_w>
<input type=hidden name=namber value=$namber><input type=hidden name=mo value=$mo>
<table>
<tr><td bgcolor=$ttb>Name</td><td>/<input type=text name="name" value="$name" size=20></td></tr>
<tr><td bgcolor=$ttb>E-Mail</td><td>/<input type=text name="email" value="$email" size=40></td></tr>
$Mbox
<tr><td bgcolor=$ttb>Title</td><td>/<input type=text name="d_may" size=40 value="$d_may"></td></tr>
<tr><td bgcolor=$ttb>URL</td><td>/<input type=text name="url" value="http://$url" size=60></td></tr>
<tr><td colspan=2 bgcolor=$ttb>Comment▽
通常モード/<input type=radio name=pre value=0$T>
図表\モード/<input type=radio name=pre value=1$Z>
(適当に改行を入れて下さい)<br>
<textarea name="comment" rows=15 cols=80 wrap=$wrap>$comment</textarea></td></tr>
_HTML_
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		if($font){
			print "<tr><td bgcolor=$ttb>文字色</td><td>/\n";
			foreach (0 .. $#fonts) {
				if($font eq ""){$font="$fonts[0]";}
				print"<input type=radio name=font value=\"";
				if($font eq "$fonts[$_]"){print"$fonts[$_]\" checked><font color=$fonts[$_]>■</font>\n";}
				else{print"$fonts[$_]\"><font color=$fonts[$_]>■</font>\n";}
			}
			print"</td></tr>";
		}
		if($hr){
			print"<tr><td bgcolor=$ttb>枠線色</td><td>/\n";
			foreach (0 .. $#hr) {
				if($hr eq ""){$cr="$hr[0]";}
				print "<input type=radio name=hr value=\"";
				if($hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=$hr[$_]>■</font>\n";}
				else{print"$hr[$_]\"><font color=$hr[$_]>■</font>\n";}
			}
			print"</td></tr>";
		}
		if($ICON ne ""){
			if($CICO){$ICO=$CICO;}
			print"<tr><td bgcolor=$ttb>Icon</td><td>/ <select name=Icon>\n";
			foreach(0 .. $#ico1) {
				if($ICO eq $ico1[$_]){print"<option value=\"$_\" selected>$ico2[$_]\n";}
				else{print"<option value=\"$_\">$ico2[$_]\n";}
			}
			print"</select> <small>(画像を選択/";
			print"<a href='$cgi_f?mode=img&no=$no$pp' target=_blank>サンプル一覧</a>)</small></td></tr>\n";
		}
		if($sel){
			print"<tr><td bgcolor=$ttb>$SEL_T</td><td>/ <select name=sel>\n";
			foreach(0 .. $#SEL) {
				if($sel eq "$SEL[$_]"){print"<option value=\"$SEL[$_]\" selected>$SEL[$_]\n";}
				else{print"<option value=\"$SEL[$_]\">$SEL[$_]\n";}
			}
			print"</select></td></tr>\n";
		}
		if($txt){
			print"<tr><td bgcolor=$ttb>$TXT_T</td><td>/\n";
			print"<input type=text name=txt value=\"$txt\" maxlength=$TXT_Mx>\n";
			print"</td></tr>";
		}
		print<<"_HTML_";
<tr><td colspan=2><br>$end_form</td></tr>
</td></tr><tr><td colspan=2 align=right><input type=submit value=" 編 集 ">
<input type=reset value=リセット></td></tr></table></form></ul><hr width="95\%">
_HTML_
		if($i_mode){
			if($ico){
				&size;
				print<<"_DEL_";
<center>
・ここからファイル削除できます。<br><br>
<table width=90\%>$Pr</table>
<form action="$cgi_f">$nf$pf
<input type=hidden name=mode value=h_w><input type=hidden name=pass value=$FORM{"pass"}>
<input type=hidden name=IMD value=$namber><input type=submit value="ファイルを削除">
</form><hr width="95\%"></center>
_DEL_
			}elsif($s==0 || ($s && $ResUp)){
				print<<"_DEL_";
<ul>
・ここからファイルアップできます。<br>
<form action="$cgi_f" method=$met enctype="multipart/form-data">$nf$pf
File / <input type=file name=ups size=60$ff>　<input type=submit value="送信">
<ul>アップ可能\拡張子=&gt;
_DEL_
				foreach (0..$#exn) {
					if($exi[$I] eq "img"){$EX="<b>$exn[$_]</b>";}else{$EX="$exn[$_]";}
					print"/$EX"; $I++;
				}
				print<<"_DEL_";
<br>
1) 太字の拡張子は画像として認識されます。<br>
2) 画像は初期状態で縮小サイズ$H2×$W2ピクセル以下で表\示されます。<br>
3) 同名ファイルがある、またはファイル名が不適切な場合、<br>
　　ファイル名が自動変更されます。<br>
4) アップ可能\ファイルサイズは1回<B>$max_fs\KB</B>(1KB=1024Bytes)までです。<br></ul>
<input type=hidden name=mode value=h_w><input type=hidden name=pass value=$FORM{"pass"}>
<input type=hidden name=UP value=$namber><input type=hidden name=UPt value=$t>
<input type=hidden name=mo value=$mo></form></ul><hr width="95\%">
_DEL_
			}
		}
		last;
	}
}
close(DB);
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [パスワード暗号化]
# -> パスワードを暗号化する(cry_)
#
sub cry_ {
$time = time;
($p1, $p2) = unpack("C2", $time);
$wk = $time / (60*60*24*7) + $p1 + $p2 - 8;
@saltset = ('a'..'z','A'..'Z','0'..'9','.','/');
$nsalt = $saltset[$wk % 64] . $saltset[$time % 64];
$epasswd = crypt($FORM{'delkey'}, $nsalt);
}
#--------------------------------------------------------------------------------------------------------------------
# [パスワード解読]
# -> パスワードを暗号化しマッチング(cryma_)
#
sub cryma_ {
if($de =~ /^\$1\$/){ $crptkey=3; }else{ $crptkey=0; }
$ok = "n";
if(crypt($FORM{'delkey'}, substr($de,$crptkey,2)) eq $de){$ok = "y";}
}
#--------------------------------------------------------------------------------------------------------------------
# [削除処理]
# -> 記事の削除処理(key_)
#
sub key_ {
if($mo eq ""){
	if($FORM{'del'} eq ""){ &er_("登録No が未入力!"); }
	if($delkey eq "") { &er_("削除キー が未入力!"); }
}elsif($mo==1){if($FORM{'pass'} ne "$pass"){ &er_("パスワードが違います!"); }}
if($locks){&lock_("$lockf");}
open(DB,"$log") || &er_("Can't open $log");
@CAS=(); $dok=0; $OYA=0; $SP="";
while ($mens=<DB>) {
	$mens =~ s/\n//g; $Pdel=0;
	($nam,$d,$na,$mail,$d_,$com,$url,
		$sp,$e,$ty,$de,$ip,$ti) = split(/<>/,$mens);
	if($d eq ""){push (@CAS,"$mens\n"); $OYA=1; next;}
	foreach $namber (@d_) {
		if ($namber eq "$nam") {
			if($mo eq ""){
				if($de eq "" && $dok==0){&er_("記事に削除キーがありません!","1");}
				&cryma_($de);
				if($delkey eq "$pass"){$ok="m";}
				if($ok eq "n" && $dok==0){&er_("パスワードが違います!","1");}
			}
			if($SP < $sp || $SP==$sp || $SP eq ""){$Pdel=1;}
			$mens=""; $dok=1;
			($I,$ico,$E,$fi,$TX,$S,$R)=split(/:/,$ip);
			if($ico && -e "$i_dir/$ico"){unlink("$i_dir/$ico");}
		}
	}
	if($kiji ne "" && ($kiji eq "$nam"||$kiji eq "$ty")){$mens = "";}
	$n="\n";
	if($mens eq "" && $kiji eq "" && $Pdel==0){
		if($mo || $ok eq "m"){$Dm="(管理者)";}else{$Dm="(投稿者)";}
		$mens = "$nam<>$d<><><>（削除）<>この記事は$Dm削除されました<><>$sp<><>$ty<><><>$ti<><>";
	}elsif($mens eq "" && ($kiji ne "" || $Pdel)){
		$mens=""; $n="";
		if($OYA==0){$mens="$nam<><><><><><><><><>$nam<><><><><>"; $n="\n";}
	}
	$OYA=1; $SP=$sp;
	push (@CAS,"$mens$n");
}
close(DB);

open (DB,">$log");
print DB @CAS;
close(DB);
if(-e $lockf){rmdir($lockf);}
if($FORM{'URL'}){&ktai("削除","$FORM{'URL'}");}
if($mo){$msg="<h3>削除完了</h3>"; &del_;}else{$mode="";}
}
#--------------------------------------------------------------------------------------------------------------------
# [編集記事置換]
# -> 編集内容を置き換える(h_w_)
#
sub h_w_ {
if($KLOG){&er_("過去ログは編集不可");}
if($FORM{'pass'} ne "$pass" && $mo){&er_("パスワードが違います!");}
if($E_[0] eq "" && $I_[0] eq ""){
	$delkey=$FORM{'pass'}; &check_;
	if($tag){
		$comment=~ s/\&lt\;/</g;
		$comment=~ s/\&gt\;/>/g;
		$comment=~ s/\&quot\;/\"/g;
		$comment=~ s/<>/\&lt\;\&gt\;/g;
	}
}
if($locks){&lock_("$lockf");}
if($FORM{"pre"}){$comment="<pre>$comment</pre>";}
@new=(); $flag=0; $SIZE=0;
open(DB,"$log");
while ($line=<DB>) {
	$line =~ s/\n//g;
	($knam,$k,$kname,$kemail,$kd_may,$kcomment,$kurl,
		$ks,$ke,$kty,$kd,$ki,$kt,$sml) = split(/<>/,$line);
	if($k eq ""){push (@new,"$line\n"); next;}
	if($namber eq "$knam") {
		if($mo eq ""){
			$de=$kd; $FORM{'delkey'}=$FORM{'pass'};
			&cryma_($epasswd);
			if($FORM{"pass"} eq $pass){$ok="m";}
			if($ok eq "n"){ &er_("パスワードが違います!","1"); }
		}
		if($EStmp){
			&time_("");
			$EditCom="$date 編集";
			if($mo || $ok eq "m"){$EditCom.="(管理者)";}else{$EditCom.="(投稿者)";}
			if($comment !~ /([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) 編集/){$EditCom.="<br><br>";}else{$EditCom.="<br>";}
			$comment=$EditCom.$comment;
		}
		($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
		($Ktxt,$Ksel,$Kyobi)=split(/\|\|/,$KS);
		if($o_mail){if($send && $FORM{'pub'}==0){$send=2;}elsif($send==0 && $FORM{'pub'}==0){$send=3;}}
		$line="$namber<>$k<>$name<>$email<>$d_may<>$comment<>$url<>$ks<>$end<>$kty<>$kd";
		$line.="<>$KI:$Kico:$E:$Kfi:$ICON|$ICO|$font|$hr|:$txt\|\|$sel\|\|$Kyobi\|\|:$KR:<>$kt<>$send<>";
		$flag = 1;
	}elsif(@E_){
		($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
		$EF=0;
		foreach $ENT (@E_){if($ENT eq $knam){$EF=1; if($E){$EE=0;}else{$EE=1;} last;}}
		if($EF){
			if($mo eq ""){
				$de=$kd; $FORM{'delkey'}=$FORM{'pass'};
				&cryma_($epasswd);
				if($ok eq "n"){ &er_("パスワードが違います!","1"); }
			}
			$line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
			$flag=1;
		}
	}elsif(@I_){
		($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
		$EF=0;
		foreach $ENT (@I_){if($ENT eq $knam){$EF=1;last;}}
		if($EF){
			if($mo eq ""){
				$de=$kd; $FORM{'delkey'}=$FORM{'pass'};
				&cryma_($epasswd);
				if($ok eq "n"){ &er_("パスワードが違います!","1"); }
			}
			if($Kico && -e "$i_dir/$Kico"){unlink("$i_dir/$Kico");}
			$Kico=""; $E=0; $Kfi="";
 			$line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$Kico:$EE:$Kfi:$KTX:$KS:$KR:<>$kt<>$sml<>";
			$flag=1;
		}
	}elsif($FORM{'UP'}){
		$UPt=$FORM{'UPt'}; $UP=$FORM{'UP'};
		($KI,$Kico,$E,$Kfi,$KTX,$KS,$KR)=split(/:/,$ki);
		if($UPt){if($UPt eq $kty && $Kico){$SIZE+= -s "$i_dir/$Kico";}}
		else{if($UP eq $kty && $Kico){$SIZE+= -s "$i_dir/$Kico";}}
		if($UP eq $knam){
			if($mo eq ""){
				$de=$kd; $FORM{'delkey'}=$FORM{'pass'};
				&cryma_($epasswd);
				if($ok eq "n"){ &er_("パスワードが違います!","1"); }
			}
 			if($mas_c){$E=0;}else{$E=1;}
			$SIZE+=-s "$i_dir/$file";
			$line="$knam<>$k<>$kname<>$kemail<>$kd_may<>$kcomment<>$kurl<>$ks<>$ke<>$kty<>$kd<>$KI:$file:$E:$TL:$KTX:$KS:$KR:<>$kt<>$sml<>";
			$flag=1;
		}
	}
	push(@new,"$line\n");
}
close(DB);
if($SIZE && $max_or < int($SIZE/1024)){&er_("このファイルは総ファイルサイズを超えるためアップできません!","1");}
if($flag==0){&er_("その記事Noは存在しません!","1");}
if($flag==1){
	open (DB,">$log");
	print DB @new;
	close(DB);
}
if(-e $lockf){rmdir($lockf);}
if($FORM{'URL'}){&ktai("編集","$FORM{'URL'}");}
if(@E_ || @I_ || $FORM{'UP'}){
	if($mo && (@E_ || @I_)){&ent_;}
	else{
		if(@I_){$msg="<h3>ファイル削除</h3>"; $FORM{"del"}=$I_[0];}
		elsif($FORM{'UP'}){$msg="<h3>ファイルアップ完了</h3>$Henko"; if($mo){$kiji=$FORM{'UP'};}else{$FORM{"del"}=$FORM{'UP'};}}
		$delkey=$FORM{"pass"}; &hen_;
	}
}elsif($mo){$msg="<h3>編集完了</h3>"; &del_;}
else{$msg="<h3>以下のように編集完了</h3>"; $delkey=$FORM{"pass"}; $FORM{"del"}=$namber; &hen_;}
}
#--------------------------------------------------------------------------------------------------------------------
# [排除IP/禁止文字追加]
# -> 排除IP/禁止文字追加システム(Den_)
#
sub Den_ {
if($FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}
($m,$Log)=split(/:/,$FORM{"m"});
if($m eq "Make"){
	open(DB,">$Log") || &er_("Can't make $Log");
	print DB "";
	close(DB);
	chmod(0666,"$Log");
}elsif($m eq "Add"){
	$FORM{'u'}=~ s/\&lt\;/</g; $FORM{'u'}=~ s/\&gt\;/>/g;
	open(OUT,">>$Log");
	print OUT "$FORM{'u'}\n";
	close(OUT);
	$msd="<h3>$Logへ登録完了</h3>";
}elsif($m eq "Del"){
	open(DB,"$Log");
	@deny = <DB>;
	close(DB);
	@NEW = ();$F=0;
	foreach $b (@deny) {
		$b =~ s/\n//g;
		foreach $u (@d_) {if($u eq "$b"){$F=1; last;}}
		if($F){$F=0; next;}
		push(@NEW,"$b\n");
	}
	open (DB,">$Log");
	print DB @NEW;
	close(DB);
	$msd="<h3>$Log内削除完了</h3>";
}
&hed_("Deny IP/Word Editor");
print<<"_HTML_";
<center><table width=95\%><tr bgcolor="$ttb"><th>排除IP/禁止文字列設定モード</th></tr></table>$msd</center><ul>
<li>指定した物が含まれているとそれぞれ排除されます。
<li><b>[排除IP?]</b> IPアドレスは4桁で構\成されており、通常4桁目がアクセス毎に変わります。よって、3桁目までを指定します。<br>
例) 127.0.0.1 を排除したい場合は 127.0.0. と指定する。192.168.0.1 → 192.168.0. (*)自分のIPは絶対に設定しない!
<li><b>[禁止文字列?]</b> 使用されたくない文字列を指定します。大文字小文字は区別されます。<br>
例) 宣伝記事→URLを指定。タグ→開始タグの一部 &lt;img &lt;font 等。
_HTML_
@Deny=("$IpFile","$NWFile");
@Dcom=("排除IP","禁止文字列");
foreach(0..1){
	if($mo){if($_==0){$mo=~ s/(\d+\.\d+\.\d+\.)(\d+)/$1/;}else{$mo="";}}
	if(-e "$Deny[$_]"){
		open(DB,"$Deny[$_]") || &er_("Can't open $Deny[$_]");
		@deny = <DB>;
		close(DB);
		print<<"_EDIT_";
<hr><b>■ $Dcom[$_]の追加</b><ul>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Add:$Deny[$_]">
$Dcom[$_] /<input type=text name=u size=25 value="$mo"> (例/cj-c.com)
<input type=submit value="追 加">
</form></ul>
<b>■ $Deny[$_] に登録済みの$Dcom[$_]</b><ul>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Del:$Deny[$_]">
_EDIT_
		foreach(0..$#deny){
			$deny[$_]=~ s/\n//g; $deny[$_]=~ s/</\&lt\;/g; $deny[$_]=~ s/>/\&gt\;/g;
			print"<input type=checkbox name=del value=\"$deny[$_]\">- $deny[$_]<br>\n";
		}
		print"<br><input type=submit value=\"削 除\"><input type=reset value=\"リセット\"></form></ul>\n";
	}else{
		print<<"_EDIT_";
<hr><br><b>■ $Dcom[$_]設定をするファイルの作成</b><ul>
<li>$Dcom[$_]を設定するファイル($Deny[$_])がないのでオンラインで設定する場合、このファイルを作成する必要があります。
<li>このCGIのあるディレクトリに作成します(このディレクトリのパーミッションが777or755 である必要があります)。
<li>ここでうまく作成できない場合は同名ファイルをFTPから作成してください(パーミッション:666)
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Make:$Deny[$_]">
<input type=submit value="$Deny[$_] を作成する"></ul>
</form>
_EDIT_
	}
}
print"</ul><hr width=\"95\%\">\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ロック処理]
# -> ファイルロック処理(lock_)
#
sub lock_ {
$lflag = 0;
foreach(1 .. 5){if(mkdir($_[0], 0755)){$lflag=1; last;}else{sleep(1);}}
if($lflag==0){
	if(-e $_[0]){rmdir($_[0]);}
	&er_("LOCK is BUSY (ロック中)","1");
}
}
#--------------------------------------------------------------------------------------------------------------------
# [メール通知処理]
# -> 投稿通知メール処理(mail_)
sub mail_ {
$mail_subj = "$title 投稿通知";
if($type != 0 && $type ne ""){$types="($type\RES)";}
if($email eq ""){$email='nomail@xxx.xxx';}
if($url ne "")  {$url  ="URL  : http://$url\n";}
if($d_may eq ""){$d_may="No Title";}
if($sel){$Selm="$SEL_T : $sel\n";}else{$Selm="";}
if($txt){$Txtm="$TXT_T : $txt\n";}else{$Txtm="";}
$Mail_Msg=<<"_MAIL_";
$mail_subj
--Comment------------------------------
Title: $d_may $types
Name : $name ($email)
Time : $date
$url
$comment
$Selm$Txtm
----------------------------------END--
_MAIL_
$Mail_Msg=~ s/<br>/\n/g;
$Mail_Msg=~ s/\&lt\;/</g;
$Mail_Msg=~ s/\&gt\;/>/g;
$Mail_Msg=~ s/\&quot\;/\"/g;
$Mail_Msg=~ s/\&amp\;/&/g;
if($t_mail){
	if($mymail){if($SeMail !~ /$mailto/){$SeMail="$mailto"."$SeMail";}}
	else{if(($email ne $mailto) && ($SeMail !~ /$mailto/)){$SeMail="$mailto"."$SeMail";}}
}
if($SeMail =~ /^\,|^ /){$SeMail=substr($SeMail,1);}
&jcode'convert(*mail_subj,'jis');
&jcode'convert(*Mail_Msg,'jis');

if($SeMail){
	if (open(MAIL,"| $s_mail $SeMail")) {
	print MAIL "X-Mailer: CBBS MAILER\n";
	print MAIL "To: $mailto\n";
	print MAIL "From: $email\n";
	print MAIL "Subject: $mail_subj\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=ISO-2022-JP\n";
	print MAIL "Content-Transfer-Encoding: 7bit\n";
	print MAIL "\n\n";
	print MAIL "$Mail_Msg\n";
	close(MAIL);
	}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [URLをリンク等]
# -> コメント内、リンク・文字色など処理(auto_)
#
sub auto_ {
if($_[0]=~/<\/pre>/){$_[0]=~ s/(>|\n)((&gt;|＞|>)[^\n]*)/$1<font color=$res_f>$2<\/font>/g;}
else{$_[0]=~ s/>((&gt;|＞|>)[^<]*)/><font color=$res_f>$1<\/font>/g;}
$_[0]=~ s/([^=^\"]|^)((http|ftp|https)\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+)/$1<a href=$2 target=$TGT>$2<\/a>/g;
$_[0]=~ s/([^\w^\.^\~^\-^\/^\?^\&^\+^\=^\:^\%^\;^\#^\,^\|]+)(No|NO|no|No.|NO.|no.|&gt;&gt;|＞＞|>>)([0-9\,\-]+)/$1<a href=\"$cgi_f?mode=red&namber=$3&no=$no$pp\" target=$TGT>$2$3<\/a>/g;
}
#--------------------------------------------------------------------------------------------------------------------
# [カウンタ処理]
# -> カウントアップ処理(con_)
#
sub con_ {
if($mode eq "" || $mode eq "alk"){
	if($locks){&lock_("$cloc");}
	open(NO,"$c_f") || &er_("Can't open $c_f","1");
	$cnt = <NO>;
	close(NO);
	if($FORM{'mode'} eq "" && $FORM{'page'} eq "" && $ENV{'HTTP_REFERER'} !~ /$cgi_f/) {
		$cnt++;
		open(NO,">$c_f") || &er_("Can't write $c_f","1");
		print NO $cnt;
		close(NO);
	}
	if(-e $cloc){rmdir($cloc);}
	while(length($cnt) < $fig){$cnt="0".$cnt;}
	@cnts = split(//,$cnt);
	if($m_pas){foreach(0..$#cnts){print"<img src=\"$m_pas/$cnts[$_]\.gif\" width=$m_wid height=$m_hei>";}}
	else{print "<font color=$c_co face=\"Times New Roman\">$cnt</font>";}
	print"<br><br>\n";
}
}
#--------------------------------------------------------------------------------------------------------------------
# [エラー表示]
# -> エラーの内容を表示する(er_)
#
sub er_ {
if(-e $lockf && $_[1]==1){rmdir($lockf);}
if(-e $cloc && $_[1]==1){rmdir($cloc);}
if(-e "$i_dir/$file"){unlink("$i_dir/$file");}
if($FORM{"URL"}){
	($KURL,$Ag) = split(/::/,$FORM{'URL'});
	&ktai("ERROR-$_[0]<br>未","$KURL");
}
if($BG eq ""){&hed_("Error");}
print"<hr width=\"90\%\"><center>ERROR-$_[0]</center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [過去ログ]
# -> 過去ログへの書き込み(log_)
#
sub log_ {
open(NO,"$klog_c") || &er_("Can't open $klog_c");
$n = <NO>;
close(NO);

$klog_f = "$klog_d\/$n\.txt";
unless(-e $klog_f){ &l_m($klog_f);}

$klog_size=$klog_l*1024;
if(-s $klog_f > $klog_size) {&log_up;}

open(LOG,">>$klog_f") || &er_("Can't write $klog_f");
print LOG @KLOG;
close(LOG);
}
#--------------------------------------------------------------------------------------------------------------------
# [カウントアップ]
# -> 過去ログ番号のカウントアップ(log_up)
#
sub log_up {
$n++;

open(NUM,">$klog_c") || &er_("Can't write $klog_c");
print NUM "$n";
close(NUM);

$klog_f="$klog_d\/$n\.txt";
&l_m($klog_f);
}
#--------------------------------------------------------------------------------------------------------------------
# [ログ生成]
# -> ログを自動生成します(l_m)
#
sub l_m {
open(DB,">$_[0]") || &er_("Can't make $_[0]");
print DB "";
close(DB);

chmod(0666,"$_[0]");
}
#--------------------------------------------------------------------------------------------------------------------
# [バックアップ処理]
# -> 簡易バックアップ処理(backup_)
#
sub backup_{
unless(-e $bup_f){&l_m($bup_f);}
if(-M "$bup_f" > $bup || $FORM{"mode2"} eq "Backup"){
	open(LOG,">$bup_f") || &er_("Can't write $bup_f");
	print LOG @lines;
	close(LOG);
}
}
#--------------------------------------------------------------------------------------------------------------------
# [修復処理]
# -> バックアップファイルリネーム処理(bma_)
#
sub bma_ {
if($FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}
if(-e $lockf){rmdir($lockf);}
if(-e $bup_f){rename ($bup_f,$log) || &er_("Rename Error");}
else{&er_("バックアップがないので修復不可能\です!","1");}
$msg="<h3>修復完了</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [スレッド表示]
# -> スレッド形式で記事の一覧を表示する(alk_)
#
sub alk_ {
if($FORM{'page'} eq ''){$page = 0;}else{$page=$FORM{'page'};}
@NEW=(); @RES=(); $List=""; $news=""; $On=1; %N=(); %d=(); %n=(); $RS=0; $K=1;
open(LOG,"$log") || &er_("Can't open $log");
while (<LOG>) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
	if($type){
		if($On){if(($time_k-$tim)>$new_t*3600){$n{$type}="$hed_i";}else{$n{$type}="$up_i_"; $On=0;}}
		$tim=sprintf("%011d",$tim); if($date){$R{$type}.="$tim<>$_";} $N{$type}++; $RS++;
	}else{
		if($n{$namber} eq ""){if(($time_k-$tim)>$new_t*3600){$n{$namber}="$hed_i";}else{$n{$namber}="$new_i";}}
		if($tim eq ""){$tim="$TIM";} $tim=sprintf("%011d",$tim);
		if($Res_T==2){$tim=$N{$namber}; $tim=sprintf("%05d",$tim);}
		push(@NEW,"$tim<>$_");
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		if($txt){$Txt="$TXT_T:[$txt]　";}else{$Txt="";}
		if($sel){$Sel="$SEL_T:[$sel]　";}else{$Sel="";}
		if($d_may eq ""){$d{$namber}="無題";}else{$d{$namber}=$d_may;}
		if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d{$namber}="$Txt$Sel/"."$d{$namber}";}}
		if($N{$namber} eq ""){$N{$namber}=0;}
		if($Top_t && $Res_T==0 && $Rno < $LiMax){
			$Rno++; $PAH=$alk_su*$K; if(($PAH) < $Rno){$PAL="&page=$PAH"; $K++;} $L_3=$Rno-1;
			if(($page+$alk_su)>=$Rno && ($page)<$Rno){$List.="<a href=\"#$L_3\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
			else{$List.="<a href=\"$cgi_f?mode=res&namber=$namber&page=&no=$no$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
		}
		$news=""; $On=1;
	}
	$TIM=$tim;
}
close(LOG);

$PAGE=$page/$alk_su;
&hed_("All Thread / Page: $PAGE");
if($Res_T){
	@NEW=sort(@NEW); @NEW=reverse(@NEW);
	if($Top_t){
		foreach (0..$#NEW){
			if($Rno > $LiMax){last;}
			($T,$namber,$date,$name,$email,$d_may,$comment,$url,
				$space,$end,$type,$del,$ip,$tim) = split(/<>/,$NEW[$_]);
			$Rno++; $PAH=$alk_su*$K; if(($PAH) < $Rno){$PAL="&page=$PAH"; $K++;} $L_3=$Rno-1;
			if(($page+$alk_su)>=$Rno && ($page)<$Rno){$List.="<a href=\"#$L_3\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
			else{$List.="<a href=\"$cgi_f?mode=res&namber=$namber&page=&no=$no$pp\">$n{$namber}$d{$namber}($N{$namber})</a> |\n";}
		}
	}
}
if($Top_t){
	$com_top.="■ $new_t時間以内に作成されたスレッドは $new_i で表\示されます。<br>\n";
	$com_top.="■ $new_t時間以内に更新されたスレッドは $up_i_ で表\示されます。<br>\n";
}
print"<center><table cellspacing=0 cellpadding=0><tr><td>\n";
print"$com_top</td></tr></table>$Henko<hr width=\"95\%\">";
if($i_mode){&minf_("N");}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$alk_su);
$end_data=@NEW-1;
$page_end=$page+($alk_su-1);
if($page_end >= $end_data){$page_end = $end_data;}
$Pg=$page+1; $Pg2=$page_end+1;
$nl=$page_end+1;
$bl=$page-$alk_su;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=alk&page=$bl&no=$no$pp$Wf\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=alk&page=$nl&no=$no$pp$Wf\">"; $Nle="</a>";}
print"</center><a name=list></a><ul>[ 全$totalスレッド($Pg-$Pg2 表\示) ]　\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n";
$a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$alk_su;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=alk&page=$a&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$alk_su;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?mode=alk&W=W&no=$no$pp\">更新順</a>"; $OJ2="投稿順"; $OJ3="<a href=\"$cgi_f?mode=alk&W=R&no=$no$pp\">レス数</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?mode=alk&W=W&no=$no$pp\">更新順</a>"; $OJ2="<a href=\"$cgi_f?mode=alk&W=T&no=$no$pp\">投稿順</a>"; $OJ3="レス数";}
else{$OJ1="更新順"; $OJ2="<a href=\"$cgi_f?mode=alk&W=T&no=$no$pp\">投稿順</a>"; $OJ3="<a href=\"$cgi_f?mode=alk&W=R&no=$no$pp\">レス数</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ]←ソ\ート方法変更</ul><center>";
if($Top_t){
	print"<table width=\"95\%\" border=1 bordercolor=\"$ttb\"><tr>\n";
	print"<td bgcolor=\"$k_back\"><center><b>記事リスト</b> ( )内の数字はレス数</center>$List</td></tr></table><br>\n";
}
$LinkNo="";
foreach ($page .. $page_end) {
	($T,$nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$NEW[$_]);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
		$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,"","TR");
	print"<hr width=\"95\%\"><br><a name=\"$_\"></a><table width=\"95\%\" bgcolor=\"$k_back\"><tr><td align=right>\n";
	if($Top_t){print"<a href=\"#list\">■記事リスト</a>";}
	if($_ ne $page_end){$L_=$_+1; print" / <a href=\"#$L_\">▼下のスレッド</a>\n";}
	if($_ ne $page){$L_2=$_-1; print" / <a href=\"#$L_2\">▲上のスレッド</a>\n";}
	print"$HTML";
	@RES=split(/\n/,$R{$nam}); $PNO=0;
	@RES=sort(@RES);
	if(@RES){
		$Rn=$alk_rm; $RC=@RES; $Pg=$RC-$alk_rm+1; if($Pg<=0){$Pg=1;}
		print"<hr size=1 color=\"$ttb\">▽[全レス$RC件(ResNo.$Pg-$RC 表\示)]\n";
		$RC_=int($RC/$ResHy);
		$res=0; $Dk=0; $ResNo=$Pg-1; $PgSt=$Pg-1; $PgEd=$RC-1;
		foreach ($PgSt..$PgEd) {
			($T,$rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,
				$rsp,$re,$rtype,$del,$rip,$rtim,$Se)=split(/<>/,$RES[$_]);
			if($nam eq "$rtype"){
				$ResNo++;
				($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$rip);
				($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
				($txt,$sel,$yobi)=split(/\|\|/,$SEL);
				$PNO=int($ResNo/$ResHy)*$ResHy;
				&design($rnam,$rd,$rname,$rmail,$rdm,$rcom,$rurl,$rsp,$re,$rtype,$del,$Ip,$rtim,$ico,
					$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,"TR");
				print"$HTML";
			}
			if($ResNo==$N{$nam}){last;}
		}
		if($RC){
			if($Top_t){print"<hr size=1 color=\"$ttb\"><a href=\"#list\">■記事リスト</a> /\n";}
			print"レス記事表\示 →\n";
			$a=0;
			for($i=0;$i<=$RC_;$i++){
				if($i){$St=$i*$ResHy; $En=$St+$ResHy-1; if($RC+1<=$En){$En=$RC;}}
				else{$En=$ResHy-1; if($RC<$En){$En=$RC;} $St="親記事";}
				print"[<a href=\"$cgi_f?mode=res&namber=$nam&rev=$r&page=$a&no=$no$pp\">$St-$En</a>]\n";
				$a+=$ResHy;
			}
			if($Dk){print"<br>($Dk件は削除記事)\n";}
		}
	}
	$LinkNo=$nam;
	print"</td></tr></table><br>\n";
}
print"</center><br><hr width=\"95\%\">";
&allfooter("スレッド$alk_su件");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [スレッドレス表示]
# -> スレッドのレスを表示します(res_)
#
sub res_ {
if($space eq ""){$space=0;}
$SP=$space+15;
@TOP=(); $k=0; $Dk=0; $On=0; $En=0; $O2=0; $TitleHed="";
open(DB,"$log");
while (<DB>) {
	($nam,$da,$na,$mail,$d_may,$co,$ur,
		$sp,$end,$ty,$de,$ip,$time)=split(/<>/,$_);
	if(($ty==0 && $FORM{"namber"} eq "$nam")||($ty != 0 && $FORM{"namber"} eq $ty)){
		if($space < $sp && $On==0 && $O2==0){$N_NUM=$nam; $On=1;}
		if($space eq $sp && $O2==0 && $mo ne $nam){$On=0; $N_NUM="";}
		if($time){
			$time=sprintf("%011d",$time);
			push(@TOP,"$time<>$_"); if($end){$En=1;}
		}else{$Dk++;}
		$namb=$nam; $k++; $TitleHed=$d_may;
		if($mo){if($mo eq $nam){$On=1; $O2=1; &comin_;}}else{if($k==1){$On=1; $O2=1; &comin_;}}
	}else{if($k && $time=~/[\d]+/){last;}}
}
close(DB);

@TOP=sort(@TOP);
$total=@TOP-1;
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$PAGE=$page/$ResHy;
&hed_("One Thread Res View / $TitleHed / Page: $PAGE","1");
$page_=int($total/$ResHy);
$end_data=@TOP-1;
$page_end=$page+($ResHy-1);
if($page_end >= $end_data){$page_end=$end_data;}
if($page){$Pg="$page"; $Pg2="$page_end";}else{$Pg="親記事"; $Pg2="$page_end";}
$nl=$page_end+1;
$bl=$page-$ResHy;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=res&namber=$FORM{'namber'}&page=$bl&no=$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=res&namber=$FORM{'namber'}&page=$nl&no=$no$pp\">"; $Nle="</a>";}
print"<ul>[ スレッド内全$totalレス($Pg-$Pg2 表\示) ]　\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n";
$a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$ResHy;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=res&namber=$FORM{'namber'}&page=$a&no=$no$pp\">$i</a>\n";}
	$a+=$ResHy;
}
$Plink.="$Nl&gt;&gt;$Nle\n";
print"$Plink<br>";
if($Dk){print"( $Dk件の削除記事を非表\示 )<br>";}
print"</ul><center>\n";
$i=0; $ToNo=$page; $SIZE=0;
foreach ($page .. $page_end) {
	($T,$nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se) = split(/<>/,$TOP[$_]);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
		$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,$ToNo,"TRES");
	print "$HTML";
	$ToNo++;
}
if($TrON){$TrLink="<a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&no=$no$pp\">$all_i このスレッドをツリーで一括表\示</a>";}
print"</center><ul>$TrLink</ul><center><hr width=\"90\%\"><b>\n";
if($bl >= 0){print"$Bl＜前のレス$ResHy件$Ble\n";}
if($page_end ne $end_data){if($Bl){print"| ";} print"$Nl次のレス$ResHy件＞$Nle\n";}
if($mo eq ""){$com="";}
print<<"_F_";
</b><br><br>スレッド内ページ移動 / $Plink<br><br>
<a name=F><table width=90\% align=center>
<tr><th bgcolor=$ttb>このスレッドに書きこむ</th></tr></table></a></center>
_F_
if($r_max && $total > $r_max){
	print"<center><h3>レス数の限度を超えたのでレスできません。</h3>(レス数限度:$r_max 現在のレス数:$total)\n";
	print" → <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[スレッドの新規作成]</a></b></center>";
}
else{if($En && $end_e){print"<center><h3>$end_ok / 返信不可</h3></center>";}else{&forms_("N");}}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [ランキング]
# -> 発言ランキングをカウントする(rank)
sub rank {
$flag=0; @N=(); $T=time; $Wri=0;
open(IN,"$RLOG") || &er_("$RLOG","1");
while ($R=<IN>) {
	($Na,$Co,$Em,$Time)=split(/<>/,$R);
	if($Na eq "$name"){$flag=1; $Co++; $R="$Na<>$Co<><>$T<>\n"; $RCo=$Co;}
	if(($T-$Time) > $RDEL*86400){$R=""; $Wri=1;}
	push(@N,$R);
}
close(IN);
if ($flag || $Wri) {
	open(OUT,">$RLOG") || &er_("Can't open $RLOG","1");
	print OUT @N;
	close(OUT);
}
if ($flag==0) {
	open(OUT,">>$RLOG") || &er_("Can't write $RLOG","1");
	print OUT "$name<>1<><>$T<>\n";
	close(OUT);
	$RCo=1;
}
if(@RLv){
	foreach(0..$#RLv){
		$SPL=$RSPL*($_+1);
		if($_!=$#RLv){if($RCo < $SPL){$R="$RLv[$_]($RCo回)"; last;}}
		else{$R="$RLv[$_]($RCo回)"; last;}
	}
}else{$R="$RCo回";}
}
#--------------------------------------------------------------------------------------------------------------------
# [ランク表示]
# -> 発言ランキングを表示します(ran_)
#
sub ran_ {
@R=(); $Mas="";
open(R,"$RLOG") || &er_("Can't open $RLOG");
while (<R>) {
	($Na,$Co,$Em,$Ti)=split(/<>/,$_);
	if(@d_){
		if($FORM{'pass'} ne $pass){&er_("パスワードが違います!");}
		foreach $D (@d_){if($D eq $Na){$_=""; last;}}
		if($_ eq ""){next;}else{push(@R,"$_");}
	}
	$N=0;
	if(@NoRank){foreach(0..$#NoRank){if($Na eq "$NoRank[$_]"){$N=1; last;}}}
	if($N){$Mas.="$Na -&gt\; $Co回<br>\n"; next;}
	&time_($Ti);
	$total+= $Co;
	$Co{$Na} = $Co;
	$Date{$Na}=$date;
}
close(R);

if(@R){
	open(OUT,">$RLOG") || &er_("Can't write $RLOG");
	print OUT @R;
	close(OUT);
}
&hed_("Rank");
print <<"_T_";
<center><table width=90\%><tr bgcolor=$ttb><th>発言ランキング</th></tr></table></center>
<ul>・集計発言数:$total回
<br>・最終発言日から$RDEL日経過すると自動的に削除されます。</ul><center>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=ran>$nf$pf
<table><tr><td>
<table><tr><th colspan=6>BEST 10</th></tr><tr bgcolor=$ttb>
<th>順位</th><th>名前</th><th>発言回数</th><th>最終発言日</th><th>グラフ</th><th>*</th></tr>
_T_
$J=0; $rank1=0; $rank2=1; $count_tmp=0; $K=0;
foreach (sort { ($Co{$b} <=> $Co{$a}) || ($a cmp $b)} keys(%Co)) {
	($Co{$_} == $count_tmp) || ($rank1 = $rank2);
	$P{$_}=($Co{$_} / $total) * 100;
	$P{$_}=sprintf("%2.1f",$P{$_});
	if($rank1 > 10 && $J==0){
		$J=1;
		print"<tr><td align=center colspan=6><br><b>11位～$RBEST位</b></td></tr><tr bgcolor=$ttb>\n";
		print"<th>順位</th><th>名前</th><th>発言回数</th><th>最終発言日</th><th>グラフ</th><th>*</th></tr>";
	}
	if($J && $rank1 > $RBEST){last;}
	if($rank1==1){$G=$P{$_};$G{$_}=50;}else{$G{$_}=int(($P{$_}*50)/$G);}
	print"<tr bgcolor=$k_back><th>$rank1</th><td><b>$_</b>";
	if(@RLv){ $i=0;
		foreach $RLv (@RLv){
			$SPL=$RSPL*($i+1);
			if($i!=$#RLv){if($Co{$_} < $SPL){print" -($RLv[$i])"; last;}}
			else{print" -($RLv[$i])"; last;}
			$i++;
		}
	}
	print"</td><th>$Co{$_}</th><td align=center>$Date{$_}</td><td><small>";
	if($RGimg){$G{$_}=$G{$_}*3; print"<img src=\"$RGimg\" width=$G{$_} height=$RGhei>";}
	else{print "l" x $G{$_};}
	print" $P{$_}\%</small></td><th><input type=checkbox name=del value=\"$_\"></th></tr>\n";
	$count_tmp=$Co{$_}; $rank2++;
}
if($Mas){print"<tr><td colspan=6><br>ちなみに… $Mas</td></tr>\n";}
print"</table><br>*マーク削除/Pass<input type=password name=pass size=8> <input type=submit value=\"管理用\">\n";
print"</td><td valign=\"top\">\n";
if(@RLv){
	print"<table><tr bgcolor=$ttb><th>レベル</th><th>発言回数</th></tr>\n";
	foreach(0..$#RLv){
		$SPL=$RSPL*$_;
		if($_!=$#RLv){$SPL2="～".($RSPL*($_+1)-1)."回";}else{$SPL2="回以上";}
		print"<tr align=center bgcolor=\"$k_back\"><td>$RLv[$_]</td><td>$SPL$SPL2</td></tr>\n";
	}
	print"</table>\n";
}
print"</td></tr></table></form></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [画像幅取得]
# -> ファイルが画像の場合、ファイルを読み込んで幅を取得します。それ以外のアイコン表示もおこないます(size)
# -> とほほのラウンジを参考にさせていただきました => http://tohoho.wakusei.ne.jp/
#
sub size {
if($Ent==0 && $fimg){$fimg=$no_ent; $A=0;}
if($_[0]){$FORM{"min"}=2;}else{if($CookOn eq ""){&get_("M"); $CookOn=1;}}
$A=0; $I=0;
if($fimg eq "img" && $FORM{'min'}==0){
	$Cg=1; $Wn=$W2; $Hn=$H2; $IW=0; $IH=0;
	if($ico=~/.gif$/i){ #GIF
		open(GIF,"$i_dir/$ico");
		binmode(GIF);
		seek(GIF,6,0);
		read(GIF,$size,4);
		close(GIF);
		($IW,$IH)=unpack("vv",$size);
	}elsif($ico=~/.png$/i){ #PNG
		open(PNG,"$i_dir/$ico");
		binmode(PNG);
		seek(PNG,16,0);
		read(PNG,$Pw,4);
		read(PNG,$Ph,4);
		close(PNG);
		$PW=unpack("H*",$Pw);$IW=hex($PW);
		$PH=unpack("H*",$Ph);$IH=hex($PH);
	}elsif($ico=~/.jpg$|.jpeg$/i){ #JPEG
		open(JPG,"$i_dir/$ico");
		binmode(JPG);
		read(JPG,$Top,2);
		while (JPG) {
			read(JPG,$Top,4);
			($mark,$Cell,$Lar)=unpack("aan",$Top);
			if($mark ne "\xFF"){$IW=0; $IH=0; last;}
			elsif((ord($Cell) >= 0xC0) && (ord($Cell) <= 0xC3)){
				read(JPG,$Top,5); ($IH, $IW)=unpack("xn2",$Top); last;
			}else{read(JPG,$Top,($Lar-2));}
		}
		close(JPG);
	}elsif($ico=~/.bmp$/i){ #BMP
		open(BMP,"$i_dir/$ico");
		binmode(BMP);
		seek(BMP,18,0);
		read(BMP,$size,8);
		close(BMP);
		($IW,$IH)=unpack("V2",$size);
	}
	if($IW && $IH){
		if($IW > $Wn){$IK=$Wn*$IH;$kH=int($IK/$IW);$kW=$Wn;$Cg=0;}
		if($Cg && $IH > $Hn){$IK=$Hn*$IW;$kW=int($IK/$IH);$kH=$Hn;$Cg=0;}
		elsif($Cg==0 && $kH > $Hn){$IK=$Hn*$kW;$kW=int($IK/$kH);$kH=$Hn;}
		$Pr.="<small>$IW×$IH";
		if($Cg){$kW=$IW;$kH=$IH;}
		else{$Pr.=" =\&gt\; $kW×$kH";}
		$Pr.="</small><br>\n";
	}else{$kW=$W2;$kH=$H2;}
}
if($FORM{'min'}==1){$HW="";}elsif($FORM{'min'}==2){$I=1;}else{$HW=" width=$kW height=$kH";}
if(-s "$i_dir/$ico"){$Size= -s "$i_dir/$ico";}else{$Size=0;}
$KB=int($Size/1024); if($KB==0){$KB=1;}
if($Size){
	if($Size && $_[0] && $fimg ne $no_ent){$Alt=" alt=\"$ico/$KB\KB\"";}else{$Alt="";}
	if($fimg eq $no_ent){$A=0;}
	elsif($fimg eq "img"){
		if($I){$Pr.="<a href=\"$i_Url/$ico\" target=_blank><img src='$i_Url/$i_ico' border=0$Alt>"; $A=1;}
		else{$Pr.="<a href=\"$i_Url/$ico\" target=_blank><img src='$i_Url/$ico' border=1$HW$Alt>"; $A=1;}
	}else{$Pr.="<a href=\"$i_Url/$ico\" target=_blank>";$A=1;}
	if($img_h eq "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" border=0$Alt>";}
	elsif($img_h ne "" && $fimg ne img){$Pr.="<img src=\"$i_Url/$fimg\" height=$img_h width=$img_w border=0$Alt>";}
	$AEND="";
	if($_[0] eq ""){
		if($A){$AEND="$ico</a>/";}
		$Pr="$Pr"."<br>$AEND<small>$KB\KB</small>\n";
	}else{if($A){$AEND="</a>";} $Pr.="$AEND\n";}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [許可システム]
# -> アップファイル/記事の表示許可を与えます(ent_)
#
sub ent_ {
if($FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}
&hed_("Permit");
print <<"_ENT_";
<center><table width=90\%><tr><th bgcolor=$ttb>ファイル/記事表\示許可</th></tr></table><br></center>
<ul><ul><table><tr><td>
<li><a href="$cgi_f?no=$no$pp"> 掲示板に戻る</a> / <a href="$cgi_f?mode=del&pass=$FORM{"pass"}&no=$no$pp">通常管理モード</a>
<li> 許可する/未許可にするファイルをチェックし、ボタンを押して下さい。
<li> ファイル削除をチェックしてボタンを押すとファイルのみを削除できます。
<li> 記事のみの表\示許可は一度許可済みにすると、未許可に戻せません!
</td><td><form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value=ent><input type=hidden name=pass value=$FORM{"pass"}>
<select name=check>
<option value=1>全未許可記事チェック
<option value=2>全許可済記事チェック
<option value=0>チェックをはずす
<input type=submit value="実行"></form></td></tr></table>
</ul></ul><center>
<form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value=h_w><input type=hidden name=mo value=1>
<input type=hidden name=pass value=$FORM{"pass"}>
_ENT_
$i=0; $k=0;
open(LOG,"$log") || &er_("Can't open $log");
while ($line=<LOG>) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$line);
	if($date eq ""){next;}
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	if($ico || ($Ent==0 && $mas_c==2)){
		if($i==0){
			print"<table bordercolor=$ttb width=\"95\%\"><tr bgcolor=$ttb>";
			print"<th>許可チェック</th><th>投稿者情報</th><th>コメント</th><th>ファイル情報</th><th>ファイル削除</th></tr>\n";
		}
		$check="";	
		if($Ent){$eok="○"; if($FORM{"check"}==2){$check=" checked";}}
		else{$eok="<font color=red>×</font>"; if($FORM{"check"}==1){$check=" checked";}}
		if($ty){$Re="($tyレス)";}else{$Re="";}
		if($email){$name="<a href=\"mailto:$email\">$name</a>";}
		if($url){$url="/<a href='http://$url' target=$TGT>HP</a>";}
		if(-s "$i_dir/$ico"){$Size = -s "$i_dir/$ico";}else{$Size = 0;}
		$comment =~ s/<br>/ /g; $TB=1;
		if($tag){ $comment =~ s/</&lt;/g; $comment =~ s/>/&gt;/g; }
		if(length($comment) > 100){
			$comment=substr($comment,0,98); $comment=$comment . '..';
			$comment.="<a href=\"$cgi_f?mode=red&namber=$nam&pass=$FORM{'pass'}&no=$no$pp\" target=$TGT>全文</a>";
		}
		if($k){$BG=" bgcolor=\"$k_back\""; $k=0;}else{$BG=""; $k=1;}
		print <<"_ENT_";
<tr$BG><th><input type=checkbox name=ENT value=$nam$check>-$eok</th>
<td nowrap><font color="$kijino">#$nam</font> $Re<br>├$name <small>[$Ip]</small><br>
└<small>($date$url)</small></td>
<td>$comment<a href="$cgi_f?mode=red&namber=$nam&no=$no$pp" target=$TGT></a></td>
<td><a href="$i_Url/$ico" target=_blank>$ico</a><br><small>($Size\Bytes)</small></td>
<th><input type=checkbox name=IMD value=$nam></th></tr>
_ENT_
	$i++;
	if($i==30){print"</table>"; $i=0; $TB=0;}
	}else{next;}
}
close(LOG);
if($TB){print"</table>";}
print "<br><input type=submit value=\"許可/未許可 ファイル削除\"></form></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [表示形式]
# -> アップファイル表示形式の変更など(minf_)
#
sub minf_ {
if($FORM{"min"} eq ""){&get_("M");}
if($FORM{"min"}==1){$S="";$S2=" selected";$S3="";}
elsif($FORM{"min"}==2){$S="";$S2="";$S3=" selected";}
else{$S2="";$S=" selected";$S3="";}
print"</center><ul><form action=\"$cgi_f\" method=$met>$nf$pf";
if($mas_c){print"・表\示許可が出るまでファイルは<img src='$i_Url/$no_ent'>で表\示されます。<br>\n";}
if($_[0]){print"<input type=hidden name=H value=$_[0]>";}
print <<"_KEY_";
<input type=hidden name=page value=$page><input type=hidden name=mode value=cmin>
・記事中の画像表\示形式<select name=min>
<option value=0$S>$W2×$H2以下に縮小
<option value=1$S2>原寸大
<option value=2$S3>アイコン
</select><input type=submit value="変 更"$fm>
</form>
</ul><center>
_KEY_
}
#--------------------------------------------------------------------------------------------------------------------
# [アップファイル一覧]
# -> アップされたファイルを一覧で表示します(f_a_)
#
sub f_a_ {
&hed_("All Up File");
print <<"_ENT_";
<center><table width=90\%><tr><th bgcolor=$ttb>ファイル一覧</th></tr></table><br></center>
<ul><ul>
<li><a href="$cgi_f?no=$no$pp"> 掲示板に戻る</a>
<li> アップされたファイルのみの一覧です。
</ul></ul><center>
_ENT_
@ICO=();
open(LOG,"$log") || &er_("Can't open $log");
while (<LOG>) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	if($ico){push(@ICO,"$_");}
}
close(LOG);

@NEW=(); $FS=0; $KL="";
$page_=int($#ICO/$Ico_kp);
if($page_){
	$KL.="<hr size=1 width=\"80\%\">ページ移動 / ";
	if($FORM{'page'}){$page=$FORM{'page'};}else{$page=0;}
	$page_end=$page+($Ico_kp-1);
	if($page_end > $#ICO){$page_end=$#ICO;}
	for($i=0;$i<=$page_;$i++){
		$af=$page/$Ico_kp;
		if($i != 0){$KL.="| ";}
		if($i eq $af){$KL.="<b>$i</b>\n";}else{$KL.="<a href=\"$cgi_f?mode=f_a&page=$a&no=$no$pp\">$i</a>\n";}
		$a+=$Ico_kp;
	}
	$KL.="<hr size=1 width=80\%>";
}else{$page=0; $page_end=$#ICO;}
$i=0; print"$KL";
foreach ($page..$page_end) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$ICO[$_]);
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	if($i==0){print"<table bordercolor=$ttb width=90\% border=1 bgcolor=$k_back>\n";}
	$TB=1;
	if($i_mode && $ico){$Pr=""; &size;}else{$Pr="";}
	if($Size==0){next;}
	$FS=$FS+$Size;
	if($TOPH==0){$MD="mode=res&namber="; if($ty){$MD.="$ty";}else{$MD.="$nam";}}
	elsif($TOPH==1){$MD="mode=one&namber=$nam&type=$ty&space=$sp";}
	elsif($TOPH==2){$MD="mode=al2&namber="; if($ty){$MD.="$ty";}else{$MD.="$nam";}}
	print"<tr><td align=center><br><table><tr><td align=center>$Pr</td></tr></table><br>\n";
	print"<b>[<a href=\"$cgi_f?$MD&no=$no$pp\">返信ページ</a>]</b><br><br></td></tr>\n";
	$i++;
	if($i==30){print"</table>"; $i=0; $TB=0;}
}
if($TB){print"</table>";}
$FS=int($FS/1024);
print "<br>合計ファイルサイズ/$FS\KB$KL</center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [全表示]
# -> 設定されている掲示板を一覧表示します(a_)
#
sub a_ {
print "Content-type: text/html\n\n";
print <<"_HTML_";
<html><head>
$STYLE
$fsi
<!--$ver-->
<title>全BBS最新更新記事 [All BBS New Subject]</title>
<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS"></head>
_HTML_
print"<body text=$text link=$link vlink=$vlink bgcolor=$bg";
if ($back ne "") { print " background=\"$back\">\n";} elsif ($back eq "") { print ">\n";}
print<<"_HTML_";
<table width="100\%"><tr bgcolor="$ttb"><th>全BBS最終更新記事</th></tr></table><br>
<ul>
<li>Child Tree に設定されているBBSの最終更新記事を表\示します。
<li>BBSタイトルをクリックするとその掲示板へ、親記事タイトルをクリックするとその記事群へ飛びます。
</ul><center>
<table width="95\%" bordercolor="$ttb" border=1><tr bgcolor="$ttb"><th>BBSタイトル</th>
<th>最新更新された親記事タイトル</th><th>記事数</th><th>更新者</th><th>更新時間</th></tr>
_HTML_
foreach (0..$#set){
	if($set[$_]){
		unless(-e $set[$_]){next;}
		else{
			require "$set[$_]"; $no=$_;
			@RES=(); $N=0;
			open(LOG,"$log") || &er_("Can't open $log");
			while (<LOG>) {
				($namber,$date,$name,$email,$d_may,$comment,$url,
					$space,$end,$type,$del,$ip,$tim) = split(/<>/,$_);
				if($tim eq ""){next;}
				if($type){$ti=sprintf("%011d",$tim); if($date){unshift(@RES,"$ti<>$name<>$tim<>");} $N++;}
				else{$ti=sprintf("%011d",$tim); if($date){unshift(@RES,"$ti<>$name<>$tim<>");} $N++; last;}
			}
			close(LOG);
			@lines=(); @RES=sort(@RES); @RES=reverse(@RES);
			if(@RES){
				($Ti,$Name,$Tim)=split(/<>/,$RES[0]);
				if($TOPH==0){$MD="mode=res&namber=$namber&page=0";}
				elsif($TOPH==1){$MD="mode=all&namber=$namber&type=0&space=0";}
				elsif($TOPH==2){$MD="mode=al2&namber=$namber";}
				&time_($Tim);
			}else{$namber="#"; $d_may="記事がありません!"; $date="/"; $MD=""; $Name="/";}
		}
		print<<"_TOP_";
<tr bgcolor=$k_back><th><a href="$cgi_f?no=$no">$title</a></th>
<td align=center><font color="$kijino">[$namber]</font>
<a href="$cgi_f?$MD&no=$no"><b>$d_may</b></a></td>
<th>$N</th><th>$Name</th><td align=center><small>$date</small></td>
_TOP_
	}
}
print"</table></center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [アイコン画像表示]
# -> アイコン画像のサンプルを表示します(img_)
#
sub img_ {
&hed_("All Icon");
print"<center><table width=\"90\%\"><tr><th bgcolor=\"$ttb\">アイコン画像一覧</td></tr></table>\n";
print"<br><a href=\"javascript:close()\">|X| ウィンドウを閉じる</a><br><br>\n";
$I=0;
$page_=int($#ico1/$Ico_kp);
if($page_){
	print"ページ移動 / ";
	if($FORM{'page'}){$page=$FORM{'page'};}else{$page=0;}
	$page_end=$page+($Ico_kp-1);
	if($page_end > $#ico1){$page_end=$#ico1;}
	for($i=0;$i<=$page_;$i++){
		$af=$page/$Ico_kp;
		if($i != 0){print"| ";}
		if($i eq $af){print"<b>$i</b>\n";}else{print"<a href=\"$cgi_f?mode=img&page=$a&no=$no$pp\">$i</a>\n";}
		$a+=$Ico_kp;
	}
}else{$page=0; $page_end=$#ico1;}
print"<table border=1 bordercolor=$ttb>\n";
foreach ($page..$page_end){
	if($I==0){print"<tr>";}
	$I++;
	if($ico1[$_] eq "randam"){print"<th width=$Ico_w>ランダム<br>アイコン</th>"}
	elsif($ico1[$_] eq "master"){
		print"<th width=$Ico_w>";
		foreach $MAS (@mas_i){print"<img src=\"$IconDir/$MAS\">";}
		print"<br>管理者用</th>\n";
	}elsif($ico1[$_] eq ""){print"<th width=$Ico_w>なし</th>\n";}
	else{print"<th width=$Ico_w><img src=\"$IconDir/$ico1[$_]\"><br>$ico2[$_]</th>\n";}
	if($I >= $Ico_h){print"</tr>"; $I=0;}
}
if($I){print"</tr>";}
print"</table></center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [指定記事の表示]
# -> No指定された記事などをひとつ表示(read)
#
sub read {
if($namber=~/,/){@N=split(/\,/,$namber);}
elsif($namber=~/-/){
	($St,$En)=split(/-/,$namber);
	if($St<$En){if($En-$St > 50){$St=$En-49; $MSG="幅が大きすぎたため $St-$En に変更";} $Low=$St; $High=$En;}
	if($St>$En){if($St-$En > 50){$En=$St+49; $MSG="幅が大きすぎたため $St-$En に変更";} $Low=$En; $High=$St;}
	if($St eq ""){$Low=$En-10; $High=$En; $MSG="幅が未指定のため $St-$En に指定";}
	if($En eq ""){$Low=$St; $High=$St+10; $MSG="幅が未指定のため $St-$En に指定";}
	foreach($Low..$High){unshift(@N,$_);}
}
else{@N=$namber;}
$N=@N;
if($N > 50){splice(@N,50); $N=@N; $MSG="No指定が多いため $N 以降は非表\示";}
&hed_("No$namber の記事表\示");
print"<center><table width=90\%><tr><th bgcolor=$ttb>No$namber の記事</th></tr></table><br>$MSG";
$FLAG=0; @HTML=();
open(LOG,"$log") || &er_("Can't open $log");
while ($lines=<LOG>) {
	($nam,$date,$name,$email,$d_may,$comment,$url,
		$sp,$end,$ty,$del,$ip,$tim,$Se)=split(/<>/,$lines);
	$i=0; $HTML="";
	foreach $namber (@N){
		if($namber eq "$nam" && $namber ne $ty){
			($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
			($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
			($txt,$sel,$yobi)=split(/\|\|/,$SEL);
			&design($nam,$date,$name,$email,$d_may,$comment,$url,$sp,$end,$ty,$del,$Ip,$tim,$ico,
				$Ent,$fimg,$ICON,$ICO,$font,$hr,$txt,$sel,$yobi,$Se,"","N");
			$tim=sprintf("%011d",$tim);
			push(@HTML,"$tim<>$HTML<>");
			$FLAG++; last;
		}
		$i++;
	}
	if($HTML){splice(@N,$i,1);}
	if(@N){next;}else{last;}
}
close(LOG);
@HTML=sort(@HTML);
foreach (0..$#HTML){($time,$HTML)=split(/<>/,$HTML[$_]); print"$HTML\n";}
print"</center><br>\n";
if(@N){
	@N=reverse(@N);
	print"<hr width=\"95%\"><ul>";
	foreach $N (@N){
		print"<LI>No$N の記事は現在のログ内にありません！";
		if($klog_s){print"→<a href=\"$srch?no=$no&word=$N&andor=and&logs=all&PAGE=$klog_h[0]&ALL=1\">全過去ログから No$N の記事を探す</a>";}
	}
	print"</ul>";
}
print"<hr width=\"95%\">\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [フリーフォーム修復]
# -> 以前の文字コード上の不具合修正とログコンバート(freeform_)
#
sub freeform_{
if($FORM{'pass'} ne "$pass"){&er_("パスワードが違います!");}
if($locks){&lock_("$lockf");}
@NEW=(); $T=time; $DmyNo=0;
open(DB,"$log");
while ($lines=<DB>) {
	($namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim,$S) = split(/<>/,$lines);
	if($date eq ""){push(@NEW,$lines); next;}else{$lines=~ s/\n//g;}
	if($mo==1){
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
		if($SEL !~/\|\|\|\|/){
			($txt,$sel,$yobi)=split(/\|/,$SEL);
			$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$space<>$end<>$type<>$del<>";
			$new_.="$Ip:$ico:$Ent:$fimg:$TXT:$txt\|\|$sel\|\|$yobi\|\|:$R:<>$tim<>$S<>\n";
		}else{push(@NEW,$lines); next;}
	}elsif($mo eq "I-BOARD"){
		if($space =~/[A-Za-z\#]+/){
			($font,$hr)=split(/\;/,$space);
			if($ip=~ /:/){($ip,$ID,$Sex,$Old,$Rank,$T)=split(/:/,$ip);}
			if($type){$sp=15;}else{$sp=0;}
			if($DmyNo <= $namber){$DmyNo=$namber;}
			$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$sp<><>$type<>$del<>";
			$new_.="$ip\::1::\|$end\|$font\|$hr\|:$Old\|\|$Sex\|\|$ID\|\|:$Rank:<>$T<>$tim<>\n"; $T--;
		}else{&er_("すでに ChildTree 用になっています!","1");}
	}elsif($mo eq "UPP-BOARD"){
		if($space =~/[A-Za-z\#]+/){
			($font,$hr)=split(/\;/,$space);
			if($type){$sp=15;}else{$sp=0;}
			if($DmyNo <= $namber){$DmyNo=$namber;}
			if($end){foreach(0..$#exn){if($end=~ /$exn[$_]$/ || $end=~ /\U$exn[$_]\E$/){$TL=$exi[$_]; last;}}}
			$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$sp<><>$type<>$del<>";
			$new_.="$ip:$end:$tim:$TL:\|\|$font\|$hr\|:\|\|\|\|\|\|::<>$T<>$tim<>\n"; $T--;
		}else{&er_("すでに ChildTree 用になっています!","1");}
	}
	push(@NEW,$new_);
}
close(DB);
if($DmyNo){unshift(@NEW,"$DmyNo<><><><><><><><><>$DmyNo<><><><><>\n");}
open (DB,">$log");
print DB @NEW;
close(DB);
if(-e $lockf){rmdir($lockf);}
$msg="<h3>修復完了</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [内容チェック]
# -> フォーム内容をチェック(check_)
#
sub check_ {
if($Proxy){
	while(($envkey,$envvalue) = each(%ENV)){
		if($envkey =~ /proxy|squid/i || $envvalue =~ /proxy|squid/i){&er_("ProxyServer経由では書き込みできません!");}
	}
}
if($i_mode && $UP){
	$FLAG=0;
	foreach (0..$#exn){if($file=~ /$exn[$_]$/i){$FLAG=1; $TAIL=$exn[$_]; $TL=$exi[$_]; last;}}
	if($FLAG==0){&er_("アップできないファイル形式です!");}
	if(-e "$i_dir/$file"){
		$TIME=time; $file="$TIME$TAIL";
		$Henko="<h3>同名ファイルがあったため、$fileに変更しました</h3>";
	}elsif($file=~/[^\w\-\.]/){
		$TIME=time; $file="$TIME$TAIL";
		$Henko="<h3>ファイル名が不適切だったため、$fileに変更しました</h3>";
	}
	$MaxSize=$max_fs*1024;
	if($Fsize > $MaxSize){&er_("ファイルサイズが大きすぎます!");}
	if(open(OUT, "> $i_dir/$file")) {
		binmode(OUT);
		print OUT substr($Read, $Pos2, $Fsize);
		close(OUT);
	}
	chmod(0666,"$i_dir/$file");
}
if($FORM{'UP'} eq ""){
	if($name eq ""){&er_("名前が未記入!");}
	if($comment eq ""){&er_("コメントが未入力!");}
	if($email && $email !~ /(.*)\@(.*)\.(.*)/){&er_("E-メールの入力内容が不正です!");}
	#if($email && $email !~ /^[\w@\.\-_]+$/){&er_("E-メールの入力内容が不正です!");}
	if($email && 512 < length($email)){&er_("E-メールの入力内容が不正です!");}
	if(length($delkey) > 8 && $mode ne "h_w"){&er_("削除キー は8文字以内!");}
	if($NMAX && $NMAX < length($name)){&er_("名前は半角$NMAX字以内!");}
	if($TMAX && $TMAX < length($d_may)){&er_("タイトルは半角$TMAX字以内!");}
	if($CMAX && $CMAX < length($comment)){&er_("コメントは半角$CMAX字以内!");}
	if($TXT_H && $TXT_F && $txt eq "" && ($TXT_R==0 || $TXT_R && $type==0)){&er_("$TXT_Tが未入力!");}
	if($he_tp && $delkey eq "" && $FORM{'pass'} eq ""){ &er_("トピック追加には削除キーが必須です!"); }
	if($FORM{"pre"}){$comment="<pre>$comment</pre>";}
	if($FORM{"dmay"}){$d_may=$FORM{"dmay"};}
	if($d_may eq ""){$d_may="NO TITLE";}
	$Ip = $ENV{'REMOTE_ADDR'};
	if($ICON ne ""){
		$ICO=$ico1[$ICON];
		if($ICO eq "randam"){
			srand;
			$randam=$#ico1;
			$ICON  =int(rand($randam));
			$ICO = $ico1[$ICON];
			if($ICO eq "" || $ICO eq "randam" || $ICO eq "master"){
				foreach(0..$#ico1){
					if($ico1[$_] ne "ramdam" && $ico1[$_] ne "master"){$ICO=$ico1[$_]; $ICON=$_;}
				}
			}
			$CICO="randam";
		}elsif($ICO eq "master"){
			$ICO_F=0;
			if($mode eq "h_w"){$delkey=$FORM{'pass'};}
			foreach (0..$#mas_p){if($mas_p[$_] eq $delkey){$ICO=$mas_i[$_]; $ICO_F=1; $ICON="m$_"; last;}}
			if($ICO_F==0){&er_("管理者用アイコンは使用できません!");} $CICO="master";
		}else{$CICO=$ICO;}
	}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [一覧表示のフッタ]
# -> 一覧表示時のフッタ(allfooter)
#
sub allfooter {
print"<ul><b>";
if($Bl){print"$Bl＜前の$_[0]$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl次の$_[0]＞$Nle\n";}
print <<"_HTML_";
</b><ul>( ページ移動 / $Plink )</ul></ul>
<hr size=1 width="90\%">
<form action="$srch" method=$met>
<input type=hidden name=andor value=and><input type=hidden name=logs value="$log">
$nf$pf
<ul><b>[検索フォーム]</b>
<ul>現在ログ内全記事数/<b>$NS</b> <small>(親/$total レス/$RS)</small> から検索
　キーワード/ <input type=text name=word size=10 value="$word">
<input type=submit value="検 索">
</ul></ul></form>
<hr size=1 width="90\%">
<form action="$cgi_f" method=$met>
$nf$pf
<ul><b>[削除/編集フォーム]</b>
<ul>記事No<small>(半角数字)</small>/<input type=text name=del size=8$ff> 
<select name=mode>
<option value=nam>編集
<option value=key>削除
</select>
削除キー/<input type=password name=delkey size=8$ff>
<input type=submit value=" 送信 "$fm>
</ul></form>
</ul><hr width="95\%">
_HTML_
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie削除]
# -> cookieを削除(有効期限を過去に)します(cookdel)
#
sub cookdel{
if($mo eq "ID"){
#	print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n"; $msg="<h4>ID削除完了</h4>";
}
elsif($mo eq "ALL"){
	print"Set-Cookie: $s_pas=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	print"Set-Cookie: Cmin=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
#	print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	print"Set-Cookie: CBBS=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	$msg="<h4>cookie削除完了</h4>";
}
&hed_("cookie Delete");
print<<"_HTML_";
<SCRIPT language="JavaScript">
<!--
function Link(url) {
	if(confirm("本当に削除してもOKですか?\\n(削除すると内容は元に戻せません!)")){location.href=url;}
	else{location.href="#";}
}
//-->
</SCRIPT>
<center>$msg
_HTML_
#if($UID){print"<a href=\"#\" onClick=\"Link('$cgi_f?mode=cookdel&mo=ID&no=$no$pp')\">IDのcookieのみ削除</a> /\n";}
print"<a href=\"#\" onClick=\"Link('$cgi_f?mode=cookdel&mo=ALL&no=$no$pp')\">この掲示板全般のcookie削除</a><br>";
print"*) 削除が終了したらウィンドウを閉じてください。</center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [携帯端末向け出力]
# -> 携帯オプションからの作業命令終了の表示(ktai)
#
sub ktai {
$_[1] =~ tr/+/ /;
$_[1] =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$html ="<html><head><title>$_[0]完了</title></head>";
$html.="<body><center>$_[0]完了<br><br><a href=\"$_[1]\">[戻]</a></center></body></html>";
$len = length($html);
print "Content-type: text/html\n";
print "Content-length: $len\n";
print "\n";
print "$html";
exit;
}
