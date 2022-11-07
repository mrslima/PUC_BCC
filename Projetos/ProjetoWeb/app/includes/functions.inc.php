<?php

function emptyInputSignup($name, $userid, $email, $pwd, $confirmPwd) {
    $result;

    if (empty($name) || empty($userid) || empty($email) || empty($pwd) || empty($confirmPwd)) {
        $result = true;
    }
    else {
        $result = false;
    }

    return $result;

}

function invalidUid($userid) {
    $result;
    if (!preg_match("/^[0-9]*$/", $userid)) {
        $result = true;
    }
    else {
        $result = false;
    }

    return $result;

}

function invalidEmail($email) {
    $result;
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $result = true;
    }
    else {
        $result = false;
    }

    return $result;

}

function pwdMatch($pwd, $confirmPwd) {
    $result;
    if ($pwd !== $confirmPwd) {
        $result = true;
    }
    else {
        $result = false;
    }

    return $result;

}

function uidExists($conn, $userid, $email) {
    // preventing code injection thru form inputs in db
    $sql = "SELECT * FROM users WHERE usersId = ? OR usersEmail = ?;";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ../signup.php?error=stmtfailed");
        exit();
    }

    mysqli_stmt_bind_param($stmt, "ss", $userid, $email);
    mysqli_stmt_execute($stmt);

    $resultData = mysqli_stmt_get_result($stmt);

    if ($row = mysqli_fetch_assoc($resultData)) {
        return $row;
    }
    else {
        $result = false;
        return $result;
    }

    mysqli_stmt_close($stmt);
}


function createUser($conn, $name, $userid, $email, $pwd) {
    // preventing code injection thru form inputs in db
    $name = ucwords($name);
    $sql = "INSERT INTO users (usersID, usersName, usersEmail, usersPwd) VALUES (?, ?, ?, ?);";
    $stmt = mysqli_stmt_init($conn);
    if (!mysqli_stmt_prepare($stmt, $sql)) {
        header("location: ./php/signup.php?error=stmtfailed");
        exit();
    }

    $hashedPwd = password_hash($pwd, PASSWORD_DEFAULT);
    // $hashedPwd = $pwd

    mysqli_stmt_bind_param($stmt, "ssss", $name, $userid, $email, $hashedPwd);
    mysqli_stmt_execute($stmt);
    mysqli_stmt_close($stmt);
    
    header("location: ../index.php?error=none");
    exit();
}

function emptyInputLogin($email, $pwd) {
    $result;

    if (empty($email) || empty($pwd)) {
        $result = true;
    }
    else {
        $result = false;
    }

    return $result;

}

function loginUser($conn, $email, $pwd) {
    $uidExists = uidExists($conn, $email, $email);

    if ($uidExists === false) {
        header("location: ../index.php?error=wronglogin");
        exit();
    }

    $pwdHashed = $uidExists["usersPwd"];
    $checkPwd = password_verify($pwd, $pwdHashed);

    if ($checkPwd === false) {
        header("location: ../index.php?error=wronglogin");
        exit();
    }
    else if ($checkPwd === true) {
        session_start();
        $_SESSION["userid"] = $uidExists["usersId"];
        $_SESSION["name"] = $uidExists["usersName"];
        header("location: ../php/home.php");
        exit();
    }
}