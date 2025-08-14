# main.py

import pandas as pd
from typing import TYPE_CHECKING

def read_transactions_csv(file_path: str) -> pd.DataFrame:
    """
    Читает транзакции из CSV файла.
    """
    return pd.read_csv(file_path)

def read_transactions_xlsx(file_path: str) -> pd.DataFrame:
    """
    Читает транзакции из XLSX файла.
    """
    return pd.read_excel(file_path)

# Ниже — пример использования функций (убедитесь, что файлы transactions.csv и transactions_excel.xlsx в той же папке)
if __name__ == "__main__":
    csv_file = "transactions.csv"
    xlsx_file = "transactions_excel.xlsx"

    # Чтение из CSV
    df_csv = read_transactions_csv(csv_file)
    print("Данные из CSV файла:")
    print(df_csv.head())

    # Чтение из XLSX
    df_xlsx = read_transactions_xlsx(xlsx_file)
    print("\nДанные из XLSX файла:")
    print(df_xlsx.head())