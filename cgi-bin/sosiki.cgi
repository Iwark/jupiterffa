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
<form action="sosiki.cgi" >
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

	&header;

if($chara[63]>=1){&error("�Y�����ɓ����Ă��܂��B");}

	print <<"EOM";
<h1>��̑g�D</h1>
<hr size=0>
EOM
if($chara[65]==100){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�I�I�p�Y$chara[4]����˂����I�I<br>
���ɁA�Ɉ��l�ɂȂ����݂������ȁI<br>
���̑̂Ȃ�A��\�\\�����B�Ȃ肽���񂾂�H�喂���ɁB<br>
�����A���O���A�喂���ɂ��Ă�邺�B<br>
���Ȃ��Ă���W���u���}�X�^�[���āA�p�Y�̏؂ƂȂ���̂𑕔����Ă�����B�v
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=43>
<input type=submit class=btn value="�喂���ɂȂ�">
</form>
EOM
}elsif($chara[64]==100){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�I�I�p�Y$chara[4]����˂����I�I<br>
���ɁA���P�l�ɂȂ����݂������ȁI<br>
���̑̂Ȃ�A��\�\\�����B�Ȃ肽���񂾂�H��V�g�ɁB<br>
�����A���O���A��V�g�ɂ��Ă�邺�B<br>
���Ȃ��Ă���W���u���}�X�^�[���āA�p�Y�̏؂ƂȂ���̂𑕔����Ă�����B�v
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=42>
<input type=submit class=btn value="��V�g�ɂȂ�">
</form>
EOM
}elsif($chara[65]>=60){
	if($chara[69]==0){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�c$chara[4]���c\�\\�͕����Ă邺�c���X�@���@�ɋ߂Â��Ă�݂�������˂����c<BR><BR>
���݂��Ăق�����΂��ł������ȁB<br>
�P�ǂԂ��Ă�܋��҂���Ԃ蓢���ɂ��邽�߂ɁA�l��p�ӂ��Ă��c�B<br>
���ꂩ��A�����ɂ���A���u�f�r���N���E���v�������Ă����Ƃ����B<br>
���Ȃ񂩂���˂����B�������c������󂯎�������_�ł��O�͑g�D�ƌ_������񂾂��ƂɂȂ邪�ȁB<br>
���Ȃ݂Ɉꉞ���ʂ�`���Ă������B�f�r���N���E�������҂́A���ɐ��܂�قǋ����Ȃ�B<br>
�g�D�ƌ_������Ԃ��Ă����̂́A�܂��A���O������@���ɑP�Ɍ����������ɂ͑g�D���ǎ���o�����Ă��Ƃ��B<br>
�킩�邾��H���؂�͋�����B�v
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=item value=1>
<input type=submit class=btn value="�󂯎��">
</form>
EOM
	}elsif($chara[69]==1 and $chara[86]<2){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�c$chara[4]���c�悭�����ȁc�܂��܂��@���@�݂�������˂����B<BR><BR>
����̎��݂�ɂ����̂��H<br>
�P�ǂԂ��Ă�܋��҂���Ԃ蓢���ɂ��邽�߂ɁA�l��p�ӂ��Ă��c�B<br>
�������A����͋��������邺�c�Ȃɂ��A�������̃����̐l���������邩��ȁc�B<br>
�l�A��l�ɂ��A$chara[18]000�f�����������B<br>
�����́A���O�Ɠ������炢���B�������A�R�񂨑O���Ԃ蓢���ɂ���̂���������P�l�Ԃ��Ă��炤���B<br>
���Ȃ݂ɁA�����Ɍق���̂͂Q�l�܂ł��B
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_sell>
<input type=hidden name=item value="1">
<input type=submit class=btn value="�P�l�ق�">
</form>
�v
EOM
	}
}elsif($chara[64]>=60){
	if($chara[69]==0){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�c$chara[4]���c\�\\�͕����Ă邺�c���X�@�P�@�ɋ߂Â��Ă�݂�������˂����c<BR><BR>
�ӂ��ӁB�����ɂ���A���u�G���W�F���N���E���v��_���Ă����̂��H<br>
�ǂ��������Ă����B<br>
���Ȃ񂩂���˂����B�������c������󂯎�������_�ł��O�͑g�D�ƌ_������񂾂��ƂɂȂ邪�ȁB<br>
���Ȃ݂Ɉꉞ���ʂ�`���Ă������B�G���W�F���N���E�������҂́A�P�ɐ��܂�قǋ����Ȃ�B<br>
�g�D�ƌ_������Ԃ��Ă����̂́A�܂��A���O������@���Ɉ��Ɍ����������ɂ͑g�D���ǎ���o�����Ă��Ƃ��B<br>
�킩�邾��H���؂�͋�����B�v
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=item_buy>
<input type=hidden name=item value="2">
<input type=submit class=btn value="�󂯎��">
</form>
EOM
	}
}elsif($chara[64]==50 and $chara[177]==2 and $chara[18]<=2000){
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�悤�I�I$chara[4]����˂����I�I<br>
���ς�炸�����Ƃ������c�B���ɂ��P�ɂ��������˂��ȁB���O�́B<br>
�����E�E�E���O�����̃��x���œ����N�G�X�g���I�������p�Y�ł��邱�Ƃ͊ԈႢ�Ȃ��B<br>
�]�ނȂ�A�ٔ����ɂ��Ă�낤�B<br>
���Ȃ��Ă���W���u���}�X�^�[���āA�p�Y�̏؂ƂȂ���̂𑕔����Ă�����B�v
<form action="sosiki.cgi" >
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=change>
<input type=hidden name=item value=45>
<input type=submit class=btn value="�ٔ����ɂȂ�">
</form>
EOM
}else{
	print <<"EOM";

<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�Ȃ񂾂��܂��H$chara[4]�H�����˂����O���ȁB�����ƗL���ɂȂ��Ă��痈��񂾂ȁB<BR><BR>
�ʂɈ��l�ł��낤�ƑP�ǂł��낤��\�\\��񂺁B�@���႟�ȁB
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
sub item_buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$chara[69]=$in{'item'};

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
		$eg="$chara[4]�l���g�D�ƌ_������т܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u����c�����Ă����B
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  �A�C�e������  #
#----------------#
sub item_sell {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[19]<$chara[18]*1000){&error("����������܂���");}
	else{$chara[19]-=$chara[18]*1000;}

	$chara[86]+=1;

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
		$eg="$chara[4]�l�����̑g�D����l���ĂяW�߂܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u����c�A��čs���B
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
#----------------#
#  �A�C�e������  #
#----------------#
sub change {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($chara[33]<100){&error("���݂̐E�Ƃ��}�X�^�[���Ă��܂���B");}
	if($chara[24] ne "1079"){&error("�p�Y�̏؂ƂȂ���̂𑕔����Ă��Ă��������B");}

	$chara[14]=$in{'item'};
	$chara[33]=1;

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
		$eg="$chara[4]�l���p�Y�E�ɂȂ�܂����B";
		unshift(@chat_mes,"<>���m<>$year�N$mon��$mday��(��)$hour��$min��<><font color=\"yellow\">$eg</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>�g�D�̒j</B><BR>
�u�����c���ꂩ����撣��I�I
�v</font>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}