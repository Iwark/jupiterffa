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
# 1. ���̃X�N���v�g�̓t���[�\�t�g�ł��B���̃X�N���v�g���g�p����	#
#    �����Ȃ鑹�Q�ɑ΂��č�҂͈�؂̐ӔC�𕉂��܂���B		#
# 2. �ݒu�Ɋւ��鎿��̓T�|�[�g�f���ɂ��肢�������܂��B	#
#    ���ڃ��[���ɂ�鎿��͈�؂��󂯂������Ă���܂���B	#
# 3. �ݒu������F����Ɋy����ł��炤�ׂɂ��AWeb�����O�ւ��ЎQ��#
#    ���Ă�������m(__)m						#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi		#
#---------------------------------------------------------------#

# ���{�ꃉ�C�u�����̓ǂݍ���
require 'jcode.pl';

# ���W�X�g���C�u�����̓ǂݍ���
require 'regist.pl';

# �퓬���C�u�����̓ǂݍ���
require 'battle.pl';
# �����X�^�[��p���C�u����
require 'mbattle.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

#================================================================#
#����������������������������������������������������������������#
#�� �����艺��CGI�Ɏ��M�̂�����ȊO�͈���Ȃ��ق�������ł��@��#
#����������������������������������������������������������������#
#================================================================#

if ($mente) {
	&error("���݃o�[�W�����A�b�v���ł��B���΂炭���҂����������B");
}

&decode;

#�h�o�A�h���X�ŃA�N�Z�X����
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("�A�N�Z�X�ł��܂���I�I");
	}
}

&boss;

exit;
#----------------------------#
#  ���W�F���h�v���C�X�ł̐퓬#
#----------------------------#
sub boss {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$test=0;
	$hit=0;
	if($chara[146]>0){$hit=1;}
	if ($test!=1 and $chara[134] == $mday) {
		if($hit==1){$hit=2;}
		else{
			if($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==8){
			}elsif($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==9){
			}else{
				&error("�����͊��ɒ��킵�܂����B");
			}
		}
	}

	if ($test!=1 and $wday != 0 and $wday != 6 and $hit!=2) {
		if($hit==1){$hit=2;}
		else{
			if($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==8){
				$chara[19]-=1000000000;
			}elsif($wday==2 and $chara[19]>=1000000000 and $in{'boss_file'}==9){
				$chara[19]-=1000000000;
			}else{
				&error("�����͊��ɒ��킵�܂����B");
			}
		}
	}

	if ($hit==2){$chara[146]-=1;}

	if (!$in{'boss_file'}){
		&error("�������N�֎~�I");
	}
	$chara[314]=time();

	&get_host;

	&item_load;

	&acs_add;

	$kazu=2;

	if($in{'boss_file'}==8 or $in{'boss_file'}==9){
		open(IN,"data/akumakai.ini");
		@MONSTER = <IN>;
		close(IN);
		$r_no = @MONSTER;
		$akumakai = 1;
	}else{
		open(IN,"data/akuma.ini");
		@MONSTER = <IN>;
		close(IN);
		$r_no = $in{'boss_file'} - 1;
		$aku=1;
	}

	$place = 98;

	&mons_read;

	$khp_flg = $chara[15];

	$smem1hp_flg = int(rand($mrand1)) + $msp1;
	if($in{'boss_file'}!=8 and $in{'boss_file'}!=9){
		$smem1hp = $smem1hp_flg * ($chara[135]+1);
	}elsif($in{'boss_file'}==9){
		$smem1hp = $smem1hp_flg + int(rand($smem1hp_flg));
	}else{
		$smem1hp = $smem1hp_flg;
	}
	$smem1hp_flg = $smem1hp;
	if(!$smem1hp or $smem1hp<1){&error("�����X�^�[��������܂���B�Ē��킵�Ă��������B");}

	$mem3hp_flg = $chara[42];

	$i=1;
	$j=0;@battle_date=();

	@gakusyuu=();
	open(OUT,">akuma/$chara[0].cgi");
	print OUT @gakusyuu;
	close(OUT);

	while($i<=$chara[135]+1) {

		&shokika;

		&tyousensya;
		&tyosenwaza;

		&mons_waza;

		&acs_waza;
		&mons_atowaza;

		open(IN,"akuma/$chara[0].cgi");
		@gakusyuu = <IN>;
		close(IN);
		$ghit=0;
		foreach(@gakusyuu){
			if($ghissatu==$_ and $ghissatu<999){
				if($in{'boss_file'}==8 or $in{'boss_file'}==9){
		if($chara[24]==1400 and $item[37]%100==4 and int($item[37]/100+1)*10>int(rand(100))){
				$ghit=1;
				last;
		}elsif($chara[24]==1400 and $item[38]%100==4 and int($item[38]/100+1)*10>int(rand(100))){
				$ghit=1;
				last;
		}else{
				$scom1 .= "<font class=\"yellow\" size=5>�}\��\�\\��\��\��\�J\�c\��\�J\��\�I\�I</font><br>";
				$dmg1=int($dmg1*int(rand(100)+1)/100);
				$ssake1 = $ssake1*(int(rand(100)+1));
				$ghit=1;
				last;
		}
				}
			}
		}
		if($ghit!=1){
			push(@gakusyuu,"$ghissatu\n");
			open(OUT,">akuma/$chara[0].cgi");
			print OUT @gakusyuu;
			close(OUT);
		}
		if($in{'boss_file'}==8 or $in{'boss_file'}==9){
			$dmg1=int($dmg1/10000);
			$dmg4=int($dmg4/8500);
			$mem1hit_ritu = int($mem1hit_ritu/80);
			$sake1=int($sake1/10000);
		}

		&mons_clt;
		&mons_kaihi;

		&monsbattle_sts;

		&hp_sum;

		&winlose;

		$i++;
		$j++;
	}

	$kmori_w = $chara[28];

	if($chara[70]>0 and $win==1){
		$gishi=0;
		if($in{'boss_file'}==8 and $chara[24]==1400){
			if(int(rand(100))<40){
				$gishi=int(rand(4)+30);
			}
		}elsif($in{'boss_file'}==9 and $chara[24]==1400){
			if(int(rand(100))<60){
				$gishi=int(rand(4)+30);
			}
		}elsif($in{'boss_file'}>4){
			if($item[0] eq "�c���n�V" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�R�̃c���n�V" and int(rand(2))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�����̃c���n�V" and int(rand(1))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>3){
			if($item[0] eq "�c���n�V" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�R�̃c���n�V" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�����̃c���n�V" and int(rand(2))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>2){
			if($item[0] eq "�c���n�V" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�R�̃c���n�V" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�����̃c���n�V" and int(rand(3))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}elsif($in{'boss_file'}>1){
			if($item[0] eq "�c���n�V" and int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�R�̃c���n�V" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�����̃c���n�V" and int(rand(4))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(7))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}else{
			if($item[0] eq "�c���n�V" and int(rand(7))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�R�̃c���n�V" and int(rand(6))==0){$gishi=int(rand(1)+29);}
			elsif($item[0] eq "�����̃c���n�V" and int(rand(5))==0){$gishi=int(rand(1)+29);}
			elsif(int(rand(8))==0){$gishi=int(rand(1)+29);}
			elsif($chara[55]==65 or $chara[56]==65 or $chara[57]==65 or $chara[58]==65){
				if(int(rand(2))==0){
					$gishi=int(rand(1)+29);
				}
			}
		}
		if($gishi>0){
			$gishi-=1;
			open(IN,"./kako/$chara[0].cgi");
			$isi_list = <IN>;
			close(IN);
			@isi = split(/<>/,$isi_list);
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			$so=0;
			foreach(@sozai_data){
				($sozainame) = split(/<>/);
				if($so == $gishi) {last;}
				$so++;
			}
			@isi[$gishi]+=1;
			$new_isi = '';
			$new_isi = join('<>',@isi);
			$new_isi .= '<>';
			open(OUT,">./kako/$chara[0].cgi");
			print OUT $new_isi;
			close(OUT);
			$comment .= <<"EOM";
			<font class=\"red\" size=5>$sozainame����ɓ��ꂽ�b�I�I</font><br>
EOM
		}
	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest4_item = split(/<>/,$questdata);
	$hit=0;
	if($quest4_item[1]>0 and $ssmname1 eq "�X�m��") {$hit=29;}
	if($quest4_item[2]>0 and $ssmname1 eq "�X�m��") {$hit=30;}
	if($quest4_item[3]>0 and $ssmname1 eq "�X�m�~") {$hit=31;}
	if($quest4_item[4]>0 and $ssmname1 eq "�X�m�~") {$hit=32;}
	if($hit>0){
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		$so=0;
		foreach(@sozai_data){
			($sozainame) = split(/<>/);
			if($so == $hit) {last;}
			$so++;
		}
		@isi[$hit]+=1;
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
		$hit=$hit-28;
		$quest4_item[$hit]=0;
		$new_data = '';
		$new_data = join('<>',@quest4_item);
		$new_data .= '<>';
		open(OUT,">./quest/$chara[0].cgi");
		print OUT $new_data;
		close(OUT);
		$comment .= "<b><font size=4 color=red>";
		$comment .= "�u$ssmname1�v��|���N�G�X�g���N���A�����I<br>";
		$comment .= "��V$sozainame����肵���I�I<br>";
	}
	}

	&akuma_sentoukeka;

	&acs_sub;

	&hp_after;

	&levelup;

	$chara[134]=$mday;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE= "5" COLOR= "#7777DD"><B>�����̊�</B></FONT><br>

<B><CENTER><FONT SIZE= "6">�o�g���I</FONT></CENTER>
<BR>
<BR>
EOM

	$i=0;
	foreach(@battle_date) {
		print "$battle_date[$i]";
		$i++;
	}

	&bossfooter;

	&footer;

	exit;
}

#--------------------------------#
#  ���W�F���h�v���C�X�p�t�b�^�[  #
#--------------------------------#
sub bossfooter {
	if ($win<3) { print "$comment$chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B<b>$gold</b>G��ɓ��ꂽ�B<br>\n"; }
	else { print "$comment$chara[4]�́A$mex�̌o���l����ɓ��ꂽ�B�����������ɂȂ����E�E�E(��)<br>\n"; }

	print <<"EOM";
<form action="$script" method="POST">
<input type="hidden" name="mode" value="log_in">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�">
</form>
EOM
}