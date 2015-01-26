#----------------#
#  参加者登録    #
#----------------#
sub guest_list{

	$lock_file = "$lockfolder/sanka$in{'id'}.lock";
	&lock($lock_file,'SK');
	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);

	open(IN,"llrank.cgi");
	$llrank=<IN>;
	close(IN);

	$now_time =time();

	$num = 1;
	$blist = '';
	@new_member = ();
	$sanka_hit = 0;

	foreach (@guest) {
		($ntimer,$nname,$nid,$ncolor) = split(/<>/);
			if ($ntimer + $sanka_time > $now_time && $nid ne $chara[0] && $nname ne ""){
				$ll=2;$llhit=0;
				@llrank = split(/<>/,$llrank);
				foreach(@llrank){
					if($_ eq $nid){$llhit=1;last;}
					$ll+=1;
				}
				$ll=int($ll/2);
				if($llhit==1){
					$blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\"><font color=\"#66ff00\">$ll\ξ<font color=\"yellow\">$nname</a><font size=\"1\" color=\"pink\">★</font>";
				}else{
					$blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\"><font color=\"$ncolor\">$nname</a><font size=\"1\" color=\"pink\">★</font>";
				}
				push(@new_member,"$ntimer<>$nname<>$nid<>$ncolor<>\n");
				$num++;
			}
	}
	$ll=2;$llhit=0;
	@llrank = split(/<>/,$llrank);
	foreach(@llrank){
		if($_ eq $chara[0]){$llhit=1;last;}
		$ll+=1;
	}
	$ll=int($ll/2);
	if($llhit==1){
		$blist .= "<a href=\"$scripta?mode=chara_sts&id=$chara[0]\"><font color=\"#66ff00\">$ll\ξ</font><font color=\"yellow\">$chara[4]</a><font size=\"1\" color=\"pink\">★</font>";
		push(@new_member,"$now_time<>$chara[4]<>$chara[0]<>yellow<>\n");
	}elsif($chara[70]==1){
		$blist .= "<a href=\"$scripta?mode=chara_sts&id=$chara[0]\"><font color=\"yellow\">$chara[4]</font></a><font size=\"1\" color=\"pink\">★</font>";
		push(@new_member,"$now_time<>$chara[4]<>$chara[0]<>yellow<>\n");
	}else{
		$blist .= "<a href=\"$scripta?mode=chara_sts&id=$chara[0]\">$chara[4]</a><font size=\"1\" color=\"pink\">★</font>";
		push(@new_member,"$now_time<>$chara[4]<>$chara[0]<><>\n");
	}

	open(GUEST,">$guestfile");
	print GUEST @new_member;
	close(GUEST);
	$lock_file = "$lockfolder/sanka$in{'id'}.lock";
	&unlock($lock_file,'SK');

}

#----------------#
#  参加者表示    #
#----------------#
sub guest_view {

	print "<font size=2 color=#aaaaff>現在の冒険者(<B>$num人</B>)：</font>\n";

	if ($blist) {
		print $blist;
	}
	else {
		print '誰もいません';
	}
}

sub guest_list2{

	$lock_file = "$lockfolder/sanka$in{'id'}.lock";
	&lock($lock_file,'SK');
	open(GUEST,"$guestfile");
	@guest=<GUEST>;
	close(GUEST);

	open(IN,"llrank.cgi");
	$llrank=<IN>;
	close(IN);

	$now_time =time();

	$num = 0;
	$blist = '';
	@new_member = ();
	$sanka_hit = 0;
	foreach (@guest) {
		($ntimer,$nname,$nid,$ncolor) = split(/<>/);
			if ($ntimer + $sanka_time > $now_time && $nname ne "") {
				$ll=2;$llhit=0;
				@llrank = split(/<>/,$llrank);
				foreach(@llarray){
					if($_ eq $nid){$llhit=1;last;}
					$ll+=1;
				}
				$ll=int($ll/2);
				if($llhit==1){
					$blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\"><font color=\"#66ff00\">$ll\ξ<font color=\"yellow\">$nname</a><font size=\"1\" color=\"pink\">★</font>";
				}else{
					$blist .= "<a href=\"$scripta?mode=chara_sts&id=$nid\"><font color=\"$ncolor\">$nname</a><font size=\"1\" color=\"pink\">★</font>";
				}
				push(@new_member,"$ntimer<>$nname<>$nid<>$ncolor<>\n");
				$num++;
			}
	}

	open(GUEST,">$guestfile");
	print GUEST @new_member;
	close(GUEST);
	$lock_file = "$lockfolder/sanka$in{'id'}.lock";
	&unlock($lock_file,'SK');

}

1;
