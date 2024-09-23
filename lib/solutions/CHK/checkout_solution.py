import pandas as pd
from math import floor

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
        return -1
    
    if len(skus) == 0:
        return -1
    
    total = 0

    for i, row in pricings.iterrows():
        
        n = skus.count(row['Item']) # Occurrences of the item in the basket

        if row['Special offer count'] is not None and n >= row['Special offer count']:

            offer_count = floor(n / row['Special offer count'])
            remainder = n - (row['Special offer count'] * offer_count)

            total += offer_count * row['Special offer price']
            total += remainder * row['Price']

        else:

            total += n * row['Price']

    return total
            
    
print(checkout('ABCD'))
print(checkout('AAA'))