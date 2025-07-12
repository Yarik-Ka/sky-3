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
        # Транзакция с другим валютным кодом
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        # Описание есть
        "description": "Перевод со счета на счет",
        # Остальные ключи
        'from': 'Счет 44812258784861134719',
        'to': 'Счет 74489636417521191160',
    },
    {
        # Объект без description для теста исключений
    },
]


def filter_by_currency(transactions: typing.Iterable[dict], currency: str) -> typing.Generator[dict, None, None]:
    """Фильтрует транзакции по валюте, возвращая генератор."""
    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except (KeyError, TypeError):
            continue


def transaction_descriptions(transactions: typing.Iterable[dict]) -> typing.Generator[str, None, None]:
    """Выдает описание каждой транзакции по ключу ['description'], если оно входит в допустимый набор."""
    acceptable_values = {
        'Перевод организации',
        'Перевод со счета на счет',
        'Перевод с карты на карту'
    }
    for transaction in transactions:
        try:
            description = transaction["description"]
            if description in acceptable_values:
                yield description
        except (KeyError, TypeError):
            continue


# Тестовые функции для проверки корректности работы (используем pytest)
import pytest


@pytest.fixture
def sample_transactions():
    return [
        {
            'id': 1,
            'description': 'Перевод организации',
            'operationAmount': {'amount': '1000', 'currency': {'name': 'USD', 'code': 'USD'}}
        },
        {
            'id': 2,
            'description': 'Некорректное описание',
            'operationAmount': {'amount': '2000', 'currency': {'name': 'USD', 'code': 'USD'}}
        },
        {
            'id': 3,
            'description': 'Перевод со счета на счет',
            'operationAmount': {'amount': '3000', 'currency': {'name': 'EUR', 'code': 'EUR'}}
        }
    ]


def test_filter_by_currency(sample_transactions):
    result = list(filter_by_currency(sample_transactions, 'USD'))
    assert len(result) == 2
    assert all(t['operationAmount']['currency']['code'] == 'USD' for t in result)


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ['Перевод организации', 'Перевод со счета на счет']


# Основной блок для запуска примера
if __name__ == "__main__":
    currency_input = input("Введите код валюты (например, USD): ")

    print("Транзакции по валюте:")
    for t in filter_by_currency(transactions, currency_input):
        print(t)

    print("\nОписание транзакций:")
    for desc in transaction_descriptions(transactions):
        print(desc)