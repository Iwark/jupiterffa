sub phissatu{
	if ($khp_flg>0 and int(rand(100)) < 25) {
		$hpplus1 = $dmg4 + int(rand($chara[46]*5));
		$dmg4 = 0;
		$com4 .="<font class=\"white\" size=5>�q�[�����O�I�I</font><br>";
		$kaihuku4 .= "$chara[4] �̂g�o�� $hpplus1 �񕜂����I��";
	}
}
sub patowaza{}
1;