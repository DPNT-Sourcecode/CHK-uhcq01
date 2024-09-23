import pandas as pd
from math import floor
from collections import Counter
import re


# noinspection PyUnusedLocal
# skus = unicode string


def isna(val):
    if val != val:
        return True
    else:
        return False


def checkout(skus: str) -> int:


    items = ['A','B','C','D','E']

    subtractions = {
        'EE': 'B'
    }

    pricings = pd.DataFrame({
        'Item': ['A', 'A', 'A', 'B', 'B', 'C', 'D', 'E'],
        'Special offer count': [5, 3, 1, 2, 1, 1, 1, 1],
        'Special offer price': [200, 130, 50, 45, 30, 20, 15, 40]
    })

    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCDE]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    
    

    total = 0

    for item in items:
        n = filtered_skus.count(item) # Occurrences of the item in the basket

        offer_thresholds = list(pricings[pricings['Item'] == item]['Special offer count'].values)
        offer_thresholds.sort(reverse=True)

        for offer in offer_thresholds:
            total += floor(n / offer) * pricings[(pricings['Item'] == item) & (pricings['Special offer count'] == offer)]['Special offer price'].values[0]
            n = n % offer

    print(total)
    return total
            
    
assert checkout('ABCD') == 115
assert checkout('AAA') == 130
assert checkout('AAAAA') == 200
assert checkout('EE') == 80
assert checkout('a') == -1
assert checkout('-') == -1
assert checkout('EEB') == 80
assert checkout('EEBB') == 110



