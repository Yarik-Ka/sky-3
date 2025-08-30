from unittest.mock import patch, Mock

from src.external_api import conversion_currency


@patch('requests.get')
def test_conversion_currency_successful_try(mock_get):
    test_data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 1}
    mock_get.return_value = mock_response

    assert conversion_currency(test_data) == 1
    mock_get.assert_called_once()


@patch('requests.get')
def test_conversion_currency_code_not_200(mock_get):
    test_data = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {'result': 1}
    mock_get.return_value = mock_response

    assert conversion_currency(test_data) == "Что-то пошло не так"
    mock_get.assert_called_once()


@patch('requests.get')
def test_conversion_currency_with_rub(mock_get):
    test_data = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": 31957.58,
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'result': 1}
    mock_get.return_value = mock_response

    assert conversion_currency(test_data) == 31957.58