import numpy as np
import argparse
# import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.float32([[1, 0, 25], [0, 1, 50]])
# matriz de translacao tem que ser do tipo float
# na primeira linha o ultimo numero diz quantos px vao sofrer o shift
# pra direita ou esquerda (valores positivos - direita, valores negativos -
# esquerda
# na segunda linha, ultimo numero diz quantos px vao sofrer o shift
# pra cima ou baixo (valores positivos - baixo, valores negativos - cima)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
# funcao que faz a translacao, imagem a ser transformada, matriz de traslacao,
# altura da imagem a ser modificada,
# largura da imagem a ser modificada
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

M = np.float32([[1, 0, -40], [0, 1, -100]])
# agora vai transladar para a esquerda e cima, pois tem numeros negativos
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)
