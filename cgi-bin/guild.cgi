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
<form action="guild.cgi" >
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

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);

	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_leader eq $chara[4]){last;}
	}

	open(OUT,">guildlog/$mon$mday.cgi");
	print OUT @member_data;
	close(OUT);

	print <<"EOM";
<h1>ギルド紹介所</h1>
<hr size=0>
<FONT SIZE=3>
<B>マスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
ギルドを結成する時は、8文字以内でギルド名、30字以内でコメントを設定してな。<br>
制限、に設定する値は、転生職回数×１００＋レベルだ。それを越えていない者は入れない。<br>
注：結成には、クエスト第一弾最終討伐を終えている必要があります。<br>
安全のため、解散する前に、メンバーに脱退してもらうようにしてください。<br>
ギルド名を変える時は、メンバーの方に入りなおしてもらうことになるかもしれません。」
</FONT>
<hr size=0>
EOM
if($chara[66] and $gg_leader eq $chara[4]){
	print <<"EOM";
<table>
<tr>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=henko>
コメント　：<input type="text" name="g_com" value="" size=40><br>
制限　　：<input type="text" name="g_sei" value="" size=10><br>
<br>　　
<input type=submit class=btn value="ギルド情報変更">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=memnin>
<br>　　
<input type=submit class=btn value="メンバー人数調整">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kaisan>
<br>　　
<input type=submit class=btn value="解散">
</form>
</td>
</tr>
<tr>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=keru>
対象名：<input type="text" name="keri" value="" size=10><br>
<br>　　
<input type=submit class=btn value="メンバーの強制脱退">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=master>
対象名：<input type="text" name="master" value="" size=10><br>
<br>　　
<input type=submit class=btn value="マスター権の移譲">
</form>
</td>
<td>
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=toppa>
突破者制限
<input type="radio" name="toppa" value="0" size=10>OFF
<input type="radio" name="toppa" value="1" size=10>ON<br>
<br>　　
<input type=submit class=btn value="突破者を募集する">
</form>
</td>
</tr>
</table>
EOM
}else{
	print <<"EOM";
<form action="guild.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=make>
ギルド名：<input type="text" name="g_name" value="" size=40><br>
コメント　：<input type="text" name="g_com" value="" size=40><br>
制限　　：<input type="text" name="g_sei" value="" size=10><br>
<br>　　
<input type=submit class=btn value="ギルド結成">(10億Ｇ)
</form>
<form action="guild.cgi" >
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
<th colspan="3">ギルド名</th><th>リーダー</th><th>ギルドレベル</th><th>メンバー数</th><th>制限</th><th>突破制限</th><th>コメント</th></tr><tr>
EOM
	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$gd=0;
	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_mem){
			$topp = "無";
			open(IN,"allguild2.cgi");
			@member_data2 = <IN>;
			close(IN);
			foreach(@member_data2){
				($gne,$gto) = split(/<>/);
				if($gg_name eq $gne){if($gto==1){$topp = "有";}last;}
			}
			$gg_maxmem=$gg_lv + 4;
			print <<"EOM";
			<tr>
			<td>
			<form action="./guild.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=kanyu>
			<input type=hidden name=kanyu_id value=$gg_name>
			<input type=submit class=btn value="加入">
			</form>
			</td>
			<td>
			<form action="./guild.cgi" >
			<input type=hidden name=id value="$chara[0]">
			<input type=hidden name=mydata value="$chara_log">
			<input type=hidden name=mode value=hyouji>
			<input type=hidden name=hyouji_id value=$gg_name>
			<input type=submit class=btn value="メンバー">
			</form>
			</td>
			<td align=center>$gg_name</td>
			<td align=center>$gg_leader</td>
			<td align=center>$gg_lv</td>
			<td align=center>$gg_mem\/$gg_maxmem</td>
			<td align=center>$gg_sei</td>
			<td>$topp</td>
			<td>$gg_com</td></tr>
EOM
		}
		$gd++;
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
		&error("testキャラはギルドを作成できません。$back_form");
	}
	if($chara[127]!=2){
		&error("クエスト第一弾最終討伐を終えていないためギルドを作れません。$back_form");
	}
	if ($chara[66]){&error("既にギルドに所属しています。$back_form");}
	else{
		if ($in{'g_name'} eq "") {
			&error("ギルド名が入力されていません。$back_form");
		}
		if (length($in{'g_name'}) > 16) {
			&error("ギルド名が長すぎます。$back_form");
		}
		if (length($in{'g_com'}) > 60) {
			&error("コメントが長すぎます。$back_form");
		}
		if ($in{'g_sei'} =~ m/[^0-9]/){
			&error("制限レベルに数字以外の文字が含まれています。$back_form"); 
		}
	}
	if($chara[19]<1000000000){
		&error("お金が足りません");
	}else{
		$chara[19]-=1000000000;
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;

	foreach(@member_data){
		($gg_name,$gg_leader,$gg_exp,$gg_lv,$gg_mem,$gg_sei,$gg_com) = split(/<>/);
		if($gg_name eq $in{'g_name'}){&error("ギルド名を変えてください。$back_form");}
	}

	push(@member_data,"$in{'g_name'}<>$chara[4]<>0<>1<>1<>$in{'g_sei'}<>$in{'g_com'}<>$chara[0]<>\n");

	open(OUT,">allguild.cgi");
	print OUT @member_data;
	close(OUT);

	$chara[66]=$in{'g_name'};

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「ギルドを作ったぞ！」</font>
<br>
<form action="guild.cgi" >
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
		&error("testキャラはギルドに加入できません。$back_form");
	}
	$gutime=time();
	$gutime=int($gutime/3600) - 12;
	if($chara[68] > $gutime){
		&error("前回ギルドに加入してからの時間が短すぎます。$chara[68] / $gutime $back_form");
	};

	if ($chara[66]){&error("既にギルドに所属しています。$back_form");}
	elsif($in{'kanyu_id'} eq "") {&error("加入先を選択してください。$back_form");}

	open(IN,"allguild2.cgi");
	@member_data2 = <IN>;
	close(IN);
	$hit=0;
	foreach(@member_data2){
		@array2 = split(/<>/);
		if($array2[0] eq $in{'kanyu_id'}){$hit=1;last;}
	}
	
	if ($hit == 1 and $chara[70]<1 and $array2[1]==1){&error("突破者のみが入れるよう制限されています。$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $in{'kanyu_id'}){
			$gg_maxmem=$array[3] + 4;
			if($array[4] >= $gg_maxmem){&error("そのギルドは満員です。$back_form");}
			if(!$chara[37] or $chara[70]==1){if($chara[18] < $array[5]){&error("制限下です。$back_form");}}
			elsif($chara[18] + $chara[37] * 100 < $array[5]){&error("制限下です。$back_form");}
			$array[4]+=1;
			$new_array = '';
			$new_array = join('<>',@array);
			$new_array =~ s/\n//;
			$new_array .= "$chara[0]<>\n";
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}


	$chara[66]=$in{'kanyu_id'};

	$gutime=time();
	$gutime=int($gutime/3600);
	$chara[68]=$gutime;
	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「ギルドに加入したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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

	if($chara[66]){

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=0;$g<$gg_maxmem+10;$g++){
				if($array[$g] eq $chara[0]){splice(@array,$g,1);$hit=1;last;}
			}
			if($hit){
				$array[4]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$new_array =~ s/\n//;
				$new_array .= "<>\n";
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
				print OUT @member_data;
				close(OUT);
				last;
			}
			#if(!$hit){&error("脱退失敗 $back_form");}
		}
		$i++;
	}

	$chara[66]="";

	}else{&error("ギルドに入ってません。$back_form");}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「ギルド脱退したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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

	if (length($in{'g_com'}) > 60) {
		&error("コメントが長すぎます。$back_form");
	}
	if ($in{'g_sei'} =~ m/[^0-9]/){
		&error("制限レベルに数字以外の文字が含まれています。$back_form"); 
	}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			if($in{'g_sei'}){$array[5] = $in{'g_sei'};}
			if($in{'g_com'}){$array[6] = $in{'g_com'};}
			$new_array = '';
			$new_array = join('<>',@array);
			$member_data[$i]=$new_array;
			open(OUT,">allguild.cgi");
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
「ギルド情報変更したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$member_data[$i]="";
			open(OUT,">allguild.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$i++;
	}

	$chara[66]="";

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「ギルド情報変更したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=8;$g<=@array;$g++){
				$lock_file = "$lockfolder/$array[$g].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[$g].cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[$g].lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				if($mem1[4] eq $in{'keri'}){splice(@array,$g,1);$hit=1;last;}
			}
			if($hit){
				$array[4]-=1;
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
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
「ギルド情報変更したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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

	$ima = time();

	if($in{'hyouji_id'} eq "") {&error("ギルドを選択してください。$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				if($mem[70]<1){$sou=$mem[18]+$mem[37]*100;}
				else{$sou=$mem[18];}
				$rdate = $mem[27];
				$niti = $ima - $rdate;
				if(int($niti / (60*60*24))==0){
					$niti=int($niti / (60*60));
					$kniti="$niti時間前";
				}else{
					$niti = int($niti / (60*60*24));
					$kniti="$niti日前";
				}
				if($mem[4]){
					if($mem[70]<1){
						$ct.= "<tr><td>$mem[4]</td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
					}elsif($mem[70]<2){
$ct.= "<tr><td><font color=\"yellow\">$mem[4]</font></td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
					}else{
$ct.= "<tr><td><font color=\"red\">$mem[4]</font></td><td>$sou</td><td>$mem[66]</td><td>$kniti</td></tr>";
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
<th>名前</th><th>レベル</th><th>バグチェック用</th><th>最後のログイン</th>
$ct<p>
</table>
<br>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvsort">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="レベル順に並び替え">
</form>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="戻る">
</form>
<hr size=0>
EOM
if($chara[0] eq "jupiter"){
	print <<"EOM";
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="jogai">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="バグってる人除外">
</form>
EOM
}

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub memnin {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$i=0;
	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){$hit=1;last;}
		$i++;
	}
	if($hit){
		$g=0;
		foreach(@array){
			if(!$_ and $g>6){splice(@array,$g,1);}
			$g++;
		}
		$memmem=@array;
		$array[4]=$memmem - 8;
		$new_array = '';
		$new_array = join('<>',@array);
		$member_data[$i]=$new_array;
		open(OUT,">allguild.cgi");
		print OUT @member_data;
		close(OUT);
	}

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「メンバーの人数を調整したぞ。」</font>
<br>
<form action="guild.cgi" >
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
sub master {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if(!$in{'master'}){&error("ちゃんと入力してください");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$gg_maxmem=$array[3] + 4;
			for($g=8;$g<=@array;$g++){
				$lock_file = "$lockfolder/$array[$g].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$array[$g].cgi");
				$member1_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$array[$g].lock";
				&unlock($lock_file,'DR');
				@mem1 = split(/<>/,$member1_data);
				if($mem1[4] eq $in{'master'}){
					$array[1]=$mem1[4];
					$array[7]=$mem1[0];
					$array[$g]=$chara[0];
					$hit=1;
					last;
				}
			}
			if($hit){
				$new_array = '';
				$new_array = join('<>',@array);
				$member_data[$i]=$new_array;
				open(OUT,">allguild.cgi");
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
「ギルド情報変更したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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
sub toppa {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"allguild2.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$hit=0;

	foreach(@member_data){
		@array = split(/<>/);
		if($array[0] eq $chara[66]){
			$member_data[$i]="$chara[66]<>$in{'toppa'}<>\n";
			$hit=1;
			last;
		}
		$i++;
	}
	if(!$hit){
		push(@member_data,"$chara[66]<>$in{'toppa'}<>\n");
	}
	open(OUT,">allguild2.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>マスター</B><BR>
「ギルド情報変更したぞ！<br>
」</font>
<br>
<form action="guild.cgi" >
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
sub lvsort {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	$ima = time();

	if($in{'hyouji_id'} eq "") {&error("ギルドを選択してください。$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";
	foreach(@member_data){
		s/\n//i;
		s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			$a=0;$b=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				$rdate = $mem[27];
				$niti = $ima - $rdate;
				if(int($niti / (60*60*24))==0){
					$niti=int($niti / (60*60));
					$kniti="$niti時間前";
				}else{
					$niti = int($niti / (60*60*24));
					$kniti="$niti日前";
				}
				if($mem[70]<1){
					$sou=$mem[18]+$mem[37]*100;
					$tmaename[$a]=$mem[4];
					$tmaelv[$a]=$sou;
					$tmaeniti[$a]=$kniti;
					$tmaeguild[$a]=$mem[66];
					$a++;
				}else{
					$sou=$mem[18];
					$tgoname[$b]=$mem[4];
					$tgolv[$b]=$sou;
					$tgoniti[$b]=$kniti;
					$tgoguild[$b]=$mem[66];
					$b++;
				}
			}
			@gosort = sort { $b <=> $a } @tgolv;
			@maesort = sort { $b <=> $a } @tmaelv;
			for($aa=0;$aa<$b;$aa++){
				if($gosort[$aa]){
					$t=0;$cc=$aa-1;
					foreach(@tgolv){
						if($aa==0 and $_ == $gosort[$aa]){last;}
						elsif($_ == $gosort[$aa] and $gonamesort[$cc] ne $tgoname[$t]){last;}
						$t++;
					}
					$gonamesort[$aa]=$tgoname[$t];
$ct.= "<tr><td><font color=\"yellow\">$gonamesort[$aa]</font></td><td>$tgolv[$t]</td><td>$tgoguild[$t]</td><td>$tgoniti[$t]</td></tr>";
				}
			}
			for($bb=0;$bb<$a;$bb++){
				if($maesort[$bb]){
					$t=0;$dd=$bb-1;
					foreach(@tmaelv){
						if($bb==0 and $_ == $maesort[$bb]){last;}
						elsif($_ == $maesort[$bb] and $maenamesort[$dd] ne $tmaename[$t]){last;}
						$t++;
					}
					$maenamesort[$bb]=$tmaename[$t];
$ct.= "<tr><td>$maenamesort[$bb]</font></td><td>$tmaelv[$t]</td><td>$tmaeguild[$t]</td><td>$tmaeniti[$t]</td></tr>";
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
<th>名前</th><th>レベル</th><th>バグチェック用</th><th>最後のログイン</th>
$ct<p>
</table>
<br>
EOM
	print <<"EOM";
<form action="guild.cgi" >
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

sub jogai {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'ST');

	&chara_load;

	&chara_check;

	&get_host;

	if($in{'hyouji_id'} eq "") {&error("ギルドを選択してください。$back_form");}

	open(IN,"allguild.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$ct="";$t=0;
	foreach(@member_data){
		#s/\n//i;
		#s/\r//i;
		($g_name,$gg_leader) = split(/<>/);
		@pre = split(/<>/,$_,8);
		@battle_mem = split(/<>/,$pre[7]);
		if($g_name eq $in{hyouji_id}){
			$battle_mem_num = @battle_mem;
			$ht=0;
			for($bgb=0;$bgb<=$battle_mem_num;$bgb++){
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&lock($lock_file,'DR');
				open(IN,"./charalog/$battle_mem[$bgb].cgi");
				$mem_data = <IN>;
				close(IN);
				$lock_file = "$lockfolder/$battle_mem[$bgb].lock";
				&unlock($lock_file,'DR');
				@mem = split(/<>/,$mem_data);
				if($mem[66] ne $g_name){
					splice(@battle_mem,$bgb,1);
					#$bgb-=1;
				}
			}
			last;
		}
		$t++;
	}
	$member_data[$t] = "$pre[0]<>$pre[1]<>$pre[2]<>$pre[3]<>$pre[4]<>$pre[5]<>$pre[6]<>";
	$i=0;
	while($battle_mem[$i]){
		$member_data[$t].="$battle_mem[$i]<>";
		$i++;
	}
	$member_data[$t].="\n";

	open(OUT,">allguild.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'ST');
	
	&header;

	print <<"EOM";

<B></B><p>
<br>
<form action="guild.cgi" >
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type="hidden" name="mode" value="lvsort">
<input type=hidden name=hyouji_id value=$in{'hyouji_id'}>
<input type=submit class=btn value="レベル順に並び替え">
</form>
<form action="guild.cgi" >
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
