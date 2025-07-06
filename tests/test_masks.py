import pytest
from masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("account_number, expected", [
    ("1234567890", "******7890"),
    ("9876543210", "******3210"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

@pytest.mark.parametrize("card_number, expected", [
    ("1234 5678 9012 3456", "**** **** **** 3456"),
    ("1234567890123456", "**** **** **** 3456"),
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected