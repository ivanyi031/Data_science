from cmath import pi, sin
from tkinter import font
import matplotlib.pyplot as plt
import numpy as np
from simple_colors import *

x= np.arange(0,0.51,0.01)
y1=np.sin(2*pi*5*x)
y2=np.cos(2*pi*5*x)
y=np.arange(-1.5,2,0.5)
print(y1)
plt.plot(x,y1,"*c-",)
plt.plot(x,y2,"ok-")
plt.yticks(y)
plt.xlabel("Time"+" ("+r'$\mu s$'+")")
yg="Normalized"
plt.ylabel("$\it{'Normalized'}$ Signals")
plt.text(0.18,1.2, r'$\pi$' +"/2 phase lag",style='normal',fontsize='10')
plt.annotate("",xy=(0.2,1.1),xytext=(0.25,1.1),fontsize='10',arrowprops=dict(facecolor='black',arrowstyle='<->'))
plt.title("In-Phase $\it{(solid)}$ and Quadrature $\it{(dotted)}$ Signals ",fontsize=14)
plt.xlim(0,0.5)
plt.show()
