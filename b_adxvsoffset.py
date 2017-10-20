import numpy as np
from sklearn import svm , cluster
import clusterfinder
import b_adxmodel
import matplotlib.pyplot as plt
import adxvsoffsetclassifier as clfi
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier

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

def collectpoints(comp,day):
    X=[]
    Y=[]
    for i in range((comp[1]-1)*10+1,comp[1]*10+1):
        x,y,r=b_adxmodel.main(comp[0],i,day)
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

def main(comp,day):
    p=[]
    n=[]
    X=[]
    Y=[]
    trainedmodels=[]
    color=['green','purple']
    colors=[]
    C=1.0
    n_estimators=10
    models=(OneVsRestClassifier(svm.SVC(kernel='linear',C=C,probability=True)),
            #svm.LinearSVC(C=C),
            #svm.SVC(kernel='rbf',gamma=0.7,C=C),
            #svm.SVC(kernel='poly',degree=3,C=C)
            #OneVsRestClassifier(BaggingClassifier(SVC(kernel='poly', probability=True, class_weight='auto'), max_samples=1.0 / n_estimators, n_estimators=n_estimators)),
            #RandomForestClassifier(min_samples_leaf=20)
            #BaggingClassifier(SVC(kernel='poly', probability=True, class_weight='auto'), max_samples=1.0 / n_estimators, n_estimators=n_estimators)
            AdaBoostClassifier(n_estimators=100)
            )
    X,Y=collectpoints(comp,day)
    trainedmodels=trainmodel(models,X,Y)
    titles=('SVC with linear kernel',
            #'LinearSVC (linear kernel)',
            #'SVC with rbg kernel',
            'bagging',
            'SVC with polynomial (degree 3) kernel')
    #X0=np.array([j[0] for j in X])
    #X1=np.array([j[1] for j in X])
    #xx,yy=make_meshgrid(X0,X1)
    #fig, sub = plt.subplots(1, 2)
    #fig.suptitle(comp[0]+" "+str(comp[1]))
    #plt.subplots_adjust(wspace=0.4, hspace=0.4)
    #for i in range(len(Y)):
    #    colors.append(color[Y[i]])
    #for clf,title,ax in zip(trainedmodels,titles,sub.flatten()):
    #    plot_contours(ax,clf,xx,yy,cmap=plt.cm.coolwarm, alpha=0.8)
    #    ax.scatter(X0, X1, c=colors, cmap=plt.cm.coolwarm, s=20, edgecolors='k')
    #    ax.set_xlabel('adx')
    #    ax.set_ylabel('price')
    #    ax.set_title(title)
    #for ax in sub.flatten():
    #    ax.scatter(comp[2],comp[3],color='black')
    pred=[]
    for clf in trainedmodels:
        pred.append(clf.predict([[comp[2],comp[3]]]))
    return pred
