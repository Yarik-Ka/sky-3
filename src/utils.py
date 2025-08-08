import logging
import os
import re
from collections import Counter
from json import JSONDecodeError, load

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