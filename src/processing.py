import typing
from typing import List, Dict, Any

def filter_by_state(
    list_of_dict: List[Dict[str, Any]],
    state: str = "EXECUTED"
) -> typing.List[Dict[str, Any]]:
    """
    Функция принимает список словарей, фильтрует их по ключу 'state' и возвращает список подходящих.
    Если подходящих элементов нет — возвращает сообщение.
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
    Функция сортирует список словарей по ключу 'date'.
    По умолчанию сортировка по убыванию (самые новые в начале).
    """
    # Предполагается, что дата в формате строки или числа; при необходимости можно доработать парсинг
    return sorted(list_of_dict, key=lambda x: x.get("date", ""), reverse=descending)

if __name__ == "__main__":
    # Ввод данных пользователем
    try:
        data_input = input("Enter the list of dictionaries (например, [{'date': '2023-10-01', 'state': 'EXECUTED'}, ...]): ")
        list_of_dicts = eval(data_input)
        # Вызов функций
        filtered_result = filter_by_state(list_of_dicts)
        print("Filtered result:", filtered_result)

        sorted_result = sort_by_date(list_of_dicts)
        print("Sorted result:", sorted_result)
    except Exception as e:
        print(f"Ошибка при вводе данных или выполнении: {e}")