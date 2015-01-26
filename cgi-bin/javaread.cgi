#! /usr/local/bin/perl

require"ffadventure.ini";

$mes="【FFAニュース・・・最新の状況を一定間隔で自動更新】\n▼現在のFFA記録\n";
open (IN,"$winner_file");
$LINE = <IN>;
close (IN);
($wid,$wpass,$wsite,$wurl,$wname,$wsex,$wchara,$wn_0,$wn_1,$wn_2,$wn_3,$wn_4,$wn_5,$wn_6,$wsyoku,$whp,$wmaxhp,$wex,$wlv,$wgold,$wlp,$wtotal,$wkati,$wwaza,$witem,$wmons,$whost,$wdate,$wcount,$lsite,$lurl,$lname,$wmori,$wdef,$wtac,$lid,$wkumite)=split(/<>/,$LINE);
$mes.="チャンプ戦・$wnameさんが$lnameさんに勝利（$wcount連勝）……\n";

open(IN,"$taikai_file");
$LINE = <IN>;
close(IN);
($rnumb,$pname,$pid,$ename) = split(/<>/,$LINE);
$mes.="大会記録・$pnameさんが";
$mes.=$rnumb-1;
$mes.="連勝（$enameさんに敗北）……\n";

$mes.=<<"EOM";
▲現在のFFA状況・・おわり
▼管理人からのお知らせ
サンプルです
こういう風にスクロールします
▲管理人からのお知らせ・・おわり
【FFAニュース・・おわり】
EOM

print"Content-type: text/plain; CHARSET=Shift_JIS\n\n";
print $mes;

exit;
