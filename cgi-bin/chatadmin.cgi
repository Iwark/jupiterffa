#!/usr/local/bin/perl

require "chatini.cgi";

	if($ENV{'REQUEST_METHOD'} eq "POST"){ read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});}
	else{$buffer=$ENV{'QUERY_STRING'};}
	@pairs = split(/&/,$buffer);
	foreach $pair (@pairs) {
		($name, $value) = split(/=/, $pair);
		$value =~ tr/+/ /;
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$in{$name} = $value;
	}

#html�\��
$o= << "EOM";
Cache-Control: no-cache
Pragma: no-cache
Content-type: text/html

<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=Shift_JIS">
<META http-equiv="content-style-type" content = "text/css">
<title>�`���b�g</title>
<STYLE type="text/css">
<!--
BODY{
color : #121232;
background-color : #ffe8c8;
font-size : 11pt;
}
td{
color : #121232;
line-height : 11pt;
font-size : 9pt;
}
-->
</STYLE>
</head>
EOM


$data = time();

#�Ǘ��҃t�@�C���ǂݍ���
open(kanri,"./chatkanri.cgi");
@kanri=<kanri>;
close(kanri);

$adhit=0;
foreach $line (@kanri){
($adid,$adlv,$adpass,$adetc2) = split(/<>/,$line);
if($adid eq $in{'adid'} && $adpass eq $in{'pass'}){$adhit=1;last;}
}

#�f�[�^�ǂݍ���
@ch=();
open(cha,"$logfile");
@ch=<cha>;
close(cha);


#�u�����[�h
if($in{'mode'} eq 'kakuri' && ($adhit)){

##�����擾
	foreach $line(@ch){
		($id,$name,$msg,$tid,$nel,$ip) = split(/<>/, $line);
			$ms = substr($msg,0,4);
			if($in{'id'} eq $id && $ms eq $in{'ms'}){$mmm=$msg;last;}
	}
	
	if($in{'ip'} && $adlv > 1){$in{'id'}=$in{'ip'};}
	
	open(gues,"$limitfile");
	@gue=<gues>;
	close(gues);

	foreach $line (@gue){
		my ($gid,$gtime,$gadid,$etc) = split(/<>/,$line);
		if($gid eq $in{'id'}){$hit=1;}
	}

		if(!$hit){
			push(@gue,"$in{'id'}<>$data<>$in{'adid'}<>$mmm<>\n");

			open(gues,">$limitfile");
			print gues @gue;
			close(gues);
		}
}

#�������[�h
if(($in{'mode'} eq 'hukatu') && ($adhit) && ($adlv > 4)){
	open(gues,"$limitfile");
	@gue=<gues>;
	close(gues);

	foreach (@gue){
		my ($gid,$gtime,$gadid,$etc) = split(/<>/);
		if($gid ne $in{'id'} && $gid){push(@ngue,"$gid<>$gtime<>$gadid<>$etc<>\n");}
	}

	open(gues,">$limitfile");
	print gues @ngue;
	close(gues);
}



if(!$adhit){
	$o.="<br><br><br><br><br><br><center>

	<form action=./chatadmin.cgi>
	�Ǘ�ID<input type=text size=8 name=adid >
	�Ǘ�PASS<input type=text size=8 name=pass >
	<input type=submit name=submit value=OK>
	</form>
	</center>";
print "$o</body></html>";
exit;
}


#���C���\��
$o.="�u�����I<table>";

	foreach $line (@ch) {
		($id,$name,$msg,$tid,$nel,$ip) = split(/<>/, $line);
			if($in{'nel'} && $in{'nel'} ne $nel){next;}
			$ms=substr($msg,0,4);$ms.=" ";
			if($tid){$msg="$msg<b>(�d��)</b>"}
		
		$o.="<tr>
		<td>�� <b>$name</b></td>";
		if($adlv > 3){$o.="<td>$msg</td>";}
		if($adlv > 2){$o.="<td><a href=\"./chatadmin.cgi?mode=nel&nel=$nel&adid=$in{'adid'}&pass=$in{'pass'}\">$nel</a></td>";}
		if($adlv > 0){$o.="<td><a href=\"./chatadmin.cgi?mode=kakuri&id=$id&adid=$in{'adid'}&pass=$in{'pass'}&ms=$ms\">$id</a></td></tr>";}
	}

	$o.="</table><br>";

		if($adlv > 4){$o.="</hr>����<table><tr><td>ID or IP<td>�u�����̔���<td>�u������(�b)<td>�u�������Ǘ���ID";

		open(gues,"$limitfile");
		@gue=<gues>;
		close(gues);

		foreach (@gue) {
			my ($id,$time,$adid,$etc) = split(/<>/);
			$time = $data - $time;
			$o.="<tr><td><a href=\"./chatadmin.cgi?mode=hukatu&id=$id&adid=$in{'adid'}&pass=$in{'pass'}\">$id</a><td>$etc<td>$time<td>$adid<br>";
		}

		$o.="</table>";
		}

	print "$o</body></html>";

