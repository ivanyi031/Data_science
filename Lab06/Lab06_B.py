
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io,filters
from skimage.color import rgb2gray
from PIL import Image



# Do NOT modifify the function names

def fade_gradually(img):
    processed = img.copy()
    width=len(processed[0])
    gray=1/3*processed[:,:,0]+1/3*processed[:,:,1]+1/3*processed[:,:,2]
    print(processed.shape)
    x=np.linspace(0,1,num=int(width*0.6))
    y=np.linspace(1,0,num=int(width*0.6))
    
    for i in range(0,800):
        if i <width*0.6:
            processed[:,i,0]=y[i]*processed[:,i,0]+x[i]*gray[:,i]
            processed[:,i,1]=y[i]*processed[:,i,1]+x[i]*gray[:,i]
            processed[:,i,2]=y[i]*processed[:,i,2]+x[i]*gray[:,i]
        else:
            processed[:,i,0]=processed[:,i,1]=processed[:,i,2]=gray[:,i]
    plt.imshow(processed)
    plt.show()
    return processed


def image_matting(img):
    processed = img.copy()
    processed = processed.convert("RGBA")
    data=processed.getdata()
    newData=[]
    for item in data:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
  
    processed.putdata(newData)
    plt.imshow(processed)
    plt.show()
    return processed




# You are incouraged to test your program in the main function

def main():
    image1=io.imread("C:/Users/User/Desktop/資料科學概論lab/Lab06-4/monkey_island.jpg")
    fade_gradually(image1)
    image2=Image.open("C:/Users/User/Desktop/資料科學概論lab/Lab06-4/cat.jpg")
    image2=image_matting(image2)
if __name__ == "__main__":
    main()


