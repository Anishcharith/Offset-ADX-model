import numpy as np
from averages import *
from sklearn import svm , cluster
import b_adxmodel
from b_adx import *
import matplotlib.pyplot as plt
import b_adxvsoffset
import pandas as pd
import math

def main(comp,day):
    #print(comp,day)
    comps=[]
    offsetlist=[]
    totprofit=0
    data=pd.read_csv('../data/'+comp+'.csv')
    closep=np.flipud(data['Close'].values)[:-1*day]
    date=np.flipud(data['Date'].values)[:-1*day]
    #print(closep[np.size(closep)-1])
    avg=avrg(closep,50)
    for off in range(11,50):
        offsetoff=offset(avg,off)
        p,n,a=ADX(comp,day)

        a=a[50+off-1:]
        p=p[50+off-1:]
        n=n[50+off-1:]
        avgoff=avg[off:]
        closepoff=closep[50+off:]
        if len(closepoff)>1 and closepoff[-1]>offsetoff[-1] and closepoff[-2]<offsetoff[-2] and offsetoff[-1]>avgoff[-1]:
            x=math.ceil(off/10)
            y=(closepoff[-1]+avgoff[-1])/(closepoff[-1]-avgoff[-1])
            comps.append((comp,x,a[-1],y))
            offsetlist.append(off)
    comps=list(set(comps)) 
    for i,qwerty in zip(comps,offsetlist):
        pred=b_adxvsoffset.main(i,day)
        profit=0
        #pred0=clf[0].predict([[a[-1],y]])
        #pred1=clf[1].predict([[a[-1],y]])
        #print(pred[0])
        #print(pred[1])
        if pred[0]>=.05 and pred[1]>=.5:
            # and pred[2]>=.5:
            buy=list(closep)[-1]
            #print(qwerty)
            #print('buy = '+str(buy)+str(list(date)[-1]))
            sell=0
            j=day
            while(j!=1):
                close_sell=np.flipud(data['Close'].values)[:-1*j]
                date_sell=np.flipud(data['Date'].values)[:-1*j]
                avg_sell=list(avrg(close_sell,50))
                avgoff_sell=list(offset(avg_sell,qwerty))
                #print('avg ', avg_sell[len(avg_sell)-1])
                #print('offset ', avgoff_sell[len(avgoff_sell)-1])
                #print((avg_sell[len(avg_sell)-1])>=(avgoff_sell[len(avgoff_sell)-1]))  
                if(((avg_sell[len(avg_sell)-1])>=(avgoff_sell[len(avgoff_sell)-1]))||(close_sell[len(close_sell)-1]-buy)<(.05*buy)):
                    sell=list(close_sell)[-1]
                    break
                j-=1
            if sell:
                #print('sell ='+str(sell)+str(date_sell[len(date_sell)-1]))
                profit=sell-buy
        totprofit+=profit/closep[np.size(closep)-1]
        #print(profit)
        if(profit>0):
            break
    return totprofit

             
#main('ACC',1) 

