sub mons_waza{
	if ($i==1) {
		if($chara[14]!=44){
		$scom1 .= <<"EOM";
			<font class=\"red\" size=5>�䂪�����́A���~��̂݁I����ł͘b�ɂȂ��ȁI�I</font><br>
EOM
		}else{
		$scom1 .= <<"EOM";
			<font class=\"red\" size=5>���E�E�E����A���~�炩�I�I�J���x�����Ă���I�I</font><br>
EOM
		}
	}elsif ($i==2) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>���������c�B</font><br>
EOM
	}elsif ($i==3) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�Ȃ񂾂�c�B</font><br>
EOM
	}elsif ($i==4) {
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>�Ӂc���낻��A�邩�c�B</font><br>
EOM
	}elsif($i==5 or $i>20){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>����΂��I</font><br>
EOM
	}elsif($item[0] eq "�������イ" and $chara[196]==2 and $chara[52]==63){
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>���ɒ��ԂɂȂ�Ƃȁc�����Ƃ��뒆�X�̎����c������ʔ��������ȁc�B</font><br>
EOM
		$smem1hp_flg = int($smem1hp_flg / 100);
	}
}
sub mons_atowaza{}
1;