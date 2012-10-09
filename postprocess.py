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
		Initializes a Benchmark Object.
		Note: It will break if it grabs a time less than a second. 

		Data members:
		startTime -- Datetime object at start of benchmark.
		num -- Stores amount of objects loaded/processed so we can get a rate 
		"""
		self.reset()
	def start(self, prefix, num):
		"""Starts the timer."""
		self.startTime = datetime.datetime.now()
		self.num = num
		print(prefix + " " + str(num) + " Images...")
	def end(self):
		"""Ends the timer. Returns seconds took."""
		# Returns Datetime Timedelta
		result =  datetime.datetime.now() - self.startTime
		# Attempt to get a rate, fall back to miliseconds if seconds is less than zero
		try:
			rate = round(self.num / result.seconds, 3)
		except ZeroDivisionError:
			rate = round(self.num / result.microseconds*1000000, 3)
		print("Done in " + str(result.seconds) + " seconds. (" + str(rate) + " objects/sec)")
		self.reset()
		return result.seconds
	def reset(self):
		"""Resets the timer."""
		self.startTime = None
		self.num = 0

# PostProcess Class
# This would work really nice with threading.
class PostProcess:
	"""Used to process a batch of images."""
	def __init__(self, files):
		"""
		Initializes a PostProcess Object.

		Data members:
		files -- A list of the image paths
		queue -- A list of CompareFiles objects to process
		bench -- Benchmark object for getting processing and load times
		"""
		# Queue Var
		self.files = files
		self.queue = []
		# Benchmark Object
		self.bench = Benchmark()
	def load(self):
		"""Load frames from disk to memory, and add them to queue."""
		self.bench.start("Loading", len(self.files))
		for i in range(len(self.files)-1):
			img1 = ImageFile(self.files[i])
			img2 = ImageFile(self.files[i+1])
			self.queue.append( CompareImages(img1,img2) )
		self.bench.end()
	def process(self):
		"""Process frames in queue."""
		stuff = []
		self.bench.start("Processing", len(self.files))
		for obj in self.queue:
			obj.process( TOLERANCE )
			global LAST_SEEN
			stuff.append(LAST_SEEN)
			self.queue.remove(obj)
		self.bench.end()
		self.toFile(stuff)
	def toFile(self,stuff):
		f = open('testdata.txt', 'w')
		for i in stuff:
			f.write(str(i) + "\n")
		f.close()
	def run(self):
		"""Load and process selected frames."""
		self.load()
		self.process()

# Main
if __name__ == "__main__":
	process = PostProcess(dirFiles(FOLDER))
	process.run()