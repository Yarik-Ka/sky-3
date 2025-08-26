import unittest
from unittest.mock import patch, mock_open, MagicMock
import json
import csv
import openpyxl
from src.utils import process_bank_search, process_bank_operations
from src.data_processing import load_json, load_csv, load_xlsx

class TestBankOperations(unittest.TestCase):

    def setUp(self):
        # Пример данных для тестирования
        self.data = [
            {'date': '2023-10-01', 'description': 'Оплата по кредиту', 'amount': '1000 руб', 'status': 'EXECUTED'},
            {'date': '2023-10-02', 'description': 'Покупка в магазине', 'amount': '500 руб', 'status': 'CANCELED'},
            {'date': '2023-10-03', 'description': 'Оплата коммунальных услуг', 'amount': '2000 руб', 'status': 'EXECUTED'},
        ]

    def test_process_bank_search(self):
        result = process_bank_search(self.data, "оплата")
        self.assertEqual(len(result), 2)
        self.assertTrue(all('Оплата' in r['description'] or 'оплата' in r['description'].lower() for r in result))

    def test_process_bank_operations(self):
        categories = ['кредит', 'магазин']
        counts = process_bank_operations(self.data, categories)
        self.assertEqual(counts['кредит'], 1)
        self.assertEqual(counts['магазин'], 1)

    @patch('builtins.open', new_callable=mock_open)
    def test_load_json(self, mock_file):
        mock_file.return_value.read.return_value = json.dumps([{'date':'2023-10-01'}])
        with patch('builtins.open', mock_file):
            # Вводим путь к файлу
            with patch('builtins.input', return_value='fake.json'):
                data = load_json()
                self.assertIsInstance(data, list)
                self.assertEqual(data[0]['date'], '2023-10-01')

    @patch('builtins.open', new_callable=mock_open)
    def test_load_csv(self, mock_file):
        csv_content = "date,description,amount,status\n2023-10-01,Оплата,1000 руб,EXECUTED\n"
        mock_file.return_value.__iter__.return_value = csv_content.splitlines()
        with patch('builtins.input', return_value='fake.csv'):
            data = load_csv()
            self.assertIsInstance(data, list)
            self.assertEqual(data[0]['date'], '2023-10-01')

    @patch('openpyxl.load_workbook')
    def test_load_xlsx(self, mock_load_wb):
        # Создаем фиктивный лист с данными
        wb_mock = MagicMock()
        sheet_mock = MagicMock()
        wb_mock.active = sheet_mock

        # Заголовки
        sheet_mock.iter_rows.return_value = [
            [MagicMock(value='date'), MagicMock(value='description'), MagicMock(value='amount')],
            [MagicMock(value='2023-10-01'), MagicMock(value='Оплата'), MagicMock(value='1000 руб')]
        ]
        mock_load_wb.return_value = wb_mock

        with patch('builtins.input', return_value='fake.xlsx'):
            data = load_xlsx()
            self.assertIsInstance(data, list)
            self.assertEqual(data[0]['date'], '2023-10-01')
            self.assertEqual(data[0]['description'], 'Оплата')

if __name__ == '__main__':
    unittest.main()