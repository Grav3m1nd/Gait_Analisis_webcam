import numpy as np
import cv2
"""GOPR14.mp4"""
cap = cv2.VideoCapture('base11.mp4')#Load a specified video file
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=200, nmixtures=5, backgroundRatio=0.7, noiseSigma=0)#It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.

cv2.ocl.setUseOpenCL(False)#Opencl disabled

count = 0
while (1):

    ret, frame = cap.read()#Get or read the video data as matrix(boolean values)


    if not ret: #if the camera or video is not working , the loop is stopped.
        break


    fgmask = fgbg.apply(frame)#apply a background substraction to the video file.


    contornosimg = fgmask.copy()#copy the specified variable.


    im, contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#This line find the video image contours taking as refference the umbral specified. Assigning 3 values.The first, specified the umbral.The second, calculates the full hierarchy of the contours. The third is the contour approximation.

    for c in contornos:

        if cv2.contourArea(c) < 500:#The function computes a contour area.The area is computed using the Green formula. This loop consists in 500 iterations.
            continue#continue with the next iteration


        (x, y, w, h) = cv2.boundingRect(c)#This function is used to draw an approximate rectangle around the binary image.

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)#Drawing a rectangle over the videoimage specifying the dimensions.



    print('Read a new frame: ', fgmask)#print the specified variable
    cv2.imwrite("tejo2/frame%d.jpg" % count, fgmask)  # save frame as JPEG file
    count += 1
    k = cv2.waitKey(30) & 0xff#video delay
    if k == 27:
        break

    if key == ord("s"):#stop-close the script if the user press 's' key
        break

cap.release()#show the video in a new window(s)
cv2.destroyAllWindows()#close the window(s)
