from src.product import Product
from src.category import Category

if __name__ == "__main__":
    # Создаём продукты
    p1 = Product("Телефон", "Смартфон с хорошей камерой", 10000, 5)
    p2 = Product("Ноутбук", "Игровой ноутбук", 50000, 2)

    # Создаём категорию
    electronics = Category("Электроника", "Гаджеты и техника", [p1, p2])

    # Выводим информацию
    print(f"Категория: {electronics.name} — {electronics.description}")
    print(f"Товары в категории: {[p.name for p in electronics.products]}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")