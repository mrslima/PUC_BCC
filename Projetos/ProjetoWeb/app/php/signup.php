<?php
    include_once('../php/header.php');
?>

<div class="body">
    <!-- LOGIN FORM -->
    <section class="container">
        <form action="../includes/signup.inc.php" method="post" class="form" id="createAccount">
            <h1 class="form__title">CREATE ACCOUNT</h1>
            <div class="form__message form__message--error"></div>
            <div class="form__input-group">
                <input type="text" name="name" class="form__input" id="signupName" autofocus placeholder="Full Name">
                <div class="form__input-error-message"></div>
            </div>
            <div class="form__input-group">
                <input type="text" name="userid" class="form__input" autofocus placeholder="CPF">
                <div class="form__input-error-message"></div>
            </div>
            <div class="form__input-group">
                <input type="text" name="email" class="form__input" autofocus placeholder="Email">
                <div class="form__input-error-message"></div>
            </div>
            <div class="form__input-group">
                <input type="password" name="pwd" class="form__input" id="signupPassword" autofocus placeholder="Password">
                <div class="form__input-error-message"></div>
            </div>
            <div class="form__input-group">
                <input type="password" name="confirmpwd" class="form__input" autofocus placeholder="Confirm Password">
                <div class="form__input-error-message"></div>
            </div>
            <?php
                include_once('../includes/signup_errors.inc.php');
            ?>
            <button class="form__button" name="submit" type="submit">SIGN UP</button>
            <p class="form__text">
                <a class="form__link form__link--button" href="../index.php" id="linkLogin">Already have an account? Sign in.</a>
            </p>
        </form>
    </section>
    <!-- END OF FORM  -->
</div>
</body>
<?php
    include_once('../php/footer.php');
    // include_once('../includes/signup_errors.inc.php');
?>
