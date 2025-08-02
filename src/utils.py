import logging
import os
import re
from collections import Counter
from json import JSONDecodeError, load

log_path = os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log")

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_path, mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def read_file_json(path_file: str) -> list:
    """
    Принимает путь к json-файлу в качестве аргумента.
    Возвращает список словарей с данными о финансовых транзакциях или, если
    файл пустой, содержит не-список или не найден, возвращается пустой список.
    """

    try:
        logger.info("открытие файла")
        with open(path_file, encoding="utf-8") as file_with_operations:

            try:
                logger.info("чтение файла")
                list_info_transactions: list = load(file_with_operations)

                if type(list_info_transactions) is not list:
                    logger.error("неправильный формат файла")
                    return []

                return list_info_transactions

            except JSONDecodeError:
                logger.error("ошибка чтения файла")
                return []

    except FileNotFoundError:
        logger.error("файл не найден")
        return []


def process_bank_search(data: list[dict], search_data: str) -> list[dict]:
    """Ищет операции в описании которых есть заданная для поиска строка"""

    result = []

    for operation in data:
        if re.search(search_data, operation["description"], flags=re.IGNORECASE):
            result.append(operation)

    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчитывает кол-во операции по заданным категориям"""

    filter_list = []

    for operations in data:
        if operations["description"] in categories:
            filter_list.append(f'{operations["description"]}')

    return dict(Counter(filter_list))