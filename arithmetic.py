import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# soma e subtracao de arrays openCV
print "max of 255: " + str(cv2.add(np.uint8([200]), np.uint8([100])))
print "min of 0: " + str(cv2.subtract(np.uint8([50]), np.uint8([100])))

# soma e subtracao NumPy de arrays usando aritmetica modular
print "wrap around: " + str(np.uint8([200]) + np.uint8([100]))
print "wrap around: " + str(np.uint8([50]) - np.uint8([100]))

# import bpdb; bpdb.set_trace()

# cria uma matriz que vai ser adicionada a minha imagem
# essa matriz tem o mesmo tamanho da imagem dada
# e cada celula da matriz tem 3 campos para GBR (os vaLores de RGB)
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)
cv2.waitKey(0)

M = np.ones(image.shape, dtype="uint8") * 100
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
