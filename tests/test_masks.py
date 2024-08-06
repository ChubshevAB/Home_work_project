from src.masks import get_mask_card_number, get_mask_account


def test_card_numb(card_numb):
    assert get_mask_card_number(list('1234123412341234')) == card_numb

def test_acc_numb(acc_numb):
    assert get_mask_account(list('12345678912345678912')) == acc_numb