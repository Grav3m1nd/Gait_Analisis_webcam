import cv2
import os

FILE_OUTPUT = 'output.avi'

if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

cap = cv2.VideoCapture('base11.mp4')

currentFrame = 0


width = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)

height = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)


fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (int(width),int(height)))


while(cap.isOpened()):

    ret, frame = cap.read()

    if ret == True:

        frame = cv2.flip(frame,1)


        out.write(frame)


        cv2.imshow('frame',frame)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    currentFrame += 1


cap.release()
out.release()
cv2.destroyAllWindows()
