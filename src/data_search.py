import json
import re

file = "../data/operations.json"
search_str = "Открытие вклада"


def data_search(file: str, search_str: str) -> list:
    """Принимает на вход файл со списком банковских операций и строку для поиска, возвращает список банковских
    операций, где есть данная строка"""
    with open(file, "r", encoding="utf-8") as f:
        readed_list = json.load(f)

    result = []
    pattern = re.compile(re.escape(search_str), re.IGNORECASE)
    for el in readed_list:
        for v in el.values():
            if isinstance(v, str) and pattern.search(v):
                result.append(el)

    return result


print(data_search(file, search_str))
