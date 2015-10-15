#!/usr/bin/env python
import sys

COINS = {
'PENNY': 0.01,
'NICKEL': 0.05,
'DIME': 0.10,
'QUARTER': 0.25,
'HALF DOLLAR': 0.50,
'ONE': 1.00,
'TWO': 2.00,
'FIVE': 5.00,
'TEN': 10.00,
'TWENTY': 20.00,
'FIFTY': 50.00,
'ONE HUNDRED': 100.00
}

def calcuate_change(price,paid):
    """
    Checks underpayment and no change needed.
    Otherwise sends the price and the amount paid to the change function.
    """
    if price - paid == 0:
        print 'ZERO'
    elif price > paid:
        print 'ERROR'
    else:
        print change(price,paid)

def change(price, paid):
     change = int(paid*100) - int(price*100)

     result = []

     for coin_name, coin_value in sorted(COINS.items(), key = lambda x: x[1] * -1):
        coin_value = int(coin_value * 100)

        if change >= coin_value:
            num = change / coin_value
            change = change - coin_value * num
            [result.append(coin_name) for i in range(0, int(num))]

        if change == 0:
            break

     return ','.join(result)

def main():
    with open(sys.argv[1]) as f:
        for line in f:
            first, second = map(lambda x: float(x), line.rstrip().split(';'))
            calcuate_change(first, second)
if __name__=="__main__":
    main()
