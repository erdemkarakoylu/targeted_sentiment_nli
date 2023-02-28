from pathlib import Path
import numpy as np
import pandas as pd
import pytest

from src.nli_datamodule import NLIDataModule
from src.nli_model import LitNLI


@pytest.fixture(scope='session')
def data_directory():
    return Path('./data/')

@pytest.fixture(scope='session')
def acl_14_data(data_directory):
    return data_directory/'acl-14-short/clean'

@pytest.fixture(scope='session')
def sentfin_data(data_directory):
    return data_directory/'sentfin'

@pytest.fixture(scope='session')
def acl_14_train_dataframe(acl_14_data)->pd.DataFrame:
    return pd.read_json(acl_14_data/'df_train.json')

@pytest.fixture(scope="session")
def acl_14_test_dataframe(acl_14_data):
    return pd.read_json(acl_14_data/'df_test.json')

@pytest.fixture(scope='session')
def sentfin_dataframe(sentfin_data):
    return pd.read_json(sentfin_data/'data.json')

@pytest.fixture(scope='session')
def df_data_types_dict():
    data_types = {
        'text': np.dtype('O'), 'target': np.dtype('O'), 
        'polarity': np.dtype('int64')}
    return data_types

@pytest.fixture(scope='session')
def datamodule():
    dm = NLIDataModule()
    return dm

@pytest.fixture(scope='session')
def nli_model():
    model = LitNLI()
    return model