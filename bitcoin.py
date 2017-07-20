#!/usr/bin/env python3
# weather.py - Prints the weather for a location from the command line
import json, requests, sys, pprint

# Compute the location from the command line
if len(sys.argv) < 2:
    print('USAGE: bitcoin.py currency')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = "http://api.coindesk.com/v1/bpi/currentprice/{0}.json".format(location)
response = requests.get(url)
response.raise_for_status()

prices = json.loads(response.text)
value = prices['bpi'][location.upper()]['rate_float']
print('Current price of bitcoin is: {:.2f} '.format(value) + location)
