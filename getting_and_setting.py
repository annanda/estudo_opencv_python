import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print "Pixel at (0,0)  - Red: %d, Green: %d, Blue: %d" % (r, g, b)

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print "Pixel at (0,0)  - Red: %d, Green: %d, Blue: %d" % (r, g, b)
