#------------#
#�@����Ǎ��@#
#------------#
sub item_read {
	open(IN,"$item_file");
	@battle_item = <IN>;
	close(IN);

	$hit=0;
	foreach(@battle_item){
		($ci_no,$item[0],$item[1],$ci_gold,$item[2],$item[24]) = split(/<>/);
		if($_[0] eq $ci_no) {$hit=1;last;}
	}
	if (!$hit) {
		$ci_no = 0;
		$item[0] = '�f��';
		$item[1] = 0;
		$ci_gold = 0;
		$item[2] = 0;
		$item[20] = 0;
		$item[24] = '���ɂȂ�';
	}
}

#------------#
#�@�h��Ǎ��@#
#------------#
sub def_read {
	open(IN,"$def_file");
	@battle_def = <IN>;
	close(IN);

	$hit=0;
	foreach(@battle_def){
		($cd_no,$item[3],$item[4],$cd_gold,$item[5],$item[25]) = split(/<>/);
		if($_[0] eq $cd_no) {$hit=1;last;}
	}
	if (!$hit) {
		$cd_no = 0;
		$item[3] = '���i��';
		$item[4] = 0;
		$cd_gold = 0;
		$item[5] = 0;
		$item[22] = 0;
		$item[25] = '���ɂȂ�';
	}
}

#--------------#
#�@�����i�Ǎ��@#
#--------------#
sub acs_read {
	open(IN,"$acs_file");
	@log_acs = <IN>;
	close(IN);

	$hit=0;
	foreach(@log_acs){
		($a_no,$item[6],$a_gold,$item[7],$item[8],$item[9],$item[10],$item[11],$item[12],$item[13],$item[16],$item[17],$item[18],$item[19]) = split(/<>/);
		if($_[0] eq $a_no){$hit=1;last; }
	}
	if(!$hit) {
		$a_no = 0;
		$a_gold = 0;
		$item[6] = '�Ȃ�';
		$item[7] = 0;
		$item[8] = 0;
		$item[9] = 0;
		$item[10] = 0;
		$item[11] = 0;
		$item[12] = 0;
		$item[13] = 0;
		$item[16] = 0;
		$item[17] = 0;
		$item[18] = 0;
		$item[19] = '-';
	}
}

#----------------------------#
#�@�A�C�e���t�@�C���������݁@#
#----------------------------#
sub item_regist {

	$new_item = "";
	foreach(@item){
		$new_item .="$_<>";
	}
	open(OUT,">./item/$chara[0].cgi"); 
	print OUT $new_item; 
	close(OUT);
	open(OUT,">./autobackup/item/$chara[0].cgi"); 
	print OUT $new_item; 
	close(OUT);

}

#----------------------#
#�@����t�@�C���������@#
#----------------------#
sub item_lose{
	$item[0] = '�f��';
	$item[1] = 0;
	$item[2] = 0;
	$item[20] = 0;
	$item[24] = '���ɂȂ�';
	$chara[24] = 0;
}

#----------------------#
#�@�h��t�@�C���������@#
#----------------------#
sub def_lose{
	$item[3] = '���i��';
	$item[4] = 0;
	$item[5] = 0;
	$item[22] = 0;
	$item[25] = '���ɂȂ�';
	$chara[29] = 0;
}

#------------------------#
#�@�����i�t�@�C���������@#
#------------------------#
sub acs_lose {
	$item[6] = '�Ȃ�';
	$item[7] = 0;
	$item[8] = 0;
	$item[9] = 0;
	$item[10] = 0;
	$item[11] = 0;
	$item[12] = 0;
	$item[13] = 0;
	$item[14] = 0;
	$item[15] = 0;
	$item[16] = 0;
	$item[17] = 0;
	$item[18] = 0;
	$item[19] = '-';
	$chara[31] = 0;
}
#------------------------#
#�@�y�b�g�t�@�C���������@#
#------------------------#
sub pet_lose {
	$chara[38] = 0;
	$chara[39] = "";
	$chara[40] = 0;
	$chara[41] = 0;
	$chara[42] = 0;
	$chara[43] = 0;
	$chara[44] = 0;
	$chara[45] = 0;
	$chara[46] = 0;
	$chara[47] = 0;
	$chara[48] = 0;
	$chara[49] = 0;
}
#------------------------#
#�@�q�Ƀt�@�C���������@�@#
#------------------------#
sub souko_lose {
	open(IN,"$souko_folder/item/$chara[0].cgi");
	@souko_item = <IN>;
	close(IN);

	@souko_item = ();

	open(OUT,">$souko_folder/item/$chara[0].cgi");
	print OUT @souko_item;
	close(OUT);

	open(IN,"$souko_folder/def/$chara[0].cgi");
	@souko_def = <IN>;
	close(IN);

	@souko_def = ();

	open(OUT,">$souko_folder/def/$chara[0].cgi");
	print OUT @souko_def;
	close(OUT);

	open(IN,"$souko_folder/acs/$chara[0].cgi");
	@souko_acs = <IN>;
	close(IN);

	@souko_acs = ();

	open(OUT,">$souko_folder/acs/$chara[0].cgi");
	print OUT @souko_acs;
	close(OUT);

	open(IN,"pets/$chara[0].cgi");
	@log_item = <IN>;
	close(IN);

	@log_item = ();

	open(OUT,">pets/$chara[0].cgi");
	print OUT @log_item;
	close(OUT);

	open(IN,"$itemya_file");
	@item_array = <IN>;
	close(IN);
	$it=0;
	foreach(@item_array){			($i_id,$ino,$i_no,$i_name,$i_gold,$i_dmg,$i_def,$ihit,$i_kai,$i_str,$i_int,$i_dex,$i_vit,$i_luk,$i_ego,$i_hissatu,$i_tokusyu,$i_setumei,$ilv,$iexp) = split(/<>/);

	if($i_id eq $chara[0]){$item_array[$it]="";}
	$it++;
	}

	open(OUT,">$itemya_file");
	print OUT @item_array;
	close(OUT);

	open(IN,"seisanmati.cgi");
	@item_array = <IN>;
	close(IN);
	$it=0;
	foreach(@item_array){
		($i_iname,$i_iiname) = split(/<>/);

	if($i_iname eq $chara[4]){$item_array[$it]="";}
	$it++;
	}

	open(OUT,">seisanmati.cgi");
	print OUT @item_array;
	close(OUT);
}
#------------------------------------#
# �֗��ȃt�b�^�[(�L�����f�[�^�X�V��) #
#------------------------------------#
sub shopfooter {
	print <<"EOM";
<hr>
<td valign="top">
<table width="50%">
<tr>
<form action="$scripty">
<td align="center" class="b2">
<input type=hidden name=mode value="yado">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value=" �@�@�h���@ �@"></td>
</form>
<form action="shops.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value=" �@���X�X�@ "></td>
</form>
<form action="$script_souko">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�A�C�e���q��"></td>
</form>
<form action="$script_bank">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@�@��s�@�@"></td>
</form>
<form action="sakaba.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@�@����@�@"></td>
</form>
<form action="market.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value=" �@�t���}�@ "></td>
</form>
<form action="seizou.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value=" �@�������@ "></td>
</form>
</tr>
<br>
<tr>
<form action="jyoho.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value=" �@��񉮁@ ">
</td>
</form>
<form action="guild.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value=" �@�M���h�@ ">
</td>
</form>
<form action="petsts.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�@�y�b�g�@ ">
</td>
</form>
<form action="bokujyo.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@�@�q��@�@">
</td>
</form>
<form action="kaji.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@ �b�艮�@ ">
</td>
</form>
EOM
if($chara[70]<1){
	print <<"EOM";
<form action="gosei.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�@ �������@ ">
</td>
</form>
<form action="haigo.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@ �z�����@ ">
</td>
</form>
EOM
}else{
	print <<"EOM";
<form action="seityo.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type=submit class=btn value="�@ �������@ "></td>
</form>
<form action="koubou.cgi">
<td align="center" class="b2">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�@�@�H�[�@�@">
</td>
</form>
EOM
}
	print <<"EOM";
</tr>
<tr>
<form action="$script">
<input type="hidden" name="id" value="$chara[0]">
<input type="hidden" name="mydata" value="$new_chara">
<input type="submit" class="btn" value="�X�e�[�^�X��ʂ�"></form>
</tr>
</tr>
</table>
<br>
EOM
}

1;