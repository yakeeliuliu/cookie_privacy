<?php
require('connect.php');
$url = mysqli_real_escape_string($connection, $_POST['url']);
$sql = "INSERT INTO url (url) VALUES ($url)";
if(mysqli_query($sql)){
    echo "Records inserted successfully.";
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
 
// Close connection
mysqli_close($link);
?>


