import backtesting
import pandas as pd
total=0
NIFTY=pd.read_csv('nifty200.csv')
NIFTYnse=NIFTY['Symbol'].values
for comp in NIFTYnse:
    test=0
    for i in range(50,0,-1):
        try:
            test+=backtesting.main(comp,i)
            total+=test
        except:
            pass
    print(comp,test)
print(total)
