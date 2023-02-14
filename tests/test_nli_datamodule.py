import sys
#sys.path.append('../')
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
import pytest

from src.nli_datamodule import split_data

@pytest.fixture
def dataframe()->pd.DataFrame:
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