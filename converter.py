import requests

currency = input().lower()
coin = dict(requests.get(f'http://www.floatrates.com/daily/{currency}.json').json())
if currency == 'usd':
    cache = {
        'usd': coin['eur']['inverseRate'],
        'eur': coin['eur']['rate']
    }
elif currency == 'eur':
    cache = {
        'usd': coin['usd']['rate'],
        'eur': coin['usd']['inverseRate']
    }
else:
    cache = {
        'usd': coin['usd']['rate'],
        'eur': coin['eur']['rate']
    }
while currency2 := input().lower():
    amount = int(input())
    print('Checking the cache...')
    if currency2 in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache.update({currency2: coin[currency2]['rate']})
    print(f'You received {cache[currency2] * amount} {currency2}.')

