import logging
import os
import re
from collections import Counter
from json import JSONDecodeError, load
import pandas as pd
from pathlib import Path

# Создаем папку logs, если еще не существует
os.makedirs("logs", exist_ok=True)

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/app.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def read_file_json(path_file: str) -> list:
    """
    Принимает путь к json-файлу в качестве аргумента.
    Возвращает список словарей с данными о финансовых транзакциях или, если
    файл пустой, содержит не-список или не найден, возвращается пустой список.
    """
    try:
        logger.info("Открытие файла")
        with open(path_file, encoding="utf-8") as file_with_operations:
            try:
                logger.info("Чтение файла")
                list_info_transactions: list = load(file_with_operations)

                if not isinstance(list_info_transactions, list):
                    logger.error("Неправильный формат файла")
                    return []

                return list_info_transactions

            except JSONDecodeError:
                logger.error("Ошибка чтения файла JSON")
                return []

    except FileNotFoundError:
        logger.error("Файл не найден")
        return []

def process_bank_search(data: list[dict], search_data: str) -> list[dict]:
    """Ищет операции в описании которых есть заданная строка для поиска"""
    result = []
    for operation in data:
        if re.search(search_data, operation["description"], flags=re.IGNORECASE):
            result.append(operation)
    logger.info(f"Найдено операций по поиску '{search_data}': {len(result)}")
    return result

def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает кол-во операций по заданным категориям"""
    filter_list = []
    for operations in data:
        if operations["description"] in categories:
            filter_list.append(f'{operations["description"]}')
    counts = dict(Counter(filter_list))
    logger.info(f"Подсчет операций по категориям завершен. Результат: {counts}")
    return counts

if __name__ == "__main__":
    # Пример вызова функций (можете убрать или оставить по необходимости)
    pass

import re
from collections import Counter

def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет в списке операций те, у которых описание содержит заданную строку.
    Использует регулярные выражения для поиска.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = [transaction for transaction in data if pattern.search(transaction.get('description', ''))]
    return result

def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций по категориям.
    Возвращает словарь {категория: количество}.
    """
    counts = Counter()
    for transaction in data:
        description = transaction.get('description', '')
        for category in categories:
            pattern = re.compile(re.escape(category), re.IGNORECASE)
            if pattern.search(description):
                counts[category] += 1
                break  # если категория найдена, переходим к следующей операции
    return dict(counts)
def load_transactions(file_path: str) -> pd.DataFrame:
    """Загружает транзакции из Excel."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")
    df = pd.read_excel(file_path)
    return df