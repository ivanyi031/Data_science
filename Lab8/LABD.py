
import matplotlib.pyplot as plt
from skimage import io,filters ,morphology
import numpy as np
from scipy.signal import convolve2d
import cv2 ,math
import skimage


def cross_number(image):
    w=image.shape[0]+2
    h=image.shape[1]+2
    print(w,h)
    CN_image=np.zeros((w,h))
    im=np.zeros((w,h))
    im[1:w-1,1:h-1]=image
    P2=[]
    for i in range(1,image.shape[0]+1):
        for j in range(1,image.shape[1]+1):
            if im[i,j]==1:
                P=np.zeros((9))
                P[0]= P[8]= im[i,j+1]
                P[1]= im[i-1,j+1]
                P[2]= im[i-1,j]
                P[3]= im[i-1,j-1]
                P[4]= im[i,j-1]
                P[5]= im[i+1,j-1]
                P[6]= im[i+1,j]
                P[7]= im[i+1,j+1]
                sum=0
                for k in range(0,8):    
                    sum+=abs(P[k]-P[k+1])
                CN_image[i,j]=0.5*sum
                    
    CN_image=CN_image[1:w-1,1:h-1]
    return CN_image,P2

            
fingerprint= io.imread("C:\\Users\\User\\Desktop\\資料科學概論lab\\Lab8\\Fingerprint.tif")
fingerprint_normalize= ((fingerprint-fingerprint.min())*255/(fingerprint.max()-fingerprint.min()))*255


laplace_filter=np.array([[0,1,0],[1,-4,1],[0,1,0]])
laplace=convolve2d(fingerprint_normalize,laplace_filter)
fingerprint_normalize=fingerprint_normalize-laplace[1:481,1:401]
kernel = cv2.getGaborKernel((15, 15), 5, 1, 10, 0.5, 0, cv2.CV_32F)
kernel /= math.sqrt((kernel * kernel).sum())
fingerprint_normalize== cv2.filter2D(fingerprint_normalize, -1, kernel)
plt.imshow(fingerprint_normalize,cmap='gray')
plt.show()

otsu_thresh= filters.threshold_otsu(fingerprint_normalize)
otsu_local= fingerprint_normalize>otsu_thresh
plt.imshow(otsu_local,cmap='gray')
plt.show()
#
otsu_local= morphology.remove_small_holes(otsu_local,30)
plt.imshow(otsu_local,cmap='gray')
plt.show()
otsu_local= morphology.dilation(otsu_local,morphology.square(2))
plt.imshow(otsu_local,cmap='gray')
plt.show()
otsu_local= morphology.erosion(otsu_local,morphology.square(2))
fingerprint2=otsu_local
plt.imshow(fingerprint2,cmap='gray')
plt.show()


fingerprint2= morphology.skeletonize(fingerprint2)
cn_image,p2=cross_number(fingerprint2)
fingerprint= skimage.color.gray2rgb(fingerprint)


for i in range (90,370):
    for j in range(100,380):
        if cn_image[i,j]==1:
            rr,cc=skimage.draw.circle_perimeter(i,j,10,method='bresenham',shape=None)
            fingerprint[rr,cc,2]=0
            fingerprint[rr,cc,1]=255
            fingerprint[rr,cc,0]=0
        if cn_image[i,j]==3:
            rr,cc=skimage.draw.circle_perimeter(i,j,10,method='bresenham',shape=None)
            fingerprint[rr,cc,2]=0
            fingerprint[rr,cc,1]=0
            fingerprint[rr,cc,0]=255

#print(count)
plt.subplot(1,2,1)
plt.imshow(fingerprint2,cmap='gray')
plt.subplot(1,2,2)
plt.imshow(fingerprint)
plt.show()