import numpy as np
import cv2

cap = cv2.VideoCapture('base11.mp4') # Capturing from video file
fgbg = cv2.createBackgroundSubtractorMOG2() # Calling function for Gaussian Mixtured-based Background/Foreground Segmentation Algotihm

count = 0 # Define variable to count
while (1):

    success, frame = cap.read() # Extract the video parameters  

    fgmask = fgbg.apply(frame) # Apply the mask for extracting the background


    print('Read a new frame: ', fgmask) # Showing the mask of that frame
    cv2.imwrite("C:/Users/Luis Cervantes/Documents/Marcha_1/frames_1/frame%d.jpg" % count, fgmask) # Save the mask of that frame in a jpg image
    count += 1 # Add 1 to the count variable to save the next frame


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop the script
        break

cap.release()
cv2.destroyAllWindows()
