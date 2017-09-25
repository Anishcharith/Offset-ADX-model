import sklearn.svm as svm
import numpy as np
def main(x,y):
    xx, yy = np.meshgrid(np.linspace(-3, 3, 500),np.linspace(-3, 3, 500))
    clf=svm.SVC(kernel='rbf')
    clf.fit(x,y)
    z=clf.coef_[0]
    I=clf.intercept_
    return z,I

