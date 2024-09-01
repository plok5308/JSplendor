import numpy as np
import gymnasium as gym
from gymnasium import spaces

from jsplendor.game import Game
from jsplendor.env.observation import get_observation_space, get_observation
from jsplendor.utils import get_verbose_dict


class JsplendorEnv(gym.Env):
    def __init__(self, verbose_dict=None):
        if verbose_dict is None:
            verbose_dict = get_verbose_dict()
        else:
            verbose_dict = verbose_dict

        self.game = Game(verbose_dict)
        action_n = self.game.player1.num_actions
        self.action_space = spaces.Discrete(action_n)
        self.observation_space = get_observation_space()
        self.verbose = verbose_dict['env']
        self.skip_sum = 0

        # parameters
        self.target_vp = 15
        self.max_step = 127
        self.penalty = dict()
        self.penalty['invalid'] = 0.1
        self.penalty['over_coin'] = 0
        self.penalty['step_over'] = 10

        self.reward = dict()
        self.reward['get_card'] = 0
        self.reward['reach_goal'] = 50  # final_reward = reach_goal - step

    def step(self, action):
        terminated = False
        truncated = False

        reward, terminated, step_ = self._run_action(action)

        if step_ >= self.max_step:
            reward = -1 * self.penalty['step_over']
            if self.verbose:
                print('reward: {}'.format(reward))
            terminated = True
        else:
            if self.verbose:
                print('reward: {}'.format(reward))

        observation = get_observation(self.game)
        info = dict()

        return observation, reward, terminated, truncated, info

    def get_possible_actions(self):
        return self.game.player1.get_all_possible_actions(self.game.board)

    def _run_action(self, action):
        terminated = False
        action_result = self.game.run_with_action(action)
        # action_result = dict()
        # action_result['victory_point'] = 0
        # action_result['over_coin_count'] = 0
        # action_result['is_skip'] = False
        # action_result['is_get_card'] = False
        # action_result['step'] = int
        step_ = action_result['step']

        if action_result['is_skip']:
            self.skip_sum += 1
            reward = -1 * self.penalty['invalid']
            if self.verbose:
                print('is skip.')

        else:
            if action_result['victory_point'] >= self.target_vp:
                #reward = self.reward['reach_goal']
                reward = self.reward['reach_goal'] - step_

                if self.verbose:
                    print('player reach the VP at step {}.'.format(step_))
                    print('skip ratio: {}.'.format(self.skip_sum / step_))

                terminated = True

            else:
                if self.verbose:
                    print('VP: {}'.format(action_result['victory_point']))

                reward = 0

        # adjust reward
        if action_result['is_get_card']:
            reward += self.reward['get_card']
        
        if action_result['over_coin_count'] > 0:
            reward -= self.penalty['over_coin'] * action_result['over_coin_count']

        return reward, terminated, step_

    def reset(self, seed=None, options=None):
        np.random.seed(seed)
        self.skip_sum = 0
        self.game.reset()
        observation = get_observation(self.game)
        info = {}

        return observation, info

    def render(self):
        pass

    def close(self):
        pass
