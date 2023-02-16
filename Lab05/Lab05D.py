from cmath import exp, pi, sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
x=np.arange(0,5,0.1)
y=np.arange(0,5,0.1)
X,Y=np.meshgrid(x,y)
Z=1/(2*pi)*np.exp(-1/2*((X-2.5)**2+(Y-2.5)**2))
ax.plot_surface(X,Y,Z,cmap=cm.viridis)
plt.show()



