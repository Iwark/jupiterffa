sub phissatu{
	if ($taisyo1 == 3 or $taisyo2 == 3 or $taisyo3 == 3 or $taisyo4 == 3){
		if( int(rand(100)) < 30) {
			$com4 .="<font class=\"white\" size=5>�N���X�J�E���^�[�I�I</font><br>";
			$dmg4 = $dmg4 * 2;
			$pkaihi += 1000000;
		}
	}
}
sub patowaza{}
1;