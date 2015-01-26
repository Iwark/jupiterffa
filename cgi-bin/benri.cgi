#!/usr/local/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

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

# [設定はここまで]------------------------------------------------------------#

# これより下は、CGIのわかる方以外は、変更しないほうが良いです。

#-----------------------------------------------------------------------------#
if($mente) {
	&error("現在バージョンアップ中です。しばらくお待ちください。");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="benri.cgi" >
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

&sakaba;

&error;

exit;

#----------#
#  情報屋  #
#----------#
sub sakaba {

	&chara_load;

	&chara_check;

	&item_load;

	&header;

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	open(IN,"mayaku.cgi");
	@mayaku_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>便利屋</h1>
<hr size=0>
<FONT SIZE=3>
<B>便利屋のお兄さん</B><BR>
「こんにちは。ドリームワールドから引っ越してきた便利屋のスティーブンです。<br>
えっ、ドリームワールドの鍵？　それはちょっと売れないなぁ…(・ｘ・)<br>
ここでは、君の持っている悪魔界のアイテム(<font color="red" size=4>魔薬</font>)を人間界用に調整して使うことができるよ。<br>
<font color="red" size=4>魔薬</font>についての説明は、情報屋のおじさんとかに聞いてください。<br>
そういえば最近弟がカジノの経営を始めたので、ここから行けるから良かったら行ってみてください。<br>
EOM
if($chara[24]==1400){
	print <<"EOM";
<font color="yellow">
えっ、君、その武器はどこで手に入れたの！？<br>
それは凄い武器だよ。魔薬を与えることで成長する武器だ。<br>
さらに、悪魔界から元素を手に入れて、『マテリア』を入手することができれば、武器に特殊な能\力を与えることもできるんだ！<br>
マテリアの精製は、店の奥にあるマテリア室で行っているよ。マテリア精製技術を持っているのは、この世界ではうちだけなのさ！<br>
ただし、その武器がある段階に達するまでは、マテリア室へ通すわけにはいかないな…というより、無駄だからな…。<br>
</font>
EOM
}
if($chara[18]>2000){
	print <<"EOM";
<form action="./casino.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=submit class=btn value="カジノへ">
</form>
EOM
}
	print <<"EOM";
」
</FONT>
<hr size=0>
<br>
EOM
	print <<"EOM";
<table><tr><th></th><th>魔薬</th><th>数</th><th>対象</th></tr>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=mayaku>
EOM
	$i=0;
	foreach(@mayaku){
		if($_>0){
			foreach(@mayaku_data){
				($mayano,$mayaname,$mayakind) = split(/<>/);
				if($mayano == $i){last;}
			}
			print "<tr><th>";
			if($mayakind==0){
				$kind="オリジナル武器";
				if($chara[24]==1400){
					$c=$i+1;
					print "<input type=radio name=item_no value=$c>";
				}else{
					print "×";
				}
			}
			if($mayakind==1){
				$kind="ペット(Lv1000のペットのみ)";
				if($chara[46]==1000){
					$c=$i+1;
					print "<input type=radio name=item_no value=$c>";
				}else{
					print "×";
				}
			}
			if($mayakind==2){
				$kind="ペット";
				$c=$i+1;
				print "<input type=radio name=item_no value=$c>";
			}
			print "</th><th>$mayaname</th><th>$_</th><th>$kind</th></tr>";
		}
		$i++;
	}
	print <<"EOM";
</table><br>
<input type=submit class=btn value="使用する">
</form>
<hr size=0>
EOM
if($chara[128]==5 and $chara[24]==1400){
	print <<"EOM";
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia>
<input type=submit class=btn value="マテリア室へ">
</form>
<hr size=0>
EOM
}
if($chara[24]==1400){
$next_ex = $chara[18] * ($lv_up * 10 - $chara[32] * 50) * 10;
	print <<"EOM";
<br>現在の経験値：$chara[17]/$next_ex<br><br>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=seityou>
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}
sub present {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$chara[146]+=3;
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>はい、どーぞ♪</B><BR></font>
<br>
<form action="benri.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub seityou {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if ($in{'abi'} eq "") {
		&error("与える経験値が入力されていません。$back_form");
	}
	if ($in{'abi'} =~ m/[^0-9]/){
		&error("与える経験値に数字以外の文字が含まれています。$back_form"); 
	}
	if ($in{'abi'} > $chara[17]){
		&error("与える経験値が持っている経験値よりも高いです。$back_form"); 
	}

	$item[26]+=$in{'abi'};
	$chara[17]-=$in{'abi'};
	if(!$item[27]){$item[27]=1;}
	if($item[27]<=10){
		while($item[26] >= $item[27] * 10000000 ){
		$item[1]+=10;
		$item[2]+=5;
		$item[26]-=$item[27] * 10000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]のレベルが$item[27]にあがった！攻撃力＋１０、命中率＋５</font><br>";
		}
	}elsif($item[27]<=100){
		while($item[26] >= $item[27] * 50000000 ){
		$item[1]+=20;
		$item[2]+=10;
		$item[26]-=$item[27] * 50000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]のレベルが$item[27]にあがった！攻撃力＋２０、命中率＋１０</font><br>";
		}
	}else{
		while($item[26] >= $item[27] * 100000000 ){
		$item[1]+=30;
		$item[2]+=15;
		$item[26]-=$item[27] * 100000000;
		$item[27]+=1;
		$lvup.="<font color=\"red\" size=5>$item[0]のレベルが$item[27]にあがった！攻撃力＋３０、命中率＋１５</font><br>";
		}
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
<B>武器に$in{'abi'}の経験値を与えた。</B><BR>
$lvup</font>
<br>
<form action="benri.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub mayaku {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	if(!$in{'item_no'}){&error("ちゃんと選んでください");}
	else{$item_no=$in{'item_no'}-1;}

	if($item_no==0 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(30)+30);
		}else{
			$up=int(rand(100)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up上がった！</font><br>";
	}elsif($item_no==1 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(30)+30);
		}else{
			$up=int(rand(100)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up上がった！</font><br>";
	}elsif($item_no==2 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(30)+30);
			$up2=int(rand(30)+30);
		}else{
			$up1=int(rand(100)+100);
			$up2=int(rand(100)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up1上がった！</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up2上がった！</font><br>";
	}elsif($item_no==3 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(60)+30);
		}else{
			$up=int(rand(200)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up上がった！</font><br>";
	}elsif($item_no==4 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(60)+30);
		}else{
			$up=int(rand(200)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up上がった！</font><br>";
	}elsif($item_no==5 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(60)+30);
			$up2=int(rand(60)+30);
		}else{
			$up1=int(rand(200)+100);
			$up2=int(rand(200)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up1上がった！</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up2上がった！</font><br>";
	}elsif($item_no==6 and $chara[24]==1400){
		if($chara[128]>=5 and $item[1]>9998){
			$up=int(rand(90)+30);
		}else{
			$up=int(rand(300)+100);
		}
		if($item[1]+$up>9999 and $chara[128]<5){$up=9999-$item[1];}
		$item[1]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up上がった！</font><br>";
	}elsif($item_no==7 and $chara[24]==1400){
		if($chara[128]>=5 and $item[2]>9998){
			$up=int(rand(90)+30);
		}else{
			$up=int(rand(300)+100);
		}
		if($item[2]+$up>9999 and $chara[128]<5){$up=9999-$item[2];}
		$item[2]+=$up;
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up上がった！</font><br>";
	}elsif($item_no==8 and $chara[24]==1400){
		if($chara[128]>=5){
			$up1=int(rand(90)+30);
			$up2=int(rand(90)+30);
		}else{
			$up1=int(rand(300)+100);
			$up2=int(rand(300)+100);
		}
		if($item[1]+$up1>9999 and $chara[128]<5){$up1=9999-$item[1];}
		if($item[2]+$up2>9999 and $chara[128]<5){$up2=9999-$item[2];}
		$item[1]+=$up1;
		$item[2]+=$up2;
		$lvup.="<font color=\"red\" size=5>$item[0]の攻撃力が$up1上がった！</font><br>";
		$lvup.="<font color=\"red\" size=5>$item[0]の命中力が$up2上がった！</font><br>";
	}elsif($item_no==10 and $chara[46]==1000){
		$up=int(rand(10000000)+10000000);
		$chara[44]+=$up;
		$lvup.="<font color=\"red\" size=5>$chara[39]の攻撃力が$up上がった！</font><br>";
	}elsif($item_no==11 and $chara[46]==1000){
		$up=int(rand(1000000)+1000000);
		$chara[43]+=$up;
		$chara[42]=$chara[43];
		$lvup.="<font color=\"red\" size=5>$chara[39]のHPが$up上がった！</font><br>";
	}elsif($item_no==12){
		$up=int(rand(100)+1);
		if($chara[46]+$up>1000){
			$chara[46]=1000;
			$lvup.="<font color=\"red\" size=5>$chara[39]のレベルが1000になった！</font><br>";
		}elsif($chara[46]+$up>20 and $chara[46]+$up<120){
			$chara[46]=20;
			$lvup.="<font color=\"red\" size=5>$chara[39]のレベルが20になった！</font><br>";
		}else{
			$chara[46]+=$up;
			$lvup.="<font color=\"red\" size=5>$chara[39]のHPが$up上がった！</font><br>";
		}
	}

	open(IN,"./mayaku/$chara[0].cgi");
	$mayaku_list = <IN>;
	close(IN);
	@mayaku = split(/<>/,$mayaku_list);
	$mayaku[$item_no]-=1;
	$new_mayaku = '';
	$new_mayaku = join('<>',@mayaku);
	$new_mayaku .= '<>';
	open(OUT,">./mayaku/$chara[0].cgi");
	print OUT $new_mayaku;
	close(OUT);

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');
	
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>魔薬を使用した。</B><BR>
$lvup</font>
<br>
<form action="benri.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub materia{

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if(!$isi[29]){$isi[29]=0;}
	if(!$isi[30]){$isi[30]=0;}
	if(!$isi[31]){$isi[31]=0;}
	if(!$isi[32]){$isi[32]=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);

	&header;

	print << "EOM";
<h1>マテリア室</h1><hr>
<font size=3>
<B>便利屋のお兄さん</B><BR>
「ここがマテリア室さ。元素からマテリアを精製し、武器に纏う場所なのだ！<br>
マテリア精製の際の注意事項を説明しておこう。<br>
①マテリアを付けられる数を<font color="red" size=4>キャパ</font>と呼ぶ。<br>
<font color="red" size=4>初期状態のキャパは１であり、最大キャパは４</font>だ。キャパを上げるのには特殊なマテリアが必要だ。<br>
②武器の型によって適応するマテリアが違う。<font color="red" size=4>不適応のマテリアを纏う為には、キャパが２必要</font>だ。<br>
（ただし、精製されるマテリアが武器の型に適応しているかどうかは、\予\め知ることが出来る。）<br>
③マテリアは、成長する。進化させるのにも元素を使う。進化先が複数あるようなマテリアも存在するかもしれないな。<br>
④<font color="red" size=4>最終形態まで進化すると、必要キャパが１増える</font>。不適応マテリアだと、必要キャパが３になる。<br>
⑤<font color="red" size=4>同じ型のマテリアは２つまで</font>しか付けられない。また、同一マテリアを複数纏うことは出来ない。<br>
<br>
以上。マテリア精製にも、マテリア成長にも、尋常でない数の元素が必要になる。<br>
さらに、どのぐらい、どの元素を組み合わせればどのマテリアが出来るのか、それはやってみないとわからない。<br>
ほぼ全てのマテリアは、超強力だからな。元素を石コロのように簡単に集められるとは思わないほうがいいぞ。」<br></font>
<hr>
現在のキャパ：$item[29] / $item[30]<br>
<table><tr><th>現在のマテリア</th><th>レベル</th><th>限界レベル(最終形態)</th></tr>
EOM
	foreach(@mtdata){
		@mt = split(/<>/);
		for($i=31;$i<39;$i++){
			$mtt=int($item[$i]/100+1);
			if($item[$i]%100 == $mt[0]){print "<tr><th>$mt[2]</th><th>$mtt</th><th>$mt[7]</th></tr>";}
		}
	}
	print << "EOM";
</table>
<table width='20%' border=0>
<form action="benri.cgi" >
<table><tr><th>元素</th><th>数</th><th>使用数</th></tr>
<tr><td>火の元素</td><td>$isi[29]</td><td><input type="text" name="hi" size="4"></td></tr>
<tr><td>水の元素</td><td>$isi[30]</td><td><input type="text" name="mizu" size="4"></td></tr>
<tr><td>闇の元素</td><td>$isi[31]</td><td><input type="text" name="yami" size="4"></td></tr>
<tr><td>光の元素</td><td>$isi[32]</td><td><input type="text" name="hikari" size="4"></td></tr>
</table>
<input type="hidden" name="mode" value="seisei">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="マテリア精製に挑戦"></form>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="マテリアの付け替え">
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub materia2{

	&chara_load;

	&chara_check;

	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	if(!$isi[29]){$isi[29]=0;}
	if(!$isi[30]){$isi[30]=0;}
	if(!$isi[31]){$isi[31]=0;}
	if(!$isi[32]){$isi[32]=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	&header;

	print << "EOM";
<h1>マテリア室</h1><hr>
<font size=3>
<B>便利屋のお兄さん</B><BR>
「ここはマテリア倉庫だ。<br>
君のマテリアを外したり、装備できるぞ。<br>
マテリアの保管は、超最新設備で、かつ最新の注意を払って行っている。<br>
膨大な費用がかかっているが…まぁ$chara[4]は、無料で使わせてあげよう。」<br></font>
<hr>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="hazusu">
現在のキャパ：$item[29] / $item[30]<br>
<table><tr><th></th><th>現在のマテリア</th><th>レベル</th><th>限界レベル(最終形態)</th></tr>
EOM
	foreach(@mtdata){
		@mt = split(/<>/);
		for($i=31;$i<39;$i++){
			$mtt=int($item[$i]/100+1);
			if($item[$i]%100 == $mt[0]){
				print << "EOM";
<tr>
<th><input type=radio name=item_no value="$i"></th>
<th>$mt[2]</th>
<th>$mtt</th>
<th>$mt[7]</th>
</tr>
EOM
			}
		}
	}
	print << "EOM";
</table>
<input type=submit class=btn value="マテリアを外す">
</form>
<table>
<br>
<h3>マテリア倉庫</h3>
<form action="benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value="soubi">
<table>
<tr><th></th><th nowrap>なまえ</th><th nowrap>レベル</th><th nowrap>限界レベル</th></tr>
EOM
	$i=1;
	foreach(@mtcdata){
		@mtc = split(/<>/);
		print << "EOM";
<tr>
<td class=b1 align="center">
<input type=radio name=item_no value=$i>
</td>
<td class=b1 nowrap>$mtc[2]</td>
<td align=right class=b1>$mtc[3]</td>
<td align=right class=b1>$mtc[4]</td>
</tr>
EOM
		$i++;
	}
		print << "EOM";
</table>
<input type=submit class=btn value="マテリアを纏う">
</form>
<hr>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=materia>
<input type=submit class=btn value="戻る">
</form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub seisei{

	&chara_load;

	&chara_check;

	&item_load;

	if ($in{'hi'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'mizu'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'yami'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}
	if ($in{'hikari'} =~ m/[^0-9]/){
		&error("数字以外が入力されています。$back_form"); 
	}

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$hi=$in{'hi'};
	if($hi > $isi[29]){&error("火の元素が足りません。$back_form");}
	$mizu=$in{'mizu'};
	if($mizu > $isi[30]){&error("水の元素が足りません。$back_form");}
	$yami=$in{'yami'};
	if($yami > $isi[31]){&error("闇の元素が足りません。$back_form");}
	$hikari=$in{'hikari'};
	if($hikari > $isi[32]){&error("光の元素が足りません。$back_form");}
	$goukei=$hi+$mizu+$yami+$hikari;
	if(!$goukei){&error("元素を１つも使っていません。$back_form");}
	if(!$hi){$hi=0;}if(!$mizu){$mizu=0;}if(!$yami){$yami=0;}if(!$hikari){$hikari=0;}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	foreach(@mtdata){
		@mt = split(/<>/);
		if($mt[3] <= $hi and $mt[4] <= $mizu and $mt[5] <= $yami and $mt[6] <= $hikari){last;}
	}
	if($mt[1] == $item[28]){
		$cap=1;
	}elsif($mt[1]==5){
		if($item[30]==4){
			&error("これ以上キャパを上げることは出来ません。$back_form");
		}else{
			$cap=0;
		}
	}elsif($mt[1]==6){
		if($chara[33]<100){&error("現在の職業をマスターしていません。");}
		$cap=0;
	}else{
		$cap=2;
	}
	if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-2){$cap=1;}elsif($item[31]%100 == $mt[0]){$cap=0;}
	if($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-2){$cap=1;}elsif($item[32]%100 == $mt[0]){$cap=0;}
	if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-2){$cap=1;}elsif($item[33]%100 == $mt[0]){$cap=0;}
	if($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-2){$cap=1;}elsif($item[34]%100 == $mt[0]){$cap=0;}
	if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-2){$cap=1;}elsif($item[35]%100 == $mt[0]){$cap=0;}
	if($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-2){$cap=1;}elsif($item[36]%100 == $mt[0]){$cap=0;}
	if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-2){$cap=1;}elsif($item[37]%100 == $mt[0]){$cap=0;}
	if($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-2){$cap=1;}elsif($item[38]%100 == $mt[0]){$cap=0;}

	if($item[29] < $cap){&error("キャパが足りません。$back_form");}
	
	if($mt[1] == 1){
		if($item[31] and $item[32] and $item[31]%100 != $mt[0] and $item[32]%100 != $mt[0]){
			&error("これ以上物理型のアビを纏うことは出来ません。$back_form");
		}
		if($item[31]%100 == $mt[0]){
			if(int($item[31]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}elsif($item[32]%100 == $mt[0]){
			if(int($item[32]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}else{
			$com1="物理型のマテリアが出来そうですが、";
		}
	}
	if($mt[1] == 2){
		if($item[33] and $item[34] and $item[33]%100 != $mt[0] and $item[34]%100 != $mt[0]){
			&error("これ以上必殺型のアビを纏うことは出来ません。$back_form");
		}
		if($item[33]%100 == $mt[0]){
			if(int($item[33]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}elsif($item[34]%100 == $mt[0]){
			if(int($item[34]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}else{
			$com1="必殺型のマテリアが出来そうですが、";
		}
	}
	if($mt[1] == 3){
		if($item[35] and $item[36] and $item[35]%100 != $mt[0] and $item[36]%100 != $mt[0]){
			&error("これ以上能力型のアビを纏うことは出来ません。$back_form");
		}
		if($item[35]%100 == $mt[0]){
			if(int($item[35]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}elsif($item[36]%100 == $mt[0]){
			if(int($item[36]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}else{
			$com1="能\力\型のマテリアが出来そうですが、";
		}
	}
	if($mt[1] == 4){
		if($item[37] and $item[38] and $item[37]%100 != $mt[0] and $item[38]%100 != $mt[0]){
			&error("これ以上特殊型のアビを纏うことは出来ません。$back_form");
		}
		if($item[37]%100 == $mt[0]){
			if(int($item[37]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}elsif($item[38]%100 == $mt[0]){
			if(int($item[38]/100)==$mt[7]-1){
				&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
			}else{
				$com1="$mt[2]が進化しそうですが、";
			}
		}else{
			$com1="特殊型のマテリアが出来そうですが、";
		}
	}
	if($mt[1] == 5){$com1="キャパアップが出来そうですが、";}
	if($mt[1] == 6){$com1="型職チェンジが出来そうですが";}
	if($mt[1] == 5 or $mt[1] == 6 or $goukei>=90){$com2="成功はほぼ確実でしょう。";}
	elsif($goukei>=75){$com2="成功してもおかしくないでしょう。";}
	elsif($goukei>=50){$com2="成功は運次第です。";}
	elsif($goukei>=25){$com2="成功する見込みは低いです。";}
	elsif($goukei>=10){$com2="まぁ、まず失敗するでしょう。";}
	else{$com2="ほぼ確実に失敗します。";}

	&header;

	print << "EOM";
<h2>火の元素$hi個、水の元素$mizu個、闇の元素$yami個、光の元素$hikari個を使います。<br>
$com1$com2続行しますか？<hr></h2>
<form action="benri.cgi" >
<input type="hidden" name="hi" value=$hi>
<input type="hidden" name="mizu" value=$mizu>
<input type="hidden" name="yami" value=$yami>
<input type="hidden" name="hikari" value=$hikari>
<input type="hidden" name="mode" value="jikko">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="submit" class="btn" value="続行する"></form>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub jikko{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	$hi=$in{'hi'};
	if($hi > $isi[29]){&error("火の元素が足りません。$back_form");}
	$mizu=$in{'mizu'};
	if($mizu > $isi[30]){&error("水の元素が足りません。$back_form");}
	$yami=$in{'yami'};
	if($yami > $isi[31]){&error("闇の元素が足りません。$back_form");}
	$hikari=$in{'hikari'};
	if($hikari > $isi[32]){&error("光の元素が足りません。$back_form");}
	$goukei=$hi+$mizu+$yami+$hikari;
	if(!$goukei){&error("元素を１つも使っていません。$back_form");}

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	foreach(@mtdata){
		@mt = split(/<>/);
		if($mt[3] <= $hi and $mt[4] <= $mizu and $mt[5] <= $yami and $mt[6] <= $hikari){last;}
	}
	if($mt[1] == $item[28]){
		$cap=1;
	}elsif($mt[1]==5){
		if($item[30]==4){
			&error("これ以上キャパを上げることは出来ません。$back_form");
		}else{
			$cap=0;
		}
	}elsif($mt[1]==6){
		if($chara[33]<100){&error("現在の職業をマスターしていません。");}
		$cap=0;
	}else{
		$cap=2;
	}
	if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-2){$cap=1;}elsif($item[31]%100 == $mt[0]){$cap=0;}
	if($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-2){$cap=1;}elsif($item[32]%100 == $mt[0]){$cap=0;}
	if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-2){$cap=1;}elsif($item[33]%100 == $mt[0]){$cap=0;}
	if($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-2){$cap=1;}elsif($item[34]%100 == $mt[0]){$cap=0;}
	if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-2){$cap=1;}elsif($item[35]%100 == $mt[0]){$cap=0;}
	if($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-2){$cap=1;}elsif($item[36]%100 == $mt[0]){$cap=0;}
	if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-2){$cap=1;}elsif($item[37]%100 == $mt[0]){$cap=0;}
	if($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-2){$cap=1;}elsif($item[38]%100 == $mt[0]){$cap=0;}

	if($item[29] < $cap){&error("キャパが足りません。$back_form");}
	
	if($mt[1] == 1){
		if($item[31] and $item[32] and $item[31]%100 != $mt[0] and $item[32]%100 != $mt[0]){
			&error("これ以上物理型のアビを纏うことは出来ません。$back_form");
		}
		if($item[31]%100 == $mt[0] and int($item[31]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}elsif($item[32]%100 == $mt[0] and int($item[32]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}
	}
	if($mt[1] == 2){
		if($item[33] and $item[34] and $item[33]%100 != $mt[0] and $item[34]%100 != $mt[0]){
			&error("これ以上必殺型のアビを纏うことは出来ません。$back_form");
		}
		if($item[33]%100 == $mt[0] and int($item[33]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}elsif($item[34]%100 == $mt[0] and int($item[34]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}
	}
	if($mt[1] == 3){
		if($item[35] and $item[36] and $item[35]%100 != $mt[0] and $item[36]%100 != $mt[0]){
			&error("これ以上能力型のアビを纏うことは出来ません。$back_form");
		}
		if($item[35]%100 == $mt[0] and int($item[35]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}elsif($item[36]%100 == $mt[0] and int($item[36]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}
	}
	if($mt[1] == 4){
		if($item[37] and $item[38] and $item[37]%100 != $mt[0] and $item[38]%100 != $mt[0]){
			&error("これ以上特殊型のアビを纏うことは出来ません。$back_form");
		}
		if($item[37]%100 == $mt[0] and int($item[37]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}elsif($item[38]%100 == $mt[0] and int($item[38]/100)==$mt[7]-1){
			&error("これ以上$mt[2]を進化させることは出来ません。$back_form");
		}
	}

	$isi[29]-=$hi;
	$isi[30]-=$mizu;
	$isi[31]-=$yami;
	$isi[32]-=$hikari;

	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);
	if($mt[0]<5){$goukei=int($goukei*1.5);}
	if($mt[1] == 5){
		$item[29]+=1;
		$item[30]+=1;
		$com="キャパアップに成功しました！";
	}elsif($mt[1] == 6){
		$lock_file = "$lockfolder/syoku$in{'id'}.lock";	
		&lock($lock_file,'SK');
		&syoku_load;
		$syoku_master[51] = 0;
		$syoku_master[52] = 0;
		$syoku_master[53] = 0;
		$syoku_master[54] = 0;
		&syoku_regist;
		&unlock($lock_file,'SK');
		if($chara[51]==71 or $chara[51]==72 or $chara[51]==73 or $chara[51]==74){$chara[51]=0;$chara[13]+=650;}
		if($chara[52]==71 or $chara[52]==72 or $chara[52]==73 or $chara[52]==74){$chara[52]=0;$chara[13]+=650;}
		if($chara[53]==71 or $chara[53]==72 or $chara[53]==73 or $chara[53]==74){$chara[53]=0;$chara[13]+=650;}
		if($chara[54]==71 or $chara[54]==72 or $chara[54]==73 or $chara[54]==74){$chara[54]=0;$chara[13]+=650;}
		$chara[14]=51+int(rand(4));
	
		$chara[33]=1;
		if($mt[0]==98){$chara[33]=80;}
		&chara_regist;
		$lock_file = "$lockfolder/$in{'id'}.lock";
		&unlock($lock_file,'CR');
		$com="型職チェンジに成功しました！";
	}elsif(int(rand(100))<$goukei){
		if($mt[1] == 1){
			if($item[31]%100 == $mt[0]){
				$item[31]+=100;
				if(int($item[31]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[32]%100 == $mt[0]){
				$item[32]+=100;
				if(int($item[32]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[31]){
				$item[32]=$mt[0];
			}else{
				$item[31]=$mt[0];
			}
		}
		if($mt[1] == 2){
			if($item[33]%100 == $mt[0]){
				$item[33]+=100;
				if(int($item[33]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[34]%100 == $mt[0]){
				$item[34]+=100;
				if(int($item[34]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[33]){
				$item[34]=$mt[0];
			}else{
				$item[33]=$mt[0];
			}
		}
		if($mt[1] == 3){
			if($item[35]%100 == $mt[0]){
				$item[35]+=100;
				if(int($item[35]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[36]%100 == $mt[0]){
				$item[36]+=100;
				if(int($item[36]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[35]){
				$item[36]=$mt[0];
			}else{
				$item[35]=$mt[0];
			}
		}
		if($mt[1] == 4){
			if($item[37]%100 == $mt[0]){
				$item[37]+=100;
				if(int($item[37]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[38]%100 == $mt[0]){
				$item[38]+=100;
				if(int($item[38]/100)==$mt[7]-1){$cap=1;}else{$cap=0;}
			}elsif($item[37]){
				$item[38]=$mt[0];
			}else{
				$item[37]=$mt[0];
			}
		}
		$item[29]-=$cap;
		$com="$mt[2]の精製に成功しました！$item[0]に纏います！！！！";
	}else{
		$com="マテリア精製に失敗しました･･･(泣)";
	}

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$com</B><BR><br><br>
</font>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub soubi{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	if(!$in{'item_no'}){
		&error("選択してください。");
	}
	$i=0;
	foreach(@mtcdata){
		@mtc = split(/<>/);
		if($i == $in{'item_no'}-1){last;}
		$i++;
	}
	if($mtc[1] == $item[28]){
		$cap=1;
	}else{
		$cap=2;
	}
	if($mtc[3]==$mtc[4]){ $cap++; }

	if($item[29] < $cap){&error("キャパが足りません。$back_form");}
	
	if($mtc[1] == 1){
		if($item[31] and $item[32]){
			&error("これ以上物理型のマテリアを纏うことは出来ません。$back_form");
		}elsif($item[31]%100 == $mtc[0] or $item[32]%100 == $mtc[0]){
			&error("既に同じマテリアを纏っています。$back_form");
		}elsif($item[31]){
			$item[32]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[31]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 2){
		if($item[33] and $item[34]){
			&error("これ以上必殺型のマテリアを纏うことは出来ません。$back_form");
		}elsif($item[33]%100 == $mtc[0] or $item[34]%100 == $mtc[0]){
			&error("既に同じマテリアを纏っています。$back_form");
		}elsif($item[33]){
			$item[34]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[33]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 3){
		if($item[35] and $item[36]){
			&error("これ以上能力型のマテリアを纏うことは出来ません。$back_form");
		}elsif($item[35]%100 == $mtc[0] or $item[36]%100 == $mtc[0]){
			&error("既に同じマテリアを纏っています。$back_form");
		}elsif($item[35]){
			$item[36]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[35]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}
	if($mtc[1] == 4){
		if($item[37] and $item[38]){
			&error("これ以上特殊型のマテリアを纏うことは出来ません。$back_form");
		}elsif($item[37]%100 == $mtc[0] or $item[38]%100 == $mtc[0]){
			&error("既に同じマテリアを纏っています。$back_form");
		}elsif($item[37]){
			$item[38]=$mtc[0] + ($mtc[3]-1)*100;
		}else{
			$item[37]=$mtc[0] + ($mtc[3]-1)*100;
		}
	}

	$item[29]-=$cap;

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	splice(@mtcdata,$i,1);

	open(OUT,">materia/$chara[0].cgi");
	print OUT @mtcdata;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$mtc[2]を纏いました。</B><BR><br><br>
</font>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="戻る">
</form>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub hazusu{

	&get_host;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');
	&chara_load;

	&chara_check;

	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&lock($lock_file,'IM');
	&item_load;

	open(IN,"materia/$chara[0].cgi");
	@mtcdata = <IN>;
	close(IN);

	if(!$in{'item_no'}){
		&error("選択してください。");
	}

	$ino = $in{'item_no'};

	open(IN,"materiadata.cgi");
	@mtdata = <IN>;
	close(IN);
	$hit=0;
	foreach(@mtdata){
		@mt = split(/<>/);
		if($item[$ino]%100 == $mt[0]){$hit=1;last;}
	}
	if($hit!=1){ &error("エラー。");}
	$mtt = int($item[$ino]/100)+1;

	push(@mtcdata,"$mt[0]<>$mt[1]<>$mt[2]<>$mtt<>$mt[7]<>\n");

	if($mt[1] == $item[28]){
		$cap=1;
	}else{
		$cap=2;
	}
	if($mtt==$mt[7]){ $cap++; }

	$item[$ino] = 0;
	$item[29] += $cap;

	$chara[26] = $host;

	&item_regist;
	$lock_file = "$lockfolder/item$in{'id'}.lock";
	&unlock($lock_file,'IM');

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	open(OUT,">materia/$chara[0].cgi");
	print OUT @mtcdata;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=4><br><br>
<B>$mt[2]を外しました。</B><BR><br><br>
</font>
<form action="./benri.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$new_chara">
<input type=hidden name=mode value=materia2>
<input type=submit class=btn value="戻る">
</form>
<hr size=0><br><br>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub syoku_regist {

	$new_syoku = '';

	for ($s=0;$s<=$chara[14];$s++) {
		if (!$syoku_master[$s]){
			$syoku_master[$s] = 0;
		}
	}

	$new_syoku = join('<>',@syoku_master);

	$new_syoku .= "<>";

	open(OUT,">./syoku/$in{'id'}.cgi");
	print OUT $new_syoku;
	close(OUT);

}