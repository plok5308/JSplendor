import torch
from torch import optim
from torch.utils.data import Dataset, DataLoader
from torchmetrics.classification import BinaryAccuracy
import h5py
from stable_baselines3 import PPO
import lightning as L

from jsplendor.env import JsplendorEnv, FeatureExtractor, get_observation_space


class LitModel(L.LightningModule):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.loss = torch.nn.BCELoss()
        self.acc = BinaryAccuracy()

    def training_step(self, batch, batch_idx):
        obs = batch[0]
        actions_bool = batch[1].float()

        y1 = self.model.extract_features(obs)
        y2 = self.model.mlp_extractor.policy_net(y1)
        y3 = self.model.action_net(y2)
        y4 = torch.sigmoid(y3)

        loss = self.loss(y4, actions_bool)

        return loss

    def validation_step(self, batch, batch_idx):
        obs = batch[0]
        actions_bool = batch[1].float()

        y1 = self.model.extract_features(obs)
        y2 = self.model.mlp_extractor.policy_net(y1)
        y3 = self.model.action_net(y2)
        y4 = torch.sigmoid(y3)

        acc = self.acc(y4, actions_bool)
        self.log('acc', acc, prog_bar=True)

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer


class HDF5Dataset(Dataset):
    def __init__(self, hdf5_file):
        self.file = h5py.File(hdf5_file, 'r')
        self.obs = self.file['obs']
        self.actions_bool = self.file['actions_bool']

    def __len__(self):
        return len(self.obs)

    def __getitem__(self, idx):
        obs = self.obs[idx]
        actions_bool = self.actions_bool[idx]

        obs = torch.from_numpy(obs).long()
        actions_bool = torch.from_numpy(actions_bool).long()

        return obs, actions_bool


def main():
    exp = 'pre_train'
    exp_log = 'logs/{}'.format(exp)
    env = JsplendorEnv()

    policy_kwargs = dict(
            features_extractor_class=FeatureExtractor,
            net_arch=[64],
            activation_fn=torch.nn.ReLU)

#    model = FeatureExtractor(get_observation_space())
    model = PPO("MlpPolicy",
                 env,
                 verbose=False,
                 policy_kwargs=policy_kwargs,
                 tensorboard_log=exp_log)


    dataset = HDF5Dataset('test.h5')
    train_dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

    dataset2 = HDF5Dataset('test.h5')
    valid_dataloader = DataLoader(dataset, batch_size=32)


    system = LitModel(model.policy)

    trainer = L.Trainer()
    trainer.fit(system, 
                train_dataloader,
                valid_dataloader,
                )

    import pdb; pdb.set_trace()
    print('done')


if __name__ == "__main__":
    main()
