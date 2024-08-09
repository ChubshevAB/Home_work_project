import logging
from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала и конца выполнения функции, а также её результатов или возникших ошибок. Имеет необязательный параметр filename, если он указат, то все логи будут записаны в соответствующий файл"""

    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"Начало выполнения '{func.__name__}' с аргументами: {args} {kwargs}")

            try:
                result = func(*args, **kwargs)
                logging.info(f"'{func.__name__}' завершилась успешно, результат: {result}")
                return result
            except Exception as e:
                logging.error(
                    f"Функция '{func.__name__}' завершилась ошибкой: {type(e).__name__} - {e}, введенные аргументы: {args} {kwargs}"
                )
                raise  # Передаем исключение дальше

        return wrapper

    return my_decorator


# Примеры использования декоратора

# @log()  # Логи будут выводиться в консоль
# def get_date(user_date: str) -> str:
#     """Функция принимает в качестве аргумента строку с датой и возвращает эту дату в другом формате."""
#
#     new_date = f"{user_date[8:10]}-{user_date[5:7]}-{user_date[:4]}"
#
#     return new_date
#
# print(get_date(user_date="2024-07-20T02:26:18.671407"))


@log("logs.txt")  # Логи будут записываться в файл
def mask_account_card(user_input: str) -> str:
    """Функция маскирует номер карты или номер счета в зависимости от полученного аргумента."""

    new_card_name = ""
    card_numbers = ""

    # Проверка на введенный аргумент. Маскировка счета, если аргумент - счет.
    # Подготовка к маскировке карты, если аргумент - карта
    if "С" in user_input:
        new_account_name = user_input[:5]
        new_account_numbers = user_input[-4:]
        mask_account = new_account_name + "**" + new_account_numbers
        return mask_account

    for char in user_input:
        if char.isalpha() or char == " ":
            new_card_name += char
        elif char.isdigit():
            card_numbers += char

    # Разбиваем номер карты на список из 4 элементов
    card_numbers_list = [card_numbers[i : i + 4] for i in range(0, len(card_numbers), 4)]

    # Создание маски для номера карты
    # Только первая и последняя части остаются открытыми,
    # вторая часть замаскирована на половину
    if len(card_numbers_list) > 1:
        masked_second_segment = "".join(card_numbers_list[1][:2]) + "*" * (4 - 2)  # Замаскируем 2 из 4
    else:
        masked_second_segment = card_numbers_list[1] if len(card_numbers_list[1]) < 4 else "****"

    masked_card_numbers = [
        card_numbers_list[0],  # Первая часть остается
        masked_second_segment,  # Вторая часть с частичной маскировкой
        "*" * len(card_numbers_list[2]),  # Вся третья часть замаскирована, если есть
        card_numbers_list[3] if len(card_numbers_list) > 3 else "",  # Четвертая часть остается
    ]

    # Формируем окончательный замаскированный номер карты
    mask_card = f"{new_card_name} {' '.join(masked_card_numbers)}"

    return mask_card


print(mask_account_card(user_input="Счет 12345678901234567890"))
