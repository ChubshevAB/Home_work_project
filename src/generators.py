transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list) -> iter:
    """Функция принимает в качестве аргумента список транзакций и код транзакции и возвращает итератор
    в соответствии с заданными аргументами"""
    my_transactions = []
    for element in transactions:
        if element["operationAmount"]["currency"]["code"] == "USD":
            my_transactions.append(element)
    return iter(my_transactions)


def transaction_descriptions(transactions: list) -> iter:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    my_description = iter([el["description"] for el in transactions])
    return my_description


def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение (должно быть в диапазоне от 1 до 9999 9999 9999 9999)
    :param end: Конечное значение (должно быть в пределах от 1 до 9999 9999 9999 9999)
    """
    if start < 1 or end > 9999999999999999 or start > end:
        raise ValueError("Начальное и конечное значения должны быть в правильном диапазоне.")

    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]


# Пример работы функции
# transactions_list = transaction_descriptions(transactions)
# for i in range(5):
#     print(next(transactions_list))


# Пример использования генератора
# for card_number in card_number_generator(1, 5):
#     print(card_number)
