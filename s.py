"""Stocks CLI
Usage:
    s.py
    s.py <name>
    s.py -h|--help
    s.py -d|--dummy
    s.py -v|--version
Options:
    <name>  Optional name argument.
    -h --help  Show this screen.
    -d --dummy  Show something dummy.
    -v --version  Show version.
"""

from docopt import docopt

def say_hello(name):
    return("Hello {}!".format(name))

class stocks:
    def dummy():
        print("Hello, welcome!")


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    if arguments['<name>']:
        print(say_hello(arguments['<name>']))
        print(arguments)
    elif arguments["--dummy"]:
        stocks.dummy()
    else:
        print(arguments)
