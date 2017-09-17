import adxvsoffset
import pandas as pd

def main(comps):
    companies=pd.read_csv('nifty.csv')
    NSE=companies['Symbol'].values[1:]
    for comp in comps:#['COALINDIA','ENGINERSIN','EXIDEIND','HINDPETRO','ONGC','PFC','SUNTV','TATACHEM','TCS','ULTRACEMCO','WIPRO']:
        adxvsoffset.main(comp)

main(['ARVIND'])

