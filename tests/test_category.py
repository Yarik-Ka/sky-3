import pytest
from src.product import Product
from src.category import Category

def test_str_category():
    p1 = Product("Телефон", "Смартфон", 10000, 5)
    p2 = Product("Ноутбук", "Игровой", 50000, 2)
    c = Category("Электроника", "Гаджеты", [p1, p2])
    assert str(c) == "Электроника, количество продуктов: 7 шт."