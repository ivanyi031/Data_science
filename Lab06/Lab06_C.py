import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io,data
import math

# Do NOT modifify the function names

def my_resize(img, height, width):
    
    w, h  = img.shape
    Sx=width/w
    Sy=height/h
    resize=np.zeros((height,width))
    x=np.arange(0,w)
    y=np.arange(0,h)
    x,y=np.meshgrid(x,y)
    X=np.floor(Sx*x)
    X=X.astype(int)
    Y=np.floor(Sy*y)
    Y=Y.astype(int)
    resize[Y,X]=img[y,x]
    plt.imshow(resize)
    plt.show()

    return resize
def my_rotation(img, angle):
    
    # TODO_C2
    w, h  = img.shape
    angle=angle/180*math.pi
    midx=w/2
    midy=h/2
    rot_img=np.zeros((w,h))
    for i in range(h):
        for j in range(w):
            x=(i-midx)*math.cos(angle)+(j-midy)*math.sin(angle)
            y=-(i-midx)*math.sin(angle)+(j-midy)*math.cos(angle)

            x=int(round(x)+midx)
            y=int(round(y)+midy)

            if x>=0 and x < w and y>=0 and y<h : 
                if len(img.shape)==2:
                    rot_img[x,y]=img[i,j]
                elif len(img.shape)==3:
                    rot_img[x,y,:]=img[i,j,:]
    return rot_img


# You are incouraged to test your program in the main function

def main():
    camera = data.camera()
    my_resize(camera,1024,256)
    
    plt.imshow(my_rotation(camera,30))
    plt.show()
if __name__ == "__main__":
    main()


