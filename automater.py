import alladxvsoffsetmodel
import dailyfinder
import adxvsoffset

def main():
    companies=[]
    companies=dailyfinder.main()
    for comp in companies:
        adxvsoffset.main(comp)

main()
