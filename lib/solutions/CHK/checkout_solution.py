import pandas as pd
from math import floor
from collections import Counter
import re


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    pricings = pd.DataFrame({
        'Item': [
            'A', 'A', 'A', 'B', 'B', 'C', 'D', 'E', 'F','G','H','H','H','I','J','K','K','L','M','N','O','P','P','Q','Q','R','S','T','U','V','V','V','W','X','Y','Z'],
        'Special offer count': [
            5, 3, 1, 2, 1, 1, 1, 1, 1, 1, 10, 5, 1, 1, 1, 2, 1, 1, 1, 1, 1, 5, 1, 3, 1, 1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1],
        'Special offer price': [
            200, 130, 50, 45, 30, 20, 15, 40, 10, 20, 80, 45, 10, 35, 60, 150, 80, 90, 15, 40, 10, 200, 50, 80, 30, 50, 30, 20, 40, 130, 90, 50, 20, 90, 10, 50]
    })

    subtractions = pd.DataFrame({
        'Item': ['E', 'F', 'N', 'R', 'U'],
        'Count': [2, 3, 3, 3, 4],
        'Subtract': ['B', 'F', 'M', 'Q', 'U']
    })


    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCDEFGHIJKLMNOPQRSTUVWXYZ]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    item_counter = Counter(filtered_skus)
    print(item_counter)

    for i, row in subtractions.iterrows():
        if item_counter[row['Item']] >= row['Count'] and item_counter[row['Subtract']] > 0:
            item_counter[row['Subtract']] -= floor(item_counter[row['Item']] / row['Count'])
        
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
            
    
assert checkout('FF') == 20
assert checkout('ABCD') == 115
assert checkout('AAA') == 130
assert checkout('AAAAA') == 200
assert checkout('EE') == 80
assert checkout('a') == -1
assert checkout('-') == -1
assert checkout('EEB') == 80
assert checkout('EEBB') == 110
assert checkout('EEEEEBBB') == 230
assert checkout('EEEEEBBBFF') == 250
assert checkout('EEEEEBBBFFF') == 250
assert checkout('EEEEEBBBFFFF') == 260
assert checkout('NNNM') == 120


# print(item_counter)
# if item_counter['B'] > 0:
#     item_counter['B'] -= floor(item_counter['E'] / 2)

# if item_counter['F'] >= 3:
#     item_counter['F'] -= floor(item_counter['F'] / 3)
# print(item_counter)

