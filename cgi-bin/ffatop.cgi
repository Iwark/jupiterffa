#!/usr/local/bin/perl

#------------------------------------------------------#
#�@�{�X�N���v�g�̒��쌠�͂����ɂ���܂��B
#�����Ȃ闝�R�������Ă����̕\�L���폜���邱�Ƃ͂ł��܂���
#�ᔽ�𔭌������ꍇ�A�X�N���v�g�̗��p���~���Ă�������
#�����łȂ��A�R��ׂ����u�������Ă��������܂��B
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

# ���W�X�g���C�u�����̓ǂݍ���
require 'sankasya.pl';

# �����ݒ�t�@�C���̓ǂݍ���
require 'data/ffadventure.ini';

open(IN,"$winner_file") or &error('�t�@�C�����J���܂���ł����B');
	@winner_log = <IN>;
	close(IN);

	@winner = split(/<>/,$winner_log[0]);


if($mente) {
	&error("�����e�i���X���ł�");
}

&header;
	print "<br>";
	&guest_list2;

	&guest_view;
	print "<br><br><br><br><br><br><br>";
	print << "EOM";
<script type="text/javascript">
<!--

// �ݒ�J�n�i�X�N���[���̓�����ݒ肵�Ă��������j

var speed = 100; // �X�N���[���̃X�s�[�h�i1�ɋ߂��قǑ����j
var move = 5; // �X�N���[���̂Ȃ߂炩���i1�ɋ߂��قǂȂ߂炩�Ɂj

// �ݒ�I��


// ������
var x = 0;
var y = 0;
var nx = 0;
var ny = 0;

function scroll(){

	window.scrollBy(0, move); // �X�N���[������

	var rep = setTimeout("scroll()", speed);

	// �X�N���[���ʒu���`�F�b�N�iIE�p�j
	if(document.all){

		x = document.body.scrollLeft;
		y = document.body.scrollTop;

	}
	// �X�N���[���ʒu���`�F�b�N�iNN�p�j
	else if(document.layers || document.getElementById){

		x = pageXOffset;
		y = pageYOffset;

	}

	if(nx == x && ny == y){ // �X�N���[�����I����Ă����珈�����I��

		clearTimeout(rep);

	}
	else{

		nx = x;
		ny = y;

	}

}

// -->
</script>

EOM
exit;
