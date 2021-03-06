PyTrack
========
A simplified computer vision framework for object and motion tracking, using Python and Pygame. 

Dependencies and Pre-Setup
-------
**You must have [PyGame](http://pygame.org/) and [NumPy](http://numpy.scipy.org/) installed.** Developed in Python 3.2 (previous versions of Python may work if you're lucky).

PyTrack accepts a folder of image frames from a video. I suggest you use [IrfanView](http://www.irfanview.com/) or another tool to extract your images. 
These files can be in any sequential format, but must be the same pixel dimensions. PyTrack will accept any image formats accepted by PyGames's
[image modulee](http://www.pygame.org/docs/ref/image.html) (these include: JPG, PNG, GIF (non animated), BMP, PCX, TGA (uncompressed), TIF, LBM, PBM, PBM, PGM, PPM, and XPM). 

If you want to get PyTrack up and running right away, [download this sample image set](https://github.com/downloads/super3/PyTrack/SampleAnt.zip). 
Extract `ant_maze` into root PyTrack directory. You should be able to run `viewer.py` or `process.py` now. See setup below for more detailed instructions.

Setup
-------
1. Open `Classes/Config.py` in your text editor or IDE.
2. Change the FOLDER variable to the path of the image folder.
4. Select the best TOLERANCE for the data set. Default is 840000.
7. Save your changes.
8. Run `viewer.py` or `process.py`.

####Notes:
* Files must be in some sort of sequential format. Example: (image0001.jpg, image0002.jpg, etc.)
* Files must be the same pixel dimensions. 
* Will not track more than one object at a time.

Modules
-------

####Viewer.py
This module will display annotated results. 
* `Forward` and `Back` arrows to move forward or back 1 frame.
* `Up` and `Down` arrows to move forward or back 10 frames.
* `S` key to toggle between source images and PyTrack's pixel differencing.
* `1` key to toggle search area box around object.
* `2` key to toggle search area box center.

####Process.py
This module will quickly process image data. 
* Will load and process images without any input from the user.
* Outputs the coordinates of the dataset to `data.txt`.

Info and Thanks
-------
* Author: Shawn Wilkinson <me@super3.org>
* Author Website: http://super3.org/
* Project Github: https://github.com/super3/PyTrack
* License: GPLv3 <http://gplv3.fsf.org/>

This project was created during the summer of 2012 at [University of Washington](https://www.washington.edu/) in the [Tom Daniel Lab](http://faculty.washington.edu/danielt/), 
as part of the [Center for Sensorimotor Neural Engineering](http://www.csne-erc.org/) Research Experiences for Undergraduates(REU) program. 
Special thanks to the National Science Foundation(NSF). Currently this project is part of ongoing computer vision research at
[Morehouse College](https://morehouse.edu/)'s computer science department under Dr. Amos Johnson.