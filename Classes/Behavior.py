#!/usr/bin/env python
# Filename: Behavior.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# Imports
from Classes.Config import *

# Functions
def isMoving(totalConflicts):
	"""Returns bool if within movement threshold."""
	if totalConflicts <= MOVEMENT:
		return False
	return False
def abTip(targetConflicts, maxX, minY):
	"""Returns point of abdomen tip, or None if empty."""
	if targetConflicts > 20:
			return (maxX, minY)
	return None