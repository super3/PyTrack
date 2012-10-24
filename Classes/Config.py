#!/usr/bin/env python
# Filename: Config.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import os

# Colors Constants
BLACK  = (0,0,0)
WHITE  = (255,255,255)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
PURPLE = (255,0,255)

# Enum Hack (http://stackoverflow.com/a/2182437)
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError
algorithm = Enum(["BACKGROUND_SUBTRACTION", "FRAME_DIFFERENCING"])

# Helpful File Functions
def dirFiles(path):
	"""Return a list of files in a directory."""
	fileList = []
	for r,d,f in os.walk(path):
		for afile in f:
			afile = str(os.path.join(r,afile)).replace("\\", "/")
			fileList.append(afile)
	return fileList
def listToFile(data, filename):
		"""List to text file."""
		with open(filename, 'w') as file:
			for item in data:
				file.write("{}\n".format(item))
def fileExists(path):
	"""Simply checks if a file exists. Prints an error if not."""
	return os.path.exists( path )

# Config Vars
FOLDER = "SampleMosq" # Folder that contains the images you want to process.
TOLERANCE = 840000 # The tolerance of the image comparisons while processing.
MAX_RECT = 20 # Pixel length of the search rectangle.
METHOD = algorithm.FRAME_DIFFERENCING