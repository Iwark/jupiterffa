#!/usr/bin/perl
#BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR, ">&STDOUT"); }

#---------------------------------------------------------------#
#�@ChatSystem ver.2.10
#�@Edit by Lost
#�@http://kirbys.oo.lv/
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �{�݃��C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# �`���b�g���C�u�����̓ǂݍ���
require 'chat.pl';

# �`���b�g�ݒ�̓ǂݍ���
require 'chat_conf.cgi';

$script_name = "./post_chat.cgi";

#-----------------------------------------------------------------------------#
# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��B
#-----------------------------------------------------------------------------#

if ($mente) {
	&error("�����e�i���X���ł��B"); 
}
&decode;

foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

if ($mode) { &$mode; }
&chat_main;

#------------------#
#�@�`���b�g�\���@�@#
#------------------#
sub chat_main {

	&header;
if($_[1] ne ""){
$log_chat = "$_[1]\.cgi";
}else{
$log_chat = "$chat_log_file";
}
open(IN,"$log_chat");
@CHAT_LOG = <IN>;
close(IN);
$hit=0;$i=1;
foreach(@CHAT_LOG){
($cid,$cname,$chatmes,$cday,$ctime,$cico,$clvl) = split(/<>/);
if($view_mes <= $i) {
last;
}
if($_[0] eq "wlm09"){
print <<"EOM";
<span style="color:#545454;font-size:10pt;">$cname ����̔��� Lv.$clvl ($ctime):</span><br>
<table><tr><td>
<span style="color:#000000;font-size:10pt;">
<span style="color:#545454;font-size:10pt;">�E</span>$chatmes
</span>
</td></tr></table>
EOM
}elsif($_[0] eq "skype"){
print <<"EOM";
<table width="100%" bgcolor="#DBDBDB">
<tr>
<td width="30%" border="1" style="color:#000000;background-color:#DBDBDB;"><span style="color:#000000;font-size:10pt;">$cname�̔���</span></td><td width="70%" align="right" border="1" style="color:#000000;background-color:#DBDBDB;"><span style="color:#000000;font-size:10pt;">Lv.$clvl $ctime</span>
</td></tr></table>
<table><tr><td>
<span style="color:#000000;font-size:10pt;">
$chatmes
</span>
</td></tr></table>
EOM
}elsif($_[0] eq "skype4"){
print <<"EOM";
<table width="100%">
<tr>
<td width="15%" align="left">
<span style="color:#8599FF;font-size:10pt;">$cname</span>
</td><td width="65%">
<span style="color:#000000;font-size:10pt;">$chatmes</span>
</td><td width="20%" align="right">
<span style="color:#999999;font-size:10pt;">Lv.$clvl $ctime</span>
</td></tr></table>
EOM
}elsif($_[0] eq "wlm08"){
print <<"EOM";
<span style="color:#545454;font-size:10pt;">$cname �̔��� Lv.$clvl ($ctime) :</span><br>
<table><tr><td>
<span style="color:#000000;font-size:10pt;">
\&nbsp;$chatmes
</span>
</td></tr></table>
EOM
}elsif($_[0] eq "irc"){
print <<"EOM";
<br><span style="color:#000000;font-size:10pt;">[$ctime] <span style="color:#;font-size:10pt;">$cname�̔���:</span> $chatmes Lv.$clvl $cday $ctime</span>
EOM
}else{
print <<"EOM";
<hr size=0>
<font color="$mes_c">
<span style="font-size:11px;"><strong>$cname</strong> > $chatmes</span> <span style="font-size:8pt;">Lv.$clvl ($cday$ctime)</span>
</font><br>
EOM
}
$hit=1;$i++;
}
if(!$hit){
print "<hr size=0><span style=\"color:#FF0000;\">���O���L��܂���</span>\n";
}

print "<hr size=0>";

# ���쌠�\���i�폜���ցj
print "<div align=\"center\"><span style=\"font-size:small;\">- <a href=\"http://kirbys.oo.lv/\" target=\"_blank\">ChatSystem Ver.2.10</a> -</span></div>";
}

#--------------------#
# �S���փ��b�Z�[�W   #
#--------------------#
sub chat_mes {

	&chara_load;

	&chara_check;

	&time_geting(time());

	$cm = $in{'cmes'};
	$style = $in{'style'};

	unless($cm eq ""){

	while ($chara[0] eq $bad_id[$n]){
		&error("�����ł��܂���I�I");
      ++$n;
	if($n == $num){
	last;
	}
	}

	foreach (@ban_word) {
	&error("�֎~���ꂽ�����������Ă��܂��B") if index($cm,$_) >= 0;
	}
	$n_mes = length($cm);
	
	&error("���b�Z�[�W���������܂��I���p��$mes_n�����܂łł��I(���ݕ������F$n_mes)<br>") if $n_mes > $mes_n;
	
	$tag_option ="";
	if($in{'font_bold'} eq "����"){ $tag_option.=" font-weight:bold;"; }	
	if($in{'font_ital'} eq "�Α�"){ $tag_option.=" font-style:italic;"; }
	if($in{'font_line'} eq "���"){ $tag_option.=" text-decoration:line-through;"; }
	#if($chara[$color_chara] ne ""){ $text_c = $chara[$color_chara]; }else{ $text_c = $mes_c; }
	$text_c = $mes_c;
	if($in{'font_color'} ne ""){ $text_color ="$in{'font_color'}"; }else{ $text_color = $text_c; }
	#if($chara[$size_chara] ne ""){ $text_s = $chara[$size_chara]; }else{ $text_s = $mes_s; }
	$text_s = $mes_s;
	if($in{'font_size'}){ $text_size ="$in{'font_size'}"; }else{ $text_size = $text_s; }
	
		$comment= "<span style=\"font-size: $text_size;color: $text_color;$tag_option\">$cm</span>";

	$lock_file = "$lockfolder/cal.lock";
	&lock($lock_file,'CA');
	if($in{'room'} ne ""){
		$log_chat = "$in{'room'}\.cgi";
	}else{
		$log_chat = "$chat_log_file";
	}
	open(IN,"$log_chat");
	@CLOG = <IN>;
	close(IN);

	$c_num = @CLOG;

	if ($c_num > $save_mes) { pop(@CLOG); }

	unshift(@CLOG,"$chara[0]<>$chara[4]<>$comment<>$get_day<><>$chara[6]<>$chara[18]<>\n");
	if($in{'room'} ne ""){
		$log_chat = "$in{'room'}\.cgi";
	}else{
		$log_chat = "$chat_log_file";
	}
	open(OUT,">$log_chat");
	print OUT @CLOG;
	close(OUT);

	&unlock($lock_file,'CA');
	}

	&chat_main("$style","$in{'room'}");
exit;
}
#--------------#
#  ���Ԃ��擾  #
#--------------#
sub time_geting {

	$ENV{'TZ'} = "JST-9";
	($s,$m,$h,$md,$mo,$y,$wd) = localtime($_[0]);
	@week = ('Sun','Mon','Tue','Wed','Thu','Fri','Sat');

	# �����̃t�H�[�}�b�g
	$get_day = sprintf("%02d/%02d(%s)",$mo+1,$md,$week[$wd]);
	$get_time = sprintf("%02d:%02d:%02d",$h,$m,$s);
}