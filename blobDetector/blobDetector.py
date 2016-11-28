# Standard imports
import cv2
import numpy as np;
 
# Read image
cap = cv2.VideoCapture(0)
 
# Set up the detector with default parameters.
detector = cv2.SimpleBlobDetector_create()
n = 0

while(True):
	n += 1
	image = cap.read()[1]
	image2 = image.copy()
	im = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
	# Detect blobs.
	keypoints = detector.detect(image)
 
	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
	image = cv2.drawKeypoints(image, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	if n % 5 == 1:
		circles = cv2.HoughCircles(im, cv2.HOUGH_GRADIENT, 1.2, 100)

        	if circles is not None:
               		# convert the (x, y) coordinates and radius of the circles to integers
            		circles = np.round(circles[0, :]).astype("int")
                	# loop over the (x, y) coordinates and radius of the circles

                	for (x, y, r) in circles:
                       		# draw the circle in the output image, then draw a rectangle
                       		# corresponding to the center of the circle
                       		cv2.circle(image2, (x, y), r, (0, 255, 0), 4)
                       		cv2.rectangle(image2, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                        	# print coordinates, radius and number of circle found 
	# Show keypoints
	cv2.imshow("Keypoints", np.hstack([image2, image]))
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
