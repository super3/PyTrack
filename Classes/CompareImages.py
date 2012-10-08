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
		Load in two images to compare. 
		Assuming these images are loaded correctly, and are the same size.

		Data members:
		imgLeft, imgRight -- The two images to be compared (ImageFile Class)
		minX, maxX, minY, maxY -- Bounds for a bounding box. These are all initialized
								  to unreasonable values that will be adjusted after
								  the two images are compared
		boundRect -- The pygame rect which contains the current look area. Start with full area.
		trackCount -- Counts the number of times we found stuff.

		"""

		# Check ImageFile Dimensions then Load into CompareImages Object
		if imgLeft.width != imgRight.width or imgLeft.height != imgRight.height:
			raise ValueError("Images are not the same dimensions.")
		else:
			self.imgLeft  = imgLeft
			self.imgRight = imgRight

		# Get Globals
		global LAST_SEEN
		global TRACK_COUNT

		# Info
		if TRACK_COUNT > 20:
			#print(LAST_SEEN)
			self.boundRect = pygame.Rect((LAST_SEEN[0]-MAX_RECT,LAST_SEEN[1]-MAX_RECT), (MAX_RECT*2, MAX_RECT*2))

			#self.boundRect = pygame.Rect((0,0), (imgLeft.width, imgLeft.height))
		else:
			self.boundRect = pygame.Rect((0,0), (imgLeft.width, imgLeft.height))

	def comparray(self, tolerance):
		"""Use NumPy to Compare Two SurfArray, and Return a Surface."""
		left = self.imgLeft.getSurfArray()
		right = self.imgRight.getSurfArray()
		diff = abs(left.__sub__(right))
		diff = diff.__ge__(tolerance)*255
		surface = pygame.surfarray.make_surface(diff)
		surface.set_colorkey(BLACK)
		return surface

	def process(self, tolerance):
		"""Compare the two images, and Return diffed Surface."""
		# Compare Pixel Surfs (with params) and Get Surface
		surfDiff = self.comparray(tolerance)

		# Process Bounds
		try:
			self.processBound(surfDiff)	
		except ValueError:
			print("Error Track.")
			global LAST_SEEN
			global TRACK_COUNT
			LAST_SEEN = (0,0)
			TRACK_COUNT = 0

		# Return Diffed Surface
		return surfDiff

	def processBound(self, surfDiff):
		"""Find the Bounding Box."""
		# Get Globals
		global LAST_SEEN
		global TRACK_COUNT
		global RESET

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
			# Set LAST_SEEN to that Largest Component's Center
			LAST_SEEN = (maxRect.centerx + self.boundRect.left, maxRect.centery + self.boundRect.top)
			TRACK_COUNT += 1
			RESET = 0
		else:
			# Set Track as Bad
			print("No Track (" + str(mask.count()) + ")")
			if TRACK_COUNT >= 21:
				RESET += 1

			if RESET >= 2:
				TRACK_COUNT = 0


		#print(TRACK_COUNT)

	def drawBound(self, surface):
		"""Draw the bounding box on a surface."""
		pygame.draw.rect(surface, BLUE, self.boundRect, 3)

	def drawBoundCenter(self, surface):
		"""Draw the bound center on a surface."""
		pygame.draw.circle(surface, GREEN, (self.boundRect.centerx, self.boundRect.centery), 5)