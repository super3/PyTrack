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
		"""Process frames in queue/memory."""
		data = []
		self.bench.start("Processing", len(self.files))
		for obj in self.queue:
			obj.process( TOLERANCE )
			global LAST_SEEN
			data.append(LAST_SEEN)
			self.queue.remove(obj)
		self.bench.end()
		self.toFile(data)
	def toFile(self,data):
		f = open('data.txt', 'w')
		for i in data:
			f.write(str(i) + "\n")
		f.close()
	def run(self):
		"""Load and process given files."""
		self.load()
		self.process()

# Main
if __name__ == "__main__":
	process = PostProcess(dirFiles(FOLDER))
	process.run()