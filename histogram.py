from image import Picture
import scipy.stats
import numpy as np
import cv2
import os

IMAGE_DIRECTORY = "amymoving"

# normalize histogram
def normalize(arr):
	total = sum(arr)
	for i in range(len(arr)):
		arr[i] = float(arr[i])/total
	return arr

# create color histogram from image object
def create_histogram(image):
	red = [0] * 256
	green = [0] * 256
	blue = [0] * 256

	size_x, size_y = image.width, image.height

	for y in range(size_y):
		for x in range(size_x):
			r, g, b = image.get_RGB_value((x,y))
			red[r] = red[r] + 1
			green[g] = green[g] + 1
			blue[b] = blue[b] + 1

	rgb = [normalize(red), normalize(green), normalize(blue)]
	return rgb

# calculate chi-squared value
def chi_square(v1, v2):
	if v2 != 0:
		val = (v1 - v2)*(v1 - v2)/(v2*v2)
	else:
		val = 0
	return val

# pass in two arrays, each histograms of 1 color channel
def chi_squared_comp(hist1, hist2):
	comp1 = [0] * 256
	for i in range(255):
		comp1[i] = chi_square(hist1[i], hist2[i])/2
	return sum(comp1)

# get chi-squared values of all three color channels
def comp_color_histograms(hist1, hist2):
	red_comp = chi_squared_comp(hist1[0], hist2[0])
	green_comp = chi_squared_comp(hist1[1], hist2[1])
	blue_comp = chi_squared_comp(hist1[2], hist2[2])
	return (red_comp, green_comp, blue_comp)

model = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
image = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'output.png'))
comp_color_histograms(create_histogram(model), create_histogram(image))
print (comp_color_histograms(create_histogram(model),create_histogram(image)))


