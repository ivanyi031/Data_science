import numpy as np
import matplotlib.pyplot as plt
from skimage import io,transform,filters,morphology
from skimage.color import rgb2gray

invoice=io.imread("C:/Users/User/Desktop/資料科學概論lab/Lab7/invoice.jpg")

plt.imshow(invoice)
#[166,122] [155,267 ][533,314][521,58]
src=np.array([[0,0],[0,680],[350,680],[350,0]])
dst=np.array([[125,185], [65,525], [300,530],[267,180] ])
tform3 = transform.ProjectiveTransform()
tform3.estimate(src, dst)
warped = transform.warp(invoice, tform3, output_shape=(680, 350))

warped=rgb2gray(warped)
warped_reverse=1-warped
plt.imshow(warped_reverse,cmap='gray')
bg=morphology.erosion(warped_reverse,morphology.square(3))
bg=filters.gaussian(bg, sigma=7)
warped_reverse=warped_reverse-bg

local_thresh=filters.threshold_local(warped_reverse,block_size=255,offset=-10/255)
warped_final=warped_reverse<local_thresh


plt.figure(figsize=(12,12))
plt.subplot(1,3,1)
plt.imshow(warped,cmap='gray')
plt.subplot(1,3,2)
plt.imshow(warped,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(warped_final,cmap='gray')
plt.show()


