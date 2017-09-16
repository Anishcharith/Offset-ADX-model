import numpy as np
from sklearn import cluster
import matplotlib.pyplot as plt

def main(x,y,r):
    PX=[]
    NX=[]
    for i  in range(len(x)):
        if r[i]>0:
            PX.append([x[i],y[i]])
        else:
            NX.append([x[i],y[i]])
    pkmeans=cluster.KMeans(n_clusters=20)
    p=pkmeans.fit_predict(PX)
    try:
        nkmeans=cluster.KMeans(n_clusters=20)
        n=nkmeans.fit_predict(NX)
    except:
        pass
    for i in pkmeans.cluster_centers_:
        plt.scatter(i[0],i[1],color='blue',marker='x')
    for i in nkmeans.cluster_centers_:
        plt.scatter(i[0],i[1],color='blue',marker='o')
    plt.show()
            
