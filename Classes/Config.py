#!/usr/bin/env python
# Filename: Config.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
import os

# Constant Colors
WHITE  = (255,255,255)
BLACK  = (0,0,0)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0,255)
PURPLE = (255,0,255)

# Config Vars
# FOLDER -- Folder that contains the images you want to process.
# TOLERANCE -- The tolerance of the image comparisons while processing.
# MOVEMENT -- Minimum amount of image change(%) that signifies movement.
FOLDER = "MosqTop"
TOLERANCE = 640000
MAX_RECT = 15
LAST_SEEN = (25,25)
TRACK_COUNT = 0
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