import json
import logging
import os
from typing import Any

# logging.basicConfig(filename="../logs/logs_utils.log", filemode="w", level=logging.DEBUG,
# ormat="%(levelname)s: %(asctime)s - %(filename)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
my_logger = logging.getLogger("log_utils")


transactions_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json'))
# transactions_path = "../data/operations.json"


def financial_transaction(transactions_path: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""

    if not os.path.isfile(transactions_path) or os.stat(transactions_path).st_size == 0:
        my_logger.warning("Файл пуст, не содержит нужных данных или не найден")
        return []

    else:
        with open(transactions_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                my_logger.info("Функция завершила работу, данные успешно загружены")
                return data


# print(financial_transaction(transactions_path))
