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
<form action="uketorijyo.cgi" method="post">
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

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$g=0;
	foreach(@member_data){
		($name,$no,$kazu) = split(/<>/);
		if($name eq $chara[4]){$hit=1;last;}
		$g++;
	}
	if($hit==1 and $no==189){
		$suke="闇空間チケット";
	}elsif($hit==1 and $no==301){
		$suke="火の石";
	}elsif($hit==1 and $no==302){
		$suke="水の石";
	}
	print <<"EOM";
<h1>受取所</h1>
<hr size=0>
<FONT SIZE=3>
<B>受取所のマスター</B><BR>
「ん？、おまえ<B>$chara[4]</B>じゃないか。<br>
誰かから預かってるものがあったかな？」<br>
※ここでは、主にイベントで獲得したアイテムなどを受け取ることができます。<br>
</FONT>
<hr size=0>
EOM
if($hit==1){
	print <<"EOM";
$sukeを$kazu、預かっています。受け取りますか？
<form action="./uketorijyo.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
<input type=submit class=btn value="受け取る">
</form>
EOM
}else{
	print <<"EOM";
預かっているものはありません。<br>
(総預かり数：$g)
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
sub uketoru {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$hit=0;$g=0;
	foreach(@member_data){
		($name,$no,$kazu) = split(/<>/);
		if($name eq $chara[4]){
			$hit=1;
			splice(@member_data,$g,1);
			open(OUT,">uketori.cgi");
			print OUT @member_data;
			close(OUT);
			last;
		}
		$g++;
	}
	if($hit==1 and $no==189){
		$suke="闇空間チケット";
	}elsif($hit==1 and $no==301){
		$suke="火の石";
	}elsif($hit==1 and $no==302){
		$suke="水の石";
	}

	$chara[$no]+=$kazu;

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$sukeを$kazu個、受け取りました。<br>
</font>
<br>
<form action="uketorijyo.cgi" method="post">
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
sub uketoru2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	if($chara[301] == $chara[18] and $chara[302] == $chara[17]){&error("そのアイテムは既に受け取りました");}
	else{$chara[301]=$chara[18];$chara[302]=$chara[17];}

	open(IN,"uketori.cgi");
	@member_data = <IN>;
	close(IN);
	$i_no=$chara[4];
	$i_name=$in{'mono'};
	$i_dmg=1;
	push(@member_data,"$i_no<>$i_name<>$i_dmg<>\n");
	open(OUT,">uketori.cgi");
	print OUT @member_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	if($i_name==189){
		$suke="闇空間チケット";
	}elsif($i_name==301){
		$suke="火の石";
	}elsif($i_name==302){
		$suke="水の石";
	}
	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
$sukeが受取所に届きました<br>
</font>
<br>
<form action="uketorijyo.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="受取所へ">
</form>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}