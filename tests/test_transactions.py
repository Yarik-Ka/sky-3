# test.py

import unittest
import pandas as pd
from src.transactions import read_transactions_csv, read_transactions_xlsx

class TestReadFiles(unittest.TestCase):
    def test_read_csv(self):
        df = read_transactions_csv('transactions.csv')
        self.assertIsInstance(df, pd.DataFrame)
        # Проверка наличия ожидаемых колонок (замените на реальные названия колонок вашего файла)
        self.assertIn('amount', df.columns)

    def test_read_xlsx(self):
        df = read_transactions_xlsx('transactions_excel.xlsx')
        self.assertIsInstance(df, pd.DataFrame)
        # Проверка наличия ожидаемых колонок
        self.assertIn('amount', df.columns)

if __name__ == '__main__':
    unittest.main()