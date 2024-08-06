def mask_account_card(user_input: str) -> str:
    """Функция маскирует номер карты или номер счета в зависимости от полученного аргумента"""

    new_card_name = ""
    card_numbers = ""

    # Проверка на введенный аргумент. Маскировка счета, если аргумент - счет. Подготовка к маскировки карты, если аргумент - карта
    for i in user_input:
        if i == "С":
            new_account_name = user_input[:5]
            new_account_numbers = user_input[-4:]
            mask_account = new_account_name + "**" + new_account_numbers
        elif i != "С":
            if i.isalpha() or i == " ":
                new_card_name += i
            elif i.isdigit():
                card_numbers += i

    # Разбиваем номер карты на список из 4 элементов
    card_numbers_list = [card_numbers[i : i + 4] for i in range(0, len(card_numbers), 4)]

    mask_card_numbers = " ".join(card_numbers_list[1]) + " " + " ".join(card_numbers_list[2])

    mask_card_numbers_list = []

    for i in mask_card_numbers:
        if i != " ":
            mask_card_numbers_list.append(i)

    for i, v in enumerate(mask_card_numbers_list):
        if i >= 2:
            mask_card_numbers_list[i] = "*"

    mask_card = (
        new_card_name
        + card_numbers_list[0]
        + " "
        + "".join(mask_card_numbers_list[0:4])
        + " "
        + "".join(mask_card_numbers_list[4::])
        + " "
        + card_numbers_list[3]
    )

    # Возврат работы функции в зависимости от полученного аргумента
    if "С" in user_input:
        return mask_account
    else:
        return mask_card


def get_date(user_date: str) -> str:
    """Функция принимает в качестве аргумента строку с датой и возвращает эту дату в другом формате"""

    new_date = "".join(user_date[8:10]) + "-" + "".join(user_date[5:7]) + "-" + "".join(user_date[:4])

    return new_date


# print(mask_account_card(user_input="Master Card 1234123412341234"))
# print(get_date(user_date="2024-07-20T02:26:18.671407"))
