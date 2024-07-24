def filter_by_state(filterable_list: list, state: str = "EXECUTED") -> list:
    """Фильтрует входящий список словарей по заданному ключу. По умолчанию значение ключа "EXECUTED" """

    new_list = []

    # Цикл сравнивает значение ключа элемента списка с аргументом state и если они равны записывает этот элемент в новый список
    for i in filterable_list:
        if i["state"] == state:
            new_list.append(i)

    return new_list


print(
    filter_by_state(
        filterable_list=[
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state="EXECUTED",
    )
)
