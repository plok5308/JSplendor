from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

from jsplendor.env import JsplendorEnv

def main():
    env = JsplendorEnv(verbose=True)
    exp = 'train-10M'

    model = PPO("MlpPolicy", env, verbose=1)
    model.load('models/{}'.format(exp))
    print('load model.')

    vec_env = model.get_env()
    obs = vec_env.reset()
    for i in range(1000):
        print('[step {}]'.format(i))
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, done, info = vec_env.step(action)
        if done:
            break

    print('done')


if __name__ == "__main__":
    main()
