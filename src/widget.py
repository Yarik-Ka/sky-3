import re

def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в строке.
    Вход:
        info: строка вида "Visa Platinum 7000792289606361" или "Счет 73654108430135874305"
    Выход:
        строка с маскированным номером.
    """
    # Разделяем строку на части
    parts = info.split()
    # Определяем тип (карта или счет)
    if parts[0] == "Счет":
        # Обработка счета
        account_number = parts[1]
        masked_number = "**" + account_number[-4:]
        return f"{parts[0]} {masked_number}"
    else:
        # Обработка карты
        # Предполагается, что номер карты - последний элемент строки
        card_number = parts[-1]
        # Маскируем номер карты
        first4 = card_number[:4]
        last4 = card_number[-4:]
        middle_masked = "**** ****"
        return f"{parts[0]} {parts[1]} {first4} {middle_masked} {last4}"

def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата "2024-03-11T02:26:18.671407" в "ДД.ММ.ГГГГ".
    """
    # Используем срезы или парсим дату
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"bgtedg
