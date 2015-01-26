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
<form action="kinkyuu.cgi" >
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
<h1>緊急所</h1>
<hr size=0>
<FONT SIZE=3>
<B>緊急所</B><BR>
「最近発生しているキャラバグ対策。<br>
ここでデータを保存しておくと、キャラ消失時に復活する、と思います。<br>
一日に１回ぐらいしておくと良い感じです。<br>
既に消失してしまったデータの復帰対応も、ここで出来るようにしたいとおもっていますが…。<br>
キャラが消失して、IDが見つかりませんとなった時は、<font color="red" size=5><b>同じID</b></font>でキャラを作り直し、ここへ来てください。」
<font color="red" size=5><b>現在、データは自動で保存されるようになっています。手動保存は停止中。</b></font>
</FONT>
<hr size=0>
<br>
<form action="./kinkyuu.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=data>
<input type=submit class=btn value="とりあえずデータを保存" disabled>
</form>
<form action="./kinkyuu.cgi" >
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen>
<input type=submit class=btn value="データを復元" disabled>(消失時以外の場合に押すとバグの原因になります。)
</form>
<font size =5 color="red">すでに消失してしまったデータ復帰(最小限)(同じIDでキャラを作って入力してください)</font><br>
以下の復帰に必要な情報を全て半角英数字で入力してください。（おおよそで\構\いません）<br>
<font size =5 color="red">同じIDでキャラを作っていれば倉庫内、牧場内、職業履歴などは自動で復元しているはずです</font><br>
<form action="./kinkyuu.cgi" >
アビリティポイント:<input type="text" name="13" value="" size=10><br>
レベル:<input type="text" name="18" value="" size=10><br>
所持金:<input type="text" name="19" value="" size=10><br>
転生回数:<input type="text" name="37" value="" size=10><br>
善人度:<input type="text" name="64" value="" size=10><br>
悪人度:<input type="text" name="65" value="" size=10><br>
クラウン:<input type="text" name="69" value="" size=10>(デビルクラウンなら1、エンジェルクラウンなら2と入力)<br>
突破の有無:<input type="text" name="70" value="" size=10>(突破後なら1、突破前なら0と入力)<br>
闇の石所持数:<input type="text" name="71" value="" size=10><br>
白い光所持数:<input type="text" name="72" value="" size=10><br>
王石所持数:<input type="text" name="73" value="" size=10><br>
空豆所持数:<input type="text" name="74" value="" size=10><br>
ダークマター所持数:<input type="text" name="75" value="" size=10><br>
セブンスター所持数:<input type="text" name="76" value="" size=10><br>
閃光石所持数:<input type="text" name="77" value="" size=10><br>
復活の石所持数:<input type="text" name="78" value="" size=10><br>
神秘石所持数:<input type="text" name="79" value="" size=10><br>
王者の証所持数:<input type="text" name="80" value="" size=10><br>
帝王の証所持数:<input type="text" name="81" value="" size=10><br>
無敵所持数:<input type="text" name="82" value="" size=10><br>
黄金のつるはし所持数:<input type="text" name="97" value="" size=10><br>
特殊合成石所持数:<input type="text" name="98" value="" size=10><br>
合成石所持数:<input type="text" name="99" value="" size=10><br>
つるはし所持数:<input type="text" name="100" value="" size=10><br>
イエローワールドの鍵所持の有無:<input type="text" name="131" value="" size=10>(有れば1、無ければ0)<br>
レッドワールドの鍵所持の有無:<input type="text" name="132" value="" size=10>(有れば1、無ければ0)<br>
ドラゴンワールドの鍵所持の有無:<input type="text" name="133" value="" size=10>(有れば1、無ければ0)<br>
屋敷で使ったお金:<input type="text" name="187" value="" size=10><br>
レベルダウン回数(突破後):<input type="text" name="188" value="" size=10><br>
闇空間チケット所持数:<input type="text" name="189" value="" size=10><br>
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=hukugen2>
<input type=submit class=btn value="確認">
</form>
EOM

	$new_chara = $chara_log;

	&shopfooter;

	&footer;

	exit;
}

#----------------#
#  情報買う　　  #
#----------------#
sub data {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	$chara[303]=$mday + $mon + $year;

	$dnew_chara = '';

	$dnew_chara = join('<>',@chara);

	$dnew_chara .= '<>';

	open(OUT,">./dcharalog/$in{'id'}.cgi");
	print OUT $dnew_chara;
	close(OUT);

	&chara_regist;
	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
キャラデータを保存しました。<br>
</font>
<br>
<form action="kinkyuu.cgi" >
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

sub hukugen {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	open(IN,"./dcharalog/$in{'id'}.cgi") || &error("$in{'id'}キャラクターが($!)見つかりません$ENV{'CONTENT_LENGTH'}");
	$chara_log2 = <IN>;
	close(IN);

	@chara2 = split(/<>/,$chara_log2);

	if($chara2[303] == $mday + $mon + $year){
		&error("すみません、今日は復元できません。明日、試してください。(バグ利用対策)");
	}
	elsif($chara[70] == 1 or $chara[37] > 40){
		&error("あなたのキャラは消失後とは思えない強さです。");
	}
	else{
		open(OUT,">./charalog/$in{'id'}.cgi");
		print OUT $chara_log2;
		close(OUT);
	}

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
無事に復元が完了しました！！<br>
</font>
<br>
<form action="kinkyuu.cgi" >
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

sub hukugen2 {

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&lock($lock_file,'SU');

	&chara_load;

	&chara_check;

	&get_host;

	for($noo=0;$noo<200;$noo++){
		if($in{$noo}){$chara[$noo]=$in{$noo};}
	}
	if($in{'70'}==1){
		for($nooo=101;$nooo<128;$nooo++){
			$chara[$nooo]=2;
		}
	}
	$enew_chara = '';

	$enew_chara = join('<>',@chara);

	$enew_chara .= '<>';

	open(OUT,">./echaralog/$in{'id'}.cgi");
	print OUT $enew_chara;
	close(OUT);

	$lock_file = "$lockfolder/$in{'id'}.lock";
	&unlock($lock_file,'SU');
	
	&header;

	print <<"EOM";
<FONT SIZE=3>
<B></B><BR>
復元\申\請\しました。この復元は<font color="red">手動</font>で行われます。<br>
掲示板などを通じて、復元\申\請\完了したことを管理人に一言伝えてください。<br>
入力お疲れ様でした。<br>
</font>
<br>
<form action="kinkyuu.cgi" >
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