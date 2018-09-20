import numpy as np #Numbers library
import cv2 #Opencv library
import time #Time library
"""'base11.mp4'"""
camara = cv2.VideoCapture('base11.mp4',0)#Class for video capturing from video files, image sequences or cameras.

fondo = None #Null object

while True:
    (grabbed, frame) = camara.read()#Get or read the video data as matrix(boolean values)

    if not grabbed:#if the camera is not working , the loop is stopped.
        break


    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Video frames are converted from BGR(Blue,Green,Red) to gray scale.

    gris = cv2.GaussianBlur(gris, (21, 21), 0)#Video image is filtered by a gaussian function. This is the result of blurring an image.


    if fondo is None:#If the video background is null or none, it is changed to a gray scale with a gaussianBlur.
        fondo = gris
        continue#continue with the next iteration


    resta = cv2.absdiff(fondo, gris)#apply a backgroung substraction


    umbral = cv2.threshold(resta, 25, 255, cv2.THRESH_BINARY)[1]#A simple segmentation. Separate out regions of an image corresponding to objects which we want to analyze


    umbral = cv2.dilate(umbral, None, iterations=2)#This operation consist of convoluting an image A with some kernel (B), which can have any shape or size.Video image is dilated around specified regions.


    contornosimg = umbral.copy()#Copy umbral values


    im, contornos, hierarchy = cv2.findContours(contornosimg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)#This line find the video image contours taking as refference the umbral specified. Assigning 3 values.The first, specified the umbral.The second, calculates the full hierarchy of the contours. The third is the contour approximation.


    for c in contornos:

        if cv2.contourArea(c) < 500:#The function computes a contour area.The area is computed using the Green formula. This loop consists in 500 iterations.
            continue


        (x, y, w, h) = cv2.boundingRect(c)#This function is used to draw an approximate rectangle around the binary image.

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)#Drawing a rectangle over the videoimage specifying the dimensions.



    cv2.imshow("Camara", frame)#show the frames captured by the cam.
    cv2.imshow("Umbral", umbral)#show the video with the umbral specified.
    cv2.imshow("Resta", resta)#show the substraction between the original video and the umbral
    cv2.imshow("Contorno", contornosimg)# show the contours applyied to the filtered video image(umbral)


    key = cv2.waitKey(1) & 0xFF#Delay - 1 millisecond


    time.sleep(0.015)#The number of seconds the program should pause execution.


    if key == ord("s"):#stop the script if the user press 's' key
        break


camara.release()#show the video in a new window(s)
cv2.destroyAllWindows()#close the window(s)
