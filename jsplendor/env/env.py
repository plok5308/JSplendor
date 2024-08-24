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
        self.step_log = 0
        self.skip_sum = 0

        # parameters
        self.target_vp = 1
        self.max_step = 100
        self.penalty = dict()
        self.penalty['invalid'] = 0.1
        self.penalty['over_coin'] = 0.1
        self.penalty['step_over'] = 10
        self.reward = dict()
        self.reward['get_card'] = 5
        self.reward['reach_goal'] = 10

    def step(self, action):
        self.step_log += 1
        terminated = False
        truncated = False

        if self.step_log > self.max_step:
            reward = -1 * self.penalty['step_over']
            if self.verbose:
                print('reward: {}'.format(reward))
            terminated = True
        else:
            reward, terminated = self._run_action(action)

        observation = get_observation(self.game)
        info = dict()

        return observation, reward, terminated, truncated, info

    def _run_action(self, action):
        terminated = False
        action_result = self.game.run_with_action(action)
        # action_result = dict()
        # action_result['victory_point'] = 0
        # action_result['over_coin_count'] = 0
        # action_result['is_skip'] = False
        # action_result['is_get_card'] = False

        if action_result['is_skip']:
            self.skip_sum += 1
            reward = -1 * self.penalty['invalid']
            if self.verbose:
                print('is skip. reward: {}'.format(reward))

        else:
            if action_result['victory_point'] >= self.target_vp:
                reward = self.reward['reach_goal']
                if self.verbose:
                    print('player reach the VP at step {}.'.format(self.step_log))
                    print('skip ratio: {}.'.format(self.skip_sum / self.step_log))
                    print('reward: {}'.format(reward))

                terminated = True

            else:
                reward = 0
                if self.verbose:
                    print('reward: {}'.format(reward))

        # adjust reward
        if action_result['is_get_card']:
            reward += self.reward['get_card']
        
        if action_result['over_coin_count'] > 0:
            reward -= self.penalty['over_coin'] * action_result['over_coin_count']

        return reward, terminated

    def reset(self, seed=None, options=None):
        self.step_log = 0
        self.skip_sum = 0
        self.game.reset()
        observation = get_observation(self.game)
        info = {}

        return observation, info

    def render(self):
        pass

    def close(self):
        pass