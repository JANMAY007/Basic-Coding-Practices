<?php
$errorAlert = false;

if($_SERVER["REQUEST_METHOD"] == "POST"){
  include "dbconnect.php";
  $username = $_POST['username'];
  $email = $_POST['email'];
  $password = $_POST['password'];

  $sql = "SELECT * FROM `users` WHERE username='$username'";  
  $result = mysqli_query($conn, $sql);  
  $num = mysqli_num_rows($result);

  if($num == 1){
    while ($row = mysqli_fetch_assoc($result)) 
        {
            if (password_verify($password, $row['password'])) {
                session_start();
                $_SESSION['username'] = $username;
                $_SESSION['loggedin'] = true;
                header("location: /project/Home.php");
            }
            else {
                $errorAlert = true;
                $errorContent = "Invalid Credentials";
            }
        }
  }
  else {
    $errorAlert = true;
    $errorContent = "Invalid Credentials";
  }
}
?>

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Login</title>
<!-- google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@500&display=swap" rel="stylesheet"/>
<!-- Login Page CSS -->
<link rel="stylesheet" href="login.css">

<script src="https://kit.fontawesome.com/a076d05399.js"></script>
<script   src="https://code.jquery.com/jquery-3.6.0.js"></script>
  </head>

  <body>

    <!-- navigation bar -->
    <nav class="navbar">
          <div class="left">
            <img src="/project/pics/logo.png" alt="" />
            <h2>Mystic Grill</h2>
          </div>
              <ul>
                <li class="item"><a href="/project/Home.php">Home</a></li>
                <li class="item"><a href="/project/login.php">login</a></li>
                <li class="item"><a href="/project/signup.php">Signup</a></li>
              </ul>
        </nav>

   <!-- Error alert -->
    <?php

    if ($errorAlert) {
      echo "
      <div class='alert '>
        <span class='fas fa-exclamation-circle'></span>
        <span class='msg'>Error: Invalid Credentials</span>
      </div>
      ";
    }
    ?>
 

    <div class="container">
      <div class="form">
        <h1>Login:</h1>
        <form action="/project/login.php" method="POST">
            <div class="form-group">
              <label for="name">username: </label>
              <input type="text" id="username" name="username" placeholder="enter your name"/>
            </div>
            <div class="form-group">
              <label for="email">Email: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</label>
              <input type="email" id="email" name="email" placeholder="enter your email"/>
            </div>
            <div class="form-group">
              <label for="password">Password:</label>
              <input type="password" id="password" name="password" placeholder="enter your password"/>
            </div>
            <button class="button">Login</button>
        </form>
      </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

  </body>
</html>
