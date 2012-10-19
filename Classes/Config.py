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

# Helpful File Function
def dirFiles(path):
	"""Return a list of files in a directory."""
	fileList = []
	for r,d,f in os.walk(path):
		for afile in f:
			afile = str(os.path.join(r,afile)).replace("\\", "/")
			fileList.append(afile)
	return fileList

# Config Vars
FOLDER = "ant_maze" # Folder that contains the images you want to process.
TOLERANCE = 840000 # The tolerance of the image comparisons while processing.
MAX_RECT = 20 # Pixel length of the search rectangle.
METHOD = algorithm.FRAME_DIFFERENCING

LAST_SEEN = (0,0) # Last know coordinate of the object.
TRACK_COUNT = 0  # Counts the number of times we consecutively found the object.
RESET = 0