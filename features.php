	<?php include('header.php'); ?>
	<!-- Start Content -->
	<div id="content">
		<div class="container">
			<div class="row fix">
				<div class="page-header">
				  <h1>Features &amp; Tutorials</h1>
				</div>
				<div class="tabbable"> <!-- Only required for left/right tabs -->
				  <ul class="nav nav-tabs">
					<li class="active"><a href="#tab1" data-toggle="tab"><strong>Overview</strong></a></li>
					<li><a href="#tab2" data-toggle="tab"><strong>Object Tracking Tutorial</strong></a></li>
					<li><a href="#tab3" data-toggle="tab"><strong>Manual Annotations Tutorial</strong></a></li>
					<li><a href="#tab4" data-toggle="tab"><strong>Batch Processing Tutorial</strong></a></li>		
				  </ul>
				  <div class="tab-content">
					<div class="tab-pane active" id="tab1">
					  <div class="row">
						<div class="span4">
							<h3>Object Tracking</h3>
							<p><img src="img/objtracking.png" alt="Object Tracking"></p>
							<p>
								Simple object tracking is the core feature of PyTrack. Using basic <a href="javascript://">frame differencing</a> and <a href="javascript://">background subtraction</a>
								computer vision algorithms, PyTrack can accurately track single	objects in clean visual environments. The location of the tracked object is returned in (x,y) coordinates.
								In the current version of PyTrack, all data is post processed and returned as a data file. 
							</p>
						</div>
						<div class="span4">
							<h3>Manual Annotations</h3>
							<p><img src="img/mantracking.png" alt="Manual Annotations"></p>
							<p>
								In order to verify the accuracy of the of the object tracker, PyTrack also allows manual annotations of the image data. By clicking on the object that you want to track 
								for each frame of your image data you get a highly accurate track on your object. You can compare this data to the automatic data produced by PyTrack, and adjust the 
								configurations to more accurate data. 
							</p>
						</div>
						<div class="span4">
							<h3>Batch Processing</h3>
							<p><img src="img/batchtracking.png" alt="Color Detection"></p>
							<p>
								After you are satisfied with the accuracy of PyTrack for your data, you can use the batch processing script to process large amounts of that image data. You can set all
								options that you want, and PyTrack will simply return the data file when it is done.
						    </p>
						</div>
					  </div>
					</div>
					<div class="tab-pane" id="tab2">
						<div class="row">
							<div class="span6">
								<h3>Setup</h3>
								<p>
									If you have not already, please review <a href="documentation.php">Getting Started</a> in the <a href="documentation.php">Documentation</a>.
								</p>
								<h3>Keyboard Shortcuts</h3>
								<table class="table table-bordered table-striped">
									<colgroup>
										<col class="span2">
										<col class="span4">
									</colgroup>
									<thead>
										<tr>
											<th>Key</th>
											<th>Description</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>
												<code>&larr; or &rarr;</code>
											</td>
											<td>
												Move forward or back 1 frame.
											</td>
										</tr>
										<tr>
											<td>
												<code>&uarr; or &darr;</code>
											</td>
											<td>
												Move forward or back 10 frames.
											</td>
										</tr>
										<tr>
											<td>
												<code>S</code>
											</td>
											<td>
												Toggle between source images and PyTrack's pixel differencing.
											</td>
										</tr>
										<tr>
											<td>
												<code>1</code>
											</td>
											<td>
												Toggle search area box around object.
											</td>
										</tr>
										<tr>
											<td>
												<code>2</code>
											</td>
											<td>
												Toggle search area box center.
											</td>
										</tr>
									</tbody>
								</table>
							</div>
							<div class="span6">
								<h3>Video</h3>
								<iframe width="560" height="315" src="http://www.youtube.com/embed/3f7l-Z4NF70" frameborder="0" allowfullscreen></iframe>
							</div>
					    </div>
					</div>
					<div class="tab-pane" id="tab3">
					 <div class="row">
					  		<div class="span6">
								<h3>Setup</h3>
								<p>
									If you have not already, please review <a href="documentation.php">Getting Started</a> in the <a href="documentation.php">Documentation</a>.
								</p>
								<h3>Keyboard Shortcuts</h3>
								<table class="table table-bordered table-striped">
									<colgroup>
										<col class="span2">
										<col class="span4">
									</colgroup>
									<thead>
										<tr>
											<th>Key</th>
											<th>Description</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>
												<code>&larr; or &rarr;</code>
											</td>
											<td>
												Move forward or back 1 frame.
											</td>
										</tr>
										<tr>
											<td>
												<code>S</code>
											</td>
											<td>
												Save current data.
											</td>
										</tr>
									</tbody>
								</table>	
							</div>
							<div class="span6">
								<h3>Video</h3>
								<iframe width="560" height="315" src="http://www.youtube.com/embed/3f7l-Z4NF70" frameborder="0" allowfullscreen></iframe>
							</div>
					  	</div>
					</div>
					<div class="tab-pane" id="tab4">
						<div class="row">
							<div class="span6">
								<h3>Setup</h3>
								<p>
									If you have not already, please review <a href="documentation.php">Getting Started</a> in the <a href="documentation.php">Documentation</a>.
								</p>
								<h3>Command Arguments</h3>
								<table class="table table-bordered table-striped">
									<colgroup>
										<col class="span1">
										<col class="span3">
										<col class="span2">
									</colgroup>
									<thead>
										<tr>
											<th>Argument</th>
											<th>Usage</th>
											<th>Description</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>
												<code>-a</code>
											</td>
											<td>
												<code>BackSub</code> or <code>FrameDiff</code> <br/> Default: FrameDiff
											</td>
											<td>
												Computer vision algorithm used. 
											</td>
										</tr>
										<tr>
											<td>
												<code>-f</code>
											</td>
											<td>
												Valid filename or filename path. <br/> Example: <code>folder/filename.txt</code> <br/> Default: /data.txt
											</td>
											<td>
												Save data to this file location.
											</td>
										</tr>
										<tr>
											<td>
												<code>-s</code>
											</td>
											<td>
												Any frame number. <br/> Default: 0
											</td>
											<td>
												Start frame to process(inclusive).
											</td>
										</tr>
										<tr>
											<td>
												<code>-e</code>
											</td>
											<td>
												Any frame number. <br/> Default: End frame
											</td>
											<td>
												End frame to process(inclusive).
											</td>
										</tr>
										<tr>
											<td>
												<code>-m</code>
											</td>
											<td>
												1 to 10,000 images. <br/> Default: 500
											</td>
											<td>
												Number of images to load into memory at a time.
											</td>
										</tr>
									</tbody>
								</table>	
							</div>
							<div class="span6">
								<h3>Video</h3>
								<iframe width="560" height="315" src="http://www.youtube.com/embed/3f7l-Z4NF70" frameborder="0" allowfullscreen></iframe>
							</div>
						</div>
					</div>
				  </div>
				</div>
			</div>
		</div>
	</div>
	<!-- End Content -->
	<?php include('footer.php'); ?>