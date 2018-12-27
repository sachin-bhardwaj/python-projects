
# coding: utf-8

# In[2]:


import cv2
import numpy as np
imag=cv2.imread('im.jpg')
cv2.imshow('photu',imag)
cv2.waitKey(0)
gray=cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

template=cv2.imread('original.jpg',0)
w,h=template.shape[::-1]
result=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.40
loc=np.where(result>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(imag,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
    
cv2.imshow("detected",imag)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


pwd

