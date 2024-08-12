import json
import os
from typing import Any


file_path = "../data/operations.json"


def financial_transaction(file_path: str) -> Any:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    if not os.path.isfile(file_path) or os.stat(file_path).st_size == 0:
        return []

    else:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data


print(financial_transaction(file_path))
