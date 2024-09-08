import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()


transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}


def conversion(transaction: dict) -> float:
    """Принимает на вход словарь с данными о транзакции и возвращает сумму транзакции в рублях.
    Если сумма указана в валюте, переводит валюту в рубли"""

    amount = transaction["operationAmount"]["amount"]
    check_currency = transaction["operationAmount"]["currency"]["code"]

    if check_currency == "RUB":
        return float(amount)
    if check_currency == "USD" or check_currency == "EUR":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={check_currency}&amount={amount}"
        apilayer_key = os.getenv("apilayer_key")
        headers = {"apikey": apilayer_key}
        response = requests.request("GET", url, headers=headers)
        result = dict(response.json())
        return float(result["result"])


# print(conversion(transaction))
