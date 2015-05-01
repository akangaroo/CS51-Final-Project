import median, os, compare, numpy, cv2
from image import Picture


print "Welcome to our CS51 Project: \nPhotographing the John Harvard Statue"
print "Our project removes moving objects in the background in a collection " \
		"of photos. Make a selection below for the option you would like to run " \
		"by entering the letter in the parenthesis:" \
		"\n(A) Amy in Basement" + "\n(B) Beach" + "\n(J) John Harvard Statue" \
		"\n(S) Sculpture" + "\n(M) Movie of Room"

user_choice = raw_input("Enter your choice: ")

def make_choice(x):
	x = x.lower().strip()
	return {
		'a' : 'amy',
		'b' : 'beach',
		'j' : 'john_harvard',
		's' : 'statue',
		'm' : 'samplemov'
 	}.get(x, "Pictures not found")

# folder containing image set or movie to use
IMAGE_DIRECTORY = make_choice(user_choice)

img_list = []
size_x = None
size_y = None

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
		rm = median.get_median(r_list)
		gm = median.get_median(g_list)
		bm = median.get_median(b_list)

		image.put_RGB_value((x,y),(rm,gm,bm))

image.save(os.path.join(IMAGE_DIRECTORY, 'output.png'))

model = Picture(filename = os.path.join(IMAGE_DIRECTORY, 'final.png'))
print "Similarity: " + compare.brute(image, model) + "%"

image.display()


