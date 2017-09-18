import adxvsoffset
import pandas as pd

def main(comps):
    companies=pd.read_csv('nifty.csv')
    NSE=companies['Symbol'].values[1:]
    for comp in comps:
        adxvsoffset.main(comp)
    return
