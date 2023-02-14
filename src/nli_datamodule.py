##from functools import partial
#from multiprocessing import cpu_count
#from pathlib import Path
import numpy as np
import pandas as pd
#from sklearn.model_selection import GroupShuffleSplit
from torch.utils.data import Dataset, DataLoader, random_split
#from transformers import AutoTokenizer
from pytorch_lightning import LightningDataModule

def split_data(d:pd.DataFrame, group_by_col:str, seed:int) -> tuple:
    pass

class NLIDataset(Dataset):
    
    def __init__(self):
        pass
    
    def __len__(self):
        pass

    def __getitem__(self):
        pass


class NLIDataModule(LightningDataModule):
    
    def __init__(self):
        pass

    def _split_data(self):
        pass

    def _set_tokenizer(self):
        pass

    def prepare_data(self) -> None:
        pass

    def setup(self):
        pass

    def training_dataloader(self):
        pass

    def validation_dataloader(self):
        pass
    
    def testing_dataloader(self):
        pass