sub mons_waza{
	if ($i==1) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�悤�����A�������d�w�̏�ցc�B</font><br>
EOM
	}elsif ($i==2) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�ǂ������B�����Ƌ����������Ă����I</font><br>
EOM
	}elsif ($i==3) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>����Ȃ��̂��c�H</font><br>
EOM
	}elsif ($i==4) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�c���҂͂��ꂾ�ȁc�o�����ė����I</font><br>
EOM
	}else{
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>����΂��I</font><br>
EOM
	}
}
sub mons_atowaza{}
1;