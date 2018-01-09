import numpy as np
import cv2
import time

##time.sleep(5)

cap=cv2.VideoCapture(0)

#take first frame of the video
ret, frame=cap.read()

#track color first to set init window for meanshift

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


lower_blue = np.array([90,100,100])
upper_blue = np.array([130,255,255])


##time.sleep(5)

blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
blue_mask = cv2.erode(blue_mask , None, iterations=2)
blue_mask = cv2.dilate(blue_mask , None, iterations=2)

    #get coordinates of density population of blue mask
coords=cv2.findNonZero(blue_mask)
print coords
cv2.imshow('mask',blue_mask)

initblue=coords[0]#coordinate of blue object initially
##print
##print initblue, int(initblue[0][0]), initblue[0][1] 

#set up init locaton of window (video window is 640 x 480 px)
#r=bottom val, h=height, c=left value, w=width
##r,h,c,w= 250,90,400,125
r,h,c,w= int(initblue[0][1])-20,50,int(initblue[0][0])-25,50
track_window=(c,r,w,h)

#setting up region of interest

roi=frame[r:r+h, c:c+w]
hsv_roi=cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) #gets pure color
#not based on lighting #changing color space

mask= cv2.inRange(hsv_roi,np.array((0.,60.,32.)), np.array((180.,255.,255.)))
#gets image between range given, adjusts for lighting
##mask= cv2.inRange(hsv_roi,np.array((40.,100.,100.)), np.array((100.,255.,255.)))
#CHANGED LIMITS

roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)

        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        cv2.imshow('img2',img2)

        #get center of track window -> translate into unity
        cof=[x+(w/2),y+(h/2)]#send to sql database

        #print(x+w/2,y+h/2)
            
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            cv2.imwrite(chr(k)+".jpg",img2)

    else:
        break

cv2.destroyAllWindows()
cap.release()
