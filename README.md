# Attention Tracker - Syracuse University CIS600 Project
This project is an effort between Doug Rickert, Chris Halbert, and Joshua
Poirier to determine whether or not a user is paying attention in the
direction of a camera.  Utilizing OpenCV's computer vision libraries,
we are able to determine if a face is detected in the image, and two open
eyes are present in the detected face.  A threshold accounts for any
minor inconsistencies with the computer vision and temporary loss of face
or open eyes to behaviors such as blinking or sneezing.

## Getting started
These instructions will get you a copy of the project up and running on your
local machine.

### Prerequisites
This software runs on Python 2.7 or Python 3.6, https://www.python.org/

A user must install OpenCV in order to run the software.  Releases of OpenCV
can be installed from here: https://opencv.org/releases.html

Tutorials for installing OpenCV-Python can be found here:
https://docs.opencv.org/3.4.0/da/df6/tutorial_py_table_of_contents_setup.html

### Installing
All other libraries can be found in the requirements.txt file.  To install,
use:
```
pip install --requirements.txt
```

### Run Software
Once properly set up, run the software with:
```
python main.py
```

## Authors
* **Doug Rickert**
* **Chris Halbert**
* **Josh Poirier**

## Acknowledgements
* Thank you to http://www.meddlemedia.com/freemusic/ for giving us audio for demonstration purposes!
* Thank you to OpenCV for the great tutorials.
