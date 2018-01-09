import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
    lower_blue = np.array([90,150,150])
    upper_blue = np.array([130,255,255])

##    lower_orange=np.array([20, 80, 70])#30,92,81
##    upper_orange=np.array([40,100,90])
    #purple=np.uint8([[[128,0,128]]])
    
##    print cv2.cvtColor(purple,cv2.COLOR_BGR2HSV)

    # define range of purple color in HSV
##    lower_purple=np.array([140, 200, 120])#150,255,128
##    upper_purple=np.array([160,255,140])

    
    lower_green=np.array([40,150,150])#hsv=60,255,255
    upper_green=np.array([90,255,255])

    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    
    mask=blue_mask+green_mask
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    coords= cv2.findNonZero(mask)
##    print coords

    # Bitwise-AND mask and original image to give color as well to mask
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
