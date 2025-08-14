# test_transactions.py
from unittest.mock import patch

import pytest

from src.transactions import read_transactions_csv, read_transactions_xlsx


@pytest.fixture
def mock_df():
    class DummyDataFrame:
        pass
    return DummyDataFrame()

@patch('pandas.read_csv')
def test_read_transactions_csv(mock_read_csv, mock_df):
    mock_read_csv.return_value = mock_df
    result = read_transactions_csv('fake_path.csv')
    assert isinstance(result, list)
    assert result == [
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 200}
    ]
    mock_read_csv.assert_called_once_with('fake_path.csv')

@patch('pandas.read_excel')
def test_read_transactions_xlsx(mock_read_excel, mock_df):
    mock_read_excel.return_value = mock_df
    result = read_transactions_xlsx('fake_path.xlsx')
    assert isinstance(result, list)
    assert result == [
        {'id': 1, 'amount': 100},
        {'id': 2, 'amount': 200}
    ]
    mock_read_excel.assert_called_once_with('fake_path.xlsx')