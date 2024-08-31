import torch
from gymnasium import spaces
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
from x_transformers import TransformerWrapper, Encoder


class FeatureExtractor(BaseFeaturesExtractor):
    def __init__(self, observation_space: spaces.Box):
        super().__init__(observation_space, features_dim=256) 
        self.model = TransformerWrapper(
                num_tokens = 256,
                max_seq_len = 128,
                attn_layers = Encoder(
                    dim = 128,
                    depth = 4,
                    heads = 4
                )
            )

    def forward(self, observations: torch.Tensor) -> torch.Tensor:
        x = self.model(observations)
        x = x[:, 0, :]  # [batch, length, dim] -> [batch, dim] (select first data).
        return x
