import pandas as pd
from datetime import datetime
from typing import Optional
import json

def save_report(filename: Optional[str] = None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            file = filename or f"report_{func.__name__}.json"
            with open(file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            return result
        return wrapper
    return decorator

@save_report()
def spending_by_category(df: pd.DataFrame, category: str, date: Optional[str] = None) -> dict:
    if date:
        end_date = datetime.strptime(date, "%Y-%m-%d")
    else:
        end_date = datetime.now()
    start_date = end_date - pd.DateOffset(months=3)

    df_filtered = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= end_date)]
    df_cat = df_filtered[df_filtered["Категория"] == category]
    total_spent = df_cat[df_cat["Сумма операции"] < 0]["Сумма операции"].sum() * -1

    return {
        "category": category,
        "total_spent": round(total_spent, 2),
        "period": f"{start_date.date()} - {end_date.date()}"
    }