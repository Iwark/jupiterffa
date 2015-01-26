#!/usr/local/bin/perl -w
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
# モジュール読み込み
use strict;
use CGI;

# POSTサイズの上限
$CGI::POST_MAX = 1024 * 1024; # 1MB

my $query = new CGI;

# 初期設定 -------------------------------------
# 最大許容サイズ（KByte）
my $maxsize = 300;

# 保存先ディレクトリ
my $logfiles = "./images/chara";

# アップロードを許可するファイルの種類（MIMEと拡張子）
my %hash_mime = (
  'text/html' => 'html', # HTMLファイル
  'image/jpeg' => 'jpg', # JPEGファイル
  'image/pjpeg' => 'jpg',# プログレッシブJPEGファイル
  'image/gif' => 'gif'   # GIF
  );


# 送られてきたデータを処理する -----------------
# ファイル取得
my $fH = $query->upload('filename');

# エラーチェック
if ($query->cgi_error) {
  my $err = $query->cgi_error;
  &error("$err") if ($err);
}

&error("File transfer error.") unless (defined($fH));

# MIMEタイプ取得
my $mimetype = $query->uploadInfo($fH)->{'Content-Type'};

# 保存するファイル名を取得
my $set = &set_name($mimetype);

# ファイルサイズ取得
my $size = (stat($fH))[7];

# サイズ制限
&error("The filesize is too large. Max $maxsize KB") if ($size > $maxsize * 1024);


# ファイル保存 ---------------------------------
my ($buffer);
open (OUT, ">$logfiles/$set") || &error("Can't open $set");
binmode (OUT);
while(read($fH, $buffer, 1024)){
    print OUT $buffer;
}
close (OUT);
close ($fH) if ($CGI::OS ne 'UNIX'); # Windowsプラットフォーム用
chmod (0666, "$logfiles/$set");


# HTML出力 -------------------------------------
print $query->header(-charset=>'Shift_JIS'),
      $query->start_html(-lang=>'ja', -encoding=>'Shift_JIS', -title=>'upload.cgi');

	open(IN,"data/img.cgi");
	my @img = <IN>;
	close(IN);

	push(@img,"$set\n");

	open(OUT,">data/img.cgi");
	print OUT @img;
	close(OUT);
	my $imgno = @img + 200;
print <<"HTML_VIEW";
<h1>ファイルアップロード</h1>
<p>ファイルのアップロードが完了しました。ステータスの変更で画像Ｎｏに「$imgno」と入力してください。</p>
<ul>
  <li><a href="others.cgi">ＴＯＰへ</a></li>
</ul>
HTML_VIEW

print $query->end_html;

exit;


# ファイル名を設定 -----------------------------
sub set_name {
  my ($mime) = @_;

  # 拡張子をセット
  my $ext = $hash_mime{$mime} ? $hash_mime{$mime} : &error("Can't permit this file.");
  # ファイル名のフォーマット
  my $set = time . "_" . $$ . "." . $ext;

  return $set;
}

# エラー出力 -----------------------------------
sub error {
  my ($mes) = @_;

  print $query->header(-charset=>'Shift_JIS'),
        $query->start_html(-lang=>'ja', -encoding=>'Shift_JIS', -title=>'upload.cgi');

  print <<"HTML_VIEW";
<h1>ERROR</h1>
<p>$mes</p>
HTML_VIEW

  print $query->end_html;
  exit;
}
__END__
