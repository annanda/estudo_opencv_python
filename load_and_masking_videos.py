import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="Path to the video")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["video"])

while(True):
    # Capturando frame a frame
    ret, frame = cap.read()

    # Mostrando o resultado
    cv2.imshow('frame', frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
