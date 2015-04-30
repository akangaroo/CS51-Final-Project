from image import Picture
import os

# IMAGE_DIRECTORY = "amymoving"

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

	rgb = [red, green, blue]
	return rgb

# image = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
# print (create_histogram(image))
# print image.width * image.height

def chi_square(hist1, hist2):