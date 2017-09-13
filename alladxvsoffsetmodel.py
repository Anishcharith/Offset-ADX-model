import adxvsoffset
import pandas as pd

def main(companies):
    companies=pd.read_csv('nifty.csv')
    NSE=companies['Symbol'].values[1:]
    for comp in ['COALINDIA','ENGINERSIN','EXIDEIND','HINDPETRO','ONGC','PFC','SUNTV','TATACHEM','TCS','ULTRACEMCO','WIPRO']:
        adxvsoffset.main(comp)

