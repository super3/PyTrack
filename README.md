PyTrack
========
Computer Vision Object/Motion Tracking, with Bounding Rectangles and Frame Subtraction, using Python and PyGame. 

Developed during the summer of 2012 at University of Washington in the Tom Daniel Lab, as part of the Center for Sensorimotor
Neural Engineering(CSNE)'s Research Experiences for Undergraduates(REU) program. Special thanks to the National Science Foundation(NSF).

Info
-------
* Author: Shawn Wilkinson <me@super3.org>
* Author Website: http://super3.org/
* Project Github: https://github.com/super3/PyTrack
* License: GPLv3 <http://gplv3.fsf.org/>

Folders and Files
-------
* Classes - Contains all the classes for the project, as well as a helper module.
* viewer.py - Used to display annotated results. Navigate with the arrow keys.
* postprocess.py - Used to quicky process image data, saving results to file.

Pre-Setup
-------
**You must have [PyGame](http://pygame.org/) and [NumPy](http://numpy.scipy.org/) installed.** Developed in Python 3.2 (previous versions of Python may work if you're lucky).

PyTrack accepts a folder of image frames from a video. I suggest you use [IrfanView](http://www.irfanview.com/) or another tool to extract your images. 
These files can be in any sequential format, but must be the same pixel dimetions. PyTrack will accept any image formats accepted by PyGames's
[image module](http://www.pygame.org/docs/ref/image.html) (these include: JPG, PNG, GIF (non animated), BMP, PCX, TGA (uncompressed), TIF, LBM, PBM, PBM, PGM, PPM, and XPM). 

If you want to get PyTrack up and running right away, [download this sample image set](https://github.com/downloads/super3/PyTrack/SampleAnt.zip). Extract `ant_maze` into root PyTrack directory. You should be able to run `viewer.py` or `postprocess.py` now. See setup below for more detailed instructions.

Setup
-------
1. Open `Classes/Config.py` in your text editor or IDE.
2. Change the FOLDER variable to the path of the image folder.
4. Select the best TOLERANCE for the data set. Default is 840000.
7. Save your changes.
8. Run `viewer.py` or `postprocess.py`.

Viewer.py
-------
* `Forward` and `Back` arrows to move forward or back 1 frame.
* `Up` and `Down` arrows to move forward or back 10 frames.
* `S` key to toggle between source images and PyTrack's pixel differencing.
* `1` key to toggle bounding box around object.
* `2` key to toggle bounding box center.

Warnings
-------
* Files must be in some sort of sequential format. Example: (image0001.jpg, image0002.jpg, etc.)
* Files must be the same pixel dimentions. 
* Will not track more than one object at a time.