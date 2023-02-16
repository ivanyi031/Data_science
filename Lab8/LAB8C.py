import skimage
import matplotlib.pyplot as plt
from skimage import io,filters ,morphology
import numpy as np
from scipy.signal import convolve2d

image=io.imread("C:\\Users\\User\\Desktop\\資料科學概論lab\\Lab8\\Xray.png")
laplace_filter=np.array([[0,1,0],[1,-4,1],[0,1,0]])
#laplace=filters.laplace(image,ksize=3,mask=None)
laplace=convolve2d(image,laplace_filter)
sharpen_image=image-laplace[2:413,2:259]
#plt.imshow(laplace,cmap='gray')
sobel= filters.sobel(sharpen_image)#_v(sharpen_image)+filters.sobel_h(sharpen_image)
avg_filter=np.ones((5,5))/25
avg_sobel= convolve2d(sobel,avg_filter)
multiply= avg_sobel[2:413,2:259]*sharpen_image
add=image+multiply
Power_law=add**0.5
Power_law[np.isnan(Power_law)]=0
image_list=[image,laplace,sharpen_image,sobel,avg_sobel,multiply,add,Power_law]
title_list=['oringinal','a','b','c','d','e','f','g']

for i in range (8):
    plt.subplot(2,4,i+1)
    plt.imshow(image_list[i],cmap='gray')
    plt.title(title_list[i])
plt.show()
