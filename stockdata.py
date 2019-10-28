import os
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
from datetime import datetime

def getStockDate(symbols):
    if not os.path.exists("stockdata"):
        os.makedirs("stockdata")
    for s in symbols:
        try:
            df = web.DataReader(s, "yahoo")
            print(df.head())
            df.to_csv("stockdata/{}.csv".format(s))
            print(s, "downloaded")
        except Exception as e:
            print(e, "error.")
        
