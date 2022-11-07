<?php
    include_once('../php/header.php');
?>

<!--image slider start-->
<div class="slider">
    <div class="slides">
        <!--radio buttons start-->
        <input type="radio" name="radio-btn" id="radio1">
        <input type="radio" name="radio-btn" id="radio2">
        <input type="radio" name="radio-btn" id="radio3">
        <input type="radio" name="radio-btn" id="radio4">
        <!--radio buttons end-->
        <!--slide images start-->
        <div class="slide first">
            <img src="../img/album_abbeyroad_x820.webp" alt="">
            <div class="slide__info s1">
                <h2>The Beatles</h2>
                <h1>ABBEY ROAD</h1>
                <div class="album_info">
                    Abbey Road is the eleventh studio album released by the English rock band the Beatles. It is the last album the group started recording, although Let It Be was the last album completed before the band's break-up in April 1970.
                </div>
                <div class="album_more_btn"><a href="http://google.com" target="_blank">Find out more!</a></div>
            </div>
        </div>
        <div class="slide">
            <img src="../img/album_bipolar_x1200.png" alt="">
            <div class="slide__info s2">
                <h2>Tame Impala</h2>
                <h1>CURRENTS</h1>
                <div class="album_info">
                    Currents is the third studio album by Australian musical project Tame Impala. It was released on 17 July 2015 by Modular Recordings and Universal Music Australia. In the United States it was released by Interscope Records and Fiction Records, while Caroline International released it in other international regions.
                </div>
                <div class="album_more_btn"><a href="http://google.com" target="_blank">Find out more!</a></div>
            </div>
        </div>
        <div class="slide">
            <img src="../img/album_optimist_x2400.webp" alt="">
            <div class="slide__info s3">
                <h2>FINNNEAS</h2>
                <h1>OPTIMIST</h1>
                <div class="album_info">
                    Optimist is the debut studio album by American singer-songwriter Finneas, released on October 15, 2021, through his record label OYOY, distributed by Interscope Records. The album was entirely produced and written by Finneas.
                </div>
                <div class="album_more_btn"><a href="http://google.com" target="_blank">Find out more!</a></div>
            </div>
        </div>
        <div class="slide">
            <img src="../img/album_wipedout_x1000.png" alt="">
            <div class="slide__info s4">
                <h2>The Neighbourhood</h2>
                <h1>WIPED OUT!</h1>
                <div class="album_info">
                    Wiped Out! is the second studio album by American rock band the Neighbourhood. It was released on October 30, 2015 by Columbia Records. In late 2020, the song "Daddy Issues" went viral on TikTok, along with "Sweater Weather", a song off of the band's debut album I Love You.
                </div>
                <div class="album_more_btn"><a href="http://google.com" target="_blank">Find out more!</a></div>
            </div>
        </div>
        <!--slide images end-->
        <!--automatic navigation start-->
        <div class="navigation-auto">
        <div class="auto-btn1"></div>
        <div class="auto-btn2"></div>
        <div class="auto-btn3"></div>
        <div class="auto-btn4"></div>
        </div>
        <!--automatic navigation end-->
    </div>
    <!--manual navigation start-->
    <div class="navigation-manual">
        <label for="radio1" class="manual-btn"></label>
        <label for="radio2" class="manual-btn"></label>
        <label for="radio3" class="manual-btn"></label>
        <label for="radio4" class="manual-btn"></label>
    </div>
    <!--manual navigation end-->
</div>
<!--image slider end-->

<div class="feedback-container">
    <h1>FEEDBACK OF THE GREAT ARTISTS</h1>
    <div class="fb-circles">
        <div class="feedback-circle c1">
            <h1>Tom Holland</h1>
            <p>OMG! Finneas' new album is f*ckin' amazing.</p>
        </div>
        <div class="feedback-circle c2">
            <h1>Ellen DeGeneres</h1>
            <p>Wiped Out! is a fine wine in a sea of vodka Red Bulls. It seems like they have finally defined their sound as a band. </p>
        </div>
        <div class="feedback-circle c3">
            <h1>James Hetfield</h1>
            <p>Nothing remotely insipid here; rather anger as an energy and top tunes.</p>
        </div>
        <div class="feedback-circle c4">
            <h1>Lady Gaga</h1>
            <p>One of the most beautiful and iconic albums of all time.</p>
        </div>
    </div>
</div>

<div class="about-container">
    <div class="about-container-box">
        <div class="about-us">
            <h1>About Us</h1>
            <p>We are a specialist vinyl record store based in Rammstein, Beatlesland. We started selling relics from the 20's and today we sell almost everything in the music world.</p>
        </div>
        <div class="addr-ctt">
            <h2>Address</h2>
            <p>Central Park West, 758 - Rammstein, Beatlesland.</p>
            <h2>Contact</h2>
            <p>Phone: +1 21 2299-1777</p>
            <p>Email: postmodern_vinylshop@pmvs.com</p>
        </div>
    </div>
</div>

<div class="partners-container">
    <div class="partners-container-box">
        <h1>PARTNERS</h1>
        <div class="partner_logos">
            <img class="partner_logo" src="../img/logo_gibson.png" alt="">
            <img class="partner_logo" src="../img/logo_roland.png" alt="">
            <img class="partner_logo" src="../img/logo_shure.png" alt="">
            <img class="partner_logo" src="../img/logo_cfmartin.png" alt="">
        </div>
    </div>
</div>

<?php
    include_once('../php/footer.php');
?>
