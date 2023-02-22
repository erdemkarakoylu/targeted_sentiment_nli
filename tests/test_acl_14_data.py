"""Tests in this script test the data located in data/sentfin."""

from src.constants import DATA_COLUMNS

def test_duplicate_rows(acl_14_dataframe):
    duplicated_df = acl_14_dataframe[acl_14_dataframe.duplicated()]
    assert duplicated_df.empty

def test_dataframe_column_dtypes(acl_14_dataframe, df_data_types_dict):
    assert acl_14_dataframe.dtypes.to_dict() == df_data_types_dict

def test_dataframe_columns(acl_14_dataframe):
    assert set(acl_14_dataframe.columns.tolist()) == set(DATA_COLUMNS)
