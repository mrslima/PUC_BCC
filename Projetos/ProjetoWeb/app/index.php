<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css">
    <link rel="stylesheet" href="./css/header.css">
    <link rel="stylesheet" href="./css/footer.css">
    <link rel="stylesheet" href="./css/auth.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Roboto+Mono&family=Roboto+Slab&family=Secular+One&family=Teko&display=swap" rel="stylesheet">
    <title>Postmodern Vinyl Shop</title>
</head>
<body>
    <!-- HEADER -->
    <div class="announce-bar">
        <a href="#">NEW RELEASE! Buy &#60COPINGMECHANISM&#62 by Willow Smith</a>
    </div>
    <!-- NAV BAR -->
    <div class="nav-bar">
        <nav>
            <ul class="nav-links nav-links-txt-default hidden">
                <li><a href="#">SHOP</a></li>
                <li><a href="#">CART</a></li>
            </ul>
            <img src="./img/pvs_logo.png" id="pvs_logo">
            <ul class="nav-links nav-links-txt-default hidden">
                <li><a href="../includes/logout.inc.php">LOG OUT</a></li>
                <li>
                    <div class="icon">
                        <div class="tooltip">
                            <span class="span__title">PROFILE:</span>
                            <?php echo '<span class="span__content">'. ucwords($_SESSION['userid']) . '</span>' ?>
                        </div>
                        <span class="icon"><i class="fa-solid fa-user"></i></span>
                    </div>
                </li>
            </ul>
        </nav>
    </div>
    <!-- END OF NAV BAR -->
    <!-- END OF HEADER -->
    <div class="body">
        <!-- LOGIN FORM -->
        <section class="container">
            <form action="includes/login.inc.php" method="post" class="form" id="login">
                <h1 class="form__title">LOGIN</h1>
                <div class="form__message form__message--error"></div>
                <div class="form__input-group">
                    <input type="text" name="email" class="form__input" autofocus placeholder="Email">
                    <div class="form__input-error-message"></div>
                </div>
                <div class="form__input-group">
                    <input type="password" name="pwd" class="form__input" autofocus placeholder="Password">
                    <div class="form__input-error-message"></div>
                </div>
                <?php
                    include_once('includes/login_errors.inc.php');
                ?>
                <button class="form__button" name="submit" type="submit">SIGN IN</button>
                <p class="form__text">
                    <a class="form__link form__link--button" href="php/signup.php" id="linkCreateAccount">Don't have an account? Create account.</a>
                </p>
            </form>
        </section>
        <!-- END OF FORM  -->
    </div>
</body>
<footer class="footer">
    <div class="footer__container">
        <img src="img/pvs_logo.png" class="footer__container-logo">
        <p>@ Postmodern Vinyl Shop</p>
        <div class="footer__container-socials">
            <a href="https://facebook.com" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            <a href="https://twitter.com" target="_blank"><i class="fa-brands fa-twitter"></i></a>
            <a href="https://pinterest.com" target="_blank"><i class="fa-brands fa-pinterest"></i></a>
            <a href="https://instagram.com" target="_blank"><i class="fa-brands fa-instagram"></i></a>
        </div>
    </div>
</footer>

