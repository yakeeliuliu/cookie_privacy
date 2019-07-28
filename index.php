<head>
	Cookies Pravicy Checker
</head>
	<p>Put your url here: </p>
<form method="post">
	<input type="text" name="url" placeholder="suspicious url">
	<input type="submit" value="Check">
</form>

<?php

require('connect.php');
if(isset($_POST) & !empty($_POST)){
	$url = mysqli_real_escape_string($connection, $_POST['url']);
	$isql = "INSERT INTO url (url) VALUES ('$url')";
	$ires = mysqli_query($connection, $isql) or die(mysqli_error($connection));
	if($ires){
		$smsg = "Your url Submitted Successfully";
	}else{
		$fmsg = "Failed to Submit Your url";
	}
}
?>
