import median, os, numpy, compression, similarity
from image import Picture

IMAGE_DIRECTORY = "samplemov"

image = Picture(filename = os.path.join(IMAGE_DIRECTORY, "output.png"))
model = Picture(filename = os.path.join(IMAGE_DIRECTORY, "final.png"))

# image_pixels = list(image.get_pixel_list())
# compression.compress_rgb(image_pixels)

print "\n\nBrute Similarity: " + similarity.sim_brute(image, model)
print "Correlation Similarity: " + similarity.sim_correlation(image, model)
print "Chi Squared p-value: " + similarity.sim_chi(image, model)
print "Note: Closer to 0 is perfect for chi-squared, 1 is perfect for brute and correlation\n\n"