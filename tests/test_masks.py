import typing

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card(fixture_for_mask: typing.Any) -> typing.Any:
    assert get_mask_card_number(fixture_for_mask) == "1234 56** **** 3456"


def test_for_atypical_numbers() -> None:
    assert get_mask_card_number("!@#$%^&*()--===") == "Error: invalid number format"


def test_for_an_empty_value() -> None:
    assert get_mask_card_number("") == "Error: invalid number format"


def test_get_mask_account(fixture_for_mask: typing.Any) -> typing.Any:
    assert get_mask_account(fixture_for_mask) == "**7890"


def test_for_atypical_account() -> None:
    assert get_mask_account("!@#$$%^^^&^%$") == "Error: invalid account format"


def test_for_incorrect_num_len() -> None:
    assert get_mask_account("1234567890") == "Error: invalid account format"