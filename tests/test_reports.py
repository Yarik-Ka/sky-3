import pandas as pd
from src.reports import spending_by_category

def test_spending_by_category(tmp_path):
    data = {
        "Дата операции": pd.to_datetime(["2025-06-01", "2025-07-15", "2025-08-20"]),
        "Категория": ["Супермаркеты", "Супермаркеты", "Кафе"],
        "Сумма операции": [-100, -200, -50]
    }
    df = pd.DataFrame(data)

    result = spending_by_category(df, "Супермаркеты", "2025-08-30")
    assert result["category"] == "Супермаркеты"
    assert result["total_spent"] == 300
    assert "period" in result