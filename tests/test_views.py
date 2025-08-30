import pandas as pd
from src.views import main_page

def test_main_page(tmp_path):
    # Создаём тестовый DataFrame
    data = {
        "Дата операции": pd.to_datetime(["2025-08-01", "2025-08-15", "2025-08-20"]),
        "Номер карты": ["1234567890123456", "1234567890123456", "9876543210987654"],
        "Сумма операции": [-1000, -500, -200],
        "Категория": ["Супермаркеты", "Кафе", "Супермаркеты"],
        "Описание": ["Пятёрочка", "Шоколадница", "Магнит"]
    }
    df = pd.DataFrame(data)

    # Создаём временный settings.json
    settings_file = tmp_path / "user_settings.json"
    settings_file.write_text('{"user_currencies": ["USD"], "user_stocks": ["AAPL"]}', encoding="utf-8")

    result = main_page("2025-08-20 14:00:00", df, str(settings_file))

    assert "greeting" in result
    assert isinstance(result["cards"], list)
    assert isinstance(result["top_transactions"], list)
    assert isinstance(result["currency_rates"], list)
    assert isinstance(result["stock_prices"], list)