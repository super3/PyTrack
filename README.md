PyTrack
========
Computer Vision Object/Motion Tracking, with Bounding Rectangles and Background Subtraction, using Python and PyGame.

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
* postprocess.py - Used to process image data, and saving results rather than displaying them.
* realtime.py - Using ROS as a backend it will process realtime streams as fast as it can. 

Setup
-------
1. Open `Classes/Config.py` in your text editor or IDE.
2. Change the FOLDER, FILE_PREFIX, ZERO_FILL, FILE_EXT to reflect the file path of the images that you want to process.
3. Change COMPARE_DISTANCE, COMPARE_WEIGHTS, COMPONENT_SIZE to reflect your thresholds for image procesesing.
4. Change START_FRAME and END_FRAME to reflect the limits of the images you want to process. 
5. (Optional) LIMIT is the max amount of images the script is allowed to load into memory, and process at once. The default value of 500 should work for most systems.
6. Save your changes.
7. Run `viewer.py` or `postprocess.py` or `realtime.py`.

Viewer.py
-------
* For checking the accuracy, and debugging the computer vision algorithms.
* Use the forward and back arrows to move forward or back 1 frame.
* Use the up and down arrows to move forward of back 10 frames.

Realtime.py
-------
* Only run in UNIX environment with ROS and PIL installed.

Warnings
-------
* Files must be be in an sequential format. Example: (image0001.jpg, image0002.jpg, etc.)
* Will not track more than one object at a time.