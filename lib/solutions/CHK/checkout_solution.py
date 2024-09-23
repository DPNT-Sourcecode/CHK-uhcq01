import pandas as pd

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    pricings = pd.DataFrame({
        'Item': ['A','B','C','D'],
        'Price': [50, 30, 20, 15],
        'Special offers': ['3A for 130', '2B for 45', None, None]
    })

    print(pricings)

    if not isinstance(skus, str):
        return -1
    
checkout('sdas')
