from PIL import Image
import os

class Picture(object):

    # initialize image object
    def __init__ (self, filename = None, type = None, size = None):
        if filename is None:
            self.img = Image.new(type, size)
            self.rgb_img = self.img
            x, y = size
            self.width, self.height = x, y
        else:
            self.img = Image.open(filename)
            self.rgb_img = self.img.convert('RGB')
            self.width, self.height = self.img.size

    # pos should always be a tuple of two integers
    def get_RGB_value(self, pos):
        return self.rgb_img.getpixel(pos)

    def get_next_RGB(self, pos):
        (x, y) = pos
        if x >= self.width:
            return self.get_RGB_value(self, (1, y+1))
        else:
            return self.get_RGB_value(self, (x+1, y))

    # insert RGB value into image at pos
    def put_RGB_value(self, pos, rgb):
        (x, y) = pos
        (r, g, b) = rgb
        self.img.putpixel((x,y), (r,g,b))

    def save(self, filename):
        self.img.save(filename)