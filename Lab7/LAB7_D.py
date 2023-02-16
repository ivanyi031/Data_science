import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2hsv
from skimage.filters.rank import median
from skimage.morphology import square 
fan=io.imread("C:/Users/User/Desktop/資料科學概論lab/Lab7/YellowFan.png")
width = fan.shape[1]
height = fan.shape[0]
img = np.zeros((height,width))
#height(100,430)wide(200,550)
fan_hsv=rgb2hsv(fan)
for h in range(100,430):
    for w in range(200,520):
        if fan_hsv[h,w,0]>0.15 and fan_hsv[h,w,0]<0.18:
            if fan_hsv[h,w,2]>0.6 and fan_hsv[h,w,2]<=1:
                 if fan_hsv[h,w,1]>0.65 and fan_hsv[h,w,1]<=1: 
                    img[h,w]=1

neighborhood=square(width=5)
#img=median(img,neighborhood)
plt.imshow(img,cmap='gray')
plt.show()
