	<?php include('header.php'); ?>
	<!-- Start Content -->
	<div id="content">
		<div class="container">
			<div class="row">
				<div class="page-header">
				  <h1>Contact</h1>
				</div>
			</div>
			<div class="row">
				<div class="span5">
					<form method="post">
						<fieldset>
							<div class="clearfix">	
								<label>Your Name:</label>
								<input tabindex="1" name="name" type="text" class="span5">	
							</div>
							<div class="clearfix">
								<label>Your Email:</label>
								<input tabindex="2" name="email" type="text" class="span5"> 
							</div>
							<div class="clearfix">
								<label>Your Message:</label>
								<textarea name="comment" rows="8" tabindex="5" class="span5 input-xlarge"></textarea>
							</div>
							<input name="submit" tabindex="5" type="submit" value="Send Message" class="btn btn-success btn-large">
						</fieldset>
					</form>
				</div>
				<div class="span6 offset1">
					<iframe id="contact-map" width="570" height="200" src="https://maps.google.com/maps?ie=UTF8&amp;ll=33.767713,-84.420604&amp;spn=0.507445,1.056747&amp;t=m&amp;z=11&amp;output=embed"></iframe>
					<br /><small><a href="https://maps.google.com/maps?ie=UTF8&amp;ll=33.767713,-84.420604&amp;spn=0.507445,1.056747&amp;t=m&amp;z=11&amp;source=embed" style="color:#0000FF;text-align:left"></a></small>

					<div class="well">
						<h3>Contact:</h3>
						<div class="row">
							<div class="span6">
								<address>
									<br/>
									<p><i class="icon-home"></i> 830 Westview Dr. SW, Atlanta, GA 30314</p>
									<p><i class="icon-envelope"></i> mail@pytrack.com</p>
								</address>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Container -->
	</div>
	<!-- End Content -->
	<?php include('footer.php'); ?>