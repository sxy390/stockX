import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('ggplot')


def pltChart(symbol, start=dt.datetime(2018,1,1), end=dt.datetime.now()):
    df = web.DataReader(symbol, "yahoo", start, end)
    df["50ma"] = df["Adj Close"].rolling(window=50).mean()
    df["20ma"] = df["Adj Close"].rolling(window=20).mean()
    df.dropna(inplace=True)

    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

    ax1.plot(df.index, df["Adj Close"])
    ax1.plot(df.index, df["50ma"])
    ax1.plot(df.index, df["20ma"])
    ax2.bar(df.index, df["Volume"])

    plt.show()
