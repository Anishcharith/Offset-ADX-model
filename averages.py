import numpy as np

def avrg(close,days):
    avg=[]
    for i in range(days,np.size(close)):
        avg.append(np.mean(close[i-days:i]))
    return avg

def offset(avg,days):
    offset=[]
    for i in range(days,np.size(avg)):
        offset.append(avg[i-days])
    return offset

