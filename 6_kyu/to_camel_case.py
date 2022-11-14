# https://www.codewars.com/kata/517abf86da9663f1d2000003/python

import re


def to_camel_case(text: str):
    """
    >>> to_camel_case("the-stealth-warrior")
    'theStealthWarrior'
    >>> to_camel_case("The_Stealth_Warrior")
    'TheStealthWarrior'
    >>> to_camel_case("")
    ''
    >>> to_camel_case("the_stealth_warrior")
    'theStealthWarrior'
    >>> to_camel_case("The-Stealth-Warrior")
    'TheStealthWarrior'
    >>> to_camel_case("The_pippi-was-Omoshiroi")
    'ThePippiWasOmoshiroi'
    """
    words = re.split("-|_", text)
    return "".join([words[0]] + [word.title() for word in words[1:]])
