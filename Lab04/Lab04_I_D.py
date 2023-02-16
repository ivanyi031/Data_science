from contextlib import _AsyncGeneratorContextManager
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df=pd.read_csv("C:/Users/User/Desktop/資料科學概論lab/Lab04/pokemon_data.csv")
attack=df['Attack']
defense=df['Defense']
cluster=df['cluster']

attack0=[]
defense0=[]
attack1=[]
defense1=[]
attack2=[]
defense2=[]
color=[]
for i in range(len(cluster)):
    if cluster[i] ==0:
        attack0.append(attack[i])
        defense0.append(defense[i])
    elif cluster[i] ==1:
        attack1.append(attack[i])
        defense1.append(defense[i])
    elif cluster[i] ==2:
        attack2.append(attack[i])
        defense2.append(defense[i])

fig=plt.gcf()

c0=plt.scatter(attack0,defense0,s=5*np.ones((len(attack0),1)),c="Magenta")
c1=plt.scatter(attack1,defense1,s=5*np.ones((len(attack1),1)),c="green")
c2=plt.scatter(attack2,defense2,s=5*np.ones((len(attack2),1)),c="cyan")
fig.set_size_inches(9,8)
centriod_x=[49.875000,79.801887,112.270833]
centriod_y=[48.075000,74.386792,102.479167]
c_color=['Magenta','green','cyan']
centers0=plt.scatter(centriod_x[0],centriod_y[0],s=100,marker='^',c=c_color[0])
centers1=plt.scatter(centriod_x[1],centriod_y[1],s=100,marker='^',c=c_color[1])
centers2=plt.scatter(centriod_x[2],centriod_y[2],s=100,marker='^',c=c_color[2])
plt.title("Scatter plot of pokemons")
plt.xlabel("Attack")
plt.ylabel("Defense")
plt.legend((c0,c1,c2,centers0,centers1,centers2),
("Cluster0","Cluster1","Cluster2","Cent. of cluster0","Cent. of cluster1","Cent. of cluster2"),loc='upper right',ncol=2)
plt.show()



