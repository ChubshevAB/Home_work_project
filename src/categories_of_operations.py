import json


file = "../data/operations.json"

list_of_categories = [
    "Перевод организации",
    "Открытие вклада",
    "Перевод со счета на счет",
    "Перевод с карты на счет",
    "Перевод с карты на карту",
]


def categories_of_operations(file: list, list_of_categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    category_count = {category: 0 for category in list_of_categories}
    with open(file, 'r', encoding='utf-8') as f:
        operations = json.load(f)

    for operation in operations:
        description = operation.get("description")
        if description in category_count:
            category_count[description] += 1

    return category_count


print(categories_of_operations(file, list_of_categories))
