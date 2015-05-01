import median, os, compare, numpy, cv2, compression
from image import Picture

IMAGE_DIRECTORY = "statue"

image = Picture(filename = os.path.join(IMAGE_DIRECTORY, "output.png"))

image_pixels = list(image.get_pixel_list())
#compression.compress_rgb(image_pixels)

lst = [0,0,0,0,0,0,0,0,1,1,1,1,2,2,3]
compression.compress_rgb(lst)