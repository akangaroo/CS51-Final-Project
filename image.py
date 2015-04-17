from PIL import Image

class image(object):

	#initialize image object
	def __init__(self, filename):
		self.img = Image.open(filename)
		self.rgb_img = img.convert('RGB')
		self.width, self.height = self.img.size

	#pos should always be a tuple of two integers
	def get_RGB_value(self, pos):
		return self.rgb_img.getpixel(pos)

	def get_next_RGB(self, pos):
		(x, y) = pos
		if x >= self.width:
			return self.get_RGB_value(self, (1, y+1))
		else:
			return self.get_RGB_value(self, (x+1, y))
