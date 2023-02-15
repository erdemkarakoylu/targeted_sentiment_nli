from pathlib import Path
import sys

import numpy as np
#sys.path.append('../')
import pandas as pd
import pytest
from sklearn.datasets import make_classification

from src.nli_datamodule import split_data


@pytest.fixture
def dataframe_dir():
    return Path('../data/sentihood')

@pytest.fixture
def dataframe()->pd.DataFrame:
    return pd.read_json(dataframe_dir/'sentihood_dev.json')

def test_data_exists(dataframe_dir):
    assert dataframe_dir.exists()
    assert (dataframe_dir/'sentihood_dev.json').exists()
    assert (dataframe_dir/'sentihood_test.json').exists()
    assert (dataframe_dir/'sentihood_train.json').exists()

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