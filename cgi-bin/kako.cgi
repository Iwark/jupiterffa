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
<form action="kako.cgi" >
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

	&header;

	if($chara[190]){
		$hit=0;
		if($chara[190]>2000){
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($chara[190] eq "$si_no"){$hit=1;last;}
			}
		}elsif($chara[190]>1000){
			open(IN,"$item_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
				if($chara[190] eq "$si_no"){$hit=1;last;}
			}
		}else{
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if("$ai_no" eq $chara[190]){$hit=1;last;}
			}
		}
		if($hit){$setu="$i_nameです。";}else{$setu="復元できない特殊装備です。";}
	}else{
		$setu="ありません。";
	}

	open(IN,"./kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);

	open(IN,"kakodata.cgi");
	@kako_data = <IN>;
	close(IN);

	print <<"EOM";
<h1>加工屋</h1>
<hr size=0>
<FONT SIZE=3>
<B>加工屋の女の人</B><BR>
「あら？<B>$chara[4]</B>さんですね・・・？<br>
大陸からやってきた加工屋です。よろしくね＾＾<br>
色んなことをやってるけど、今は準備中なの。<br>
もし狭間で装備が壊れたら私のところに持ってきなさい。復元できるか試してみるから。<br>
闇空間で壊れたアイテムも復元することができるけど高いわよ。」
</FONT>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="home.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="基地">
</form>
EOM
}
	print <<"EOM";
<hr size=0>
加工できるアイテムは…。
<table><tr><th></th><th>作れるもの</th><th>必要な素材１</th><th>必要な素材２</th><th>必要な素材３</th></tr>
<form action="kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kako>
EOM
	$i=0;
	foreach (@kako_data) {
		($ano,$aname,$bno,$bkazu,$cno,$ckazu,$dno,$dkazu) = split(/<>/);
		$bhit=0;$chit=0;$dhit=0;
		if($bkazu>0 and $isi[$bno]>0){$bhit=1;}
		if($ckazu>0 and $isi[$cno]>0){$chit=1;}
		if($dkazu>0 and $isi[$dno]>0){$dhit=1;}
		if($bhit==1 or $chit==1 or $dhit==1){
			open(IN,"sozai.cgi");
			@sozai_data = <IN>;
			close(IN);
			$g=0;$bname="";$cname="";$dname="";
			foreach(@sozai_data){
				($sozainame) = split(/<>/);
				if($g == $bno and $bkazu>0) {$bname="$sozainame×$bkazu";}
				if($g == $cno and $ckazu>0) {$cname="$sozainame×$ckazu";}
				if($g == $dno and $dkazu>0) {$dname="$sozainame×$dkazu";}
				$g++;
			}
			print "<tr><th>";
			if($isi[$bno]>=$bkazu and $isi[$cno]>=$ckazu and $isi[$dno]>=$dkazu){
				$c=$i+1;
				print "<input type=radio name=item_no value=$c>";
			}else{
				print "×";
			}
			print "</th><th>$aname</th><th>$bname</th><th>$cname</th><th>$dname</th></tr>";
		}
		$i++;
	}

	print <<"EOM";
</table><br>
<input type=submit class=btn value="加工する">
</form>
<hr size=0>
復元できる装備は・・・$setu<br>
EOM
if($hit==1){
	$kane=int($chara[18]/100)*10000000;
	if($kane>5000000000){$kane=5000000000;}
	print <<"EOM";
復元しますか？($kane G)<br>
<form action="./kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=hidden name=hmod value=1>
<input type=submit class=btn value="復元">
</form>
EOM
}
if($chara[200]==1){$setu="闇封じの剣です。";}
elsif($chara[200]==2){$setu="闇の羽衣です。";}
elsif($chara[200]==3){$setu="闇の衣です。";}
else{$setu="ありません。";}
	print <<"EOM";
<hr size=0>
(闇空間で壊れた)復元できる装備は・・・$setu<br>
EOM
if($chara[200]>0){
	$kane=int($chara[18]/100)*30000000;
	if($kane>5000000000){$kane=5000000000;}
	print <<"EOM";
復元しますか？($kane G)<br>
<form action="./kako.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=hidden name=hmod value=2>
<input type=submit class=btn value="復元">
</form>
EOM
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'hmod'}==1){$kane=int($chara[18]/100)*10000000;}
	else{$kane=int($chara[18]/100)*30000000;}
	if($kane>5000000000){$kane=5000000000;}

	if($chara[19]<$kane){&error("お金が足りません");}
	else{$chara[19]-=$kane;}

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

	if($chara[190] or $chara[200]){
		$hit=0;
		if($chara[190]>2000 or $chara[200]==2){
			open(IN,"$def_file");
			@log_item = <IN>;
			close(IN);
			foreach(@log_item){
				($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
				if($in{'hmod'}==1 and $chara[190] eq "$si_no"){$hit=1;last;}
				if($in{'hmod'}==2 and $i_name eq "闇の羽衣" and $chara[200]==2){$hit=1;last;}
			}
		}
		if($hit!=1){
			if($chara[190]>1000 or $chara[200]==1){
				if($in{'hmod'}==1){
					open(IN,"$item_file");
					@log_item = <IN>;
					close(IN);
					foreach(@log_item){
						($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
						if($chara[190] eq "$si_no"){$hit=2;last;}
					}
				}elsif($in{'hmod'}==2 and $chara[200]==1){
					open(IN,"data/item/stitem.ini");
					@log_item = <IN>;
					close(IN);
					foreach(@log_item){
						($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
						if($i_name eq "闇封じの剣"){$hit=2;last;}
					}
				}
			}
		}
		if($hit!=1 and $hit!=2){
			open(IN,"$acs_file");
			@acs_array = <IN>;
			close(IN);
			foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
				if($in{'hmod'}==1 and "$ai_no" eq "$chara[190]"){$hit=3;last;}
				if($in{'hmod'}==2 and $chara[200]==3 and $i_name eq "闇の衣"){$hit=3;last;}
			}
		}
		if($hit==1){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_def,"$si_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
			open(OUT,">$souko_folder/def/$chara[0].cgi");
			print OUT @souko_def;
			close(OUT);
		}elsif($hit==2){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_item,"$si_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
			open(OUT,">$souko_folder/item/$chara[0].cgi");
			print OUT @souko_item;
			close(OUT);
		}elsif($hit==3){
			if($in{'hmod'}==1){$chara[190]=0;}
			else{$chara[200]=0;}
			push(@souko_acs,"$ai_no<>$i_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
			open(OUT,">$souko_folder/acs/$chara[0].cgi");
			print OUT @souko_acs;
			close(OUT);
		}else{
			&error("$chara[190]エラー$in{'hmod'}");
		}
	}else{&error("エラー$chara[200]");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$i_nameを復元しました。<br>
</font>
<br>
<form action="kako.cgi" >
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
sub kako {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if(!$in{'item_no'}){&error("ちゃんと選んでください");}
	else{$item_no=$in{'item_no'}-1;}

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

	open(IN,"kakodata.cgi");
	@kako_data = <IN>;
	close(IN);
	$i=0;
	foreach (@kako_data) {
		($ano,$aname,$bno,$bkazu,$cno,$ckazu,$dno,$dkazu) = split(/<>/);
		if($item_no==$i){last;}
		$i++;
	}

	open(IN,"./kako/$chara[0].cgi");
	$isi_list = <IN>;
	close(IN);
	@isi = split(/<>/,$isi_list);
	$jjjj=0;$tttt=0;
	if($ano>9000){
		$ano-=9000;
		if($chara[33]<100){&error("現在の職業をマスターしていません。");}
		$chara[14]=$ano;
		$chara[33]=1;
		$hit=4;
		$jjjj=1;
	}elsif($ano>3000){
		$ano-=3000;
		$isi[$ano]+=1;
		$tttt=1;
		$so=0;
		open(IN,"sozai.cgi");
		@sozai_data = <IN>;
		close(IN);
		foreach(@sozai_data){
			($i_name) = split(/<>/);
			if($so == $ano) {$hit=4;last;}
			$so++;
		}
	}elsif($ano>2000){
		open(IN,"$def_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_def,$i_gold,$i_kai) = split(/<>/);
			if($ano eq "$si_no"){$hit=1;last;}
		}
	}elsif($ano>1000){
		open(IN,"$item_file");
		@log_item = <IN>;
		close(IN);
		foreach(@log_item){
			($si_no,$i_name,$i_dmg,$i_gold,$i_hit) = split(/<>/);
			if($ano eq "$si_no"){$hit=2;last;}
		}
	}else{
		open(IN,"$acs_file");
		@acs_array = <IN>;
		close(IN);
		foreach(@acs_array){
		($ai_no,$i_name,$ai_gold,$ai_kouka,$ai_0up,$ai_1up,$ai_2up,$ai_3up,$ai_4up,$ai_5up,$ai_hitup,$ai_kaihiup,$ai_wazaup,$ai_msg) = split(/<>/);
			if("$ai_no" eq $ano){$hit=3;last;}
		}
	}

	if($hit==1){
		push(@souko_def,"$si_no<>$i_name<>$i_def<>$i_gold<>$i_kai<>\n");
		open(OUT,">$souko_folder/def/$chara[0].cgi");
		print OUT @souko_def;
		close(OUT);
	}elsif($hit==2){
		push(@souko_item,"$si_no<>$i_name<>$i_dmg<>0<>$i_hit<>\n");
		open(OUT,">$souko_folder/item/$chara[0].cgi");
		print OUT @souko_item;
		close(OUT);
	}elsif($hit==3){
		push(@souko_acs,"$ai_no<>$i_name<>$ai_gold<>$ai_kouka<>$ai_0up<>$ai_1up<>$ai_2up<>$ai_3up<>$ai_4up<>$ai_5up<>$ai_hitup<>$ai_kaihiup<>$ai_wazaup<>$ai_msg<>\n");
		open(OUT,">$souko_folder/acs/$chara[0].cgi");
		print OUT @souko_acs;
		close(OUT);
	}elsif($hit==4){
	}else{
		&error("エラー");
	}
	if($bkazu>0){$isi[$bno]-=$bkazu;if($isi[$bno]<0){&error("エラー２b");}}
	if($ckazu>0){$isi[$cno]-=$ckazu;if($isi[$cno]<0){&error("エラー２c");}}
	if($dkazu>0){$isi[$dno]-=$dkazu;if($isi[$dno]<0){&error("エラー２d");}}
	$new_isi = '';
	$new_isi = join('<>',@isi);
	$new_isi .= '<>';
	open(OUT,">./kako/$chara[0].cgi");
	print OUT $new_isi;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

		$lock_file = "$lockfolder/messa$in{'id'}.lock";
		&lock($lock_file,'MS');

		open(IN,"$chat_file");
		@chat_mes = <IN>;
		close(IN);
		$mes_sum = @chat_mes;
		if($mes_sum > $mes_max) { pop(@chat_mes); }
		($sec, $min, $hour, $mday, $mon, $year, $wday, $yday, $isdst) = localtime(time);
		$mon = $mon+1;$year = $year +1900;
		if($jjjj==1){$eg="$chara[4]様が特別職になりました。";}
		elsif($tttt!=1){$eg="$chara[4]様が加工によって$i_nameを入手しました。";}
		if($eg){unshift(@chat_mes,"<>告知<>$year年$mon月$mday日(火)$hour時$min分<><font color=\"yellow\">$eg</font><>$host<><>\n");}

		open(OUT,">$chat_file");
		print OUT @chat_mes;
		close(OUT);

		&unlock($lock_file,'MS');
if($jjjj==1){
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
おめでとうございます！特別職になりました！<br>
</font>
<br>
<form action="kako.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM
}else{
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
加工によって$i_nameを入手しました。<br>
</font>
<br>
<form action="kako.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM
}

	&shopfooter;

	&footer;

	exit;
}