# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x: int, y: int) -> int:

    if not isinstance(x, int):
        raise Exception('x must be of type integer')
    
    if not isinstance(y, int):
        raise Exception('y must be of type integer')

    if x >= 0 and x <= 100 and y >= 0 and y <= 100:
        return x + y
    else:
        raise Exception('x or y not in range 0 - 100')