#! /usr/local/bin/perl

require"ffadventure.ini";

$mes="�yFFA�j���[�X�E�E�E�ŐV�̏󋵂����Ԋu�Ŏ����X�V�z\n�����݂�FFA�L�^\n";
open (IN,"$winner_file");
$LINE = <IN>;
close (IN);
($wid,$wpass,$wsite,$wurl,$wname,$wsex,$wchara,$wn_0,$wn_1,$wn_2,$wn_3,$wn_4,$wn_5,$wn_6,$wsyoku,$whp,$wmaxhp,$wex,$wlv,$wgold,$wlp,$wtotal,$wkati,$wwaza,$witem,$wmons,$whost,$wdate,$wcount,$lsite,$lurl,$lname,$wmori,$wdef,$wtac,$lid,$wkumite)=split(/<>/,$LINE);
$mes.="�`�����v��E$wname����$lname����ɏ����i$wcount�A���j�c�c\n";

open(IN,"$taikai_file");
$LINE = <IN>;
close(IN);
($rnumb,$pname,$pid,$ename) = split(/<>/,$LINE);
$mes.="���L�^�E$pname����";
$mes.=$rnumb-1;
$mes.="�A���i$ename����ɔs�k�j�c�c\n";

$mes.=<<"EOM";
�����݂�FFA�󋵁E�E�����
���Ǘ��l����̂��m�点
�T���v���ł�
�����������ɃX�N���[�����܂�
���Ǘ��l����̂��m�点�E�E�����
�yFFA�j���[�X�E�E�����z
EOM

print"Content-type: text/plain; CHARSET=Shift_JIS\n\n";
print $mes;

exit;
