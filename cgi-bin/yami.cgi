#!/usr/local/bin/perl

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

	$back_form = << "EOM";
<br>
<form action="yami.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="�߂�">
</form>
EOM

# [�ݒ�͂����܂�]------------------------------------------------------------#

# �����艺�́ACGI�̂킩����ȊO�́A�ύX���Ȃ��ق����ǂ��ł��B

#-----------------------------------------------------------------------------#
if($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

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

	&item_load;

	&header;

	print <<"EOM";
<h1>�ł̋��</h1>
<hr size=0>

<FONT SIZE=3>
<B>�H�H�H�H</B><BR>
�u�����́c�ł̋�ԁc���c�B<br>
�����ɓ���ׂɂ́A�`�P�b�g�������Ă��邩�A�ŕ����̌��E�ł̉H�߁E�ł̈߂𑕔����邱�Ƃ��K�v���c�B<br>
�������A���̂R�̑����́A�����o�傪������΂��̐�֐i�ނ��Ƃ͂ł��Ȃ��c�B<br>
�Q����p��100���f���E�E�E���A���͓��ʃT�[�r�X�łR���f���E�E�E�B<br>
�ŕ����̌��E�ł̉H�߁E�ł̈߂͂����Ŕ������Ƃ��ł��邼�E�E�E�B<br>
EOM
if($chara[24]==1400){
	print <<"EOM";
<font color="yellow">
���̕���́E�E�E�I<br>
�E�E�E���̕�����X�ɒb���������30���f�����Ă��邱�Ƃ��ȁE�E�E�B<br>
100���f�͍�������Ƃ������͂����̂Œl���������̂��E�E�E�t�b�t�b�t�B<br>
���������ɐi�ނ̂ɂ͑����͂��̕��킾���ŗǂ��B������񂻂̕��킪�����邱�Ƃ͖������c�B<br>
���Ȃ݂Ɉŋ�ԃ`�P�b�g��10������Ζ����œ���ł��邼�B
</font>
�v
</FONT><br>
<br>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="�ŋ��EX�֐i��">(�`�P�b�g��$chara[189]������)
</td>
</form>
EOM
}else{
	print <<"EOM";
�v
</FONT><br>
<br>
EOM
if($chara[189]>0){
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu">
<input type=submit class=btn value="�`�P�b�g���g��">($chara[189]������)
</td>
</form>
EOM
}elsif($item[0] eq "�ŕ����̌�" and $item[3] eq "�ł̉H��" and $item[6] eq "�ł̈�"){
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu">
<input type=submit class=btn value="������">
</td>
</form>
EOM
}else{
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=1>
<input type=submit class=btn value="�ŕ����̌��𔃂�(1��G)">
</td><br>
</form>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=2>
<input type=submit class=btn value="�ł̉H�߂𔃂�(100��G)">
</td>
</form><br>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=3>
<input type=submit class=btn value="�ł̈߂𔃂�(10��G)">
</td>
</form>
EOM
}
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

sub susumu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;
	$tic=0;
	$kane=int(((14/15)**7)*10000)/100;
	$kane2=int(((12/13)**7)*10000)/100;
	if($chara[189]>0){$chara[189]-=1;$tic=1;}
	elsif($chara[19]<300000000){&error("����������܂���B$kane/$kane2");}
	else{
		if($item[0] ne "�ŕ����̌�" or $item[3] ne "�ł̉H��" or $item[6] ne "�ł̈�"){
			&error("�ǂ���炱��ȏ�i�ވׂɂ͑��������������悤���c�B");
		}
		$chara[19]-=300000000;
	}

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$souko_item_num = @souko_item;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);
	$souko_def_num = @souko_def;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}elsif ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I");
	}elsif ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I");
	}

	if($tic==0){$dx=int(rand(4))+2;}

	if(int(rand(10000))==0){
		$i_no=1170;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
	}elsif(int(rand(15-$dx))==0){
		$mes.="����Ɓc�Ȃ�ƁA20���f�𔭌������I<br>";
		$chara[19]+=2000000000;
	}elsif(int(rand(15-$dx))==0){
		$mes.="����Ɓc�Ȃ�ƁA�_��̗͂ł`�o���O�[�����Əオ�����I<br>";
		$chara[13]+=int(rand(8)+5);
	}elsif(int(rand(30-$dx))==0){
		$mes.="����Ɓc�Ȃ�ƁASTR���O�[�����Əオ�����I<br>";
		$chara[7]+=int(rand(101)+20);
	}elsif(int(rand(45-$dx))==0){
		$i_no=1121;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
	}elsif(int(rand(45-$dx))==0){
		$i_no=2121;
		open(IN,"$def_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		$mes.="����Ɓc�Ȃ�ƁA$i_name���������I<br>";
	}elsif(int(rand(100-$dx))==0){
		$i_no="0031";
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $i_no){last;}
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		$mes.="����Ɓc�Ȃ�ƁA$ai_name���������I<br>";
	}elsif(int(rand(15-$dx))==0){
		$ssno=int(rand(12)+71);
		$chara[$ssno]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$mes.="����Ɓc�Ȃ�ƁA$sname3�𔭌������I<br>";
	}elsif(int(rand(15-$dx))==0){
		$mes.="����Ɓc�Ȃ�ƁA���i���P�ɌX������<br>";
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$hendo=int(rand(30)+1);
		$chara[65]-=$hendo;
		$chara[64]+=$hendo;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[65]<0){$chara[65]=0;}
		if($chara[64]>100){$chara[64]=100;}
	}elsif(int(rand(15-$dx))==0){
		$mes.="����Ɓc�Ȃ�ƁA���i�����ɌX������<br>";
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$hendo=int(rand(30)+1);
		$chara[64]-=$hendo;
		$chara[65]+=$hendo;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[64]<0){$chara[64]=0;}
		if($chara[65]>100){$chara[65]=100;}
	}elsif($tic==1){
		$mes="�����������N���Ȃ������B";
	}else{
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$lost=int(rand(10));
		if($lost<5){
			$mes="�ŕ����̌��������������đ�R�̐΂ɂȂ����B<br>";
			$hi=int(rand(5));
			$isi[0]+=$hi;
			$mes.="<font color=\"red\">�΂̐΂�$hi��ɓ��ꂽ�b�I<br></font>";
			$mizu=int(rand(5));
			$isi[1]+=$mizu;
			$mes.="<font color=\"red\">���̐΂�$mizu��ɓ��ꂽ�b�I<br></font>";
			$numa=int(rand(5));
			$isi[2]+=$numa;
			$mes.="<font color=\"red\">���̐΂�$numa��ɓ��ꂽ�b�I<br></font>";
			$chara[200]=1;
			&item_lose;
		}elsif($lost<9){
			$mes="�ł̈߂������������đ�R�̐΂ɂȂ����B";
			$yama=int(rand(5));
			$isi[3]+=$yama;
			$mes.="<font color=\"red\">�R�̐΂�$yama��ɓ��ꂽ�b�I<br></font>";
			$yami=int(rand(5));
			$isi[4]+=$yami;
			$mes.="<font color=\"red\">�ł̐΂�$yami��ɓ��ꂽ�b�I<br></font>";
			$hikari=int(rand(5));
			$isi[5]+=$hikari;
			$mes.="<font color=\"red\">���̐΂�$hikari��ɓ��ꂽ�b�I<br></font>";
			$chara[200]=3;
			&acs_lose;
		}elsif($lost==9){
			$mes="�ł̉H�߂������������đ�R�̐΂ɂȂ����B";
			$hi=int(rand(4));
			$isi[0]+=$hi;
			$mes.="<font color=\"red\">�΂̐΂�$hi��ɓ��ꂽ�b�I<br></font>";
			$mizu=int(rand(4));
			$isi[1]+=$mizu;
			$mes.="<font color=\"red\">���̐΂�$mizu��ɓ��ꂽ�b�I<br></font>";
			$numa=int(rand(4));
			$isi[2]+=$numa;
			$mes.="<font color=\"red\">���̐΂�$numa��ɓ��ꂽ�b�I<br></font>";
			$yama=int(rand(4));
			$isi[3]+=$yama;
			$mes.="<font color=\"red\">�R�̐΂�$yama��ɓ��ꂽ�b�I<br></font>";
			$yami=int(rand(4));
			$isi[4]+=$yami;
			$mes.="<font color=\"red\">�ł̐΂�$yami��ɓ��ꂽ�b�I<br></font>";
			$hikari=int(rand(4));
			$isi[5]+=$hikari;
			$mes.="<font color=\"red\">���̐΂�$hikari��ɓ��ꂽ�b�I<br></font>";
			$gin=int(rand(4));
			$isi[6]+=$gin;
			$mes.="<font color=\"red\">��̐΂�$gin��ɓ��ꂽ�b�I<br></font>";
			$si=int(rand(4));
			$isi[7]+=$si;
			$mes.="<font color=\"red\">���̐΂�$si��ɓ��ꂽ�b�I<br></font>";
			$mura=int(rand(4));
			$isi[8]+=$mura;
			$mes.="<font color=\"red\">���̐΂�$mura��ɓ��ꂽ�b�I<br></font>";
			$chara[200]=2;
			&def_lose;
		}
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}
sub buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$souko_item_num = @souko_item;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);
	$souko_def_num = @souko_def;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("����q�ɂ������ς��ł��I");
	}
	elsif ($souko_def_num >= $def_max) {
		&error("�h��q�ɂ������ς��ł��I");
	}
	elsif ($souko_acs_num >= $acs_max) {
		&error("�A�N�Z�T���[�q�ɂ������ς��ł��I$back_form");
	}

	if($in{'kai'}==1){
		if($chara[19]<100000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=100000000;
			$i_no=1135;
			open(IN,"data/item/stitem.ini");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes="$i_name�𔃂����I<br>";
		}
	}elsif($in{'kai'}==2){
		if($chara[19]<10000000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=10000000000;
			$i_no=2147;
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="$i_name�𔃂����I<br>";
		}
	}elsif($in{'kai'}==3){
		if($chara[19]<1000000000){
			&error("����������܂���B");
		}else{
			$chara[19]-=1000000000;
			$i_no="0028";
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $i_no){last;}
			}
			push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
			$mes.="$ai_name�𔃂����I<br>";
		}
	}else{&error("�G���[");}
	
	$chara[26] = $host;
	$hit=0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}

sub susumu2 {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;
	if($chara[189]>9){$chara[189]-=10;}
	elsif($chara[19]<3000000000){&error("����������܂���B");}
	else{$chara[19]-=3000000000;}

	$chara[26] = $host;

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	$i_name="";
	if(int(rand(80))==0){
		$mayaku[5]+=1;
		$i_name="�X�^�[�g�b�JS2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[2]+=1;
		$i_name="�X�^�[�g�b�JS";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[3]+=1;
		$i_name="�X�^�[�g�b�JA2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[4]+=1;
		$i_name="�X�^�[�g�b�JH2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(10))==0){
		$mayaku[0]+=1;
		$i_name="�X�^�[�g�b�JA";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(10))==0){
		$mayaku[1]+=1;
		$i_name="�X�^�[�g�b�JH";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(3))==0){
		if($chara[128]>=5 and $item[1]>9998){
			$kougeki=int(rand(30));
		}else{
			$kougeki=int(rand(100));
		}
		if($item[1]+$kougeki>9999 and $chara[128]<5){$kougeki=9999-$item[1];}
		$item[1]+=$kougeki;
		$mes.="����Ɓc�Ȃ�ƁA����̍U���͂�$kougeki�|�C���g�㏸�����I";
	}elsif(int(rand(3))==0){
		if($chara[128]>=5 and $item[2]>9998){
			$hit=int(rand(30));
		}else{
			$hit=int(rand(100));
		}
		if($item[2]+$hit>9999 and $chara[128]<5){$hit=9999-$item[2];}
		$item[2]+=$hit;
		$mes.="����Ɓc�Ȃ�ƁA����̖����͂�$hit�|�C���g�㏸�����I";
	}else{
		$mes="�����������N���Ȃ������B";
	}
	if($i_name){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		$chmes="$chara[4]�l���ŋ��EX�ŁA$i_name����肵�܂����I";
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		unshift(@chat_mes,"<><font color=\"yellow\">���m</font><>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$chmes</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

		open(IN,"akuma_log.cgi");
		@akuma_log = <IN>;
		close(IN);

		$aku_sum = @akuma_log;
		$akumes="$chara[4]�l���ŋ��EX�ŁA$i_name����肵�܂����I";
		if($aku_sum > 100) { pop(@akuma_log); }
		unshift(@akuma_log,"$year�N$mon��$mday��(��)$hour��$min��$akumes\n");

		open(OUT,">akuma_log.cgi");
		print OUT @akuma_log;
		close(OUT);

		$mes .= "<b><font size=5 color=red>����Ɓc�Ȃ�ƁA$i_name����ɓ��ꂽ�I�I</font></b><br>";
	}
	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�߂�">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}