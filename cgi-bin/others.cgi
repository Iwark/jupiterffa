#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠��T.CUMRO����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FFA Emilia Ver1.01
#  edit by Emilia
#  http://www5d.biglobe.ne.jp/~sprite/
#  y-kamata@jcom.home.ne.jp
#------------------------------------------------------#
#
#�@FF ADVENTURE ��i v2.1
#�@programed by jun-k
#�@http://www5b.biglobe.ne.jp/~jun-kei/
#�@jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#�@FF ADVENTURE v0.21
#�@programed by CUMRO
#�@http://cgi.members.interq.or.jp/sun/cumro/mm/
#�@cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(��) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���̏����ݒ�
$midi = $title_midi;
$backgif = $backgif;

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

#--------------#
#�@���C�������@#
#--------------#
if ($mente) {
	&error("�o�[�W�����A�b�v���ł��B�Q�A�R�O�b�قǂ��҂��������Bm(_ _)m");
}

if($link_flg){
	&link_chack;
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&html_top;

#-----------------#
#  TOP�y�[�W�\��  #
#-----------------#
sub html_top {

$non = int(rand(4));
if ($non == 3) {
	&read_winner4;
	$sity = "�h���S�����[���h";
}
elsif ($non == 2) {
	&read_winner3;
	$sity = "���b�h���[���h";
} elsif ($non == 1) {
	&read_winner2;
	$sity = "�C�G���[���[���h";
} elsif ($non == 0) {
	&read_winner;
	$sity = "�W���s�^���[���h";
}

	# �N�b�L�[�擾
	&get_cookie;

	# �����v�Z
	if($winner[18]) {
		$ritu = int(($winner[19] / $winner[18]) * 100);
	}
	else {
		$ritu = 0;
	}

	# �`�����v���ʎ擾
	if($winner[4]) {
		$esex = "�j";
	} else {
		$esex = "��";
	}

	# �`�����v��{�l�Z�o
	$divpm = int($charamaxpm / 100);
	$wci_plus = $winner[23] + $winner[52];
	$wcd_plus = $winner[26] + $winner[35];
	$hit_ritu = int($winner[9] / 3 + $winner[11] / 10 + $winner[30] / 3) + 40;
	$kaihi_ritu = int($winner[9] / 10 + $winner[11] / 20 + $winner[30]/10);
	$waza_ritu = int(($winner[11] / 10)) + 10;
	if($waza_ritu > 90){$waza_ritu = 90;}

	# �\�͒l�o�[�̏ڂ������ݒ�
#	$bw0     = int(1 * ($winner[7] / $divpm));
#	$bw1     = int(1 * ($winner[8] / $divpm));
#	$bw2     = int(1 * ($winner[9] / $divpm));
#	$bw3     = int(1 * ($winner[10] / $divpm));
#	$bw4     = int(1 * ($winner[11] / $divpm));
#	$bw5     = int(1 * ($winner[12] / $divpm));
	$winner[23] += $a_hitup;
	$winner[26] += $a_kaihiup;
#	$bwhit   = int(0.5 * ($hit_ritu + $winner[23]));
#	$bwkaihi = int(0.5 * ($kaihi_ritu + $winner[26]));
#	$bwwaza  = int(1 * ($waza_ritu + $winner[35]));
#	if($bwhit > 100){$bwhit = 100;}
#	if($bwkaihi > 100){$bwkaihi = 100;}
#	if($bwwaza > 100){$bwwaza = 100;}

	$date = time();

	&header;

	# HTML�̕\��
	print <<"EOM";
<table border=0>
<tr>
<td valign="top">
<table border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">�O��̑���</font></td></tr>
<tr><td class=b1>I D</td>
<form action="$loginscript" method="POST">
<input type="hidden" name="mode" value="log_in">
<td><input type="text" size="10" name="id" value="$c_id"></td>
<td class=b1>�p�X���[�h</td>
<td><input type="password" size="10" name="pass" value="$c_pass"></td>
<td><input type="submit" class="btn" value="���O�C��"></td>
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
<font class="$white">�e�X�g�v���C</font></td></tr>
<tr>
<form action="$loginscript" method="POST">
<td>
<input type="hidden" name="mode" value="log_in">
<input type=hidden name="id" value=test>
<input type=hidden name="pass" value=test>
<input type="submit" class="btn" value="�e�X�g�v���C"></td>
</form>
</tr></table>
EOM
} else {
print "���ݎg�p���ł�<br>���҂�������";
}
	print <<"EOM";
</td><td>
<table border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">�V�K�L�����쐬</font></td></tr>
<tr>
<FORM ACTION="$chara_make" METHOD="POST">
<INPUT TYPE="hidden" NAME="mode" VALUE="chara_make">
<td><input type="submit" class="btn" value="�V�K�L�����N�^�쐬"></td>
</form>
</tr></table>
</td></tr></table>
<table border=0 width='90%'>
<tr><td align="center" talign="center" class="b1">
<MARQUEE>$telop_message</MARQUEE></td>
</tr></table>
EOM

	# �`���Ґ��\��
	open(GUEST,"$guestfile");
	@member=<GUEST>;
	close(GUEST);

	$num = 0;
	$blist = '';
	foreach (@member) {
		($ntimer,$nname,$nid) = split(/<>/);
		if($date - $ntimer < $sanka_time){
			$blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\">$nname</a><font size=1 color=#ffff00>��</font>";
			$num++;
		}
	}


	print "<font size=2 color=#aaaaff>���݂̖`����(<B>$num�l</B>)�F</font>\n";

	if ($blist) {
		print $blist;
	}
	else {
		print '�N�����܂���';
	}

	print <<"EOM";
<br>���݂̘A���L�^�́A$winner[47]����́u<A HREF=\"$winner[49]\" TARGET=\"_blank\"><FONT SIZE=\"3\" COLOR=\"#6666BB\">$winner[48]</FONT></A>�v�A$winner[45]�A���ł��B�V�L�^���o�����T�C�g���̉��ɂ́A<IMG SRC="$mark">�}�[�N�����܂��B
<table border=0 width='100%'>
<tr>
<td width="500" valign="top">
	<table border=1 width="100%">
	<tr>
	<td id="td1" colspan=5 align="center" class="b2">�y$sity�z�`�����v<font class="white">$winner[44]�A����</font><br><font class = "yellow">(<a href=$scripta?mode=chara_sts&id=$winner[40]>$winner[41]</a><font class = "yellow">�ɏ����I�I\[�T�C�g\]</font><A HREF=\"$winner[43]" TARGET="_blank">$winner[42]</A> )</font></td>
	</tr>
	<tr>
	<td id="td2" align="center" class="b1">�z�[���y�[�W</td>
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
<td align="center" rowspan="11" valign=bottom><img src="$img_path/$chara_img[$winner[5]]"><font color=$white>$winner[18]</font>��<font color=$white>$winner[19]</font>����<br>�����F$ritu\%<br>
<table width="100%" border=1>
<tr><td id="td2" class="b2">����</td><td align="center" class="b2">$winner[21] $bukilv</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="center" class="b2">$winner[24] $bogulv</td></tr>
<tr><td id="td2" class="b2">����</td><td align="center" class="b2">$winner[27]</td></tr>
<tr><td id="td2" class="b2">������</td><td align="left" class="b2"><img src=\"$bar\" width=$bwhit height=$bh><br><b>$hit_ritu + $winner[23] %</b></td></tr>
<tr><td id="td2" class="b2">���</td><td align="left" class="b2"><img src=\"$bar\" width=$bwkaihi height=$bh><b><br>$kaihi_ritu + $winner[26] %</b></td></tr>
<tr><td id="td2" class="b2">�K�E��</td><td align="left" class="b2"><img src=\"$bar\" width=$bwwaza height=$bh><br><b>$waza_ritu + $winner[35]%</b></td><td></td></tr>
</table></td><tr>
<td id="td2" align="center" class="b1">�Ȃ܂�</td><td class="b2"><b>$winner[3]</b></td>
<td id="td2" align="center" class="b1">����</td><td class="b2"><b>$esex</b></td></tr>
<tr><td id="td2" align="center" class="b1">�W���u</td><td class="b2"><b>$chara_syoku[$winner[14]]</b></td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$winner[39]</b></td></tr>
<tr><td id="td2" align="center" class="b1">���x��</td><td class="b2"><b>$winner[17]</b></td>
<td id="td2" align="left" class="b1">-</td><td class="b2">-</td></tr>
<tr><td id="td2" align="left" class="b1">HP</td><td class="b2"><b>$winner[15]\/$winner[16]</b></td>
<td id="td2" align="left" class="b1">�܋�</td><td class="b2"><b>$winner[50]</b></td></tr>
<tr><td id="td2" align="left" class="b1">STR</td><td class="b2"><img src=\"$bar\" width=$bw0 height=$bh><br><b>$winner[7] + $winner[28]</b></td>
<td id="td2" align="left" class="b1">INT</td><td class="b2"><img src=\"$bar\" width=$bw1 height=$bh><br><b>$winner[8] + $winner[29]</b></td></tr>
<tr><td id="td2" align="left" class="b1">DEX</td><td class="b2"><img src=\"$bar\" width=$bw2 height=$bh><br><b>$winner[9] + $winner[30]</b></td>
<td id="td2" align="left" class="b1">VIT</td><td class="b2"><img src=\"$bar\" width=$bw3 height=$bh><br><b>$winner[10] + $winner[31]</b></td>	</tr>
<tr><td id="td2" align="left" class="b1">LUK</td><td class="b2"><img src=\"$bar\" width=$bw4 height=$bh><br><b>$winner[11] + $winner[32]</b></td>
<td id="td2" align="left" class="b1">EGO</td><td class="b2"><img src=\"$bar\" width=$bw5 height=$bh><br><b>$winner[12] + $winner[33]</b></td></tr>
</table>
</td>
<td valign="top">
<td valign="top" align="left">

<table width=340 border=1>
<tr><td id="td2" align=center colspan=5 class=b2>
<font class="$white">�^�C���C�x���g</font></td></tr>
<tr>
<td align=center>
EOM
($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
$mon = $mon+1;
	if ($hour >= 19 and $hour < 21){
		print '<font color=yellow>19���`21�����ʁF��͂��h���b�v��+20%</font><br>';
	}
	if ($hour >= 21 and $hour < 23){
		print '<font color=yellow>21���`23�����ʁF�擾�o���l+100%</font><br>';
		print '<font color=yellow>21���`23�����ʁF�h���b�v��+100%</font><br>';
	}
	if ($wday == 0){
		print '<font color=yellow>���j���ʁF�擾�o���l+20��</font><br>';
	}
	if ($wday == 1){
		print '<font color=yellow>���j���ʁF�擾�o���l+20��</font><br>';
	}
	if ($wday == 3 and $hour >= 18 and $hour < 19){
		print '<font color=yellow>���j��18���`19�����ʁF�h���b�v��+100%</font><br>';
	}
	if ($wday == 5){
		print '<font color=yellow>���j���ʁF�h�̑����0�ƂȂ�</font><br>';
	} 
	if ($wday == 6){
		print '<font color=yellow>�y�j���ʁF�h���b�v���Q�{�I�I</font><br>';
	}
	if ($mday == 15 and $mon == 3){
		#�C�x���g�I
		print '<font color=yellow>���ʃC�x���g�J�Ò��I</font><br>';
	}
	print <<"EOM";
</td>
</tr></table>

[<B><FONT COLOR=$yellow>$main_title �̗V�ѕ�</FONT></B>]
<OL>
<LI>�܂��A�u�V�K�L�����N�^�[�o�^�v�{�^���������āA�L�����N�^�[���쐬���܂��B
<LI>�L�����N�^�[�̍쐬������������A���̃y�[�W�̍���ɂ���Ƃ��납�烍�O�C�����āA���Ȃ���p�̃X�e�[�^�X��ʂɓ���܂��B
<LI>�����ł��Ȃ��̍s����I�����邱�Ƃ��ł��܂��B
<LI>��x�L�����N�^�[���쐬������A�E��̂Ƃ��납�烍�O�C�����ėV�т܂��B�V�K�ɃL�����N�^�[������̂́A��l�Ɉ�̃L�����N�^�[�݂̂ł��B
<LI>����́AHP�o�g���[�ł͂Ȃ��A�L�����o�g���[�ł��B�L�����N�^�[����ĂĂ����Q�[���ł��B
<LI>�\\�͂�U�蕪���邱�Ƃ��ł��L�����N�^�[�̔\\�͂��������Ō��߂邱�Ƃ��ł��܂��B(�����Ō��߂��\\�͂͂����܂�ɂ����㏸���Ȃ��̂ŁA�T�d��)
<LI><b>$limit��</b>�ȏ㓬��Ȃ���΁A�L�����N�^�[�̃f�[�^���폜����܂��B
<LI>��x�퓬�����<b>$b_time</b>�b�o�߂��Ȃ��ƍĂѐ퓬�ł��܂���B
</OL>
</td>
</tr>
</table>
<hr size=0>
<!--
<font color=$white>���L�ݒu��/<a href="$homepage" TARGET="_top">$home_title</a> / $kyouyuu<br>
<font color=$white>���j���[/</font><a href="$scripta?mode=ranking">�o�^�҈ꗗ</a> / <a href="$ranking">\�\\�͕ʃ����L���O��</a> / <a href="$syoku_html" target="_blank">�e�E�ƂɕK�v�ȓ����l</a> /<a href="$img_all_list" target="_blank">$vote_gazou</a> /<a href="$bbs">$bbs_title</a> /<a href="$helptext" target="_blank">$helptext_url</a><br>
<font color=$white>���̊O��/</font><a href="$sbbs">$sbbs_title</a> / <a href="$vote">$vote_title</a> /<br>
-->
<table border=0 width="100%">
�e�e�`�ݒu�����L���O�ɓo�^���ł��B���[�̓N���b�N��<A href="http://www.seijyuu.com/game/link/in.cgi?kind=ffa&id=kohe&mode=top" target="_blank">�����Q�[���ݒu�T�C�g�����L���O�yFF ADVENTURE �z</A>
<TR><TD class="b1" bgcolor="#000000" align="center"><B>�A������</B></font></TD></TR>
<TR><TD class="b2">$kanri_message</TD></TR></table>

<form action="$scriptk" method="POST">
<table><td><input type="password" size="10" name="pass"></td>
<td><input type="submit" class="btn" value="�Ǘ���"></td>
</tr></table></form>
EOM

	# �t�b�^�[�\��
	&footer;

	exit;
}
#------------------#
#  �N�b�L�[���擾  #
#------------------#
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

#------------------#
#�������N�`�F�b�N  #
#------------------#
sub link_chack {
	#�������N�h�~����
	$geturl = $ENV{'HTTP_REFERER'};
	#�������N�}�~�@�\�g�p�Ɉē�����t�q�k
	$guid ="<H1>�Ăяo����������������܂���I�I</H1>";
	if ($top_url) {
		$guid.="<a href=\"$top_url\">$top_url</a>�������Ȃ����Ă��������B";
	}
	else{
		$guid.="<font color=$yellow size=4>���L�T�C�g�ꗗ</font>";
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
