sub mons_waza{
	if ($mons_ritu1 > int(rand(80))) {
	if($smem1hp_flg<50000){
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>��邶��˂����c�B</font><br>
EOM
		$i=51;
	}else{
		$sake1 -= 100;
		$sake2 -= 100;
		$sake3 -= 100;
		$sake4 -= 100;
		$sdmg1 += int(rand(100000));
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
<font class=\"red\" size=5>�܂��܂����W�r��̂悤���Ȃ��o�����ė����b�I�I</font><br>
EOM
	}
	}
}
sub mons_atowaza{}
1;