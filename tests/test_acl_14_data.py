"""
This module contains tests all "cleaned datasets". 
Data are assumed to be in  PanDaS dataframes. 
Author: Erdem Karaköylü
Created: 2/15/2023
"""

from src.constants import DATA_COLUMNS

def test_duplicate_rows(acl_14_train_dataframe, acl_14_test_dataframe):
    """This functions tests ACL 14 train and test dataframes for duplicate rows."""
    train_dup = acl_14_train_dataframe[acl_14_train_dataframe.duplicated()]
    test_dup = acl_14_test_dataframe[acl_14_test_dataframe.duplicated()]
    assert train_dup.empty
    assert test_dup.empty

def test_dataframe_column_dtypes(
        acl_14_train_dataframe, acl_14_test_dataframe, df_data_types_dict):
    assert acl_14_train_dataframe.dtypes.to_dict() == df_data_types_dict
    assert acl_14_test_dataframe.dtypes.to_dict() == df_data_types_dict

def test_dataframe_columns(
        acl_14_train_dataframe, acl_14_test_dataframe):
    assert set(acl_14_train_dataframe.columns.tolist()) == set(DATA_COLUMNS)
    assert set(acl_14_test_dataframe.columns.tolist()) == set(DATA_COLUMNS)