#!/usr/bin/env python
# Filename: viewer.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import pygame
from Classes.Images import ImageFile
from Classes.Config import *

# Start PyGame
pygame.init()
 
# Basic PyGame Setup
screen = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

# Get List of Image Files
files = dirFiles(FOLDER)

# File Incrementors 
currentFile = 0
processedFile = -1

# Manual Point Data
if fileExists('checker.txt'):
	data = []
	for line in open( "checker.txt", "r" ).readlines():
		for value in line.split( ' ' ):
			data.append( value )
	print(data)
else:
	data = []
	for i in range(len(files)):
		data.append((-1,-1))

# Game Loop Sentinel
notDone = True
refresh = False

# Main Game Loop
while notDone:
	# Fill Display with Black
	screen.fill(BLACK)

	# If Current File is not the Processed File or a 
	if currentFile != processedFile or refresh:
		# Reset refresh
		refresh = False

		# Get the first frame for display
		tmpImage = ImageFile(files[currentFile]).imgFile

		# Fit Window Size to Image
		x, y = screen.get_size()
		if x != tmpImage.get_width() or y != tmpImage.get_height():
			screen = pygame.display.set_mode((tmpImage.get_width(),tmpImage.get_height()))

		# Display Title
		pygame.display.set_caption("PyTrack Checker. Frame: " + str(currentFile) + "-" + str(currentFile+1))

		# Change to Correct Frame
		processedFile = currentFile

	# Draw Annotation
	pygame.draw.circle(tmpImage, GREEN, (data[currentFile][0], data[currentFile][1]), 5)

	# Draw Image
	screen.blit(tmpImage, dest=(0,0))

	# Check Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			notDone = False # Goodbye!
		elif event.type == pygame.MOUSEBUTTONDOWN:
			data[currentFile] = pygame.mouse.get_pos()
			refresh = True
		elif event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_RIGHT) and (currentFile+1 < len(files)-1):
				currentFile += 1
			elif (event.key == pygame.K_LEFT) and (currentFile > 0):
				currentFile -= 1
			elif (event.key == pygame.K_s):
				listToFile(data, 'checker.txt')

	# Refresh Display
	pygame.display.flip()
	# Limit Frames
	clock.tick(30)