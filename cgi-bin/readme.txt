
CrazaChat ver 1.03
　作った人　kroko
　連絡先？　kroko_ffb@hotmail.com
　　　　　　http://kroko.maxs.jp/~kroko/mt/

　転送量がやばくなりそうな危険なチャットなので
　使用に際しては各自の判断で責任を持ってやって下さい。
　あと、穴があると思います。


　適当なチャットを使用するには以下の使用条件に同意する必要があります。
　同意できない場合は使わないで下さい。
　　- それなりにCGIに関して知識のある方のみお使いください。 
　　- すべて自己責任でお使い下さい。 
　　- 適当なチャットを使用して起こったいかなる損害も作者は保証しません。 
　　- 作者はサポート、不具合修正をはじめいかなる義務も負いません。 




内容物
	chat.cgi
	chatm.cgi
	chatadmin.cgi
　　chatini.cgi

　　readme.txt
　　index.htm

　勝手に作成されるはずのファイル(作成されないときは自分で作ってね)
	guest.cgi
	chatlog.cgi

　作成されないファイル
　　chatkanri.cgi

使用法
　cgiファイルの一行目をサーバーで指定されている物に変更。
　FTPで同一ディレクトリ内にアップ。
　パーミッションを、chat.cgiとchatm.cgi、chatadmin.cgiは705にします。（サーバーによっては違うので注意）
　勝手に生成されるはずのファイルのパーミションは606などが良いかもです

　chat.cgiにアクセスすれば動くと思います。




隔離使用法
　chatadmin.cgiで簡単に荒らしを隔離できます。
　chatkanri.cgiというファイルを作成して１行ごとに
　管理者ID<>管理レベル<>管理パス
　の形式で作成して下さい。
　よく分からない人は使わないで下さい


変更履歴
ver 1.03
　名称をCrazeChatに変更した(「熱狂のチャット」の意味を期待
　設定を外部ファイルにした(chatini.cgi
　設定可能箇所を増やした
　判別用IDをipを元にとることにした
　他所に設置されたCrazaChatからの進入防止策(乱数の種のとこ)　
　作り直した管理用cgiを同梱した

ver 1.02
　管理用スクリプト削除(後で作る予定)
　chatm.cgiの過去の遺産(複数行入力対応部分削除)

ver 1.01
　管理用スクリプトchat*****.cgi追加

ver 1.00
　一応完成
　配色、文字サイズ、制限文字数に改良の余地有り


今後の予定として考えられること
  長い名前対策
　管理者管理スクリプト作成
　表示設定(<hr>で区切る　時間表示　rom表示 etcetc)
　トリップ表示をもっとスマートに
　スタイルシートの外部化によりデザイン可能なチャットに
　書き込み色を選択できるように
　人工無能
　チャンネルごとに人工無能の種類を設定