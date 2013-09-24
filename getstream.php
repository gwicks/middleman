<?php
$uname = $_POST['uname'];

$pass = $_POST['pass'];

$songid = $_POST['id'];


$command = "echo 'YOUR_ROOT_PASSWORD_HERE' | sudo -u root -S python getsong.py " . $uname . " " . $pass . " " . $songid;

echo shell_exec($command);

?>
