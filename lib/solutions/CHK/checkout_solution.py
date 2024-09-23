import pandas as pd
from math import floor
from collections import Counter
import re


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    pricings = pd.DataFrame({
        'Item': ['A', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'F'],
        'Special offer count': [5, 3, 1, 2, 1, 1, 1, 1, 1],
        'Special offer price': [200, 130, 50, 45, 30, 20, 15, 40, 10]
    })

    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCDEF]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    item_counter = Counter(filtered_skus)
    print(item_counter)
    if item_counter['B'] > 0:
        item_counter['B'] -= floor(item_counter['E'] / 2)

    if item_counter['F'] >= 2:
        item_counter['F'] -= floor(item_counter['F'] / 2)
    print(item_counter)
    
    total = 0

    for item in item_counter:
        n = item_counter[item]
        offer_thresholds = list(pricings[pricings['Item'] == item]['Special offer count'].values)
        offer_thresholds.sort(reverse=True)

        for offer in offer_thresholds:
            total += floor(n / offer) * pricings[(pricings['Item'] == item) & (pricings['Special offer count'] == offer)]['Special offer price'].values[0]
            n = n % offer

    print(total)
    return int(total)
            
    

assert checkout('ABCD') == 115
assert checkout('AAA') == 130
assert checkout('AAAAA') == 200
assert checkout('EE') == 80
assert checkout('a') == -1
assert checkout('-') == -1
assert checkout('EEB') == 80
assert checkout('EEBB') == 110
assert checkout('EEEEEBBB') == 230
assert checkout('EEEEEBBBFF') == 240
assert checkout('EEEEEBBBFFF') == 250
assert checkout('EEEEEBBBFFFF') == 250
