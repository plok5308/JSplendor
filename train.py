import torch
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback

from jsplendor.env import JsplendorEnv
from jsplendor.utils import get_verbose_dict

def main():
    train_verbose_dict = get_verbose_dict()
    eval_verbose_dict = get_verbose_dict()
    eval_verbose_dict['player'] = True

    train_env = JsplendorEnv(train_verbose_dict)
    eval_env = JsplendorEnv(eval_verbose_dict)
    exp = 'int32_refactoring'
    eval_log_dir = 'logs/{}'.format(exp)

    train_steps = 10000000
    eval_freq = 10000

    eval_callback = EvalCallback(
        eval_env, 
        best_model_save_path=eval_log_dir,
        log_path=eval_log_dir, eval_freq=eval_freq,
        n_eval_episodes=5, deterministic=True,
        render=False)

    model = PPO("MlpPolicy", 
                train_env, 
                verbose=False,
                policy_kwargs=dict(net_arch=[256, 256, 256], activation_fn=torch.nn.ReLU),
                tensorboard_log=eval_log_dir)

    model.learn(total_timesteps=train_steps, progress_bar=True, callback=eval_callback)
    print('train done.')


if __name__ == "__main__":
    main()
