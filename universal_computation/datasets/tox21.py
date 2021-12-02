from universal_computation.datasets.dataset import Dataset

from torch_geometric.datasets import MoleculeNet
from torch_geometric.data import DataLoader

class Tox21Dataset(Dataset):

    def __init__(self, batch_size, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = MoleculeNet(root="data/tox21", name="Tox21")
        self.data_size = len(self.data)

        self.d_train = DataLoader(
            self.data[:int(self.data_size * .8)], batch_size=batch_size, drop_last=True, shuffle=True,
        )
        self.d_test = DataLoader(
            self.data[int(self.data_size * .8):], batch_size=batch_size, drop_last=True, shuffle=True,
        )

        self.train_enum = enumerate(self.d_train)
        self.test_enum = enumerate(self.d_test)

    def get_batch(self, batch_size=None, train=True):
        if train:
            _, (x, y) = next(self.train_enum, (None, (None, None)))
            if x is None:
                self.train_enum = enumerate(self.d_train)
                _, (x, y) = next(self.train_enum)
        else:
            _, (x, y) = next(self.test_enum, (None, (None, None)))
            if x is None:
                self.test_enum = enumerate(self.d_test)
                _, (x, y) = next(self.test_enum)

        x = x.to(device=self.device)
        y = y.to(device=self.device)

        self._ind += 1

        return x, y
