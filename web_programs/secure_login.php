<?php
// Database connection
$host = "localhost";
$username = "root";
$password = "";
$database = "studentdb";
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// User input
$user = $_POST['username'];
$pass = $_POST['password'];

// Prepared statement to prevent SQL Injection
$sql = "SELECT * FROM users WHERE username=? AND password=?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ss", $user, $pass);
$stmt->execute();
$result = $stmt->get_result();

// Login validation
if ($result->num_rows > 0) {
    echo "Login Successful";
} else {
    echo "Invalid Username or Password";
}
$stmt->close();
$conn->close();
?>
