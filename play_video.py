import numpy as np
import cv2

cap = cv2.VideoCapture('/home/annanda/projetos/videos_fontes/baby.mp4')

while(True):
    # Capturando frame a frame
    ret, frame = cap.read()

    # Operacao de cor, aplicando grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrando o resultado
    cv2.imshow('frame', gray)
    if cv2.waitKey(35) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
