sub mons_waza{
	if ($i==1) {
		if ($item[1]<0){
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���ւ̒Ǖ��I�I</font><br>
EOM
		}elsif(int(rand(10))<5)
			$khp_flg=0;
			$mem1hp_flg=0;
			$mem2hp_flg=0;
			$mem3hp_flg=0;
			$mem4hp_flg=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���ւ̒Ǖ��I�I</font><br>
EOM
		}elsif($item[0] eq "�ŕ����̌�"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߁I�ށc����́A�ŕ����̌��c�I�ł̈߂����ʂ𔭊����Ȃ��I</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߂𔭓������I�S�Ă̍U�����łɋz�����ށI�E�E�E���̈ꌂ���󂯂ė����Ă����Ȃ����̂ɁA���̒��Ő키���i�͂Ȃ��I�I</font><br>
EOM
		}
	}elsif(int(rand(10))<7) {
		$sdmg1=$sdmg1*1111;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�W���s�^���[���h�G���h�I�I</font><br>
EOM
	}elsif(int(rand(10))<7) {
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>���ւ̒Ǖ��I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;