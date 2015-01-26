#!/usr/local/bin/perl

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
<form action="quest.cgi" method="post">
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

&quest_view;

exit;

#----------------#
#  クエスト表示  #
#----------------#
sub quest_view {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>討伐クエスト</h1>
<hr size=0>

<FONT SIZE=3>
<B>張り紙</B><BR>
「凶悪なモンスターを倒してくれる冒険者を募集しています。<br>
一度に受けられるクエストは３つまで、上から順番に受けてください。」
EOM
if($chara[135]==7){
	print <<"EOM";
<form action="quest.cgi" >
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$chara_log">
<input type="hidden" name="mode" value="special">
<input type=submit class=btn value="特別クエストへ"></td>
</form>
EOM
}
	print <<"EOM";
</FONT>
<br><br>
討伐クエスト第一弾
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy>
<table>
<tr>
<th>No.</th><th>対象</th><th>報酬</th><th>進行状態</th></tr>
EOM
	open(IN,"inquest.cgi");
	@quest_item = <IN>;
	close(IN);

	foreach(@quest_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 100;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp経験値";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>未</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>進行中</th></tr>";
		}
		else{
			print "<th>完了</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno>
<option value="no">選択してください
$selection
</select>
<input type=submit class=btn value="引き受ける">
<br>
</table>
</form>
運と力を持って、なおかつ知恵は控えめでー。レベルは高めでー。
EOM
if($chara[127]==2){
	print <<"EOM";
<br><br>
討伐クエスト第二弾
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy2>
<table>
<tr>
<th>No.</th><th>対象</th><th>報酬</th><th>進行状態</th></tr>
EOM
	open(IN,"inquest2.cgi");
	@quest2_item = <IN>;
	close(IN);

	foreach(@quest2_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 150;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp経験値";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem2.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>未</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>進行中</th></tr>";
		}
		else{
			print "<th>完了</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno2>
<option value="no">選択してください
$selection
</select>
<table><input type=submit class=btn value="引き受ける">
<br>
</table>
</form>
EOM
if($chara[188]>0){
	print <<"EOM";
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest2_tobasi>
<select name=questno2>
<option value="no">選択してください
$selection
</select>
<table><input type=submit class=btn value="ぶっ飛ばす">
<br>
</table>
</form>
EOM
}
}
if($chara[127]==2 and $chara[18]>=1500 and $chara[7]>99 and $chara[8]<100 and $chara[11]>1000){
	print <<"EOM";
<br><br>
おまけ
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy3>
<table>
<tr>
<th>No.</th><th>目的</th><th>報酬</th><th>進行状態</th></tr>
EOM
	open(IN,"inquest3.cgi");
	@quest3_item = <IN>;
	close(IN);
	$selection="";
	foreach(@quest3_item){
		($q_no,$q_name,$q_gold,$q_exp,$q_item) = split(/<>/);
		$a_no = $q_no - 195;
		print "<th>$a_no</th><th>$q_name</th><th>";
		if($q_gold){print "$q_gold G";}
		if($q_exp){print "$q_exp経験値";}
		if($q_item){
			$item_no=$q_no;
			open(IN,"questitem3.cgi");
			@item_array = <IN>;
			close(IN);
			foreach(@item_array){
($ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei) = split(/<>/);
				if($item_no eq "$ino") {last;}
			}
			print "$i_name";
		}
		print "</th>";
		if($chara[$q_no]==""){
			print "<th>未</th></tr>";
			$selection.="<option value=\"$q_no\">$q_name</option>\n";
		}
		elsif($chara[$q_no]==1){
			print "<th>進行中</th></tr>";
		}
		else{
			print "<th>完了</th></tr>";
		}
	}

	print <<"EOM";
</table>
<br><br>
<select name=questno3>
<option value="no">選択してください
$selection
</select>
<input type=submit class=btn value="引き受ける">
<br>
</table>
</form>
EOM
}
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

sub special {

	&chara_load;

	&chara_check;

	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest_data = split(/<>/,$questdata);

	$hit=0;
	foreach(@quest_data){
		if($_>0){$hit=1;last;}
	}

	&header;

	print <<"EOM";
<h1>スペシャル・クエスト</h1>
<hr size=0>

<FONT SIZE=3>
<B>張り紙</B><BR>
「以下の悪魔を、悪魔界で倒してください。これらのクエストは何度でも受けられますが、同時に受けられるのは１つまでです。」
</FONT>
<br><br>
<form action="./quest.cgi" method="post">
<input type=hidden name=id value=$in{'id'}>
<input type="hidden" name="mydata" value="$chara_log">
<input type=hidden name=mode value=quest_buy4>
<table>
<tr><th>No.</th><th>対象</th><th>報酬</th></tr>
<tr><th> 1 </th><th>スノム</th><th>火の元素</th></tr>
<tr><th> 2 </th><th>スノム</th><th>水の元素</th></tr>
<tr><th> 3 </th><th>スノミ</th><th>闇の元素</th></tr>
<tr><th> 4 </th><th>スノミ</th><th>光の元素</th></tr>
</table>
<br><br>
<select name=questno>
<option value="no">選択してください</option>\n
<option value="1">1．スノム</option>\n
<option value="2">2．スノム</option>\n
<option value="3">3．スノミ</option>\n
<option value="4">4．スノミ</option>\n
</select>
EOM
if($hit!=1){print "<input type=submit class=btn value=\"引き受ける\">";}
	print <<"EOM";
<br>
</table>
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  アイテム買う  #
#----------------#
sub quest_buy {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno'} eq 'no'){
		&error("受けるクエストを選択してください$back_form");
	}

	for($i=101;$i<127;$i++){
		if($chara[$i]=="" and $i < $in{'questno'}){
			&error("前のクエストの中に受けていないクエストがあります。$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("一度に受けられるクエストは３つまでです。$back_form");}

	$quest_no = $in{'questno'};
	if($chara[$quest_no] != ""){
	&error("既にそのクエストは受けています$back_form");
	} else { $chara[$quest_no] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>引き受けました。</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}
sub quest_buy2 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno2'} eq 'no'){
		&error("受けるクエストを選択してください$back_form");
	}

	for($i=151;$i<180;$i++){
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("一度に受けられるクエストは３つまでです。$back_form");}

	$quest_no2 = $in{'questno2'};
	if($chara[$quest_no2] != ""){
	&error("既にそのクエストは受けています$back_form");
	} else { $chara[$quest_no2] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>引き受けました。</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest_buy3 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno3'} eq 'no'){
	&error("受けるクエストを選択してください$back_form");
	}

	for($i=196;$i<200;$i++){
		if($chara[$i]=="" and $i < $in{'questno3'}){
			&error("前のクエストの中に受けていないクエストがあります。$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}
	if($qq>2){&error("一度に受けられるクエストは３つまでです。$back_form");}

	$quest_no3 = $in{'questno3'};
	if($chara[$quest_no3] != ""){
	&error("既にそのクエストは受けています$back_form");
	} else { $chara[$quest_no3] = 1; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>引き受けました。</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest_buy4 {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	open(IN,"quest/$chara[0].cgi");
	$questdata = <IN>;
	close(IN);
	@quest_data = split(/<>/,$questdata);
	$hit=0;
	foreach(@quest_data){
		if($_>0){$hit=1;last;}
	}

	if($in{'questno'} eq 'no'){
	&error("受けるクエストを選択してください$back_form");
	}
	if($hit==1){&error("一度に受けられるクエストは１つまでです。$back_form");}

	$quest_no = $in{'questno'};
	
	$quest_data[$quest_no] = 1;

	$new_data = '';
	$new_data = join('<>',@quest_data);
	$new_data .= '<>';
	open(OUT,">./quest/$chara[0].cgi");
	print OUT $new_data;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>引き受けました。</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}

sub quest2_tobasi {

	&get_host;

	&chara_load;

	&chara_check;

	$chara[26] = $host;

	if($in{'questno2'} eq 'no'){
	&error("ぶっ飛ばすクエストを選択してください$back_form");
	}

	for($i=151;$i<180;$i++){
		if($chara[$i]=="" and $i < $in{'questno2'}){
			&error("前のクエストの中に終了していないクエストがあります。$back_form");
		}
		if($chara[$i]==1){
			$qq++;
		}
	}

	$quest_no2 = $in{'questno2'};
	if($chara[$quest_no2] != ""){
	&error("既にそのクエストは受けています$back_form");
	}elsif($quest_no2 > 166){
	&error("そのクエストはぶっ飛ばせません$back_form");
	}else{ $chara[$quest_no2] = 2; }

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'CR');

	&header;

	print <<"EOM";
<FONT SIZE=5><B>いらないクエストをぶっ飛ばしました。</B></font><BR>
<hr size=0>
EOM

	&shopfooter;

	&footer;

	exit;
}