

import pytest
from src import masks


def test_get_mask_card_number():
    assert masks.get_mask_card_number('1234 5678 9012 3456') == '**** **** **** 3456'
    assert masks.get_mask_card_number('1234567890123456') == '**** **** **** 3456'


def test_get_mask_account():
    assert masks.get_mask_account('1234567890') == '******7890'


def test_short_card():
    with pytest.raises(ValueError):
        masks.get_mask_card_number('123')


def test_short_account():
    with pytest.raises(ValueError):
        masks.get_mask_account('1')
