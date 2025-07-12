import pytest
from src.generators import filter_by_currency, transaction_descriptions

# --- Начало тестового файла ---

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
    for t in result:
        assert t['operationAmount']['currency']['code'] == 'USD'

def test_filter_by_currency_no_matches():
    transactions = [
        {
            "id": 1,
            "operationAmount": {"amount": "100", "currency": {"name": "JPY", "code": "JPY"}},
        }
    ]
    result = list(filter_by_currency(transactions, "USD"))
    assert result == []

def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    expected = ['Перевод организации', 'Перевод со счета на счет']
    assert descriptions == expected

def test_transaction_descriptions_with_invalid():
    transactions = [
        {
            "id": 1,
            "description": "Перевод организации"
        },
        {
            "id": 2,
            # Нет description - пропустится
        },
        {
            "id": 3,
            "description": "Некорректное описание"
        }
    ]
    result = list(transaction_descriptions(transactions))
    # Должен вернуть только допустимые описания
    assert result == ['Перевод организации']

