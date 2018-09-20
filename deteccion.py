import numpy as np
import cv2
cap = cv2.VideoCapture('base11.mp4')    # Capturing from video file
fgbg = cv2.createBackgroundSubtractorMOG2() # Calling function for Gaussian Mixtured-based Background/Foreground Segmentation Algotihm
fondo = None
while(1):

    ret, frame = cap.read() # It assign ret a boolean value that means if is there something in cap variable. Frame is asigned with the matrix of that frame of the video
    
    fgmask = fgbg.apply(frame) # Applies the function to do the segmentation to that frame



    _, contours, _ = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Extract the contour list of the image
    

    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2, cv2.LINE_AA) # Draw the contours on the original frame

    frame1 = cv2.resize(frame, (960, 500)) # Resize the window 
    fgmask1 = cv2.resize(fgmask, (960, 500)) # Resize the window
    cv2.imshow('Original', frame1) # Show the original video with contours
    cv2.imshow('Binarizacion',fgmask1) # Show the binary video with contours


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop the script
        break
cap.release()
cv2.destroyAllWindows()
