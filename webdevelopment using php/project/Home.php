<?php

session_start();
if (!(isset($_SESSION['loggedin'])) || $_SESSION['loggedin'] != true)  
{
    header("location: /project/login.php");  
    exit;    
}
?>

<!-- this is php code for contact form of the footer  -->
<?php

$successAlert = false;

if($_SERVER['REQUEST_METHOD'] == 'POST'){
include 'contact_dbconnect.php';
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $message = $_POST['message'];

    $sql = "INSERT INTO `contact` (`name`, `email`, `phone`, `message`, `date`) VALUES ('$name', '$email', '$phone', '$message', current_timestamp());";
    $result = mysqli_query($conn , $sql);
    $successAlert = true; // Success Alert
}

?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Best online food delievery services</title>
    <link rel="stylesheet" href="style.css" />

    <!-- jquery cdn -->
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
    <!-- flickity link -->
    <link rel="stylesheet" href="https://unpkg.com/flickity@2/dist/flickity.min.css"/>
    <!-- flickity JavaScript -->
    <script src="https://unpkg.com/flickity@2/dist/flickity.pkgd.min.js"></script>
    <!-- bootstrap css -->
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous"> -->
    <!-- google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@500&display=swap" rel="stylesheet"/>
 <!-- FONT_AWESOME    -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.13.0/css/all.min.css" rel="stylesheet">
  </head>
  <body>

<!-- NAVIGATION BAR -->
    <nav class="navbar">
      <div class="logo">
        <img src="/project/pics/logo.png" alt=""/>
        <h2>Mystic Grill</h2>
      </div>
      <ul>
        <li class="item"><a href="/project/Home.php">Home</a></li>
        <li class="item"><a href="#">About Us</a></li>
        <li class="item"><a href="#">Services</a></li>
        <li class="item"><a href="#">Contact Us</a></li>
      </ul>
      <div class="right">
        <a href="/project/logout.php" class="logout">Logout</a>
      </div>    
    </nav>


<!-- search bar -->
    <div class="search-box">
        <input type="text" class="search-txt" name="" placeholder="Type to search">
        <a href="#" class="search-btn"><i class="fas fa-search"></i></a>
    </div>


<!-- CROUSEL SECTION -->
    <section class="carousel-container">
        <div class="carousel" data-flickity='{"wrapAround": true , "autoPlay": true}'>
            <div class="carousel-cell"><img src="/project/pics/carousel1.jfif" alt="" /></div>
            <div class="carousel-cell"><img src="/project/pics/carousel6.jpg" alt="" /></div>
            <div class="carousel-cell"><img src="/project/pics/carousel3.jpg" alt="" /></div>
            <div class="carousel-cell"><img src="/project/pics/carousel4.webp" alt="" /></div>
            <div class="carousel-cell"><img src="/project/pics/carousel2.jfif" alt="" /></div>
        </div>
    </section>

<!-- SERVICE SECTION -->
    <section class="service-container">
        <h1 class="h-primary center">Our services</h1>
        <div class="services">
            <div class="box">
                <img src="/project/pics/card1.png" alt="">
                <h2 class="h-secondary center">Food Catering</h2>
                <p class="center">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus iste
                    fugit soluta nisi, quo nam error assumenda consequuntur. Nostrum
                    cumque mollitia corrupti, tenetur commodi reiciendis error id
                    debitis! Id, velit.
                   </p>
               </div>
            <div class="box">
                <img src="/project/pics/card2.png" alt="">
                <h2 class="h-secondary center">Food Ordering</h2>
                <p class="center">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus iste
                    fugit soluta nisi, quo nam error assumenda consequuntur. Nostrum
                    cumque mollitia corrupti, tenetur commodi reiciendis error id
                    debitis! Id, velit.
                </p>
            </div>
            <div class="box">
                <img src="/project/pics/card3.jpg" alt="">
                <h2 class="h-secondary center">Bulk Order</h2>
                <p class="center">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus iste
                    fugit soluta nisi, quo nam error assumenda consequuntur. Nostrum
                    cumque mollitia corrupti, tenetur commodi reiciendis error id
                    debitis! Id, velit.
                </p>
            </div>
            <div class="box">
                <img src="/project/pics/card4.png" alt="">
                <h2 class="h-secondary center">Party Pack</h2>
                <p class="center">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus iste
                    fugit soluta nisi, quo nam error assumenda consequuntur. Nostrum
                    cumque mollitia corrupti, tenetur commodi reiciendis error id
                    debitis! Id, velit.
                </p>
            </div>
      </div>
    </section>

<!-- CLIENT SECTION -->
    <section class="client-section">
        <h1 class="h-primary center">Our Clients</h1>
            <div class="client">
                <div class="client-item"><img src="/project/pics/client1.png" alt=""></div>
                <div class="client-item"><img src="/project/pics/client2.png" alt=""></div>
                <div class="client-item"><img src="/project/pics/client3.png" alt=""></div>
                <div class="client-item"><img src="/project/pics/client4.png" alt="" height="400px"></div>
                <div class="client-item"><img src="/project/pics/client5.png" alt=""></div>
            </div>
    </section>

<!-- CONTACT SECTION -->
    <section class="contact">
        <?php
            if ($successAlert) {
                echo "
                    <div class='alert '>
                      <span class='fas fa-exclamation-circle'></span>
                      <span class='msg'>Success! Your response has been saved</span>
                    </div>";
            }
        ?>

        <h1 class="h-primary center">Contact Us</h1>
        <div class="contact-box">
            <!-- TEST AREA -->
            <div class="text">
                <h2 class="h-tertiary ">WE'RE OPEN:</h2>
                <p>Monday - Saturday</p>
                <p>12PM - 9PM</p><br>
                <p>B-100 Pratap Nagar<br>
                    Chittorgarh , Rajasthan 312001
                </p><br>
                <p>Tel: 123-456-7890<br>
                    Email: MysticGrill@gmail.com</p>
            </div>

            <!-- CONTACT FORM -->
            <form action="/project/Home.php" method="POST">
                <div class="form-group">
                    <label for="name">Name: </label>
                    <input type="text" id="name" name="name" placeholder="Enter your name" required >
                </div>
                <div class="form-group">
                    <label for="email">Email: &nbsp;</label>
                    <input type="email" id="email" name="email" placeholder="Enter your email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Phone:</label>
                    <input type="phone" id="phone" name="phone" placeholder="Enter your Number" required>
                </div>
                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea name="message" id="message" name="message" cols="30" rows="3" placeholder="Enter your message..." required></textarea>
                </div>
                <button class="btn">Submit</button>
            </form>  
            <!-- Social Media Handles -->
            <div class="social-media">
                <h1 class="h-tertiary ">Follow US:</h1>
                <a href="https://www.instagram.com/vaibhavpaliwal620/" target="black"><img src="/project/pics/instagram.png" alt="img"></a>
                <a href="https://www.linkedin.com/in/vaibhav-paliwal-a47bb7207/" target="black"><img src="/project/pics/linkedIn.png" alt="img"></a>
                <a href="#"><img src="/project/pics/whatsapp.png" alt="img" target="black"></a>
                <a href="#"><img src="/project/pics/facebook.png" alt="img" target="black"></a>
            </div>
        </div>
    </section>

<!-- FOOTER -->
    <footer>
        <div class="center">
            Copyright &copy; www.MysticGrill.com All rights reserved!
        </div>
    </footer>
        
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
  </body>
</html>
