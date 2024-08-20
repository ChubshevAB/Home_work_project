from unittest.mock import patch


from src.external_api import conversion


@patch("requests.get")
def test_conversion(mock_resp):

    mock_resp.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1723577764, "rate": 90.497981},
        "date": "2024-08-13",
        "result": 2892096.467646,
    }
    assert (
        conversion(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == 2892096.467646
    )

    mock_resp.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
    )
