import os
import h5py
import numpy as np
import argparse
from tqdm import tqdm

from jsplendor.game import Game
from jsplendor.env import get_observation

def save_data(filename, total_obs, total_actions):
    with h5py.File(filename, 'w') as h5file:
        h5file.create_dataset('obs', data=total_obs)
        h5file.create_dataset('actions_bool', data=total_actions)

    print("Data successfully written to {}".format(filename))


def main(args):
    game = Game()
    data_n = 10000
    limit_victory_point = 20

    init_obs = get_observation(game)
    total_obs = np.zeros((data_n, len(init_obs)))
    total_actions = np.zeros((data_n, game.player1.num_actions))

    for i in tqdm(range(data_n)):
        obs = get_observation(game)
        action, action_result, possible_actions = game.get_random_action_datas()

        total_obs[i] = obs
        total_actions[i] = possible_actions
        if (action_result['victory_point'] > limit_victory_point) or game.step >= 255:
            game.reset()

    os.makedirs('./data', exist_ok=True) 
    save_data('./data/data_{}.h5'.format(args.idx), total_obs, total_actions)

    print('done')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--idx', default=0)
    args = parser.parse_args()
    main(args)
