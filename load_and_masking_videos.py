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
    blurred2 = cv2.GaussianBlur(frame, (7, 7), 0)
    blurred3 = cv2.medianBlur(frame, 7)
    blurred4 = cv2.bilateralFilter(frame, 7, 31, 31)

    # Mostrando o resultado
    cv2.imshow('Blurred', frame)
    cv2.imshow('Blurred', blurred4)
    if cv2.waitKey(45) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
