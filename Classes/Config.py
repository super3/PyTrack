#!/usr/bin/env python
# Filename: Config.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import os

# Colors Constants
WHITE  = (255,255,255)
BLACK  = (0,0,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
PURPLE = (255,0,255)

# Config Vars
FOLDER = "ant_maze" # Folder that contains the images you want to process.
TOLERANCE = 840000 # The tolerance of the image comparisons while processing.
MAX_RECT = 20 # Pixel length of the search rectangle.
LAST_SEEN = (0,0) # Last know coordinate of the object.
TRACK_COUNT = 0  # Counts the number of times we consecutively found the object.
RESET = 0

# Helpful File Function
def dirFiles(path):
	"""Return a list of files in a directory."""
	fileList = []
	for r,d,f in os.walk(path):
		for afile in f:
			afile = str(os.path.join(r,afile)).replace("\\", "/")
			fileList.append(afile)
	return fileList