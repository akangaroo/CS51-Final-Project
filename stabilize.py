import numpy as numpy
import cv2
from image import Picture

class Transform(object):

    #initialize image object
    def __init__ (x_change, y_change, a_change):
    	dx = x_change
    	dy = y_change
    	da = a_change

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
	cvtColor(prev, prev_gray, COLOR_BGR2GRAY)

	for i in xrange(1, len(cv_images)):
		current = cv_images[i]
		cvtColor(current, current_gray, COLOR_BGR2GRAY)

		goodFeaturesToTrack(prev_gray, prev_corner, 200, 0.01, 30)
		calcOpticalFlowPyrLK(prev_gray, current_gray, prev_corner, current_corner, status, err)

		prev_corner2 = []
		current_corner2 = []

		for j in xrange(len(status)):
			if(status[j]):
				prev_corner2.push_back(prev_corner[j])
				current_corner2.push_back(current_corner[j])

		T = estimateRigidTransform(prev_corner2, current_corner2, false)

		if T.data == NULL:
			last_T.copyTo(T)

		T.copyTo(last_T)

		dx = T.at<double>(0,2)
		dy = T.at<double>(1,2)
		da = atan2(T.at<double>(1,0), T.at<double>(0,0))

		transform = []
		transform.push_back(Transform(dx, dy, da))

		current.copyTo(prev)
		current_gray.copyTo(prev_gray)

	return img_list
