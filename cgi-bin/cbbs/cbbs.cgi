#!/usr/local/bin/perl

require './jcode.pl';

#------------------------------------------
$ver = "Child Tree v8.94";# (�c���[���f����)
#------------------------------------------
# Copyright(C) ��イ����
# E-Mail:ryu@cj-c.com
# W W W :http://www.cj-c.com/
#------------------------------------------

#---[�ݒ�t�@�C��]-------------------------

# �����悤�ɂ����ł����₹�܂��B
# [ ]���̐������g��CGI�ɃA�N�Z�X����Ƃ��̐ݒ�t�@�C���œ��삵�܂��B
# $set[12] �̐ݒ�t�@�C�����g���ꍇ: http://www.---.com/cgi-bin/cbbs.cgi?no=12
$set[0]="./set.cgi";
$set[1]="./set1.cgi";
$set[2]="./set2.cgi";
$set[3]="./set3.cgi";
$set[4]="./set4.cgi";

# �֎~������ �^�O�g�p�̏ꍇ�͋֎~�^�O������OK �����悤�ɂ����ł��w��\
@NW=('����');

# �r��IP/�֎~������ݒ�t�@�C��
$IpFile="IpAcDeny.cgi";
$NWFile="WordDeny.cgi";

# ---[�ݒ肱���܂�]--------------------------------------------------------------------------------------------------
#
# �t�@�C���A�b�v�@�\�͂Ƃقق����WWWUPL���Q�l�ɂ��Ă��܂��B
# -> http://tohoho.wakusei.ne.jp/
#
# ---[�r��IP/�֎~������ǂݍ���]-------------------------------------------------------------------------------------
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
	if($match){&er_("���Ȃ��ɂ͉{������������܂���!");}
}
# ---[�ݒ�t�@�C���ǂݍ���]------------------------------------------------------------------------------------------
$res_r=1;
&d_code_;
if($no eq ""){$no=0;}
if($set[$no]){unless(-e $set[$no]){&er_('�ݒ�t�@�C���������ł�!');}else{$SetUpFile="$set[$no]"; require"$SetUpFile";}}
else{&er_('�ݒ�t�@�C����CGI�ɐݒ肳��Ă܂���!');}
$nf="<input type=hidden name=no value=$no>\n";
# ---[�t�H�[���X�^�C���V�[�g�ݒ�]------------------------------------------------------------------------------------
$ag=$ENV{'HTTP_USER_AGENT'};
if($fss && $ag =~ /IE|Netscape6/){
	$fm=" onmouseover=\"this.style.$on\" onmouseout=\"this.style.$off\"";
	$ff=" onFocus=\"this.style.$on\" onBlur=\"this.style.$off\"";
	$fsi="$fst";
}
# ---[�ȈՃp�X���[�h�����֘A]----------------------------------------------------------------------------------------
if($s_ret){if($FORM{"P"} eq ""){
	&get_("P");} $P=$FORM{"P"};
	$pf="<input type=hidden name=P value=$P>\n";
	$pp="&P=$P";
}else{$pf=""; $pp="";}
if($FORM{'KLOG'}){
	$KLOG=$FORM{'KLOG'}; $TrON=0; $TpON=1; $ThON=0; $TOPH=2;
	unless($KLOG=~ /^[\d]+/){&er_("���̃t�@�C���͉{���ł��܂���!");}
	$log="$klog_d\/$KLOG\.txt";
	$pp.="&KLOG=$KLOG";
	$pf.="<input type=hidden name=KLOG value=$KLOG>\n";
}
if($s_ret && $P eq "" && ($mode eq "alk"||$mode eq "")){&pas_;}
if($s_ret==2 && $P eq "R"){&er_("�p�X���[�h���Ⴂ�܂�!");}
if($s_ret && $P ne "R"){if($P ne "$s_pas"){&er_("�p�X���[�h���Ⴂ�܂�!");}else{&set_("P");}}
# ---[�T�u���[�`���̓ǂݍ���/�\���m��]-------------------------------------------------------------------------------
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
# [�L���f�U�C��] 
# -> �L���𓝈�f�U�C���ŕ\��(design)
#
sub design {
local($namber,$date,$name,$email,$d_may,$comment,$url,$space,$end,$type,$delkey,$ip,$tim,$ico,
	$Ent,$fimg,$mini,$icon,$font,$hr,$txt,$sel,$yobi,$Se,$ResNo,$htype,$hanyo)=@_; @_=();
$HTML="";
if($font eq ""){$font=$text;}
if($hr eq ""){$hr=$ttb;}
if($d_may eq ""){$d_may="NO TITLE";}
if($Icon && $comment=~/<br>\(�g��\)$/){$icon="$Ico_k";}
if($icon ne ""){
	if($IconHei){$WH=" height=$IconHei width=$IconWid";}
	$icon="<img src=\"$IconDir\/$icon\"$WH>";
}
if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
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
if($mas_c==2 && $Ent==0){$comment="�R�����g�\\��:������";}
$comment="<!--C-->$comment"; &auto_($comment);
if($o_mail){$Smsg="[���[����M/";if($Se==2 || $Se==1){$Smsg.="ON]\n";}else{$Smsg.="OFF]\n";}}
if($ico && $i_mode){$Pr=""; &size(); $Pr="<tr><td align=center>$Pr</td></tr>\n"; $SIZE+=$Size;}else{$Pr="";}
$agsg=""; $UeSt=""; $Pre="";
if($ResNo==0){$ResNo="�e";}
if($htype eq "T"){
	$ResNo="$ResNo�K�w"; $Border=1; $Twidth=90;
	if($Res_i){$IN="<b><a href=\"$cgi_f?mo=1&mode=one&namber=$namber&type=$type&space=$space&no=$no$pp#F\">�L�����p</a></b>";}
}elsif($htype eq "T2"){
	$ResNo="$ResNo�K�w"; $Border=1; $Twidth=90;
	$IN="<b><a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">�ԐM</a></b>";
	if($Res_i){$IN.="/<b><a href=\"$cgi_f?mo=1&mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">���p�ԐM</a></b>\n";}
	$VNo=$namber; $OTL="";
	if($type > 0){$UeSt.="$b_ "; $OTL=" <a href=#$ty>�e $type </a> /";}else{$UeSt.="�e�L���@/ ";}
	if($n_){$UeSt.="$n_ </a>\n";}else{$UeSt.="�ԐM����\n";}
	$OTL.=" <a href=#>�� Tree</a>\n";
	$IN="[$OTL]\n".$IN;
	$HTML.="<br>";
}elsif($htype eq "F"){
	$VNo++;	$ResNo="inTopicNo.$ResNo"; $Border=0; $Twidth=90;
	$IN="<a href=\"$cgi_f?mode=al2&mo=$nam&namber=$FORM{'namber'}&space=$sp&rev=$rev&page=$fp&no=$no$pp#F\"><b>���p�ԐM</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=al2&mo=$nam&namber=$FORM{'namber'}&space=$space&rev=$rev&page=$fp&In=1&no=$no$pp#F\"><b>�ԐM</b></a>";}
	if($VNo==1){$sg=$VNo+1; $agsg="\&nbsp\;\&nbsp\;<a href=\"#$sg\">��</a><a href=\"#1\">��</a>";}
	elsif($VNo >= $topic){$ag=$VNo-1; $agsg="<a href=\"#$ag\">��</a>�@<a href=\"#1\">��</a>";}
	else{$ag=$VNo-1; $sg=$VNo+1; $agsg="<a href=\"#$ag\">��<a href=\"#$sg\">��<a href=\"#1\">��</a>";}
}elsif($htype eq "N"){
	$ResNo=""; $Border=1; $Twidth=90;
	if($TOPH==0){$MD="mode=res&namber="; if($type){$MD.="$type";}else{$MD.="$namber";}}
	elsif($TOPH==1){$MD="mode=one&namber=$namber&type=$type&space=$space";}
	elsif($TOPH==2){$MD="mode=al2&namber="; if($type){$MD.="$type";}else{$MD.="$namber";} $MD.="&space=$space";}
	$IN="<b><a href=\"$cgi_f?$MD&no=$no$pp#F\">�ԐM</a></b>";
	if($Res_i){$IN.="/<b><a href=\"$cgi_f?$MD&mo=$namber&no=$no$pp#F\">���p�ԐM</a></b>\n";}
	$HTML.="<br>";
}elsif($htype eq "P"){
	$ResNo=""; $Border=1; $Twidth=90;
	if($hanyo eq "randam"){$icon="�A�C�R��<br>�����_��";}
	$Smsg.="<!--"; $Pre="--";
}elsif($htype eq "TR"){
	if($ResNo eq "�e"){$ResNo="�e�L��"; $Twidth=100;}else{$ResNo="ResNo.$ResNo"; $Twidth=90;}
	$Border=0; $Smsg.="<!--"; $Pre="--";
	$IN="<a href=\"$cgi_f?mode=res&namber=$nam&type=$type&space=$space&mo=$namber&page=$PNO&no=$no$pp#F\"><b>���p�ԐM</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=res&namber=$nam&type=$type&space=$space&mo=$namber&page=$PNO&In=1&no=$no$pp#F\"><b>�ԐM</b></a>";}
}elsif($htype eq "TRES"){
	$Border=0; $Twidth=90; $VNo++;
	if($ResNo eq "�e"){$ResNo="�e�L��";}else{$ResNo="ResNo.$ResNo";}
	if($VNo==1){$sg=$VNo+1; $agsg="\&nbsp\;\&nbsp\;<a href=\"#$sg\">��</a><a href=\"#1\">��</a>";}
	elsif($VNo >= $topic){$ag=$VNo-1; $agsg="<a href=\"#$ag\">��</a>�@<a href=\"#1\">��</a>";}
	else{$ag=$VNo-1; $sg=$VNo+1; $agsg="<a href=\"#$ag\">��<a href=\"#$sg\">��<a href=\"#1\">��</a>";}
	$IN="<a href=\"$cgi_f?mode=res&mo=$nam&namber=$FORM{'namber'}&space=$sp&page=$page&no=$no$pp#F\"><b>���p�ԐM</b></a>";
	if($Res_i){$IN.="/<a href=\"$cgi_f?mode=res&mo=$nam&namber=$FORM{'namber'}&space=$sp&page=$page&In=1&no=$no$pp#F\"><b>�ԐM</b></a>"}
}
$HTML.=<<"_HTML_";
<a name="$VNo"></a>
<table width=$Twidth\% bgcolor=$k_back border=$Border bordercolor=$hr cellspacing=0><tr><td>$UeSt
<table border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$hr>
<tr><td width=1\% nowrap><b><font color="$kijino">��$namber</font></b> / $ResNo)</td>
<td bgcolor=$hr>�@<b><font color=$t_font>$d_may</font></b>
</td></tr></table><div align=right>$agsg</div>
�����e��/ $name $email <small>$R-($date) $yobi<br>$url</small>
<ul><table><tr><td align=center>$icon</td><td><font color="$font">$comment<br></td></tr></table></ul>
<div align=right>$end</div></td></tr>
$Pr<tr><form action="$cgi_f" method=$met>
<td align=right>$IN
$Smsg
<input type=hidden name=del value=$namber>$nf$pf
�폜�L�[/<input type=password name=delkey size=8$ff>
<select name=mode>
<option value=nam>�ҏW
<option value=key>�폜
</select>
<input type=submit value="�� �M"$fm$Pre></td></form></tr></table>
_HTML_
}
#--------------------------------------------------------------------------------------------------------------------
# [�p�X���[�h�F��]
# -> �������̃p�X���[�h�F��(pas_)
#
sub pas_ {
&hed_("Pass Input");
print <<_PAS_;
<center><table width=90\%>
<tr bgcolor=$ttb><th>�p�X���[�h�F��</th></tr>
<tr><th>*�������ނɂ̓p�X���[�h���K�v�ł�!<form action=$cgi_f method=$met>
<input type=password size=8 name=P$ff>$nf
<input type=submit value=" �F�� "$fm>
</form></th></tr></table>
_PAS_
if($s_ret==1){
	print"�L���̉{���͂ł��܂�(���[�h�I�����[)\n";
	print" <a href=\"$cgi_f?P=R&no=$no\"><b>�L�����{������</b></a>\n";
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�g�s�b�N�ꗗ�\��]
# -> �g�s�b�N���ꗗ�\��(html2_)
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
�� $new_t���Ԉȓ��ɍ쐬���ꂽ�g�s�b�N�� $new_i �ŕ\\������܂��B<br>
�� $new_t���Ԉȓ��ɍX�V���ꂽ�g�s�b�N�� $up_i_ �ŕ\\������܂��B<br>
�� �g�s�b�N�^�C�g�����N���b�N����Ƃ��̃g�s�b�N�̓��e�ƕԐM��\\�����܂��B
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

print"</center><ul>[ �S$total�g�s�b�N($Pg-$Pg2 �\\��) ]�@\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/($tpmax*$tab_m);
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?page=$a&H=F&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$tpmax*$tab_m;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=F&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="���e��"; $OJ3="<a href=\"$cgi_f?H=F&W=R&no=$no$pp\">���X��</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=F&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="<a href=\"$cgi_f?H=F&W=T&no=$no$pp\">���e��</a>"; $OJ3="���X��";}
else{$OJ1="�X�V��"; $OJ2="<a href=\"$cgi_f?H=F&W=T&no=$no$pp\">���e��</a>"; $OJ3="<a href=\"$cgi_f?H=F&W=R&no=$no$pp\">���X��</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ] ���\\�[�g���@�ύX </ul><center>";
$k=0; $q=0;
if($k){$p=$tab_m-$i; $page+=$tpmax*$p; last;}
if($topok){$TP="<th>�g�s�b�N�쐬��</th>";}
if($he_tp==0){$SK="<th>�ŏI������</th>";}
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
		print"<th>�g�s�b�N�^�C�g��</th><th>�L����</th>$TP$SK<th>�ŏI�X�V</th>$EE</tr>\n";
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
	$FL="<br><small>��<font color=$kijino>#$namber</font>�@[�쐬:$date]";
	if($File && $Size){$FL.="�@[File:$File -$KB\KB]";}
	if($topic < $ksu){
		$a=0; $PG_=int(($ksu-1)/$topic); $RP="";
		for($j=0;$j<=$PG_;$j++){
			$RP.="<a href=\"$cgi_f?mode=al2&namber=$namber&page=$a&rev=$tp_hi&no=$no$pp$Wf\">$j</a>\n";
			$a+=$topic;
		}
		if($FL){$FL.="�@[ $RP]";}else{$FL="<br>�@<small>[ $RP]";}
	}
	$FL.="</small>";
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
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
&allfooter("�g�s�b�N$view");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�R�����g���p]
# -> �g�s�b�N/�X���b�h�\���̍ۂ̈��p����(comin_)
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
	$com="��No$nam�ɕԐM($na����̋L��)<br>$co";
	$com=~ s/<br>/\r&gt; /g;
	$com=~ s/&gt; &gt; /&gt;&gt;/g;
}
$FORM{"type"}=$ty; $type=$ty; $namber=$nam;
}
#--------------------------------------------------------------------------------------------------------------------
# [�g�s�b�N���e�\��]
# -> �g�s�b�N���e��\��(all2)
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
$fhy.="<tr><th bgcolor=$ttb>���̃g�s�b�N�ɏ�������</th></tr></table></a></center>\n";
$total=@TOP;
if($FORM{'page'} eq ''){$page=0;}else{$page=$FORM{'page'};}
$PAGE=$page/$topic;
&hed_("One Topic All View / $TitleHed / Page: $PAGE","1");
print"<center>";
if($rev == 0){
	print"<b>[ <a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&rev=1&no=$no$pp\">";
	print"�ŐV�L���y�ѕԐM�t�H�[�����g�s�b�N�g�b�v��</a> ]</b><br><br>\n";
}elsif($rev){
	print"<b>[ <a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&rev=0&no=$no$pp\">�e�L�����g�s�b�N�g�b�v��</a> ]</b><br><br>\n";
}
if($rev){
	print"$fhy";
	if($r_max && ($total-1) >= $r_max){
		print"<center><br><h3>���X���̌��x�𒴂����̂Ń��X�ł��܂���B</h3>(���X�����x:$r_max ���݂̃��X��:$#TOP)\n";
		print" �� <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[�g�s�b�N�̐V�K�쐬]</a></b></center>";
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
print"</center><ul>[ �g�s�b�N���S$total�L��($Pg-$Pg2 �\\��) ]�@\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$topic;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$a&rev=$rev&no=$no$pp\">$i</a>\n";}
	$a+=$topic;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
print"$Plink<br>";
if($Dk){print"($Dk���̍폜�L�����\\��)<br>";}
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
if($TrON){$TrLink="<a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&no=$no$pp\">$all_i ���̃g�s�b�N���c���[�ňꊇ�\\��</a>";}
print"</center><ul>$TrLink</ul>\n";
print"<center><hr width=\"90\%\"><b>\n";
if($Bl){print"$Bl���O��$topic��$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl����$topic����$Nle\n";}
print"</b><br><br>�g�s�b�N���y�[�W�ړ� / $Plink";
$Ta=$total-1;
if($r_max && $Ta > $r_max){
	print"<br><br><h3>���X���̌��x�𒴂����̂Ń��X�ł��܂���B</h3>(���X�����x:$r_max ���݂̃��X��:$Ta)";
	print" �� <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[�g�s�b�N�̐V�K�쐬]</a></b></center>";
}else{
	if($En && $end_e){print"<center><h3>$end_ok / �ԐM�s��</h3></center>";}
	else{
		if($total <= ($page+$topic) && $rev==0){
			print"<br><br>$fhy</center>";
			&forms_("F");
		}elsif($total >= ($page+$topic) && $rev==0){
			$page=$i-1; $a-=$topic;
			print"<br><br><b>[<a href=\"$cgi_f?mode=al2&namber=$FORM{'namber'}&page=$a&no=$no$pp#F\">���̃g�s�b�N�ɕԐM</a>]</b>";
		}
	}
}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�t�H�[��]
# -> �t�H�[����\������(forms_)
#
sub forms_ {
if($s_ret && $P ne "$s_pas"){print"<center><h3>�������ݕs��</h3></center>\n";}
elsif($KLOG){print"<center><h3>�ߋ����O�ɂ͏������ݕs��</h3></center>";}
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
��&gt; �֘A���郌�X�L�������[���Ŏ�M���܂���?<select name=send>
<option value=0>NO
<option value=1$PVE>YES
</select> /
�A�h���X<select name=pub>
<option value=0>����J
<option value=1$Pch>���J
</select></td></tr>
_MAIL_
	}
	if($he_tp){
		$TPH="<h3>�g�s�b�N���쐬�������̍폜�L�[�ł̂ݕԐM���ł��܂��B</h3>";
		$KEY="/�g�s�b�N�ǉ��ɂ͍폜�L�[���K�{�ł�!\n";
	}
	if(($com =~ /<pre>/)&&($com =~ /<\/pre>/)){$com=~ s/<pre>//g;$com=~ s/<\/pre>//g;}
	if($tag){$com=~ s/</&lt;/g; $com=~ s/>/&gt;/g;}
	if($mas_c==2 && $Ent==0){$com="�R�����g�\��:������";}
	if($Res_i && $mo eq "" && $FORM{'PV'} eq ""){$com="";}
	if($i_mode && ($ResUp || ($ResUp==0 && $sp==0))){
		$FORM_E=" enctype=\"multipart/form-data\"";
		$FI="<tr><td bgcolor=$ttb>File</td><td>/<input type=file name=ups size=60$ff><br>�A�b�v�\\�g���q=&gt;\n";
		foreach (0..$#exn) {
			if($exi[$I] eq "img"){$EX="<b>$exn[$_]</b>";}else{$EX="$exn[$_]";}
			$FI.="/$EX"; $I++;
		}
		$FI.=<<"_M_";
<br>
1) �����̊g���q�͉摜�Ƃ��ĔF������܂��B<br>
2) �摜�͏�����Ԃŏk���T�C�Y$H2�~$W2�s�N�Z���ȉ��ŕ\\������܂��B<br>
3) �����t�@�C��������A�܂��̓t�@�C�������s�K�؂ȏꍇ�A<br>
�@�@�t�@�C�����������ύX����܂��B<br>
4) �A�b�v�\\�t�@�C���T�C�Y��1��<B>$max_fs\KB</B>(1KB=1024Bytes)�܂łł��B<br>
5) �t�@�C���A�b�v���̓v���r���[�͗��p�ł��܂���B<br>
_M_
		if($ResUp && $sp){
			$SIZE=int($SIZE/1024);
			$Rest=$max_or-$SIZE;
			$FI.="6) �X���b�h���̍��v�t�@�C���T�C�Y:[$SIZE/$max_or\KB] <b>�c��:[$Rest\KB]</b>\n";
		}
	}else{$FORM_E=""; $FORM_I="";}
	if($NMAX){$NML=" maxlength=$NMAX";}
	if($TMAX){$YML=" maxlength=$TMAX";}
	if($CMAX){$CML="/���p$CMAX�����ȓ�";}
	if($UID){$uidv=" [ID:$pUID]<!--��<a href=\"$cgi_f?mode=cookdel\" target=\"_blank\">����ID��j��</a>-->";}
	if($tag){$tagmsg="�\\�ł��B";}else{$tagmsg="�ł��܂���B";}
	if($FORM{"PV"} eq ""){print"<form action=\"$cgi_f\" method=\"$met\"$FORM_E>";}
	print <<"_FORM_";
<ul><ul><li>���͓��e�Ƀ^�O�͗��p$tagmsg</ul>$atcom<br><input type=hidden name=N value=$N_NUM>
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
�ʏ탂�[�h-&gt;<input type=radio name=pre value=0$T>�@
�}�\\���[�h-&gt;<input type=radio name=pre value=1$Z>
(�K���ɉ��s���ĉ�����$CML)<br>
<textarea name="comment" rows=12 cols=75 wrap=$wrap$ff>$com</textarea></td></tr>
$FI
_FORM_
	if(@fonts){
		print "<tr><td bgcolor=$ttb>�����F</td><td>/\n";
		foreach (0 .. $#fonts) {
			if($c_font eq ""){$c_font="$fonts[0]";}
			print"<input type=radio name=font value=\"";
			if($c_font eq "$fonts[$_]"){print"$fonts[$_]\" checked><font color=$fonts[$_]>��</font>\n";}
			else{print"$fonts[$_]\"><font color=$fonts[$_]>��</font>\n";}
		}
		print"</td></tr>";
	}
	if(@hr){
		print"<tr><td bgcolor=$ttb>�g���F</td><td>/\n";
		foreach (0 .. $#hr) {
			if($c_hr eq ""){$c_hr="$hr[0]";}
			print "<input type=radio name=hr value=\"";
			if($c_hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=$hr[$_]>��</font>\n";}
			else{print"$hr[$_]\"><font color=$hr[$_]>��</font>\n";}
		}
		print"</td></tr>";
	}
	if($Icon){
		print"<tr><td bgcolor=$ttb>Icon</td><td>/ <select name=Icon>\n";
		foreach(0 .. $#ico1) {
			if($c_ico eq $ico1[$_]){print"<option value=\"$_\" selected>$ico2[$_]\n";}
			else{print"<option value=\"$_\">$ico2[$_]\n";}
		}
		print"</select> <small>(�摜��I��/";
		print"<a href='$cgi_f?mode=img&no=$no$pp' target=_blank>�T���v���ꗗ</a>)</small></td></tr>\n";
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
		if($end_c){$end_form="<tr><td colspan=2>$end_ok �ɂȂ����炻�̎|�������Ă��������B</td></tr>";}
		else{$end_form="<tr><td colspan=2>$end_ok BOX/<input type=checkbox name=end value=\"1\"$PVC>$end_m</td></tr>";}
	}
	if($AgSg && $sp > 0){
		$AgSgIn ="�L���\\�[�g/<select name=\"AgSg\">";
		if($FORM{"AgSg"} eq "0"){$SgS=" selected";}
		$AgSgIn.="<option value=1>�グ��(age)<option value=0$SgS>������(sage)</select>\n";
	}else{$AgSgIn="<input type=hidden name=AgSg value=1>\n";}
	if($_[0]){print"<input type=hidden name=H value=$_[0]>";}
print<<"_FORM_";
<tr><td bgcolor=$ttb>�폜�L�[</td><td>/
<input type=password name=delkey value="$c_key" size=8$ff>
<small>(���p8�����ȓ�$KEY)</small>
</td></tr>
$end_form
<tr><td colspan=2 align=right>$AgSgIn�@
�v���r���[/<input type=checkbox name=PV value=1>�@
<input type=submit value=" �� �M "$fm>
<input type=reset value="���Z�b�g"$fm></td></tr></table></form></ul><hr width=\"95\%\">
_FORM_
	}
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�L���\��]
# -> �c���[�̋L����\������(one_)
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
		$com="��No$namber�ɕԐM($name����̋L��)<br>$comment";
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
		print"<tr align=center><td bgcolor=$ttb><b>�O�̋L��</b><small>(���ɂȂ����L��)</small></td>\n";
		print"<td bgcolor=$ttb><b>���̋L��</b><small>(���̋L���̕ԐM)</small></td></tr>\n";
	}
	if($end){$end="$end_ok"; $En=1;}
	if($d_may eq ""){$d_may="No Title";}
	$date=substr($date,2,19);
	if(($time_k-$tim)>$new_t*3600){$news="$hed_i";}else{$news="$new_i";}
	if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
	if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
	if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
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
			$b_="<a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">��$d_may</a>\n/$name <small>$yobi</small>$Pr";
		}elsif($type == 0){$b_="�e�L��";}
		if($sp eq $psp && $nam > $namber && $i == 1){
			$n_.="<a href=\"$cgi_f?mode=one&namber=$nam&type=$ty&space=$sp&no=$no$pp\">��$d_may</a>\n/$name <small>$yobi</small>$Pr<br>";
			$N_NUM=$nam;
		}
		if($i==1){$rs=1;}
	}
	$im=""; $im2=""; $im3="";
	if($sp > $SP && $F){$N_NUM=$nam;}
	if($sp eq $SP && $F){$F=0;}
	if($N_NUM eq $nam && $F==0){$F=1; $SP=$sp;}
	if($nam eq $namber){$im="<b STYLE=\"background-color:$t_back\">"; $im2="</b>"; $im3=" <b>��Now</b>";}
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
if($n_){print"$n_\n";}else{print"�ԐM����<br>\n";}
print"�@</td></tr><th colspan=2 bgcolor=\"$ttb\">��L�֘A�c���[</th></tr><tr><td colspan=2><br>$Tree\n";
$total=@TREE-1;
if($type>0){$a_="$type";}elsif($type==0){$a_="$namber";}
if($TpON){$TpLink=" / <a href=\"$cgi_f?mode=al2&namber=$a_&rev=$r&no=$no$pp\">��L�c���[���g�s�b�N�\\��</a>\n";}
print"<br><a href=\"$cgi_f?mode=all&namber=$a_&type=0&space=0&no=$no$pp\">$all_i ��L�c���[���ꊇ�\\��</a>$TpLink\n";
print"<br>�@</td></tr><tr><th colspan=2 bgcolor=\"$ttb\"><a name=F>��L�̋L���֕ԐM</a></th></tr></table></center>\n";
if($r_max && $total >= $r_max){
	print"<center><h3>���X���̌��x�𒴂����̂Ń��X�ł��܂���B</h3>(���X�����x:$r_max ���݂̃��X��:$total)\n";
	print" �� <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[�c���[�̐V�K�쐬]</a></b></center>\n";
}else{if($En && $end_e){print"<center><h3>$end_ok / �ԐM�s��</h3></center>";}else{&forms_("T");}}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�\��]
# -> �c���[�̈ꗗ��\������(html_)
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
�� $new_t���Ԉȓ��̋L���� $new_i �ŕ\\������܂��B<br>
�� $all_i ���N���b�N����Ƃ��̃c���[���ꊇ�ŕ\\�����܂��B
</td></tr></table>$Henko<hr width=\"95\%\">
_HTML_
if($i_mode){&minf_("T");}

print"</center><ul>[ �S$total�c���[($Pg-$Pg2 �\\��) ]�@\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n"; $a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$a_max;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?page=$a&H=T&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$a_max;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle\n";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?H=T&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="���e��"; $OJ3="<a href=\"$cgi_f?H=T&W=R&no=$no$pp\">���X��</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?H=T&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="<a href=\"$cgi_f?H=T&W=T&no=$no$pp\">���e��</a>"; $OJ3="���X��";}
else{$OJ1="�X�V��"; $OJ2="<a href=\"$cgi_f?H=T&W=T&no=$no$pp\">���e��</a>"; $OJ3="<a href=\"$cgi_f?H=T&W=R&no=$no$pp\">���X��</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ] ���\\�[�g���@�ύX </ul><center>";
foreach ($page .. $page_end) {
	($T,$namber,$date,$name,$email,$d_may,$comment,$url,
		$space,$end,$type,$del,$ip,$tim,$Se)=split(/<>/,$NEW[$_]);
	if(($time_k - $tim) > $new_t*3600){$news="$hed_i";}else{$news="$new_i";}
	if($email && $Se < 2){$name="$name <a href=\"mailto:$SPAM$email\">$AMark</a>";}
	($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$ip);
	($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
	($txt,$sel,$yobi)=split(/\|\|/,$SEL);
	if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
		if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
		if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
		elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
		$news.="<img src=\"$IconDir\/$mICO\" border=0$WHm>";
	}
	if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
	if($d_may eq ""){$d_may="No Title";}
	if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
	if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
	if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
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
			if(@ico3 && $Icon &&($rICON ne "" || $rcom=~/<br>\(�g��\)$/)){
				if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
				if($rICON ne ""){if($rICON=~ /m/){$rICON=~ s/m//; $mrICO=$mas_m[$rICON];}else{$mrICO=$ico3[$rICON];}}
				elsif($Icon && $rcom=~/<br>\(�g��\)$/){$mrICO="$Ico_km";}
				$news.="<img src=\"$IconDir\/$mrICO\" border=0$WHm>";
			}
			if($ico && $i_mode){$Pr=""; &size(1); $Pr=" "."$Pr";}else{$Pr="";}
			if($rdm eq ""){$rdm="No Title"; }
			if($yobi){$yobi="<font color=\"$IDCol\">[ID:$yobi]</font> ";}
			if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
			if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
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
&allfooter("�c���[$a_max");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�c���[�ꊇ�\��]
# -> �c���[�̊֘A�L����\������(all_)
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
<th bgcolor=$ttb>�c���[�ꊇ�\\��</th></tr>$IcCom
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
				if($s eq $nsp && $nam > $n && $i != 1){$b_="<a href=\#$n>��[ $n ]</a> / ";}
				if($s eq $psp && $nam < $n && $i == 1){$n_.="<a href=\#$n>��[ $n ]</a>\n";}
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
		if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
		if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
		if($Txt || $Sel ||($Txt && $Sel)){if($TS_Pr==0){$d_may="$Txt$Sel/"."$d_may";}}
		if(length($d_may)>$t_max){$d_may=substr($d_may,0,($t_max-2));$d_may="$d_may..";}
		if(@ico3 && $Icon && ($ICON ne "" || $comment=~/<br>\(�g��\)$/)){
			if($I_Hei_m){$WHm=" width=$I_Wid_m height=$I_Hei_m";}
			if($ICON ne ""){if($ICON=~ /m/){$ICON=~ s/m//; $mICO=$mas_m[$ICON];}else{$mICO=$ico3[$ICON];}}
			elsif($Icon && $comment=~/<br>\(�g��\)$/){$mICO="$Ico_km";}
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
# [�V���L���\��]
# -> �V���L����\������(n_w_)
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
<center><table width=90\%><tr><th bgcolor=$ttb>$new_t���Ԉȓ��ɓ��e���ꂽ�V���L��</th></tr></table><br></center>
<ul>[ �V���L���S$total��($Pg-$Pg2 ��\\��) ]�@
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
if($new_su){$SL1="�V����"; $SL2="<a href=\"$cgi_f?mode=n_w&s=0&no=$no$pp\">�Â���</a>";}
else{$SL1="<a href=\"$cgi_f?mode=n_w&s=1&no=$no$pp\">�V����</a>"; $SL2="�Â���";}
print"$Plink<br>[ $SL1 / $SL2 ] ���\\�[�g���@�ύX</ul><center>";
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
	if($Bl){print"$Bl���O��$new_s��$Ble\n";}
	if($Nl){if($Bl){print"| ";} print"$Nl����$new_s����$Nle\n";}
	print"</b><ul>( �y�[�W�ړ� / $Plink )</ul></ul><br>\n";
}else{print"<br>�V���L���͂���܂���B<br><br>\n";}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�V�K���e]
# -> �V�K���e�̃t�H�[����\������(new_)
#
sub new_ {
if($topok==0 && $FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}
&hed_("Write New Message","1");
print"<center><table width=90\%><tr><th bgcolor=$ttb>";
if($TrON){$T01="�c���[�@";} if($TpON){$T02="�g�s�b�N�@";} if($ThON){$T03="�X���b�h�@";}
print"$T01$T02$T03�̐V�K�쐬</th></tr></table></center>\n";
&forms_;
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���O�������ݏ���]
# -> ���O�ɋL������������(wri_)
#
sub wri_ {
if($s_ret && $P ne "$s_pas"){&er_("�p�X���[�h���Ⴂ�܂�!");}
if($KLOG){&er_("�ߋ����O�ɂ͏������݂ł��܂���!");}
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
	if($AgSg){if($FORM{"AgSg"}){$HTML.="�L���\\�[�g:�グ��(age)";}else{$HTML.="�L���\\�[�g:������(sage)";}}
	print<<"_PV_";
<center><table width=95\%><tr><th bgcolor=$ttb>�v���r���[</th></tr></table><br>
$HTML
<form action="$cgi_f" method="$met"$FORM_E>
<input type=submit value="���M O K"$fm> / <b>[<a href="#F">��������</a>]</b>
<br><br><a name="F">
<table width=90\%><tr><th bgcolor=$ttb>�� �������� ��</th></tr></table></a></center>
_PV_
	&forms_($H);
	&foot_;
}
if($FORM{'URL'}){
	($KURL,$Ag) = split(/::/,$FORM{'URL'});
	$comment.="<br><br>(�g��)";
}
if($UID){
	if($Ag){$pUID=$Ag;}else{&get_("I");}
	if($pUID eq "n"){&er_("�u���E�U��cookie�@�\\��OFF�ł͓��e�s�B�Ή��u���E�U�ɂ��邩�AON�ɂ��Ă�������!");}
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
$oya=0; @new=(); $SeMail=""; $WR=0; $R=~ s/:/�F/g; $SIZE=0;
$txt=~ s/\:/�F/g; $sel=~ s/\:/�F/g; $txt=~ s/\|\|/�b�b/g; $sel=~ s/\|\|/�b�b/g; 
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
		if($name eq $na && $comment eq $com){&er_("�������e�͑��M�s��!","1");}
		if($FORM{'N'} eq $nam){	push(@r_data,$new_); $oya=1; $resres=1;}
		if($ty == 0 && $nam eq "$type"){
			if($i_mode && $ico){$SIZE+=-s "$i_dir/$ico";}
			if($sml==2 || $sml==1){if($SeMail !~ /$mail/){if($q_mail){$SeMail.=" $mail";}else{$SeMail.=",$mail";}}}
			$new_line="$lines[$_]";
			if($he_tp){&cryma_($de); if($ok eq "n"){&er_("�g�s�b�N����҂����ԐM�ł��܂���!","1");}}
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
			if($he_tp){&cryma_($de); if($ok eq "n"){&er_("�g�s�b�N����҂����ԐM�ł��܂���!","1");}}
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
		if($name eq $na && $comment eq $com){ &er_("�������e�͑��M�s��!","1"); }
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
if($SIZE && $max_or < int($SIZE/1024)){&er_("���x�t�@�C���T�C�Y�𒴂����̂ŁA�t�@�C���A�b�v�ł��܂���!","1");}
if($type==0 || $oya==0){unshift(@new,$new_);}
elsif($oya){unshift(@new,"$namber<><><><><><><><><>$namber<><><><><>\n");}

open(LOG,">$log") || &er_("Can't write $log","1");
print LOG @new;
close(LOG);
if($i_mode){&get_("M"); &set_("M");}
if($klog_s && @KLOG){&log_;}
if(-e $lockf){rmdir($lockf);}
if($t_mail || $o_mail){&mail_;}
if($KURL){&ktai("��������","$KURL");}
if($H eq "F" && $tpend && $type){$FORM{"namber"}=$type; $space=0; &all2;}
}
#--------------------------------------------------------------------------------------------------------------------
# [�L���ꊇ�폜]
# -> �L���t�H�[�}�b�g�������Ȃ�(s_d_)
#
sub s_d_ {
if($s_ret && $P ne "$s_pas"){&er_("�p�X���[�h���Ⴂ�܂�!");}
if($FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}

open(DB,">$log");
print DB "";
close(DB);
$msg="<h3>�t�H�[�}�b�g����</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [������]
# -> �ȈՃw���v��\������(man_)
#
sub man_ {
&hed_("Help");
if($TrON){$Tr=" �c���[ ";}else{$Tr="";}
if($TpON){$Tp=" �g�s�b�N ";}else{$Tp="";}
if($ThON){$Th=" �X���b�h ";}else{$Th="";}
print <<"_HTML_";
<center><table width=95\%><tr><th bgcolor="$ttb">$title �}�j���A��</th></tr>
<tr><td bgcolor="$k_back">
�� ��{����/�g�p���@<ul>
<li><b>�d�q�f����(BBS)�ɂ���</b>
<ul><u>�d�q�f����(BBS)�Ƃ́A�C���^�[�l�b�g��ŕs���葽���Ɍ��J����Ă�����̔����̏�ł��B</u><ul>
<li>���ӔC�Ȕ�����A���l�̈����E�l���Ȃǂ́A��������ł͂����܂���B
<li>���̂悤�ȋL�q���������ꍇ�A�Ǘ��Ҍ����ɂ��\\���Ȃ��폜����A�R��ׂ����u���Ƃ��܂��B</ul></ul><br>
<li><b>����BBS�̋L���\\���`�Ԃɂ���</b>
<ul><u>����BBS��$Tr$Tp$Th�\\���^��BBS�ł��B</u><ul>
_HTML_
if($Tr){
	print"<li>[�c���[] ...�L����؂̎}������̂悤�ɕ\\�����܂��B�b�̗��ꂪ������Ղ��̂������ł��B<br>\n";
	print"�{��/�ԐM�������L���^�C�g�����N���b�N���܂��B$all_i ���N���b�N����ƃc���[���ꊇ�\\�����܂��B<br>\n";
}
if($Tp){
	print"<li>[�g�s�b�N] ...�L����b�育�Ƃɕ\\�����܂��B�ЂƂ̘b��̑����̋L�����X���[�Y�ɓǂގ����ł��܂��B<br>\n";
	print"�{��/�ԐM�������g�s�b�N(�b��)�^�C�g�����N���b�N���܂��B\n";
}
if($Th){
	print"<li>[�X���b�h] ...�ŏ�����L�����e��\\�����܂��B��x�ɑ����̘b��ɖڂ�ʂ����Ƃ��ł��܂��B<br>\n";
	print"�����\\����$alk_su���̃X���b�h(�b��)�Ƃ��ꂼ��̍ŐV$alk_rm���̕ԐM�L�����{���ł��܂��B";
}
print <<"_HTML_";
</ul></ul><br>
<li><b>�L���̓��e���@�ɂ���</b><ul>
<li><u>�V�����b��𓊍e����ɂ�...</u><br>�㕔/�������j���[�ɂ��� [�V�K�쐬] ���N���b�N���āA�K�v�ȏ�����͂��Ă��������B
<li><u>���ɓ��e����Ă���L���ɁA�ԐM�L���𓊍e����ɂ�...</u><br>�ԐM�������L����\\���� [�ԐM] ���N���b�N���āA
�K�v�ȏ�����͂��Ă��������B</ul><br>
<li><b>���̑��̃��j���[�ɂ���</b><ul>
<li>[�V���L��] ���N���b�N�����$new_t���ԓ��ɓ��e���ꂽ�L���𒊏o���ĉ{���ł��܂��B
<li>[����] ���N���b�N����ƃ��O���̋L�����L�[���[�h�����猟���ł��܂��B
_HTML_
if($M_Rank){print"<li>[���������N] ���N���b�N����Ɩ��O�����ɏW�v���ꂽ���e�񐔂̃����L���O��\\�����܂��B\n";}
if($i_mode){print"<li>[�t�@�C���ꗗ] ���N���b�N����Ɠ��e�L���ɓY�t���ꂽ�t�@�C���݂̂��{���ł��܂��B\n";}
if($klog_s){print"<li>[�ߋ����O] ���N���b�N����Ɖߋ��̘b����{���ł��܂��B�ߋ����O�̌����� [����] ����s�Ȃ��܂��B\n";}
print <<"_HTML_";
</ul><br><li><b>����BBS�̋@�\\�ɂ���</b><ul>
<li>�b���$max���܂ŕێ����A�����b����̋L���ɂ͕ԐM���ł��܂��B<br>
�b�肪$max���𒴂����ꍇ�A�X�V�������Â��b�肩��
_HTML_
if($klog_s){print" [�ߋ����O] �֕ۑ�����܂��B�ԐM�͂ł��܂���B\n";}else{print"�폜����܂��B\n";}
if($r_max){print"<br>�܂��A�e�b�薈�̕ԐM���x���́A$r_max���ł��B����ȏ�͕ԐM�ł��܂���B";}
if($end_f && $end_c==0){print"<li>�b�肪 $end_ok �ɂȂ������A$end_ok BOX ���`�F�b�N���ē��e���Ă��������B\n";}
elsif($end_c && $end_f){print"<li>�b�肪 $end_ok �ɂȂ������A���̎|�����m�点�������B�Ǘ��҂��`�F�b�N���܂��B\n";}
if($UID){
	print"<li>���e�҂ɂ͌ʂ�ID�����s����܂�(�����_���Ȕ��p�p��8����)�B���l�ɐ��肷�܂����Ƃ�h���܂��B<br>\n";
	print"���̏ꍇ�A�u���E�U��cookie�� ON �łȂ���Γ��e�ł��܂���(�u���E�U�̏����ݒ�ł�ON�ɂȂ��Ă��܂�)�B\n";
}
if($SPAM){
	print"<li>���[���A�h���X�������W�\\�t�g�΍�̂��߁A���[�������N�� $SPAM �Ƃ����������t�����ĕ\\�����Ă��܂��B<br>\n";
	print"���[���𑗂�ۂ� $SPAM �Ƃ�����������폜���Ă��������B\n";
}
if($i_mode){
	print"<li>���[�J��(������PC��)�ɂ���$max_fs\KB�ȓ��̃t�@�C�����A�b�v���[�h���邱�Ƃ��ł��܂��B<br>\n";
	print"�ڂ����͓��e�̍ۂ̐������Q�Ƃ��Ă��������B\n";
}
print <<"_HTML_";
<li>$new_i\...$new_t���ԓ��ɓ��e���ꂽ�b��/�L�� $up_i_\...$new_t���ԓ��ɍX�V���ꂽ�b�� $hed_i\...���L�ȊO�̘b��/�L��
<li>cookie�ɑΉ����Ă��܂��B����BBS�Ɋւ���cookie���폜���邱�Ƃ��ł��܂��B
��[<a href=\"$cgi_f?mode=cookdel\" target="_blank">cookie�̍폜</a>]<br>
cookie...�u���E�U�����͓��e��ۑ����Ă����@�\\�ł��B�ʂ̃T�C�g�ŗ��p����邱�Ƃ͒ʏ킠��܂���B
<li>�L�����e�̍� �폜�L�[(�C�ӂ̃p�X���[�h) ����͂��邱�Ƃɂ���āA�����̓��e�L���̕ҏW/�폜���ł��܂��B
</ul></ul><hr>
�� �������ލۂ̒���
$atcom
</td></tr></table></center>
_HTML_
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�w�b�_�\��]
# -> HTML�w�b�_�̐���(hed_)
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
	if($pUID eq "n"){$pUID="�����s";}
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
<!--�w�b�_�L���^�O�}���ʒu��-->

<!--�������܂�-->
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
if($klog_s){$klog_link="<td><a href=\"$srch?mode=log&no=$no$pp\">�ߋ����O</a></td>\n";}
if($M_Rank){$rank_link="<td$T6><a href=\"$cgi_f?mode=ran&no=$no$pp\">���������N</a></td>\n";}
if($topok){$New_link="<td$T3><a href=\"$cgi_f?mode=new&no=$no$pp\">�V�K�쐬</a></td>\n";}
if($TrON){$TrL="<td$T5><a href=\"$cgi_f?H=T&no=$no$pp$Wf\">�c���[�\\��</a></td>\n";}
if($TpON){$TpL="<td$T7><a href=\"$cgi_f?H=F&no=$no$pp$Wf\">�g�s�b�N�\\��</a></td>\n";}
if($ThON){$ThL="<td$T4><a href=\"$cgi_f?mode=alk&no=$no$pp$Wf\">�X���b�h�\\��</a></td>\n";}
if($i_mode){$FiL="<td$T8><a href=\"$cgi_f?mode=f_a&no=$no$pp\">�t�@�C���ꗗ</a></td>\n";}
$HEDF= <<"_HTML_";
<p><table border=1 cellspacing=0 cellpadding=0 width=100\% bordercolor=$ttb><tr align=center bgcolor="$k_back">
<td><a href="$backurl">HOME</a></td>
<td$T1><a href="$cgi_f?mode=man&no=$no$pp">HELP</a></td>
$New_link<td$T2><a href="$cgi_f?mode=n_w&no=$no$pp">�V���L��</a></td>
$TrL$ThL$TpL$rank_link$FiL<td><a href="$srch?no=$no$pp">����</a></td>
$klog_link
</td></tr></table></p>
_HTML_
if($KLOG){print"<br>(���� �ߋ����O$KLOG ��\\����)";}
print"$HEDF";
if($cou){&con_;} print"</center>";
}
#--------------------------------------------------------------------------------------------------------------------
# [�t�b�^�\��]
# -> HTML�t�b�^�̐���(foot_)
#
sub foot_ {
print"<div align=right><form action=\"$cgi_f\" method=$met>$nf$pf\n";
if($i_mode || $mas_c){print"Mode/<select name=mode><option value=del>�ʏ�Ǘ�<option value=ent>�\\������</select>�@\n";}
else{print"<input type=hidden name=mode value=del>\n";}
print <<"_HTML_";
Pass/<input type=password name=pass size=6$ff><input type=submit value=\"�Ǘ��p\"$fm></form></div><br>
<center>$HEDF
<!--���쌠�\\�� �폜�s��-->
- <a href="http://www.cj-c.com/" target=$TGT>Child Tree</a> -<br>
<!--�t�b�^�L���^�O�}���ʒu��-->

<!--�������܂�-->
</center>
</body></html>
_HTML_
exit;
}
#--------------------------------------------------------------------------------------------------------------------
# [�t�H�[���f�R�[�h]
# -> �t�H�[�����͓��e������(d_code_)
#
sub d_code_ {
$file="";
if($ENV{'CONTENT_LENGTH'} && $ENV{'CONTENT_TYPE'} =~ /^multipart\/form-data/){
	$buf=""; $read_data="";
	$remain=$ENV{'CONTENT_LENGTH'};
	binmode(STDIN);
	while($remain){
		$remain-=($read_length=sysread(STDIN, $buf, $remain));
		exit if $read_length == 0; # �ڑ����r���Ő؂ꂽ
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
						&er_("�u$NW[$_]�v�͎g�p�ł��܂���!");
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
					&er_("�u$NW[$_]�v�͎g�p�ł��܂���!");
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
# [cookie���s]
# -> cookie�𔭍s����(set_)
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
# [cookie�擾]
# -> cookie���擾����(get_)
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
# [���Ԑݒ�]
# -> ���Ԃ�ݒ肷��(time_)
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
# [�Ǘ��p�y�[�W]
# -> �Ǘ����[�h��\������(del_)
#
sub del_ {
if($FORM{'pass'} ne "$pass"){ &er_("�p�X���[�h���Ⴂ�܂�!"); }
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
if($FORM{"mode2"} eq "Backup"){&backup_; $msg="<h3>�o�b�N�A�b�v����</h3>"; @lines=();}
elsif($FORM{"mode2"} =~/\d/){
	open(NO,">$c_f") || &er_("Can't write $c_f","1");
	print NO $FORM{"mode2"};
	close(NO);
	$msg="<h3>�J�E���^�l�ҏW����</h3>";
}elsif($FORM{"mode2"} eq "LockOff"){
	$msg="<h3>���b�N��������</h3>";
	if(-e $lockf){rmdir($lockf); $msg.="($lockf����)";}else{$msg.="($lockf����)";}
	if(-e $cloc){rmdir($cloc);   $msg.="($cloc����)"; }else{$msg.="($cloc����)";}
}
$total=@NEW; $NS=$RS+$total;
$page_=int(($total-1)/$a_max);
if(-s $log){$l_size=int((-s $log)/1024);}else{$l_size=0;}
if($topok==0){$NewMsg="<li><a href=\"$cgi_f?mode=new&no=$no&pass=$FORM{'pass'}$pp\">�Ǘ��p�V�K�쐬</a>\n";}
if($i_mode || $mas_c){
	if($FSize){$FSize=int($FSize/1024); $FileSize="<br>�A�b�v�t�@�C�����v�T�C�Y�F$FSize\KB";}else{$FSize=0;}
	$FP ="<form action=\"$cgi_f\" method=$met target=_blank>\n";
	$FP.="<b>[�摜/�L���\\������]</b><br><input type=hidden name=mode value=ent>$nf$pf\n";
	$FP.="<input type=hidden name=pass value=$FORM{'pass'}><input type=submit value=\"�\\�����V�X�e��\"></form>\n";
}
if($bup){$BUL="/�o�b�N�A�b�v";}
print <<"_HTML_";
<center><table width=90\%>
<tr><td align=right colspan=2><a href="http://www.cj-c.com/help/cbbs.html" target="_blank">�Ǘ����[�h�w���v</a></td></tr>
<tr><th bgcolor="$ttb" colspan=2>�Ǘ����[�h</th><tr><td>
���݂̃��O�̃T�C�Y�F$l_size\KB�@�L�����F$NS(�e/$total ���X/$RS)$FileSize<ul>
<li>�L����ҏW�������ꍇ�A���̋L���̃^�C�g�����N���b�N�B
<li>�폜�������L���Ƀ`�F�b�N�����u�폜�v�{�^���������ĉ������B
<li>�L��No�̉���IP�A�h���X���N���b�N����Ɣr��IP���[�h�֏��𑗂�܂��B
<li>�c���[�폜������ƃc���[���Ռ`�����������܂��B
<li>�L���폜�́A���̋L���ɑ΂��郌�X���Ȃ��ꍇ�͊��S�폜�ɂȂ�܂��B<br>
���̋L���ɑ΂��郌�X������ꍇ�͊��S�ɍ폜���ꂸ�폜�L���ɂȂ�܂��B
<li>�폜�L���́u�L�����S�폜�v���`�F�b�N����Ɗ��S�ɏ����܂��B
<li><a href=#FMT>���b�N����/���O������/�t���[�t�H�[���C��/���O�R���o�[�g$BUL</a>
$NewMsg
</ul></td><td>
<form action="$cgi_f" method=$met target="_blank">$nf$pf
<input type=hidden name=mode value="Den"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[�r��IP/�֎~�����ǉ�]</b><br>
<input type=submit value="�r���ݒ�ǉ�"></form>
$FP
_HTML_
if($cou){
	open(NO,"$c_f") || &er_("Can't open $c_f");
	$cnt = <NO>;
	close(NO);
	print <<"_BUP_";
<form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value="del"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[�J�E���^�l�ҏW]</b><br>
�J�E���g��/<input type=text name=mode2 value=$cnt size=7><input type=submit value="�ҏW"></form>
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
$Plink="�y�[�W�ړ� / $Bl\&lt;\&lt\;$Ble\n";
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
<ul><input type=radio name="kiji" value="$namber">�c���[�폜<br><input type=checkbox name="del" value="$namber">
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
<center><input type=checkbox name=kiji value=A>�L�����S�폜<br>
<input type=submit value=" �� �� ">
<input type=reset value="���Z�b�g"></form>
<b>
_DEL_
if($Bl){print"$Bl���O��$a_max��$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl����$a_max����$Nle\n";}
print <<"_HTML_";
</b><br><br>$Plink
<SCRIPT language="JavaScript">
<!--
function Link(url) {
	if(confirm("�{���Ɏ��s���Ă�OK�ł���?\\n(���s����Ɠ��e�͌��ɖ߂��܂���!)")){location.href=url;}
	else{location.href="#FMT";}
}
//-->
</SCRIPT>
<a name=FMT><hr width="95\%"></a>
*JavaScript �� ON�ɂ��Ă�������*
<table border=1 bordercolor=$ttb width=90\%>
<tr><td colspan=2><form action="$cgi_f" method="$met"><b>[���b�N�t�@�C���̉���(�폜)]</b><ul>
<input type=button value="���b�N����" onClick="Link('$cgi_f?mode=del&pass=$FORM{"pass"}&mode2=LockOff&no=$no$pp')">
<li>���b�N�t�@�C�����ǂ����Ă��폜����Ȃ��ꍇ�Ɏ����Ă��������B��肪�����ꍇ�͂��܂�g��Ȃ��ŉ�����<ul>
_HTML_
if(-e $lockf){print"<li>���C�����O($lockf):���b�N��\n";}
if(-e $cloc){print"<li>�J�E���^���O($cloc):���b�N��\n";}
print<<"_HTML_";
</ul><li>���b�N���̃��O�������Ă��A���[�U�����쒆�̏ꍇ������܂��B���΂炭�l�q�����Ď��s���Ă��������B
</ul></form></td></tr>
<tr valign="top"><td>
<form action="$cgi_f" method=$met>
<b>[���O�t�H�[�}�b�g(������)]</b>
<ul><input type=button value="�t�H�[�}�b�g" onClick="Link('$cgi_f?mode=s_d&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>�t�@�C���A�b�v�@�\\��ON�̏ꍇ�A�\\�������[�h�Ńt�@�C�������ׂč폜���s�Ȃ��Ă�������!
</ul></form>
</td><td>
<form action="$cgi_f" method=$met>
<b>[�t���[�t�H�[���C��]</b>
<ul><input type=button value="�C������" onClick="Link('$cgi_f?mode=ffs&mo=1&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>�����R�[�h��̕s��C�����܂��B�����������N�����ꍇ�͕ҏW�ŏC�����Ă��������B<br>
<li>�O�̂��߃o�b�N�A�b�v������Ă������Ƃ������߂��܂�(v7.0��������t���[�t�H�[�����g�p\���Ă���ꍇ)
</ul></form>
</td></tr><tr valign="top"><td>
<form action="$cgi_f" method=$met>
<b>[���O�R���o�[�g]</b>
<ul><input type=button value="I-BOARD" onClick="Link('$cgi_f?mode=ffs&mo=I-BOARD&pass=$FORM{"pass"}&no=$no$pp')"> /
<input type=button value="UPP-BOARD" onClick="Link('$cgi_f?mode=ffs&mo=UPP-BOARD&pass=$FORM{"pass"}&no=$no$pp')"><br>
<li>I-BOARD�V���[�Y �������� UPP-BOARD �̃��O�� ChildTree �p�ɃR���o�[�g���܂��B<br>
<li>�R���o�[�g����ƌ��ɖ߂��̂͑�ςȂ̂Œ���! �{�^�����ԈႦ�Ȃ���!<br>
<li>�L���͂��ׂĐV���L�������ƂȂ�܂��B<br>
<li>�R���o�[�g�Ώۃ��O:[$log]<br>
</ul></form>
</td><td>
_HTML_
if($bup){
	if(-e $bup_f){
		$bl=(-M $bup_f); $bh=sprintf("%.1f",24*$bl); $bl=sprintf("%.2f",$bl); $bs=int((-s $bup_f)/1024);
		$bc="����($bs\KB / $bl��(��$bh����)�O)"; $Nb=$bup-$bl; $Nh=sprintf("%.1f",$Nb*24);
	}else{$bc="����";}
	print <<"_BUP_";
<form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value="del"><input type=hidden name=pass value="$FORM{'pass'}">
<b>[�o�b�N�A�b�v]</b>
<ul><input type=button value="���O���C��" onClick="Link('$cgi_f?mode=bma&pass=$FORM{"pass"}&no=$no$pp')">
/ <input type=submit value="Backup" name=mode2><br>
<li>[Backup]�{�^�����N���b�N����ƌ��݂̃��O���o�b�N�A�b�v���܂��B
<li>�o�b�N�A�b�v�@\�\\���g�p���Ă���l�̂ݏC���\\�ł��B<br>
<li>�o�b�N�A�b�v$bc
<li>���̃o�b�N�A�b�v�� $Nb��(��$Nh����)��
</ul></form>
_BUP_
}
print"</td></tr></table></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�L���ҏW]
# -> �L���ҏW�̃t�H�[�����o��(hen_)
#
sub hen_ {
if($KLOG){&er_("�ߋ����O�͕ҏW�s��");}
if($mo eq ""){
	if($FORM{'del'} eq ""){ &er_("�o�^No ��������!"); }
	if($delkey eq ""){ &er_("�폜�L�[ ��������!"); }
	$kiji=$FORM{'del'};
}elsif($mo==1){if($FORM{'pass'} ne "$pass"){ &er_("�p�X���[�h���Ⴂ�܂�!"); }}
open(DB,"$log");
while ($line=<DB>) {
	($namber,$d,$name,$email,$d_may,$comment,$url,
		$s,$end,$t,$de,$i,$ti,$sml) = split(/<>/,$line);
	if($d eq ""){next;}
	if($kiji eq "$namber"){
		if($mo eq ""){
			if($de eq "") { &er_("���̋L���͍폜�L�[������܂���!"); }
			&cryma_($de);
			if($delkey eq "$pass"){$ok="m";}
			if($ok eq "n"){ &er_("�p�X���[�h���Ⴂ�܂�!"); }
			$hen_l="$cgi_f?no=$no$pp"; $Lcom="";
		}else{$hen_l="$cgi_f?mode=del&pass=$FORM{'pass'}&no=$no$pp"; $Lcom="�Ǘ����[�h��";}
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
��&gt; �֘A���郌�X�L�������[���Ŏ�M���܂���?<select name=send>
<option value=0>NO
<option value=1$Y>YES
</select> /
�A�h���X<select name=pub>
<option value=0>����J
<option value=1$Pch>���J
</select></td></tr>
_MAIL_
		}
		if($tag){$comment=~ s/</\&lt\;/g; $comment=~ s/>/\&gt\;/g;}
		($Ip,$ico,$Ent,$fimg,$TXT,$SEL,$R)=split(/:/,$i);
		print <<"_HTML_";
<center><table width=90\%><tr bgcolor=$ttb><th>�L��No[$namber] �̕ҏW</th></tr></table>
$msg</center>
<ul><form action="$cgi_f" method="$met">$nf$pf
��<a href="$hen_l"> $Lcom�߂�</a><br><br>
<input type=hidden name=pass value="$FORM{'pass'}">
<input type=hidden name=mode value=h_w>
<input type=hidden name=namber value=$namber><input type=hidden name=mo value=$mo>
<table>
<tr><td bgcolor=$ttb>Name</td><td>/<input type=text name="name" value="$name" size=20></td></tr>
<tr><td bgcolor=$ttb>E-Mail</td><td>/<input type=text name="email" value="$email" size=40></td></tr>
$Mbox
<tr><td bgcolor=$ttb>Title</td><td>/<input type=text name="d_may" size=40 value="$d_may"></td></tr>
<tr><td bgcolor=$ttb>URL</td><td>/<input type=text name="url" value="http://$url" size=60></td></tr>
<tr><td colspan=2 bgcolor=$ttb>Comment��
�ʏ탂�[�h/<input type=radio name=pre value=0$T>
�}�\\���[�h/<input type=radio name=pre value=1$Z>
(�K���ɉ��s�����ĉ�����)<br>
<textarea name="comment" rows=15 cols=80 wrap=$wrap>$comment</textarea></td></tr>
_HTML_
		($ICON,$ICO,$font,$hr)=split(/\|/,$TXT);
		($txt,$sel,$yobi)=split(/\|\|/,$SEL);
		if($font){
			print "<tr><td bgcolor=$ttb>�����F</td><td>/\n";
			foreach (0 .. $#fonts) {
				if($font eq ""){$font="$fonts[0]";}
				print"<input type=radio name=font value=\"";
				if($font eq "$fonts[$_]"){print"$fonts[$_]\" checked><font color=$fonts[$_]>��</font>\n";}
				else{print"$fonts[$_]\"><font color=$fonts[$_]>��</font>\n";}
			}
			print"</td></tr>";
		}
		if($hr){
			print"<tr><td bgcolor=$ttb>�g���F</td><td>/\n";
			foreach (0 .. $#hr) {
				if($hr eq ""){$cr="$hr[0]";}
				print "<input type=radio name=hr value=\"";
				if($hr eq "$hr[$_]"){print"$hr[$_]\" checked><font color=$hr[$_]>��</font>\n";}
				else{print"$hr[$_]\"><font color=$hr[$_]>��</font>\n";}
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
			print"</select> <small>(�摜��I��/";
			print"<a href='$cgi_f?mode=img&no=$no$pp' target=_blank>�T���v���ꗗ</a>)</small></td></tr>\n";
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
</td></tr><tr><td colspan=2 align=right><input type=submit value=" �� �W ">
<input type=reset value=���Z�b�g></td></tr></table></form></ul><hr width="95\%">
_HTML_
		if($i_mode){
			if($ico){
				&size;
				print<<"_DEL_";
<center>
�E��������t�@�C���폜�ł��܂��B<br><br>
<table width=90\%>$Pr</table>
<form action="$cgi_f">$nf$pf
<input type=hidden name=mode value=h_w><input type=hidden name=pass value=$FORM{"pass"}>
<input type=hidden name=IMD value=$namber><input type=submit value="�t�@�C�����폜">
</form><hr width="95\%"></center>
_DEL_
			}elsif($s==0 || ($s && $ResUp)){
				print<<"_DEL_";
<ul>
�E��������t�@�C���A�b�v�ł��܂��B<br>
<form action="$cgi_f" method=$met enctype="multipart/form-data">$nf$pf
File / <input type=file name=ups size=60$ff>�@<input type=submit value="���M">
<ul>�A�b�v�\\�g���q=&gt;
_DEL_
				foreach (0..$#exn) {
					if($exi[$I] eq "img"){$EX="<b>$exn[$_]</b>";}else{$EX="$exn[$_]";}
					print"/$EX"; $I++;
				}
				print<<"_DEL_";
<br>
1) �����̊g���q�͉摜�Ƃ��ĔF������܂��B<br>
2) �摜�͏�����Ԃŏk���T�C�Y$H2�~$W2�s�N�Z���ȉ��ŕ\\������܂��B<br>
3) �����t�@�C��������A�܂��̓t�@�C�������s�K�؂ȏꍇ�A<br>
�@�@�t�@�C�����������ύX����܂��B<br>
4) �A�b�v�\\�t�@�C���T�C�Y��1��<B>$max_fs\KB</B>(1KB=1024Bytes)�܂łł��B<br></ul>
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
# [�p�X���[�h�Í���]
# -> �p�X���[�h���Í�������(cry_)
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
# [�p�X���[�h���]
# -> �p�X���[�h���Í������}�b�`���O(cryma_)
#
sub cryma_ {
if($de =~ /^\$1\$/){ $crptkey=3; }else{ $crptkey=0; }
$ok = "n";
if(crypt($FORM{'delkey'}, substr($de,$crptkey,2)) eq $de){$ok = "y";}
}
#--------------------------------------------------------------------------------------------------------------------
# [�폜����]
# -> �L���̍폜����(key_)
#
sub key_ {
if($mo eq ""){
	if($FORM{'del'} eq ""){ &er_("�o�^No ��������!"); }
	if($delkey eq "") { &er_("�폜�L�[ ��������!"); }
}elsif($mo==1){if($FORM{'pass'} ne "$pass"){ &er_("�p�X���[�h���Ⴂ�܂�!"); }}
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
				if($de eq "" && $dok==0){&er_("�L���ɍ폜�L�[������܂���!","1");}
				&cryma_($de);
				if($delkey eq "$pass"){$ok="m";}
				if($ok eq "n" && $dok==0){&er_("�p�X���[�h���Ⴂ�܂�!","1");}
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
		if($mo || $ok eq "m"){$Dm="(�Ǘ���)";}else{$Dm="(���e��)";}
		$mens = "$nam<>$d<><><>�i�폜�j<>���̋L����$Dm�폜����܂���<><>$sp<><>$ty<><><>$ti<><>";
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
if($FORM{'URL'}){&ktai("�폜","$FORM{'URL'}");}
if($mo){$msg="<h3>�폜����</h3>"; &del_;}else{$mode="";}
}
#--------------------------------------------------------------------------------------------------------------------
# [�ҏW�L���u��]
# -> �ҏW���e��u��������(h_w_)
#
sub h_w_ {
if($KLOG){&er_("�ߋ����O�͕ҏW�s��");}
if($FORM{'pass'} ne "$pass" && $mo){&er_("�p�X���[�h���Ⴂ�܂�!");}
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
			if($ok eq "n"){ &er_("�p�X���[�h���Ⴂ�܂�!","1"); }
		}
		if($EStmp){
			&time_("");
			$EditCom="$date �ҏW";
			if($mo || $ok eq "m"){$EditCom.="(�Ǘ���)";}else{$EditCom.="(���e��)";}
			if($comment !~ /([0-9][0-9]):([0-9][0-9]):([0-9][0-9]) �ҏW/){$EditCom.="<br><br>";}else{$EditCom.="<br>";}
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
				if($ok eq "n"){ &er_("�p�X���[�h���Ⴂ�܂�!","1"); }
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
				if($ok eq "n"){ &er_("�p�X���[�h���Ⴂ�܂�!","1"); }
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
				if($ok eq "n"){ &er_("�p�X���[�h���Ⴂ�܂�!","1"); }
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
if($SIZE && $max_or < int($SIZE/1024)){&er_("���̃t�@�C���͑��t�@�C���T�C�Y�𒴂��邽�߃A�b�v�ł��܂���!","1");}
if($flag==0){&er_("���̋L��No�͑��݂��܂���!","1");}
if($flag==1){
	open (DB,">$log");
	print DB @new;
	close(DB);
}
if(-e $lockf){rmdir($lockf);}
if($FORM{'URL'}){&ktai("�ҏW","$FORM{'URL'}");}
if(@E_ || @I_ || $FORM{'UP'}){
	if($mo && (@E_ || @I_)){&ent_;}
	else{
		if(@I_){$msg="<h3>�t�@�C���폜</h3>"; $FORM{"del"}=$I_[0];}
		elsif($FORM{'UP'}){$msg="<h3>�t�@�C���A�b�v����</h3>$Henko"; if($mo){$kiji=$FORM{'UP'};}else{$FORM{"del"}=$FORM{'UP'};}}
		$delkey=$FORM{"pass"}; &hen_;
	}
}elsif($mo){$msg="<h3>�ҏW����</h3>"; &del_;}
else{$msg="<h3>�ȉ��̂悤�ɕҏW����</h3>"; $delkey=$FORM{"pass"}; $FORM{"del"}=$namber; &hen_;}
}
#--------------------------------------------------------------------------------------------------------------------
# [�r��IP/�֎~�����ǉ�]
# -> �r��IP/�֎~�����ǉ��V�X�e��(Den_)
#
sub Den_ {
if($FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}
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
	$msd="<h3>$Log�֓o�^����</h3>";
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
	$msd="<h3>$Log���폜����</h3>";
}
&hed_("Deny IP/Word Editor");
print<<"_HTML_";
<center><table width=95\%><tr bgcolor="$ttb"><th>�r��IP/�֎~������ݒ胂�[�h</th></tr></table>$msd</center><ul>
<li>�w�肵�������܂܂�Ă���Ƃ��ꂼ��r������܂��B
<li><b>[�r��IP?]</b> IP�A�h���X��4���ō\\������Ă���A�ʏ�4���ڂ��A�N�Z�X���ɕς��܂��B����āA3���ڂ܂ł��w�肵�܂��B<br>
��) 127.0.0.1 ��r���������ꍇ�� 127.0.0. �Ǝw�肷��B192.168.0.1 �� 192.168.0. (*)������IP�͐�΂ɐݒ肵�Ȃ�!
<li><b>[�֎~������?]</b> �g�p���ꂽ���Ȃ���������w�肵�܂��B�啶���������͋�ʂ���܂��B<br>
��) ��`�L����URL���w��B�^�O���J�n�^�O�̈ꕔ &lt;img &lt;font ���B
_HTML_
@Deny=("$IpFile","$NWFile");
@Dcom=("�r��IP","�֎~������");
foreach(0..1){
	if($mo){if($_==0){$mo=~ s/(\d+\.\d+\.\d+\.)(\d+)/$1/;}else{$mo="";}}
	if(-e "$Deny[$_]"){
		open(DB,"$Deny[$_]") || &er_("Can't open $Deny[$_]");
		@deny = <DB>;
		close(DB);
		print<<"_EDIT_";
<hr><b>�� $Dcom[$_]�̒ǉ�</b><ul>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Add:$Deny[$_]">
$Dcom[$_] /<input type=text name=u size=25 value="$mo"> (��/cj-c.com)
<input type=submit value="�� ��">
</form></ul>
<b>�� $Deny[$_] �ɓo�^�ς݂�$Dcom[$_]</b><ul>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Del:$Deny[$_]">
_EDIT_
		foreach(0..$#deny){
			$deny[$_]=~ s/\n//g; $deny[$_]=~ s/</\&lt\;/g; $deny[$_]=~ s/>/\&gt\;/g;
			print"<input type=checkbox name=del value=\"$deny[$_]\">- $deny[$_]<br>\n";
		}
		print"<br><input type=submit value=\"�� ��\"><input type=reset value=\"���Z�b�g\"></form></ul>\n";
	}else{
		print<<"_EDIT_";
<hr><br><b>�� $Dcom[$_]�ݒ������t�@�C���̍쐬</b><ul>
<li>$Dcom[$_]��ݒ肷��t�@�C��($Deny[$_])���Ȃ��̂ŃI�����C���Őݒ肷��ꍇ�A���̃t�@�C�����쐬����K�v������܂��B
<li>����CGI�̂���f�B���N�g���ɍ쐬���܂�(���̃f�B���N�g���̃p�[�~�b�V������777or755 �ł���K�v������܂�)�B
<li>�����ł��܂��쐬�ł��Ȃ��ꍇ�͓����t�@�C����FTP����쐬���Ă�������(�p�[�~�b�V����:666)
<form action="$cgi_f" method=$met><input type=hidden name=mode value=Den>$nf$pf
<input type=hidden name=pass value=$pass><input type=hidden name=m value="Make:$Deny[$_]">
<input type=submit value="$Deny[$_] ���쐬����"></ul>
</form>
_EDIT_
	}
}
print"</ul><hr width=\"95\%\">\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���b�N����]
# -> �t�@�C�����b�N����(lock_)
#
sub lock_ {
$lflag = 0;
foreach(1 .. 5){if(mkdir($_[0], 0755)){$lflag=1; last;}else{sleep(1);}}
if($lflag==0){
	if(-e $_[0]){rmdir($_[0]);}
	&er_("LOCK is BUSY (���b�N��)","1");
}
}
#--------------------------------------------------------------------------------------------------------------------
# [���[���ʒm����]
# -> ���e�ʒm���[������(mail_)
sub mail_ {
$mail_subj = "$title ���e�ʒm";
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
# [URL�������N��]
# -> �R�����g���A�����N�E�����F�ȂǏ���(auto_)
#
sub auto_ {
if($_[0]=~/<\/pre>/){$_[0]=~ s/(>|\n)((&gt;|��|>)[^\n]*)/$1<font color=$res_f>$2<\/font>/g;}
else{$_[0]=~ s/>((&gt;|��|>)[^<]*)/><font color=$res_f>$1<\/font>/g;}
$_[0]=~ s/([^=^\"]|^)((http|ftp|https)\:[\w\.\~\-\/\?\&\+\=\:\@\%\;\#\,\|]+)/$1<a href=$2 target=$TGT>$2<\/a>/g;
$_[0]=~ s/([^\w^\.^\~^\-^\/^\?^\&^\+^\=^\:^\%^\;^\#^\,^\|]+)(No|NO|no|No.|NO.|no.|&gt;&gt;|����|>>)([0-9\,\-]+)/$1<a href=\"$cgi_f?mode=red&namber=$3&no=$no$pp\" target=$TGT>$2$3<\/a>/g;
}
#--------------------------------------------------------------------------------------------------------------------
# [�J�E���^����]
# -> �J�E���g�A�b�v����(con_)
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
# [�G���[�\��]
# -> �G���[�̓��e��\������(er_)
#
sub er_ {
if(-e $lockf && $_[1]==1){rmdir($lockf);}
if(-e $cloc && $_[1]==1){rmdir($cloc);}
if(-e "$i_dir/$file"){unlink("$i_dir/$file");}
if($FORM{"URL"}){
	($KURL,$Ag) = split(/::/,$FORM{'URL'});
	&ktai("ERROR-$_[0]<br>��","$KURL");
}
if($BG eq ""){&hed_("Error");}
print"<hr width=\"90\%\"><center>ERROR-$_[0]</center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�ߋ����O]
# -> �ߋ����O�ւ̏�������(log_)
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
# [�J�E���g�A�b�v]
# -> �ߋ����O�ԍ��̃J�E���g�A�b�v(log_up)
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
# [���O����]
# -> ���O�������������܂�(l_m)
#
sub l_m {
open(DB,">$_[0]") || &er_("Can't make $_[0]");
print DB "";
close(DB);

chmod(0666,"$_[0]");
}
#--------------------------------------------------------------------------------------------------------------------
# [�o�b�N�A�b�v����]
# -> �ȈՃo�b�N�A�b�v����(backup_)
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
# [�C������]
# -> �o�b�N�A�b�v�t�@�C�����l�[������(bma_)
#
sub bma_ {
if($FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}
if(-e $lockf){rmdir($lockf);}
if(-e $bup_f){rename ($bup_f,$log) || &er_("Rename Error");}
else{&er_("�o�b�N�A�b�v���Ȃ��̂ŏC���s�\\�ł�!","1");}
$msg="<h3>�C������</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�X���b�h�\��]
# -> �X���b�h�`���ŋL���̈ꗗ��\������(alk_)
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
		if($txt){$Txt="$TXT_T:[$txt]�@";}else{$Txt="";}
		if($sel){$Sel="$SEL_T:[$sel]�@";}else{$Sel="";}
		if($d_may eq ""){$d{$namber}="����";}else{$d{$namber}=$d_may;}
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
	$com_top.="�� $new_t���Ԉȓ��ɍ쐬���ꂽ�X���b�h�� $new_i �ŕ\\������܂��B<br>\n";
	$com_top.="�� $new_t���Ԉȓ��ɍX�V���ꂽ�X���b�h�� $up_i_ �ŕ\\������܂��B<br>\n";
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
print"</center><a name=list></a><ul>[ �S$total�X���b�h($Pg-$Pg2 �\\��) ]�@\n";
$Plink="$Bl\&lt\;\&lt\;$Ble\n";
$a=0;
for($i=0;$i<=$page_;$i++){
	$af=$page/$alk_su;
	if($i != 0){$Plink.="| ";}
	if($i eq $af){$Plink.="<b>$i</b>\n";}else{$Plink.="<a href=\"$cgi_f?mode=alk&page=$a&no=$no$pp$Wf\">$i</a>\n";}
	$a+=$alk_su;
}
$Plink.="$Nl\&gt\;\&gt\;$Nle";
if($Res_T==1){$OJ1="<a href=\"$cgi_f?mode=alk&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="���e��"; $OJ3="<a href=\"$cgi_f?mode=alk&W=R&no=$no$pp\">���X��</a>";}
elsif($Res_T==2){$OJ1="<a href=\"$cgi_f?mode=alk&W=W&no=$no$pp\">�X�V��</a>"; $OJ2="<a href=\"$cgi_f?mode=alk&W=T&no=$no$pp\">���e��</a>"; $OJ3="���X��";}
else{$OJ1="�X�V��"; $OJ2="<a href=\"$cgi_f?mode=alk&W=T&no=$no$pp\">���e��</a>"; $OJ3="<a href=\"$cgi_f?mode=alk&W=R&no=$no$pp\">���X��</a>";}
print"$Plink<br>[ $OJ1 / $OJ2 / $OJ3 ]���\\�[�g���@�ύX</ul><center>";
if($Top_t){
	print"<table width=\"95\%\" border=1 bordercolor=\"$ttb\"><tr>\n";
	print"<td bgcolor=\"$k_back\"><center><b>�L�����X�g</b> ( )���̐����̓��X��</center>$List</td></tr></table><br>\n";
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
	if($Top_t){print"<a href=\"#list\">���L�����X�g</a>";}
	if($_ ne $page_end){$L_=$_+1; print" / <a href=\"#$L_\">�����̃X���b�h</a>\n";}
	if($_ ne $page){$L_2=$_-1; print" / <a href=\"#$L_2\">����̃X���b�h</a>\n";}
	print"$HTML";
	@RES=split(/\n/,$R{$nam}); $PNO=0;
	@RES=sort(@RES);
	if(@RES){
		$Rn=$alk_rm; $RC=@RES; $Pg=$RC-$alk_rm+1; if($Pg<=0){$Pg=1;}
		print"<hr size=1 color=\"$ttb\">��[�S���X$RC��(ResNo.$Pg-$RC �\\��)]\n";
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
			if($Top_t){print"<hr size=1 color=\"$ttb\"><a href=\"#list\">���L�����X�g</a> /\n";}
			print"���X�L���\\�� ��\n";
			$a=0;
			for($i=0;$i<=$RC_;$i++){
				if($i){$St=$i*$ResHy; $En=$St+$ResHy-1; if($RC+1<=$En){$En=$RC;}}
				else{$En=$ResHy-1; if($RC<$En){$En=$RC;} $St="�e�L��";}
				print"[<a href=\"$cgi_f?mode=res&namber=$nam&rev=$r&page=$a&no=$no$pp\">$St-$En</a>]\n";
				$a+=$ResHy;
			}
			if($Dk){print"<br>($Dk���͍폜�L��)\n";}
		}
	}
	$LinkNo=$nam;
	print"</td></tr></table><br>\n";
}
print"</center><br><hr width=\"95\%\">";
&allfooter("�X���b�h$alk_su��");
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�X���b�h���X�\��]
# -> �X���b�h�̃��X��\�����܂�(res_)
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
if($page){$Pg="$page"; $Pg2="$page_end";}else{$Pg="�e�L��"; $Pg2="$page_end";}
$nl=$page_end+1;
$bl=$page-$ResHy;
if($bl >= 0){$Bl="<a href=\"$cgi_f?mode=res&namber=$FORM{'namber'}&page=$bl&no=$no$pp\">"; $Ble="</a>";}
if($page_end ne $end_data){$Nl="<a href=\"$cgi_f?mode=res&namber=$FORM{'namber'}&page=$nl&no=$no$pp\">"; $Nle="</a>";}
print"<ul>[ �X���b�h���S$total���X($Pg-$Pg2 �\\��) ]�@\n";
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
if($Dk){print"( $Dk���̍폜�L�����\\�� )<br>";}
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
if($TrON){$TrLink="<a href=\"$cgi_f?mode=all&namber=$FORM{'namber'}&space=0&type=0&no=$no$pp\">$all_i ���̃X���b�h���c���[�ňꊇ�\\��</a>";}
print"</center><ul>$TrLink</ul><center><hr width=\"90\%\"><b>\n";
if($bl >= 0){print"$Bl���O�̃��X$ResHy��$Ble\n";}
if($page_end ne $end_data){if($Bl){print"| ";} print"$Nl���̃��X$ResHy����$Nle\n";}
if($mo eq ""){$com="";}
print<<"_F_";
</b><br><br>�X���b�h���y�[�W�ړ� / $Plink<br><br>
<a name=F><table width=90\% align=center>
<tr><th bgcolor=$ttb>���̃X���b�h�ɏ�������</th></tr></table></a></center>
_F_
if($r_max && $total > $r_max){
	print"<center><h3>���X���̌��x�𒴂����̂Ń��X�ł��܂���B</h3>(���X�����x:$r_max ���݂̃��X��:$total)\n";
	print" �� <b><a href=\"$cgi_f?mode=new&no=$no$pp\">[�X���b�h�̐V�K�쐬]</a></b></center>";
}
else{if($En && $end_e){print"<center><h3>$end_ok / �ԐM�s��</h3></center>";}else{&forms_("N");}}
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�����L���O]
# -> ���������L���O���J�E���g����(rank)
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
		if($_!=$#RLv){if($RCo < $SPL){$R="$RLv[$_]($RCo��)"; last;}}
		else{$R="$RLv[$_]($RCo��)"; last;}
	}
}else{$R="$RCo��";}
}
#--------------------------------------------------------------------------------------------------------------------
# [�����N�\��]
# -> ���������L���O��\�����܂�(ran_)
#
sub ran_ {
@R=(); $Mas="";
open(R,"$RLOG") || &er_("Can't open $RLOG");
while (<R>) {
	($Na,$Co,$Em,$Ti)=split(/<>/,$_);
	if(@d_){
		if($FORM{'pass'} ne $pass){&er_("�p�X���[�h���Ⴂ�܂�!");}
		foreach $D (@d_){if($D eq $Na){$_=""; last;}}
		if($_ eq ""){next;}else{push(@R,"$_");}
	}
	$N=0;
	if(@NoRank){foreach(0..$#NoRank){if($Na eq "$NoRank[$_]"){$N=1; last;}}}
	if($N){$Mas.="$Na -&gt\; $Co��<br>\n"; next;}
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
<center><table width=90\%><tr bgcolor=$ttb><th>���������L���O</th></tr></table></center>
<ul>�E�W�v������:$total��
<br>�E�ŏI����������$RDEL���o�߂���Ǝ����I�ɍ폜����܂��B</ul><center>
<form action="$cgi_f" method=$met><input type=hidden name=mode value=ran>$nf$pf
<table><tr><td>
<table><tr><th colspan=6>BEST 10</th></tr><tr bgcolor=$ttb>
<th>����</th><th>���O</th><th>������</th><th>�ŏI������</th><th>�O���t</th><th>*</th></tr>
_T_
$J=0; $rank1=0; $rank2=1; $count_tmp=0; $K=0;
foreach (sort { ($Co{$b} <=> $Co{$a}) || ($a cmp $b)} keys(%Co)) {
	($Co{$_} == $count_tmp) || ($rank1 = $rank2);
	$P{$_}=($Co{$_} / $total) * 100;
	$P{$_}=sprintf("%2.1f",$P{$_});
	if($rank1 > 10 && $J==0){
		$J=1;
		print"<tr><td align=center colspan=6><br><b>11�ʁ`$RBEST��</b></td></tr><tr bgcolor=$ttb>\n";
		print"<th>����</th><th>���O</th><th>������</th><th>�ŏI������</th><th>�O���t</th><th>*</th></tr>";
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
if($Mas){print"<tr><td colspan=6><br>���Ȃ݂Ɂc $Mas</td></tr>\n";}
print"</table><br>*�}�[�N�폜/Pass<input type=password name=pass size=8> <input type=submit value=\"�Ǘ��p\">\n";
print"</td><td valign=\"top\">\n";
if(@RLv){
	print"<table><tr bgcolor=$ttb><th>���x��</th><th>������</th></tr>\n";
	foreach(0..$#RLv){
		$SPL=$RSPL*$_;
		if($_!=$#RLv){$SPL2="�`".($RSPL*($_+1)-1)."��";}else{$SPL2="��ȏ�";}
		print"<tr align=center bgcolor=\"$k_back\"><td>$RLv[$_]</td><td>$SPL$SPL2</td></tr>\n";
	}
	print"</table>\n";
}
print"</td></tr></table></form></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�摜���擾]
# -> �t�@�C�����摜�̏ꍇ�A�t�@�C����ǂݍ���ŕ����擾���܂��B����ȊO�̃A�C�R���\���������Ȃ��܂�(size)
# -> �Ƃقق̃��E���W���Q�l�ɂ����Ă��������܂��� => http://tohoho.wakusei.ne.jp/
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
		$Pr.="<small>$IW�~$IH";
		if($Cg){$kW=$IW;$kH=$IH;}
		else{$Pr.=" =\&gt\; $kW�~$kH";}
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
# [���V�X�e��]
# -> �A�b�v�t�@�C��/�L���̕\������^���܂�(ent_)
#
sub ent_ {
if($FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}
&hed_("Permit");
print <<"_ENT_";
<center><table width=90\%><tr><th bgcolor=$ttb>�t�@�C��/�L���\\������</th></tr></table><br></center>
<ul><ul><table><tr><td>
<li><a href="$cgi_f?no=$no$pp"> �f���ɖ߂�</a> / <a href="$cgi_f?mode=del&pass=$FORM{"pass"}&no=$no$pp">�ʏ�Ǘ����[�h</a>
<li> ������/�����ɂ���t�@�C�����`�F�b�N���A�{�^���������ĉ������B
<li> �t�@�C���폜���`�F�b�N���ă{�^���������ƃt�@�C���݂̂��폜�ł��܂��B
<li> �L���݂̂̕\\�����͈�x���ς݂ɂ���ƁA�����ɖ߂��܂���!
</td><td><form action="$cgi_f" method=$met>$nf$pf
<input type=hidden name=mode value=ent><input type=hidden name=pass value=$FORM{"pass"}>
<select name=check>
<option value=1>�S�����L���`�F�b�N
<option value=2>�S���ϋL���`�F�b�N
<option value=0>�`�F�b�N���͂���
<input type=submit value="���s"></form></td></tr></table>
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
			print"<th>���`�F�b�N</th><th>���e�ҏ��</th><th>�R�����g</th><th>�t�@�C�����</th><th>�t�@�C���폜</th></tr>\n";
		}
		$check="";	
		if($Ent){$eok="��"; if($FORM{"check"}==2){$check=" checked";}}
		else{$eok="<font color=red>�~</font>"; if($FORM{"check"}==1){$check=" checked";}}
		if($ty){$Re="($ty���X)";}else{$Re="";}
		if($email){$name="<a href=\"mailto:$email\">$name</a>";}
		if($url){$url="/<a href='http://$url' target=$TGT>HP</a>";}
		if(-s "$i_dir/$ico"){$Size = -s "$i_dir/$ico";}else{$Size = 0;}
		$comment =~ s/<br>/ /g; $TB=1;
		if($tag){ $comment =~ s/</&lt;/g; $comment =~ s/>/&gt;/g; }
		if(length($comment) > 100){
			$comment=substr($comment,0,98); $comment=$comment . '..';
			$comment.="<a href=\"$cgi_f?mode=red&namber=$nam&pass=$FORM{'pass'}&no=$no$pp\" target=$TGT>�S��</a>";
		}
		if($k){$BG=" bgcolor=\"$k_back\""; $k=0;}else{$BG=""; $k=1;}
		print <<"_ENT_";
<tr$BG><th><input type=checkbox name=ENT value=$nam$check>-$eok</th>
<td nowrap><font color="$kijino">#$nam</font> $Re<br>��$name <small>[$Ip]</small><br>
��<small>($date$url)</small></td>
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
print "<br><input type=submit value=\"����/������ �t�@�C���폜\"></form></center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�\���`��]
# -> �A�b�v�t�@�C���\���`���̕ύX�Ȃ�(minf_)
#
sub minf_ {
if($FORM{"min"} eq ""){&get_("M");}
if($FORM{"min"}==1){$S="";$S2=" selected";$S3="";}
elsif($FORM{"min"}==2){$S="";$S2="";$S3=" selected";}
else{$S2="";$S=" selected";$S3="";}
print"</center><ul><form action=\"$cgi_f\" method=$met>$nf$pf";
if($mas_c){print"�E�\\�������o��܂Ńt�@�C����<img src='$i_Url/$no_ent'>�ŕ\\������܂��B<br>\n";}
if($_[0]){print"<input type=hidden name=H value=$_[0]>";}
print <<"_KEY_";
<input type=hidden name=page value=$page><input type=hidden name=mode value=cmin>
�E�L�����̉摜�\\���`��<select name=min>
<option value=0$S>$W2�~$H2�ȉ��ɏk��
<option value=1$S2>������
<option value=2$S3>�A�C�R��
</select><input type=submit value="�� �X"$fm>
</form>
</ul><center>
_KEY_
}
#--------------------------------------------------------------------------------------------------------------------
# [�A�b�v�t�@�C���ꗗ]
# -> �A�b�v���ꂽ�t�@�C�����ꗗ�ŕ\�����܂�(f_a_)
#
sub f_a_ {
&hed_("All Up File");
print <<"_ENT_";
<center><table width=90\%><tr><th bgcolor=$ttb>�t�@�C���ꗗ</th></tr></table><br></center>
<ul><ul>
<li><a href="$cgi_f?no=$no$pp"> �f���ɖ߂�</a>
<li> �A�b�v���ꂽ�t�@�C���݂̂̈ꗗ�ł��B
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
	$KL.="<hr size=1 width=\"80\%\">�y�[�W�ړ� / ";
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
	print"<b>[<a href=\"$cgi_f?$MD&no=$no$pp\">�ԐM�y�[�W</a>]</b><br><br></td></tr>\n";
	$i++;
	if($i==30){print"</table>"; $i=0; $TB=0;}
}
if($TB){print"</table>";}
$FS=int($FS/1024);
print "<br>���v�t�@�C���T�C�Y/$FS\KB$KL</center>\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�S�\��]
# -> �ݒ肳��Ă���f�����ꗗ�\�����܂�(a_)
#
sub a_ {
print "Content-type: text/html\n\n";
print <<"_HTML_";
<html><head>
$STYLE
$fsi
<!--$ver-->
<title>�SBBS�ŐV�X�V�L�� [All BBS New Subject]</title>
<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS"></head>
_HTML_
print"<body text=$text link=$link vlink=$vlink bgcolor=$bg";
if ($back ne "") { print " background=\"$back\">\n";} elsif ($back eq "") { print ">\n";}
print<<"_HTML_";
<table width="100\%"><tr bgcolor="$ttb"><th>�SBBS�ŏI�X�V�L��</th></tr></table><br>
<ul>
<li>Child Tree �ɐݒ肳��Ă���BBS�̍ŏI�X�V�L����\\�����܂��B
<li>BBS�^�C�g�����N���b�N����Ƃ��̌f���ցA�e�L���^�C�g�����N���b�N����Ƃ��̋L���Q�֔�т܂��B
</ul><center>
<table width="95\%" bordercolor="$ttb" border=1><tr bgcolor="$ttb"><th>BBS�^�C�g��</th>
<th>�ŐV�X�V���ꂽ�e�L���^�C�g��</th><th>�L����</th><th>�X�V��</th><th>�X�V����</th></tr>
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
			}else{$namber="#"; $d_may="�L��������܂���!"; $date="/"; $MD=""; $Name="/";}
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
# [�A�C�R���摜�\��]
# -> �A�C�R���摜�̃T���v����\�����܂�(img_)
#
sub img_ {
&hed_("All Icon");
print"<center><table width=\"90\%\"><tr><th bgcolor=\"$ttb\">�A�C�R���摜�ꗗ</td></tr></table>\n";
print"<br><a href=\"javascript:close()\">|X| �E�B���h�E�����</a><br><br>\n";
$I=0;
$page_=int($#ico1/$Ico_kp);
if($page_){
	print"�y�[�W�ړ� / ";
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
	if($ico1[$_] eq "randam"){print"<th width=$Ico_w>�����_��<br>�A�C�R��</th>"}
	elsif($ico1[$_] eq "master"){
		print"<th width=$Ico_w>";
		foreach $MAS (@mas_i){print"<img src=\"$IconDir/$MAS\">";}
		print"<br>�Ǘ��җp</th>\n";
	}elsif($ico1[$_] eq ""){print"<th width=$Ico_w>�Ȃ�</th>\n";}
	else{print"<th width=$Ico_w><img src=\"$IconDir/$ico1[$_]\"><br>$ico2[$_]</th>\n";}
	if($I >= $Ico_h){print"</tr>"; $I=0;}
}
if($I){print"</tr>";}
print"</table></center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�w��L���̕\��]
# -> No�w�肳�ꂽ�L���Ȃǂ��ЂƂ\��(read)
#
sub read {
if($namber=~/,/){@N=split(/\,/,$namber);}
elsif($namber=~/-/){
	($St,$En)=split(/-/,$namber);
	if($St<$En){if($En-$St > 50){$St=$En-49; $MSG="�����傫���������� $St-$En �ɕύX";} $Low=$St; $High=$En;}
	if($St>$En){if($St-$En > 50){$En=$St+49; $MSG="�����傫���������� $St-$En �ɕύX";} $Low=$En; $High=$St;}
	if($St eq ""){$Low=$En-10; $High=$En; $MSG="�������w��̂��� $St-$En �Ɏw��";}
	if($En eq ""){$Low=$St; $High=$St+10; $MSG="�������w��̂��� $St-$En �Ɏw��";}
	foreach($Low..$High){unshift(@N,$_);}
}
else{@N=$namber;}
$N=@N;
if($N > 50){splice(@N,50); $N=@N; $MSG="No�w�肪�������� $N �ȍ~�͔�\\��";}
&hed_("No$namber �̋L���\\��");
print"<center><table width=90\%><tr><th bgcolor=$ttb>No$namber �̋L��</th></tr></table><br>$MSG";
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
		print"<LI>No$N �̋L���͌��݂̃��O���ɂ���܂���I";
		if($klog_s){print"��<a href=\"$srch?no=$no&word=$N&andor=and&logs=all&PAGE=$klog_h[0]&ALL=1\">�S�ߋ����O���� No$N �̋L����T��</a>";}
	}
	print"</ul>";
}
print"<hr width=\"95%\">\n";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�t���[�t�H�[���C��]
# -> �ȑO�̕����R�[�h��̕s��C���ƃ��O�R���o�[�g(freeform_)
#
sub freeform_{
if($FORM{'pass'} ne "$pass"){&er_("�p�X���[�h���Ⴂ�܂�!");}
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
		}else{&er_("���ł� ChildTree �p�ɂȂ��Ă��܂�!","1");}
	}elsif($mo eq "UPP-BOARD"){
		if($space =~/[A-Za-z\#]+/){
			($font,$hr)=split(/\;/,$space);
			if($type){$sp=15;}else{$sp=0;}
			if($DmyNo <= $namber){$DmyNo=$namber;}
			if($end){foreach(0..$#exn){if($end=~ /$exn[$_]$/ || $end=~ /\U$exn[$_]\E$/){$TL=$exi[$_]; last;}}}
			$new_="$namber<>$date<>$name<>$email<>$d_may<>$comment<>$url<>$sp<><>$type<>$del<>";
			$new_.="$ip:$end:$tim:$TL:\|\|$font\|$hr\|:\|\|\|\|\|\|::<>$T<>$tim<>\n"; $T--;
		}else{&er_("���ł� ChildTree �p�ɂȂ��Ă��܂�!","1");}
	}
	push(@NEW,$new_);
}
close(DB);
if($DmyNo){unshift(@NEW,"$DmyNo<><><><><><><><><>$DmyNo<><><><><>\n");}
open (DB,">$log");
print DB @NEW;
close(DB);
if(-e $lockf){rmdir($lockf);}
$msg="<h3>�C������</h3>"; &del_;
}
#--------------------------------------------------------------------------------------------------------------------
# [���e�`�F�b�N]
# -> �t�H�[�����e���`�F�b�N(check_)
#
sub check_ {
if($Proxy){
	while(($envkey,$envvalue) = each(%ENV)){
		if($envkey =~ /proxy|squid/i || $envvalue =~ /proxy|squid/i){&er_("ProxyServer�o�R�ł͏������݂ł��܂���!");}
	}
}
if($i_mode && $UP){
	$FLAG=0;
	foreach (0..$#exn){if($file=~ /$exn[$_]$/i){$FLAG=1; $TAIL=$exn[$_]; $TL=$exi[$_]; last;}}
	if($FLAG==0){&er_("�A�b�v�ł��Ȃ��t�@�C���`���ł�!");}
	if(-e "$i_dir/$file"){
		$TIME=time; $file="$TIME$TAIL";
		$Henko="<h3>�����t�@�C�������������߁A$file�ɕύX���܂���</h3>";
	}elsif($file=~/[^\w\-\.]/){
		$TIME=time; $file="$TIME$TAIL";
		$Henko="<h3>�t�@�C�������s�K�؂��������߁A$file�ɕύX���܂���</h3>";
	}
	$MaxSize=$max_fs*1024;
	if($Fsize > $MaxSize){&er_("�t�@�C���T�C�Y���傫�����܂�!");}
	if(open(OUT, "> $i_dir/$file")) {
		binmode(OUT);
		print OUT substr($Read, $Pos2, $Fsize);
		close(OUT);
	}
	chmod(0666,"$i_dir/$file");
}
if($FORM{'UP'} eq ""){
	if($name eq ""){&er_("���O�����L��!");}
	if($comment eq ""){&er_("�R�����g��������!");}
	if($email && $email !~ /(.*)\@(.*)\.(.*)/){&er_("E-���[���̓��͓��e���s���ł�!");}
	#if($email && $email !~ /^[\w@\.\-_]+$/){&er_("E-���[���̓��͓��e���s���ł�!");}
	if($email && 512 < length($email)){&er_("E-���[���̓��͓��e���s���ł�!");}
	if(length($delkey) > 8 && $mode ne "h_w"){&er_("�폜�L�[ ��8�����ȓ�!");}
	if($NMAX && $NMAX < length($name)){&er_("���O�͔��p$NMAX���ȓ�!");}
	if($TMAX && $TMAX < length($d_may)){&er_("�^�C�g���͔��p$TMAX���ȓ�!");}
	if($CMAX && $CMAX < length($comment)){&er_("�R�����g�͔��p$CMAX���ȓ�!");}
	if($TXT_H && $TXT_F && $txt eq "" && ($TXT_R==0 || $TXT_R && $type==0)){&er_("$TXT_T��������!");}
	if($he_tp && $delkey eq "" && $FORM{'pass'} eq ""){ &er_("�g�s�b�N�ǉ��ɂ͍폜�L�[���K�{�ł�!"); }
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
			if($ICO_F==0){&er_("�Ǘ��җp�A�C�R���͎g�p�ł��܂���!");} $CICO="master";
		}else{$CICO=$ICO;}
	}
}
}
#--------------------------------------------------------------------------------------------------------------------
# [�ꗗ�\���̃t�b�^]
# -> �ꗗ�\�����̃t�b�^(allfooter)
#
sub allfooter {
print"<ul><b>";
if($Bl){print"$Bl���O��$_[0]$Ble\n";}
if($Nl){if($Bl){print"| ";} print"$Nl����$_[0]��$Nle\n";}
print <<"_HTML_";
</b><ul>( �y�[�W�ړ� / $Plink )</ul></ul>
<hr size=1 width="90\%">
<form action="$srch" method=$met>
<input type=hidden name=andor value=and><input type=hidden name=logs value="$log">
$nf$pf
<ul><b>[�����t�H�[��]</b>
<ul>���݃��O���S�L����/<b>$NS</b> <small>(�e/$total ���X/$RS)</small> ���猟��
�@�L�[���[�h/ <input type=text name=word size=10 value="$word">
<input type=submit value="�� ��">
</ul></ul></form>
<hr size=1 width="90\%">
<form action="$cgi_f" method=$met>
$nf$pf
<ul><b>[�폜/�ҏW�t�H�[��]</b>
<ul>�L��No<small>(���p����)</small>/<input type=text name=del size=8$ff> 
<select name=mode>
<option value=nam>�ҏW
<option value=key>�폜
</select>
�폜�L�[/<input type=password name=delkey size=8$ff>
<input type=submit value=" ���M "$fm>
</ul></form>
</ul><hr width="95\%">
_HTML_
}
#--------------------------------------------------------------------------------------------------------------------
# [cookie�폜]
# -> cookie���폜(�L���������ߋ���)���܂�(cookdel)
#
sub cookdel{
if($mo eq "ID"){
#	print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n"; $msg="<h4>ID�폜����</h4>";
}
elsif($mo eq "ALL"){
	print"Set-Cookie: $s_pas=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	print"Set-Cookie: Cmin=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
#	print"Set-Cookie: UID=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	print"Set-Cookie: CBBS=; expires=Sunday, 1-Jun-2001 00:00:00 GMT\n";
	$msg="<h4>cookie�폜����</h4>";
}
&hed_("cookie Delete");
print<<"_HTML_";
<SCRIPT language="JavaScript">
<!--
function Link(url) {
	if(confirm("�{���ɍ폜���Ă�OK�ł���?\\n(�폜����Ɠ��e�͌��ɖ߂��܂���!)")){location.href=url;}
	else{location.href="#";}
}
//-->
</SCRIPT>
<center>$msg
_HTML_
#if($UID){print"<a href=\"#\" onClick=\"Link('$cgi_f?mode=cookdel&mo=ID&no=$no$pp')\">ID��cookie�̂ݍ폜</a> /\n";}
print"<a href=\"#\" onClick=\"Link('$cgi_f?mode=cookdel&mo=ALL&no=$no$pp')\">���̌f���S�ʂ�cookie�폜</a><br>";
print"*) �폜���I��������E�B���h�E����Ă��������B</center>";
&foot_;
}
#--------------------------------------------------------------------------------------------------------------------
# [�g�ђ[�������o��]
# -> �g�уI�v�V��������̍�Ɩ��ߏI���̕\��(ktai)
#
sub ktai {
$_[1] =~ tr/+/ /;
$_[1] =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
$html ="<html><head><title>$_[0]����</title></head>";
$html.="<body><center>$_[0]����<br><br><a href=\"$_[1]\">[��]</a></center></body></html>";
$len = length($html);
print "Content-type: text/html\n";
print "Content-length: $len\n";
print "\n";
print "$html";
exit;
}
