#!/usr/local/bin/perl

require "./chatini.cgi";

&main;
exit;

sub main{

	$hit=0;
	if($ENV{'REQUEST_METHOD'} eq "POST"){ read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});}
	else{$buffer=$ENV{'QUERY_STRING'};}
		if ($buffer > 6400) { &error("投稿量が大きすぎます"); }
	@pairs = split(/&/,$buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ s/\&/&amp;/g;
		$value =~ s/</&lt;/g;
		$value =~ s/>/&gt;/g;
		$value =~ s/"/&quot;/g;
		$value =~ s/\r|\n|\r\n| //g;
		$in{$name} = $value;
	}


	$tname = &trip($in{'name'});
	$addr = $ENV{'REMOTE_ADDR'};

$o= << "EOM";
Cache-Control: no-cache
Pragma: no-cache
Content-type: text/html

<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="content-style-type" content = "text/css">
<title>CrazeChat</title>

<STYLE type="text/css">
<!--
BODY{
color : #121232;
background-color : #ffe8c8;
font-size : 11pt;
}
small{
font-size : 9pt;
}
-->
</STYLE>
</head>
EOM

	$times = time;
	open(gues,"$guestfile");
	@gue=<gues>;
	close(gues);

$rom=0;

foreach $line (@gue) {
	my ($timer,$id,$name,$cch,$hos) = split(/<>/, $line);
	if($times-120 > $timer){$line = '';next;}


#ROM表示処理
	if(!$id){
		if(!$in{'id'} && ($hos eq $addr)){$line = "$times<><><><>$addr<>\n";$flug=1;}
		$rom++;next;
	}

	push (@sanka,"[$name]");

	if($name eq $in{'name'} || $id eq $in{'id'}){
		if($timer > $times){$in{'msg'}="";$times=$timer + 2;}
		if($in{'msg'}){$times += $checklimit;}

		$line = "$times<>$id<>$name<>$in{'nel'}<>$in{'host'}<>\n";
		$flug=1;$hit=1;
	}

}

if(!$flug && $in{'id'}){
	push (@sanka,"[$tname]");
	push (@gue,"$times<>$in{'id'}<>$tname<>$in{'nel'}<>$in{'host'}<>\n");
	$adding ++;
}elsif(!$flug && !$in{'id'}){
	$rom++;
	push (@gue,"$times<><><><>$addr<>\n");
	$adding ++;
}

if($in{'msg'} || $adding){
	open(gues,">$guestfile");
	print gues @gue;
	close(gues);
}


	open(cha,"$logfile");
	@ch=<cha>;
	close(cha);

# メッセージ書き込み
if($hit && $in{'msg'} ne '') {


	#強制hoge
	if($usehoge){
		open(ggs,"$limitfile");
		@ggg=<ggs>;
		close(ggs);

		$i=0;

		foreach (@ggg){
			my ($id) = split(/<>/);
			if($id eq $in{'id'} || $id eq $in{'host'}){$in{'nel'}="hoge";$in{'tid'}="";$i=35}
			}
	}


	$in{'msg'}=~ s/\///g;
	($sec,$min,$hour,$mday,$mon,$year,$wday) = localtime();
	unshift(@ch,"$in{'id'}<>$tname<>$in{'msg'} <small>[$hour:$min]</small><>$in{'tid'}<>$in{'nel'}<>$in{'host'}<>\n");
}


	$sanka=@sanka;
	$o.= "参加者 $sanka 人 ： @sanka ROM $rom人<br><br>";

#以下で宣伝とか可能

if($in{'msg'}) {
	$ch = @ch;
	if($ch>$limitlog){pop(@ch);}

	open(cha,">$logfile");
	print cha @ch;
	close(cha);
}

print "$o<br><center><small><a href=http://kroko.maxs.jp/~kroko/mt/ target=_blank>CrazeChat</a></small></center></body></html>";
}

#ホスト取得
sub get_host {
	$addr = $ENV{'REMOTE_ADDR'};

	if ($get_remotehost) {
		if ($host eq "" || $host eq "$addr") {
			$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2);
		}
	}
	if ($host eq "") { $host = $addr; }
}
#トリップ生成
sub trip{
	local $name = $_[0];

	$name =~ s/◆/◇/;

	if ($name =~ /(#|＃)(.*)/) {
		$string = crypt("$2", "H.");
		$tripstr = substr($string,2,8);
		$name =~ s/(#|＃)(.*)$/ ◆$tripstr/;
}
	return($name);
}
#ホスト変換
sub ango{
	local $id = $_[0];
		$id = crypt("$id", "$seed");
	return($id);
}

sub error{
$o.="$_[0]";
print $o;
exit;
}