
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

df=pd.read_csv("C:/Users/User/Desktop/資料科學概論lab/Lab05/sales_data.csv")
facewash=df['facewash']
bathingsoap=df['bathingsoap']

with plt.xkcd():
    fig ,ax=plt.subplots(2,1,constrained_layout=True)
    ax[0].plot(range(1,13),bathingsoap,'ok-')
    ax[0].set_title("Sales data of Bathingsoap")
    ax[0].set_yticks([12500,10000,7500])
    ax[0].xaxis.set_ticklabels([])
    
    ax[1].plot(range(1,13),facewash,'ok-')
    ax[1].set_title("Sales data of facewash")
    ax[1].set_yticks([2000,1500])
    ax[1].set_xlabel("Month Number")
    
    #plt.subplots_adjust(left=0.1,bottom=0.15,right=0.9,top=0.75)

    fig.supylabel("Sales units in number")
    fig.tight_layout()

    plt.show()
