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
<form action="itemya2.cgi" >
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
	if($chara[70]<1){&error("�˔j�O�ł�");}	
	if($chara[18]<100){&error("���x��������܂���");}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	open(IN,"freekako2.cgi");
	@kako_array2 = <IN>;
	close(IN);

	&header;

	print <<"EOM";
<h1>���H�i�f�ރt���[�}�[�P�b�g</h1>
<hr size=0>
<FONT SIZE=3><B>�ӂ�[�܁[�����Ƃ̐l</B><BR>
�u<B>$chara[4]</B>���ȁB<br>
�����ł́A���H�i�f�ނ̔������o���邼�B��{�I�ȃ��[���̓t���[�}�[�P�b�g�Ƃقړ������B<br>
<font color="red" size=4><b>�������A���z�͂P���f�P�ʁA�P�O�O�O���f�܂ł̐ݒ�ƂȂ�B</b></font>�v<br></FONT>
���݂̎������F$chara[19]�@�f
<hr>

<table width = "100%">
	<tr>
	<td width = "49%" align = "center" valign = "top">
	<form action="./itemya2.cgi" >
	<table border=1>
		<tr><th></th><th>���H�i�f�ޖ�</th><th>��</th><th>���i</th></tr>
		<tr>
EOM
		$i=1;
		#�o�i�҂̂h�c�A�l�i�A�m���A���O�A��
		foreach(@kako_array){
			($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
			$i_gold=$i_gold/100000000;
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$i></td>
			<td>$i_name</td><td>$i_kazu</td><td>$i_gold���f</td></tr>
EOM
		$i++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=buki>
	<input type=submit class=btn value="�A�C�e���𔃂�">
	</form>
	</td>

	<td width = "49%" align = "center" valign = "top">
	<form action="./itemya2.cgi" >
	<table border=1>
		<tr><th></th><th>���H�i�f�ޖ�</th><th>��</th><th>����</th></tr>
		<tr>
EOM
		$g=1;
		#�o�i�҂̂h�c�A�l�i�A�m���A���O�A��
		foreach(@kako_array2){
			($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
			if($i_name){
			print <<"EOM";
			<tr><td><input type=radio name=item_no value=$g></td>
			<td>$i_name</td><td>$i_kazu</td><td>$i_gold</td></tr>
EOM
			}
		$g++;
		}
			print <<"EOM";
		</tr>
		</table>
	<p>
	<input type=hidden name="id" value="$chara[0]">
	<input type=hidden name="mydata" value="$chara_log">
	<input type=hidden name=mode value=bogu>
	<input type=submit class=btn value="�P�������A�C�e�����Q�b�g����">
	</form>
	</td>
	</tr></table>

<form action="./itemya2.cgi" >
<hr>
<table width = "100%">
<tr>
<td width = "49%" align = "center" valign = "top">
���H�i�f��
<table width = "98%">
<tr><th></th><th nowrap>�Ȃ܂�</th><th nowrap>����</th></tr>
EOM
	$i = 0;
	foreach (@isi) {
		if($_>0){
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			($sozai) = split(/<>/,$sozai_data[$i]);
			$g=$i+1;
			print << "EOM";
			<tr><td class=b1 align="center"><input type=radio name=soubi value=$g></td>
			<td class=b1 nowrap>$sozai</td>
			<td align=right class=b1>$_</td>
			</tr>
EOM
		}
		$i++;
	}
		print << "EOM";
</table>
</td>
<td width = "49%" align = "center" valign = "top">

<table width = "98%">
<tr><th></th><th nowrap></th><th nowrap></th><th nowrap></th></tr>
EOM
	$i = 100;
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
</table>
<p>
���l�F<input type="text" name="sgold" size=30>���f</td>
���F<input type="text" name="skazu" size=10></td>
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemu>
<input type=submit class=btn value="����">
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
sub buki {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if(!$in{'item_no'}){&error("�I�����Ă�������");}

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	$hit=0;$ii=1;
	foreach(@kako_array){
		($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($i_id eq $chara[0]){
		&header;
	print <<"EOM";
<FONT SIZE=3>
<B>�ӂ�[�܁[�����Ƃ̐l</B><BR>
�u����͂��񂽂̏o�i����������I<br>
�Ԃ����Ƃ͂ł��Ȃ����ȁA����Ȃ��Ȃ牴��������Ă�낤���H�v</font>
<form action="./itemya2.cgi" >
<input type=hidden name="item_no" value="$in{'item_no'}">
<input type=hidden name="id" value="$chara[0]">
<input type=hidden name="mydata" value="$chara_log">
<input type=hidden name=mode value=itemsyobun>
<input type=submit class=btn value="�͂�">
</form>
<hr size=0>
EOM
	}else{
	if($chara[19] < $i_gold) { &error("����������܂���"); }
	else { $chara[19] -= $i_gold; }

	$chara[26] = $host;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$isi[$i_no]+=$i_kazu;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	$ii-=1;

	splice(@kako_array,$ii,1);

	open(OUT,">freekako.cgi");
	print OUT @kako_array;
	close(OUT);

	open(IN,"./charalog/$i_id.cgi") || &error("�L�����N�^�[��������܂���$ENV{'CONTENT_LENGTH'}");
	$charan_log = <IN>;
	close(IN);
	@charan = split(/<>/,$charan_log);
	$charan[34] += $i_gold;
	$charan[137] -= 1;
	if($charan[137]<0){$charan[137]=0;}
	$new_charan = '';
	$new_charan = join('<>',@charan);
	$new_charan .= '<>';
	open(OUT,">./charalog/$i_id.cgi");
	print OUT $new_charan;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	open(IN,"$chat_file");
	@chat_mes = <IN>;
	close(IN);
	$mes_sum = @chat_mes;
	if($mes_sum > $mes_max) { pop(@chat_mes); }
	($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
	$mon = $mon+1;$year = $year +1900;
	if($ilv>0){$ibuki="+ $ilv";}else{$ibuki="";}
	$eg="$charan[4]�l���o�i���Ă���$i_name($i_kazu��)���A$chara[4]�l��$i_gold G�ōw�����܂����B";
	unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

	open(OUT,">$chat_file");
	print OUT @chat_mes;
	close(OUT);

	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�ӂ�[�܁[�����Ƃ̐l</B><BR>
�u�ق��A����I�����Ȃ��B�v</font>
<hr size=0>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub bogu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	if(!$in{'item_no'}){&error("�I�����Ă�������");}

	open(IN,"freekako2.cgi");
	@kako_array2 = <IN>;
	close(IN);

	$hit=0;$ii=1;
	foreach(@kako_array2){
		($i_id,$i_gold,$i_no,$i_name,$i_kazu) = split(/<>/);
		@array2 = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	if($chara[129] == $mday) { &error("�����B"); }
	else { $chara[129] = $mday; }

	$chara[26] = $host;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$isi[$i_no]+=1;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	$ii-=1;
	if($i_kazu>1){
		$array2[4]-=1;
		$new_isi2 = '';
		$new_isi2 = join('<>',@array2);
		$new_isi2 .= '<>';
		$kako_array2[$ii]=$new_isi2;
	}else{splice(@kako_array2,$ii,1);}

	open(OUT,">freekako2.cgi");
	print OUT @kako_array2;
	close(OUT);

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	$lock_file = "$lockfolder/messa$in{'id'}.lock";
	&lock($lock_file,'MS');
		
	&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�ӂ�[�܁[�����Ƃ̐l</B><BR>
�u�ق��A����I�����Ȃ��B�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub itemu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if(!$in{'soubi'}) {&error("�o�i������̂�I�����Ă�������");}
	if($chara[137]>=4){&error("�����ɏo�i�ł��鐔�͂S�܂łł��B");}
	$soubi = $in{'soubi'}-1;
	$sgold = $in{'sgold'}*100000000;
	$skazu = $in{'skazu'};

	if(!$sgold) {&error("���z��ݒ肵�Ă�������");}
	if(!$skazu) {&error("����ݒ肵�Ă�������");}

	if($in{'sgold'} =~ /[^0-9]/){
		&error('�G���[�I���l�s���̂��ߎ󂯕t���܂���');
	}
	if($sgold > 100000000000){&error("�������܂��B�ő剿�i�͂P�O�O�O���f�ł��B");}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if($isi[$soubi]<$skazu){&error("����܂���");}
	else{$isi[$soubi]-=$skazu;}

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	open(IN,"freekako.cgi");
	@kako_array = <IN>;
	close(IN);

	$ckazu=0;
	foreach(@kako_array){
		@array = split(/<>/);
		if($array[0] eq $chara[0]){$ckazu+=1;}
	}
	$chara[137]=$ckazu;
	if($chara[137]>=4){&error("�����ɏo�i�ł��鐔�͂S�܂łł��B");}
	else{
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		($sozai) = split(/<>/,$sozai_data[$soubi]);
		push(@kako_array,"$chara[0]<>$sgold<>$soubi<>$sozai<>$skazu<>\n");
		open(OUT,">freekako.cgi");
		print OUT @kako_array;
		close(OUT);
	}

	$chara[137]++;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>�ӂ�[�܁[�����Ƃɏo�i���܂���</h1>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub itemsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"freekako.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=1;
	foreach(@item_chara){
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;
	$ii-=1;
	splice(@item_chara,$ii,1);

	open(OUT,">freekako.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[137] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�ӂ�[�܁[�����Ƃ̐l</B><BR>
�u�ق����A���񂪂Ƃ�I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub defsyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"freedef.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){				($i_id,$i_gold,$i_no,$i_name,$i_dmg,$igold,$ihit,$i_setumei,$ilv,$iexp) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	open(OUT,">freedef.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u�������Ă������I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub acssyobun {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/sitem$in{'id'}.lock";
	&lock($lock_file,'SI');

	open(IN,"freeacs.cgi");
	@item_chara = <IN>;
	close(IN);
	$hit=0;$ii=0;

	foreach(@item_chara){
($i_id,$i_gold,$a_no,$a_name,$a_gold,$a_kouka,$a_0up,$a_1up,$a_2up,$a_3up,$a_4up,$a_5up,$a_hitup,$a_kaihiup,$a_wazaup,$a_ex) = split(/<>/);
		if($in{'item_no'} == $ii) { $hit=1;last; }
		$ii++;
	}
	if(!$hit) { &error("����ȃA�C�e���͑��݂��܂���"); }

	$chara[26] = $host;

	splice(@item_chara,$ii,1);

	open(OUT,">freeacs.cgi");
	print OUT @item_chara;
	close(OUT);

	$chara[88] -= 1;

	&unlock($lock_file,'SI');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�t���[�}�[�P�b�g�̐l</B><BR>
�u�������Ă������I�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}