

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:

    if not isinstance(skus, str):
        return -1
    
    
