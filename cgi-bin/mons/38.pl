sub mons_waza{
	if($chara[51]==64 or $chara[52]==64 or $chara[53]==64 or $chara[54]==64
	or $mem1[51]==64 or $mem1[52]==64 or $mem1[53]==64 or $mem1[54]==64
	or $mem2[51]==64 or $mem2[52]==64 or $mem2[53]==64 or $mem2[54]==64){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 9999999;$sake2 -= 9999999;
		$sake3 -= 9999999;$sake4 -= 9999999;
		$sdmg1=$sdmg1*111111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉMÅEÅEÅEÉKÉKÉKÅEÅEÅEÅI</font><br>
EOM
		$shpplus1 = int($sdmg1*111111);
		$smem1hp_flg = $maxhp1;
	}elsif($chara[51]==46 or $chara[52]==46 or $chara[53]==46 or $chara[54]==46
	or $mem1[51]==46 or $mem1[52]==46 or $mem1[53]==46 or $mem1[54]==46
	or $mem2[51]==46 or $mem2[52]==46 or $mem2[53]==46 or $mem2[54]==46){
		$dmg1=0;$dmg2=0;$dmg3=0;$dmg4=0;
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*111111;
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉMÅEÅEÅEÉKÉKÉKÅEÅEÅEÅI</font><br>
EOM
		$smem1hp_flg = $maxhp1;
		$shpplus1 = int($sdmg1*111111);
	}elsif($mimg1==254 and $bva<2){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 9999999999;$sake2 -= 9999999999;
		$sake3 -= 9999999999;$sake4 -= 9999999999;
		$sdmg1=$sdmg1*int(rand(100));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉKÉKÉKÉKÉKÉKÉKÅEÅEÅEÅI</font><br>
EOM
	}elsif($bva==2){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*int(rand(1000));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉMÉMÉMÉMÉMÉMÉMÅEÅEÅEÅI</font><br>
EOM
		$mimg1=255;
	}elsif($bva==4){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*int(rand(10000));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉOÉOÉOÉOÉOÉOÉOÅEÅEÅEÅI</font><br>
EOM
		$mimg1=256;
	}elsif($bva==6){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*int(rand(100000));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉQÉQÉQÉQÉQÉQÉQÅEÅEÅEÅI</font><br>
EOM
		$mimg1=257;
	}elsif($bva==8){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*int(rand(1000000));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>ÉSÉSÉSÉSÉSÉSÉSÅEÅEÅEÅI</font><br>
EOM
		$mimg1=258;
	}elsif($bva==10){
		$dmg1=int(rand(100000000));$dmg2=int(rand(100000000));$dmg3=int(rand(100000000));$dmg4=int(rand(100000000));
		$sake1 -= 999999999;$sake2 -= 999999999;
		$sake3 -= 999999999;$sake4 -= 999999999;
		$sdmg1=$sdmg1*int(rand(10000000));
		$scom1 .= <<"EOM";
		<font class=\"red\" size=5>OMEGAÅ@SMASHÅEÅEÅEÅI</font><br>
EOM
		$mimg1=259;
	}
	$bva++;
	if($i>25){
		$khp_flg=0;
		$mem1hp_flg=0;
		$mem2hp_flg=0;
		$mem3hp_flg=0;
		$mem4hp_flg=0;
	$taisyo1 = 4;
	$scom1 .= <<"EOM";
	<font class=\"red\" size=5>ÉOÉKÉKÉKÉKÉKÉKÉbÉKÉKÉKÉKÉKÉbÉKÉKÉKÅIÅIÅI</font><br>
EOM
	}
}
sub mons_atowaza{}
1;