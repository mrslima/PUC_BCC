<?php

if (isset($_GET["error"])) {
        if ($_GET["error"] == "emptyinput") {
            echo "<p class='form__message form__message--error'>Fill in all fields!</p>";
        }
        else if ($_GET["error"] == "invaliduid") {
            echo "<p class='form__message form__message--error'>User a valid CPF!<br>(11 characters long, ex: 12345678910)</p>";
        }
        else if ($_GET["error"] == "invalidemail") {
            echo "<p class='form__message form__message--error'>Choose a proper email!</p>";
        }
        else if ($_GET["error"] == "passwordsdontmatch") {
            echo "<p class='form__message form__message--error'>Password doesn't match!</p>";
        }
        else if ($_GET["error"] == "useralreadyexists") {
            echo "<p class='form__message form__message--error'>User already exists, try loging in!</p>";
        }
        else if ($_GET["error"] == "stmtfailed") {
            echo "<p class='form__message form__message--error'>Something went wrong, try again!</p>";
        }
        else if ($_GET["error"] == "none") {
            echo "<p class='form__message form__message--success'>You have signed up!</p>";
        }
    }