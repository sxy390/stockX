"""Stocks CLI
Usage:
    s.py
    s.py -a <symbol>
    s.py -d|--dummy
    s.py -h|--help
    s.py -u|--updatedata
    s.py -v|--version
    s.py -w|--watchlist
Options:
    <symbol> Optional symbol.
    -a --add  Add symbol to watchlist.
    -d --dummy  Show something dummy.
    -h --help  Show this screen.
    -u --updatedata  Update stock data.
    -v --version  Show version.
    -w --watchlist  Show symbols in current watchlist.
"""

from docopt import docopt
import mysql.connector
from stockdata import getStockDate

class stocks:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='testuser',
            password='123',
            host='localhost',
            database='stock'
        )
        self.cursor = self.cnx.cursor()
        self.watchlist = []

    def dummy(self):
        print("Hello, welcome!")

    def addToWatch(self, symbol):
        add_symbol = "INSERT INTO symbols (symbol) VALUES (%(symbol)s)"
        data_symbol = {'symbol': symbol}
        try:
            self.cursor.execute(add_symbol, data_symbol)
            self.cnx.commit()
            print("{} is added to the watchlist.".format(symbol))
        except Exception:
            print("Operation failed. Symbol may exist.")

    def getWatchlist(self):
        self.cursor.execute("SELECT * FROM symbols ORDER BY symbol")
        result = self.cursor.fetchall()
        self.watchlist = [s[0] for s in result]

    def printWatchlist(self):
        for s in self.watchlist:
            print(s)
        print("----------------------------")
        print("{} symbols in the watchlist.".format(len(self.watchlist)))

    def updateData(self):
        if len(self.watchlist) == 0:
            self.getWatchlist()
        getStockDate(self.watchlist)

    def exit(self):
        self.cursor.close()
        self.cnx.close()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    stocks = stocks()
    if arguments["--dummy"]:
        stocks.dummy()
    elif arguments["--add"]:
        stocks.addToWatch(arguments['<symbol>'])
        stocks.exit()
    elif arguments["--watchlist"]:
        stocks.getWatchlist()
        stocks.printWatchlist()
        stocks.exit()
    elif arguments["--updatedata"]:
        stocks.updateData()
        stocks.exit()
    else:
        print(arguments)
