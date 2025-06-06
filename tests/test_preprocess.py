import pytest
import pandas as pd
from preprocess import clean_data

def test_clean_data_normalizes_date_column():
    # DataFrame with 'at' as string dates
    df = pd.DataFrame({
        'at': ['2024-06-01 12:34:56', '2024-06-02 08:00:00'],
        'A': [1, 2],
        'B': [3, 4]
    })
    cleaned = clean_data(df)
    assert pd.api.types.is_datetime64_any_dtype(cleaned['at'])
    # Should be normalized (time set to 00:00:00)
    assert all(cleaned['at'].dt.hour == 0)
    assert all(cleaned['at'].dt.minute == 0)
    assert all(cleaned['at'].dt.second == 0)

def test_clean_data_drops_columns_with_many_missing():
    # Column 'B' has 100% missing, should be dropped (threshold=0.75)
    df = pd.DataFrame({
        'at': ['2024-06-01', '2024-06-02', '2024-06-03'],
        'A': [1, 2, 3],
        'B': [None, None, None]
    })
    cleaned = clean_data(df)
    assert 'B' not in cleaned.columns
    assert 'A' in cleaned.columns

def test_clean_data_keeps_columns_below_threshold():
    # Column 'B' has 1/3 missing, below threshold=0.75, should NOT be dropped
    df = pd.DataFrame({
        'at': ['2024-06-01', '2024-06-02', '2024-06-03'],
        'A': [1, 2, 3],
        'B': [1, None, 3]
    })
    cleaned = clean_data(df)
    assert 'B' in cleaned.columns

def test_clean_data_no_missing_columns():
    # No columns should be dropped
    df = pd.DataFrame({
        'at': ['2024-06-01', '2024-06-02'],
        'A': [1, 2]
    })
    cleaned = clean_data(df)
    assert list(cleaned.columns) == ['at', 'A']

def test_clean_data_empty_dataframe():
    df = pd.DataFrame(columns=['at', 'A'])
    cleaned = clean_data(df)
    assert cleaned.empty
    assert list(cleaned.columns) == ['at', 'A']