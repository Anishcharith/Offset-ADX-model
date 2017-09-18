import numpy as np
from sklearn import svm , cluster
import clusterfinder
import adxmodel
import matplotlib.pyplot as plt
import adxvsoffsetclassifier as clfi

def make_meshgrid(x, y,h=0.2):
    x_min,x_max = x.min()-1,x.max()+1
    y_min,y_max = y.min()-1,y.max()+1
    xx,yy=np.meshgrid(np.arange(x_min,x_max,h),np.arange(y_min,y_max,h))
    return xx,yy

def plot_contours(ax,clf,xx,yy,**params):
    Z=clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z=Z.reshape(xx.shape)
    out=ax.contourf(xx,yy,Z,**params)
    return out

def collectpoints(comp):
    X=[]
    Y=[]
    for i in range((comp[1]-1)*10+1,comp[1]*10+1):
        x,y,r=adxmodel.main(comp[0],i)
        p,n=clusterfinder.main(x,y,r)
        X.append([p[0],p[1]])
        X.append([n[0],n[1]])
        Y.append(1)
        Y.append(0)
    return X,Y

def plotline(x,y,color,label):
    xx=np.linspace(0,50)
    w,I=clfi.main(x,y)
    a=-w[0]/w[1]
    yy=a*xx - I[0]/w[1]
    plt.plot(xx,yy,color=color,label=label)

def trainmodel(models,X,y):
    trainmodels=(clf.fit(X,y) for clf in models)
    return trainmodels

def main(comp):
    p=[]
    n=[]
    X=[]
    Y=[]
    trainedmodels=[]
    color=['green','purple','red','blue']
    C=1.0
    models=(svm.SVC(kernel='linear',C=C),
            svm.LinearSVC(C=C),
            svm.SVC(kernel='rbf',gamma=0.7,C=C),
            svm.SVC(kernel='poly',degree=3,C=C))
    X,Y=collectpoints(comp)
    trainedmodels=trainmodel(models,X,Y)
    titles=('SVC with linear kernel',
            'LinearSVC (linear kernel)',
            'SVC with rbg kernel',
            'SVC with polynomial (degree 3) kernel')
    X0=np.array([j[0] for j in X])
    X1=np.array([j[1] for j in X])
    xx,yy=make_meshgrid(X0,X1)
    fig, sub = plt.subplots(2, 2)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    for clf,title,ax in zip(trainedmodels,titles,sub.flatten()):
        plot_contours(ax,clf,xx,yy,cmap=plt.cm.coolwarm, alpha=0.8)
        ax.scatter(X0, X1, c=Y, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
        ax.set_xlabel('adx')
        ax.set_ylabel('price')
        ax.set_title(title)
    plt.show()

