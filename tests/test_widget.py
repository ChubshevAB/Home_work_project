from src.widget import mask_account_card, get_date


def test_mask_card(widget_card):
    assert mask_account_card(list('Maestro 1234123412341234')) == widget_card

def test_mask_acc(widget_acc):
    assert mask_account_card('Счет 1234123412341234') == widget_acc

def test_get_data(widget_data):
    assert get_date('2024-07-20T02:26:18.671407') == widget_data