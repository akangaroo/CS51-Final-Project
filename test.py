import median, os, numpy, compression
from image import Picture

IMAGE_DIRECTORY = "statue"

image = Picture(filename = os.path.join(IMAGE_DIRECTORY, "output.png"))

image_pixels = list(image.get_pixel_list())
compression.compress_rgb(image_pixels)