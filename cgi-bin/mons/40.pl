sub mons_waza{
	if($chara[51]==64 or $chara[52]==64 or $chara[53]==64 or $chara[54]==64
	or $mem1[51]==64 or $mem1[52]==64 or $mem1[53]==64 or $mem1[54]==64
	or $mem2[51]==64 or $mem2[52]==64 or $mem2[53]==64 or $mem2[54]==64){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*1111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�ٔ��̓Z�R�C�����̂����I</font><br>
EOM
		$shpplus1 = int($sdmg1*1111);
		$smem1hp_flg = $smem1hp_flg + 3000000000000000000 - 1;
	}
	if($i==1){
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>��[���B�����E�`�P�b�g���ق����̂��H</font><br>
EOM
		$ticket2+=1;
	}
	if($smem1hp_flg < 1000000000000 and int(rand(10)) == 0) {
		$sdmg1=$sdmg1*9999;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$shpplus1 = int($smem1hp_flg * 0.5);
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�ӂ͂͂͂͂͂͂͂́I�I</font><br>
EOM
	}
	elsif($smem1hp_flg < 10000000000000 and int(rand(10)) == 0) {
		$sdmg1=$sdmg1*1111;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$shpplus1 = int($smem1hp_flg * 0.4);
		$sake1 -= 100;$sake2 -= 100;
		$sake3 -= 100;$sake4 -= 100;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�������������������I�I</font><br>
EOM
	}
	elsif($i > 2 and $i<10 and $smem1hp_flg < 1000000000000 and int(rand(10)) < 5){
		$sdmg1=$sdmg1*1111;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$shpplus1 = int($smem1hp_flg * 0.3);
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�ǂ������Ă���I�I</font><br>
EOM
	}
	elsif($i == 4){
		$sdmg1=$sdmg1*1111;
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$shpplus1 = int($smem1hp_flg * 0.2);
		$sake1 -= 9999;$sake2 -= 9999;
		$sake3 -= 9999;$sake4 -= 9999;
		$taisyo1 = 4;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�{���̓R�b�`���I</font><br>
EOM
	}
	elsif(int(rand(10))==0) {
		if($item[3] eq "�����̊Z"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�����̊Z�c���B�ʔ������̂𑕔����Ă���ȁc�B</font><br>
EOM
		}else{
			$sake1 -= 9999;$sake2 -= 9999;
			$sake3 -= 9999;$sake4 -= 9999;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���̍U����������邩�Ȃ��I�H</font><br>
EOM
		}
	}
	elsif($i >= 5 and int(rand(15))==1) {
		if($item[3] eq "�����̊Z"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�����̊Z�c���B�ʔ������̂𑕔����Ă���ȁc�B</font><br>
EOM
		}else{
			$shpplus1 = int($smem1hp_flg * 0.1);
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���񕜁I�I</font><br>
EOM
		}
	}
	elsif($i >= 10 and int(rand(10))==0) {
		if($item[3] eq "�����̊Z"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�����̊Z�c���B�ʔ������̂𑕔����Ă���ȁc�B</font><br>
EOM
		}else{
			$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���h��I</font><br>
EOM
		}
	}
	elsif(int(rand(10))<5) {
		if($item[3] eq "�����̊Z"){
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�����̊Z�c���B�ʔ������̂𑕔����Ă���ȁc�B</font><br>
EOM
		}else{
			$sdmg1=$sdmg1*1111;
			$taisyo1 = 4;
			$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�h���[���\\�[�h�I</font><br>
EOM
		}
	}
	elsif($item[0] eq "�}�V���K��"){
		$dmg1=$dmg1*111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�}�V���K���I�H</font><br>
EOM
	}
}
sub mons_atowaza{}
1;