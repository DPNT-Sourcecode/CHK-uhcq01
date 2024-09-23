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
        n = skus.count(row['Item'])

        if row['Special offer count'] is not None:

            floor(n / row['Special offer count'])


   
        # price = pricings[pricings['Item'] == item]['Price'].values[0]
        # total += n * price
        # print(f"item: {item}, count: {n}, price: {total}")
    
checkout('ABCD')

