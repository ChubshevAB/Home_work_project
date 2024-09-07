import csv

import pandas as pd

# Переменная хранит путь к файлу с расширением csv
file_path_csv = "..\\data\\transactions.csv"
file_path_excel = "..\\data\\transactions_excel.xlsx"


def get_data_from_csv(file_path_csv: str) -> list:
    """Принимает на вход путь к файлу в формате csv и возвращает список словарей с транзакциями"""

    with open(file_path_csv, encoding="utf-8") as file:
        file_csv = csv.DictReader(file, delimiter=";")
        result = []
        for row in file_csv:
            result.append(row)
    return result


# print(get_data_from_csv(file_path_csv))


def get_data_from_excel(file_path_excel: str) -> list:
    """Принимает на вход путь к файлу в формате xlsx и возвращает список словарей с транзакциями"""

    result = []
    df = pd.read_excel(file_path_excel)
    result = df.to_dict(orient="records")
    return result


# print(get_data_from_excel(file_path_excel))
