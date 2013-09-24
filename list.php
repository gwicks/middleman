<?php
$uname = $_POST['uname'];
$pass = $_POST['pass'];

if ($uname != '' && $pass != '')
{
	$command = "echo 'YOUR_ROOT_PASSWORD_HERE' | sudo -u root -S python listsongs.py " . $uname . " " . $pass . " ";


	echo shell_exec($command);
}
else
{
	echo "Please enter login info";
}
?>
