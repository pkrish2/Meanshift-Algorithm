import cv2
import numpy as np

cap=cv2.VideoCapture(0)#gets video from laptop camera
#cap = cv2.VideoCapture('vtest.avi') gets external video

print(cap.get(3), cap.get(4))#640 x 480 px
while True:
    
    ret,frame=cap.read()#capture frame

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #operation on frame
    
    cv2.imshow('frame',gray)#display resulting frame
    
    k=cv2.waitKey(10)& 0xff
    if k==27:#if esc key is pressed, break loop
        break

cap.release()#release capture
cv2.destroyAllWindows()
    
