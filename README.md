PyTrack
========
Computer Vision Object/Motion Tracking, with Bounding Rectangles and Background Subtraction, using Python and PyGame. 

Developed during the summer at University of Washington in the Tom Daniel Lab, as part of the Center for Sensorimotor Neural Engineering(CSNE)'s Research Experiences for Undergraduates(REU) program. Special thanks to NSF.

Info
-------
* Author: Shawn Wilkinson <me@super3.org>
* Author Website: http://super3.org/
* Project Github: https://github.com/super3/PyTrack
* License: GPLv3 <http://gplv3.fsf.org/>

Folders and Files
-------
* Classes - Contains all the classes for the project, as well as a helper module.
* viewer.py - Used to display annotated results. Navigate with left and right arrow keys.
* postprocess.py - Used to quicky process image data, and saving results to file.

Setup
-------
1. Open `Classes/Config.py` in your text editor or IDE.
2. Change the FOLDER variable to the path of the image folder.
4. (Optional) Select the best TOLERANCE for the data set. Default is 640000.
7. Save your changes.
8. Run `viewer.py` or `postprocess.py`.

Viewer.py
-------
* Use the forward and back arrows to move forward or back 1 frame.
* Use the up and down arrows to move forward of back 10 frames.

Warnings
-------
* Files must be in some sort of sequential format. Example: (image0001.jpg, image0002.jpg, etc.)
* Will not track more than one object at a time.