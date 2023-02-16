import numpy as np
import matplotlib.pyplot as plt
from skimage import io,transform,filters,morphology
from skimage.color import rgb2gray,rgb2hsv
import cv2
rice=cv2.imread('C:/Users/User/Desktop/SingleRice.jpg',cv2.IMREAD_UNCHANGED)
gray=cv2.cvtColor(rice,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray, (13,13),10)
cv2.imshow('blur',blur)
# blur=cv2.blur(gray,(5,5))
ret,thresh_img=cv2.threshold(blur,90,255,cv2.THRESH_BINARY)
cv2.imshow('thresh_img',thresh_img)
kernel=np.ones((3,3), np.uint8)
#ero=cv2.dilate(thresh_img,kernel,iterations=1)
#cv2.imshow('erosion',ero)
cnts,hierarchy=cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
length=0
for i in cnts:
    l=cv2.arcLength(i,True)
    if l>length:
        length=cv2.arcLength(i,True)
        points=i
cv2.drawContours(rice,points,-1,(0,0,255),5)
cv2.imshow('rice',rice)
cv2.waitKey(0)
