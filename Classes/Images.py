#!/usr/bin/env python
# Filename: Images.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import os
import pygame

class ImageFile:
	"""
	An Image File Class.

	Data members:
	imgFile -- Surface containing the image
	width -- Width(px) of the image
	height -- Height(px) of the image

	"""
	def __init__(self, filePath):
		# Load File to PyGame Surface and Get Size Info
		if os.path.exists(filePath):
			# Load Image From File
			self.imgFile = pygame.image.load(filePath)
			# Get Image Size
			self.width = self.imgFile.get_width()
			self.height = self.imgFile.get_height()
		else: 
			raise IOError("Could not find file: '"+ str(filePath) + "'")

	# Accessors
	def getArea(self):
		"""Returns the pixel area of the image."""
		return self.width * self.height
	def getSurfArray(self):
		"""Returns a surfarray."""
		return pygame.surfarray.array2d(self.imgFile)