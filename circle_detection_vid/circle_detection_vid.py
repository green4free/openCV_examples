# import the necessary packages
import numpy as np
import cv2
# start image capture from camera
cap = cv2.VideoCapture(0)
while(True):
	# read image from capture, and then convert it to grayscale
	image = cap.read()[1]
	output = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	
	# detect circles in the image
	circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 0.8, 120)
	
 	if circles is not None:
		# convert the (x, y) coordinates and radius of the circles to integers
		circles = np.round(circles[0, :]).astype("int")
		# loop over the (x, y) coordinates and radius of the circles

		for (x, y, r) in circles:
			# draw the circle in the output image, then draw a rectangle
			# corresponding to the center of the circle
			cv2.circle(output, (x, y), r, (0, 255, 0), 4)
			cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
			# print coordinates, radius and number of circle found


			 
	# show the output image
	cv2.imshow("output", np.hstack([image, output]))
	# event for close on Esc key
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
# release image capture and close all windows
cap.release()
cv2.destroyAllWindows()
