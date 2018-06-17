import cv2 as cv
import numpy as np
import matplotlib

#Create a black image
img = np.zeros((512,512,3), np.uint8);
img = cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.imshow('image',img)
cv.waitKey(0)
