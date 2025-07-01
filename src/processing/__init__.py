from typing import List, Dict, Optional

def filter_by_state(
    transactions: List[Dict],
    state: str = 'EXECUTED'
) -> List[Dict]:
    """
    Возвращает список транзакций, у которых ключ 'state' совпадает с переданным значением.

    :param transactions: список словарей с данными о транзакциях
    :param state: значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список транзакций
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]



def sort_by_date(
    transactions: List[Dict],
    reverse: bool = True
) -> List[Dict]:
    """
    Возвращает список транзакций, отсортированный по дате.

    :param transactions: список словарей с данными о транзакциях
    :param reverse: порядок сортировки; True — по убыванию, False — по возрастанию (по умолчанию)
    :return: отсортированный список транзакций
    """
    return sorted(transactions, key=lambda x: x.get('date', ''), reverse=reverse)