#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��4�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
#  FF ADVENTURE(������)
#�@remodeling by ����
#�@http://www.eriicu.com
#�@icu@kcc.zaq.ne.jp
#------------------------------------------------------#
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

#--- [���ӎ���] ------------------------------------------------#
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi�@		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'sankasya.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

require 'chat.pl';

# ���̃t�@�C���p�ݒ�
$backgif = $sts_back;
$midi = $sts_midi;
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
&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&log_in;

#----------------#
#  ���O�C�����  #
#----------------#
sub log_in {

	if (!( -e "./charalog/$in{'id'}.cgi")) {
		if ( -e "./autobackup/charalog/$in{'id'}.cgi" ) {
		}else{
			&error('ID������������܂���I');
		}
	}

	&chara_load;

	&chara_check;

	&item_load;

	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	$chara[144]=time();
	&chara_regist;
	&chara_load;

	$ltime = time();
	$ltime = $ltime - $chara[27];
	$vtime = $b_time - $ltime;
	$xtime = $vtime + 1;
	$ztime = $vtime + 1;
	$mtime = $m_time - $ltime + 1;

	if($chara[28] < $boss) {
		$chara[28] = 0;
	}

	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);
	$gnnt="<option value=\"\">�����₫\n";
	foreach(@guest){
		($gtt,$gnn,$gii) = split(/<>/);
		if($gii ne "jupiter"){ $gnnt.="<option value=\"$gnn\">$gnn�����\n"; }
	}
	if($chara[5]) { $esex = "�j"; } else { $esex = "��"; }
	if($chara[70]!=1){$next_ex = $chara[18] * ($lv_up + $chara[37] * 150 - $chara[32] * 50);}
	else{$next_ex = $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;}
        if(!$chara[32]){$chara[32] = 0;}

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}

	$syou = @shogo[$chara[32]];

        #�h��v�Z
        $yado_daix=int($yado_dai*$chara[18]);

	&header;

	&guest_list;

	&guest_view;

	if($chara[140]==2){$sity = "�C�G���[���[���h";&read_winner2;}
	elsif($chara[140]==3){$sity = "���b�h���[���h";&read_winner3;}
	elsif($chara[140]==4){$sity = "�h���S�����[���h";&read_winner4;}
	elsif($chara[140]==5){$sity = "�V�E";&read_winner5;}
	else{$sity = "�W���s�^���[���h";&read_winner;}

       print <<"EOM";
	<hr size=0>
	<font class=white>���j���[/</font><a href="$scripta?mode=ranking">�o�^�҈ꗗ</a> /
	<a href="$helptext" target="_blank">$helptext_url</a> /
	<a href="./cbbs/cbbs.cgi" target="_blank">�f����</a>
	<br>
	<!--
	<a href="$ranking">�\\�͕ʃ����L���O��</a> /
	<a href="$syoku_html" target="_blank">�e�E�ƂɕK�v�ȓ����l</a> /
	<a href="$img_all_list" target="_blank">$vote_gazou</a> /
	<a href="$bbs" target="_blank">$bbs_title</a> /
	<font class=white>���̊O��/</font>
	<a href="$sbbs" target="_blank">$sbbs_title</a> / 
	<a href="$vote" target="_blank">$vote_title</a> /
	-->
<br>
<table align="center"width="100%">
EOM
if($chara[50]==1){
	print <<"EOM";
<TR><td rowspan="2"  align="center" class="b2" width=70 height=60>
EOM
}else{
	print <<"EOM";
<TR><td rowspan="2"  align="center" class="b2" width=70 height=60><img src="$img_path/$chara_img[$winner[5]]">
EOM
}
	print <<"EOM";
<TD id="td1" align="center" colspan=2 class="b2">�y$sity�z�`�����v<a href="$scripta?mode=chara_sts&id=$winner[0]"><B>$winner[3]</B></a>����($winner[44]�A����)</TD></TR>
	<TR><td id="td2"align="center" class="b2">���݂�HP</td><TD class="b2"align="center"><B>$winner[15]\/$winner[16]</B></TD></TR></table>
<hr size=0>
<font size=5 color="yellow">$sity</font><br>
<font size=4 color="red"><b>�V�K����͌f���ŏ����擾���悤�I�����O�ɒ��ׂ悤�I</b></font>
EOM
	print <<"EOM";
<table border=0 width='30%'>
<tr><td align="center" talign="center" class="b1">
<MARQUEE><font color=yellow>$ttemes</font></MARQUEE></td>
</tr></table>

<hr width=400>
<script>
function aaa(fm){ 
fm.mes.value="";
fm.mes.focus(); 
return false; 
}
</script>
<FORM action="menu.cgi" target="chat" onSubmit="setTimeout(function(){return aaa(this)},10)">
<table border=0 align="center" width='100%'><tr>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="name" value="$chara[4]">
<input type="hidden" name="level" value="$chara[18]">
<input type="hidden" name="chattime" value="1">
<input type="hidden" name="chan" value="$chara[96]">
<input type="hidden" name="chan2" value="$chara[180]">
��A�`�����l���g�p�F�@<INPUT TYPE="radio" NAME="tch2" VALUE="$chara[96]">ON
<INPUT TYPE="radio" NAME="tch2" VALUE="" checked>OFF
�@�A<INPUT TYPE="radio" NAME="tch3" VALUE="$chara[180]">ON
<INPUT TYPE="radio" NAME="tch3" VALUE="" checked>OFF
�@<select name="sasayaki">$gnnt</select>
<td align="left"><input type="submit" class=btn value="�������X�V">
<INPUT type="text" value="" name="mes" size="100" maxlength="60">�@�@
<INPUT type="text" value="" name="tch" size="3" maxlength="3">ch</td>
</tr>
<tr></FORM>
<td align="left" class="b2">
<iframe src="menu.cgi" width="100%" height="200" frameborder="0" name="chat" allowtransparency="true" scrolling="yes"></iframe>
</td></tr></table>

EOM
#	&chat_post;

if ($ztime > 0) {
       print <<"EOM";
<table><tr>
<FORM NAME="form1">
<td>
�퓬�J�n�\\�܂Ŏc��<INPUT TYPE="text" NAME="clock" SIZE="3">�b�ł��B(�����ōX�V����܂��B)
</td>
</FORM>
</tr></table>
EOM
}
if($item[20]==10 and $chara[24]==1400){$g="yellow";}elsif($item[20]==10){$g="red";}elsif($chara[24]==1400){$g="pink";}else{$g="";}
if($item[22]==10){$w="red";}else{$w="";}
$bukikoka = "�U���� $item[1]<br>������ $item[2]<br>���� $item[24]";
$bogukoka = "�h��� $item[4]<br>��� $item[5]<br>���� $item[25]";
$acskoka = "���� $item[19]";
$waza_ritu = int(($chara[11] / 10)) + 10 + $a_wazaup;
if($waza_ritu > 90){$waza_ritu = 90;}
$hissatu_ritu = $waza_ritu + int($chara[12]/4);
$hit_ritu = int($chara[9] / 3 + $chara[11] / 10 + $item[10] / 3) + 40 + $item[2] + $item[16];
$sake = int($chara[9] / 10 + $chara[11] / 20 + $item[10]/10) + $item[5] + $item[17];
if($item[20]){$bukilv="+ $item[20]";}
if($item[22]){$bogulv="+ $item[22]";}
if($chara[138] eq ""){$pename=$chara[39];}else{$pename=$chara[138];}
       print <<"EOM";
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">�L�����N�^�[�f�[�^</td></tr>
EOM
if($chara[50] == 1){
       print <<"EOM";
<td rowspan="6" align="center" valign=bottom class="b2">
EOM
}else{
       print <<"EOM";
<td rowspan="6" align="center" valign=bottom class="b2"><img src="$img_path/$chara_img[$chara[6]]">
EOM
}
$rensyo = int($chara[20]*100000)/100000;
       print <<"EOM";
<tr><td id="td2" class="b2">����</td><td align="right" class="b2">
<A onmouseover="up('$bukikoka')"; onMouseout="kes()"><font color="$g">$item[0] $bukilv</font></A></td>
<td id="td2" class="b2">�y�b�g</td><td align="center" class="b2">$pename</td></tr>
<tr><td id="td2" class="b2">�h��</td><td align="right" class="b2">
<A onmouseover="up('$bogukoka')"; onMouseout="kes()"><font color="$w">$item[3] $bogulv</font></A></td>
<td id="td2" class="b2">HP</td><td align="center" class="b2">$chara[42]\/$chara[43]</td></tr>
<tr><td id="td2" class="b2">�A�N�Z�T���[</td><td align="right" class="b2">
<A onmouseover="up('$acskoka')"; onMouseout="kes()">$item[6]</A></td>
<td id="td2" class="b2">�y�b�g���x��</td><td align="center" class="b2">$chara[46]</td></tr>
<tr><td id="td2" class="b2">�̍�</td><td align="center" class="b2"><font color=yellow>$syou</font></td>
<td id="td2" class="b2">�y�b�g�o���l</td><td align="center" class="b2">$chara[40]\/$chara[41]</td></tr>
</table>

<table width='100%'>
<tr><td id="td1" colspan="5" class="b2" align="center">�X�e�[�^�X</td></tr>
<tr><td class="b1" id="td2">�P�Ǔx</td><td class="b2">$chara[64]</td>
<td id="td2" align="center" class="b1">���l�x</td><td class="b2"><b>$chara[65]</b></td></tr>
<tr><td class="b1" id="td2">�W���u</td><td class="b2">$chara_syoku[$chara[14]]</td>
<td id="td2" align="center" class="b1">�W���uLV</td><td class="b2"><b>$chara[33]</b></td></tr>
<tr><td class="b1" id="td2">���x��</td><td class="b2">$chara[18]</td>
<td class="b1" id="td2">�o���l</td><td class="b2">$chara[17]/$next_ex</td></tr>
<tr><td class="b1" id="td2">HP</td><td class="b2">$chara[15]\/$chara[16]</td>
<td class="b1" id="td2">����</td><td class="b2">$chara[19]\/$gold_max</td></tr>
<tr><td class="b1" id="td2">������</td><td class="b2">$hit_ritu</td>
<td class="b1" id="td2">����</td><td class="b2">$sake</td></tr>
<tr><td class="b1" id="td2">��S��</td><td class="b2">$waza_ritu %</td>
<td class="b1" id="td2">�K�E��</td><td class="b2">$hissatu_ritu %</td></tr>
<tr><td class="b1" id="td2">�p�[�e�B</td><td class="b2">$chara[61]</td>
<td class="b1" id="td2">�M���h</td><td class="b2">$chara[66]</td></tr>
<tr><td class="b1" id="td2">�A�풆�A����</td><td class="b2">$rensyo</td>
<td class="b1" id="td2">�]����</td><td class="b2">$chara[37]</td>
</tr>
<tr><td colspan="4">
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">�\\��\�l</td></td></tr>
</table>
<table width="100%">
<tr><td class="b1" id="td2">STR</td>
<td align="left" class="b2"><b>$chara[7] + $item[8]</b></td>
<td class="b1" id="td2">INT</td>
<td align="left" class="b2"><b>$chara[8] + $item[9]</b></td></tr>
<tr><td class="b1" id="td2">DEX</td>
<td align="left" class="b2"><b>$chara[9] + $item[10]</b></td>
<td class="b1" id="td2">VIT</td>
<td align="left" class="b2"><b>$chara[10] + $item[11]</b></td></tr>
<tr><td class="b1" id="td2">LUK</td>
<td align="left" class="b2"><b>$chara[11] + $item[12]</b></td>
<td class="b1" id="td2">EGO</td>
<td align="left" class="b2"><b>$chara[12] + $item[13]</b></td></tr>
</table></td></tr>
<tr>
<td class="b1" id="td2">�`�����s�I����ڎw��</td>
EOM
$gold = int($winner[50] / 10000);
if($chara[140]==2){print "<form action=\"$scriptb2\" name=\"champ_battle\">";}
elsif($chara[140]==3){print "<form action=\"$scriptb3\" name=\"champ_battle\">";}
elsif($chara[140]==4){print "<form action=\"$scriptb4\" name=\"champ_battle\">";}
elsif($chara[140]==5){print "<form action=\"$scriptb5\" name=\"champ_battle\">";}
else{print "<form action=\"$scriptb\" name=\"champ_battle\">";}
	print <<"EOM";
<td colspan="3" align="center" class="b2">
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
EOM
	if ($winner[0] eq $chara[0]) {
		print "���݃`�����v�Ȃ̂œ����܂���\n";
	} elsif ($winner[40] eq $chara[0] and $chanp_milit == 1) {
		print "�`�����v�Ɛ��������Ȃ̂Ŕ��ē����܂���\n";
	}elsif($ltime > $b_time) {
		print "<input type=\"submit\" class=btn value=\"�`�����v�ɒ���\">\n";
	}else{        print "<input type=submit class=btn value=\"�`�����v�ɒ���\" name=\"battle_start\" disabled>\n";    }
	print <<"EOM";
<br>���܋��F$gold G
</td></form>
</tr>
EOM
if($chara[0] eq "jupiter" or $chara[18] > 10000){
	print <<"EOM";
<tr><td class="b1" id="td2">�`���b�g�����U������</td>
<form action="kougeki.cgi" >
<td colspan="3" align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�U���I�I" disabled>
<br>���Ǘ��l�A�������̓��x��10000�ȏ�̐l�̂݁B
</td></form></tr>
EOM
}
	print <<"EOM";
</table>
</td>
EOM

# ��������E�����̃e�[�u��
	print <<"EOM";
<td valign="top">
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">�X�̎{��</td></tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y���̏h�z(<b>$yado_daix</b>G)</td>
<td bgcolor="#cbfffe" align="center">�y���X�X�z</td>
<td bgcolor="#cbfffe" align="center">�y�A�C�e���q�Ɂz</td>
<td bgcolor="#cbfffe" align="center">�y��s�z</td>
</tr>
<tr>
<form action="$scripty" >
<td align="center" class="b2">
<input type=hidden name=mode value="yado">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�̗͂���"></td>
</form>
<form action="shops.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���X�X"></td>
</form>
<form action="$script_souko" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�A�C�e���q��"></td>
</form>
<form action="$script_bank" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��s"></td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�X�e�[�^�X�̕ύX�z</td>
<td bgcolor="#cbfffe" align="center">�y�X�e�U�菊�z</td>
<td bgcolor="#cbfffe" align="center">�y�]�E�̐_�a�z</td>
<td bgcolor="#cbfffe" align="center">�y�A�r���e�B�z</td>
</tr><tr>
<td align="center" class="b2">
<form action="$scriptst" >
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�[�^�X�̕ύX">
</td>
</form>
<form action="shop_ability.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�X�e�U�菊">
</td>
</form>
<form action="syokuchange.cgi" >
<td align="center" class="b2">
<input type=hidden name=mode value=tensyoku>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�]�E�̐_�a">
</td>
</form>
<form action="abilitychange.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�A�r���e�B">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�y�b�g�z</td>
<td bgcolor="#cbfffe" align="center">�y�q��z</td>
<td bgcolor="#cbfffe" align="center">�y�t���}�z</td>
<td bgcolor="#cbfffe" align="center">�y����z</td>
</tr>
<tr>
<form action="petsts.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�y�b�g">
</td>
</form>
<form action="bokujyo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�q��">
</td>
</form>
<form action="market.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="�t���}">
</td>
</form>
<form action="sakaba.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="����">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�N�G�X�g�z</td>
<td bgcolor="#cbfffe" align="center">�y�b�艮�z</td>
<td bgcolor="#cbfffe" align="center">�y�������z</td>
<td bgcolor="#cbfffe" align="center">�y�V���E�z</td>
</tr><tr>
<form action="quest.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�N�G�X�g">
</td>
</form>
<form action="kaji.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�b�艮">
</td>
</form>
<form action="seizou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="������">
</td>
</form>
<form action="anotherworld.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�V���E">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�ً}���z</td>
<td bgcolor="#cbfffe" align="center">�y�\\��\���z</td>
<td bgcolor="#cbfffe" align="center">�y�z�R�z</td>
<td bgcolor="#cbfffe" align="center">�y��񉮁z</td>
</tr><tr>
<form action="kinkyuu.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�ً}��">
</td>
</form>
<form action="yohou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�\\��\��">
</td>
</form>
<form action="kouzan.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�z�R">
</td>
</form>
<form action="jyoho.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�M���h�z</td>
<td bgcolor="#cbfffe" align="center">�y�U���z</td>
<td bgcolor="#cbfffe" align="center">�y���z</td>
<td bgcolor="#cbfffe" align="center">�y�x�z�Ҏ{�݁z</td>
</tr><tr>
<form action="guild.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�M���h">
</td>
</form>
<form action="g_b.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�U���">
</td>
</form>
<form action="hatake.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��">
</td>
</form>
<form action="sihai.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�x�z�Ҏ{��">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y��̑g�D�z</td>
<td bgcolor="#cbfffe" align="center">�y�܋���z</td>
<td bgcolor="#cbfffe" align="center">�y�Y�����z</td>
<td bgcolor="#cbfffe" align="center">�y�����L���O�z</td>
</tr>
<tr>
<form action="sosiki.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="��̑g�D">
</td>
</form>
<form action="syoukin.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�܋���">
</td>
</form>
<form action="keimusyo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�Y����">
</td>
</form>
<form action="seirank.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�����L���O">
</td>
</form>
</tr>
EOM
if($chara[70] < 1){
	print <<"EOM";
<tr>
<td bgcolor="#cbfffe" align="center">�y�������z</td>
<td bgcolor="#cbfffe" align="center">�y�z�����z</td>
<td bgcolor="#cbfffe" align="center">�y���E�˔j�z</td>
<td bgcolor="#cbfffe" align="center"></td>
</tr>
<tr>
<form action="gosei.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="������">
</td>
</form>
<form action="haigo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�z����">
</td>
</form>
<form action="genkai.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���E�˔j">
</td>
</form>
<td align="center" class="b2">
</td>
</tr>
EOM
}else{
	print <<"EOM";
<tr>
<td bgcolor="#cbfffe" align="center">�y�������z</td>
<td bgcolor="#cbfffe" align="center">�y�H�[�z</td>
<td bgcolor="#cbfffe" align="center">�y���H���z</td>
<td bgcolor="#cbfffe" align="center">�y�˗����z</td>
</tr>
<tr>
<form action="seityo.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="������">
</td>
</form>
<form action="koubou.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�H�[">
</td>
</form>
<form action="kako.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���H��">
</td>
</form>
<form action="ippatu.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�˗���">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y���O�ύX���z</td>
<td bgcolor="#cbfffe" align="center">�y�A�C�R�����z</td>
<td bgcolor="#cbfffe" align="center">�y���~�z</td>
<td bgcolor="#cbfffe" align="center">�y�ŋ�ԁz</td>
</tr>
<tr>
<form action="name.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���O�ύX��">
</td>
</form>
<form action="icon.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�A�C�R����">
</td>
</form>
<form action="yashiki.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���~">
</td>
</form>
<form action="yami.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�ŋ��">
</td>
</form>
</tr>
<tr>
<td bgcolor="#cbfffe" align="center">�y�P�����z</td>
<td bgcolor="#cbfffe" align="center">�y���`�̊فz</td>
<td bgcolor="#cbfffe" align="center">�y�����̊فz</td>
<td bgcolor="#cbfffe" align="center">�y�֗����z</td>
</tr>
<tr>
<form action="kunren.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�P����">
</td>
</form>
<form action="seigi.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="���`�̊�">
</td>
</form>
<form action="akuma.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�����̊�">
</td>
</form>
<form action="benri.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�֗���">
</td>
</form>
</tr>
EOM
}
	print <<"EOM";
</table>
<table width="100%">
<tr><td id="td1" colspan="2" class="b2" align="center">�`���ɏo������</td></tr>
<tr>
<td class="b1" id="td2">���ӂ̒T��</td>
<form action="$scriptm"  name="monster_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=monster>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
if(!$chara[21]) {print "��x�`�����s�I���Ɛ���ĉ�����\n";
} else { 
	if($chara[140]==2){
		$opt = "<option value=\"monster8\">�C�G���[���[���h";
	} elsif($chara[140]==3){
		$opt = "<option value=\"monster9\">���b�h���[���h";
	} elsif($chara[140]==4){
		$opt = "<option value=\"monster10\">�h���S�����[���h";
		$opt .= "<option value=\"monster12\">�h���S���w�u��";
	} elsif($chara[140]==5){
		$opt = "<option value=\"monster17\">�V�E";
	} else {
		$opt = <<"EOM";
		<option value="monster0">���������e���B�[�k
		<option value="monster1">���A�����H�X
		<option value="monster2">��Ȃ��̓D��
		<option value="monster3">�ŎR���`���������b�c
		<option value="monster4">�_�[�N�E�G���A
		<option value="monster5">�_�̓��G�����@�[�k
		<option value="monster6">�X�y�V�����G���[�g
		<option value="monster7">���҂䂭�ꏊ
EOM
	}
	if ($chara[140]!=5 and $chara[70] >= 1) {
		$opt .= "<option value=\"monster15\">�K�b�J����\n";
		$opt .= "<option value=\"monster16\">�I���̒�\n";
		$opt .= "<option value=\"monster30\">���L��\n";
		$opt .= "<option value=\"monster31\">���L���n��\n";
		$opt .= "<option value=\"monster14\">�T���^�̊�n\n";
		#$opt .= "<option value=\"monster18\">�e�X�g��\n";
	}
	if ($chara[93]>0) {
		$opt .= "<option value=\"monster29\">�x�@��\n";
	}
	if ($chara[140]!=5 and $chara[163] >= 1) {
		$opt .= "<option value=\"monster28\">�����W���s�^���̖{���n\n";
	}
	if ($chara[127] == 1 or $chara[176] == 1) {
		$opt .= "<option value=\"monster27\">�������̏�\n";
	}
	if ($ltime >= $m_time or !$chara[21]) {
		print <<"EOM";
		<select name="mons_file">$opt</select>
		<input type=submit class=btn value="�����X�^�[�Ɠ���">
EOM
	}else{
		print <<"EOM";
		<select name="mons_file" disabled>$opt</select>
		<input type=submit class=btn value="�����X�^�[�Ɛ키" name="battle_start" disabled>
EOM
	}
	print <<"EOM";
	</td>
	</form>
</tr>
<tr><td colspan=2>���C�s�̗��ɂ����܂��B</td></tr>
EOM
}
if($chara[27]%5 == 0){
	print <<"EOM";
<tr>
<td class="b1" id="td2">�ˑR�̏o��</td>
<form action=\"$scriptm\" method=\"post\" name="gennei_battle">
<td align=\"center\" class=\"b2\">
<input type=hidden name=mode value=genei>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "�P�x�����X�^�[�Ɛ���ĉ�����\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"���e�̏��\">\n";
	} else {
		print qq|<input type=submit class=btn value="���e�̏��" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>�����󂪖���ƌ�����u���e�̏�v�ɂ����܂��B</td></tr>
EOM
}
	print <<"EOM";
<tr>
<td class="b1" id="td2">���W�F���h�v���C�X</td>
<form action="$script_legend"  name="legend_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=boss>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21] || $chara[28] != $bossd) {
		print "�P�x�����X�^�[�Ɛ���ĉ�����\n";
	} else {
		my $opt = qq|<option value="0">���킳�̂ق���\n|;
		if ($chara[32] > 0) {
			$opt .= "<option value=\"1\">�Â̐_�a\n";
		}
		if ($chara[32] > 1) {
			$opt .= "<option value=\"2\">�E�҂̓��A\n";
		}
		if ($chara[32] > 2) {
			$opt .= "<option value=\"3\">�K�C�A�t�H�[�X\n";
		}
		if ($chara[193]==1){
			$opt .= "<option value=\"4\">�A���N�h�����t�H�[�X\n";
		}
		if ($ltime >= $m_time or !$chara[21]) {
			print <<"EOM";
			<select name="boss_file">$opt</select>
			<input type=submit class=btn value="�`���ɒ���">
EOM
		} else {
			print <<"EOM";
			<select name="boss_file" disabled>$opt</select>
			<input type=submit class=btn value="�`���ɒ���" name="battle_start" disabled>
EOM
		}
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>���ł񂹂̏ꏊ�֖K��邱�Ƃ��ł��܂��B</td></tr>
EOM
	print <<"EOM";
<tr>
<td class="b1" id="td2">�M���h�_���W����</td>
<form action="guild_battle.cgi"  name="guild_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=guild_battle>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	$opt = <<"EOM";
		<option value="guild0">�V�E�ւ̓���
		<option value="guild1">�V�E�̕���
EOM
	if($chara[70]>=1 and $chara[18]>1000){
	$opt .= <<"EOM";
		<option value="guild2">���V��
EOM
	}
	if(!$chara[66]){
		print "�M���h�ɉ������Ă��܂���B<br>\n";
	} elsif ($chara[70]==1 and $chara[18]<70){
		print "���x��������܂���B<br>\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		print <<"EOM";
		<select name="guild_file">$opt</select>
		<input type=submit class=btn value="�M���h�_���W������">
EOM
    } else {
		print <<"EOM";
		<select name="guild_file" disabled>$opt</select>
		<input type=submit class=btn value="�M���h�_���W������" name="battle_start" disabled>
EOM
    }

	print <<"EOM";
</td></form></tr>
<tr><td colspan=2>���M���h�����҂̂ݒ���ł���A���ɂ����낵���_���W�����ł��B</td></tr>
EOM
	print <<"EOM";
<tr>
<td class="b1" id="td2">�ِ��E</td>
<form action="$scriptm"  name="isekai_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=isekiai>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if ($chara[18] < $isekai_lvl) {
		print "���x����$isekai_lvl�𒴂���܂ōs���܂���B<br>\n";
	} elsif ($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"�ِ��E�֍s��\"><br>\n";
	} else {
		print qq|<input type=submit class=btn value="�ِ��E�֍s��" name="battle_start" disabled>\n|;
	}

	print <<"EOM";
</td></form></tr>
<tr><td colspan=2>���_�X�̗̈�ƌ����邱�̐��E�ɑ����ӂ݂���āA�����ɋA�������̂͒N��l���Ȃ��E�E�E</td></tr>
EOM
open(IN,"sihaisya.cgi");
@sihai_data = <IN>;
close(IN);
foreach (@sihai_data) {
	@sihaisya = split(/<>/);
	if($sihaisya[0]){last;}
}
$point= int($sihaisya[2]/10)+int($sihaisya[11] * $sihaisya[14] * ($sihaisya[12]+$sihaisya[13])/ 2 * 3);
if($point <= 10000){
	print <<"EOM";
<tr>
<td class="b1" id="td2">�x�z�҃_���W����</td>
<form action=\"$scriptm\" method=\"post\" name="sihai_battle">
<td align=\"center\" class=\"b2\">
<input type=hidden name=mode value=sihaid>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "�P�x�����X�^�[�Ɛ���ĉ�����\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"�x�z�҃_���W����\">\n";
	} else {
		print qq|<input type=submit class=btn value="�x�z�҃_���W����" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr>
<tr><td colspan=2>�����ꗿ�F$sihaisya[2] G</td></tr>
EOM
}
if($chara[27]%2 == 0 and $chara[70] >= 1){
	print <<"EOM";
<tr><td class="b1" id="td2">�ˑR�̏o��</td>
<form action="$scriptm"  name="ijigen_battle">
<td align="center" class="b2">
<input type=hidden name=mode value=ijigen>
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
EOM
	if (!$chara[21]) {
		print "�P�x�����X�^�[�Ɛ���ĉ�����\n";
	} elsif($ltime >= $m_time or !$chara[21]) {
		print "<input type=submit class=btn value=\"�����̋��Ԃ�\"><br>\n";
	} else {
		print qq|<input type=submit class=btn value="�����̋��Ԃ�" name="battle_start" disabled>\n|;
	}
	print <<"EOM";
</td>
</form>
</tr><tr><td colspan=2>�����̐��ōł��댯�ȏꏊ�ł��B�o��Ȃ��ɂ͂����Ȃ��ł��������B</td></tr>
EOM
}
	print <<"EOM";
</table></td></tr>
</table>
EOM

	&footer;

	exit;
}
