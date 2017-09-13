import numpy as np
from sklearn import cluster
import clusterfinder
import adxmodel
import matplotlib.pyplot as plt
import adxvsoffsetclassifier as clf

def main(comp):
    p=[]
    n=[]
    xx=np.linspace(0,50)
    X10=[]
    X20=[]
    X30=[]
    X40=[]
    Y10=[]
    Y20=[]
    Y30=[]
    Y40=[]
    for i in range(8,50):
        x,y,r=adxmodel.main(comp,i)
        p,n=clusterfinder.main(x,y,r)
        if i<50 and i>40:
            plt.scatter(p[0],p[1],color='blue',marker='x')
            plt.scatter(n[0],n[1],color='blue',marker='o')
            X40.append([p[0],p[1]])
            X40.append([n[0],n[1]])
            Y40.append(1)
            Y40.append(0)
        if i<20:
            plt.scatter(p[0],p[1],color='green',marker='x')
            plt.scatter(n[0],n[1],color='green',marker='o')
            X10.append([p[0],p[1]])
            X10.append([n[0],n[1]])
            Y10.append(1)
            Y10.append(0)
        elif i<30:
            plt.scatter(p[0],p[1],color='purple',marker='x')
            plt.scatter(n[0],n[1],color='purple',marker='o')
            X20.append([p[0],p[1]])
            X20.append([n[0],n[1]])
            Y20.append(1)
            Y20.append(0)
        elif i<40:
            plt.scatter(p[0],p[1],color='red',marker='x')
            plt.scatter(n[0],n[1],color='red',marker='o')
            X30.append([p[0],p[1]])
            X30.append([n[0],n[1]])
            Y30.append(1)
            Y30.append(0)

    plt.title(comp)
    w,I=clf.main(X10,Y10)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color='green',label='9-20')
    w,I=clf.main(X20,Y20)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color='purple',label='20-30')
    w,I=clf.main(X30,Y30)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color='red',label='30-40')
    w,I=clf.main(X40,Y40)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color='blue',label='40-50')
    plt.legend()
    plt.show()
