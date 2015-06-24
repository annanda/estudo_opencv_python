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
    # import bpdb; bpdb.set_trace()
    frame_inicial = frame
    frame_novo = frame
    altura = frame.shape[0]
    largura = frame.shape[1]
    alfa = 0.9
    contador_frame = 0

    for i in xrange(0, altura):
        for j in xrange(0, largura):
            B = frame[i, j] - frame_inicial[i, j]
            frame_novo[i, j] = frame[i, j] + alfa * B

    contador_frame =+ 1;
    cv2.imshow('Magnificated, %d, contador_frame', frame_novo)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()