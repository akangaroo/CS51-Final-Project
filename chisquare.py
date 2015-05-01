from picture import Picture
import os
import scipy.stats

IMAGE_DIRECTORY = "amy"

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

model = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
image = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'output.png'))
r_comp, g_comp, b_comp = comp_color_histograms(create_histogram(image), create_histogram(model))
print (r_comp, g_comp, b_comp)
r_prob = scipy.stats.chi2.cdf(r_comp, 255)
g_prob = scipy.stats.chi2.cdf(g_comp, 255)
b_prob = scipy.stats.chi2.cdf(b_comp, 255)
print (r_prob, g_prob, b_prob)
print ((r_prob+g_prob+b_prob)/3)