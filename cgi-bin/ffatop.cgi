#!/usr/local/bin/perl

#------------------------------------------------------#
#　本スクリプトの著作権はいくにあります。
#いかなる理由があってもこの表記を削除することはできません
#違反を発見した場合、スクリプトの利用を停止していただく
#だけでなく、然るべき処置をさせていただきます。
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

# レジストライブラリの読み込み
require 'sankasya.pl';

# 初期設定ファイルの読み込み
require 'data/ffadventure.ini';

open(IN,"$winner_file") or &error('ファイルを開けませんでした。');
	@winner_log = <IN>;
	close(IN);

	@winner = split(/<>/,$winner_log[0]);


if($mente) {
	&error("メンテナンス中です");
}

&header;
	print "<br>";
	&guest_list2;

	&guest_view;
	print "<br><br><br><br><br><br><br>";
	print << "EOM";
<script type="text/javascript">
<!--

// 設定開始（スクロールの動きを設定してください）

var speed = 100; // スクロールのスピード（1に近いほど速く）
var move = 5; // スクロールのなめらかさ（1に近いほどなめらかに）

// 設定終了


// 初期化
var x = 0;
var y = 0;
var nx = 0;
var ny = 0;

function scroll(){

	window.scrollBy(0, move); // スクロール処理

	var rep = setTimeout("scroll()", speed);

	// スクロール位置をチェック（IE用）
	if(document.all){

		x = document.body.scrollLeft;
		y = document.body.scrollTop;

	}
	// スクロール位置をチェック（NN用）
	else if(document.layers || document.getElementById){

		x = pageXOffset;
		y = pageYOffset;

	}

	if(nx == x && ny == y){ // スクロールし終わっていたら処理を終了

		clearTimeout(rep);

	}
	else{

		nx = x;
		ny = y;

	}

}

// -->
</script>

EOM
exit;
