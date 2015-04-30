from image import Picture
import os

def brute(image, base):
	count = 0
	size_x, size_y = base.width, base.height
	for y in range(size_y):
		for x in range(size_x):
			r, g, b = image.get_RGB_value((x,y))
			rb, gb, bb = base.get_RGB_value((x,y))
			rgb = [abs(rb-r),abs(gb-g),abs(bb-b)]
			if sum(rgb) <= 10:
				count = count+1
	print count
	print size_x*size_y
	print  (float (count) / (size_x * size_y))
	return '%.2f' % (float(count) / (size_x * size_y) * 100)
