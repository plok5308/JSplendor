from enum import Enum

class Element(Enum):
    WHITE=0
    BLUE=1
    GREEN=2
    RED=3
    BLACK=4
    GOLD=5

def get_verbose_dict():
    verbose_dict = dict()
    verbose_dict['env'] = False
    verbose_dict['game'] = False
    verbose_dict['board'] = False
    verbose_dict['player'] = False

    return verbose_dict