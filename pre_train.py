import torch
from torch import optim
from torch.utils.data import Dataset, DataLoader
from torchmetrics.classification import BinaryAccuracy
import numpy as np
import h5py
from stable_baselines3 import PPO
import lightning as L
from lightning.pytorch.callbacks import ModelCheckpoint

from jsplendor.env import JsplendorEnv, FeatureExtractor, get_observation_space


class LitModel(L.LightningModule):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.loss = torch.nn.BCELoss()
        self.train_acc = BinaryAccuracy()
        self.valid_acc = BinaryAccuracy()

    def training_step(self, batch, batch_idx):
        obs = batch[0]
        actions_bool = batch[1].float()

        y1 = self.model.extract_features(obs)
        y2 = self.model.mlp_extractor.policy_net(y1)
        y3 = self.model.action_net(y2)
        y4 = torch.sigmoid(y3)

        loss = self.loss(y4, actions_bool)
        acc = self.train_acc(y4, actions_bool)
        self.log('train_loss', loss, prog_bar=True)
        self.log('train_acc', acc, prog_bar=True)

        return loss

    def validation_step(self, batch, batch_idx):
        obs = batch[0]
        actions_bool = batch[1].float()

        y1 = self.model.extract_features(obs)
        y2 = self.model.mlp_extractor.policy_net(y1)
        y3 = self.model.action_net(y2)
        y4 = torch.sigmoid(y3)

        loss = self.loss(y4, actions_bool)
        acc = self.valid_acc(y4, actions_bool)
        self.log('valid_loss', loss, prog_bar=True)
        self.log('valid_acc', acc, prog_bar=True)

    def configure_optimizers(self):
        optimizer = optim.Adam(self.parameters(), lr=1e-3)
        return optimizer


class HDF5Dataset(Dataset):
    def __init__(self, hdf5_file_list):
        for idx, hdf5_file in enumerate(hdf5_file_list):
            datas = h5py.File(hdf5_file, 'r')
            obs = datas['obs']
            actions_bool = datas['actions_bool']

            if idx==0:
                full_obs = obs
                full_actions_bool = actions_bool
            else:
                full_obs = np.concatenate([full_obs, obs], axis=0)
                full_actions_bool = np.concatenate([full_actions_bool, actions_bool], axis=0)

        self.obs = full_obs
        self.actions_bool = full_actions_bool

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


    train_files = [
        'data/data_0.h5',
        'data/data_1.h5',
        'data/data_2.h5',
        'data/data_3.h5',
    ]

    valid_files = [
        'data/data_10.h5',
    ]

    num_workers = 8
    train_dataset = HDF5Dataset(train_files)
    train_dataloader = DataLoader(train_dataset, batch_size=512, shuffle=True, num_workers=num_workers)

    valid_dataset = HDF5Dataset(valid_files)
    valid_dataloader = DataLoader(valid_dataset, batch_size=512, num_workers=num_workers)

    checkpoint_callback = ModelCheckpoint(
            monitor='valid_acc',
            save_top_k=3,
            filename='{epoch}-{valid_acc}',
            mode='max'
            )

    system = LitModel(model.policy)
#    state_dict = torch.load('./ckpt/e120.ckpt')['state_dict']
#    system.load_state_dict(state_dict)
#    print('load ckpt file.')

    trainer = L.Trainer(
            val_check_interval=0.1, 
            callbacks=checkpoint_callback)

    trainer.fit(system, 
                train_dataloader,
                valid_dataloader,
                )

    print('done')


if __name__ == "__main__":
    main()
