import pytest


from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "value, expected",
    [(list("1234123412341234"), "1234 12** **** 1234"), (list("7290231685194711"), "7290 23** **** 4711")],
)
def test_card_numb(value, expected):
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected", [(list("12345678912345678912"), "**8912"), (list("98765432198765432198"), "**2198")]
)
def test_acc_numb(value, expected):
    assert get_mask_account(value) == expected
