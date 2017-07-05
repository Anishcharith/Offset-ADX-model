import urllib.request
import pandas as pd
import os

NIFTY=pd.read_csv('nifty.csv')
NIFTYnse=NIFTY['Symbol'].values
os.system('mkdir -p data/')
for comp in NIFTYnse:
    urllib.request.urlretrieve('https://www.quandl.com/api/v3/datasets/NSE/'+comp+'.csv',filename='data/'+comp+'.csv')
    print(comp+' done')
