from typing import List, Dict, Any
from datetime import datetime

def investment_bank(month: str, transactions: List[Dict[str, Any]], limit: int) -> float:
    """Считает сумму, которую можно было бы отложить в инвесткопилку."""
    total_saved = 0.0
    for tx in transactions:
        tx_date = datetime.strptime(tx["Дата операции"], "%Y-%m-%d")
        if tx_date.strftime("%Y-%m") == month and tx["Сумма операции"] < 0:
            spent = abs(tx["Сумма операции"])
            rounded = ((spent // limit) + 1) * limit
            total_saved += rounded - spent
    return round(total_saved, 2)