import pandas as pd
import requests
from datetime import datetime
import json
from pathlib import Path

def get_greeting(current_time: datetime) -> str:
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 18:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"

def get_currency_rates(currencies: list) -> list:
    """Получает курсы валют с API ЦБ РФ."""
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    response = requests.get(url)
    data = response.json()["Valute"]
    return [{"currency": cur, "rate": round(data[cur]["Value"], 2)} for cur in currencies if cur in data]

def get_stock_prices(stocks: list) -> list:
    """Заглушка для цен акций (можно подключить Yahoo Finance API)."""
    return [{"stock": s, "price": round(100 + i * 10.5, 2)} for i, s in enumerate(stocks)]

def main_page(date_str: str, df: pd.DataFrame, settings_path: str) -> dict:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    greeting = get_greeting(date_obj)

    start_date = date_obj.replace(day=1)
    df_period = df[(df["Дата операции"] >= start_date) & (df["Дата операции"] <= date_obj)]

    cards_info = []
    for card, group in df_period.groupby("Номер карты"):
        total_spent = group[group["Сумма операции"] < 0]["Сумма операции"].sum() * -1
        cashback = round(total_spent / 100, 2)
        cards_info.append({
            "last_digits": str(card)[-4:],
            "total_spent": round(total_spent, 2),
            "cashback": cashback
        })

    top_transactions = df_period.nlargest(5, "Сумма операции")[["Дата операции", "Сумма операции", "Категория", "Описание"]]
    top_transactions_list = [
        {
            "date": row["Дата операции"].strftime("%d.%m.%Y"),
            "amount": row["Сумма операции"],
            "category": row["Категория"],
            "description": row["Описание"]
        }
        for _, row in top_transactions.iterrows()
    ]

    settings = json.loads(Path(settings_path).read_text(encoding="utf-8"))
    currency_rates = get_currency_rates(settings["user_currencies"])
    stock_prices = get_stock_prices(settings["user_stocks"])

    return {
        "greeting": greeting,
        "cards": cards_info,
        "top_transactions": top_transactions_list,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }