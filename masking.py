import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# criando a matriz com zeros do mesmo tamanho da imagem e com dados do tipo
# inteiro sem sinal de 8 bits
mask = np.zeros(image.shape[:2], dtype="uint8")
# centro da imagem
(cX, cY) = (image.shape[1] / 2, image.shape[0] / 2)
# cria retangulo na tela mask, da cor branco e preenchido
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)

cv2.imshow("Mask", mask)
cv2.waitKey(0)
####
# Faz um bitewise_and com uma matriz com cor 0 (preto), exceto um retangulo com numeros 255
# (1 nos 8 bits) (cor branca). Qualquer coisa em and com 1 vai ser a reproducao daquela coisa.
# Assim a mascara funciona
####
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
