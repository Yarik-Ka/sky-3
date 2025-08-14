# transactions.py
from typing import List, Dict, Any
import pandas as pd


def read_transactions_csv(filepath: str) -> List[Dict[str, Any]]:
    """
    Reads financial transactions from a CSV file and returns a list of dictionaries.

    :param filepath: Path to the CSV file.
    :return: List of dictionaries representing transactions.
    """
    df = pd.read_csv(filepath)
    return df.to_dict(orient='records')


def read_transactions_xlsx(filepath: str) -> List[Dict[str, Any]]:
    """
    Reads financial transactions from an Excel file and returns a list of dictionaries.

    :param filepath: Path to the Excel file.
    :return: List of dictionaries representing transactions.
    """
    df = pd.read_excel(filepath)
    return df.to_dict(orient='records')