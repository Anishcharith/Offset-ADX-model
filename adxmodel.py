import numpy as np
import matplotlib.pyplot as plt
from newadx import *
from averages import *

def main(comp,off):
    data=pd.read_csv('data/'+comp+'.csv')
    closep=np.flipud(data['Close'].values)

    avg=avrg(closep,50)
    offset33=offset(avg,off)
    p,n,a=ADX(comp)

    a=a[50+off-1:]
    p=p[50+off-1:]
    n=n[50+off-1:]
    avg=avg[off:]
    closep=closep[50+off:]

    entry=[]
    for i in range(1,np.size(closep)):
        if avg[i]<offset33[i] and closep[i]>offset33[i] and closep[i-1]<=offset33[i-1]:
            entry.append(i)

    b=[]
    for i in entry:
        j=i
        while avg[j]<offset33[j] and j<np.size(closep)-1:
            j+=1
        b.append(j)

    x=[]
    y=[]
    r=[]
    for i in range(np.size(entry)):
        x.append(p[entry[i]])        
        y.append((closep[entry[i]]+avg[entry[i]])/(closep[entry[i]]-avg[entry[i]]))
        r.append(closep[b[i]]-closep[entry[i]])

    return x,y,r

