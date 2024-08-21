import gymnasium as gym
from gymnasium import spaces

from jsplendor.game import Game
from jsplendor.env.observation import get_observation_space, get_observation


class JsplendorEnv(gym.Env):
    def __init__(self, verbose):
        self.game = Game(verbose)
        action_n = self.game.player1.num_actions
        self.action_space = spaces.Discrete(action_n)
        self.observation_space = get_observation_space()
        self.verbose = verbose
        self.step_log = 0
        self.skip_sum = 0

    def step(self, action):
        self.step_log += 1
        reward, is_done, is_skip = self.game.run_with_action(action)
        self.skip_sum += is_skip

        terminated = False
        truncated = False

        if is_done:
            reward = (200 - self.step_log) / 10
            print('player reach the 15 VP at step {}.'.format(self.step_log))
            print('skip ratio: {}.'.format(self.skip_sum / self.step_log))
            print('reward: {}'.format(reward))

            terminated = True

            self.step_log = 0
            self.skip_sum = 0
        elif self.step_log > 300:
            reward = -10
            print('reward: {}'.format(reward))
            terminated = True
            #truncated = True
            self.step_log = 0
            self.skip_sum = 0
        else:
            pass

        observation = get_observation(self.game)
        info = dict()

        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        self.game.reset()
        observation = get_observation(self.game)
        info = {}

        return observation, info

    def render(self):
        pass

    def close(self):
        pass