from src.product import Product
from src.category import Category

if __name__ == "__main__":
    p1 = Product("Телефон", "Смартфон", 10000, 5)
    p2 = Product("Ноутбук", "Игровой ноутбук", 50000, 2)

    electronics = Category("Электроника", "Гаджеты", [p1, p2])

    print(p1)  # Телефон, 10000 руб. Остаток: 5 шт.
    print(electronics)  # Электроника, количество продуктов: 7 шт.

    total_value = p1 + p2
    print(f"Общая стоимость: {total_value} руб.")