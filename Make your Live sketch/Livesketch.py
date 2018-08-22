
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
#sketch generating function
# first convert image to grayscale
def sketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cleanup image using gaussian Blur
    img_blur=cv2.GaussianBlur(img_gray,(5,5),0)
    # extract edges
    canny_edges=cv2.Canny(img_blur,10,70)
    # do an invert binarize the image
    ret,mask=cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
    return mask
# initialize the webcam,cap is the object provided by videocapture
#it contains a boolean indicating if it was successful (ret)
# it also contain the images collected from the webcam(frame)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('Our live Sketcher',sketch(frame))
    if cv2.waitKey(1)==13:
        break
        #13 is enterkey
cap.release()
cv2.destroyAllWindows()
   

