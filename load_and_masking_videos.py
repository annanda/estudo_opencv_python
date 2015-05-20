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

    blurred = cv2.blur(frame, (7, 7))

    # Mostrando o resultado
    cv2.imshow('Blurred', frame)
    cv2.imshow('Blurred', blurred)
    if cv2.waitKey(45) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
