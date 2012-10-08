#!/usr/bin/env python
# Filename: realtime.py
# Project Github: http://github.com/super3/PyTrack
# Author: Shawn Wilkinson <me@super3.org>
# Author Website: http://super3.org/
# License: GPLv3 <http://gplv3.fsf.org/>

# PyTrack Imports
import pygame
from PIL import Image as PILimage
from Classes.Images import ImageFile
from Classes.Images import ImageBuffer
from Classes.CompareImages import CompareImages
from Classes.Config import *

# Ros Imports
import rospy
import roslib; roslib.load_manifest('moth_3d')
from sensor_msgs.msg import Image
from std_msgs.msg import String
from moth_3d.msg import AbPosition

# Loop Vars
file1 = None
file2 = None
back = ImageFile("background.jpg")
start = True

# ROS Publisher(s)
pub = rospy.Publisher('/bev/abPos', AbPosition)

# Basic PyGame Setup
pygame.init()
screen = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()

# Functions
def callback(data):
	# Get Vars
	global file1
	global file2
	global back
	global start
	global pub
	global screen
	global clock

	# Fill Both ImageBuffer Objects Just After Start
	if start:
		print(pygame.image.get_extended())
		file1 = ImageBuffer(data.data, (data.width, data.height), 'RGB')
		file2 = ImageBuffer(data.data, (data.width, data.height), 'RGB')
		start = False
	else:
		# Fill Display with Black
		screen.fill(BLACK)

		# Switch Objects and Load in New One
		file1 = file2
		file2 = ImageBuffer(data.data, (data.width, data.height), 'RGB')

		# Load ImageFile Objects into CompareImages Objects
		backgroundSub = CompareImages(file1, back)
		frameDiff = CompareImages(file1, file2)
		
		# Process Frames
		backgroundSub.process(TOLERANCE)
		frameDiff.process(TOLERANCE)
		disp = file1.imgFile

		# Draw Annotations
		backgroundSub.drawBound(disp)
		backgroundSub.drawBoundCenter(disp)
		backgroundSub.drawLegTarget(disp)
		backgroundSub.drawAbTarget(disp)

		# Info to ROS
		msg = AbPosition()
		msg.x = backgroundSub.abLoc[0]
		msg.y = backgroundSub.abLoc[1]
		pub.publish(msg)

		# Fit Window Size to Image
		x, y = screen.get_size()
		if x != disp.get_width() or y != disp.get_height():
			screen = pygame.display.set_mode((disp.get_width(),disp.get_height()))

		# Draw Image
		screen.blit(disp, dest=(0,0))
		
		# Refresh Display
		pygame.display.flip()
		# Limit Frames
		clock.tick(30)

def listener():
	"""Starts PyTrack Node and Subscribes to the /camera/image_raw Topic."""
	rospy.init_node('pytrack', anonymous=True)
	rospy.Subscriber("camera/image_raw", Image, callback)
	rospy.spin()

# Main
if __name__ == '__main__':
	listener()
