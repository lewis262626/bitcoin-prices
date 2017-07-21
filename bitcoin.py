#!/usr/bin/env python3
# bitcoin.py - Prints the current bitcoin price for a current x
import json, requests, sys

# Compute the location from the command line
if len(sys.argv) < 2:
    print('USAGE: bitcoin.py currency [-p] [amount]')
    sys.exit()

location = sys.argv[1]


url = "http://api.coindesk.com/v1/bpi/currentprice/{0}.json".format(location)
response = requests.get(url)
response.raise_for_status()

prices = json.loads(response.text)
value = prices['bpi'][location.upper()]['rate_float']
print('Current price of bitcoin is: {:.2f} '.format(value) + location)

if '-p' in sys.argv:
    index = sys.argv.index('-p')
    amountBTC = float(sys.argv[index+1])
    priceInCur = value * amountBTC
    print('Value of {0} BTC is: {1:.2f} {2}'.format(amountBTC, priceInCur, location))

