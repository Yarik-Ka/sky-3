from __future__ import annotations

import os

import requests
from dotenv import load_dotenv


def conversion_currency(transaction: dict) -> float | str:
    """
    Получает на вход словарь с данными о транзакции.
    Конвертирует валюту из USD и EUR в RUB и возвращает сумму транзакции в рублях
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amount: float = transaction["operationAmount"]["amount"]

    load_dotenv()

    if currency in ["USD", "EUR"]:

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(url, headers=headers)

        result: float = response.json()["result"]

        if response.status_code == 200:
            return result

        else:
            return "Что-то пошло не так"

    return amount