import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# imagens sao representadas com ALTURA x LARGURA (y, x)
# pixels sao representados com COLUNAS x LINHAS (x, y)
cropped = image[92:154, 474:527]
cv2.imshow("Pedaco da Imagem", cropped)
cv2.waitKey(0)
