<?php

if (isset($_GET["error"])) {
    if ($_GET["error"] == "emptyinput") {
        echo "<p class='form__message form__message--error'>Fill in all fields!</p>";
    }
    else if ($_GET["error"] == "wronglogin") {
        echo "<p class='form__message form__message--error'>Wrong information!</p>";
    }
    else if ($_GET["error"] == "sessionexpired") {
        echo "<p class='form__message form__message--error'>Session expired!</p>";
    }
}