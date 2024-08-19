import numpy as np
import itertools

from jsplendor.utils import Element

def adjust_price(price, point):
    """
    args:
        price - np.array(5)
        point - np.array(5)
    """
    price = price - point
    price = np.maximum(price, 0)

    return price

def get_coin_comb(x):
    assert(x>=0 and x<10)
    lst = [0, 1, 2, 3, 4]
    combinations = list(itertools.combinations(lst, 3))

    return combinations[x]