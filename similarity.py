from picture import Picture
import os
import numpy
import cv2
import scipy.stats

# brute force comparison (pixel by pixel comparison)
def sim_brute(image, base):
	count = 0
	size_x, size_y = base.width, base.height
	for y in range(size_y):
		for x in range(size_x):
			r, g, b = image.get_RGB_value((x,y))
			rb, gb, bb = base.get_RGB_value((x,y))
			rgb = [abs(rb-r),abs(gb-g),abs(bb-b)]
			if sum(rgb) <= 10:
				count = count+1
	return '%.2f' % (float(count) / (size_x * size_y))

# make histograms for correlation test using OpenCV functions
def create_correlation_hist(image):
	image = numpy.array(image.rgb_img)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	hist = cv2.calcHist([image], [0,1,2], None, [8,8,8],[0,256,0,256,0,256])
	hist = cv2.normalize(hist).flatten()
	return hist

# compare histograms based on correlation
def compare_correlation(hist1, hist2):
	return cv2.compareHist(hist1, hist2, cv2.cv.CV_COMP_CORREL)

def sim_correlation(image1, image2):
	return '%.2f' % compare_correlation(create_correlation_hist(image1), create_correlation_hist(image2))

# histogram for chi-square
# normalize histogram
def normalize(arr):
	total = sum(arr)
	for i in range(len(arr)):
		arr[i] = float(arr[i])/total
	return arr

# create color histogram from image object
def create_chi_hist(image):
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
# chi-square test
def chi_squared_comp(hist1, hist2):
	comp1 = [0] * 256
	for i in range(255):
		comp1[i] = chi_square(hist1[i], hist2[i])/2
	return sum(comp1)

def comp_color_histograms(hist1, hist2):
	red_comp = chi_squared_comp(hist1[0], hist2[0])
	green_comp = chi_squared_comp(hist1[1], hist2[1])
	blue_comp = chi_squared_comp(hist1[2], hist2[2])
	return (red_comp, green_comp, blue_comp)

def get_p_value (r_comp, g_comp, b_comp):
	r_prob = scipy.stats.chi2.cdf(r_comp, 255)
	g_prob = scipy.stats.chi2.cdf(g_comp, 255)
	b_prob = scipy.stats.chi2.cdf(b_comp, 255)
	return (r_prob, g_prob, b_prob)

def sim_chi(image1, image2):
	r, g, b = comp_color_histograms(create_chi_hist(image1), create_chi_hist(image2))
	rp, gp, bp =  get_p_value (r, g, b)
	return '%.2f' % ((rp+gp+bp)/3.0)