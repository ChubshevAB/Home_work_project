import math

from src.data_search import data_search
from src.processing import filter_by_state, sort_by_date
from src.utils import financial_transaction
from src.utils_csv_excel import get_data_from_csv, get_data_from_excel
from src.widget import get_date, mask_account_card

json_file = "data\\operations.json"
csv_file = "data\\transactions.csv"
xlsx_file = "data\\transactions_excel.xlsx"


def main():
    """Функция обеспечивает взаимодействие с пользователем.
    Использует ранее написанные функции из модулей пакета src"""

    choose_file = input(
        "Привет! Добро пожаловать в программу для работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n-> "
    )
    if choose_file == "1":
        print("Для обработки выбран JSON-файл.")
        operation_list = financial_transaction(json_file)
    elif choose_file == "2":
        print("Для обработки выбран CSV-файла.")
        operation_list = get_data_from_csv(csv_file)
    elif choose_file == "3":
        print("Для обработки выбран XLSX-файла.")
        operation_list = get_data_from_excel(xlsx_file)
    else:
        print("Введен неверный пункт меню")

    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    status_input = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n-> "
    ).upper()

    while status_input not in status_list:
        print(f'Статус операции "{status_input}" недоступен.')
        status_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n-> "
        ).upper()

    print(f'Операции отфильтрованы по статусу "{status_input}"')
    result_state = filter_by_state(operation_list, status_input)

    date_filter = input("Отсортировать операции по дате? Да/Нет\n-> ")
    if date_filter == "Да":
        date_sort_descending = input("Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию\n-> ")
        if date_sort_descending == "По возрастанию":
            result_date = sort_by_date(result_state, sorter=False)
        elif date_sort_descending == "По убыванию":
            result_date = sort_by_date(result_state, sorter=True)
    elif date_filter == "Нет":
        result_date = result_state

    currency_selection = input("Выводить только рублевые тразакции? Да/Нет\n-> ")
    filter_by_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n-> ")

    result_rub = []

    if currency_selection == "Да" and filter_by_description == "Да":
        search = input("Введите описание операции для фильтрации: ")

        if choose_file == "1":
            for el in result_date:
                if el["operationAmount"]["currency"]["code"] == "RUB":
                    result_rub.append(el)
            end_result = data_search(result_rub, search)  # Рублевый список с фильрацией по описанию json

        elif choose_file == "2" or choose_file == "3":
            for el in result_date:
                if el["currency_code"] == "RUB":
                    result_rub.append(el)
            end_result = data_search(result_rub, search)  # Рублевый список с фильрацией по описанию csv или xlsx

    elif currency_selection == "Да" and filter_by_description == "Нет":

        if choose_file == "1":
            for el in result_date:
                if el["operationAmount"]["currency"]["code"] == "RUB":
                    result_rub.append(el)  # Рублевый список без фильтрации по описанию json
            end_result = result_rub

        elif choose_file == "2" or choose_file == "3":
            for el in result_date:
                if el["currency_code"] == "RUB":
                    result_rub.append(el)  # Рублевый список без фильтрации по описанию csv или xlsx
            end_result = result_rub

    elif currency_selection == "Нет" and filter_by_description == "Да":
        search = input("Введите описание операции для фильтрации: ")
        end_result = data_search(result_date, search)  # Общий список с фильтрацией по описанию

    elif currency_selection == "Нет" and filter_by_description == "Нет":
        end_result = result_date  # Общий список без фильтрации

    # end_result

    if len(end_result) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(end_result)}\n")
        # return end_result

    check_key_json = "from"
    check_key_csv = ""
    # value = np.nan

    if choose_file == "1":
        for i in end_result:
            if check_key_json in i:
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['from'])} -> "
                    f"{mask_account_card(i['to'])}\nСумма: {i['operationAmount']['amount']} "
                    f"{i['operationAmount']['currency']['name']}\n"
                )
            elif check_key_json not in i:
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['to'])}\n"
                    f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n"
                )

    elif choose_file == "2":
        for i in end_result:
            if i["from"] != check_key_csv:
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['from'])} -> "
                    f"{mask_account_card(i['to'])}\nСумма: {i['amount']} {i['currency_code']}\n"
                )
            elif i["from"] == check_key_csv:
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['to'])}\nСумма: {i['amount']} "
                    f"{i['currency_code']}\n"
                )

    elif choose_file == "3":
        for i in end_result:
            value = i["from"]
            if isinstance(value, float) and math.isnan(value):
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['to'])}\nСумма: {i['amount']} "
                    f"{i['currency_code']}\n"
                )
            else:
                print(
                    f"{get_date(i['date'])} {i['description']}\n{mask_account_card(i['from'])} -> "
                    f"{mask_account_card(i['to'])}\nСумма: {i['amount']} {i['currency_code']}\n"
                )


main()
