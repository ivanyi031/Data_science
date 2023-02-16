from cmath import pi
from turtle import color
import numpy as np
import matplotlib.pyplot as plt



x=np.arange(0,4*pi+0.01,0.01)
y=np.sin(x)+np.sin(3*x)
ytick=[-1,-0.3,0.1,1]
ylabel=["Minimum","Critical","Collapse","Maximum"]


plt.plot(x,y,lw=3,color="#FF00CC")
plt.yticks(ytick,ylabel)
plt.xlabel("x-axis",color="#00FF00")
plt.xticks(color="#00FF00")
plt.grid(axis='x',lw=0.5,color="#00FF00")
plt.grid(axis='y',lw=1,color="black")
ax=plt.gca()
ax.spines["bottom"].set_color("#00FF00")
ax.spines["top"].set_color("#00FF00")

plt.show()