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
<form action="./kouzan.cgi" method="post">
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
#  �y�b�g�\���@  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	if(!$chara[100]){$chara[100]=0;}
	if(!$chara[97]){$chara[97]=0;}
	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	&header;

	print <<"EOM";
	<h1>�z�R</h1>
	<hr size=0>

	<FONT SIZE=3>
	<B>��������</B><BR>
	�u��҂͓����[�B�o�C�g���񂶂��`�H�n�b�n�B<br>
	���R�A��͂����K�v�����΁v
	</FONT>
	<br>
	���݂̂g�o�F$chara[15]\/$chara[16]<br>
	��͂��̐��F$chara[100]�{<br>
	�����̂�͂��̐��F$chara[97]�{<br>
	�v���`�i�̂�͂��̐��F$chara[310]�{
	<br>
EOM
	if($chara[100]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=goto_world>
		<input type=submit class=btn value="����">
		</form>
EOM
	}
	if($chara[97]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=ougon_world>
		<input type=submit class=btn value="�����̂�͂��œ���">
		</form>
EOM
	}
	if($chara[310]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=pra_world>
		<input type=submit class=btn value="�v���`�i�̂�͂��œ���">
		</form>
EOM
	}
	if($chara[24] == 1341){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$chara_log">
		<input type=hidden name=mode value=turu_world>
		<input type=submit class=btn value="�ߚ{�œ���">���Ȃ��Ȃ�܂�
		</form>
EOM
}

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub goto_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	if(!$chara[100]){&error("��͂�������܂���");}
	else{$chara[100]-=1;}
	if(!$chara[37]){$chara[37]=1;$ten=1;}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=30;$i++){
		if($chara[70]!=1){$rdd=int(rand(3000));}
		else{$rdd=int(rand(5000));}
		$com.="<hr size=0>$i�^�[��<br>�g�o�F$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>���ꍇ���΂��I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd==1){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>�����̂�͂����I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<5){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>��͂����I�Ђ�ف[���I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<10){
			$com.="���I�H�������I�~�j�f�r�����I�I<br><br>";
			$com.="�|���Α�ϒ�����������ɓ���Ƃ��c�B<br><br>";
			$com.="<b><font size=6 color=red>�����ۂ��Ȃ�͂����ᖳ���I</font></b><br>";
			$dmg = $chara[16] + int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<20){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>�����΂��I�Ђ�ف[��!!</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<50){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("����q�ɂ������ς��ł��I$back_form");
			}
			if(int(rand(4))<3){$i_no=1001+int(rand(15));}
			else{$i_no=1001+int(rand(30+$chara[37]));}
			if($i_no > 1060){$i_no=1001+int(rand(60));}
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
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="�Ȃ񂾂����E�E�E�I�H<br><br>";
			$com.="<b><font size=4 color=yellow>$i_name���I�Ђ�ف[��!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<80){
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
			$souko_def_num = @souko_def;
			if ($souko_def_num >= $def_max) {
				&error("�h��q�ɂ������ς��ł��I$back_form");
			}
			if(int(rand(4))<3){$i_no=2001+int(rand(15));}
			else{$i_no=2001+int(30+$chara[37]);}
			if($i_no > 2060){$i_no=2001+int(rand(60));}
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
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="�Ȃ񂾂����E�E�E�I�H<br><br>";
			$com.="<b><font size=4 color=yellow>$i_name���I�Ђ�ف[��!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<85){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=5 color=red>�ʎ蔠�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 3 / 2));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[70]>=1){
				if($chara[18]<50000){
					$lv = int(rand($chara[18]/100));
				}else{
					$lv = int(rand($chara[18]/500));
				}
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=red>$lv���x���オ�����I</font></b><br>";
				}else{
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$kexp = int($chara[15]/3) * int(rand($chara[18] / 50) + 1);
				$com.="<b><font size=4 color=yellow>$kexp�̌o���l�I</font></b><br>";
				$exp += $kexp;
				}
			}else{
				$lvdown = int(rand($chara[18]/1000));
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdown���x�����������I</font></b><br>";
			}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<150){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=4 color=yellow>�����X�^�[�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>���Ƃ��|����!!</font></b><br>";
				$kexp = int($chara[15]/3) * int(rand($chara[18] / 50) + 1);
				$com.="<b><font size=4 color=yellow>$kexp�̌o���l�I</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>�_���������c�B</font></b><br>";}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<250){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="���E�E�E�I�H<br><br>";
			$kgold = int(rand($chara[37] * 10000 + $chara[18] * 100));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>�����I�Ђ�ف[��!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgold�f���肵���I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 5) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<500){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<font color=white><b>�����������A�x�e�����I�I�I</b></font><br><br>";
			if(int(rand(3))<2){$com.="�ƁA�v�����炻��Ȃ̂���킯�Ȃ������I<br><br>";}
			else{
				$com.="<b><font size=4 color=white>������Ɖ�!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>�g�o��$dmg�񕜁B</font></b><br>";
			}
		}
		elsif($rdd<800){
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="<b><font size=4 color=red>�S���I���Ɋ₪!!</font></b><br><br>";
			$com.="�����Ă��ȃ{�P�R���@�E�E�E�E�I�I�I�I<br><br>";
			$dmg = int(rand($chara[16] / 3) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		else{
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�ӂ��`��ꂽ�`�B�����ˁ[�B<br><br>";
			$dmg = int(rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]�͌��E���I�I";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}
	if($ten==1){$chara[37]=0;}

	$chara[15]=$chara[16];
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	���ʁF<br>
	���x��$lv<br>
	�o���l$exp<br>
	��$gold�f<br>
	������$goseiseki��<br>
	���ꍇ����$tokusyugoseiseki��<br>
	��͂�$turu��<br>
	�����̂�͂�$turu_gold��<br>
	���̑�$k��<br></font>
EOM
	if($chara[100]){
		print <<"EOM";
		<form action="./kouzan.cgi" method="post">
		<input type=hidden name=id value=$in{'id'}>
		<input type="hidden" name="mydata" value="$new_chara">
		<input type=hidden name=mode value=goto_world>
		<input type=submit class=btn value="�����ꔭ�I�I">
		</form>
EOM
	}
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub ougon_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if(!$chara[97]){&error("�����̂�͂�������܂���");}
	if(!$chara[37]){$chara[37]=1;$ten=1;}
	if($chara[140]==2 and $jisin==1){$chara[15]=1;}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=30;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$i�^�[��<br>�g�o�F$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>���ꍇ���΂��I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd==1){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>�����̂�͂����I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<3){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>��͂����I�Ђ�ف[���I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<10){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>�����΂��I�Ђ�ف[��!!</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<20){
			$com.="���I�H�������I�~�j�f�r�����I�I<br><br>";
			$com.="�|���Α�ϒ�����������ɓ���Ƃ��c�B<br><br>";
			$com.="�ӂ��A�]�T�I�����̂�͂��Ȃ߂�Ȃ��I�����������邩�c�H<br><br>";
			$ran=int(rand(5));
			for($i=0;$i<$ran;$i++){
			$rann=int(rand(4));
			if($rann==0){
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>�����΂��I�Ђ�ف[��!!</font></b><br>";
			}
			elsif($rann==1){
			$turu+=1;
			$com.="<b><font size=5 color=yellow>��͂����I�Ђ�ف[���I</font></b><br>";
			}
			elsif($rann==2){
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>�����̂�͂����I�I</font></b><br>";
			}
			elsif($rann==3){
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>���ꍇ���΂��I�I</font></b><br>";
			}
			}
			$dmg = $chara[16] + int(rand($chara[16]));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<35){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("����q�ɂ������ς��ł��I$back_form");
			}
			if(int(rand(4))<2){$i_no=1001+int(rand(30));}
			else{$i_no=1001+int(rand(45));}
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
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="�Ȃ񂾂����E�E�E�I�H<br><br>";
			$com.="<b><font size=4 color=yellow>$i_name���I�Ђ�ف[��!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<50){
			open(IN,"$souko_folder/def/$chara[0].cgi");
			@souko_def = <IN>;
			close(IN);
			$souko_def_num = @souko_def;
			if ($souko_def_num >= $def_max) {
				&error("�h��q�ɂ������ς��ł��I$back_form");
			}
			if(int(rand(4))<2){$i_no=2001+int(rand(30));}
			else{$i_no=2001+int(rand(45));}
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
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="�Ȃ񂾂����E�E�E�I�H<br><br>";
			$com.="<b><font size=4 color=yellow>$i_name���I�Ђ�ف[��!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 4));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<60){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=5 color=red>�ʎ蔠�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 4 / 3));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[18]<50000){
					$lv = int(rand($chara[18]/99));
				}else{
					$lv = int(rand($chara[18]/495));
				}
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=red>$lv���x���オ�����I</font></b><br>";
			}else{
				$lvdown = int(rand($chara[18]/5000));
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdown���x�����������I</font></b><br>";
			}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<85){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=4 color=yellow>�����X�^�[�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>���Ƃ��|����!!</font></b><br>";
				$kexp = $chara[15] * int(rand($chara[18] / 25) + 1);
				$com.="<b><font size=4 color=yellow>$kexp�̌o���l�I</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>�_���������c�B</font></b><br>";}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<125){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="���E�E�E�I�H<br><br>";
			$kgold = int(rand($chara[37] * 10000 + $chara[18] * 100));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>�����I�Ђ�ف[��!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgold�f���肵���I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 5) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<200){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<font color=white><b>�����������A�x�e�����I�I�I</b></font><br><br>";
			if(int(rand(3))<2){$com.="�ƁA�v�����炻��Ȃ̂���킯�Ȃ������I<br><br>";}
			else{
				$com.="<b><font size=4 color=white>������Ɖ�!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>�g�o��$dmg�񕜁B</font></b><br>";
			}
		}
		elsif($rdd<350){
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="<b><font size=4 color=red>�S���I���Ɋ₪!!</font></b><br><br>";
			$com.="�����Ă��ȃ{�P�R���@�E�E�E�E�I�I�I�I<br><br>";
			$dmg = int(rand($chara[16] / 3) + rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		else{
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�ӂ��`��ꂽ�`�B�����ˁ[�B<br><br>";
			$dmg = int(rand($chara[16] / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]�͌��E���I�I";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}

	if(int(rand(3))<2){$chara[97]-=1;$mes="�����̂�͂������Ă��܂����B";}
	
	if($ten==1){$chara[37]=0;}

	$chara[15]=$chara[16];

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	���ʁF<br>
	���x��$lv<br>
	$mes<br>
	�o���l$exp<br>
	��$gold�f<br>
	������$goseiseki��<br>
	���ꍇ����$tokusyugoseiseki��<br>
	��͂�$turu��<br>
	�����̂�͂�$turu_gold��<br>
	���̑�$k��<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub pra_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	if(!$chara[310]){&error("�v���`�i�̂�͂�������܂���");}
	$k=0;
	$com="<font size=3><center>";
	$hi=0;$mizu=0;$yami=0;$hikari=0;
	$rdd=0;
	for($i=0;$i<=10;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$i�^�[��<br>�g�o�F$chara[15]\/$chara[16]<br>";

		if($rdd==0){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=6 color=yellow>���f���U�N�U�N�I�I</font></b><br>";
			$hi += int(rand(10));
			$mizu += int(rand(10));
			$yami += int(rand(10));
			$hikari += int(rand(10));
			$dmg = int(rand($chara[16] * 4));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<10){
			$com.="��E�E�E�H����������P���Ă���E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=5 color=yellow>�F��Ȍ��f��������������C������I�I</font></b><br>";
			$hi += int(rand(3));
			$mizu += int(rand(3));
			$yami += int(rand(3));
			$hikari += int(rand(3));
			$dmg = int(rand($chara[16] * 3));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<100){
			$com.="��E�E�E�H�����������邼�E�E�E�B<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			if(int(rand(4))==0){$hi += int(rand(3));}
			elsif(int(rand(4))==0){$mizu += int(rand(3));}
			elsif(int(rand(4))==0){$yami += int(rand(3));}
			else{$hikari += int(rand(3));}
			$com.="<b><font size=4 color=yellow>�C�̂������A���f��������C������I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 2));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<500){
			$com.="��E�E�E�H�����������邼�E�E�E�B<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			if(int(rand(4))==0){$hi += int(rand(2));}
			elsif(int(rand(4))==0){$mizu += int(rand(2));}
			elsif(int(rand(4))==0){$yami += int(rand(2));}
			else{$hikari += int(rand(2));}
			$com.="<b><font size=3 color=yellow>�C�̂������A���f��������C������I�I</font></b><br>";
			$dmg = int(rand($chara[16]));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		else{
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�ӂ��`��ꂽ�`�B�����ˁ[�B<br><br>";
			$dmg = int(rand($chara[16] / 3));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]�͌��E���I�I";
			$chara[15]=1;
			$i=31;
		}
	}
	$com.="</center></font>";

	$chara[310]-=1;

	$chara[15]=$chara[16];

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$isi[29]+=$hi;
		$isi[30]+=$mizu;
		$isi[31]+=$yami;
		$isi[32]+=$hikari;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	���ʁF<br>
	�΂̌��f$hi��<br>
	���̌��f$mizu��<br>
	�ł̌��f$yami��<br>
	���̌��f$hikari��<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}
sub turu_world {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
		if($chara[15]>100){$chara[15]=int($chara[15]/100);}
	}

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if($chara[24] != 1341){&error("�ߚ{������܂���");}
	$k=0;
	$com="<font size=3><center>";
	$gold=0;$exp=0;$tokusyugoseiseki=0;$turu_gold=0;$turu=0;
	$rdd=0;
	for($i=0;$i<=50;$i++){
		$rdd=int(rand(1000));
		$com.="<hr size=0>$i�^�[��<br>�g�o�F$chara[15]\/$chara[16]<br>";

		if($rdd<100){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>���ꍇ���΂��I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<200){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>�����̂�͂����I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<350){
			$com.="��E�E�E�H����ȂƂ���ɂ�͂��E�E�E�H<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$turu+=1;
			$com.="<b><font size=5 color=yellow>��͂����I�Ђ�ف[���I</font></b><br>";
			$dmg = int(rand($chara[16] / 5));
			$chara[15]-= dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<500){
			$com.="��E�E�E�H�����d�����̂ɂԂ��������E�E�E<br><br>";
			$com.="���E�E�E����́I�I�I<br><br>";
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>�����΂��I�Ђ�ف[��!!</font></b><br>";
			$dmg = int(rand($chara[16] / 10));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<550){
			$com.="���I�H�������I�f�r�����I�I<br><br>";
			$com.="�|���Α�ϒ�����������ɓ���Ƃ��c�B<br><br>";
			$com.="�ӂ��A�]�T�I�ߚ{�Ȃ߂�Ȃ��I�����������邩�c�H<br><br>";
			$ran=int(rand(20));
			for($i=0;$i<$ran;$i++){
			$rann=int(rand(4));
			if($rann==0){
			$goseiseki+=1;
			$com.="<b><font size=6 color=yellow>�����΂��I�Ђ�ف[��!!</font></b><br>";
			}
			elsif($rann==1){
			$turu+=1;
			$com.="<b><font size=5 color=yellow>��͂����I�Ђ�ف[���I</font></b><br>";
			}
			elsif($rann==2){
			$turu_gold+=1;
			$com.="<b><font size=6 color=yellow>�����̂�͂����I�I</font></b><br>";
			}
			elsif($rann==3){
			$tokusyugoseiseki+=1;
			$com.="<b><font size=6 color=yellow>���ꍇ���΂��I�I</font></b><br>";
			}
			}
			$dmg = $chara[16] + int(rand($chara[16]/10));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<600){
			open(IN,"$souko_folder/item/$chara[0].cgi");
			@souko_item = <IN>;
			close(IN);
			$souko_item_num = @souko_item;
			if ($souko_item_num >= $item_max) {
				&error("����q�ɂ������ς��ł��I$back_form");
			}
			if(int(rand(4))<2){$i_no=1170;}
			else{$i_no=1193+int(rand(8));}
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
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="�Ȃ񂾂����E�E�E�I�H<br><br>";
			$com.="<b><font size=4 color=yellow>$i_name���I�Ђ�ف[��!!</font></b><br>";
			$k++;
			$dmg = int(rand($chara[16] * 3 / 40));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<650){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=5 color=red>�ʎ蔠�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] * 4 / 30));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				if($chara[18]<50000){
					$lvc = int(rand($chara[18]/100));
				}else{
					$lvc = int(rand($chara[18]/500));
				}
				$lv += $lvc;
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=red>$lv���x���オ�����I</font></b><br>";
			}else{
				$lvc =  int(rand($chara[18]/5000));
				$lvdown += $lvc;
				$com.="<b><font size=4 color=yellow>�����J����Ɓc</font></b><br>";
				$com.="<b><font size=6 color=blue>$lvdown���x�����������I</font></b><br>";
			}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<700){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<b><font size=4 color=yellow>�����X�^�[�����I�I�I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 5 / ($chara[37]/2)));
			$chara[15]-= $dmg;
			if($chara[15]>0){
				$com.="<b><font size=4 color=yellow>���Ƃ��|����!!</font></b><br>";
				$kexp = $chara[15] * int(rand($chara[18] / 25) + 1);
				$com.="<b><font size=4 color=yellow>$kexp�̌o���l�I</font></b><br>";
				$exp += $kexp;
			}else{$com.="<b><font size=4 color=yellow>�_���������c�B</font></b><br>";}
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<800){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="���E�E�E�I�H<br><br>";
			$kgold = int(rand($chara[37] * 100000 + $chara[18] * 10000));
			$gold+= $kgold;
			$com.="<b><font size=4 color=yellow>�����I�Ђ�ف[��!!</font></b><br>";
			$com.="<b><font size=4 color=yellow>$kgold�f���肵���I�I</font></b><br>";
			$dmg = int(rand($chara[16] / 50) + rand($chara[16] / 10 / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}
		elsif($rdd<900){
			$com.="���E�E�E����́I�I�I<br><br>";
			$com.="<font color=white><b>�����������A�x�e�����I�I�I</b></font><br><br>";
			if(int(rand(3))<2){$com.="�ƁA�v�����炻��Ȃ̂���킯�Ȃ������I<br><br>";}
			else{
				$com.="<b><font size=4 color=white>������Ɖ�!!</font></b><br>";
				$dmg = int(rand($chara[16] - $chara[15]) / 2);
				$chara[15]+= $dmg;
				$com.="<b><font size=3 color=white>�g�o��$dmg�񕜁B</font></b><br>";
			}
		}
		else{
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�U�N�U�N�U�N�U�N�U�N�U�N�B�U�N�U�N�U�N�U�N�U�N�U�N�B<br><br>";
			$com.="�ӂ��`��ꂽ�`�B�����ˁ[�B<br><br>";
			$dmg = int(rand($chara[16] / 10 / (30 + $chara[37])));
			$chara[15]-= $dmg;
			$com.="<b><font size=3 color=red>�g�o��$dmg�������B</font></b><br>";
		}

		if($chara[15]<0){
			$com.="$chara[4]�͌��E���I�I";
			$chara[15]=1;
			$i=51;
		}
	}
	$com.="</center></font>";
	$lv = $lv - $lvdown;
	$chara[18]+=$lv;
	$chara[35]+=$lv*4;
	$chara[17]+=$exp;
	$chara[19]+=$gold;
	$chara[100]+=$turu;
	$chara[99]+=$goseiseki;
	$chara[98]+=$tokusyugoseiseki;
	$chara[97]+=$turu_gold;
	if(!$gold){$gold=0;}
	if(!$goseiseki){$goseiseki=0;}

	if(int(rand(4))<3){&item_lose;$chara[24]="";$mes="�ߚ{�����Ă��܂����B";}

	$chara[15]=$chara[16];

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
	$com<br>
	<font size=5>
	���ʁF<br>
	���x��$lv<br>
	$mes<br>
	�o���l$exp<br>
	��$gold�f<br>
	������$goseiseki��<br>
	���ꍇ����$tokusyugoseiseki��<br>
	��͂�$turu��<br>
	�����̂�͂�$turu_gold��<br>
	���̑�$k��<br></font>
EOM
	&shopfooter;

	&footer;

	exit;
}