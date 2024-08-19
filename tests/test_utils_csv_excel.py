import unittest
from unittest.mock import MagicMock, mock_open, patch

import pandas as pd

from src.utils_csv_excel import get_data_from_csv, get_data_from_excel


class TestGetDataFromCsv(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="name;amount\nAlice;100\nBob;200")
    def test_get_data_from_csv(self, mock_file):
        expected_result = [{"name": "Alice", "amount": "100"}, {"name": "Bob", "amount": "200"}]
        file_path = "dummy_path.csv"

        result = get_data_from_csv(file_path)

        self.assertEqual(result, expected_result)

        mock_file.assert_called_once_with(file_path, encoding="utf-8")


class TestGetDataFromExcel(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_get_data_from_excel(self, mock_read_excel):
        mock_data = pd.DataFrame({"name": ["Alice", "Bob"], "amount": [100, 200]})

        mock_read_excel.return_value = mock_data

        file_path = "dummy_path.xlsx"

        result = get_data_from_excel(file_path)

        expected_result = [{"name": "Alice", "amount": 100}, {"name": "Bob", "amount": 200}]

        self.assertEqual(result, expected_result)

        mock_read_excel.assert_called_once_with(file_path)
