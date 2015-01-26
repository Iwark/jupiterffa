#!/usr/bin/perl
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }

# 日本語ライブラリの読み込み
require 'jcode.pl';

# レジストライブラリの読み込み
require 'regist.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

# shopfooter呼び出し
require 'item.pl';

# このファイル用設定
$backgif = $shop_back;
$midi = $shop_midi;

#================================================================#
#┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓#
#┃ これより下はCGIに自信のある方以外は扱わないほうが無難です　┃#
#┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛#
#================================================================#

#--------------#
#　メイン処理　#
#--------------#
if ($mente) {
	&error("バージョンアップ中です。２、３０秒ほどお待ち下さい。m(_ _)m");
}

&decode;

	$back_form = << "EOM";
<br>
<form action="icon.cgi" method="post">
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

if ($mode) { &$mode; }
&tensyoku;

exit;

#------------#
# 転職の神殿 #
#------------#
sub tensyoku {

	&chara_load;

	&chara_check;

	&header;

	print <<"EOM";
<h1>アイコン所</h1><hr>
アイコンをアップロードできます。<br>
形式はＧＩＦもしくはＪＰＥＧのみで、サイズは小さい奴をお願いします。<br>
まぁ既にここに来れている方には関係ない話ですが、ハードモードの方専用ですよっと。<br>
また、アイコンをアップロードしたあとは、必ず専用化ボタンを押してください。<br>
<font color="red" size=4>自分のアップロードした画像以外を専用化するのは絶対にやめてください！！</font><br>
<font color="red" size=4>一日に何度も行ったり、送信後に更新ボタン(Ｆ５)を押したりしないでください。</font><br>
<font color="red" size=4><br>画像は小さめのもの、サイズは20K Bytes以下を目安にしてください。</br></font>
    <form action="upload.cgi" method="post" enctype="multipart/form-data">
      <p><input type="file" name="filename" /></p>
      <p>
         <input type="submit" class=btn value="送信" />
         <input type="reset" class=btn value="リセット" />
      </p>
    </form>
<form action="./icon.cgi" method="post">
<input type=hidden name=id value="$chara[0]">
<input type=hidden name=mydata value="$chara_log">
<input type=hidden name=mode value=uketoru>
画像No.：<input type="text" name="no" value="" size=20><br>
<td><input type=submit class=btn value="専用化"></td>
</form>
EOM

	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}
sub uketoru {
	
	&get_host;

	&chara_load;

	&chara_check;

	if (!$in{'no'}){ &error("画像ナンバーを入力してください。$back_form"); }

	open(IN,"senyou.cgi");
	@member_data = <IN>;
	close(IN);
	$i=0;$sakujyo=0;
	foreach (@member_data) {
		($cid,$cno) = split(/<>/);
		if ($cno == $in{'no'}) {
			&error("既にそのアイコンは専用化されています。$back_form");
		}
		if ($cid eq $chara[0]){$sakujyo=$i+1;}
		$i++;
	}
	open(IN,"data/img.cgi");
	@img_data = <IN>;
	close(IN);
	$no_img_data=@img_data;
	if (200>$in{'no'} or 201+$no_img_data<$in{'no'}) {
		&error("専用化できる番号ではないようです。$back_form");
	}
	if($sakujyo){
		$sakujyo=$sakujyo-1;
		splice(@member_data,$sakujyo,1);
	}

	push(@member_data,"$chara[0]<>$in{'no'}<>\n");

	open(OUT,">senyou.cgi");
	print OUT @member_data;
	close(OUT);

	&header;

	print <<"EOM";
<FONT SIZE=3>
<B>アイコン所のマスター</B><BR>
「専用化が完了したぞ。
」</font>
<hr size=0>
EOM
	$new_chara = $chara_log;
	&shopfooter;

	&footer;

	exit;
}