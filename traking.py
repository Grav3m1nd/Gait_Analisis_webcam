import cv2
import numpy as np


captura = cv2.VideoCapture('base11.mp4') # Obtaining the video

while (1):


    _, imagen = captura.read()   # Extract the current frame in variable imagen
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)  # Convert BGR(RGB) to HSV


    verde_bajos = np.array([0, 50, 140], dtype=np.uint8) # Range of selected color
    verde_altos = np.array([10, 235, 255], dtype=np.uint8)


    mask = cv2.inRange(hsv, verde_bajos, verde_altos) # Extracting the mask


    moments = cv2.moments(mask) # Calculates all of the moments
    area = moments['m00'] # Get the area of the selected color
    print(area)


    if (area > 10000):

        x = int(moments['m10'] / moments['m00']) # Get the coordinates of the center of interest area
        y = int(moments['m01'] / moments['m00'])


        print ("x = ", x)# Print coordinates
        print ("y = ", y)


        cv2.rectangle(imagen, (x, y), (x + 200, y + 200), (0, 0, 255), 2) # Draw a rectangle on the interest area

    mask = cv2.resize(mask, (960, 500)) # Resize the windows
    imagen = cv2.resize(imagen, (960, 500))


    cv2.imshow('mask', mask)  # Show the mask
    cv2.imshow('Camara', imagen) # Show the original video with rectangle identifier
    tecla = cv2.waitKey(5) & 0xFF
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Stop the script
        break

cv2.destroyAllWindows()
