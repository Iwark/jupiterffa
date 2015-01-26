#!/usr/local/bin/perl

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

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
<form action="party.cgi" method="post">
<input type=hidden name=id value="$in{'id'}">
<input type="hidden" name="mydata" value="$in{'mydata'}">
<input type=submit class=btn value="戻る">
</form>
EOM

#ＩＰアドレスでアクセス制限
foreach (@shut_host) {
	$_ =~ s/\*/\.\*/g;
	if ($ENV{'REMOTE_ADDR'} =~ /$_/) {
		&error("アクセスできません！！");
	}
}

if($mode) { &$mode; }

&party;

exit;

#--------------------#
# パーティ表示　　　 #
#--------------------#
sub party {

	&chara_load;

	&chara_check;

	&header;

	$party_lvl=10;

	print <<"EOM";
<h1>酒場</h1>
※<font color=red>パーティの作成・加入はLvが$party_lvlにならないとできません。</font><br>
<hr size=0>
<table><tr>
<td rowspan="2" id=td2 class=b2 align="center">パーティ</td>
<td class=b1 align="right">
<form action="party.cgi" method="POST">
パーティ名：<input type="text" name="p_name" value="" size=40><br>
コメント：<input type="text" name="f_name" value="" size=40>
<td class=b1 width=80 align="center"><br><br>
EOM
	if ($chara[61] eq "" and $chara[18] > $party_lvl){
print <<"EOM";
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=sakusei>
<input type="submit" class="btn" value="作成">
EOM
	}else{
		print"作成\n";
	}
print <<"EOM";
</form>
</td>
<form action="guild.cgi" method="POST">
<td class=b1 width=80 align="center"><br><br>
EOM
	if ($chara[61] eq ""){
		print"脱退\n";
	}else{
print <<"EOM";
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=datai>
<input type="submit" class="btn" value="脱退">
EOM
	}
print <<"EOM";
</form>
</td></tr><tr>
<form action="guild.cgi" method="POST">
<td class=b1 align="right">
コメント：<input type="text" name="g_apiru" value="" size=40>
<td colspan=2 class=b1 width=160 align="center">
EOM
	if ($chara[0] eq $chara[130]){
print <<"EOM";
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=kousin>
<input type="submit" class="btn" value="更新">
EOM
	}else{
		print"更新\n";
	}
print <<"EOM";
</tr><tr>
<td id=td2 class=b2 align="center">パーティ加入</td>
<td class=b1 align="right">
<form action="guild.cgi" method="POST">
コメント：<input type="text" name="kome_name" value="" size=40>
<td class=b1 align="center" colspan="2"><br><br>
EOM
	if ($chara[46] eq ""){
		print"登録\n";
	}elsif($chara[135] eq 1){
		print"登録完了\n";
	}elsif($chara[135] eq ""){
print <<"EOM";
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=gran>
<input type="submit" class="btn" value="登録">
EOM
	}
print <<"EOM";
</form>
</td>
</tr><tr>
</td></tr></table>
</form>
<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

#------#
# 作成 #
#------#
sub sakusei {

	&chara_load;

	&chara_check;

	if($in{'id'} eq test){
		&error("testキャラはパーティを作成できません。$back_form");
	}

	if ($chara[46] eq ""){
		if ($in{'p_name'} eq "") {
			&error("パーティ名が入力されていません。$back_form");
		}
		if (length($in{'p_name'}) > 50) {
			&error("パーティ名が長すぎます。$back_form");
		}
		if ($in{'f_name'} =~ m/[^0-9a-zA-Z]/){
			&error("ファイル名に半角英数字以外の文字が含まれています。$back_form"); 
		}
		open(IN,"$all_data_file");
		@all_data = <IN>;
		close(IN);
		foreach (@all_data) {
			@all_chara = split(/<>/);
			if ($all_chara[46] eq $in{'f_name'} or $all_chara[121] eq $in{'g_name'}) {
				close(IN);
				&error("同一名のギルド名・ファイル名があります。$back_form");
			}
		}
		$chara[46] = $in{'f_name'};
		$chara[130] = $chara[0];
		$chara[121] = $in{'g_name'};
		$chara[123] = $chara[4];
		$chara[124] = "[";
		$chara[125] = "]";
		$chara[135] = 1;
		$chara[4] = $chara[4].$chara[124].$chara[121].$chara[125];

		open(IN,"$g_message_file/member/$chara[46].cgi");
		@member_data = <IN>;
		close(IN);

		push(@member_data,"$chara[0]<>$chara[4]<>$chara[18]<>$chara[2]<>$chara[3]<>　<>$chara[14]<>$chara[127]<>\n");
	
		open(OUT,">$g_message_file/member/$chara[46].cgi");
		print OUT @member_data;
		close(OUT);

		open(IN,"$g_message_file/data/guildmember.cgi");
		@data_data = <IN>;
		close(IN);

		push(@data_data,"$chara[0]<>$chara[4]<>$chara[121]<>　<>\n");
	
		open(OUT,">$g_message_file/data/guildmember.cgi");
		print OUT @data_data;
		close(OUT);

		open(IN,"$g_message_file/log/$chara[46].cgi");
		@log_data = <IN>;
		close(IN);

		push(@log_data,"0<>0<>\n");

		open(OUT,">$g_message_file/log/$chara[46].cgi");
		print OUT @log_data;
		close(OUT);
	}else{
		&error("パーティに加入しているので作成はできません。$back_form");
	}

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&all_message("$chara[4]さんがパーティ「$chara[121]」を作成しました。");

	&header;

	print <<"EOM";
<h1>パーティ「$in{'p_name'}」を作成しました。</h1>
<hr size=0>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

#------#
# 脱退 #
#------#
sub datai {

	&chara_load;

	&chara_check;

	if ($chara[46] eq ""){
		&error("パーティに加入していません。$back_form");
	}else{

	open(IN,"./guild/member/$chara[46].cgi");
	@member_data = <IN>;
	close(IN);

	$i = 0;
	foreach(@member_data){
		($ino,$iname,$ilv,$ihp,$iurl,$ikome,$syoku,$syokui) = split(/<>/);
	
	if ($chara[0] eq $ino){
		$member_data[$i] =~ s/\n//g;
		$member_data[$i] =~ s/\r//g;

		($ino,$iname,$ilv,$ihp,$iurl,$ikome) = split(/<>/,$member_data[$i]);

		$member_data[$i] = ();

	}
	$i++;
	}

	open(OUT,">./guild/member/$chara[46].cgi");
	print OUT @member_data;
	close(OUT);

	open(IN,"./guild/data/guildmember.cgi");
	@data_data = <IN>;
	close(IN);

	$i = 0;
	foreach(@data_data){
		($ino,$iname,$iguild,$iapiru) = split(/<>/);
	
	if ($chara[130] eq $ino){
		$data_data[$i] =~ s/\n//g;
		$data_data[$i] =~ s/\r//g;

		($ino,$iname,$iguild,$iapiru) = split(/<>/,$data_data[$i]);

		$data_data[$i] = ();

	}
	$i++;
	}

	open(OUT,">./guild/data/guildmember.cgi");
	print OUT @data_data;
	close(OUT);

	&g_message("$chara[4]さんが脱退しました。");

	$chara[46] = "";
	$chara[130] = "";
	$chara[127] = "";
	$chara[122] = $chara[121];
	$chara[121] = "";
	$chara[135] = "";
	$chara[4] = $chara[123];

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');
	}

	&header;

	print <<"EOM";
<h1>パーティ「$chara[122]」を脱退しました。</h1><hr size=0>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

#------#
# 加入 #
#------#
sub kanyu {

	&chara_load;

	&all_data_read;
	foreach(@RANKING) { 
	($aid,$apass,$asite,$aurl,$aname) = split(/<>/); 
	$aidn.= qq|\n<option value="$aid">$anameさんへ|; 
	}
 
	&chara_check;

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";

	<form action="./guild.cgi" method="post">
	<select name=si size=20>
	<option value="">加入\申\請するパーティを選択$aidn
	</select>さんへ
	<input type="hidden" name="id" value="$chara[0]">
	<input type="hidden" name="mydata" value="$chara_log">
	<input type=hidden name=mode value=kanyu2>
	<input type=submit class=btn value="加入\申\請">
	</form>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

sub kanyu2 {

	&chara_load;

	if($in{'si'} eq ""){
		&error("名前が選択されていません。$back_form");
	}

	if($in{'si'} eq test){
		&error("testキャラはパーティに加入できません。$back_form");
	}
	open(IN,"./charalog/$in{'si'}.cgi") || &error("相手が見つかりません$ENV{'CONTENT_LENGTH'}$back_form");
	$schara_log = <IN>;
	close(IN);

	@schara = split(/<>/,$schara_log);

	&chara_check;

	$lock_file = "$lockfolder/sm$in{'si'}.lock"; 
	&lock($lock_file,'MS');
	&unlock($lock_file,'MS'); 

	if ($schara[46] eq ""){

	}else{
		&error("$schara[4]さんはすでにパーティに加入しています。$back_form");
	}

	$schara[46] = $chara[46];
	$schara[121] = $chara[121];
	$schara[123] = $schara[4];
	$schara[124] = "[";
	$schara[125] = "]";
	$schara[135] = 1;
	$schara[4] = $schara[4].$schara[124].$schara[121].$schara[125];

	open(IN,"$g_message_file/member/$chara[46].cgi");
	@member_data = <IN>;
	close(IN);

	push(@member_data,"$schara[0]<>$schara[4]<>$schara[18]<>$schara[2]<>$schara[3]<>　<>$schara[14]<>$schara[127]<>\n");
	
	open(OUT,">$g_message_file/member/$chara[46].cgi");
	print OUT @member_data;
	close(OUT);

	$new_schara = '';

	$new_schara = join('<>',@schara);

	$new_schara .= '<>';

	open(OUT,">./charalog/$in{'si'}.cgi");
	print OUT $new_schara;
	close(OUT);

	&chara_regist;

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&g_message("$schara[4]さんが加入しました。");

	&header;

	print <<"EOM";
<h1>$schara[4]さんがパーティ「$schara[121]」に加入しました。</h1><hr size=0>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

#--------------#
# ギルド一覧表 #
#--------------#
sub guild_itiran {

	&chara_load;

	&chara_check;

	open(IN,"./guild/data/guildmember.cgi");
	@data_data = <IN>;
	close(IN);

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print << "EOM";
<table>
<tr>
<td id="td1" align="center" class="b2">ギルドマスター</td>
<td id="td1" align="center" class="b2">ギルド</td>
<td id="td1" align="center" class="b2">アピール</td></tr>
EOM
	$i = 0;
	foreach(@data_data){
		($ino,$iname,$iguild,$iapiru) = split(/<>/);
	print << "EOM";
<tr><td align=left class=b1 nowrap><a href="./system.cgi?mode=chara_sts&id=$ino">$iname</a></td>
<td align=left align=right class=b1>$iguild</td>
<td align=left class=b1>$iapiru　</td>
</tr>
EOM
	$i++;
	}
	print << "EOM";
</td>
</table>
<hr size=0>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}

sub kousin {

	&chara_load;

	&chara_check;

	if ($in{'g_apiru'} eq "") {
		&error("アピールが入力されていません。$back_form");
	}
	if (length($in{'g_apiru'}) > 50) {
		&error("アピールが長すぎます。$back_form");
	}

	open(IN,"./guild/data/guildmember.cgi");
	@data_data = <IN>;
	close(IN);

	$i = 0;
	foreach(@data_data){
		($ino,$iname,$iguild,$iapiru) = split(/<>/);
	
	if ($chara[0] eq $ino){
		$data_data[$i] =~ s/\n//g;
		$data_data[$i] =~ s/\r//g;

		($ino,$iname,$iguild,$iapiru) = split(/<>/,$data_data[$i]);

		$data_data[$i] = ();

	}
	$i++;
	}

	open(OUT,">./guild/data/guildmember.cgi");
	print OUT @data_data;
	close(OUT);

	open(IN,"$g_message_file/data/guildmember.cgi");
	@data_data = <IN>;
	close(IN);

	push(@data_data,"$chara[0]<>$chara[4]<>$chara[121]<>$in{'g_apiru'}<>\n");
	
	open(OUT,">$g_message_file/data/guildmember.cgi");
	print OUT @data_data;
	close(OUT);

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<h1>更新しました。</h1><hr size=0>

<form action="$script" method="post">
<input type=hidden name=mode value=log_in>
<input type=hidden name=id value=$chara[0]>
<input type="hidden" name="mydata" value="$chara_log">
<input type=submit class=btn value="ステータス画面へ">
</form>

EOM

	&footer;

	exit;
}
