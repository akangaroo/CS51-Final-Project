import median, os, similarity, numpy, cv2
from picture import Picture

# introduction to project
print "\n\nWelcome to our CS51 Project: \nPhotographing the John Harvard Statue\n" \
		"Our project removes moving objects in the background in a collection " \
		"of photos. Make a selection below for the option you would like to run " \
		"by entering the letter in the parenthesis:" \
		"\n(A) Amy in Basement" + "\n(B) Beach" + "\n(J) John Harvard Statue" \
		"\n(S) Sculpture" + "\n(M) Movie of Room"

user_choice = raw_input("\nEnter your choice: ")

# function for the user to choose an image collection
def choose_images(x):
	x = x.lower().strip()
	return {
		'a' : 'amy',
		'b' : 'beach',
		'j' : 'john_harvard',
		's' : 'statue',
		'm' : 'samplemov'
 	}.get(x, "Pictures not found")

# folder containing image set or movie to use
IMAGE_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data', choose_images(user_choice)))

img_list = []
size_x = None
size_y = None

# if analyzing a movie, get frames from movie
if "mov" in IMAGE_DIRECTORY:
	capture_video = cv2.VideoCapture(os.path.join(IMAGE_DIRECTORY, "sample.mov"))
	success = True
	while success:
		success, image = capture_video.read()
		if success:
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			img_list.append(Picture(array = image))
else:
	# create list of Picture objects from image directory
	for f in os.listdir(IMAGE_DIRECTORY):
		if f is not "final.png" or "output.png":
			img_list.append(Picture(filename = os.path.join(IMAGE_DIRECTORY, f)))

# get width (size_x) and height (size_y) of each image
if img_list:
	size_x = img_list[0].width
	size_y = img_list[0].height

# empty Picture object to hold output image
image = Picture(type = 'RGB', size = (size_x, size_y))


# user chooses which median finding algorithm to apply to images
print "\n\nSeveral functions are available to process the image:\n" \
		"(A) Quick Select\n" + "(B) Median of Fives\n" + "(C) Counting Sort\n" \
		"(D) Median of Sorted List\n"

while True:
	user_median = raw_input("Choose a function: ")
	user_median = user_median.lower().strip().replace("(","").replace(")","")
	if user_median in ['a','b','c','d']:
		break

print "Processing image..."

# iterate through image set and retrieve RGB values
for y in range(size_y):
	for x in range(size_x):
		r_list = []
		g_list = []
		b_list = []
		for i in img_list:
			r, g, b = i.get_RGB_value((x,y))
			r_list.append(r)
			g_list.append(g)
			b_list.append(b)

		# insert median values into output image
		rm = median.get_median(r_list, user_median)
		gm = median.get_median(g_list, user_median)
		bm = median.get_median(b_list, user_median)

		image.put_RGB_value((x,y),(rm,gm,bm))

image.save(os.path.join(IMAGE_DIRECTORY, 'output.png'))

print "Done processing!"

# compare output image to reference image, named final.png
model = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
print "\n\nBrute Similarity: " + similarity.sim_brute(image, model)
print "Correlation Similarity: " + similarity.sim_correlation(image, model)
print "Chi Squared p-value: " + similarity.sim_chi(image, model)
print "Note: Closer to 0 is perfect for chi-squared, 1 is perfect for brute and correlation\n\n"

# displays output image to the user
image.display()


