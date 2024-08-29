import logging


logging.basicConfig(
    filename="../logs/logs_masks.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(levelname)s: %(asctime)s - %(filename)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
my_logger = logging.getLogger("log_mask")


def get_mask_card_number(user_input_card: list) -> str:
    """Функция принимает в качестве аргумента номер карты и возвращает его маску."""

    # Выводит сообщение, если не введен номер карты
    if not user_input_card:
        my_logger.warning(msg="Некорректный ввод")
        return "Некорректный ввод"

    # Разбиваем номер карты на список из 4 элементов
    mask = [user_input_card[i: i + 4] for i in range(0, len(user_input_card), 4)]

    # Заменяем цифры в номере карты на знак *
    for i in range(2, len(mask[1])):  # Заменяем все кроме первых двух
        mask[1][i] = "*"

    for i in range(len(mask[2])):  # Заменяем все цифры из третьей части
        mask[2][i] = "*"

    # Собираем замаскированный номер карты
    mask_card_number = " ".join("".join(part) for part in mask)
    my_logger.info(msg=f"Замаскированный номер карты: {mask_card_number}")
    return mask_card_number


def get_mask_account(user_input_account: list) -> str:
    """Функция принимает в качестве аргумента номер счета и возвращает его маску."""

    # Выводит сообщение, если не введен номер счета или он не соответствует формату в 20 знаков
    if not user_input_account or len(user_input_account) != 20:
        my_logger.warning(msg="Некорректный ввод")
        return "Некорректный ввод"

    # Берем последние 6 цифр из номера счета для формирования маски
    new_mask_account = user_input_account[-6:]

    # Замена первых двух символов на знак *
    for i in range(min(2, len(new_mask_account))):  # Проверяем длину
        new_mask_account[i] = "*"

    # Преобразовываем получившийся список в строку для формирования окончательного вида маски
    mask_account = "".join(new_mask_account)
    my_logger.info(msg=f"Замаскированный номер счета: {mask_account}")
    return mask_account


# Пример использования
# user_input_card = list(input("Введите номер карты: "))
# user_input_account = list(input("Введите номер счета: "))
# print(get_mask_card_number(user_input_card))
# print(get_mask_account(user_input_account))
