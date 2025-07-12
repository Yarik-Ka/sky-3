import typing

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list, currency: str) -> typing.List[dict]:
    """фильтрует транзакции в зависимости от валюты"""
    filtered_transactions = [
        transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency
    ]
    if not filtered_transactions:
        return []
    return filtered_transactions


if __name__ == "__main__":
    currency = input("Enter the currency: ")
    usd_transactions = filter_by_currency(transactions, currency=currency)
    if usd_transactions:
        for item in usd_transactions:
            print(item)
    else:
        print(f"There is no {currency} currency in transactions")


def transaction_descriptions(transactions: typing.List[dict]) -> typing.List[str]:
    """выводит описание каждой транзакции по ключу ["description"], если оно входит в множество
    'acceptable_values'"""
    acceptable_values = {
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    }
    descriptions = []
    for transaction in transactions:
        try:
            description = transaction["description"]
            if description in acceptable_values:
                descriptions.append(description)
        except TypeError or KeyError:
            return []
    return descriptions


if __name__ == "__main__":
    descriptions = transaction_descriptions(transactions)
    if descriptions:
        for item in descriptions:
            print(item)
    else:
        print("No correct description of the transaction was found")


def format_card_number(number: str) -> str:
    """Форматирует номер карты в формат XXXX XXXX XXXX XXXX."""
    return f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:16]}"


def card_number_generator(start: int, stop: int) -> typing.Generator[str, None, None]:
    """генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне"""
    if not isinstance(start, int) or not isinstance(stop, int):
        yield "Incorrect data entered: start and stop must be integers"
        return

    elif start > stop or start < 0:
        yield "Incorrect data entered: start must be less than or equal to stop and non-negative"
        return

    for number in range(start, stop + 1):
        formatted_number = format_card_number(str(number).zfill(16))
        yield formatted_number


if __name__ == "__main__":
    try:
        for card_number in card_number_generator(1, 5):
            print(card_number)
    except TypeError:
        print("Please provide both start and stop arguments")