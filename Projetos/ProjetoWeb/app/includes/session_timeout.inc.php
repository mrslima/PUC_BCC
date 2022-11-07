<?php

$timeout = 60;

//Set the maxlifetime of the session
ini_set( "session.gc_maxlifetime", $timeout );

//Set the cookie lifetime of the session
ini_set( "session.cookie_lifetime", $timeout );

session_start();

//Set the default session name
$s_name = session_name();


//Check the session exists or not
if(isset( $_COOKIE[ $s_name ] )) {
    setcookie( $s_name, $_COOKIE[ $s_name ], time() + $timeout, '/' );
}

else {
    header("location: ../index.php?error=sessionexpired");
    exit();
}


