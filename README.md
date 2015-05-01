# CS51 Final Project
Project Name: Photographing the John Harvard Statue

Created by Amy Kang, Anna Liu, Cecilia Zhou, Haoqing Wang

# Setup
Our project runs in Python 2.7 using the numpy library and the OpenCV package.

1. Follow [this link](https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/) to setup OpenCV on Python

	Note: We're using OpenCV version 2.4.11 instead of 2.4.9

2. Install numpy by following [this link](http://www.numpy.org/)

# Running the Program

Start the program
```shell
python main.py
```
Make a selection
```shell
	(A) Amy in Basement
	(B) Beach
	(J) John Harvard Statue
	(S) Sculpture
	(M) Movie of Room
```

Wait until the program finishes, and the you will get a percent similarity of the generated image to the reference frame using the pixel-to-pixel comparison. You'll see your generated image as well!

# Documentation

**main.py** - Main document for project, where image is processed
**compare.py**
**compression.py**
**correlation.py**
**chisquare.py**
**image.py** - Picture class
**median.py**