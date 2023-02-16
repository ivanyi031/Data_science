import numpy as np
from skimage.filters.rank import mean
from skimage.filters import _gaussian
import  matplotlib.pyplot as plt
from skimage import io
import skimage
from scipy.signal import convolve2d
from skimage.morphology import square
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,denoise_wavelet)

saturn=io.imread("C:/Users/User/Desktop/資料科學概論lab/Lab7/Saturn.jpg",as_gray=True)

Laplacian=[[1,1,1],[1,-8,1],[1,1,1]]




saturn_wavelet=denoise_wavelet(saturn) 


neighborhood=square(width=3)


saturn_tv=denoise_tv_chambolle(saturn)
saturn_gaussian=skimage.filters.gaussian(saturn)
saturn_mean=mean(saturn,neighborhood)
saturn_bil=denoise_bilateral(saturn) 
saturn_wavelet=denoise_wavelet(saturn)   
plt.figure(figsize=(12,12))
plt.subplot(1,4,1)
plt.imshow(saturn,cmap='gray')
plt.title("original")
plt.subplot(1,4,2)
plt.imshow(saturn_wavelet,cmap='gray')
plt.title("one")
plt.subplot(1,4,3)
saturn_wavelet=denoise_wavelet(saturn_wavelet)
plt.imshow(saturn_wavelet,cmap='gray')
plt.title("two")
plt.subplot(1,4,4)
saturn_wavelet=denoise_wavelet(saturn_wavelet)
plt.imshow(saturn_wavelet,cmap='gray')
plt.title("three")
plt.show()