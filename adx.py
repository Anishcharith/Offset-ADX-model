import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

closep=[]
openp=[]
highp=[]
lowp=[]

def TR(o,h,l,c,yc):
    x=h-l
    y=abs(h-yc)
    z=abs(l-yc)

    T=0

    if y<=x>=z:
        T=x
    elif x<=y>=z:
        T=y
    elif x<=z>=y:
        T=z
    return T

def ExpMovingAverage(values,window):
    weights=np.exp(np.linspace(-1,0,window))
    weights/=weights.sum()
    a=np.convolve(values,weights,mode='full')[:len(values)]
    a[:window]=a[window]
    return a

def DM(o,h,l,c,yo,yh,yl,yc):
    moveUp=h-yh
    moveDown=yl-l

    if 0<moveUp>moveDown:
        pdm=moveUp
    else:
        pdm=0

    if 0<moveDown>moveUp:
        ndm=moveDown
    else:
        ndm=0

    return pdm,ndm

def calcDIs():
    TRs=[]
    PosDM=[]
    NegDM=[]

    for i in range(1,np.size(closep)):
        PDM,NDM=DM(openp[i],highp[i],lowp[i],closep[i],openp[i-1],highp[i-1],lowp[i-1],closep[i-1])
        PosDM.append(PDM)
        NegDM.append(NDM)

    expPosDM=ExpMovingAverage(PosDM,14)
    expNegDM=ExpMovingAverage(NegDM,14)

    PDIs=[]
    NDIs=[]
    
    for i in range(1,np.size(closep)):
        TRs.append(TR(openp[i],highp[i],lowp[i],closep[i],closep[i-1]))

    ATR=ExpMovingAverage(TRs,14)

    for i in range(np.size(ATR)):
        PDI=100*(expPosDM[i]/ATR[i])
        PDIs.append(PDI)
        NDI=100*(expNegDM[i]/ATR[i])
        NDIs.append(NDI)

    return PDIs,NDIs

def ADX(comp):
    data=pd.read_csv('../data/'+comp+'.csv')
   
    global closep
    global openp
    global lowp
    global highp
    closep=list(np.flipud(data['Close'].values))
    openp=list(np.flipud(data['Open'].values))
    highp=list(np.flipud(data['High'].values))
    lowp=list(np.flipud(data['Low'].values))
    
    PositiveDI,NegetiveDI=calcDIs()
    
    DXs=[]
    for i in range(np.size(closep)-1):
        DX=100*((abs(PositiveDI[i]-NegetiveDI[i])/(PositiveDI[i]+NegetiveDI[i])))
        DXs.append(DX)
    ADX=ExpMovingAverage(DXs,14)
    return PositiveDI,NegetiveDI,ADX
