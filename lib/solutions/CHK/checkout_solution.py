import pandas as pd
from math import floor
from collections import Counter
import re


    # pricings = pd.DataFrame({
    #     'Item': ['A','B','C','D'],
    #     'Price': [50, 30, 20, 15],
    #     'Special offer count': [3, 2, None, None],
    #     'Special offer price': [130, 45, None, None]
    # })
    
# noinspection PyUnusedLocal
# skus = unicode string

def checkout(skus: str) -> int:


    items = ['A','B','C','D','E']

    pricings = pd.DataFrame({
        'Item': ['A', 'A', 'B', 'C', 'D', 'E'],
        'Price': [50, 50, 30, 20, 15],
        'Special offer count': [3, 5, 2, None, None, 2],
        'Special offer price': [130, 200, 45, None, None, '-B']
    })

    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCD]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    total = 0

    for item in items:
        n = filtered_skus.count(item) # Occurrences of the item in the basket

        if row['Special offer count'] is not None and n >= row['Special offer count']:
            offer_count = floor(n / row['Special offer count'])
            remainder = n - (row['Special offer count'] * offer_count)
            total += offer_count * row['Special offer price']
            total += remainder * row['Price']

        else:
            total += n * row['Price']

    return int(total)
            
    
def checkout(skus: str) -> int:

    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCD]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    total = 0

    item_counts = Counter(filtered_skus)

    if 'E'
    

print(checkout('ABCD'))
print(checkout('AAA'))
print(checkout('BBBBB'))
print(checkout('AAAAAA'))
print(checkout('a'))
print(checkout('-'))




