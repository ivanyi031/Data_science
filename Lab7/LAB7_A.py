import numpy as np
import skimage
import  matplotlib.pyplot as plt
from skimage import io,data
from scipy.signal import convolve2d


filtera = np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
filterb = np.array([[-1,-1,2],[-1,2,-1],[2,-1,-1]])
filterc=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
filterd=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
filtere=np.array([[0,-1,0],[1,0,1],[0,-1,0]])
building= data.coins()#io.imread("E:/building.jpg",as_gray=True)
a=convolve2d(building,filtera)
b=convolve2d(building,filterb)
c=convolve2d(building,filterc)
d=convolve2d(building,filterd)
e=convolve2d(building,filtere)
plt.figure(figsize=(12, 15))
plt.subplot(2,3,1)
plt.imshow(building,cmap='gray')
plt.subplot(2,3,2)
plt.title('a')
plt.imshow(a,cmap='gray')
plt.subplot(2,3,3)
plt.imshow(b,cmap='gray')
plt.title('b')
plt.subplot(2,3,4)
plt.imshow(c,cmap='gray')
plt.title('c')
plt.subplot(2,3,5)
plt.imshow(d,cmap='gray')
plt.title('d')
plt.subplot(2,3,6)
plt.imshow(e,cmap='gray')
plt.title('e')
plt.show()