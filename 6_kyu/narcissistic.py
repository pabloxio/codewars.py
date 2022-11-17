# https://www.codewars.com/kata/5287e858c6b5a9678200083c/python


def narcissistic(value):
    """
    >>> narcissistic(7)
    True
    >>> narcissistic(371)
    True
    >>> narcissistic(122)
    False
    >>> narcissistic(4887)
    False
    """
    return value == sum([int(n)**len(str(value)) for n in str(value)])

