import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
b,g,r = cv2.split(image)
image = cv2.merge([r,g,b])
plt.imshow(image, cmap='gray', interpolation='bicubic')
# plt.xticks([]), plt.yticks([])
plt.show()
