<?php

if (isset($_POST["submit"])) {
    $name = $_POST["name"];
    $userid = $_POST["userid"];
    $email = $_POST["email"];
    $pwd = $_POST["pwd"];
    $confirmPwd = $_POST["confirmpwd"];

    require_once("./dbh.inc.php");
    require_once("./functions.inc.php");

    if (emptyInputSignup($name, $userid, $email, $pwd, $confirmPwd) !== false) {
        header("location: ../php/signup.php?error=emptyinput");
        exit();
    }
    if (invalidUid($userid) !== false) {
        header("location: ../php/signup.php?error=invaliduid");
        exit();
    }
    if (invalidEmail($email) !== false) {
        header("location: ../php/signup.php?error=invalidemail");
        exit();
    }
    if (pwdMatch($pwd, $confirmPwd) !== false) {
        header("location: ../php/signup.php?error=passwordsdontmatch");
        exit();
    }
    if (uidExists($conn, $userid, $email) !== false) {
        header("location: ../php/signup.php?error=useralreadyexists");
        exit();
    }

    createUser($conn, $name, $userid, $email, $pwd);
}
else {
    header("location: ../index.php");
    exit();
}