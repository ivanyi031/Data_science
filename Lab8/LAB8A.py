import numpy as np 
from skimage import morphology
import matplotlib.pyplot as plt
A=np.ones((10,10))
A[1,2:7]=0
A[2,1:3]=0
A[2,6:9]=0
A[3,1:3]=0
A[3,7:9]=0
A[4,1:5]=0
A[4,7]=0
A[5,1]=0
A[5,4:8]=0
A[6,1]=0
A[6,7:9]=0
A[7,1:4]=0
A[7,6:9]=0
A[8,3:8]=0
B=np.ones((2,2))
E=np.ones((11,11))
E[1:,1:]=A
EA=E.copy()
for r in range(10,0,-1):
    for c in range(10,0,-1):
        fit=E[r,c]+E[r-1,c]+E[r-1,c-1]+E[r,c-1]
        if fit !=4:
            EA[r,c]=0
erode_A=EA[1:,1:]
plt.subplot(1,2,1)
plt.imshow(A,cmap='gray')
plt.title("original")
plt.subplot(1,2,2)
plt.title("erosion")
plt.imshow(erode_A,cmap='gray')
plt.show()