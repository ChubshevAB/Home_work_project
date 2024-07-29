def get_mask_card_number(user_input_card: list) -> str:
    """Функция принимает в качестве аргумента номер карты и возвращает его маску"""

    #Выводит сообщение, если не введен номер карты
    if user_input_card == []:
        return 'Некорректный ввод'

    else:
        # Разбиваем номер карты на список из 4 элементов
        mask = [user_input_card[i : i + 4] for i in range(0, len(user_input_card), 4)]

        # Заменяем цифры в монере карты на знак *
        for i, v in enumerate(mask[1]):
            if i > 1:
                mask[1][i] = "*"

        # Заменяем цифры в монере карты на знак *
        for i, v in enumerate(mask[2]):
            mask[2][i] = "*"

    # Собираем замаскированный номер карты
    mask_card_number = "".join(mask[0]) + " " + "".join(mask[1]) + " " + "".join(mask[2]) + " " + "".join(mask[3])

    return mask_card_number


def get_mask_account(user_input_account: list) -> str:
    """Функция принимает в качестве аргумента номер счета и возвращает его маску"""

    #Выводит сообщение, если не введен номер счета или он не соответствует формату в 20 знаков
    if user_input_account == [] or len(user_input_account) != 20:
        return 'Некорректный ввод'
    else:
        # Берем последние 6 цифр из номера счета для формирования маски
        new_mask_account = user_input_account[-6::]

        # Замена первых двух символов на знак *
        for i, v in enumerate(new_mask_account):
            if i <= 1:
                new_mask_account[i] = "*"

    # Преобразоввываем получившийся списко в строку для формирования окончательного вида маски
    mask_account = "".join(new_mask_account)

    return mask_account


# user_input_card = list(input("Введите номер карты: "))
#
# user_input_account = list(input("Введите номер счета: "))
#
# print(get_mask_card_number(user_input_card))
# print(get_mask_account(user_input_account))
