from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy

from jsplendor.env import JsplendorEnv

env = JsplendorEnv(verbose=False)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000, progress_bar=True)

mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

print('mean reward: {}'.format(mean_reward))
print('std reward: {}'.format(std_reward))

#vec_env = model.get_env()
#obs = vec_env.reset()
#for i in range(1000):
#    action, _state = model.predict(obs, deterministic=True)
#    obs, reward, done, info = vec_env.step(action)
