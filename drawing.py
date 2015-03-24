import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
# porque uso 8 bits sem sinal para representar o valor do RGB de cada pixel
# que varia de 0 a 255 para cada um dos R G B.
