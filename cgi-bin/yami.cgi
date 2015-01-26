#!/usr/local/bin/perl

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# アイテムライブラリの読み込み
require 'item.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

	$back_form = << "EOM";
<br>
<form action="yami.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {&error("アクセスできません！！");}
}
if($mode) { &$mode; }

&item_view;

exit;

#----------------#
#  アイテム表示  #
#----------------#
sub item_view {

	&chara_load;

	&chara_check;

	&item_load;

	&header;

	print <<"EOM";
<h1>闇の空間</h1>
<hr size=0>

<FONT SIZE=3>
<B>？？？？</B><BR>
「ここは…闇の空間…だ…。<br>
ここに入る為には、チケットを持ってくるか、闇封じの剣・闇の羽衣・闇の衣を装備することが必要だ…。<br>
ただし、その３つの装備は、失う覚悟が無ければこの先へ進むことはできない…。<br>
参加費用は100億Ｇだ・・・が、今は特別サービスで３億Ｇだ・・・。<br>
闇封じの剣・闇の羽衣・闇の衣はここで買うこともできるぞ・・・。<br>
EOM
if($chara[24]==1400){
	print <<"EOM";
<font color="yellow">
その武器は・・・！<br>
・・・その武器を更に鍛えたければ30億Ｇ持ってくることだな・・・。<br>
100億Ｇは高すぎるという苦情が届いたので値下げしたのだ・・・フッフッフ。<br>
ここから先に進むのには装備はその武器だけで良い。もちろんその武器が失われることは無いぞ…。<br>
ちなみに闇空間チケットが10枚あれば無料で入場できるぞ。
</font>
」
</FONT><br>
<br>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu2">
<input type=submit class=btn value="闇空間EXへ進む">(チケットは$chara[189]枚所持)
</td>
</form>
EOM
}else{
	print <<"EOM";
」
</FONT><br>
<br>
EOM
if($chara[189]>0){
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu">
<input type=submit class=btn value="チケットを使う">($chara[189]枚所持)
</td>
</form>
EOM
}elsif($item[0] eq "闇封じの剣" and $item[3] eq "闇の羽衣" and $item[6] eq "闇の衣"){
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="susumu">
<input type=submit class=btn value="すすむ">
</td>
</form>
EOM
}else{
	print <<"EOM";
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=1>
<input type=submit class=btn value="闇封じの剣を買う(1億G)">
</td><br>
</form>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=2>
<input type=submit class=btn value="闇の羽衣を買う(100億G)">
</td>
</form><br>
<form action="yami.cgi" method="post">
<td class=b1 align="center">
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="buy">
<input type=hidden name=kai value=3>
<input type=submit class=btn value="闇の衣を買う(10億G)">
</td>
</form>
EOM
}
}

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

sub susumu {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;
	$tic=0;
	$kane=int(((14/15)**7)*10000)/100;
	$kane2=int(((12/13)**7)*10000)/100;
	if($chara[189]>0){$chara[189]-=1;$tic=1;}
	elsif($chara[19]<300000000){&error("お金が足りません。$kane/$kane2");}
	else{
		if($item[0] ne "闇封じの剣" or $item[3] ne "闇の羽衣" or $item[6] ne "闇の衣"){
			&error("どうやらこれ以上進む為には装備がおかしいようだ…。");
		}
		$chara[19]-=300000000;
	}

	$chara[26] = $host;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$souko_item_num = @souko_item;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);
	$souko_def_num = @souko_def;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("武具倉庫がいっぱいです！");
	}elsif ($souko_def_num >= $def_max) {
		&error("防具倉庫がいっぱいです！");
	}elsif ($souko_acs_num >= $acs_max) {
		&error("アクセサリー倉庫がいっぱいです！");
	}

	if($tic==0){$dx=int(rand(4))+2;}

	if(int(rand(10000))==0){
		$i_no=1170;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$mes.="すると…なんと、$i_nameを見つけた！<br>";
	}elsif(int(rand(15-$dx))==0){
		$mes.="すると…なんと、20億Ｇを発見した！<br>";
		$chara[19]+=2000000000;
	}elsif(int(rand(15-$dx))==0){
		$mes.="すると…なんと、神秘の力でＡＰがグーンっと上がった！<br>";
		$chara[13]+=int(rand(8)+5);
	}elsif(int(rand(30-$dx))==0){
		$mes.="すると…なんと、STRがグーンっと上がった！<br>";
		$chara[7]+=int(rand(101)+20);
	}elsif(int(rand(45-$dx))==0){
		$i_no=1121;
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_item,"$i_no<>$i_name<>$i_dmg<>$i_gold<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
		$mes.="すると…なんと、$i_nameを見つけた！<br>";
	}elsif(int(rand(45-$dx))==0){
		$i_no=2121;
		open(IN,"$def_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($i_no eq "$si_no"){last;}
		}
		push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
		$mes.="すると…なんと、$i_nameを見つけた！<br>";
	}elsif(int(rand(100-$dx))==0){
		$i_no="0031";
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $i_no){last;}
		}
		push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
		$mes.="すると…なんと、$ai_nameを見つけた！<br>";
	}elsif(int(rand(15-$dx))==0){
		$ssno=int(rand(12)+71);
		$chara[$ssno]+=1;
		open(IN,"seisan.cgi");
		@seisan_data = <IN>;
		close(IN);
		foreach(@seisan_data){
			($syoukyu3,$sno3,$sname3) = split(/<>/);
			if($sno3 eq $ssno){last;}
		}
		$mes.="すると…なんと、$sname3を発見した！<br>";
	}elsif(int(rand(15-$dx))==0){
		$mes.="すると…なんと、性格が善に傾いたっ<br>";
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$hendo=int(rand(30)+1);
		$chara[65]-=$hendo;
		$chara[64]+=$hendo;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[65]<0){$chara[65]=0;}
		if($chara[64]>100){$chara[64]=100;}
	}elsif(int(rand(15-$dx))==0){
		$mes.="すると…なんと、性格が悪に傾いたっ<br>";
		if($chara[64]==0 and $chara[65]==0){$chara[64]=50;$chara[65]=50;}
		$hendo=int(rand(30)+1);
		$chara[64]-=$hendo;
		$chara[65]+=$hendo;
		if($chara[64]!=100 - $chara[65]){$chara[64]=50;$chara[65]=50;}
		if($chara[64]<0){$chara[64]=0;}
		if($chara[65]>100){$chara[65]=100;}
	}elsif($tic==1){
		$mes="しかし何も起きなかった。";
	}else{
		open(IN,"./kako/$chara[0].cgi");
		$isi_list = <IN>;
		close(IN);
		@isi = split(/<>/,$isi_list);
		$lost=int(rand(10));
		if($lost<5){
			$mes="闇封じの剣がくだけちって沢山の石になった。<br>";
			$hi=int(rand(5));
			$isi[0]+=$hi;
			$mes.="<font color=\"red\">火の石を$hi個手に入れたッ！<br></font>";
			$mizu=int(rand(5));
			$isi[1]+=$mizu;
			$mes.="<font color=\"red\">水の石を$mizu個手に入れたッ！<br></font>";
			$numa=int(rand(5));
			$isi[2]+=$numa;
			$mes.="<font color=\"red\">沼の石を$numa個手に入れたッ！<br></font>";
			$chara[200]=1;
			&item_lose;
		}elsif($lost<9){
			$mes="闇の衣がくだけちって沢山の石になった。";
			$yama=int(rand(5));
			$isi[3]+=$yama;
			$mes.="<font color=\"red\">山の石を$yama個手に入れたッ！<br></font>";
			$yami=int(rand(5));
			$isi[4]+=$yami;
			$mes.="<font color=\"red\">闇の石を$yami個手に入れたッ！<br></font>";
			$hikari=int(rand(5));
			$isi[5]+=$hikari;
			$mes.="<font color=\"red\">光の石を$hikari個手に入れたッ！<br></font>";
			$chara[200]=3;
			&acs_lose;
		}elsif($lost==9){
			$mes="闇の羽衣がくだけちって沢山の石になった。";
			$hi=int(rand(4));
			$isi[0]+=$hi;
			$mes.="<font color=\"red\">火の石を$hi個手に入れたッ！<br></font>";
			$mizu=int(rand(4));
			$isi[1]+=$mizu;
			$mes.="<font color=\"red\">水の石を$mizu個手に入れたッ！<br></font>";
			$numa=int(rand(4));
			$isi[2]+=$numa;
			$mes.="<font color=\"red\">沼の石を$numa個手に入れたッ！<br></font>";
			$yama=int(rand(4));
			$isi[3]+=$yama;
			$mes.="<font color=\"red\">山の石を$yama個手に入れたッ！<br></font>";
			$yami=int(rand(4));
			$isi[4]+=$yami;
			$mes.="<font color=\"red\">闇の石を$yami個手に入れたッ！<br></font>";
			$hikari=int(rand(4));
			$isi[5]+=$hikari;
			$mes.="<font color=\"red\">光の石を$hikari個手に入れたッ！<br></font>";
			$gin=int(rand(4));
			$isi[6]+=$gin;
			$mes.="<font color=\"red\">銀の石を$gin個手に入れたッ！<br></font>";
			$si=int(rand(4));
			$isi[7]+=$si;
			$mes.="<font color=\"red\">死の石を$si個手に入れたッ！<br></font>";
			$mura=int(rand(4));
			$isi[8]+=$mura;
			$mes.="<font color=\"red\">村の石を$mura個手に入れたッ！<br></font>";
			$chara[200]=2;
			&def_lose;
		}
		$new_isi = '';
		$new_isi = join('<>',@isi);
		$new_isi .= '<>';
		open(OUT,">./kako/$chara[0].cgi");
		print OUT $new_isi;
		close(OUT);
	}

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}
sub buy {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);
	$souko_item_num = @souko_item;

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);
	$souko_def_num = @souko_def;

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);
	$souko_acs_num = @souko_acs;

	if ($souko_item_num >= $item_max) {
		&error("武具倉庫がいっぱいです！");
	}
	elsif ($souko_def_num >= $def_max) {
		&error("防具倉庫がいっぱいです！");
	}
	elsif ($souko_acs_num >= $acs_max) {
		&error("アクセサリー倉庫がいっぱいです！$back_form");
	}

	if($in{'kai'}==1){
		if($chara[19]<100000000){
			&error("お金が足りません。");
		}else{
			$chara[19]-=100000000;
			$i_no=1135;
			open(IN,"data/item/stitem.ini");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_item,"$i_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
			$mes="$i_nameを買った！<br>";
		}
	}elsif($in{'kai'}==2){
		if($chara[19]<10000000000){
			&error("お金が足りません。");
		}else{
			$chara[19]-=10000000000;
			$i_no=2147;
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($i_no eq "$si_no"){last;}
			}
			push(@souko_def,"$i_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
			$mes.="$i_nameを買った！<br>";
		}
	}elsif($in{'kai'}==3){
		if($chara[19]<1000000000){
			&error("お金が足りません。");
		}else{
			$chara[19]-=1000000000;
			$i_no="0028";
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$ai_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $i_no){last;}
			}
			push(@souko_acs,"$ai_no<>$ai_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
			$mes.="$ai_nameを買った！<br>";
		}
	}else{&error("エラー");}
	
	$chara[26] = $host;
	$hit=0;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}

sub susumu2 {

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;
	if($chara[189]>9){$chara[189]-=10;}
	elsif($chara[19]<3000000000){&error("お金が足りません。");}
	else{$chara[19]-=3000000000;}

	$chara[26] = $host;

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	$i_name="";
	if(int(rand(80))==0){
		$mayaku[5]+=1;
		$i_name="スタートッカS2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[2]+=1;
		$i_name="スタートッカS";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[3]+=1;
		$i_name="スタートッカA2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(30))==0){
		$mayaku[4]+=1;
		$i_name="スタートッカH2";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(10))==0){
		$mayaku[0]+=1;
		$i_name="スタートッカA";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(10))==0){
		$mayaku[1]+=1;
		$i_name="スタートッカH";
		$new_mayaku = '';
		$new_mayaku = join('<>',@mayaku);
		$new_mayaku .= '<>';
		open(OUT,">./mayaku/$chara[0].cgi");
		print OUT $new_mayaku;
		close(OUT);
	}elsif(int(rand(3))==0){
		if($chara[128]>=5 and $item[1]>9998){
			$kougeki=int(rand(30));
		}else{
			$kougeki=int(rand(100));
		}
		if($item[1]+$kougeki>9999 and $chara[128]<5){$kougeki=9999-$item[1];}
		$item[1]+=$kougeki;
		$mes.="すると…なんと、武器の攻撃力が$kougekiポイント上昇した！";
	}elsif(int(rand(3))==0){
		if($chara[128]>=5 and $item[2]>9998){
			$hit=int(rand(30));
		}else{
			$hit=int(rand(100));
		}
		if($item[2]+$hit>9999 and $chara[128]<5){$hit=9999-$item[2];}
		$item[2]+=$hit;
		$mes.="すると…なんと、武器の命中力が$hitポイント上昇した！";
	}else{
		$mes="しかし何も起きなかった。";
	}
	if($i_name){
		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');
		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		$chmes="$chara[4]様が闇空間EXで、$i_nameを入手しました！";
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		unshift(@chat_mes,"<><font color=\"yellow\">告知</font><>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$chmes</font><>$host<><>\n");

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');

		open(IN,"akuma_log.cgi");
		@akuma_log = <IN>;
		close(IN);

		$aku_sum = @akuma_log;
		$akumes="$chara[4]様が闇空間EXで、$i_nameを入手しました！";
		if($aku_sum > 100) { pop(@akuma_log); }
		unshift(@akuma_log,"$year年$mon月$mday日(火)$hour時$min分$akumes\n");

		open(OUT,">akuma_log.cgi");
		print OUT @akuma_log;
		close(OUT);

		$mes .= "<b><font size=5 color=red>すると…なんと、$i_nameを手に入れた！！</font></b><br>";
	}
	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>$mes</B><BR>
<form action="yami.cgi">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&footer;

	exit;
}