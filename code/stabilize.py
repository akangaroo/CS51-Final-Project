# Adapted from nghiaho.com: http://nghiaho.com/?p=2093
# We used the above C++ implementation of a video stabilization algorithm using OpenCV
# as a starting point to identify helpful functions within OpenCV and to
# learn about how the relevant functions within OpenCV work.

# From here, we intended to adapt the algorithm to create a more robust stabilization
# taking in image sets rather than video, and accounting for not only rigid transformations
# (translations and rotations in the plane) as this algorithm does, but also shearing
# and scaling by using findHomography and warpAffine functions in OpenCV rather than
# estimateRigidTransform. We quickly found, however, that OpenCV, as well as
# methods to calculate optical flow and transforms have a very steep
# learning curve, and the time could be used to work on our other extensions instead.
# We decided to leave our attempts for now to move on to other extensions (video, similarity
# and image compression)

import numpy as numpy
import cv2

class Transform(object):

    #initialize Transform object
    def __init__ (dx, dy, da):
        dx
        dy
        da

class Trajectory(object):

    #initialize Trajectory object
    def __init__ (x, y, a):
        x
        y
        a

def pil_to_opencv (img):
	open_cv_image = numpy.array(img.rgb_img)
	open_cv_image = open_cv_image[:, :, ::-1].copy()
	return open_cv_image

def stabilize (img_list):
	cv_images = []

	for i in xrange(len(img_list)):
		cv_images.append(pil_to_opencv(img_list[i]))

	#prev and prev_gray should be of type Mat
	prev = cv_images[0]
	cv2.cvtColor(prev, prev_gray, cv2.COLOR_BGR2GRAY)

	for i in xrange(1, len(cv_images)):
		current = cv_images[i]
		cv2.cvtColor(current, current_gray, cv2.COLOR_BGR2GRAY)

		cv2.goodFeaturesToTrack(prev_gray, prev_corner, 200, 0.01, 30)
		cv2.calcOpticalFlowPyrLK(prev_gray, current_gray, prev_corner, current_corner, status, err)

		prev_corner2 = []
		current_corner2 = []

		for j in xrange(len(status)):
			if(status[j]):
				prev_corner2.push_back(prev_corner[j])
				current_corner2.push_back(current_corner[j])

		T = cv2.estimateRigidTransform(prev_corner2, current_corner2, false)

		if T.data == NULL:
			last_T.copyTo(T)

		T.copyTo(last_T)

		dx = T.at(0,2)
		dy = T.at(1,2)
		da = numpy.atan2(T.at(1,0), T.at(0,0))

		transform = []
		transform.push_back(Transform(dx, dy, da))

		current.copyTo(prev)
		current_gray.copyTo(prev_gray)

	# accumulate transformations to get image trajectory
	x = 0
	y = 0
	a = 0

	trajectory_list = []

	for k in xrange(len(transform)):
		x += transform[i].dx
        y += transform[i].dy
        a += transform[i].da
		#trajectory_list.push_back(Trajectory(x,y,a))

	return img_list
