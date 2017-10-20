import adxmodel
import matplotlib.pyplot as plt
import clustering 

comp='YESBANK'
X=[]
Y=[]
R=[]
count1=0
count2=0
for i in range(40,50):
    x,y,r=adxmodel.main(comp,i)
    
    for j in range(len(x)):
        X.append(x[j])
        Y.append(y[j])
        R.append(r[j])
for j in range(len(X)):
    if R[j]>0:
        count1+=1
    else:
        count2+=1
print(count1,count2)
clustering.main(X,Y,R)

