import numpy as np
import cv2
"""GOPR14.mp4"""
cap = cv2.VideoCapture('base11.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

count = 0
while (1):

    success, frame = cap.read()

    fgmask = fgbg.apply(frame)


    print('Read a new frame: ', fgmask)
    cv2.imwrite("tejo/frame%d.jpg" % count, fgmask)
    count += 1
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    if k == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
quit()
