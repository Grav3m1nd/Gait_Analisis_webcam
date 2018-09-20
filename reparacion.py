import numpy as np
import cv2

"""GOPR14.mp4"""
cap = cv2.VideoCapture('base11.mp4',0)#Load a specified video file


fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=200, nmixtures=2, backgroundRatio=0.5, noiseSigma=.5)#It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm.

cv2.ocl.setUseOpenCL(False)#Opencl disabled

while (1):

    ret, frame = cap.read()#Get or read the video data as matrix(boolean values)


    if not ret:#if the camera or video is not working , the loop is stopped.
        break


    fgmask = fgbg.apply(frame)#apply a background substraction to the video file.


    contornosimg = fgmask.copy()#copy the specified variable.


    im, contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#This line find the video image contours taking as refference the umbral specified. Assigning 3 values.The first, specified the umbral.The second, calculates the full hierarchy of the contours. The third is the contour approximation.

    for c in contornos:

        if cv2.contourArea(c) < 900:#The function computes a contour area.The area is computed using the Green formula. This loop consists in 500 iterations.
            continue#continue with the next iteration


        (x, y, w, h) = cv2.boundingRect(c)#This function is used to draw an approximate rectangle around the binary image.

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)#Drawing a rectangle over the videoimage specifying the dimensions.


    frame1 = cv2.resize(frame, (960, 500))#Modify(resize) the size of the video-image
    fgmask1 = cv2.resize(fgmask, (960, 500))#Modify(resize) the size of the video-image
    cont = cv2.resize(contornosimg, (960, 500))#Modify(resize) the size of the video-image
    cv2.imshow('Camara', frame1)#show the original video file
    cv2.imshow('Umbral', fgmask1)#show the video with the umbral specified.
    cv2.imshow('Contornos', cont)# show the contours applyied to the filtered video image(umbral)


    k = cv2.waitKey(30) & 0xff#delay - 30 milliseconds
    if k == ord("s"):#stop-close the script if the user press 's' key
        break


cap.release()#show the video in a new window(s)
cv2.destroyAllWindows()#close the window(s)
