# price array - [(w)hite, bl(u)e, (g)reen, (r)ed, blac(k)]
# price array - [w, u, g, r, k]

# level / VP / gem_color / price 
l1_list = [
    # level1 black
    (1, 0, 'black', [1, 1, 1, 1, 0]),
    (1, 0, 'black', [1, 2, 1, 1, 0]),
    (1, 0, 'black', [2, 2, 0, 1, 0]),
    (1, 0, 'black', [0, 0, 1, 3, 1]),
    (1, 0, 'black', [0, 0, 2, 1, 0]),
    (1, 0, 'black', [2, 0, 2, 0, 0]),
    (1, 0, 'black', [0, 0, 3, 0, 0]),
    (1, 1, 'black', [0, 4, 0, 0, 0]),

    # level1 blue
    (1, 0, 'blue', [1, 0, 1, 1, 1]),
    (1, 0, 'blue', [1, 0, 1, 2, 1]),
    (1, 0, 'blue', [1, 0, 2, 2, 0]),
    (1, 0, 'blue', [0, 1, 3, 1, 0]),
    (1, 0, 'blue', [1, 0, 0, 0, 2]),
    (1, 0, 'blue', [0, 0, 2, 0, 2]),
    (1, 0, 'blue', [0, 0, 0, 0, 3]),
    (1, 1, 'blue', [0, 0, 0, 4, 0]),

    # level1 white
    (1, 0, 'white', [0, 1, 1, 1, 1]),
    (1, 0, 'white', [0, 1, 2, 1, 1]),
    (1, 0, 'white', [0, 2, 2, 0, 1]),
    (1, 0, 'white', [3, 1, 0, 0, 1]),
    (1, 0, 'white', [0, 0, 0, 2, 1]),
    (1, 0, 'white', [0, 2, 0, 0, 2]),
    (1, 0, 'white', [0, 3, 0, 0, 0]),
    (1, 1, 'white', [0, 0, 4, 0, 0]),

    # level1 green
    (1, 0, 'green', [1, 1, 0, 1, 1]),
    (1, 0, 'green', [1, 1, 0, 1, 2]),
    (1, 0, 'green', [0, 1, 0, 2, 2]),
    (1, 0, 'green', [1, 3, 1, 0, 0]),
    (1, 0, 'green', [2, 1, 0, 0, 0]),
    (1, 0, 'green', [0, 2, 0, 2, 0]),
    (1, 0, 'green', [0, 0, 0, 3, 0]),
    (1, 1, 'green', [0, 0, 0, 0, 4]),

    # level1 red
    (1, 0, 'red', [1, 1, 1, 0, 1]),
    (1, 0, 'red', [2, 1, 1, 0, 1]),
    (1, 0, 'red', [2, 0, 1, 0, 2]),
    (1, 0, 'red', [1, 0, 0, 1, 3]),
    (1, 0, 'red', [0, 2, 1, 0, 0]),
    (1, 0, 'red', [2, 0, 0, 2, 0]),
    (1, 0, 'red', [3, 0, 0, 0, 0]),
    (1, 1, 'red', [4, 0, 0, 0, 0]),
]

l2_list = [
    # level2 black
    (2, 1, 'black', [3, 2, 2, 0, 0]),
    (2, 1, 'black', [3, 0, 3, 0, 2]),
    (2, 2, 'black', [0, 1, 4, 2, 0]),
    (2, 2, 'black', [0, 0, 5, 3, 0]),
    (2, 2, 'black', [5, 0, 0, 0, 0]),
    (2, 3, 'black', [0, 0, 0, 0, 6]),

    # level2 blue
    (2, 1, 'blue', [0, 2, 2, 3, 0]),
    (2, 1, 'blue', [0, 2, 3, 0, 3]),
    (2, 2, 'blue', [5, 3, 0, 0, 0]),
    (2, 2, 'blue', [2, 0, 0, 1, 4]),
    (2, 2, 'blue', [0, 5, 0, 0, 0]),
    (2, 3, 'blue', [0, 6, 0, 0, 0]),

    # level2 white
    (2, 1, 'white', [0, 0, 3, 2, 2]),
    (2, 1, 'white', [2, 3, 0, 3, 0]),
    (2, 2, 'white', [0, 0, 1, 4, 2]),
    (2, 2, 'white', [0, 0, 0, 5, 3]),
    (2, 2, 'white', [0, 0, 0, 5, 0]),
    (2, 3, 'white', [6, 0, 0, 0, 0]),

    # level2 green
    (2, 1, 'green', [3, 0, 2, 3, 0]),
    (2, 1, 'green', [2, 3, 0, 0, 2]),
    (2, 2, 'green', [4, 2, 0, 0, 1]),
    (2, 2, 'green', [0, 5, 3, 0, 0]),
    (2, 2, 'green', [0, 0, 5, 0, 0]),
    (2, 3, 'green', [0, 0, 6, 0, 0]),

    # level2 red
    (2, 1, 'red', [2, 0, 0, 2, 3]),
    (2, 1, 'red', [0, 3, 0, 2, 3]),
    (2, 2, 'red', [1, 4, 2, 0, 0]),
    (2, 2, 'red', [3, 0, 0, 0, 5]),
    (2, 2, 'red', [0, 0, 0, 0, 5]),
    (2, 3, 'red', [0, 0, 0, 6, 0]),
]

l3_list = [
    # level3 black
    (3, 3, 'black', [3, 3, 5, 3, 0]),
    (3, 4, 'black', [0, 0, 0, 7, 0]),
    (3, 4, 'black', [0, 0, 3, 6, 3]),
    (3, 5, 'black', [0, 0, 0, 7, 3]),

    # level3 blue
    (3, 3, 'blue', [3, 0, 3, 3, 5]),
    (3, 4, 'blue', [7, 0, 0, 0, 0]),
    (3, 4, 'blue', [6, 3, 0, 0, 3]),
    (3, 5, 'blue', [7, 3, 0, 0, 0]),

    # level3 white
    (3, 3, 'white', [0, 3, 3, 5, 3]),
    (3, 4, 'white', [0, 0, 0, 0, 7]),
    (3, 4, 'white', [3, 0, 0, 3, 6]),
    (3, 5, 'white', [3, 0, 0, 0, 7]),

    # level3 green
    (3, 3, 'green', [5, 3, 0, 3, 3]),
    (3, 4, 'green', [0, 7, 0, 0, 0]),
    (3, 4, 'green', [3, 6, 3, 0, 0]),
    (3, 5, 'green', [0, 7, 3, 0, 0]),

    # level3 red
    (3, 3, 'red', [3, 5, 3, 0, 3]),
    (3, 4, 'red', [0, 0, 7, 0, 0]),
    (3, 4, 'red', [0, 3, 6, 3, 0]),
    (3, 5, 'red', [0, 0, 7, 3, 0]),
]





