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
	"""For comparing two ImageFiles."""
	def __init__(self, imgLeft, imgRight):
		"""
		Initialize data members, and the search area(bounding rect) to the full image.

		Data members:
		imgLeft, imgRight -- The two images to be compared (ImageFile Class)
		surfDiff -- Contains the processing result, the comparison between two images
		track_count -- The number of sequential object finds, if the object is not found it resets to 0
	 	last_seen -- The x,y location of where the object was last seen
		searchArea -- The pygame rect which contains the current look area. 

		Globals (Defined in Config.py).

		"""

		# Images to vars
		self.imgLeft = imgLeft
		self.imgRight = imgRight
		self.surfDiff = None
		
		# Tracking vars
		self.last_seen = (0,0)
		self.track_count = 0

		# Set full screen look area
		self.searchArea = None
		self.setSearchArea()

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
	def setSearchArea(self):
		if self.track_count > 1:
			self.searchArea = pygame.Rect((self.last_seen[0]-MAX_RECT,self.last_seen[1]-MAX_RECT), (MAX_RECT*2, MAX_RECT*2))
		else:
			self.searchArea = pygame.Rect((0,0), (self.imgLeft.width, self.imgLeft.height))

	# Process Methods
	def comparray(self, tolerance):
		"""Use NumPy to compare two SurfArrays, and return a Surface result."""
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
		"""Compare the two images, and return the location of the object found."""

		# Get the search area
		self.setSearchArea()

		# Compare images with a tolerance, and get surface result
		self.surfDiff = self.comparray(tolerance)

		# Process search area of the surface result
		try:
			self.processSearchArea(self.surfDiff)	
		except ValueError:
			# Couldn't find object. Reset.
			print("Error Track.")
			self.last_seen = (0,0)
			self.track_count = 0

		# Return object location
		return self.last_seen

	def processSearchArea(self, surfDiff):
		"""
		Find the center of the largest object dectected.

		Algorithm in English:
		Rather than trying to process the entire image for an object, look only in the area 
		specified by searchArea(bounding rectangle). We assume that the object will not make 
		huge movements between frames, so we don't have to look at the entire image. searchArea 
		is calculated by drawing a box around the area we last saw the the object. The size of 
		this box is specified in the Config.py file. The largest object found in that area will
		be specified as the location of the object.

		"""
		# Subsurface of the main image
		targetSurf = surfDiff.subsurface(self.searchArea)
		# Masks allows us to perform simple operations on the image
		mask = pygame.mask.from_surface(targetSurf)
		# List of bounding rectangles
		rects = mask.get_bounding_rects()

		if len(rects) > 0:
			# Set first rect to the max rect
			maxRect = rects[0]
			maxNum = rects[0].width*rects[0].height 
			# See if any of the other rects are bigger
			for aRect in rects:
				if aRect.width*aRect.height >= maxNum:
					maxRect = aRect
					maxNum = aRect.width*aRect.height
			# Set the largest rect to the position of the object
			# Offset, for the fact that we were looking a subset of the main image
			self.last_seen = (maxRect.centerx + self.searchArea.left, maxRect.centery + self.searchArea.top)
			self.track_count += 1
		else:
			# Didn't find anything in the image comparison
			# Print message and reset
			print("No Track ( Pixels Found: " + str(mask.count()) + ", Frame: " +
			      str(self.imgLeft.frame) + " )")
			self.track_count = 0

	# Annotations 
	def drawBound(self, surface):
		"""Draw the search area on a Surface."""
		pygame.draw.rect(surface, BLUE, self.searchArea, 3)

	def drawBoundCenter(self, surface):
		"""Draw the search area center on a Surface."""
		pygame.draw.circle(surface, GREEN, (self.searchArea.centerx, self.searchArea.centery), 5)