#!/usr/bin/env python
# Filename: viewer.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import pygame
from Classes.Images import ImageFile
from Classes.CompareImages import CompareImages
from Classes.Config import *

# Start PyGame
pygame.init()
 
# Basic PyGame Setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("PyTrack Viewer.")
clock = pygame.time.Clock()

# Load Background
if METHOD == algorithm.BACKGROUND_SUBTRACTION:
	background = ImageFile(FOLDER + "/background.jpg")
# Get List of Image Files
files = dirFiles(FOLDER)

# File Incrementors 
currentFile = 0
processedFile = -1

# Display Vars
showSource = False
showBound = True
showBoundCenter = True

# Game Loop Sentinel
notDone = True
refresh = False

# Initialize Compare Object
if METHOD == algorithm.BACKGROUND_SUBTRACTION:
	# Load Current Frame and Background
	compare = CompareImages( ImageFile(files[0], 0), background )
elif METHOD == algorithm.FRAME_DIFFERENCING:
	# Load Current Frame and Next Frame, currentFile
	compare = CompareImages( ImageFile(files[0], 0), ImageFile(files[1], 1) )

# Main Game Loop
while notDone:
	# Fill Display with Black
	screen.fill(BLACK)

	# Redraw. Switch Between Source Image Surface, and Diffed Image.
	if refresh:
		# Reset Refresh
		refresh = False

		# If showSource is enabled then process the frames, and get the diffed result for display
		if showSource:
			tmpImage = compare.surfDiff
		# Else then process the frames, but get the first frame for display
		else:
			tmpImage = ImageFile(files[currentFile]).imgFile

	# If Current File is not the Processed File or a 
	if currentFile != processedFile:
		

		# Get the Images Needed Based on the Algorithm
		try:
			if METHOD == algorithm.BACKGROUND_SUBTRACTION:
				# Load Current Frame
				compare.setLeft( ImageFile(files[currentFile], currentFile) )

			elif METHOD == algorithm.FRAME_DIFFERENCING:
				# Load Next Frame
				compare.setRight( ImageFile(files[currentFile+1], currentFile+1) )

		except IOError as e:
			# Display Screen Error if Images are Missing
			font = pygame.font.SysFont("Consolas", 18)
			tmpImage = font.render("Could not load one or more images.", 1, RED)
		except ValueError as e:
			# Display Screen Error if Images are not Equal Dimensions
			font = pygame.font.SysFont("Consolas", 18)
			tmpImage = font.render("Images are not the same dimensions.", 1, RED)

		else:
			# Do Compare Operation
			compare.process(TOLERANCE)

			# If showSource is enabled then process the frames, and get the diffed result for display
			if showSource:
				tmpImage = compare.surfDiff
			# Else then process the frames, but get the first frame for display
			else:
				tmpImage = ImageFile(files[currentFile]).imgFile

			# Fit Window Size to Image
			x, y = screen.get_size()
			if x != tmpImage.get_width() or y != tmpImage.get_height():
				screen = pygame.display.set_mode((tmpImage.get_width(),tmpImage.get_height()))

			# Display Title
			pygame.display.set_caption("PyTrack Viewer. Frame: " + str(currentFile) + "-" + str(currentFile+1))

			# Change to Correct Frame
			processedFile = currentFile

	# Draw Annotations in Enabled
	if showBound:
		compare.drawBound(tmpImage)
	if showBoundCenter:
		compare.drawBoundCenter(tmpImage)

	# Draw Image
	screen.blit(tmpImage, dest=(0,0))

	# Look For Exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			notDone = False # Goodbye!
		elif event.type == pygame.KEYDOWN:
			# Get ready to refresh display
			refresh = True
			# Check for display hotkeys
			if event.key == pygame.K_s:
				# Controls which surface to display
				showSource = not showSource
			elif event.key == pygame.K_1:
				# Toggle Bounding Box
				showBound = not showBound
			elif event.key == pygame.K_2:
				# Toggle Bounding Box Center
				showBoundCenter = not showBoundCenter
			# No hotkeys selected, so don't refresh
			else:
				refresh = False

	# Get Keys
	key = pygame.key.get_pressed()

	# Change current frame based on the arrow keys, and check 
	# to make sure the next frame is within the frame limits
	if key[pygame.K_RIGHT] and currentFile+1 < len(files)-1:
		currentFile += 1
	elif key[pygame.K_LEFT] and currentFile-1 > 0:
		currentFile -= 1
	elif key[pygame.K_UP] and currentFile+10 < len(files)-1:
		currentFile += 10
	elif key[pygame.K_DOWN] and currentFile-10 > 0:
		currentFile -= 10

	# Refresh Display
	pygame.display.flip()
	# Limit Frames
	clock.tick(30)