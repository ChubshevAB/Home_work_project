import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "value, expected",
    [
        (list("Maestro 1234123412341234"), "Maestro 1234 12** **** 1234"),
        (list("Master Card 1234123412341234"), "Master Card 1234 12** **** 1234"),
    ],
)
def test_mask_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("Счет 1234123412341234", "Счет **1234"), ("Счет 98765432198765432198", "Счет **2198")]
)
def test_mask_acc(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected", [("2024-07-20T02:26:18.671407", "20-07-2024"), ("2023-01-17T03:15:48.487193", "17-01-2023")]
)
def test_get_data(value, expected):
    assert get_date(value) == expected
