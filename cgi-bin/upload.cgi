#!/usr/local/bin/perl -w
BEGIN{ $| = 1; print "Content-type: text/html\n\n"; open(STDERR,">&STDOUT"); }
# ���W���[���ǂݍ���
use strict;
use CGI;

# POST�T�C�Y�̏��
$CGI::POST_MAX = 1024 * 1024; # 1MB

my $query = new CGI;

# �����ݒ� -------------------------------------
# �ő勖�e�T�C�Y�iKByte�j
my $maxsize = 300;

# �ۑ���f�B���N�g��
my $logfiles = "./images/chara";

# �A�b�v���[�h��������t�@�C���̎�ށiMIME�Ɗg���q�j
my %hash_mime = (
  'text/html' => 'html', # HTML�t�@�C��
  'image/jpeg' => 'jpg', # JPEG�t�@�C��
  'image/pjpeg' => 'jpg',# �v���O���b�V�uJPEG�t�@�C��
  'image/gif' => 'gif'   # GIF
  );


# �����Ă����f�[�^���������� -----------------
# �t�@�C���擾
my $fH = $query->upload('filename');

# �G���[�`�F�b�N
if ($query->cgi_error) {
  my $err = $query->cgi_error;
  &error("$err") if ($err);
}

&error("File transfer error.") unless (defined($fH));

# MIME�^�C�v�擾
my $mimetype = $query->uploadInfo($fH)->{'Content-Type'};

# �ۑ�����t�@�C�������擾
my $set = &set_name($mimetype);

# �t�@�C���T�C�Y�擾
my $size = (stat($fH))[7];

# �T�C�Y����
&error("The filesize is too large. Max $maxsize KB") if ($size > $maxsize * 1024);


# �t�@�C���ۑ� ---------------------------------
my ($buffer);
open (OUT, ">$logfiles/$set") || &error("Can't open $set");
binmode (OUT);
while(read($fH, $buffer, 1024)){
    print OUT $buffer;
}
close (OUT);
close ($fH) if ($CGI::OS ne 'UNIX'); # Windows�v���b�g�t�H�[���p
chmod (0666, "$logfiles/$set");


# HTML�o�� -------------------------------------
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
<h1>�t�@�C���A�b�v���[�h</h1>
<p>�t�@�C���̃A�b�v���[�h���������܂����B�X�e�[�^�X�̕ύX�ŉ摜�m���Ɂu$imgno�v�Ɠ��͂��Ă��������B</p>
<ul>
  <li><a href="others.cgi">�s�n�o��</a></li>
</ul>
HTML_VIEW

print $query->end_html;

exit;


# �t�@�C������ݒ� -----------------------------
sub set_name {
  my ($mime) = @_;

  # �g���q���Z�b�g
  my $ext = $hash_mime{$mime} ? $hash_mime{$mime} : &error("Can't permit this file.");
  # �t�@�C�����̃t�H�[�}�b�g
  my $set = time . "_" . $$ . "." . $ext;

  return $set;
}

# �G���[�o�� -----------------------------------
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
