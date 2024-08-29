import json
from src.utils import financial_transaction
from pathlib import Path


transactions_path = Path("d:\\Python\\Projects\\Home_work_project\\data\\operations.json")


# def test_incorrect_file_path():
#     '''Проверка на некорректный путь к файлу или отсутствие файла'''
#     assert financial_transaction(transactions_path) == []


def test_financial_transaction():
    """Проверка на корректную работу функции"""
    with open(transactions_path, "r", encoding="utf-8") as f:
        chek_values = json.load(f)
    transactions = financial_transaction(transactions_path)
    assert chek_values == transactions
