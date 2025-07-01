from masks import get_mask_card_number, get_mask_account


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.

    Args:
        card_number (str): номер карты.

    Returns:
        str: маскированный номер карты.
    """
    if not isinstance(card_number, str):
        raise ValueError("card_number должен быть строкой")
    return get_mask_card_number(card_number)


def mask_account(account_number: str) -> str:
    """
    Маскирует номер счета.

    Args:
        account_number (str): номер счета.

    Returns:
        str: маскированный номер счета.
    """
    if not isinstance(account_number, str):
        raise ValueError("account_number должен быть строкой")
    return get_mask_account(account_number)