#!/usr/local/bin/perl

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
<form action="stdefshop.cgi" >
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

&item_view;

exit;

#----------------#
#  �A�C�e���\��  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	&item_load;

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>�������h�</h1>
<hr size=0>

<FONT SIZE=3>
<B>�������h��̃}�X�^�[</B><BR>
�u������������Ⴂ�I���̑嗤�̒�����A�����̏��i���ꋉ�̋�������I<BR>
�@���A�Ȃ񂾂��A<B>$chara[4]</B>����Ȃ����B���C�ɂ��Ă������H<br>
<font color="red" size=5>�����Ȃ��̂ɏ��i����Ɏ������D�_�Ƃ݂Ȃ���</font>
<BR>
�@�܂��A������茩�Ă����Ă���B
<BR><BR>���������I�ŋߑ����i�̉����͂�߂��񂾁B�v
</FONT>
<br><hr>���݂̏������F$chara[19] �f<br>
<form action="stdefshop.cgi" >
<table>
EOM

	foreach (@item_array) {
		($ino,$iname,$idmg,$igold) = split(/<>/);
		print "<tr><td class=b1 align=\"center\">\n";
		print "<input type=radio name=item_no value=\"$ino\">";
		print "</td><td align=right class=b1>$ino</td><td class=b1>$iname</td><td align=right class=b1>$idmg</td><td align=right class=b1>$igold</td>\n";
		print "</tr>\n";
	}

	print <<"EOM";
</table>
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=submit class=btn value="�h�����Ɏ��">
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($in{'kane'}>0){$chara[19]-=$in{'kane'};}
	elsif($chara[19] < $i_gold) { $bgg=1; }
	else { $chara[19] = $chara[19] - $i_gold; }

	$chara[26] = $host;
if($bgg!=1){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}

	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>1000000<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>���������퉮�̃}�X�^�[</B><BR>
�u���x����`�I<br>
����������͂��񂽂̕���q�ɂɑ����Ă�������I
�v</font>
<hr size=0>
EOM
	&shopfooter;

	&footer;
}else{

	&header;

	print <<"EOM";
<FONT SIZE=5 color="red">
<B>���������퉮�̃}�X�^�[</B><BR>
�u�M�l�E�E�E�����Ȃ��̂ɖh�����Ɏ��Ƃ͗ǂ��x������<br>
����������ł���������A�n���������낵�����|��̌����邱�ƂɂȂ邼�B
�v</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�h������ɖ߂�">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=nigeru>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="�h��������ē��S����B">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=tatakau>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="�X��Ɛ키">
</form>
EOM
if($chara[64]==100){
	print <<"EOM";
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=negiri>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="�l�؂������">
</form>
EOM
}
print "<hr size=0>";
}
	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub nigeru {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;
if(int(rand(10))==1){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I$back_form");
	}
	
	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>�������h��̃}�X�^�[</B><BR>
�u�҂ăS���@�@�@�@<br>
�E�E�E�E�E�E�����A�����������B<br>
�o���Ă��E�E�E�B
�v</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]�l���������҂ɒǂ��Ă���悤�ł��B";

	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

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
		$eg="$chara[4]�l�͈��ɐ��܂肷���A�܋���(�܋��F$syoukingaku G)�ƂȂ�܂����B";

		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

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
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[141]=1;
	$chara[13]-=1;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>�������h��̃}�X�^�[</B><BR>
�u��������Ǝv���Ă��̂��H�M�l�E�E�E��������ȁB<br>
����������ł���������A�n���������낵�����|��̌����邱�ƂɂȂ�A�ƁB<br>
������Ă��x�����E�E�E�B���O�ɂ͋��낵���􂢂����������̂��B
�v</font>
$back_form
<hr size=0>
EOM
}

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub tatakau {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}

	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;
	if($chara[18]>5000){$byouyy=int(19701+rand(400));}
	else{$byouyy=int(10000+rand($chara[18]+12500));}
if($byouyy>20000){
	$lock_file = "$lockfolder/sdefe$in{'id'}.lock";
	&lock($lock_file,'SD');
	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	$souko_def_num = @souko_def;

	if ($souko_def_num >= $item_max) {
		&error("�h��q�ɂ������ς��ł��I$back_form");
	}
	
	push(@souko_def,"$i_no<>$i_name<>$i_dmg<>0<>$ihit<>\n");

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	&unlock($lock_file,'SD');

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=6 color="red">
<B>�������h��̃}�X�^�[</B><BR>
�u���E�E�E�����͒��q���������B<br><br>
�o���Ă��E�E�E�B
�v</font>
<hr size=0>
EOM

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');

	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);

	$mes_sum = @chat_mes;

	if($mes_sum > $mes_max) { pop(@chat_mes); }

	$eg="$chara[4]�l���������h��̓X�����������悤�ł��B";

	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

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
		$eg="$chara[4]�l�͈��ɐ��܂肷���A�܋���(�܋��F$syoukingaku G)�ƂȂ�܂����B";

		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

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
}else{

	if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
	$chara[64]-=10;
	$chara[65]+=10;
	if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
	if($chara[64]<0){$chara[64]=0;}
	if($chara[65]>100){$chara[65]=100;}
	$chara[13]-=2;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;
	$byouyy-=10000;
	print <<"EOM";
<FONT SIZE=6 color="red">
<B>$byouyy�b�ŏu�E���ꂽ�B</B><BR><BR>
<B>�������h��̃}�X�^�[</B><BR>
�u�U�R���B���̒��x�̘r�ł����ւ���񂶂�˂��B�A��ȁBAP�����Ƃ��Ă�����悗
�v</font>
$back_form
<hr size=0>
EOM
}

	exit;
}
sub negiri {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[141]>0){&error("�����ɂ͓���Ȃ��������E�E�E");}

	open(IN,"data/def/stdef.ini");
	@item_array = <IN>;
	close(IN);

	$hit=0;
	foreach(@item_array){
		($i_no,$i_name,$i_dmg,$i_gold,$ihit) = split(/<>/);
		if($in{'item_no'} eq "$i_no") { $hit=1;last; }
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$ok=1;
	if($i_gold > 100000000){$kane=int($i_gold / 100);}else{$kane=int($i_gold/2);}
	if($kane > $chara[19]){$ok=0;}

	$chara[26] = $host;

	&header;
if($ok==1){
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>�������h��̃}�X�^�[</B><BR>
�u�����E�E�E�m���ɌN�́A�l�̗ǂ������Ȑl�Ԃ��E�E�E�B<br>
�C�ɂ��������I����A���񂽂̔�����l�i�ɒl�������Ă��B<br>
�ǂ����A$kane�f�Ŕ���Ȃ����H�v</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=kane value=$kane>
<input type=hidden name=item_no value=$in{'item_no'}>
<input type=submit class=btn value="����">
</form>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="����Ȃ�">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=5 color="red">
<B>�������h��̃}�X�^�[</B><BR>
�u�����E�E�E�m���ɌN�́A�l�̗ǂ������Ȑl�Ԃ��E�E�E�B<br>
�����A������Ȃ�ł��N�̏������͒Ⴗ����ȁB���̒l�i�ł͔���Ȃ���B<br>
$kane�f���炢�͗p�ӂ��Ă���B�v</font>
<form action="stdefshop.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="�h������ɖ߂�">
</form>
<hr size=0>
EOM
}
	exit;
}