#!/usr/bin/env python
# Filename: postprocess.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import datetime
from Classes.Images import ImageFile
from Classes.CompareImages import CompareImages
from Classes.Config import *

# Benchmark Class
class Benchmark:
	"""Allows for timing of load and process events."""
	def __init__(self):
		"""
		Data members:
		startTime -- Datetime object at start of benchmark
		numObjs -- Stores amount of objects loaded/processed, so we can get a rate 
		"""
		self.reset()
	def start(self, prefix, numObjs):
		"""Starts the timer."""
		self.startTime = datetime.datetime.now()
		self.numObjs = numObjs
		print(prefix + " " + str(numObjs) + " Images...")
	def end(self):
		"""Ends the timer. Returns seconds took."""
		# Returns Datetime Timedelta
		result =  datetime.datetime.now() - self.startTime
		# Attempt to get a rate, fall back to miliseconds if seconds is less than zero
		try:
			rate = round(self.numObjs / result.seconds, 3)
		except ZeroDivisionError:
			rate = round(self.numObjs / result.microseconds*1000000, 3) # Is Correct?
		print("Done in " + str(result.seconds) + " seconds. (" + str(rate) + " objects/sec)")
		self.reset()
	def reset(self):
		"""Resets the timer."""
		self.startTime = None
		self.numObjs = 0

# PostProcess Class
# This would work really nice with threading.
class PostProcess:
	"""Used to post process a batch of images."""
	def __init__(self, files):
		"""
		Data members:
		files -- A list of the image paths
		queue -- A list of CompareFiles objects to process
		bench -- Benchmark object, so we can see how long it took to load and process
		"""
		# Vars
		self.files = files
		self.queue = []
		self.data = []
		self.bench = Benchmark()
	def load(self):
		"""Load frames from disk to memory, and add them to queue."""
		self.bench.start("Loading", len(self.files))
		for frame in range(len(self.files)):
			self.queue.append( ImageFile(self.files[frame], frame) )
		self.bench.end()
	def process(self):
		"""Process frames in queue/memory."""
		# Start benchmark
		self.bench.start("Processing", len(self.files))
		# Temporary Data Var
		data = []

		# Initialize Compare Object
		if METHOD == algorithm.BACKGROUND_SUBTRACTION:
			# Load Current Frame and Background
			compare = CompareImages( self.queue[0], background )
		elif METHOD == algorithm.FRAME_DIFFERENCING:
			# Load Current Frame and Next Frame
			compare = CompareImages( self.queue[0], self.queue[1] )

		# Process Image Queue
		for frame in self.queue:
			if METHOD == algorithm.BACKGROUND_SUBTRACTION:
				# Load Current Frame
				compare.setLeft( frame )
			elif METHOD == algorithm.FRAME_DIFFERENCING:
				# Load Next Frame
				compare.setRight( frame )
			data.append( compare.process( TOLERANCE ) )

		# End benchmark
		self.bench.end()
		# Write data to file
		listToFile(data, 'data.txt')
	def run(self):
		"""Load and process given files."""
		self.load()
		self.process()

# Main
if __name__ == "__main__":
	process = PostProcess(dirFiles(FOLDER))
	process.run()