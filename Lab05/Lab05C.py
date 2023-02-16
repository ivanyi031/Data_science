from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/User/Desktop/資料科學概論lab/Lab05/Score.csv")
round=[15,14,13,12,11]
Team=df.groupby('Team')
D=Team.get_group('D')
K=Team.get_group('K')
P=Team.get_group('P')
print(D,'\n',K,'\n',P)
D_point=list(D['Score'])
K_point=list(K['Score'])
P_point=list(P['Score'])
P_point=np.append(P_point,[0,0])
LeaderD=D['Leader']
LeaderK=K['Leader']
LeaderP=P['Leader']
fig, ax=plt.subplots(num=None,figsize=(8,3))
#ax.spines['top'].set_xticks(np.arange(0,180,20))
bar1=plt.barh(round,D_point,height=0.5,color='green')
bar_length=[]
for bar, name in zip(bar1, LeaderD[::1]):
        bar_length.append(bar.get_width())
        ax.text(bar.get_width()/2, bar.get_y()+bar.get_height()/2, name, color = 'black', ha = 'left', va = 'center')
print(bar_length)
bar2=plt.barh(round,K_point,left=D_point,height=0.5,color='blue')
i=0
for bar, name in zip(bar2, LeaderK[::1]):        
        ax.text(bar_length[i]+bar.get_width()/2, bar.get_y()+bar.get_height()/2, name, color = 'black', ha = 'left', va = 'center')
        bar_length[i]+=bar.get_width()
        i+=1
for i in range(5):
 D_point[i]+=K_point[i]
bar3=plt.barh(round,P_point,left=D_point,height=0.5,color='orange')
k=0
for bar, name in zip(bar3, LeaderP[::1]):
        length=bar.get_width()/2+bar_length[k]
        ax.text(length, bar.get_y()+bar.get_height()/2, name, color = 'black', ha = 'left', va = 'center')
        k+=1
ax.legend((bar1,bar2,bar3),("Team K","Team D","Team P"),loc="lower right",bbox_to_anchor=(1.1,0))
plt.grid(axis='x',lw=0.5,color="k",alpha=0.3)
plt.title("Points")
plt.show()
#plt.b