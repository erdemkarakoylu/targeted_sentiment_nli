from pathlib import Path
import sys

import numpy as np
#sys.path.append('../')
import pandas as pd
import pytest
from sklearn.datasets import make_classification

from src.nli_datamodule import split_data


@pytest.fixture
def data_directory():
    return Path('../data/sentihood')

@pytest.fixture
def dataframe(data_directory)->pd.DataFrame:
    return pd.read_json(data_directory/'sentihood_dev.json')

def test_data_exists(data_directory):
    assert data_directory.exists()
    assert (data_directory/'sentihood_dev.json').exists()
    assert (data_directory/'sentihood_test.json').exists()
    assert (data_directory/'sentihood_train.json').exists()

def test_dataframe_columns(dataframe):
    pass

def test_split_data():
    pass

def test_set_tokenizer():
    pass

def test_prepare_data():
    pass

def test_setup():
    pass

def test_training_dataloader():
    pass

def test_validation_dataloader():
    pass

def test_testing_dataloader():
    pass