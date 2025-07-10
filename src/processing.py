import typing
from typing import List, Dict, Any

def filter_by_state(
    list_of_dict: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> typing.List[Dict[str, Any]]:
    """
    Фильтрует список словарей по ключу 'state'.
    Возвращает список или сообщение, если ничего не найдено.
    """
    filtered_list = [item for item in list_of_dict if item.get("state") == state]
    if not filtered_list:
        return "No values were found for this key"
    return filtered_list

def sort_by_date(
    list_of_dict: List[Dict[str, Any]],
    descending: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date'.
    """
    # Предполагается, что дата в виде строки или числа
    return sorted(list_of_dict, key=lambda x: x.get("date", ""), reverse=descending)

if __name__ == "__main__":
    import json

    data_input = input("Введите список словарей в формате JSON: ")
    try:
        list_of_dicts = json.loads(data_input)
    except json.JSONDecodeError:
        print("Ошибка парсинга JSON. Проверьте формат данных.")
        exit()

    result_filter = filter_by_state(list_of_dicts)
    print("Результат фильтрации:", result_filter)

    result_sort = sort_by_date(list_of_dicts)
    print("Отсортированный список:", result_sort)