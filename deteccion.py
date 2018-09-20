import numpy as np
import cv2
cap = cv2.VideoCapture('base11.mp4',0)
fgbg = cv2.createBackgroundSubtractorMOG2()
fondo = None
while(1):

    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)



    _, contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2, cv2.LINE_AA)

    frame1 = cv2.resize(frame, (960, 500))
    fgmask1 = cv2.resize(fgmask, (960, 500))
    cv2.imshow('Original', frame1)
    cv2.imshow('Binarizacion',fgmask1)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
