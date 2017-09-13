import pandas as pd
from averages import *
from newadx import *


def main():
    comps=[]
    companies=pd.read_csv('nifty200.csv')
    NSE=companies['Symbol'].values
    for comp in NSE:
        try:
            data=pd.read_csv('data/'+comp+'.csv')
            closep=np.flipud(data['Close'].values)
            avg=avrg(closep,50)
            for off in range(9,50):
                offsetoff=offset(avg,off)
                p,n,a=ADX(comp)

                a=a[50+off-1:]
                p=p[50+off-1:]
                n=n[50+off-1:]
                avgoff=avg[off:]
                closepoff=closep[50+off:]
                if len(closepoff)>1 and closepoff[-1]>offsetoff[-1] and closepoff[-2]<offsetoff[-2] and offsetoff[-1]>avgoff[-1]:
                    print(comp)
                    comps.append(comp)
                    print(off)
                    y=(closepoff[-1]+avgoff[-1])/(closepoff[-1]-avgoff[-1])
                    print('adx = '+str(a[-1]))
                    print('y   = '+str(y))
        except:
            pass
                    
    return comps
                        
            

    
    





