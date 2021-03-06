#---------------------------------------------------------------#
#　ChatSystem ver2.10 設定ファイル
#　Edit by Lost
#　http://kirbys.oo.lv/
#---------------------------------------------------------------#

# ログファイル（セキュリティ対策として変えることも出来ます。）デフォルト：./chat_log.cgi
$chat_log_file = "./chat_log.cgi";

# チャット禁止ユーザーのＩＤ（,""を増やして区切ります。）デフォルト：test
@bad_id = ("test");

# 発言文字数（半角での文字数です。全角で発言できるのは指定した数値の1/2です。）デフォルト：1000
$mes_n = "1000";

# 指定なしの発言文字色（文字色を指定しないで発言した場合の文字色です。）デフォルト：#FF0000
$mes_c = "#FF0000";

# 指定なしの発言文字サイズ（文字サイズを指定しないで発言した場合のサイズです。）デフォルト：10px
$mes_s = "13px";

# 発言文字サイズ（上と下を合わせてください。"",で増やせます。）
@size_list = ("小","中","大","極小");     # サイズ名
@size_num = ("10px","13px","18px","8px");  # サイズ pt（ポイント）やpx（ピクセル）などで指定

# 発言文字色（上と下を合わせてください。"",で増やせます。）
@color_list = ("赤色","青色","緑色","黄色","栗色","紺色","黄緑","明黄");  # 色名
@color_num = ("#FF5555","#0033FF","#66FF99","#E6B417","#CC0000","#000099","#66CC00","#F4D13F");  # 文字色 16進数のRGBカラーコードで指定します。,"#CCFFCC","#F4D13F"

# 部屋設定（すべて位置を合わせてください。"",で増やせます。）
@chat_room = ("room","room2","room3","bosyu","room4","room5","room6");  # チャットID
@room_list = ("ネタバレ","イベント","商談","募集","その他１","その他２","その他３");  # チャット名

# 文字サイズを保存するキャラログ（標準の色を設定した際に、保存する番号です。）デフォルト：35
$color_chara = "35";

# 文字色を保存するキャラログ（標準のサイズを設定した際に、保存する番号です。）デフォルト：36
$size_chara = "36";

# 表示スタイルを保存するキャラログ（標準の表示スタイルを設定した際に、保存する番号です。）デフォルト：38
$style_chara = "37";

# ログ表示数（数値を大きくするほど見れるログは増えますが、読み込みが遅くなります。）デフォルト：30
$view_mes = "30";

# ログ保存数（数値を大きくするほど保存するログは増えますが、ログ容量が大きくなります。）デフォルト：100
$save_mes = "100";

1;