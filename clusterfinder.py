import numpy as np
from sklearn import cluster


def main(x,y,r):
    PX=[]
    NX=[]
    p0=[]
    p1=[]
    p2=[]
    in0=1000
    in1=1000
    in2=1000

    for i in range(np.size(x)):
        if r[i]>0:
            PX.append([x[i],y[i]])
        else:
            NX.append([x[i],y[i]])
    pkmeans=cluster.KMeans(n_clusters=3)
    p=pkmeans.fit_predict(PX)
    try:
        nkmeans=cluster.KMeans(n_clusters=3)
        n=nkmeans.fit_predict(NX)
    except:
        try:
            nkmeans=cluster.KMeans(n_clusters=1)
            n=nkmeans.fit_predict(NX)
        except:
            b=[0,0]
        
    if max(p)==0:
        a= pkmeans.cluster_center_[0]
    elif max(p)==1:
        a=pkmeans.cluster_centers_[1]
    else:
        a= pkmeans.cluster_centers_[2]
    try:
        if max(n)==0:
            b= nkmeans.cluster_center_[0]
        elif max(n)==1:
            b= nkmeans.cluster_centers_[1]
        else:
            b= nkmeans.cluster_centers_[2]
    except:
        b=[0,0] 
    return a,b
