#!/usr/bin/env python
# Filename: Images.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import os
import pygame
from PIL import Image as PILimage

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

	# Info
	def printInfo(self):
		"""Prints basic information for the image."""
		print("Image Width: " + str(self.width) + "px")
		print("Image Height: " + str(self.height) + "px")
		print("Image Area: " + str(self.getArea()) + "px")

class ImageBuffer(ImageFile):
	"""Same as ImageFile, just accepts file buffers."""
	def __init__(self, string, size, format):
		# Python PIL
		im = PILimage.frombuffer('L', size, string)
		im2 = im.convert(format).tostring()
		# Load Image From Buffer
		self.imgFile = pygame.image.fromstring(im2, size, format)
		# Get Image Size
		self.width = self.imgFile.get_width()
		self.height = self.imgFile.get_height()
	def getArea(self):
		return ImageFile.getArea(self)
	def getSurfArray(self):
		"""Returns a surfarray."""
		return ImageFile.getSurfArray(self)
