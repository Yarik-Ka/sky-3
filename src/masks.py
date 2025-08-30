import typing
import os
import logging

# Создаем папку logs, если еще не существует
os.makedirs("logs", exist_ok=True)

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/app.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def get_mask_card_number(card_number: typing.Any) -> str:
    """Функция, которая принимает номер карты, и возвращает ее маску"""
    if isinstance(card_number, str):
        if card_number.isdigit() and len(card_number) == 16:
            formatted_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
            logger.info(f"Masked card number: {formatted_number}")
            return formatted_number
        else:
            logger.warning(f"Invalid card number format: {card_number}")
            return "Error: invalid number format"
    else:
        filter_list = []
        for item in card_number:
            if isinstance(item, str):
                if item.isdigit() and len(item) == 16:
                    formatted_number = item[:4] + " " + item[4:6] + "** **** " + item[-4:]
                    filter_list.append(formatted_number)
        result = " ".join(filter_list)
        logger.info(f"Masked multiple card numbers: {result}")
        return result

if __name__ == "__main__":
    result = get_mask_card_number(input("Enter your number card: "))
    print(result)

def get_mask_account(account: typing.Any) -> str:
    """Функция, которая принимает номер счета, и возвращает его маску"""
    if isinstance(account, str):
        if account.isdigit() and len(account) == 20:
            mask_account = account.replace(account[0:16], "**")
            logger.info(f"Masked account: {mask_account}")
            return mask_account
        else:
            logger.warning(f"Invalid account format: {account}")
            return "Error: invalid account format"
    else:
        filter_list = []
        for item in account:
            if isinstance(item, str):
                if item.isdigit() and len(item) == 20:
                    mask_account = item.replace(item[0:16], "**")
                    filter_list.append(mask_account)
        result = " ".join(filter_list)
        logger.info(f"Masked multiple accounts: {result}")
        return result

if __name__ == "__main__":
    result = get_mask_account(input("Enter account: "))
    print(result)