#!/usr/local/bin/perl

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g���g�p���������Ȃ鑹�Q�ɑ΂��Ă�             #
#    ��҂͈�؂̐ӔC�𕉂��܂��񂵕����܂���B                 #
# 2. ����Ɋւ��鎿��͌f�������[���ł�낵���ł�             #
#   �]�k�ł�����҂�                                            #
#   http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/       #
#   �������ӂɂ��܂�                                            #
#---------------------------------------------------------------#

##############
#�ϐ��ݒ�J�n#
##############

#���^�C�g�����̐F
$col_1 = "#000000";

#�����e�i���o�[�Ɓ��̐F
$col_2 = "#5588FF";

#�����b�Z�[�W�Ɩ��O�̐F
$col_3 = "#333333";

#�������̐F
$col_4 = "#CCCCCC";

#���̓t�H�[���̐��̐F(IE�̂�)
$form_line = "#000000";

#���̓t�H�[���̔w�i�F(IE�̂�)
$form_col = "#FFFFFF";

#�������̑傫��
$fontsize = "13px";

#�����N�G�X�g���\�b�h�̐ݒ�
$form = "POST";

#�����ߍ��ݕ\���ō����b�Z�[�W��
$maxmes = "18";

#���ۑ����b�Z�[�W��
$maxmes2 = "200";

#�����̃t�@�C���̃t���p�X(http://����)
$pppbbsmini = "http://w2.abcoroti.com/~ffajupiter/cgi-bin/pppbbsmini.cgi";

#���e���v���[�g�t�@�C���̃A�h���X(���΃p�X)
$templ = "./temp.html";

#�������o��HTML���O�t�@�C��(���ۂɃA�N�Z�X����t�@�C��)�̃p�X
#���΃p�X�Ŏw�肵�ĉ�����
#�p�[�~�b�V����[666]�ō쐬
$mainf = "../index.html";

#��HTML���O�t�@�C���̃t���p�X(http://����A�Ō�ɃX���b�V��[/]�͂���܂���)
$htmlog = "http://127.0.0.1/cgi-bin/cgilabo/index.html";

#�����O�t�@�C���̃p�X(���΃p�X)
#�p�[�~�b�V����[666]�ō쐬����
$lfile = "./log.cgi";

#�e�[�u���p�̉摜������f�B���N�g���̃t���p�X(http://����A�Ō�ɃX���b�V��[/]�͂���܂���)
$image_dir = "http://127.0.0.1/cgi-bin/cgilabo/images";

#���e�C���[�W�̃p�X�A�ԍ���readme�̒��Ő������Ă���g�̔ԍ��ł�
#�摜�����Ȃ��Ƃ���̓X�y�[�T�[�摜�Ŗ��߂Ă����ĉ�����
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

#���e�[�u���̍����̐ݒ�
#���Ԃ��Ă͕̂t����readme�̒��Ő������Ă���g�̔ԍ��ł�

#�P�Ԃ̍���
$height1 = "15";
#�S�Ԃ̍���
$height4 = "0";
#�V�Ԃ̍���
$height7 = "20";
#�P�O�Ԃ̍���
$height10 = "15";

#�P�Ԃ̕�
$width1 = "15";
#�Q�Ԃ̕�
$width2 = "800";
#�R�Ԃ̕�
$width3 = "15";

#�����b�Z�[�W�̍ō����p������
$mesmax = "60";

#�����O�̍ō����p������
$namemax = "10";

#�����[���A�h���X�̔��p�ō�������
$mailmax = "50";

#���g�������ߋ����O��ʂɏo��R�����g
$howto =<<"EOH";
<!--�R�R����-->

<CENTER><B>���P�s�f���A���ӓ_��</B></CENTER><br>
�E���O�ƃ��b�Z�[�W�͕K�{�ł�<br><br>
�EHTML�^�O�͎g�p�o���܂���<br><br>
�E����������������܂�<br>
���O[���p$namemax����]<br>
���[���A�h���X[���p$mailmax����]<br>
���b�Z�[�W[���p$mesmax����]<br><br>
�E�������݂����f����Ȃ��Ƃ��̓����[�h���Ă݂ĉ�����<br><br>
�E�l�̖��f�ɂȂ�悤�Ȕ����͍폜���܂�<br><br>
�E���p�J�i�͕�����������̂Ŏg��Ȃ��ŉ�����<br><br>

<!--�R�R�܂�-->
EOH

#��HTML�̐ݒ�(�ߋ����O��ʂƃG���[���)
$bgcolor = "#DDEEFF";
$bground = "";
$textc   = "#000000";
$linkc   = "#333333";
$vlinkc  = "#444444";
$alinkc  = "#555555";

#�����ߍ��݌f���ł̃^�C�g��
$title = "���߂��݌f����";

#���Ǘ��l�폜�p�X
$adpass = "pass";

#���^�O�������邩�ۂ��A������Ȃ�1�����łȂ����0
$tagok = "0";

#���������ݏI�����A�G���[���̉�ʂ��牽�b�Ŏ����I�ɖ߂邩
$backsec = "5";

###############################################################
#�ϐ��ݒ�I���`�R�R����͒m�����������l���ύX���܂��傤
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
if ($mode eq main){&emes('�������݊����I','�������݂����f����Ă��Ȃ��Ƃ��̓����[�h���Ă݂ĉ�����');}
print "Location: $htmlog\n\n";
#############################

##################
#���O�������ݏ���#
##################
sub wlog{
unless($mes){&emes('Erorr!!','���b�Z�[�W���������܂�Ă��܂���');}
unless($name){&emes('Erorr!!','���O���������܂�Ă��܂���');}

if ($namemax < length($name)){&emes('Erorr!!',"���O�̕������������I�[�o�[�ł�(���p$namemax�����܂�)");}
if ($mailmax < length($mail)){&emes('Erorr!!',"���[���A�h���X�̕������������I�[�o�[�ł�(���p$mailmax�����܂�)");}
if ($mesmax < length($mes)){&emes('Erorr!!',"���b�Z�[�W�̕������������I�[�o�[�ł�(���p$mesmax�����܂�)");}

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
#�e�[�u��#
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
$bbs .= "<tr><td width=\"$name_w\"><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">$count��</SPAN>";
if ($mail ne ""){$bbs .= "<A HREF=\"mailto\:$mail\" style\=\"font\-size\:$fontsize\;color\:$col_3;\">$name</A></td>";}
else{$bbs .= "<SPAN style\=\"font\-size\:$fontsize\;color\:$col_3;\">$name</SPAN></td>";}
$bbs .= "<td><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">��</SPAN><SPAN style\=\"font\-size\:$fontsize\;color\:$col_3;\">$mes</SPAN></td><td><SPAN style=\"font-size:$fontsize\; color\:$col_2\;\">��</SPAN><SPAN STYLE=\"font\-size\:11px\;\ color\:$col_4\;\">$date</SPAN></td></tr>\n";
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
</TD><TD><A href="$pppbbsmini?mode=view" target="_blank" STYLE="font-size:12px;color:$col_1">�g����</A>
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
#���ݎ����擾#
##############
sub gettime{
($second,$minute,$hour,$day,$month,$year) = localtime(time);
$year += 1900;
$month += 1;
$date = "$month/$day/$hour\:$minute";
}

################
#���b�Z�[�W�\��#
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
<a href="$htmlog">�y�[�W�ɖ߂�</a><br><br><br><br><br>
<span style="font-size:11px">
<a href="http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/">�Ă��Ƃ��N�����߂���</a></span></center>
</body></html>
EOH
exit;
}

##############
#�ߋ����O�\��#
##############
sub view {

print << "EOH";
Content-type: text/html; charset=Shift_JIS

<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" CONTENT="text/html;CHARSET=Shift-JIS">
<TITLE>�ߋ����O</TITLE>
</HEAD>
<BODY BGCOLOR="$bgcolor" BACKGROUND="$bground" TEXT="$textc" LINK="$linkc" VLINK="$vlinkc" ALINK="$alinkc">
<hr size=0>
<SPAN style="font-size:13px">
<center><table border=0><tr><td align=left>$howto</td></tr></table></center></SPAN>
<FORM ACTION="$pppbbsmini" METHOD="$form">
���ߋ��̋L�^�y$maxmes2���z
<hr size=1>
EOH
open(MAIN, "$lfile");
while (<MAIN>) {
if($_=~/^\t(.+)$/) {next;}
($count,$name,$mail,$mes,$date) = split(/<:>/);
print"<INPUT TYPE=\"checkbox\" NAME=\"delno\" VALUE=\"$count\"><SPAN STYLE=\"font-size:$fontsize\">$count��";
if ($mail ne ""){print"<A HREF=\"mailto\:$mail\">$name</A>";}
else{print"$name";}
print"��$mes��</SPAN><SPAN STYLE=\"font\-size\:11px\;\">$date</SPAN><HR size=0>\n";
}
close(MAIN);
print<<"EOH";
<a href="$htmlog">�y�[�W�ɖ߂�</a><br>
<INPUT TYPE="password" NAME="pass" size="10">
<INPUT TYPE="hidden" name="mode" value="admin"><INPUT TYPE="submit" VALUE="admin">
</FORM><br><br><br><br>
<span style="font-size:11px">
<center><a href="http://www.yamabuki.sakura.ne.jp/~darkrose/cgi/potya/">
�Ă��Ƃ��N�����߂���</a></span></center>
</center></body></html>
EOH
exit;
}
######
#�폜#
######
sub admin{
  if($pass ne $adpass){&emes('Erorr!!','�p�X���[�h���Ⴂ�܂��I�I');}
  unless($pass){&emes('Erorr!','�p�X�����͂���Ă��܂���I�I');}
  unless($delno[0]){&emes('Erorr!','�폜�i���o�[�����͂���Ă��܂���I�I');}

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
