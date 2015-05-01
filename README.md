# CS51 Final Project
Project Name: Photographing the John Harvard Statue.

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
Make an image or movie:
```shell
	(A) Amy in Basement
	(B) Beach
	(J) John Harvard Statue
	(S) Sculpture
	(M) Movie of Room
```

Select a median finding algorithm:
```shell
	(A) Quick Select
	(B) Median of Fives
	(C) Counting Sort
	(D) Baseline
```

Wait until the program finishes, and the you will get a percent similarity of the generated image to the reference frame using the pixel-to-pixel comparison. You'll see your generated image as well!

# Documentation

**main.py** - Main document for project, where image is processed

**compression.py** - Compresses the resulting image using Huffman Encoding

**median.py** - Collection of algorithms that finds median of list

**picture.py** - Picture class to get RGB value, save image, etc.

**similarity.py** - Collection of algorithms that find similarity between output and reference image

**stabilize.py** - Starting working on image stabilization, not completed yet


Image and Movie Files:
* Amy Moving in Basement
* Beach Scene
* John Harvard Statue
* Sculpture
* Movie of Room
