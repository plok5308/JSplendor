import numpy as np
from gymnasium import spaces

from jsplendor.game import Game
from jsplendor.utils import Element

def get_observation_space():
    # step
    # spaces.Box(low=0, high=300, shape=(1,), dtype=np.int32)

    #[player]
    #coin observation
    #spaces.Box(low=0, high=4, shape=(6,), dtype=np.uint8)
    #development observation
    #spaces.Box(low=0, high=20, space=(5,), dtype=np.uint8)
    #victory point observation
    #spaces.Box(low=0, high=30, spaces=(1,), dtype=np.uint8)

    #[board]
    #coin
      #spaces.Box(low=0, high=5, shape=(6,), dtype=np.uint8)
    #table cards observation (single)
      #price - spaces.Box(low=0, high=7, spaces=(5,), dtype=np.uint8)
      #victory point - spaces.Box(low=0, high=20, spaces=(1,), dtype=np.uint8)

    #noble cards
      #price - spaces.Box(low=0, high=4, spaces=(5,), dtype=np.uint8)
      #victory point - spaces.Box(low=0, high=20, spaces=(1,), dtype=np.uint8)


    # 1 + 6 + 5 + 1 + (6 * 12) + (6 * 3)= 102

    observation_space = spaces.Box(low=0, high=30, shape=(103,), dtype=np.int32)
    return observation_space

def get_observation(game: Game):
    player1 = game.player1
    board = game.board

    obs0 = get_step_obs(game)
    obs1 = get_coin_obs(player1)
    obs2 = get_player_development_obs(player1)
    obs3 = get_player_victory_point_obs(player1)

    obs4 = get_table_cards_obs(board)

    obs = np.concatenate([obs0, obs1, obs2, obs3, obs4])
    obs = obs.astype(np.int32)

    return obs

def get_step_obs(game):
    x = np.zeros(1, dtype=np.int32)
#    x[0] = game.step / 300
    x[0] = game.step

    return x

def get_coin_obs(player):
    coins = player.coins
    x = np.zeros(6, dtype=np.int32)
    for key, value in coins.items():
        x[Element[key].value] = value

#    x = x/4

    return x

def get_player_development_obs(player):
    cards = player.development_cards
    x = np.zeros(5, dtype=np.int32)
    for card in cards:
        x[Element[card.gem_color].value] += 1

#    x = x / 20

    return x

def get_player_victory_point_obs(player):
    x = np.zeros(1, dtype=np.int32)
    x[0] = player.sum_victory_point

#    x = x / 30

    return x

def get_table_cards_obs(board):
    cards = board.flatten_table_cards
    
    for idx, card in enumerate(cards):
        if idx==0:
            obs = get_table_card_obs(card)
        else:
            obs_ = get_table_card_obs(card)
            obs = np.concatenate([obs, obs_])

    cards = board.noble_cards
    for card in cards:
        obs_ = get_table_card_obs(card)
        obs = np.concatenate([obs, obs_])

    return obs

def get_table_card_obs(card):
    if card is None:
        x = np.ones(6, dtype=np.int32) * -1

    else:
        x = np.zeros(6, dtype=np.int32)
        x[0:5] += card.price
        x[5] = card.victory_point

#        x = x / 10

    return x
