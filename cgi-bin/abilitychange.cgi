#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
#------------------------------------------------------#
#　本スクリプトの著作権は下記の3人にあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
#　FF ADVENTURE 改i v2.1
#　programed by jun-k
#　http://www5b.biglobe.ne.jp/~jun-kei/
#　jun-kei@vanilla.freemail.ne.jp
#------------------------------------------------------#
#　FF ADVENTURE v0.21
#　programed by CUMRO
#　http://cgi.members.interq.or.jp/sun/cumro/mm/
#　cumro@sun.interq.or.jp
#------------------------------------------------------#
#  FF ADVENTURE(改) v1.021
#  remodeling by GUN
#  http://www2.to/meeting/
#  gun24@j-club.ne.jp
#------------------------------------------------------#
#  FF ADVENTURE(いく改)
#　remodeling by いく
#　http://www.eriicu.com
#　icu@kcc.zaq.ne.jp
#------------------------------------------------------#
#--- [注意事項] ------------------------------------------------#
# 1. このスクリプトはフリーソフトです。このスクリプトを使用した #
#    いかなる損害に対して作者は一切の責任を負いません。     	#
# 2. 設置に関する質問はサポート掲示板にお願いいたします。   	#
#    http://icus.s13.xrea.com/cgi-bin/cbbs/cbbs.cgi             #
#    直接メールによる質問は一切お受けいたしておりません。   	#
#---------------------------------------------------------------#
# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# このファイル用設定
$backgif = $sts_back;
$midi = $sts_midi;

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) { &error("現在バージョンアップ中です。しばらくお待ちください。"); }
&decode;

	$back_form = << "EOM";
<br>
<form action="./abilitychange.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}

if($mode) { &$mode; }

&senjutu;

exit;

#----------------#
#  戦術表示      #
#----------------#
sub senjutu {

	&chara_load;

	&chara_check;

	$ahit=0;
	$bhit=0;
	$chit=0;
	$dhit=0;
	$ehit=0;
	$fhit=0;
	$ghit=0;
	$hhit=0;
	@dou_ability = "0<>1<>0<>なし<>動アビリティなしで戦います<>0<>\n";
	@sei_ability = "0<>0<>0<>なし<>静アビリティなしで戦います<>0<>\n";

	# 現在の職業のアビリティ読み込み
	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		if (!$ks_ms || ($ks_ms && $chara[33] >= 100)) {
			#動アビリティ
			if($dousei==1){
				push(@dou_ability,"$_");
				if($chara[51] eq "$ks_no"){
					$ahit = 1;
					$nowdou1_tac = $ks_name;
					$nowdou1_tac_ex = $ks_plus;
				}
				if($chara[52] eq "$ks_no"){
					$bhit = 1;
					$nowdou2_tac = $ks_name;
					$nowdou2_tac_ex = $ks_plus;
				}
				if($chara[53] eq "$ks_no"){
					$chit = 1;
					$nowdou3_tac = $ks_name;
					$nowdou3_tac_ex = $ks_plus;
				}
				if($chara[54] eq "$ks_no"){
					$dhit = 1;
					$nowdou4_tac = $ks_name;
					$nowdou4_tac_ex = $ks_plus;
				}
			}
			#静アビリティ
			if($dousei==0){
				push(@sei_ability,"$_");
				if($chara[55] eq "$ks_no"){
					$ehit = 1;
					$nowsei1_tac = $ks_name;
					$nowsei1_tac_ex = $ks_plus;
				}
				if($chara[56] eq "$ks_no"){
					$fhit = 1;
					$nowsei2_tac = $ks_name;
					$nowsei2_tac_ex = $ks_plus;
				}
				if($chara[57] eq "$ks_no"){
					$ghit = 1;
					$nowsei3_tac = $ks_name;
					$nowsei3_tac_ex = $ks_plus;
				}
				if($chara[58] eq "$ks_no"){
					$hhit = 1;
					$nowsei4_tac = $ks_name;
					$nowsei4_tac_ex = $ks_plus;
				}
			}
		}
	}

	#マスターした戦術のインクルード
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 100 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				foreach (@gettac){
				($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
				if($dousei==1){
					push(@dou_ability,"$_");
					if($chara[51] eq "$ks_no"){
						$ahit = 1;
						$nowdou1_tac = $ks_name;
						$nowdou1_tac_ex = $ks_plus;
					}
					if($chara[52] eq "$ks_no"){
						$bhit = 1;
						$nowdou2_tac = $ks_name;
						$nowdou2_tac_ex = $ks_plus;
					}
					if($chara[53] eq "$ks_no"){
						$chit = 1;
						$nowdou3_tac = $ks_name;
						$nowdou3_tac_ex = $ks_plus;
					}
					if($chara[54] eq "$ks_no"){
						$dhit = 1;
						$nowdou4_tac = $ks_name;
						$nowdou4_tac_ex = $ks_plus;
					}
				}
				if($dousei==0){
					push(@sei_ability,"$_");
					if($chara[55] eq "$ks_no"){
						$ehit = 1;
						$nowsei1_tac = $ks_name;
						$nowsei1_tac_ex = $ks_plus;
					}
					if($chara[56] eq "$ks_no"){
						$fhit = 1;
						$nowsei2_tac = $ks_name;
						$nowsei2_tac_ex = $ks_plus;
					}
					if($chara[57] eq "$ks_no"){
						$ghit = 1;
						$nowsei3_tac = $ks_name;
						$nowsei3_tac_ex = $ks_plus;
					}
					if($chara[58] eq "$ks_no"){
						$hhit = 1;
						$nowsei4_tac = $ks_name;
						$nowsei4_tac_ex = $ks_plus;
					}
				}
				}
			}
			$i++;
		}
	}

	if(!$ahit) {$nowdou1_tac = "なし";$nowdou1_tac_ex = "動１アビリティなしで戦います";}
	if(!$bhit) {$nowdou2_tac = "なし";$nowdou2_tac_ex = "動２アビリティなしで戦います";}
	if(!$chit) {$nowdou3_tac = "なし";$nowdou3_tac_ex = "動３アビリティなしで戦います";}
	if(!$dhit) {$nowdou4_tac = "なし";$nowdou4_tac_ex = "動４アビリティなしで戦います";}
	if(!$ehit) {$nowsei1_tac = "なし";$nowsei1_tac_ex = "静１アビリティなしで戦います";}
	if(!$fhit) {$nowsei2_tac = "なし";$nowsei2_tac_ex = "静２アビリティなしで戦います";}
	if(!$ghit) {$nowsei3_tac = "なし";$nowsei3_tac_ex = "静３アビリティなしで戦います";}
	if(!$hhit) {$nowsei4_tac = "なし";$nowsei4_tac_ex = "静４アビリティなしで戦います";}

	&header;

	print <<"EOM";
<h1>アビリティチェンジ</h1>
アビリティチェンジを行います<br>
動アビリティ：戦闘中に一定確率で発動<br>
静アビリティ：常に発動<br>
アビリティはアビリティポイントに応じて登録できます。<br>
注：魔法装備時に、その種の魔法装備アビリティを外すと、現在装備している魔法が失われます。<br>
現在のアビリティポイント：$chara[13]
<hr size=0>
<BR>
<form action="abilitychange.cgi" >
<table border=0 align="center" width='100%'>
<tr>
<td valign=top width='50%'>
<table width="100%">
<tr><td id="td1" colspan="5" class="b2" align="center">現在のアビリティ</td></tr>
<td class=b1>名前</td><td class=b1>要求値</td><td class=b1>説明</td>\n
<tr><td class=b1><input type=radio name=ab value="1">
動アビリティ１</td><td class=b1>$nowdou1_tac</td><td class=b1>$nowdou1_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="2">
動アビリティ２</td><td class=b1>$nowdou2_tac</td><td class=b1>$nowdou2_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="3">
動アビリティ３</td><td class=b1>$nowdou3_tac</td><td class=b1>$nowdou3_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="4">
動アビリティ４</td><td class=b1>$nowdou4_tac</td><td class=b1>$nowdou4_tac_ex</td>
<tr><td class=b1><input type=radio name=ab value="5">
静アビリティ１</td><td class=b1>$nowsei1_tac</td><td class=b1>$nowsei1_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="6">
静アビリティ２</td><td class=b1>$nowsei2_tac</td><td class=b1>$nowsei2_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="7">
静アビリティ３</td><td class=b1>$nowsei3_tac</td><td class=b1>$nowsei3_tac_ex</td>
</tr>
<tr><td class=b1><input type=radio name=ab value="8">
静アビリティ４</td><td class=b1>$nowsei4_tac</td><td class=b1>$nowsei4_tac_ex</td>
</tr>
</td>
</tr>
</table>
</td>
EOM
	print <<"EOM";
<td valign="top">
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">動アビリティ</td></tr>
<tr>
<td class=b1></td><td class=b1>名前</td><td class=b1>要求値</td><td class=b1>説明</td>\n
EOM
	foreach(@dou_ability){
		($s_no,$s_dousei,$s_youkyu,$s_name,$s_plus,$s_ms) = split(/<>/);
		print "<tr>\n";
		print "<td class=b1><input type=radio name=senjutu_no value=\"$s_no\"></td><td class=b1>$s_name</td><td class=b1>$s_youkyu</td><td class=b1>$s_plus</td>\n";
		print "</tr>\n";
	}
	print <<"EOM";
</td>
</tr>
</table>
<table width="100%">
<tr><td id="td1" colspan="4" class="b2" align="center">静アビリティ</td></tr>
<tr>
<td class=b1></td><td class=b1>名前</td><td class=b1>要求値</td><td class=b1>説明</td>\n
EOM
	foreach(@sei_ability){
		($t_no,$t_dousei,$t_youkyu,$t_name,$t_plus,$t_ms) = split(/<>/);
		if($t_name){
			print "<tr>\n";
			print "<td class=b1><input type=radio name=senjutu_no value=\"$t_no\"></td><td class=b1>$t_name</td><td class=b1>$t_youkyu</td><td class=b1>$t_plus</td>\n";
			print "</tr>\n";
		}
	}
	print <<"EOM";
</td>
</tr>
</table>
</table>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=hidden name=mode value=senjutu_henkou>
<input type=submit class=btn value="変更する">
</form>
<form action="$script" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$chara_log">
<input type=submit class=btn value="ステータス画面へ">
</form>
EOM

	&footer;

	exit;
}

#----------------#
#  戦術変更      #
#----------------#
sub senjutu_henkou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	if($in{'ab'}==""){&error("ちゃんと選択してね＾＾$back_form");} 

	$senjutu_no=$in{'ab'}+50;
	@log_senjutu = "0<>0<>1<>なし<>動アビリティなしで戦います<>0<>\n";

	open(IN,"$tac_folder/tac$chara[14].ini");
	@gettac = <IN>;
	close(IN);
	foreach (@gettac){
		($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
		# 2004年7月7日修正
		if(!$ks_ms || ($ks_ms && $chara[33] >= 100)){
			push(@log_senjutu,"$_");
		}
		if($chara[$senjutu_no] eq "$ks_no"){
			$now_youkyu = $youkyu;
		}
	}

	#マスターした戦術のインクルード
	if ($master_tac) {
		&syoku_load;
		$i = 0;
		foreach (@syoku_master) {
			if ($_ >= 100 && $i != $chara[14]) {
				open(IN,"$tac_folder/tac$i.ini");
				@gettac = <IN>;
				close(IN);
				push(@log_senjutu,@gettac);
				foreach (@gettac){
				($ks_no,$dousei,$youkyu,$ks_name,$ks_plus,$ks_ms) = split(/<>/);
				if($chara[$senjutu_no] eq "$ks_no"){
					$now_youkyu = $youkyu;
					last;
				}
				}
			}
			$i++;
		}
	}

	$hit=0;
	foreach(@log_senjutu){
		($s_no,$s_name) = split(/<>/);
		if($in{'senjutu_no'} eq "$s_no") { $hit=1;last; }
	}

	if(!$hit) { &error("そんな戦術はありません"); }

	open(IN,"$tac_file");
	@alltac = <IN>;
	close(IN);

	foreach (@alltac){
		($a_no,$a_dousei,$a_youkyu,$a_name,$a_plus,$a_ms) = split(/<>/);
		if($in{'senjutu_no'} eq $a_no){
			$new_youkyu = $a_youkyu;
			last;
		}
	}

	if($chara[13] + $now_youkyu < $new_youkyu ){&error("ポイントが足りません");}
	if($senjutu_no<55 and $a_no ne 0){
		if($a_dousei==0){&error("動アビリティではありません");}
	}
	if($senjutu_no>54){
		if($a_dousei==1){&error("静アビリティではありません$dousei");}
	}
	&get_host;

	#巨人化
	if($in{'senjutu_no'}==84){
		if($chara[55]==84 or $chara[56]==84 or $chara[57]==84 or $chara[58]==84){
			&error("このアビリティは１つしかつけられません。");
		}else{
			$chara[16]=int($chara[16]*100);
			$chara[15]=$chara[16];
		}
	}
	#巨人化解除
	if($chara[$senjutu_no]==84 and $in{'senjutu_no'} !=84){
		$chara[16]=int($chara[16]/100);
		$chara[15]=$chara[16];
	}
	
	#アビリティが魔法かつ、その種の魔法を装備している時、
	if($chara[$senjutu_no]==3 and $in{'senjutu_no'} !=3 and $chara[59]<=10){$chara[59]=0;}
	if($chara[$senjutu_no]==13 and $in{'senjutu_no'} !=13 and $chara[59]>10 and $chara[59]<=20){$chara[59]=0;}
	if($chara[$senjutu_no]==27 and $in{'senjutu_no'} !=27 and $chara[59]>20 and $chara[59]<=30){$chara[59]=0;}
	if($chara[$senjutu_no]==31 and $in{'senjutu_no'} !=31 and $chara[59]>30 and $chara[59]<=40){$chara[59]=0;}
	if($chara[$senjutu_no]==35 and $in{'senjutu_no'} !=35 and $chara[59]>40 and $chara[59]<=50){$chara[59]=0;}
	if($in{'senjutu_no'}==55){
		if($chara[55]==55 or $chara[56]==55 or $chara[57]==55 or $chara[58]==55){
			&error("このアビリティは１つしかつけられません。");
		}
	}
	#ステータスを上昇
	if($in{'senjutu_no'}==70){
		$chara[7]+=2500;
		$chara[8]+=2500;
		$chara[9]+=2500;
		$chara[10]+=2500;
		$chara[11]+=2500;
		$chara[12]+=2500;
	}
	#アビリティがステータスを上昇させている時、
	if($chara[$senjutu_no]==70){
		$chara[7]-=2500;
		$chara[8]-=2500;
		$chara[9]-=2500;
		$chara[10]-=2500;
		$chara[11]-=2500;
		$chara[12]-=2500;
		if($chara[7]<1){$chara[7]=1;}
		if($chara[8]<1){$chara[8]=1;}
		if($chara[9]<1){$chara[9]=1;}
		if($chara[10]<1){$chara[10]=1;}
		if($chara[11]<1){$chara[11]=1;}
		if($chara[12]<1){$chara[12]=1;}
	}

	$chara[$senjutu_no] = $in{'senjutu_no'};

	$chara[13]=$chara[13]+$now_youkyu-$new_youkyu;

	&chara_regist;
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>アビリティを変更しました</h1>
<hr size=0>
<form action="./abilitychange.cgi" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="戻る">
</form><br><br>
<form action="$script" >
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name=mydata value="$new_chara">
<input type=submit class=btn value="ステータス画面へ">
</form>
EOM

	&footer;

	exit;
}

