import json
import os
from typing import Any


transactions_path = "../data/operations.json"


def financial_transaction(transactions_path: str) -> list:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    if not os.path.isfile(transactions_path) or os.stat(transactions_path).st_size == 0:
        return []

    else:
        with open(transactions_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
