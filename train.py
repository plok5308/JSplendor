from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

from jsplendor.env import JsplendorEnv

def main():
    env = JsplendorEnv(verbose=True)
    exp = 'test'

    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=1000000, progress_bar=True)
    model.save('models/{}'.format(exp))
    print('train done.')


if __name__ == "__main__":
    main()
