

def get_mask_card_number(card_number: str) -> str:
    clean_number = card_number.replace(" ", "")
    if len(clean_number) < 16:
        raise ValueError("Некорректный номер карты")
    start = clean_number[:6]
    end = clean_number[-4:]
    masked_middle = '**** ****'
    return f"{start} {masked_middle} {end}"


def get_mask_account(account_number: str) -> str:
    clean_number = account_number.replace(" ", "")
    if len(clean_number) < 8:
        raise ValueError("Некорректный номер счета")
    start = clean_number[:4]
    end = clean_number[-4:]
    return f"**{end}"
