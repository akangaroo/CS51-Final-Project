from image import Picture
import os
import numpy
import cv2

IMAGE_DIRECTORY = "amy"

def create_histogram(image):
	image = numpy.array(image.rgb_img)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	hist = cv2.calcHist([image], [0,1,2], None, [8,8,8],[0,256,0,256,0,256])
	hist = cv2.normalize(hist).flatten()
	return hist

def compare_histograms(hist1, hist2):
	return cv2.compareHist(hist1, hist2, cv2.cv.CV_COMP_CORREL)

model = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
image = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'output.jpg'))
print (compare_histograms(create_histogram(model), create_histogram(image)))
