#!/usr/bin/env python
# Filename: viewer.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>rects

# Imports
import math
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

# Load Background and Image Files
background = ImageFile(FOLDER + "/" + "background.jpg")
files = dirFiles(FOLDER)

# File Incrementors 
currentFile = 0
processedFile = -1

# Game Loop Sentinel
notDone = True

# Main Game Loop
while notDone:
	# Fill Display with Black
	screen.fill(BLACK)

	# If Current File is not the Processed File Then Update
	if currentFile != processedFile:
		try:
			# Load Files to ImageFile Objects
			img1 = ImageFile(files[currentFile])
			img2 = ImageFile(files[currentFile+1])

			# Load ImageFile Objects into CompareImages Objects
			frameDiff = CompareImages(img1,img2)
			#backgroundSub = CompareImages(img1,background)

		except IOError as e:
			# Display Screen Error if Images are Missing
			font = pygame.font.SysFont("Consolas", 18)
			tmpImage = font.render("Could not load one or more images.", 1, RED)
		except ValueError as e:
			# Display Screen Error if Images are not Equal Dimensions
			font = pygame.font.SysFont("Consolas", 18)
			tmpImage = font.render("Images are not the same dimensions.", 1, RED)

		else:
			# Compare with Thresholds. Grab a Surface to Display.
			tmpImage = frameDiff.process(TOLERANCE)
			tmpImage = img1.imgFile

			# Fit Window Size to Image
			x, y = screen.get_size()
			if x != tmpImage.get_width() or y != tmpImage.get_height():
				screen = pygame.display.set_mode((tmpImage.get_width(),tmpImage.get_height()))

			# Display Title
			pygame.display.set_caption("PyTrack Viewer. Frame: " + str(currentFile) + "-" + str(currentFile+1))

			# Draw Annotations
			frameDiff.drawBound(tmpImage)
			frameDiff.drawBoundCenter(tmpImage)

			# Change to Correct Frame
			processedFile = currentFile

	# Draw Image
	screen.blit(tmpImage, dest=(0,0))

	# Look For Exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			notDone = False # Goodbye!

	# Get Keys
	key = pygame.key.get_pressed()

	# Change Current Frame Based on Arrow Keys
	# Check to Make Sure the Next Frame is Within Frame Limits
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