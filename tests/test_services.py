from src.services import investment_bank

def test_investment_bank():
    transactions = [
        {"Дата операции": "2025-08-01", "Сумма операции": -120},
        {"Дата операции": "2025-08-05", "Сумма операции": -75},
        {"Дата операции": "2025-07-20", "Сумма операции": -200}
    ]
    result = investment_bank("2025-08", transactions, 50)
    # 120 → округление до 150 → 30 в копилку
    # 75 → округление до 100 → 25 в копилку
    assert result == 55