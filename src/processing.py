def filter_by_state(filterable_list: list, state: str = "EXECUTED") -> list:
    """Фильтрует входящий список словарей по заданному ключу. По умолчанию значение ключа "EXECUTED" """

    new_list = []

    # Цикл сравнивает значение ключа элемента списка с аргументом state
    # и если они равны записывает этот элемент в новый список
    for i in filterable_list:
        description = i.get("state")
        if description == state:
            new_list.append(i)

    return new_list


def sort_by_date(sortable_list: list, sorter: bool = True) -> list:
    """Сортирует заданный список по дате. По умолчанию список сортируется по убыванию"""

    # Процесс сортировки списка словарей по ключу 'date'
    sorted_list = sorted(sortable_list, key=lambda x: x["date"], reverse=sorter)

    return sorted_list


# print(
#     sort_by_date(
#         sortable_list=[
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ]
#     )
# )
#
# print(
#     filter_by_state(
#         filterable_list=[
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {
#                     "amount": "31957.58",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589"
#             },
#             {
#                 "id": 41428829,
#                 "state": "EXECUTED",
#                 "date": "2019-07-03T18:35:29.512364",
#                 "operationAmount": {
#                     "amount": "8221.37",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "MasterCard 7158300734726758",
#                 "to": "Счет 35383033474447895560"
#             },
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 587085106,
#                 "state": "CANCELED",
#                 "date": "2018-03-23T10:45:06.972075",
#                 "operationAmount": {
#                     "amount": "48223.05",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Открытие вклада",
#                 "to": "Счет 41421565395219882431"
#             }
#         ],
#         state="EXECUTED",
#     )
# )
#
#
# print(
#     sort_by_date(
#         sortable_list=[
#             {
#                 "id": 441945886,
#                 "state": "EXECUTED",
#                 "date": "2019-08-26T10:50:58.294041",
#                 "operationAmount": {
#                     "amount": "31957.58",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Maestro 1596837868705199",
#                 "to": "Счет 64686473678894779589"
#             },
#             {
#                 "id": 41428829,
#                 "state": "EXECUTED",
#                 "date": "2019-07-03T18:35:29.512364",
#                 "operationAmount": {
#                     "amount": "8221.37",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "MasterCard 7158300734726758",
#                 "to": "Счет 35383033474447895560"
#             },
#             {
#                 "id": 939719570,
#                 "state": "EXECUTED",
#                 "date": "2018-06-30T02:08:58.425572",
#                 "operationAmount": {
#                     "amount": "9824.07",
#                     "currency": {
#                         "name": "USD",
#                         "code": "USD"
#                     }
#                 },
#                 "description": "Перевод организации",
#                 "from": "Счет 75106830613657916952",
#                 "to": "Счет 11776614605963066702"
#             },
#             {
#                 "id": 587085106,
#                 "state": "CANCELED",
#                 "date": "2018-03-23T10:45:06.972075",
#                 "operationAmount": {
#                     "amount": "48223.05",
#                     "currency": {
#                         "name": "руб.",
#                         "code": "RUB"
#                     }
#                 },
#                 "description": "Открытие вклада",
#                 "to": "Счет 41421565395219882431"
#             }
#         ],
#         sorter=True,
#     )
# )
