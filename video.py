from PIL import Image
import numpy
import median, os, compare
import cv2

capture_video = cv2.VideoCapture('sample.mov')

image_list = []
success = True
while success:
	success, image = capture_video.read()
	print (success)
	print(image)
	if success:
		pil_image = Image.fromarray(image, 'RGB')
		image_list.append(pil_image)