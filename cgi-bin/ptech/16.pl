sub phissatu{
	if (int(rand(100)) < 10) {
			$com4 .="<font class=\"white\" size=5>�S�[�`���t�F�j�b�N�X!!</font><br>";
			$kaihuku4 .= "�o�s�����o�[���S���h��A���킶��Ɠ����o�����I�I";
		if($khp_flg<0){
			$khp_flg=int($chara[16]/4);
		}
		if($mem1[4] and $mem1hp_flg<0){
			$mem1hp_flg=int($mem1[16]/4);
		}
		if($mem2[4] and $mem2hp_flg<0){
			$mem2hp_flg=int($mem2[16]/4);
		}
	}
}
sub patowaza{}
1;