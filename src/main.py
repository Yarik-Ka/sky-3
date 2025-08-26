import sys
from utils import process_bank_search, process_bank_operations
from data_processing import load_json, load_csv, load_xlsx


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input()

        if choice == '1':
            print("Программа: Для обработки выбран JSON-файл.")
            data = load_json()
        elif choice == '2':
            print("Программа: Для обработки выбран CSV-файл.")
            data = load_csv()
        elif choice == '3':
            print("Программа: Для обработки выбран XLSX-файл.")
            data = load_xlsx()
        else:
            print("Некорректный выбор. Попробуйте снова.")
            continue

        # Запрос статуса операции
        valid_statuses = {'EXECUTED', 'CANCELED', 'PENDING'}
        while True:
            status_input = input(
                "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
            if status_input in valid_statuses:
                break
            else:
                print(f"Статус операции \"{status_input}\" недоступен.")

        filtered_data = [op for op in data if op.get('status', '').upper() == status_input]
        print(f"Операции отфильтрованы по статусу \"{status_input}\"")

        # Сортировка по дате
        sort_choice = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if sort_choice == 'да':
            order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
            reverse_sort = True if order in ['по убыванию', 'убывание'] else False
            filtered_data.sort(key=lambda x: x.get('date', ''), reverse=reverse_sort)

        # Фильтр по валюте (рубли)
        rub_filter = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if rub_filter == 'да':
            filtered_data = [op for op in filtered_data if 'руб' in op.get('amount', '')]

        # Фильтр по ключевому слову в описании
        keyword_filter = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").strip().lower()
        if keyword_filter == 'да':
            keyword = input("Введите слово для поиска:\n").strip()
            filtered_data = process_bank_search(filtered_data, keyword)

        # Вывод итоговых операций
        if not filtered_data:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print("\nРаспечатываю итоговый список транзакций...\n")
            total_count = len(filtered_data)
            print(f"Всего банковских операций в выборке: {total_count}\n")
            for op in filtered_data:
                date = op.get('date', '')
                description = op.get('description', '')
                amount = op.get('amount', '')
                print(f"{date} {description}\nСумма: {amount}\n")

        break  # завершение после одного цикла; убрать для многократных запусков


if __name__ == "__main__":
    main()