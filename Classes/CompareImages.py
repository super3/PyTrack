#!/usr/bin/env python
# Filename: CompareImages.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
from __future__ import division
import pygame
import numpy
from PIL import Image as PILimage
from Classes.Images import ImageFile
from Classes.Config import *

class CompareImages:
	"""For Comparing Two ImageFiles."""
	def __init__(self, imgLeft, imgRight):
		"""
		Load in two images to compare. 

		Data members:
		imgLeft, imgRight -- The two images to be compared (Images Class)
		minX, maxX, minY, maxY -- Bounds for a bounding box. These are all initialized
								  to the outer limits of the images. They will be adjusted
								  after the two images are compared
		totalConflicts -- Percentage of change between images
		thirdConflicts -- Percentage of change in the top 1/3 of the bounding box (target)
		boundHeight -- Stores the height of the bounding box

		"""
		
		# Check ImageFile Dimensions then Load into CompareImages Object
		if imgLeft.width != imgRight.width or imgLeft.height != imgRight.height:
			raise ValueError("Images are not the same dimensions.")
		else:
			self.imgLeft  = imgLeft
			self.imgRight = imgRight

		# Bounds
		self.minX = imgLeft.width
		self.maxX = -imgLeft.width
		self.minY = imgLeft.height
		self.maxY = -imgLeft.height

		# Info
		self.totalConflicts = 0
		self.targetAbConflicts = 0
		self.boundRect = None
		self.legRect = None
		self.abRect = None

		# Behavior
		self.isMoving = False
		self.abLoc = (0,0)
		self.legs = 0	

	def findBounds(self, x, y):
		"""Based on passed values, this narrows the bounds."""
		if x < self.minX:
			self.minX = x
		if x > self.maxX:
			self.maxX = x	
		if y < self.minY:
			self.minY = y
		if y > self.maxY:
			self.maxY = y

	def comparray(self,a, b, tolerance):
		c = abs(a.__sub__(b))
		c = c.__ge__(tolerance)*255
		im = (PILimage.fromarray(numpy.uint8(c))).convert('RGB').tostring()
		#im2 = im.convert('RGB').tostring()
		im3 = pygame.image.fromstring(im, (640,480), 'RGB') 
		return im3

	def process(self, tolerance):
		"""
		Compare the two images, and return differenced surface.

		Keyword arguments:


		"""
		# Grab Pixel Array's of Both Images
		left = self.imgLeft.getSurfArray()
		right = self.imgRight.getSurfArray()

		# Compare Pixel Arrays (with params) and Get Surface
		#surfDiff = pygame.Surface((640,480))
		surfDiff = self.comparray(left,right,tolerance)
		# Set Alpha to Black
		surfDiff.set_colorkey(BLACK)

		# Create a Mask from the Difference Surface
		mask = pygame.mask.from_surface(surfDiff)

		# Get Total Conflicts as Percent
		self.totalConflicts = round((mask.count() / self.imgLeft.getArea()) * 100, 3)

		# Process Bound and Targets
		try:
			self.processBound(mask)
			self.processLegTarget(surfDiff)
			self.processAbTarget(surfDiff)
		except ValueError:
			print("No Track.")

		# Return Diffed Surface
		return surfDiff

	def processBound(self, mask):
		"""Find the Bounding Box."""
		# Get Bounding Rects
		rects = mask.get_bounding_rects()

		# Find Bounding Box through the Limits of the Bounding Rects
		for aRect in rects:
			self.findBounds(aRect.left, aRect.top)
			self.findBounds(aRect.right, aRect.bottom)

		# Bounding Rect to PyGame Rect
		self.boundRect = pygame.Rect(self.minX, self.minY, abs(self.minX - self.maxX), abs(self.minY - self.maxY))

		# Get Movement Behavior
		if self.totalConflicts > MOVEMENT:
			self.isMoving = True

	def processLegTarget(self, surfDiff):
		"""Find Leg Target."""
		# This should contain the legs.
		targetWidth = abs(self.minX - self.maxX)*0.6
		targetHeight = abs(self.minY - self.maxY)*0.3
		self.legRect = pygame.Rect(self.minX, self.maxY-targetHeight, targetWidth, targetHeight)
		targetSurf = surfDiff.subsurface(self.legRect)

		# Create Mask from the Target Surface
		targetMask = pygame.mask.from_surface(targetSurf)

		# Get Target Conflicts as Perfect
		targetConflicts = round((targetMask.count()/(targetWidth*targetHeight)) * 100, 3)

		# Get Connected Components within componentSize Tolerance 
		self.legs = len(targetMask.connected_components(10))

	def processAbTarget(self, surfDiff):
		"""Find Abdomen Target."""
		# This should contain the abdomen.
		targetWidth = abs(self.minX - self.maxX)*0.1
		targetHeight = abs(self.minY - self.maxY)*0.75
		self.abRect = pygame.Rect(self.maxX-targetWidth, self.maxY-targetHeight, targetWidth, targetHeight)
		targetSurf = surfDiff.subsurface(self.abRect)

		# Create Mask from the Target Surface
		targetMask = pygame.mask.from_surface(targetSurf)

		# Get Target Conflicts as Perfect
		self.targetAbConflicts = round((targetMask.count()/(targetWidth*targetHeight)) * 100, 3)

		# Get Bounding Rects
		rects = targetMask.get_bounding_rects()

		# Highest Bounding Y Var
		highY = 0

		# Find Bottom Most Portion of Bounding Rects
		for aRect in rects:
			if aRect.bottom > highY:
				highY = aRect.bottom

		# Get Abdomen Tip Point:
		self.abLoc = (self.abRect.right, self.abRect.top + highY)

	def printInfo(self):
		"""Print basic information about the image comparison."""
		info = "[Bounds] "
		info += "Min X: " + str(self.minX) + ", "
		info += "Max X: " + str(self.maxX) + ", "
		info += "Min Y: " + str(self.minY) + ", "
		info += "Max Y: " + str(self.maxY)
		info += "\n[Bound Center] " + str(self.boundRect.center)
		info += "\n[Bound Height] " + str(self.boundRect.height) + "px"
		info += "\n[Total Conflicts] " + str(self.totalConflicts) + "%"
		info += "\n[Abdomen Conflicts] " + str(self.targetAbConflicts) + "%"
		info += "\n[Behavior/Moving] " + str(self.isMoving)
		info += "\n[Behavior/Abdomen] " + str(self.abLoc) + " " + str(self.targetAbConflicts>=1)
		info += "\n"
		print(info)

	def drawBoundCenter(self, surface):
		"""Draw the bound centroid on a surface."""
		point = self.boundRect.center
		pygame.draw.circle(surface, GREEN, (point[0], point[1]), 5)

	def drawBound(self, surface):
		"""Draw the bounding box on a surface."""
		pygame.draw.rect(surface, BLUE, self.boundRect, 3)

	def drawLegTarget(self, surface):
		"""Draws the target leg box on a surface."""
		pygame.draw.rect(surface, PURPLE, self.legRect, 3)

	def drawAbTarget(self, surface):
		"""Draws the target abdomen box on a surface, and the center."""
		pygame.draw.rect(surface, PURPLE, self.abRect, 3)
		point = self.abLoc
		if self.targetAbConflicts >= 1:
			pygame.draw.circle(surface, GREEN, (point[0], point[1]), 5)
		else:
			pygame.draw.circle(surface, RED, (point[0], point[1]), 5)
