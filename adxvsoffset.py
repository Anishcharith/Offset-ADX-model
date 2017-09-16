import numpy as np
from sklearn import cluster
import clusterfinder
import adxmodel
import matplotlib.pyplot as plt
import adxvsoffsetclassifier as clf

def plotpoints(p,n,color):
    x=[]
    y=[]
    plt.scatter(p[0],p[1],color=color,marker='x')
    plt.scatter(n[0],n[1],color=color,marker='o')
    x.append([p[0],p[1]])
    x.append([n[0],n[1]])
    y.append(1)
    y.append(0)
    return x,y

def plotline(x,y,color,label):
    xx=np.linspace(0,50)
    w,I=clf.main(x,y)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color=color,label=label)


def main(comp):
    p=[]
    n=[]
    X=[[],[],[],[]]
    Y=[[],[],[],[]]
    for i in range(8,50):
        x,y,r=adxmodel.main(comp,i)
        p,n=clusterfinder.main(x,y,r)
        if i<20:
            tempX,tempY=plotpoints(p,n,'green')
            X[0]+=tempX
            Y[0]+=tempY
        elif i<30:
            tempX,tempY=plotpoints(p,n,'purple')
            X[1]+=tempX
            Y[1]+=tempY
        elif i<40:
            tempX,tempY=plotpoints(p,n,'red')
            X[2]+=tempX
            Y[2]+=tempY
        elif i<50:
            tempX,tempY=plotpoints(p,n,'blue')
            X[3]+=tempX
            Y[3]+=tempY

    plt.title(comp)
    plotline(X[0],Y[0],'green','9-20')
    plotline(X[1],Y[1],'purple','20-30')
    plotline(X[2],Y[2],'red','30-40')
    plotline(X[3],Y[3],'blue','40-50')
    plt.legend()
    plt.show()
