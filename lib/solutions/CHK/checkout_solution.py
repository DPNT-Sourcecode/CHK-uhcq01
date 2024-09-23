import pandas as pd
from math import floor
import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    pricings = pd.DataFrame({
        'Item': ['A','B','C','D'],
        'Price': [50, 30, 20, 15],
        'Special offer count': [3, 2, None, None],
        'Special offer price': [130, 45, None, None]
    })

    if not isinstance(skus, str):
        return -1 # Input was not a string
    
    filtered_skus = re.sub(r'[^ABCD]', '', skus)
    if len(filtered_skus) < len(skus):
        return -1 # Invalid characters were present
    
    
    total = 0

    for i, row in pricings.iterrows():
        
        n = filtered_skus.count(row['Item']) # Occurrences of the item in the basket

        if row['Special offer count'] is not None and n >= row['Special offer count']:
            offer_count = floor(n / row['Special offer count'])
            remainder = n - (row['Special offer count'] * offer_count)

            total += offer_count * row['Special offer price']
            total += remainder * row['Price']

        else:
            total += n * row['Price']

    return int(total)
            
    
print(checkout('ABCD'))
print(checkout('AAA'))
print(checkout('BBBBB'))
print(checkout('AAAAAA'))
print(checkout('a'))
print(checkout('-'))
