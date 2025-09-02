from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создаём продукты
    p1 = Product("Телефон", "Смартфон с хорошей камерой", 10000, 5)
    p2 = Product("Ноутбук", "Игровой ноутбук", 50000, 2)

    # Создаём категорию
    electronics = Category("Электроника", "Гаджеты и техника", [p1])

    # Добавляем продукт через метод
    electronics.add_product(p2)

    # Выводим список товаров
    print(electronics.products)

    # Проверка геттера/сеттера цены
    print(p1.price)
    p1.price = -100  # Ошибка
    p1.price = 9000  # Успешно
    print(p1.price)