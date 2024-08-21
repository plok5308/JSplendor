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

    def step(self, action):
        reward, is_done = self.game.run_with_action(action)

        terminated = False
        truncated = False

        if is_done:
            terminated = True
            reward = 10

        if self.game.step > 100:
            truncated = True

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