import numpy as np
import cv2

def translate(image, x, y):

    M = np.float32([[1, 0, x], [0, 1, y]])
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
    return shifted
