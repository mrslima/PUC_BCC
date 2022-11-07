<?php
    include_once('../includes/session_timeout.inc.php');
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
    <link rel="stylesheet" href="../css/header.css">
    <link rel="stylesheet" href="../css/footer.css">
    <link rel="stylesheet" href="../css/auth.css">
    <link rel="stylesheet" href="../css/home.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto+Mono&family=Roboto+Slab&family=Secular+One&family=Teko&display=swap" rel="stylesheet">
    <script src="../js/carousel.js" defer></script>
    <title>Postmodern Vinyl Shop</title>
</head>
<body>
    <!-- HEADER -->
    <div class="announce-bar top">
        <a href="#">NEW RELEASE! Buy &#60COPINGMECHANISM&#62 by Willow Smith</a>
    </div>
    <!-- NAV BAR -->
    <div class="nav-bar">
    <nav>
        <?php
        if (isset($_SESSION['userid'])){
            echo '<ul class="nav-links nav-links-txt-default">
                <li><a href="#">SHOP</a></li>
                <li><a href="#">CART</a></li>
            </ul>
            <img src="../img/pvs_logo.png" id="pvs_logo">
            <ul class="nav-links nav-links-txt-default">
                <li><a href="../includes/logout.inc.php">LOG OUT</a></li>
                <li>
                    <div class="icon">
                        <div class="tooltip">
                            <span class="span__title">PROFILE:</span>
                            <span class="span__content">' . ucwords($_SESSION['userid']) . '</span>
                        </div>
                        <span class="icon"><i class="fa-solid fa-user"></i></span>
                    </div>
                </li>
            </ul>';
        }
        else {
            echo '<ul class="nav-links nav-links-txt-default hidden">
                <li><a href="#">SHOP</a></li>
                <li><a href="#">CART</a></li>
            </ul>
            <img src="../img/pvs_logo.png" id="pvs_logo">
            <ul class="nav-links nav-links-txt-default hidden">
                <li><a href="../includes/logout.inc.php">LOG OUT</a></li>
                <li>
                    <div class="icon">
                        <div class="tooltip">
                            <span class="span__title">PROFILE:</span>
                            <span class="span__content">' . ucwords($_SESSION['userid']) . '</span>
                        </div>
                        <span class="icon"><i class="fa-solid fa-user"></i></span>
                    </div>
                </li>
            </ul>';
        }
        ?>

            <!-- <ul class="nav-links nav-links-txt-active">
                <li><a href="#">SHOP</a></li>
                <li><a href="#">CART</a></li>
            </ul>
            <div class="burger">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div> -->
        </nav>
    </div>
    <!-- END OF NAV BAR -->
    <!-- END OF HEADER -->