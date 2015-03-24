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
cv2.line(canvas, (300, 0), (0, 300), red)
# onde desenhar a linha, pixel inicial, pixel final, cor desejada
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
