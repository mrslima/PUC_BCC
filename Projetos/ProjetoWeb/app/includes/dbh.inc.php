<!-- Database Handler -->

<?php


$severName = "localhost";
$dBUsername = "root";
$dBPassword = "Trombetas123!@#";  // PUC@1234
$dBName = "pmvshopDB";


$conn = mysqli_connect($serverName, $dBUsername, $dbPassword, $dBName);

if (!$conn) {
    die("Connection failed!".mysqli_connect_error());
}