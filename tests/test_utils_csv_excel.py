import unittest
from unittest.mock import mock_open, patch
import csv
from src.utils_csv_excel import get_data_from_csv, get_data_from_excel


class TestGetDataFromCsv(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='name;amount\nAlice;100\nBob;200')
    def test_get_data_from_csv(self, mock_file):
        expected_result = [{'name': 'Alice', 'amount': '100'}, {'name': 'Bob', 'amount': '200'}]
        file_path = "dummy_path.csv"

        # Вызов функции
        result = get_data_from_csv(file_path)

        # Проверка результата
        self.assertEqual(result, expected_result)

        # Проверка, что файл был открыт
        mock_file.assert_called_once_with(file_path, encoding='utf-8')


class TestGetDataFromExcel(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data='name;amount\nAlice;100\nBob;200')
    def test_get_data_from_excel(self, mock_file):
        expected_result = [{'name': 'Alice', 'amount': '100'}, {'name': 'Bob', 'amount': '200'}]
        file_path = "dummy_path.csv"

        # Вызов функции
        result = get_data_from_csv(file_path)

        # Проверка результата
        self.assertEqual(result, expected_result)

        # Проверка, что файл был открыт
        mock_file.assert_called_once_with(file_path, encoding='utf-8')
