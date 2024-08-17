from jsplendor.utils import Element


def get_coin_dictionary():
    coins = dict()
    for name in Element.__members__.keys():
        coins[name] = 0

    return coins

def get_full_coin_for_board():
    coins = get_coin_dictionary()
    coins["WHITE"] = 4
    coins["BLUE"] = 4
    coins["GREEN"] = 4
    coins["RED"] = 4
    coins["BLACK"] = 4
    coins["GOLD"] = 5

    return coins

def get_empty_coin():
    coins = get_coin_dictionary()
    return coins
    
