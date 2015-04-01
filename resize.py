import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# pegando a proporcao da relacao entre altura e largura da imagem
# quero que a nova largura seja 150 px
r = 150.0 / image.shape[1]
# dimensao da nova imagem mantendo a proporcao entre h e w
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)
cv2.waitKey(0)

# definindo a altura desejada
r = 200.0 / image.shape[0]
dim = (int(image.shape[1] * r), 200)
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Risized in Height", resized)
cv2.waitKey(0)

# usando a funcao de imutils
resized = imutils.resize(image, width=150)
cv2.imshow("Resized with function", resized)
cv2.waitKey(0)
