import numpy as np
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

from jsplendor.env import JsplendorEnv

def main():
    np.random.seed(1)
    env = JsplendorEnv(verbose=True)
    exp = 'int32'
    model_path = 'logs/{}/best_model'.format(exp)

    model = PPO.load(model_path, env=env)
    print('load model.')

    for exp_i in range(10):
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
