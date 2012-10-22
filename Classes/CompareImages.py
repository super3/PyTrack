#!/usr/bin/env python
# Filename: CompareImages.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import pygame
from Classes.Images import ImageFile
from Classes.Config import *

class CompareImages:
	"""For Comparing Two ImageFiles."""
	def __init__(self, imgLeft, imgRight):
		"""
		Check if these images are the same size.
		Get global. These tell the last known location of the object, as well as how good
		the track on the object is.

		Data members:
		imgLeft, imgRight -- The two images to be compared (ImageFile Class)
		boundRect -- The pygame rect which contains the current look area. Start with full area

		Globals (Defined in Config.py).

		"""

		# Images to Vars
		self.imgLeft = imgLeft
		self.imgRight = imgRight
		# Blank Surface for Diffed Result
		self.surfDiff = pygame.Surface((0, 0))
		
		# Tracking Vars
		self.last_seen = (0,0)
		self.track_count = 0

		# Set Full Screen Bounding Rect
		self.setBoundRect()

	# Image Change Methods
	def setLeft(self, pySurface):
		"""Set the left image."""
		self.imgLeft = pySurface
	def setRight(self, pySurface):
		"""Swap and set the right image."""
		self.imgLeft = self.imgRight
		self.imgRight = pySurface
	def compareDimen(self):
		"""Make sure the compared images are the same size."""
		return (self.imgLeft.width != self.imgRight.width) or (self.imgLeft.height != self.imgRight.height)
	def setBoundRect(self):
		if self.track_count > 1:
			self.boundRect = pygame.Rect((self.last_seen[0]-MAX_RECT,self.last_seen[1]-MAX_RECT), (MAX_RECT*2, MAX_RECT*2))
		else:
			self.boundRect = pygame.Rect((0,0), (self.imgLeft.width, self.imgLeft.height))
			

	# Process Methods
	def comparray(self, tolerance):
		"""Use NumPy to Compare Two SurfArray, and Return a Surface."""
		# Turn the two PyGame surface objects into SurfArrays
		left = self.imgLeft.getSurfArray()
		right = self.imgRight.getSurfArray()
		# This is NumPy magic...
		diff = abs(left.__sub__(right))
		diff = diff.__ge__(tolerance)*255
		# Get back a usable PyGame surface
		surface = pygame.surfarray.make_surface(diff)
		# Get back transparency
		surface.set_colorkey(BLACK)
		return surface

	def process(self, tolerance):
		"""Compare the two images, and Return diffed Surface."""
		self.setBoundRect()

		# Compare Pixel Surfs (with params) and Get Surface
		surfDiff = self.comparray(tolerance)

		# Process Bounds
		try:
			self.processBound(surfDiff)	
		except ValueError:
			# Couldn't find object. Reset.
			print("Error Track.")
			self.last_seen = (0,0)
			self.track_count = 0

		# Return Diffed Surface
		return surfDiff

	def processBound(self, surfDiff):
		"""Find the Bounding Box."""
		# Check Current Area for Movement and Generate Surface+Mask
		targetSurf = surfDiff.subsurface(self.boundRect)
		mask = pygame.mask.from_surface(targetSurf)

		# TODO: Find Largest Connected Component
		rects = mask.get_bounding_rects()
		if len(rects) > 0:
			maxRect = rects[0]
			maxNum = rects[0].width*rects[0].height 
			for aRect in rects:
				if aRect.width*aRect.height >= maxNum:
					maxRect = aRect
					maxNum = aRect.width*aRect.height
			# Set self.last_seen to that Largest Component's Center
			self.last_seen = (maxRect.centerx + self.boundRect.left, maxRect.centery + self.boundRect.top)
			self.track_count += 1
		else:
			# Set Track as Bad
			print("No Track ( Pixels " + str(mask.count()) + " )")
			self.track_count = 0

	# Annotations 
	def drawBound(self, surface):
		"""Draw the bounding box on a surface."""
		pygame.draw.rect(surface, BLUE, self.boundRect, 3)

	def drawBoundCenter(self, surface):
		"""Draw the bounding box center on a surface."""
		pygame.draw.circle(surface, GREEN, (self.boundRect.centerx, self.boundRect.centery), 5)