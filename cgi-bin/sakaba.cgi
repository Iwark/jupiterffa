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
<form action="sakaba.cgi" >
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

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$bug="";$hit=0;
	foreach(@member_data){
		($name,$leader,$lv,$mem,$com) = split(/<>/);
		$bug=$name;$cou=0;$g=0;
		foreach(@member_data){
			($name,$leader,$lv,$mem,$com) = split(/<>/);
			if($bug eq $name){$cou++;}
			if($cou==2){splice(@member_data,$g,1);$hit=1;last;}
			$g++;
		}
	}
	if($hit==1){
		open(OUT,">allparty.cgi");
		print OUT @member_data;
		close(OUT);
	}

	foreach(@member_data){
		($pp_name,$pp_leader,$pp_lv,$pp_mem,$pp_com) = split(/<>/);
		if($pp_leader eq $chara[4]){last;}
	}

	print <<"EOM";
<h1>酒場</h1>
<hr size=0>
<FONT SIZE=3>
<B>酒場のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ここでは他のメンバーとPTを組むことができるぞーっ<br>
パーティを結成する時は、8文字以内でパーティ名、30字以内でコメントを設定してな。<br>
あんまり強さが違うと、パーティに加入できないぞ。<br>
リーダーが脱退すると、次のメンバーがリーダーになるぞ。<br>
なお、たまに、<font color="red" size=5>PTに入れない日があるぞ！(解散日)</font>」
</FONT>
<hr size=0>
EOM
if($chara[61] and $pp_leader eq $chara[4]){
	print <<"EOM";
<form action="sakaba.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=henko>
コメント　：<input type="text" name="p_com" value="" size=40><br>
<br>　　
<input type=submit class=btn value="パーティ情報変更">
</form>
<form action="sakaba.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kaisan>
<br>　　
<input type=submit class=btn value="脱退">
</form>
<form action="sakaba.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=keru>
対象名：<input type="text" name="keri" value="" size=10><br>
<br>　　
<input type=submit class=btn value="メンバーの強制脱退">
</form>
EOM
}else{
	print <<"EOM";
<form action="sakaba.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
パーティ名：<input type="text" name="p_name" value="" size=40><br>
コメント　：<input type="text" name="p_com" value="" size=40><br>
<br>　　
<input type=submit class=btn value="パーティ結成">
</form>
<form action="sakaba.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=dattai>
<br>　　
<input type=submit class=btn value="脱退">
</form>
EOM
}
	print <<"EOM";
<table border=1>
<th colspan="3">パーティ名</th><th>リーダー</th><th>加\入\可\能\レベル</th><th>メンバー</th><th>コメント</th></tr><tr>
EOM
	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$memc=0;$hit=0;
	foreach(@member_data){
		($pp_name,$pp_leader,$pp_lv,$pp_mem,$pp_com,$pp_mem1) = split(/<>/);
		if($pp_mem){
			if(($mday % 14) == ($mon % 7)){
				$member_data[$memc]="$pp_name<>$pp_leader<>$pp_lv<>1<>$pp_com<>$pp_mem1<>\n";
				$pp_mem=1;$hit=1;
			}
			$pp_maxmem=3;
			$lock_file = "$lockfolder/$pp_mem1.lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$pp_mem1.cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$pp_mem1.lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);
			$ptlim=int($mem1[18]/1000)*50+100;
			if($mem1[70]==1){$pp_minlv=$mem1[18]-$ptlim;$pp_maxlv=$mem1[18]+$ptlim;}
			elsif($mem1[70]==2){$pp_minlv=$mem1[18]-20000;$pp_maxlv=$mem1[18]+20000;}
			else{$pp_minlv=$mem1[18]+$mem1[37]*100-300;$pp_maxlv=$mem1[18]+$mem1[37]*100+300;}
			if($pp_minlv<1){$pp_minlv=1;}
			print <<"EOM";
			<tr>
			<td>
			<form action="./sakaba.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=kanyu>
			<input type=hidden name=kanyu_id value=$pp_name>
			<input type=submit class=btn value="加入">
			</form>
			</td>
			<td>
			<form action="./sakaba.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=hyouji>
			<input type=hidden name=hyouji_id value=$pp_name>
			<input type=submit class=btn value="メンバー">
			</form>
			</td>
			<td align=center>$pp_name</td>
			<td align=center>
EOM
			if($mem1[70]<1){print "$pp_leader";}
			elsif($mem1[70]<2){print"<font color=\"yellow\">$pp_leader</font>";}
			else{print"<font color=\"red\">$pp_leader</font>";}
			print <<"EOM";
			</td>
			<td align=center>$pp_minlv～$pp_maxlv</td>
			<td align=center>$pp_mem\/$pp_maxmem</td>
			<td align=center>$pp_com</td>
			</tr>
EOM
		}
		$memc++;
	}
	if($hit==1){
		open(OUT,">allparty.cgi");
		print OUT @member_data;
		close(OUT);
	}
	print <<"EOM";
</tr>
</table>
<p>
EOM
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub make {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'CR');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[0] eq "test" or $chara[0] eq "test2"){
		&error("testキャラはパーティを作成できません。$back_form");
	}
	if ($chara[61]){&error("既にパーティに所属しています。$back_form");}
	else{
		if ($in{'p_name'} eq "") {
			&error("パーティ名が入力されていません。$back_form");
		}
		if (length($in{'p_name'}) > 16) {
			&error("パーティ名が長すぎます。$back_form");
		}
		if (length($in{'p_com'}) > 60) {
			&error("コメントが長すぎます。$back_form");
		}
	}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[5] eq $array[6]){splice(@array,6,1);$array[3]-=1;$hit=1;}
		if($array[5] eq $array[7]){splice(@array,7,1);$array[3]-=1;$hit=1;}
		if($array[6] eq $array[7]){splice(@array,7,1);$array[3]-=1;$hit=1;}
		if($hit){
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			$hit=0;
		}
		$i++;
	}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$g=0;
	foreach(@member_data){
		($pp_name,$pp_leader,$pp_lv,$pp_mem,$pp_com,$mem1,$mem2,$mem3) = split(/<>/);
		if($pp_mem <= 0 or !$pp_leader){splice(@member_data,$g,1);}
		if($pp_name eq $in{'p_name'}){&error("パーティ名を変えてください。$back_form");}
		$g++;
	}
	$solv=$chara[18]+$chara[37]*100;
	push(@member_data,"$in{'p_name'}<>$chara[4]<>$solv<>1<>$in{'p_com'}<>$chara[0]<>\n");

	open(OUT,">allparty.cgi");
	print OUT @member_data;
	close(OUT);

	$chara[61]=$in{'p_name'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティを作ったぞ！」</font>
<br>
<form action="sakaba.cgi" >
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

#----------------#
#  情報買う　　  #
#----------------#
sub kanyu {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[0] eq "test"){
		&error("testキャラはパーティに加入できません。$back_form");
	}

	if ($chara[61]){&error("既にパーティに所属しています。$back_form");}
	elsif($in{'kanyu_id'} eq "") {&error("加入先を選択してください。$back_form");}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		foreach(@array){
			if($chara[0] eq $array[$i]){splice(@array,$i,1);$array[3]-=1;$hit=1;}
			if($hit){
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				$hit=0;
			}
			$i++;
		}
	}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $in{'kanyu_id'}){
			$pp_maxmem=3;
			$lock_file = "$lockfolder/$array[5].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$array[5].cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$array[5].lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);
			$ptlim=int($mem1[18]/1000)*50+100;
			if($mem1[70]==1){$pp_minlv=$mem1[18]-$ptlim;$pp_maxlv=$mem1[18]+$ptlim;}
			elsif($mem1[70]==2){$pp_minlv=$mem1[18]-20000;$pp_maxlv=$mem1[18]+20000;}
			else{$pp_minlv=$mem1[18]+$mem1[37]*100-300;$pp_maxlv=$mem1[18]+$mem1[37]*100+300;}
			if($pp_minlv<1){$pp_minlv=1;}
			if($array[3] >= $pp_maxmem){&error("そのパーティは満員です。$back_form");}
			if($chara[70]<1){$solv=$chara[18]+$chara[37]*100;}
			elsif($chara[70]<2){$solv=$chara[18];}
			else{$solv=0;}
			if($solv < $pp_minlv or $solv > $pp_maxlv){
				if($solv!=0 and $chara[0] ne "jupiter"){&error("制限下です。$back_form");}
			}
			$lock_file = "$lockfolder/$array[5].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$array[5].cgi");
			$member1_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$array[5].lock";
			&unlock($lock_file,'DR');
			@mem1 = split(/<>/,$member1_data);
			if($mem1[70]==1 and $chara[70]<1){&error("加入は限界突破者のみです。$back_form");}
			if($mem1[70]<1 and $chara[70]==1){&error("限界突破前の人とは組めません。$back_form");}
			$array[3]+=1;
			$new_array = '';
			$new_array = join('<>',@array);
			$new_array =~ s/\n//;
			$new_array .= "$chara[0]<>\n";
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}


	$chara[61]=$in{'kanyu_id'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティに加入したぞ！<br>
」</font>
<br>
<form action="sakaba.cgi" >
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

#----------------#
#  情報買う　　  #
#----------------#
sub dattai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[1] eq $chara[4] and $array[6]!=""){
			$lock_file = "$lockfolder/$array[6].lock";
			&lock($lock_file,'DR');
			open(IN,"./charalog/$array[6].cgi");
			$member2_data = <IN>;
			close(IN);
			$lock_file = "$lockfolder/$array[6].lock";
			&unlock($lock_file,'DR');
			@mem2 = split(/<>/,$member2_data);
			$array[1]=$mem2[4];
			$solv=$mem2[18]+$mem2[37]*100;
			$array[2]=$solv;
			$array[3]-=1;
			splice(@array,5,1);
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			$chara[61]="";
			$hit=1;
			last;
		}elsif($array[1] eq $chara[4]){
			splice(@member_data,$i,1);
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			$chara[61]="";
			$hit=1;
			last;
		}
		$i++;
	}

	$phit=0;
	if($chara[61] and $hit!=1){
		open(IN,"allparty.cgi");
		@member_data = <IN>;
		close(IN);
		$i=0;$hit=0;
		foreach(@member_data){
			@array = split(/<>/);
			if($array[0] eq $chara[61]){$hit=1;last;}
			$i++;
		}
		if($hit){
			$g=0;
			foreach(@array){
				if($_ eq "" or $_ eq $chara[0]){splice(@array,$g,1);}
				$g++;
			}
			$memmem=@array;
			$array[3]=$memmem - 6;
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
		}
		$chara[61]="";
	}elsif($hit!=1){&error("パーティに入ってません。$back_form");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティ脱退したぞ！<br>
」</font>
<br>
<form action="sakaba.cgi" >
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

#----------------#
#  情報買う　　  #
#----------------#
sub henko {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if (length($in{'p_com'}) > 60) {
		&error("コメントが長すぎます。$back_form");
	}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[61]){
			$pp_maxmem=3;
			if($in{'p_com'}){$array[4] = $in{'p_com'};}
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allparty.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティ情報変更したぞ！<br>
」</font>
<br>
<form action="sakaba.cgi" >
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

#----------------#
#  情報買う　　  #
#----------------#
sub kaisan {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[61]){
			if($array[5] eq $chara[0] and $array[6]!=""){
				$lock_file = "$lockfolder/$array[6].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[6].cgi");
				$member2_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[6].lock";
				&unlock($lock_file,'DR');
				@mem2 = split(/<>/,$member2_data);
				$array[1]=$mem2[4];
				$solv=$mem2[18]+$mem2[37]*100;
				$array[2]=$solv;
				$array[3]-=1;
				splice(@array,5,1);
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}elsif($array[5] eq $chara[0]){
				splice(@member_data,$i,1);
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}

	$chara[61]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティを脱退したぞ！<br>
」</font>
<br>
<form action="sakaba.cgi" >
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
#----------------#
#  情報買う　　  #
#----------------#
sub keru {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[61]){
			$pp_maxmem=3;
			for($p=5;$p<=@array;$p++){
				$lock_file = "$lockfolder/$array[$p].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[$p].cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[$p].lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				if($mem1[4] eq $in{'keri'}){splice(@array,$p,1);$hit=1;last;}
			}
			if($hit){
				$array[3]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allparty.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
		}
		$i++;
	}
	if(!$hit){&error("そんなキャラ見つかりません$back_form");}
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「パーティ情報変更したぞ！<br>
」</font>
<br>
<form action="sakaba.cgi" >
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

#----------------#
#  情報買う　　  #
#----------------#
sub hyouji {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'hyouji_id'} eq "") {&error("パーティを選択してください。$back_form");}

	open(IN,"allparty.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($p_name,$pp_leader) = split(/<>/);
		@pre = split(/<>/,$_,6);
		@battle_mem = split(/<>/,$pre[5]);
		if($p_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bpb=0;$bpb<=$battle_mem_num;$bpb++){
				$lock_file = "$lockfolder/$battle_mem[$bpb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bpb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bpb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				if($chara[70]!=1){$sou=$mem[18]+$mem[37]*100;}
				else{$sou=$mem[18];}
				if($mem[4]){
					if($mem[70]<1){
						$ct.= "<tr><td>$mem[4]</td><td>$sou</td><td>$mem[61]</td></tr>";
					}elsif($mem[70]<2){
$ct.= "<tr><td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td><td>$mem[61]</td></tr>";
					}else{
$ct.= "<tr><td><font color=\"red\">$mem[4]</font></td><td>$sou</td><td>$mem[61]</td></tr>";
					}
				}
			}
			last;
		}
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";

<B></B><p>
<table border=1>
<th>名前</th><th>レベル</th><th>バグチェック用</th>
$ct<p>
</table>
<br>
<form action="sakaba.cgi" >
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