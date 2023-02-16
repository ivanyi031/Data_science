from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel("C:/Users/User/Desktop/資料科學概論lab/Lab05/Scatter.xlsx")
PC1=df['PC1']
PC2=df['PC2']
Genotype=df['Genotype']

type=df.groupby("Genotype")

g0=type.get_group(0)
print(g0.PC2,"fmp3",g0.PC1)
g1=type.get_group(1)
g2=type.get_group(2)

fig=plt.figure(constrained_layout=True)
gs=fig.add_gridspec(3,3)
ax1=fig.add_subplot(gs[:2,0])
ax2=fig.add_subplot(gs[:2,1:3])
ax3=fig.add_subplot(gs[-1,1:3])
ax1.hist([g0.PC2,g1.PC2,g2.PC2],bins=10,stacked=True,orientation="horizontal",color=['red','yellow','blue'],edgecolor='black')
ax1.set_yticks(np.arange(-400,600,200))
ax1.set_xticks(np.arange(0,15,5))
ax1.set_xlabel("Frequency")
ax1.set_ylabel("PC2")


sc=ax2.scatter(g0.PC1,g0.PC2,c='r',marker='^')
mc=ax2.scatter(g1.PC1,g1.PC2,c='y',marker='o')
bc=ax2.scatter(g2.PC1,g2.PC2,c='b',marker='s')
ax2.set_xticks(np.arange(-400,600,200))
ax2.set_yticks(np.arange(-400,600,200))
ax2.set_xlabel("PC1")
ax2.set_ylabel("PC2")
ax2.set_title("Scatter Plot")
ax2.legend((sc,mc,bc),("c/c","C/c","C/C"),loc="lower left",bbox_to_anchor=(-1,-1.05))

ax3.hist([g0.PC1,g1.PC1,g2.PC1],bins=10,stacked=True,orientation="vertical",color=['red','yellow','blue'],edgecolor='black')
ax3.set_xticks(np.arange(-400,600,200))
ax3.set_yticks(np.arange(0,10,5))
ax3.set_ylabel("Frequency")
ax3.set_xlabel("PC2")
# plt.show()



# plt.xticks([0,5,10])

plt.show()


