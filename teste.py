import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('oi.jpg',0)
cv2.imshow('livro',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 
# cv2.imwrite('oi-2.jpg',img)