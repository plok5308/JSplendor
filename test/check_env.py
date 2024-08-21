from stable_baselines3.common.env_checker import check_env

from jsplendor.env import JsplendorEnv

env = JsplendorEnv(verbose=True)
check_env(env)
