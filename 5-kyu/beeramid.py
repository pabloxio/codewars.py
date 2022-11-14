# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/python

def beeramid(bonus: int, price: int, level: int = 1) -> int:
    """
    >>> beeramid(-1, 4)
    0
    >>> beeramid(9, 2)
    1
    >>> beeramid(5000, 3)
    16
    >>> beeramid(21, 1.5)
    3
    >>> beeramid(1500, 2)
    12
    """
    bill = price * level**2
    if bonus < 0 or bill > bonus:
        return level - 1

    return beeramid(bonus - bill, price, level+1)
