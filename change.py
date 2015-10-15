__author__ = 'jdepaula'

import sys
import math

coins = {
    0.01:'PENNY',
    0.05: 'NICKEL',
    0.10: 'DIME',
    0.25: 'QUARTER',
    0.50: 'HALF DOLLAR',
    1.00: 'ONE',
    2.00: 'TWO',
    5.00: 'FIVE',
    10.0: 'TEN',
    20.0: 'TWENTY',
    50.0: 'FIFTY',
    100.0: 'ONE HUNDRED'
}

def greedy_change(qty, coins):
    coin_values = coins.keys()
    coin_values.sort(reverse=True)
    result = ""

    for coin in coin_values:
        if not qty or qty < 0:
            return result
        if qty >= coin:

            times = int(qty/coin)
            for x in range(0, times):

                result += coins[coin] + ","
            qty -= coin * times

    return result


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    price, cash  = test.split(';')
    cash = float(cash)
    price = float(price)

    if price > cash:
        print 'ERROR'
    elif price - cash == 0:
        print 'ZERO'
    else:
        print greedy_change(cash - price, coins).rstrip(',')

test_cases.close()
