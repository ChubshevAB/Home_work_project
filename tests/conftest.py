import pytest


@pytest.fixture
def card_numb():
    return ['1234 12** **** 1234', [], 'Некорректный ввод']


def acc_numb():
    return ['**8912', [], 'Некорректный ввод']


