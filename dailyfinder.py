import pandas as pd
from averages import *
from adx import *
import math

def main():
    comps=[]
    companies=pd.read_csv('nifty.csv')
    NSE=companies['Symbol'].values
    for comp in NSE:
        data=pd.read_csv('data/'+comp+'.csv')
        closep=np.flipud(data['Close'].values)
        avg=avrg(closep,50)
        for off in range(11,50):
            offsetoff=offset(avg,off)
            p,n,a=ADX(comp)

            a=a[50+off-1:]
            p=p[50+off-1:]
            n=n[50+off-1:]
            avgoff=avg[off:]
            closepoff=closep[50+off:]
            if len(closepoff)>1 and closepoff[-1]>offsetoff[-1] and closepoff[-2]<offsetoff[-2] and offsetoff[-1]>avgoff[-1]:
                print(comp)
                print(off)
                x=math.ceil(off/10)
                if x==1 :
                    x=2
                y=(closepoff[-1]+avgoff[-1])/(closepoff[-1]-avgoff[-1])
                comps.append((comp,x,a[-1],y))
                print('adx = '+str(a[-1]))
                print('y   = '+str(y))
    comps=list(set(comps)) 
    return comps
