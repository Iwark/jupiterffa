sub mons_waza{
	if ($i==1) {
		if ($item[1]<0){
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$sdmg1=$sdmg1*1111;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�M�l�E�E�E�������Ȃ��̂𑕔����Ă���悤���ȁE�E�E�B���̑����Ő키���Ƃ͋����Ȃ��I�I</font><br>
EOM
		}elsif($item[0] eq "�ŕ����̌�"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߁I�ށc����́A�ŕ����̌��c�I�ł̈߂����ʂ𔭊����Ȃ��I</font><br>
EOM
		}elsif($item[3] eq "�ł̉H��"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߁I�ށc����́A�ł̉H�߁c�I�ł̈߂����ʂ𔭊����Ȃ��I</font><br>
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
	}elsif(int(rand(10))<3) {
		$sdmg1=$sdmg1*1111;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�K�����[���h�G���h�I�I</font><br>
EOM
	}elsif(int(rand(10))<3) {
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�K�����[���h�G���h�I�I</font><br>
EOM
	}elsif(int(rand(5))<3) {
		if($item[0] eq "�ŕ����̌�"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߃��[���h�G���h�I�ށc����́A�ŕ����̌��c�I�ł̈߂����ʂ𔭊����Ȃ��I</font><br>
EOM
		}elsif($item[3] eq "�ł̉H��"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߃��[���h�G���h�I�ށc����́A�ł̉H�߁c�I�ł̈߂����ʂ𔭊����Ȃ��I</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�ł̈߃��[���h�G���h�I�I</font><br>
EOM
		}
	}elsif($chara[51] or $chara[52] or $chara[53] or $chara[54]){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$sdmg1=$sdmg1*111;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�A�r���e�B���E���I�I�I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;