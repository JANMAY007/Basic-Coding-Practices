<?php

$successAlert = false;
$errorAlert = false;

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    include 'dbconnect.php';
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $cpassword = $_POST['cpassword'];

    $existSQL = "SELECT * FROM `users` WHERE username='$username'";
    $existResult = mysqli_query($conn, $existSQL);
    $num = mysqli_num_rows($existResult);

    if ($num > 0) {
        $errorAlert = true;
        $errorContent = "Username already exists";
    } else {
        if ($password == $cpassword) {
            $hash = password_hash($password, PASSWORD_DEFAULT);
            $sql = "INSERT INTO `users` (`username`, `email`, `password`, `date`) VALUES ('$username', '$email', '$hash', current_timestamp())";
            $result = mysqli_query($conn, $sql);
            header("location: /project/Home.php");
        } else {
            $errorAlert = true;
            $errorContent = "Passwords do not match";
        }
    }
}

?>

<!doctype html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="signup.css">
    <!-- google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Baloo+Bhaina+2:wght@500&display=swap" rel="stylesheet"/>
    <title>Sign-Up</title>
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

    <?php
    if ($successAlert) {
      echo "
      <div class='success-alert'>
        <span class='fas fa-exclamation-circle'></span>
        <span class='msg'>Success: You are logged in</span>
      </div>
      ";
    }
    if ($errorAlert) {
      echo "
      <div class='alert '>
        <span class='fas fa-exclamation-circle'></span>
        <span class='msg'>Error:   $errorContent </span>
      </div>
      ";
    }
    ?>

<!-- SignUp form -->
<div class="container">
      <div class="form">
        <h1>Sign-up:</h1>
        <form action="/project/signup.php" method="POST">
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
            <div class="form-group">
              <label for="cpassword">Confirm Password:</label>
              <input type="password" id="cpassword" name="cpassword" placeholder="Make sure to enter same password"/>
            </div>
            <button class="btn">Sign-Up</button>
        </form>
      </div>
    </div>
</body>

</html>