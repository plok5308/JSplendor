import torch
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed

from jsplendor.env import JsplendorEnv, FeatureExtractor
from jsplendor.utils import get_verbose_dict

def make_env(rank: int, seed: int=0):
    train_verbose_dict = get_verbose_dict()

    def _init():
        env = JsplendorEnv(train_verbose_dict)
        env.reset(seed=seed+rank)
        return env

    set_random_seed(seed)
    return _init

def main():
    eval_verbose_dict = get_verbose_dict()
    eval_verbose_dict['player'] = False
    num_cpu = 8

    train_env = SubprocVecEnv([make_env(i) for i in range(num_cpu)])

    eval_env = JsplendorEnv(eval_verbose_dict)
    exp = 'transformer_model-9967'
    eval_log_dir = 'logs/{}'.format(exp)

    train_steps = 100000000
    eval_freq = 10000

    eval_callback = EvalCallback(
        eval_env, 
        best_model_save_path=eval_log_dir,
        log_path=eval_log_dir, eval_freq=eval_freq,
        n_eval_episodes=10, deterministic=False,
        render=False)

    policy_kwargs = dict(
            features_extractor_class=FeatureExtractor,
            net_arch=[64],
            activation_fn=torch.nn.ReLU)

    model = PPO("MlpPolicy", 
                train_env, 
                n_steps=4096,
                learning_rate=1e-6,
                batch_size=512,
                verbose=False,
                policy_kwargs=policy_kwargs,
                tensorboard_log=eval_log_dir,
                )

    # load pretrained model
    trained_model = torch.load('./ckpt/model-9997.ckpt')
    state_dict = trained_model['state_dict']
    new_state_dict = dict()

    for key, value in state_dict.items():
        if 'model' in key:
            new_key = key[6::]
            new_state_dict[new_key] = value
        else:
            new_state_dict[key] = value

    model.policy.load_state_dict(new_state_dict)
    print('load action trained model.')

    model.learn(total_timesteps=train_steps, progress_bar=True, callback=eval_callback)
    print('train done.')


if __name__ == "__main__":
    main()
