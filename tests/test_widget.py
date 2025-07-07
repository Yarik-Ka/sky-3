import pytest
from src.widget import mask_card_number, mask_account

# Мокаем функции из модуля masks, чтобы не зависеть от их реализации
from unittest.mock import patch

@pytest.fixture(autouse=True)
def patch_masks():
    with patch('src.widget.get_mask_card_number') as mock_mask_card, \
         patch('src.widget.get_mask_account') as mock_mask_acc:
        # Настраиваем возвращаемые значения для моков
        mock_mask_card.return_value = "**** **** **** 3456"
        mock_mask_acc.return_value = "**** 7890"
        yield

@pytest.mark.parametrize("card_number, expected", [
    ("1234 5678 9012 3456", "**** **** **** 3456"),
    ("1111 2222 3333 4444", "**** **** **** 4444"),
])
def test_mask_card_number(card_number, expected):
    result = mask_card_number(card_number)
    assert result == expected

@pytest.mark.parametrize("account_number, expected", [
    ("987654321", "**** 789"),
    ("1234567890", "**** 890"),
])
def test_mask_account(account_number, expected):
    result = mask_account(account_number)
    assert result == expected

# Можно добавить тесты на неправильный тип
def test_mask_card_number_invalid_type():
    with pytest.raises(ValueError):
        mask_card_number(1234567890)  # не строка

def test_mask_account_invalid_type():
    with pytest.raises(ValueError):
        mask_account(None)  # не строка