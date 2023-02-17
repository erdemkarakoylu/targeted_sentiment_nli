from pathlib import Path
import pandas as pd
import pytest


@pytest.fixture(scope='session')
def data_directory():
    return Path('../data/')

@pytest.fixture(scope='session')
def acl_14_data(data_directory):
    return data_directory/'acl-14-short/clean'

@pytest.fixture(scope='session')
def sentfin_data(data_directory):
    return data_directory/ 'sentfin'

@pytest.fixture(scope='session')
def acl_14_dataframe(acl_14_data)->pd.DataFrame:
    return pd.read_json(acl_14_data/'acl_14_all.json')

@pytest.fixture(scope='session')
def sentfin_dataframe(sentfin_data):
    return pd.read_json(sentfin_data/'data.json')