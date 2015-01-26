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
<form action="home.cgi" method="post">
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

	print <<"EOM";
<h1>なんだかわからない基地</h1>
<hr size=0>
<FONT SIZE=3>
<B>基地の番人</B><BR>
「ん？、おまえは誰だ！？<br>
ここは立ち入り禁止だ、帰れ帰れッ！！」<br>
</FONT>
<hr size=0>
EOM
if($chara[0] eq "jupiter"){
	print "<table><tr><th>名前</th>";
	open(IN,"sozai.cgi");
	@sozai_data = <IN>;
	close(IN);
	$i=0;
	foreach (@sozai_data){
		($name)=split(/<>/);
		print "<th>$name</th>";
		$i++;
	}
	print "<th>合計</th></tr>";
	opendir (DIR,'./kako') or die "$!";
	foreach $entry (readdir(DIR)){
		if ($entry =~ /\.cgi/) {
			open(IN,"./kako/$entry");
			$WORK=<IN>;
			close(IN);
			@membe = split(/<>/,$WORK);
			open(IN,"./charalog/$entry");
			$fm=<IN>;
			close(IN);
			@fmm = split(/<>/,$fm);
			print "<tr><td>$fmm[4]</td>";
			$goukei=0;$g=0;
			foreach (@membe) {
				print "<td>$_</td>";
				$goukei+=$_;
				$g++;
			}
			while($g<$i){print "<td></td>";$g++;}
			print "<td>$goukei</td></tr>";
		}
	}
	closedir(DIR);
	print "</table>";
}
	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}