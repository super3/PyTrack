<!DOCTYPE HTML>
<html>
<head>
	<meta charset="utf-8">
	<title>PyTrack</title>
	<link href="css/bootstrap.css" rel="stylesheet" type="text/css">
	<link href="css/bootstrap-responsive.min.css" rel="stylesheet" type="text/css">
	<link href="css/style.css" rel="stylesheet" type="text/css">
	<link href='http://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>  
	<link href='http://fonts.googleapis.com/css?family=Condiment' rel='stylesheet' type='text/css'>
	<link rel="icon" href="img/favicon.ico" type="image/x-icon">
</head>

<body id="home">
	<!-- Start Header -->
	<div id="header">
		<div class="container">
			<div class="row">
				<p class="logo"><a href="index.php">PyTrack</a></p>
				<ul class="navigation">
					<li><a href="features.php">Features &amp; Tutorials</a></li>
					<li><a href="documentation.php">Documentation</a></li>
					<li><a href="downloads.php">Downloads</a></li>
					<li><a href="about.php">About</a></li>
				</ul>
			</div>
			<?php
				function curPageName() {
					return substr($_SERVER["SCRIPT_NAME"],strrpos($_SERVER["SCRIPT_NAME"],"/")+1);
				}
			 	if (curPageName() == "index.php"): 
			 ?>
			<h1>The Simplest Computer Vision Tracking Tool</h1>
			<p class="description">PyTrack is a lightweight and well documented codebase that allows you to do simple computer vision tracking with Python</p>
			<p><a href="downloads.php" class="btn btn-success btn-large">Download Now</a> &nbsp; <a href="features.php" class="btn btn-primary btn-large"> Learn More</a></p>
			<img src="./img/screenshot.png" alt="Screenshot" class="screenshot">
			<?php endif; ?>
		</div>
	</div>
	<!-- End Header -->