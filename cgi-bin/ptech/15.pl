sub phissatu{
	if (int(rand(100)) < 20) {
		$zzz=int(rand(3));
		if($zzz==0 and $khp_flg<0){
			$sosei=1;
			$khp_flg=$chara[16] * 2;
			$com4 .="<font class=\"white\" size=5>�S�[�`���t�H�[�X!!</font><br>";
			$kaihuku4 .= "$chara[4]�������Ȃ��đh�����I";
		}
		if($zzz==1 and $mem1[4] and $mem1hp_flg<0){
			$sosei=3;
			$mem1hp_flg=$mem1[16] * 2;
			$com4 .="<font class=\"white\" size=5>�S�[�`���t�H�[�X!!</font><br>";
			$kaihuku4 .= "$mem1[4]�������Ȃ��đh�����I";
		}
		if($zzz==2 and $mem2[4] and $mem2hp_flg<0){
			$sosei=4;
			$mem2hp_flg=$mem2[16] * 2;
			$com4 .="<font class=\"white\" size=5>�S�[�`���t�H�[�X!!</font><br>";
			$kaihuku4 .= "$mem2[4]�������Ȃ��đh�����I";
		}
	}
}
sub patowaza{}
1;