#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͉��L��3�l�ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p���� #
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B     	#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B   	#
#---------------------------------------------------------------#
# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �A�C�e�����C�u�����̓ǂݍ���
require 'item.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

# ���̃t�@�C���p�ݒ�
$backgif = $shop_back;
$midi = $shop_midi;

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="azukari.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");}
}
if($mode) { &$mode; }

&itemh;

exit;

#----------------#
#  �A�C�e���\��  #
#----------------#
sub itemh {

	&chara_load;

	&chara_check;

	if($chara[0] eq "test" or $chara[0] eq "test2"){&error("�e�X�g�L�����ł��B");}
	elsif($chara[18]<30000){&error("���x��������܂���B");}

	&item_load;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	
	open(IN,"azukari/item/$chara[0].cgi");
	@item_array = <IN>;
	close(IN);

	open(IN,"azukari/def/$chara[0].cgi");
	@def_array = <IN>;
	close(IN);

	open(IN,"azukari/acs/$chara[0].cgi");
	@acs_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>�a���菊</h1>
<hr size=0>
<FONT SIZE=3><B>�a����l</B><BR>
�u<B>�N��$chara[4]</B>���낤�B<br>
���͂₱�̐��E�ŌN�̎���m��Ȃ��l�͏��Ȃ����낤�B<br>
�������������ȃA�C�e������R�����Ă��邱�Ƃ��낤�B<br>
�����A���̐��E�ɐM�p�ł���q�ɂ͐����Ȃ��A�����Ă��邱�Ƃ��낤�B<br>
�����ŁA����"�a����l"�̏o�Ԃ��낤�B<br>
�N����a�������A�C�e���͑S�͂Ŏ�邾�낤�B<br>
�������A�P�̃A�C�e���ɂ��P���f�̎萔����Ⴄ���낤�B�v<br></FONT>
���݂̎������F$chara[19]�@�f
<hr>
<form action="./azukari.cgi" method="post">
<hr>
<table width = "100%">
<tr>
<td width = "30%" align = "center" valign = "top">
�a���Ă��镐��
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���l</th></tr>
EOM
	$i = 1;
	foreach (@item_array) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	open(IN,"$item_file");
	@item_item = <IN>;
	close(IN);
	foreach(@item_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$bukikoka = "�U���� $idmg<br>������ $ihit<br>���� $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
�h��
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���l</th></tr>
EOM
	$i = 101;
	foreach (@def_array) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibogu="+ $ilv";}else{$ibogu="";}
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$bogukoka = "�h��� $idmg<br>��� $ihit<br>���� $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
�����i
<table width = "98%">
<tr><th></th><th>�Ȃ܂�</th><th>����</th><th>���l</th></tr>
EOM

	$i = 201;
	foreach (@acs_array) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$i>
</td>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_msg</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$i++;
	}
		print << "EOM";
</table>
</td></table>
<p>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemr>
<input type=submit class=btn value="�Ԃ��Ă��炤">
</form>

<form action="./azukari.cgi" method="post">
<hr>
<table width = "100%">
<td width = "30%" align = "center" valign = "top">
����
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�U����</th><th nowrap>���l</th></tr>
EOM
	$t = 1;
	foreach (@souko_item) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	open(IN,"$item_file");
	@item_item = <IN>;
	close(IN);
	foreach(@item_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$bukikoka = "�U���� $idmg<br>������ $ihit<br>���� $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap><A onmouseover="up('$bukikoka')"; onMouseout="kes()">$iname $ibuki</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td>
<td width = "30%" align = "center" valign = "top">
�h��
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>�h���</th><th nowrap>���l</th></tr>
EOM
	$t = 101;
	foreach (@souko_def) {
		($ino,$iname,$idmg,$igold,$ihit,$ilv,$iexp) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$igold = int($igold / 4) * 3;
	}else{	$igold = int($igold / 3) * 2;}
	if($ilv>0){$ibogu="+ $ilv";}else{$ibogu="";}
	open(IN,"$def_file");
	@def_item = <IN>;
	close(IN);
	foreach(@def_item){
		($ci_no,$a,$c,$ci_gold,$v,$koka) = split(/<>/);
		if($ino eq $ci_no) {last;}
	}
	if(!$koka){$koka="���ɂȂ�";}
	$bogukoka = "�h��� $idmg<br>��� $ihit<br>���� $koka";
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap><A onmouseover="up('$bogukoka')"; onMouseout="kes()">$iname $ibogu</A></td>
<td align=right class=b1>$idmg</td>
<td align=right class=b1>$igold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td>
<td width = "40%" align = "center" valign = "top">
�����i
<table width = "98%">
<tr><th></th><th>�Ȃ܂�</th><th>����</th><th>���l</th></tr>
EOM

	$t = 201;
	foreach (@souko_acs) {($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
	if ($chara[55]==12 or $chara[56]==12 or $chara[57]==12 or $chara[58]==12){
		$ai_gold = int($ai_gold / 4) * 3;
	}else{	$ai_gold = int($ai_gold / 3) * 2;}
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=soubi value=$t>
</td>
<td class=b1 nowrap>$ai_name</td>
<td align=right class=b1>$ai_msg</td>
<td align=right class=b1>$ai_gold</td>
</tr>
EOM
	$t++;
	}
		print << "EOM";
</table>
</td></table>
<p>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemu>
<input type=submit class=btn value="�a����">
</form>
EOM


	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �Ԃ��Ă��炤  #
#----------------#
sub itemr {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	if(!$soubi) {&error("�A�C�e��������܂���");}

	$soubi-=1;

	open(IN,"azukari/item/$chara[0].cgi");
	@item_chara = <IN>;
	close(IN);
		
	open(IN,"azukari/def/$chara[0].cgi");
	@def_chara = <IN>;
	close(IN);

	open(IN,"azukari/acs/$chara[0].cgi");
	@acs_chara = <IN>;
	close(IN);

	$hit=0;
	$iii=0;

	foreach(@item_chara){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
		if($soubi == $iii) { $hit=1;last; }
		$iii++;
	}
	if(!$hit){
		$ddd=0;
		$soubi-=100;
		foreach(@def_chara){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
			if($soubi == $ddd) { $hit=2;last; }
		$ddd++;
		}
	}
	if(!$hit){
		$aaa=0;
		$soubi-=100;
		foreach(@acs_chara){
($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($soubi == $aaa) { $hit=3;last; }
		$aaa++;
		}
	}

	if($hit==1){
		if($chara[18]<10000){
			&error("���x��������܂���");
		}else{
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		
		splice(@item_chara,$soubi,1);
		open(OUT,">azukari/item/$chara[0].cgi");
		print OUT @item_chara;
		close(OUT);
		
	}elsif($hit==2){
		if($chara[18]<10000){
			&error("���x��������܂���");
		}else{
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@souko_def,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		
		splice(@def_chara,$soubi,1);
		open(OUT,">azukari/def/$chara[0].cgi");
		print OUT @def_chara;
		close(OUT);
	}elsif($hit==3){
		if($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(IN,"$souko_folder/acs/$chara[0].cgi");
			@souko_acs = <IN>;
			close(IN);
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);

		splice(@acs_chara,$soubi,1);
		open(OUT,">azukari/acs/$chara[0].cgi");
		print OUT @acs_chara;
		close(OUT);
		
	}else{
		&error("����ȃA�C�e���͑��݂��܂���");
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�Ԃ��Ă��炢�܂����B</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �a����@�@�@  #
#----------------#
sub itemu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$soubi = $in{'soubi'};
	if(!$soubi) {&error("�A�C�e��������܂���");}
	
	if($chara[19]<100000000){
		&error("����������܂���");
	}else{
		$chara[19]-=100000000;
	}

	$soubi-=1;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	$hit=0;
	$iii=0;

	foreach(@souko_item){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
		if($soubi == $iii) { $hit=1;last; }
		$iii++;
	}
	if(!$hit){
		$ddd=0;
		$soubi-=100;
		foreach(@souko_def){
			($i_no,$i_name,$i_dmg,$i_gold,$ihit,$ilv,$iexp) = split(/<>/);
			if($soubi == $ddd) { $hit=2;last; }
		$ddd++;
		}
	}
	if(!$hit){
		$aaa=0;
		$soubi-=100;
		foreach(@souko_acs){
($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
		if($soubi == $aaa) { $hit=3;last; }
		$aaa++;
		}
	}

	if($hit==1){
		if($chara[18]<10000){
			&error("���x��������܂���");
		}else{
			open(IN,"azukari/item/$chara[0].cgi");
			@item_chara = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@item_chara,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">azukari/item/$chara[0].cgi");
		print OUT @item_chara;
		close(OUT);
		
		splice(@souko_item,$soubi,1);
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		
	}elsif($hit==2){
		if($chara[18]<10000){
			&error("���x��������܂���");
		}else{
			open(IN,"azukari/def/$chara[0].cgi");
			@def_chara = <IN>;
			close(IN);
		}
		if($ilv<1){$ilv=0;$iexp=1;}
		push(@def_chara,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$ihit<>$ilv<>$iexp<>\n");
		
		open(OUT,">azukari/def/$chara[0].cgi");
		print OUT @def_chara;
		close(OUT);
		
		splice(@souko_def,$soubi,1);
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}elsif($hit==3){
		if($chara[18]<1000){
			&error("���x��������܂���");
		}else{
			open(IN,"azukari/acs/$chara[0].cgi");
			@acs_chara = <IN>;
			close(IN);
		}
		push(@acs_chara,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");

		open(OUT,">azukari/acs/$chara[0].cgi");
		print OUT @acs_chara;
		close(OUT);

		splice(@souko_acs,$soubi,1);
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}else{
		&error("����ȃA�C�e���͑��݂��܂���");
	}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�a�����Ă��炢�܂����B</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
