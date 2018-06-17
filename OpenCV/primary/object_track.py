import numpy as np
import cv2 as cv
import time
import imutils
import serial

def nothing(x):
    pass

#cap = cv.VideoCapture('http://192.168.0.101:8080/video')
cap = cv.VideoCapture(0)

#Create the trackbar stuff for controlling the upper HSV boundaries
cv.namedWindow('Trackbars')

cv.createTrackbar('L-H','Trackbars',0,179,nothing)
cv.createTrackbar('L-S','Trackbars',0,255,nothing)
cv.createTrackbar('L-V','Trackbars',0,255,nothing)
cv.createTrackbar('U-H','Trackbars',179,179,nothing)
cv.createTrackbar('U-S','Trackbars',255,255,nothing)
cv.createTrackbar('U-V','Trackbars',255,255,nothing)


#Check if the webcam has been opened
if cap.isOpened() == False:
    print("There has been an error in opening the camera, moron.")

#Setup variables for serial communication
COM_PORT = '/dev/rfcomm0'
ser = serial.Serial(COM_PORT,38400,timeout = 1)

#Run when webcam is up and running
while(cap.isOpened()):
    #Save each frame to the variable frame(Frame is the original stream) 
    ret,frame = cap.read()
    height, width, channels = frame.shape

    #Find the center of the image so relative position of the tracked obect can be identified
    iX = width/2
    iY = height/2
    cX = 0
    cY = 0
    
    blurred_frame = cv.GaussianBlur(frame, (5,5), 0)
    
    
    if ret == True:

        #Convert rom BGR to HSV(for generating the mask)
        img = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
        
        
        #Getting the trackbar position
        l_h = cv.getTrackbarPos('L-H','Trackbars')
        l_s = cv.getTrackbarPos('L-S','Trackbars')
        l_v = cv.getTrackbarPos('L-V','Trackbars')
        u_h = cv.getTrackbarPos('U-H','Trackbars')
        u_s = cv.getTrackbarPos('U-S','Trackbars')
        u_v = cv.getTrackbarPos('U-V','Trackbars')
        
        #Setting the treshold values for the camera
        lower_val = np.array([l_h,l_s,l_v])
        upper_val = np.array([u_h,u_s,u_v])
        mask = cv.inRange(img,lower_val,upper_val)
        mask = cv.erode(mask, None, iterations = 2)
        mask = cv.dilate(mask, None,iterations = 2)

        #Using contours(Read that more)
        _,contours,_ = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        
        #Finding the relevant contour
        if len(contours) > 1:
            #Find the largest contour(Usually the reference shape)
            c = max(contours, key = cv.contourArea)

            #If the contour area is larger than 0. (To prevent division by zero) 
            if cv.contourArea(c) > 0:
                M = cv.moments(c);
                cX = int(M["m10"]/M["m00"])
                cY = int(M["m01"]/M["m00"])
                cv.drawContours(frame,[c],-1,(0,255,0), 2)
                cv.circle(frame,(cX,cY),7,(255,255,255),-1)
                cv.putText(frame, "center", (cX - 20, cY - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                res = cv.bitwise_and(frame,frame,mask =mask)
                # Display the resulting frame
                cv.imshow('Mask',mask)
                cv.imshow('Normal && Mask',res)
        cv.imshow('Normal', frame)

        #This part deals with the relative position of the object
        dX = cX-iX
        dY = cY-iY
        
        print 'dX:%s' %dX
        print 'dY:%s' %dY
        print 'cX:%s' %cX
        print 'cY:%s' %cY
        print 'iX:%s' %iX
        print 'iY:%s' %iY

        #Boundaries are given soe clearance to preven the bot rom tittering at zero
        if dX > 10:
            #'1' is to turn cloackwise
            print "Bot shoudld turn right"
            ser.write('1')

            
        elif dX<-10:
            #'AC' is to turn anti-clockwise
            print "Bot shoudl turn left"
            ser.write('2')

            
        elif dX in range(-10,10):
            #0 is to stop turning
            ser.write('0')    
            print "Bot should stop"

        #Close when 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print('The camera was closed')
        break


# When everything is done release the capture and close the windows
cap.release()
cv.destroyAllWindows()
