import adxvsoffset
import pandas as pd

def main():
    companies=pd.read_csv('nifty.csv')
    NSE=companies['Symbol'].values[1:]
    for comp in NSE:
        adxvsoffset.main(comp)

main()
