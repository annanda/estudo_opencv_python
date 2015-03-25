import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
# porque uso 8 bits sem sinal para representar o valor do RGB de cada pixel
# que varia de 0 a 255 para cada um dos R G B.

green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
# onde desenhar a linha, pixel inicial, pixel final, cor desejada
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
# onde desenhar a linha, pixel inicial, pixel final, cor desejada,
# a largura da linha
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
# onde desenhar o retangulo, o pixel do canto superior esquerdo
# do quadrado (inicio), o pixel do canto inferior direito do quadrado (final),
# cor desejada
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
# com o argumente da espessura da linha em -1 ele preenche o retangulo
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
