"""Tests in this script test the data located in data/sentfin."""
from src.constants import DATA_COLUMNS


def test_duplicate_rows(sentfin_dataframe):
    duplicated_df = sentfin_dataframe[sentfin_dataframe.duplicated()]
    assert duplicated_df.empty

def test_dataframe_column_dtypes(sentfin_dataframe, df_data_types_dict):
    assert sentfin_dataframe.dtypes.to_dict() == df_data_types_dict


def test_dataframe_columns(sentfin_dataframe):
    assert set(sentfin_dataframe.columns.tolist()) == set(DATA_COLUMNS)
